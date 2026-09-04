from __future__ import annotations

import hashlib
import json
import os
import re
from pathlib import Path
from typing import Any


CONFIG_PATH = Path("config/agents_mesh.json")
INDEX_SCHEMA_VERSION = "aoa_techniques_agents_mesh_index_v1"
CONFIG_SCHEMA_VERSION = "aoa_techniques_agents_mesh_v1"
SOURCE_OF_TRUTH = "agents-md-mesh-v1"
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")

# Active route cards name a lane or owner; exact command batteries live in the
# validation manifest. Keep these patterns deliberately code-shaped so normal
# prose, paths, and DESIGN.AGENTS examples are not rejected.
EXECUTABLE_LINE_RE = re.compile(
    r"^\s*(?:\$\s*)?(?:python(?:3)?|pytest|git|gh|pip|uv|make|bash|sh|find|"
    r"cargo|npm|node|ruff|mypy|jq|rg|curl|docker|podman|\./)\s+"
)
INLINE_COMMAND_RE = re.compile(
    r"`(?:python(?:3)?|pytest|git|gh|pip|uv|make|bash|sh|find|cargo|npm|node|"
    r"ruff|mypy|jq|rg|curl|docker|podman|\./)\s+"
)
README_ROUTE_EXCEPTION = "Read `README.md` only when the selected task needs its human map"
LANE_TOKENS = ("source-fast", "generated", "mechanics/part-local", "release", "advisory", "nightly")


def active_card_route_issues(text: str) -> list[str]:
    """Return narrow D-0076 shape issues for an active AGENTS card."""
    issues: list[str] = []
    lines = text.splitlines()
    in_fence = False
    read_start: int | None = None
    read_end = len(lines)
    for index, line in enumerate(lines):
        if line.strip().startswith("```"):
            in_fence = not in_fence
            issues.append(f"line {index + 1}: executable fences are not allowed")
        if EXECUTABLE_LINE_RE.match(line):
            issues.append(f"line {index + 1}: runnable command line is not allowed")
        if INLINE_COMMAND_RE.search(line):
            issues.append(f"line {index + 1}: inline runnable command is not allowed")
        if in_fence:
            continue
        if line.strip() == "## Read before editing":
            read_start = index + 1
        elif read_start is not None and line.startswith("## "):
            read_end = index
            read_start = None
    if in_fence:
        issues.append("unterminated executable fence")

    read_lines = lines[(read_start or 0):read_end] if read_start is not None else []
    if not read_lines:
        # Cards without a read section are reported by the canonical heading
        # check; avoid duplicating that error here.
        start = next((i for i, line in enumerate(lines) if line.strip() == "## Read before editing"), None)
        if start is not None:
            end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
            read_lines = lines[start + 1:end]
    for offset, line in enumerate(read_lines, 1):
        context = " ".join(read_lines[offset - 1 : offset + 2])
        if "README" in line and README_ROUTE_EXCEPTION not in context and "only when" not in context:
            issues.append(f"Read before editing line {offset}: unconditional README inventory")

    for index, line in enumerate(lines):
        if line.rstrip().endswith(":"):
            next_index = index + 1
            while next_index < len(lines) and not lines[next_index].strip():
                next_index += 1
            if next_index == len(lines) or lines[next_index].startswith("#"):
                issues.append(f"line {index + 1}: dangling colon lead-in")
        if re.match(r"^\s*[-*]\s+", line) and line.rstrip().endswith(":"):
            next_index = index + 1
            while next_index < len(lines) and not lines[next_index].strip():
                next_index += 1
            if next_index < len(lines) and re.match(r"^\s*[-*]\s+", lines[next_index]):
                issues.append(f"line {index + 1}: stacked same-level list lead-ins")

    validation = section_body(text, "## Validation")
    if not validation:
        issues.append("Validation section is empty")
    elif "VALIDATION.md" not in validation or "config/validation_lanes.json" not in validation:
        issues.append("Validation section must route to VALIDATION.md and config/validation_lanes.json")
    elif not any(token in validation for token in LANE_TOKENS):
        issues.append("Validation section must name an applicable lane")
    return issues


class AgentsMeshError(RuntimeError):
    """Raised when the AGENTS mesh contract is invalid."""


def repo_root_from_script(script_path: Path) -> Path:
    return script_path.resolve().parents[1]


def posix_rel(path: Path, repo_root: Path) -> str:
    return path.resolve().relative_to(repo_root.resolve()).as_posix()


def load_mesh_config(repo_root: Path) -> dict[str, Any]:
    path = repo_root / CONFIG_PATH
    if not path.is_file():
        raise AgentsMeshError(f"{CONFIG_PATH.as_posix()}: file is missing")
    try:
        config = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise AgentsMeshError(f"{CONFIG_PATH.as_posix()}: invalid JSON: {exc}") from exc
    if config.get("schema_version") != CONFIG_SCHEMA_VERSION:
        raise AgentsMeshError(
            f"{CONFIG_PATH.as_posix()}: schema_version must be {CONFIG_SCHEMA_VERSION!r}"
        )
    return config


def ignored_directory_names(config: dict[str, Any]) -> set[str]:
    configured = config.get("ignored_directory_names", ())
    if not isinstance(configured, list):
        raise AgentsMeshError("ignored_directory_names must be a list")
    return {str(name) for name in configured}


def top_level_exemptions(config: dict[str, Any]) -> set[str]:
    configured = config.get("top_level_exemptions", ())
    if not isinstance(configured, list):
        raise AgentsMeshError("top_level_exemptions must be a list")
    return {str(name) for name in configured}


def canonical_card_paths(config: dict[str, Any]) -> tuple[str, ...]:
    cards = config.get("canonical_cards", ())
    if not isinstance(cards, list):
        raise AgentsMeshError("canonical_cards must be a list")
    return tuple(str(path) for path in cards)


def required_headings(config: dict[str, Any]) -> tuple[str, ...]:
    headings = config.get("canonical_required_headings", ())
    if not isinstance(headings, list):
        raise AgentsMeshError("canonical_required_headings must be a list")
    return tuple(str(heading) for heading in headings)


def iter_agents_cards(repo_root: Path, config: dict[str, Any]) -> tuple[Path, ...]:
    ignored = ignored_directory_names(config)
    found: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(repo_root):
        dirnames[:] = sorted(
            dirname
            for dirname in dirnames
            if dirname not in ignored and not (Path(dirpath) / dirname).is_symlink()
        )
        if "AGENTS.md" in filenames:
            found.append(Path(dirpath) / "AGENTS.md")
    return tuple(sorted(found, key=lambda path: posix_rel(path, repo_root)))


def markdown_headings(text: str) -> tuple[str, ...]:
    headings: list[str] = []
    for line in text.splitlines():
        match = HEADING_RE.match(line)
        if match:
            headings.append(f"{match.group(1)} {match.group(2)}")
    return tuple(headings)


def section_body(text: str, heading: str) -> str:
    lines = text.splitlines()
    start: int | None = None
    heading_level = heading.split(" ", 1)[0]
    for index, line in enumerate(lines):
        if line.strip() == heading:
            start = index + 1
            break
    if start is None:
        return ""
    end = len(lines)
    for index in range(start, len(lines)):
        if lines[index].startswith("#") and lines[index].split(" ", 1)[0] <= heading_level:
            end = index
            break
    return "\n".join(lines[start:end]).strip()


def missing_required_headings(text: str, required: tuple[str, ...]) -> tuple[str, ...]:
    present = set(markdown_headings(text))
    return tuple(heading for heading in required if heading not in present)


def headings_in_order(text: str, required: tuple[str, ...]) -> bool:
    headings = list(markdown_headings(text))
    cursor = -1
    for required_heading in required:
        try:
            next_index = headings.index(required_heading, cursor + 1)
        except ValueError:
            return False
        cursor = next_index
    return True


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def card_summary(path: Path, repo_root: Path, config: dict[str, Any]) -> dict[str, Any]:
    rel_path = posix_rel(path, repo_root)
    text = path.read_text(encoding="utf-8")
    canonical = set(canonical_card_paths(config))
    required = required_headings(config)
    headings = markdown_headings(text)
    first_line = text.splitlines()[0] if text.splitlines() else ""
    shape_status = "canonical" if rel_path in canonical else "migration"
    return {
        "path": rel_path,
        "shape_status": shape_status,
        "sha256": sha256_text(text),
        "line_count": len(text.splitlines()),
        "first_line_ok": first_line == "# AGENTS.md",
        "heading_count": len(headings),
        "headings": list(headings),
        "missing_canonical_headings": list(missing_required_headings(text, required)),
    }


def build_agents_mesh_index(repo_root: Path) -> dict[str, Any]:
    config = load_mesh_config(repo_root)
    cards = [card_summary(path, repo_root, config) for path in iter_agents_cards(repo_root, config)]
    canonical_count = sum(1 for card in cards if card["shape_status"] == "canonical")
    migration_count = sum(1 for card in cards if card["shape_status"] == "migration")
    return {
        "schema_version": INDEX_SCHEMA_VERSION,
        "source_of_truth": SOURCE_OF_TRUTH,
        "config_ref": CONFIG_PATH.as_posix(),
        "authority_ref": config["authority_ref"],
        "design_ref": config["design_ref"],
        "system_design_ref": config["system_design_ref"],
        "root_agents_ref": config["root_agents_ref"],
        "generated_ref": config["generated_ref"],
        "canonical_required_headings": list(required_headings(config)),
        "counts": {
            "cards": len(cards),
            "canonical": canonical_count,
            "migration": migration_count,
        },
        "cards": cards,
    }


def compact_json(payload: dict[str, Any]) -> str:
    return json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"


def pretty_json(payload: dict[str, Any]) -> str:
    return json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
