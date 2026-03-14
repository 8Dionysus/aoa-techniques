from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


REQUIRED_FRONTMATTER_KEYS = (
    "id",
    "name",
    "domain",
    "status",
    "origin",
    "owners",
    "tags",
    "summary",
)

REQUIRED_SECTIONS = (
    "Intent",
    "When to use",
    "When not to use",
    "Inputs",
    "Outputs",
    "Core procedure",
    "Contracts",
    "Risks",
    "Validation",
    "Adaptation notes",
    "Public sanitization notes",
    "Example",
    "Checks",
    "Promotion history",
    "Future evolution",
)

REQUIRED_SUPPORT_DIRS = ("checks", "examples", "notes")

SECTION_STATUS = {
    "Canonical techniques": "canonical",
    "Promoted techniques": "promoted",
    "Deprecated techniques": "deprecated",
}

STATUS_SECTION = {value: key for key, value in SECTION_STATUS.items()}

SUPPORT_PATH_RE = re.compile(r"(?<!\w)(checks|examples|notes)/[A-Za-z0-9._/-]+\.md")
FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?", re.DOTALL)
SECTION_RE = re.compile(r"^## (.+)$", re.MULTILINE)


class ValidationError(RuntimeError):
    pass


@dataclass(frozen=True)
class TechniqueRecord:
    technique_dir: Path
    id: str
    name: str
    domain: str
    status: str
    summary: str


@dataclass(frozen=True)
class IndexRow:
    section: str
    id: str
    name: str
    domain: str
    status: str
    summary: str


def fail(message: str) -> None:
    raise ValidationError(message)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def split_frontmatter(technique_path: Path) -> tuple[str, str]:
    text = read_text(technique_path)
    match = FRONTMATTER_RE.match(text)
    if not match:
        fail(f"{technique_path}: missing YAML frontmatter block")
    return match.group(1), text[match.end() :]


def parse_frontmatter(frontmatter: str, technique_path: Path) -> dict[str, str]:
    keys: dict[str, str] = {}
    for line in frontmatter.splitlines():
        if not line.strip():
            continue
        if line.startswith((" ", "\t")):
            continue
        if ":" not in line:
            fail(f"{technique_path}: malformed frontmatter line: {line!r}")
        key, value = line.split(":", 1)
        keys[key.strip()] = value.strip()

    for key in REQUIRED_FRONTMATTER_KEYS:
        if key not in keys:
            fail(f"{technique_path}: missing frontmatter key '{key}'")

    for key in ("id", "name", "domain", "status", "summary"):
        if not keys[key]:
            fail(f"{technique_path}: frontmatter key '{key}' must not be empty")

    if keys["status"] not in STATUS_SECTION:
        allowed = ", ".join(sorted(STATUS_SECTION))
        fail(
            f"{technique_path}: unsupported status '{keys['status']}', expected one of: {allowed}"
        )

    return keys


def validate_sections(body: str, technique_path: Path) -> None:
    present_sections = {match.group(1).strip() for match in SECTION_RE.finditer(body)}
    for required_section in REQUIRED_SECTIONS:
        if required_section not in present_sections:
            fail(f"{technique_path}: missing required section '## {required_section}'")


def validate_support_dirs(technique_dir: Path) -> None:
    for support_dir_name in REQUIRED_SUPPORT_DIRS:
        support_dir = technique_dir / support_dir_name
        if not support_dir.is_dir():
            fail(f"{technique_dir}: missing support directory '{support_dir_name}/'")
        markdown_files = sorted(support_dir.rglob("*.md"))
        if not markdown_files:
            fail(f"{technique_dir}: support directory '{support_dir_name}/' is empty")


def validate_support_references(body: str, technique_dir: Path, technique_path: Path) -> None:
    referenced_paths = sorted(set(SUPPORT_PATH_RE.findall(body)))
    # The regex includes a capture group; rebuild the full match list from the body.
    full_paths = sorted(set(match.group(0) for match in SUPPORT_PATH_RE.finditer(body)))
    for relative_path in full_paths:
        target = technique_dir / relative_path
        if not target.is_file():
            fail(
                f"{technique_path}: referenced support path '{relative_path}' does not exist"
            )


def validate_technique_bundle(technique_dir: Path, expected_domain: str) -> TechniqueRecord:
    technique_path = technique_dir / "TECHNIQUE.md"
    if not technique_path.is_file():
        fail(f"{technique_dir}: missing TECHNIQUE.md")

    validate_support_dirs(technique_dir)

    frontmatter, body = split_frontmatter(technique_path)
    parsed = parse_frontmatter(frontmatter, technique_path)
    validate_sections(body, technique_path)
    validate_support_references(body, technique_dir, technique_path)

    if parsed["domain"] != expected_domain:
        fail(
            f"{technique_path}: frontmatter domain '{parsed['domain']}' does not match parent directory '{expected_domain}'"
        )

    return TechniqueRecord(
        technique_dir=technique_dir,
        id=parsed["id"],
        name=parsed["name"],
        domain=parsed["domain"],
        status=parsed["status"],
        summary=parsed["summary"],
    )


def collect_techniques(repo_root: Path) -> list[TechniqueRecord]:
    techniques_dir = repo_root / "techniques"
    if not techniques_dir.is_dir():
        fail(f"{repo_root}: missing techniques/ directory")

    records: list[TechniqueRecord] = []
    seen_ids: set[str] = set()

    for domain_dir in sorted(path for path in techniques_dir.iterdir() if path.is_dir()):
        for technique_dir in sorted(path for path in domain_dir.iterdir() if path.is_dir()):
            record = validate_technique_bundle(technique_dir, domain_dir.name)
            if record.id in seen_ids:
                fail(f"duplicate technique id '{record.id}' at {record.technique_dir}")
            seen_ids.add(record.id)
            records.append(record)

    if not records:
        fail(f"{repo_root}: no technique bundles found under techniques/")

    return records


def parse_index_rows(index_path: Path) -> dict[str, list[IndexRow]]:
    rows_by_id: dict[str, list[IndexRow]] = {}
    current_section = ""

    for line in read_text(index_path).splitlines():
        if line.startswith("## "):
            current_section = line[3:].strip()
            continue

        if current_section not in SECTION_STATUS or not line.startswith("|"):
            continue

        cells = [cell.strip() for cell in line.strip().split("|")[1:-1]]
        if not cells:
            continue
        if cells[0] == "id":
            continue
        if all(re.fullmatch(r"-+", cell) for cell in cells):
            continue
        if all(cell == "-" for cell in cells):
            continue

        if current_section == "Deprecated techniques":
            if len(cells) != 4:
                fail(f"{index_path}: malformed row in deprecated table: {line}")
            row_id, name, _replacement, _note = cells
            if row_id == "-":
                continue
            row = IndexRow(
                section=current_section,
                id=row_id,
                name=name,
                domain="",
                status="deprecated",
                summary="",
            )
        else:
            if len(cells) != 5:
                fail(f"{index_path}: malformed row in {current_section}: {line}")
            row_id, name, domain, status, summary = cells
            if row_id == "-":
                continue
            row = IndexRow(
                section=current_section,
                id=row_id,
                name=name,
                domain=domain,
                status=status,
                summary=summary,
            )

        rows_by_id.setdefault(row.id, []).append(row)

    return rows_by_id


def validate_index(repo_root: Path, records: list[TechniqueRecord]) -> None:
    index_path = repo_root / "TECHNIQUE_INDEX.md"
    if not index_path.is_file():
        fail(f"{repo_root}: missing TECHNIQUE_INDEX.md")

    rows_by_id = parse_index_rows(index_path)
    records_by_id = {record.id: record for record in records}

    for row_id in rows_by_id:
        if row_id not in records_by_id:
            fail(f"{index_path}: index contains unknown technique id '{row_id}'")

    for record in records:
        rows = rows_by_id.get(record.id)
        if not rows:
            fail(f"{index_path}: missing row for technique '{record.id}'")
        if len(rows) != 1:
            fail(f"{index_path}: technique '{record.id}' appears more than once in the index")

        row = rows[0]
        expected_section = STATUS_SECTION[record.status]
        if row.section != expected_section:
            fail(
                f"{index_path}: technique '{record.id}' is in '{row.section}' but should be in '{expected_section}'"
            )

        if row.name != record.name:
            fail(
                f"{index_path}: technique '{record.id}' name mismatch: index='{row.name}' technique='{record.name}'"
            )

        if record.status in {"canonical", "promoted"}:
            if row.domain != record.domain:
                fail(
                    f"{index_path}: technique '{record.id}' domain mismatch: index='{row.domain}' technique='{record.domain}'"
                )
            if row.status != record.status:
                fail(
                    f"{index_path}: technique '{record.id}' status mismatch: index='{row.status}' technique='{record.status}'"
                )
            if row.summary != record.summary:
                fail(
                    f"{index_path}: technique '{record.id}' summary mismatch between index and frontmatter"
                )
        else:
            if row.status != "deprecated":
                fail(f"{index_path}: technique '{record.id}' must appear in deprecated table")


def validate_repo(repo_root: Path) -> None:
    records = collect_techniques(repo_root)
    validate_index(repo_root, records)
    canonical_count = sum(1 for record in records if record.status == "canonical")
    promoted_count = sum(1 for record in records if record.status == "promoted")
    deprecated_count = sum(1 for record in records if record.status == "deprecated")

    print(
        f"[ok] validated {len(records)} technique bundles "
        f"({canonical_count} canonical, {promoted_count} promoted, {deprecated_count} deprecated)"
    )
    print("[ok] validated TECHNIQUE_INDEX.md structure and parity")


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    try:
        validate_repo(repo_root)
    except ValidationError as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
