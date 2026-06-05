"""Decision-record metadata and generated lookup index contracts."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

import yaml


DECISIONS_DIR = Path("docs/decisions")
INDEXES_DIR = DECISIONS_DIR / "indexes"
INDEX_CONTRACT_PATH = INDEXES_DIR / "index_contract.yaml"
INDEX_CONTRACT_SCHEMA = "aoa_techniques_decision_index_contract_v1"
DECISION_ID_PREFIX = "AOA-TECH-D"
PATH_MODE = "full_canonical_id_filename"
SOURCE_RECORDS = "docs/decisions/AOA-TECH-D-*.md"
GENERATED_BY = "scripts/generate_decision_indexes.py"
REQUIRED_METADATA = (
    "Original date",
    "Surface classes",
    "Technique axes",
    "Mechanic parents",
    "Guard families",
    "Posture",
)
GENERATED_INDEX_PATHS = (
    INDEXES_DIR / "README.md",
    INDEXES_DIR / "by-number.md",
    INDEXES_DIR / "by-date.md",
    INDEXES_DIR / "by-surface.md",
    INDEXES_DIR / "by-technique-axis.md",
    INDEXES_DIR / "by-mechanic.md",
    INDEXES_DIR / "by-guard.md",
)
DECISION_ID_RE = re.compile(r"^- Decision ID: (AOA-TECH-D-(\d{4}))$", re.MULTILINE)
DATE_VALUE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
FULL_ID_FILENAME_RE = re.compile(r"^(AOA-TECH-D-(\d{4}))-.+\.md$")

SURFACE_CLASS_ORDER = (
    "root/topology",
    "docs route",
    "decision record",
    "technique contract",
    "technique topology",
    "technique tree",
    "technique template",
    "technique intelligence",
    "mechanic package",
    "mechanic part",
    "mechanic evidence",
    "agent route",
    "generated/readout",
    "legacy/provenance",
    "release/GitHub",
    "public status",
    "validation guard",
    "quest/lane",
)
TECHNIQUE_AXIS_ORDER = (
    "atom",
    "topology",
    "tree",
    "kind",
    "template",
    "selection",
    "intelligence",
    "source-lift",
    "review",
    "promotion",
    "standalone portability",
    "mechanic bridge",
    "agent mesh",
    "github landing",
    "decision index",
)
MECHANIC_PARENT_ORDER = (
    "agon",
    "antifragility",
    "audit",
    "boundary-bridge",
    "checkpoint",
    "distillation",
    "experience",
    "growth-cycle",
    "method-growth",
    "questbook",
    "recurrence",
    "release-support",
    "rpg",
    "cross-mechanic",
)
GUARD_FAMILY_ORDER = (
    "decision index/read-model",
    "docs route",
    "root surface",
    "technique atom",
    "technique topology",
    "technique tree",
    "kind remap",
    "template validation",
    "mechanic topology",
    "part-local artifact",
    "generated/read-model",
    "AGENTS/mesh",
    "release/tooling",
    "public-safety",
    "sibling-owner boundary",
    "evidence intake",
    "legacy/provenance",
    "questbook",
)


@dataclass(frozen=True)
class DecisionRecord:
    decision_id: str
    number: int
    title: str
    path: Path
    date: str
    surface_classes: tuple[str, ...]
    technique_axes: tuple[str, ...]
    mechanic_parents: tuple[str, ...]
    guard_families: tuple[str, ...]
    posture: str

    @property
    def repo_path(self) -> str:
        return self.path.as_posix()

    @property
    def index_link(self) -> str:
        return f"../{self.path.name}"


def split_metadata_value(value: str) -> tuple[str, ...]:
    value = value.strip()
    if not value or value == "none":
        return ()
    return tuple(item.strip() for item in value.split(",") if item.strip())


def parse_title(text: str, *, path: Path) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].removeprefix("Decision Note: ").strip()
    raise ValueError(f"{path.as_posix()} is missing a level-one title")


def parse_decision_id(text: str, *, path: Path) -> tuple[str, int]:
    match = DECISION_ID_RE.search(text)
    if not match:
        raise ValueError(
            f"{path.as_posix()} is missing '- Decision ID: AOA-TECH-D-####'"
        )
    return match.group(1), int(match.group(2))


def parse_index_metadata(text: str, *, path: Path) -> dict[str, str]:
    marker = "\n## Index Metadata\n"
    if marker not in text:
        raise ValueError(f"{path.as_posix()} is missing ## Index Metadata")
    section = text.split(marker, 1)[1]
    next_heading = section.find("\n## ")
    if next_heading != -1:
        section = section[:next_heading]

    metadata: dict[str, str] = {}
    for raw_line in section.splitlines():
        line = raw_line.strip()
        if not line.startswith("- ") or ":" not in line:
            continue
        key, value = line[2:].split(":", 1)
        metadata[key.strip().lower()] = value.strip()

    required = {
        "decision id",
        "original date",
        "surface classes",
        "technique axes",
        "mechanic parents",
        "guard families",
        "posture",
    }
    missing = sorted(required - set(metadata))
    if missing:
        raise ValueError(
            f"{path.as_posix()} index metadata is missing: {', '.join(missing)}"
        )
    return metadata


def parse_original_date(metadata: dict[str, str], *, path: Path) -> str:
    value = metadata["original date"].strip()
    if not DATE_VALUE_RE.match(value):
        raise ValueError(f"{path.as_posix()} original date must use YYYY-MM-DD")
    return value


def load_decision_record(path: Path, *, repo_root: Path) -> DecisionRecord:
    text = path.read_text(encoding="utf-8")
    relative_path = path.relative_to(repo_root)
    decision_id, number = parse_decision_id(text, path=relative_path)
    title = parse_title(text, path=relative_path)
    metadata = parse_index_metadata(text, path=relative_path)
    if metadata["decision id"] != decision_id:
        raise ValueError(
            f"{relative_path.as_posix()} Decision ID metadata must match the note ID"
        )
    return DecisionRecord(
        decision_id=decision_id,
        number=number,
        title=title,
        path=relative_path,
        date=parse_original_date(metadata, path=relative_path),
        surface_classes=split_metadata_value(metadata["surface classes"]),
        technique_axes=split_metadata_value(metadata["technique axes"]),
        mechanic_parents=split_metadata_value(metadata["mechanic parents"]),
        guard_families=split_metadata_value(metadata["guard families"]),
        posture=metadata["posture"].strip(),
    )


def collect_decision_records(repo_root: Path) -> tuple[list[DecisionRecord], list[tuple[str, str]]]:
    records: list[DecisionRecord] = []
    issues: list[tuple[str, str]] = []
    decisions_root = repo_root / DECISIONS_DIR
    if not decisions_root.is_dir():
        return records, [(DECISIONS_DIR.as_posix(), "decision directory is missing")]

    for path in sorted(
        item
        for item in decisions_root.glob("*.md")
        if item.name not in {"AGENTS.md", "README.md", "TEMPLATE.md"}
    ):
        try:
            record = load_decision_record(path, repo_root=repo_root)
        except ValueError as exc:
            issues.append((path.relative_to(repo_root).as_posix(), str(exc)))
            continue

        filename_match = FULL_ID_FILENAME_RE.match(record.path.name)
        if not filename_match:
            issues.append(
                (
                    record.repo_path,
                    "decision path must use the full canonical ID filename format",
                )
            )
        elif filename_match.group(1) != record.decision_id:
            issues.append(
                (
                    record.repo_path,
                    "decision path canonical ID must match the note Decision ID",
                )
            )
        elif int(filename_match.group(2)) != record.number:
            issues.append(
                (
                    record.repo_path,
                    "decision path number must match the note Decision ID number",
                )
            )
        records.append(record)

    numbers = [record.number for record in records]
    if len(numbers) != len(set(numbers)):
        issues.append((DECISIONS_DIR.as_posix(), "decision numbers must be unique"))
    if numbers != sorted(numbers):
        issues.append((DECISIONS_DIR.as_posix(), "decision records must sort by number"))
    if numbers and numbers != list(range(1, max(numbers) + 1)):
        issues.append((DECISIONS_DIR.as_posix(), "decision numbers must be contiguous"))

    ids = [record.decision_id for record in records]
    if len(ids) != len(set(ids)):
        issues.append((DECISIONS_DIR.as_posix(), "decision IDs must be unique"))
    return records, issues


def ordered_values(values: Iterable[str], preferred_order: Sequence[str]) -> list[str]:
    seen = set(values)
    ordered = [value for value in preferred_order if value in seen]
    ordered.extend(sorted(seen - set(ordered)))
    return ordered


def display_title(record: DecisionRecord) -> str:
    if record.title.startswith(record.decision_id):
        return record.title
    return f"{record.decision_id} {record.title}"


def bullet_line(record: DecisionRecord) -> str:
    return (
        f"- [{display_title(record)}]({record.index_link}) "
        f"(`{record.repo_path}`)"
    )


def render_generated_notice() -> str:
    return (
        "<!-- Generated by scripts/generate_decision_indexes.py; "
        "do not edit by hand. -->\n\n"
    )


def render_indexes_readme() -> str:
    return (
        "# Decision Lookup Indexes\n\n"
        + render_generated_notice()
        + "These files are generated read models from decision-note `Index Metadata`.\n"
        + "Decision notes own rationale; these indexes only make lookup cheaper for agents.\n\n"
        + "## Indexes\n\n"
        + "- [By number](by-number.md)\n"
        + "- [By date](by-date.md)\n"
        + "- [By surface class](by-surface.md)\n"
        + "- [By technique axis](by-technique-axis.md)\n"
        + "- [By mechanic parent](by-mechanic.md)\n"
        + "- [By validation or guard family](by-guard.md)\n"
    )


def render_by_number(records: Sequence[DecisionRecord]) -> str:
    lines = [
        "# Decisions By Number",
        "",
        render_generated_notice().rstrip(),
        "",
        "| Decision ID | Date | Decision | Path | Surface classes | Technique axes | Mechanic parents | Guard families | Posture |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for record in records:
        lines.append(
            "| {decision_id} | {date} | [{title}]({link}) | `{path}` | {surfaces} | {axes} | {parents} | {guards} | {posture} |".format(
                decision_id=record.decision_id,
                date=record.date,
                title=display_title(record),
                link=record.index_link,
                path=record.repo_path,
                surfaces=", ".join(record.surface_classes) or "none",
                axes=", ".join(record.technique_axes) or "none",
                parents=", ".join(record.mechanic_parents) or "none",
                guards=", ".join(record.guard_families) or "none",
                posture=record.posture,
            )
        )
    return "\n".join(lines) + "\n"


def render_by_date(records: Sequence[DecisionRecord]) -> str:
    lines = ["# Decisions By Date", "", render_generated_notice().rstrip(), ""]
    for date in sorted({record.date for record in records}):
        lines.extend([f"## {date}", ""])
        for record in records:
            if record.date == date:
                lines.append(bullet_line(record))
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_grouped_index(
    *,
    title: str,
    records: Sequence[DecisionRecord],
    attribute: str,
    preferred_order: Sequence[str],
) -> str:
    values: list[str] = []
    for record in records:
        values.extend(getattr(record, attribute))
    lines = ["# " + title, "", render_generated_notice().rstrip(), ""]
    for value in ordered_values(values, preferred_order):
        lines.extend([f"## {value}", ""])
        for record in records:
            if value in getattr(record, attribute):
                lines.append(bullet_line(record))
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_index_files(records: Sequence[DecisionRecord]) -> dict[Path, str]:
    return {
        INDEXES_DIR / "README.md": render_indexes_readme(),
        INDEXES_DIR / "by-number.md": render_by_number(records),
        INDEXES_DIR / "by-date.md": render_by_date(records),
        INDEXES_DIR / "by-surface.md": render_grouped_index(
            title="Decisions By Surface Class",
            records=records,
            attribute="surface_classes",
            preferred_order=SURFACE_CLASS_ORDER,
        ),
        INDEXES_DIR / "by-technique-axis.md": render_grouped_index(
            title="Decisions By Technique Axis",
            records=records,
            attribute="technique_axes",
            preferred_order=TECHNIQUE_AXIS_ORDER,
        ),
        INDEXES_DIR / "by-mechanic.md": render_grouped_index(
            title="Decisions By Mechanic Parent",
            records=records,
            attribute="mechanic_parents",
            preferred_order=MECHANIC_PARENT_ORDER,
        ),
        INDEXES_DIR / "by-guard.md": render_grouped_index(
            title="Decisions By Validation Or Guard Family",
            records=records,
            attribute="guard_families",
            preferred_order=GUARD_FAMILY_ORDER,
        ),
    }


def load_index_contract(repo_root: Path) -> tuple[dict[str, object] | None, list[tuple[str, str]]]:
    path = repo_root / INDEX_CONTRACT_PATH
    if not path.is_file():
        return None, [(INDEX_CONTRACT_PATH.as_posix(), "decision index contract is missing")]
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        return None, [(INDEX_CONTRACT_PATH.as_posix(), "decision index contract must be a mapping")]
    return payload, []


def expected_contract_fields() -> dict[str, dict[str, object]]:
    return {
        "decision_id": {"required": True, "pattern": "AOA-TECH-D-####"},
        "original_date": {"required": True, "pattern": "YYYY-MM-DD"},
        "surface_classes": {"required": True},
        "technique_axes": {"required": True},
        "mechanic_parents": {"required": True},
        "guard_families": {"required": True},
        "posture": {"required": True},
    }


def validate_index_contract_payload(contract: dict[str, object]) -> list[tuple[str, str]]:
    issues: list[tuple[str, str]] = []
    expected_indexes = [path.as_posix() for path in GENERATED_INDEX_PATHS]
    expected_path_policy = {
        "path_mode": PATH_MODE,
        "current_path_authority": "full canonical-ID decision files are active source files",
        "canonical_handle": "Decision ID and matching filename prefix",
        "historical_path_policy": "previous date-prefixed paths live in git and PR history only",
        "compatibility_policy": "no repository lookup layer is generated for previous date-prefixed paths or short numbered paths",
    }
    if contract.get("schema_version") != INDEX_CONTRACT_SCHEMA:
        issues.append(
            (
                INDEX_CONTRACT_PATH.as_posix(),
                f"schema_version must be {INDEX_CONTRACT_SCHEMA}",
            )
        )
    if contract.get("authority") != "docs/decisions/AGENTS.md":
        issues.append((INDEX_CONTRACT_PATH.as_posix(), "authority must be docs/decisions/AGENTS.md"))
    if contract.get("source_records") != SOURCE_RECORDS:
        issues.append((INDEX_CONTRACT_PATH.as_posix(), f"source_records must be {SOURCE_RECORDS}"))
    if contract.get("generated_by") != GENERATED_BY:
        issues.append((INDEX_CONTRACT_PATH.as_posix(), f"generated_by must be {GENERATED_BY}"))
    if contract.get("generated_indexes") != expected_indexes:
        issues.append(
            (
                INDEX_CONTRACT_PATH.as_posix(),
                "generated_indexes must match the decision index read-model set",
            )
        )
    if contract.get("fields") != expected_contract_fields():
        issues.append(
            (
                INDEX_CONTRACT_PATH.as_posix(),
                "fields must match the parsed decision metadata fields",
            )
        )
    if contract.get("path_policy") != expected_path_policy:
        issues.append(
            (
                INDEX_CONTRACT_PATH.as_posix(),
                "path_policy must match the full canonical-ID filename policy",
            )
        )
    return issues


def validate_decision_lane_surfaces(repo_root: Path) -> list[tuple[str, str]]:
    decisions_root = repo_root / DECISIONS_DIR
    if not decisions_root.is_dir():
        return [(DECISIONS_DIR.as_posix(), "decision directory is missing")]

    allowed_paths = {
        (DECISIONS_DIR / "AGENTS.md").as_posix(),
        (DECISIONS_DIR / "README.md").as_posix(),
        (DECISIONS_DIR / "TEMPLATE.md").as_posix(),
        INDEX_CONTRACT_PATH.as_posix(),
        *(path.as_posix() for path in GENERATED_INDEX_PATHS),
    }
    issues: list[tuple[str, str]] = []
    for path in sorted(decisions_root.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(repo_root)
        relative_text = relative.as_posix()
        if relative_text in allowed_paths:
            continue
        decision_relative = path.relative_to(decisions_root)
        if len(decision_relative.parts) == 1 and FULL_ID_FILENAME_RE.match(path.name):
            continue
        issues.append(
            (
                relative_text,
                "unmodeled decision-lane surface; add it to the local decision surface contract or move it outside docs/decisions",
            )
        )
    return issues


def validate_decision_index_surfaces(repo_root: Path) -> list[tuple[str, str]]:
    records, issues = collect_decision_records(repo_root)
    issues.extend(validate_decision_lane_surfaces(repo_root))
    contract, contract_issues = load_index_contract(repo_root)
    issues.extend(contract_issues)
    if contract is not None:
        issues.extend(validate_index_contract_payload(contract))

    if issues:
        return issues

    rendered = render_index_files(records)
    for relative_path, expected_text in rendered.items():
        path = repo_root / relative_path
        if not path.is_file():
            issues.append((relative_path.as_posix(), "generated decision index is missing"))
            continue
        if path.read_text(encoding="utf-8") != expected_text:
            issues.append(
                (
                    relative_path.as_posix(),
                    "generated decision index is stale; run python scripts/generate_decision_indexes.py",
                )
            )
    return issues
