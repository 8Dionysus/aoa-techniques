from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


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
REQUIRED_STAGE1_FILES = (
    "docs/CANONICAL_RUBRIC.md",
    "docs/DOMAIN_MAP.md",
    "schemas/technique.schema.json",
    "schemas/evidence-note.schema.json",
    "schemas/relation.schema.json",
    "schemas/index-entry.schema.json",
    "scripts/build_catalog.py",
    "generated/technique_catalog.json",
    "generated/technique_catalog.min.json",
)

SECTION_STATUS = {
    "Canonical techniques": "canonical",
    "Promoted techniques": "promoted",
    "Deprecated techniques": "deprecated",
}

STATUS_SECTION = {value: key for key, value in SECTION_STATUS.items()}
DOMAIN_VALUES = {"agent-workflows", "docs", "evaluation"}
SUPPORT_PATH_RE = re.compile(r"(?<!\w)(?:checks|examples|notes)/[A-Za-z0-9._/-]+\.md")
FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?", re.DOTALL)
SECTION_RE = re.compile(r"^## (.+)$", re.MULTILINE)
EVIDENCE_KIND_BY_NAME = {
    "origin-evidence.md": "origin_evidence",
    "second-context-adaptation.md": "second_context",
    "canonical-readiness.md": "canonical_readiness",
    "external-origin.md": "external_origin",
    "external-import-review.md": "external_review",
}


class ValidationError(RuntimeError):
    pass


@dataclass(frozen=True)
class TechniqueRecord:
    technique_dir: Path
    technique_path: Path
    id: str
    name: str
    domain: str
    status: str
    summary: str
    frontmatter: dict[str, Any]
    body: str


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


def read_json(path: Path) -> Any:
    return json.loads(read_text(path))


def split_frontmatter(technique_path: Path) -> tuple[str, str]:
    text = read_text(technique_path)
    match = FRONTMATTER_RE.match(text)
    if not match:
        fail(f"{technique_path}: missing YAML frontmatter block")
    return match.group(1), text[match.end() :]


def skip_blank_lines(lines: list[str], index: int) -> int:
    while index < len(lines) and not lines[index].strip():
        index += 1
    return index


def indentation(line: str, technique_path: Path) -> int:
    if "\t" in line[: len(line) - len(line.lstrip(" \t"))]:
        fail(f"{technique_path}: tabs are not supported in frontmatter indentation")
    return len(line) - len(line.lstrip(" "))


def parse_scalar(raw: str) -> Any:
    value = raw.strip()
    if value == "[]":
        return []
    if value == "{}":
        return {}
    if value == "true":
        return True
    if value == "false":
        return False
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_block(
    lines: list[str], index: int, expected_indent: int, technique_path: Path
) -> tuple[Any, int]:
    index = skip_blank_lines(lines, index)
    if index >= len(lines):
        fail(f"{technique_path}: expected nested frontmatter block at indent {expected_indent}")

    current_indent = indentation(lines[index], technique_path)
    if current_indent != expected_indent:
        fail(
            f"{technique_path}: expected frontmatter indent {expected_indent}, found {current_indent}"
        )

    if lines[index][expected_indent:].startswith("- "):
        return parse_list(lines, index, expected_indent, technique_path)
    return parse_mapping(lines, index, expected_indent, technique_path)


def parse_mapping(
    lines: list[str], index: int, expected_indent: int, technique_path: Path
) -> tuple[dict[str, Any], int]:
    mapping: dict[str, Any] = {}

    while True:
        index = skip_blank_lines(lines, index)
        if index >= len(lines):
            break

        line = lines[index]
        current_indent = indentation(line, technique_path)
        if current_indent < expected_indent:
            break
        if current_indent != expected_indent:
            fail(
                f"{technique_path}: unexpected frontmatter indent {current_indent}, expected {expected_indent}"
            )

        text = line[expected_indent:]
        if text.startswith("- "):
            fail(f"{technique_path}: unexpected list item at indent {expected_indent}")
        if ":" not in text:
            fail(f"{technique_path}: malformed frontmatter line: {line!r}")

        key, rest = text.split(":", 1)
        key = key.strip()
        rest = rest.strip()
        if not key:
            fail(f"{technique_path}: empty frontmatter key in line: {line!r}")
        if key in mapping:
            fail(f"{technique_path}: duplicate frontmatter key '{key}'")

        index += 1
        if rest:
            mapping[key] = parse_scalar(rest)
            continue

        value, index = parse_block(lines, index, expected_indent + 2, technique_path)
        mapping[key] = value

    return mapping, index


def parse_list(
    lines: list[str], index: int, expected_indent: int, technique_path: Path
) -> tuple[list[Any], int]:
    items: list[Any] = []

    while True:
        index = skip_blank_lines(lines, index)
        if index >= len(lines):
            break

        line = lines[index]
        current_indent = indentation(line, technique_path)
        if current_indent < expected_indent:
            break
        if current_indent != expected_indent:
            fail(
                f"{technique_path}: unexpected frontmatter indent {current_indent}, expected {expected_indent}"
            )

        text = line[expected_indent:]
        if not text.startswith("- "):
            break

        content = text[2:].strip()
        index += 1

        if not content:
            value, index = parse_block(lines, index, expected_indent + 2, technique_path)
            items.append(value)
            continue

        if ":" in content:
            key, rest = content.split(":", 1)
            key = key.strip()
            rest = rest.strip()
            if not key:
                fail(f"{technique_path}: malformed inline mapping list item: {line!r}")

            item: dict[str, Any] = {}
            if rest:
                item[key] = parse_scalar(rest)
            else:
                value, index = parse_block(lines, index, expected_indent + 4, technique_path)
                item[key] = value

            while True:
                index = skip_blank_lines(lines, index)
                if index >= len(lines):
                    break

                nested_line = lines[index]
                nested_indent = indentation(nested_line, technique_path)
                if nested_indent < expected_indent + 2:
                    break
                if nested_indent != expected_indent + 2:
                    fail(
                        f"{technique_path}: unexpected list-mapping indent {nested_indent}, expected {expected_indent + 2}"
                    )

                nested_text = nested_line[expected_indent + 2 :]
                if nested_text.startswith("- "):
                    fail(
                        f"{technique_path}: nested list items are not supported inside mapping list items"
                    )
                if ":" not in nested_text:
                    fail(f"{technique_path}: malformed frontmatter line: {nested_line!r}")

                nested_key, nested_rest = nested_text.split(":", 1)
                nested_key = nested_key.strip()
                nested_rest = nested_rest.strip()
                if not nested_key:
                    fail(f"{technique_path}: empty nested frontmatter key")
                if nested_key in item:
                    fail(f"{technique_path}: duplicate nested frontmatter key '{nested_key}'")

                index += 1
                if nested_rest:
                    item[nested_key] = parse_scalar(nested_rest)
                else:
                    nested_value, index = parse_block(
                        lines, index, expected_indent + 4, technique_path
                    )
                    item[nested_key] = nested_value

            items.append(item)
            continue

        items.append(parse_scalar(content))

    return items, index


def parse_frontmatter(frontmatter: str, technique_path: Path) -> dict[str, Any]:
    lines = frontmatter.splitlines()
    parsed, index = parse_block(lines, 0, 0, technique_path)
    index = skip_blank_lines(lines, index)
    if index != len(lines):
        fail(f"{technique_path}: could not parse frontmatter completely")
    if not isinstance(parsed, dict):
        fail(f"{technique_path}: frontmatter must parse into an object")
    return parsed


def load_schema_store(repo_root: Path) -> dict[str, Any]:
    schemas_dir = repo_root / "schemas"
    if not schemas_dir.is_dir():
        fail(f"{repo_root}: missing schemas/ directory")

    store: dict[str, Any] = {}
    for schema_path in sorted(schemas_dir.glob("*.schema.json")):
        schema = read_json(schema_path)
        store[schema_path.name] = schema
        schema_id = schema.get("$id")
        if isinstance(schema_id, str) and schema_id:
            store[schema_id] = schema
    return store


def resolve_schema_ref(ref: str, schema_store: dict[str, Any]) -> Any:
    if ref not in schema_store:
        fail(f"schema reference '{ref}' is not available in schema store")
    return schema_store[ref]


def ensure_type(instance: Any, expected_type: str, instance_path: str) -> None:
    type_ok = {
        "object": isinstance(instance, dict),
        "array": isinstance(instance, list),
        "string": isinstance(instance, str),
        "integer": isinstance(instance, int) and not isinstance(instance, bool),
        "boolean": isinstance(instance, bool),
    }.get(expected_type)

    if type_ok is None:
        fail(f"{instance_path}: unsupported schema type '{expected_type}'")
    if not type_ok:
        fail(f"{instance_path}: expected {expected_type}, found {type(instance).__name__}")


def validate_schema_instance(
    instance: Any, schema: dict[str, Any], instance_path: str, schema_store: dict[str, Any]
) -> None:
    if "$ref" in schema:
        validate_schema_instance(
            instance, resolve_schema_ref(schema["$ref"], schema_store), instance_path, schema_store
        )
        return

    if "type" in schema:
        ensure_type(instance, schema["type"], instance_path)

    if "enum" in schema and instance not in schema["enum"]:
        allowed = ", ".join(repr(value) for value in schema["enum"])
        fail(f"{instance_path}: value {instance!r} is not in enum [{allowed}]")

    if isinstance(instance, str):
        if "minLength" in schema and len(instance) < schema["minLength"]:
            fail(f"{instance_path}: string is shorter than minLength {schema['minLength']}")
        if "pattern" in schema and not re.fullmatch(schema["pattern"], instance):
            fail(f"{instance_path}: value {instance!r} does not match pattern {schema['pattern']}")

    if isinstance(instance, int) and not isinstance(instance, bool):
        if "minimum" in schema and instance < schema["minimum"]:
            fail(f"{instance_path}: value {instance} is below minimum {schema['minimum']}")
        if "maximum" in schema and instance > schema["maximum"]:
            fail(f"{instance_path}: value {instance} is above maximum {schema['maximum']}")

    if isinstance(instance, list):
        if "minItems" in schema and len(instance) < schema["minItems"]:
            fail(f"{instance_path}: array has fewer than {schema['minItems']} items")
        if "maxItems" in schema and len(instance) > schema["maxItems"]:
            fail(f"{instance_path}: array has more than {schema['maxItems']} items")
        if "items" in schema:
            for item_index, item in enumerate(instance):
                validate_schema_instance(
                    item, schema["items"], f"{instance_path}[{item_index}]", schema_store
                )

    if isinstance(instance, dict):
        properties = schema.get("properties", {})
        required = schema.get("required", [])
        for required_key in required:
            if required_key not in instance:
                fail(f"{instance_path}: missing required property '{required_key}'")

        if schema.get("additionalProperties") is False:
            unexpected = sorted(set(instance) - set(properties))
            if unexpected:
                fail(
                    f"{instance_path}: unexpected properties {', '.join(repr(key) for key in unexpected)}"
                )

        for key, value in instance.items():
            if key in properties:
                validate_schema_instance(
                    value, properties[key], f"{instance_path}.{key}", schema_store
                )


def validate_frontmatter_schema(
    frontmatter: dict[str, Any], technique_path: Path, schema_store: dict[str, Any]
) -> None:
    schema = resolve_schema_ref("technique.schema.json", schema_store)
    validate_schema_instance(frontmatter, schema, str(technique_path), schema_store)


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
    for relative_path in sorted(set(match.group(0) for match in SUPPORT_PATH_RE.finditer(body))):
        target = technique_dir / relative_path
        if not target.is_file():
            fail(f"{technique_path}: referenced support path '{relative_path}' does not exist")


def validate_stage1_files(repo_root: Path) -> None:
    for relative_path in REQUIRED_STAGE1_FILES:
        target = repo_root / relative_path
        if not target.exists():
            fail(f"{repo_root}: missing required Stage 1 file '{relative_path}'")


def validate_technique_bundle(
    technique_dir: Path, expected_domain: str, schema_store: dict[str, Any]
) -> TechniqueRecord:
    technique_path = technique_dir / "TECHNIQUE.md"
    if not technique_path.is_file():
        fail(f"{technique_dir}: missing TECHNIQUE.md")

    validate_support_dirs(technique_dir)

    frontmatter_text, body = split_frontmatter(technique_path)
    frontmatter = parse_frontmatter(frontmatter_text, technique_path)
    validate_frontmatter_schema(frontmatter, technique_path, schema_store)
    validate_sections(body, technique_path)
    validate_support_references(body, technique_dir, technique_path)

    if frontmatter["domain"] != expected_domain:
        fail(
            f"{technique_path}: frontmatter domain '{frontmatter['domain']}' does not match parent directory '{expected_domain}'"
        )

    return TechniqueRecord(
        technique_dir=technique_dir,
        technique_path=technique_path,
        id=frontmatter["id"],
        name=frontmatter["name"],
        domain=frontmatter["domain"],
        status=frontmatter["status"],
        summary=frontmatter["summary"],
        frontmatter=frontmatter,
        body=body,
    )


def collect_techniques(repo_root: Path, schema_store: dict[str, Any]) -> list[TechniqueRecord]:
    techniques_dir = repo_root / "techniques"
    if not techniques_dir.is_dir():
        fail(f"{repo_root}: missing techniques/ directory")

    records: list[TechniqueRecord] = []
    seen_ids: set[str] = set()

    for domain_dir in sorted(path for path in techniques_dir.iterdir() if path.is_dir()):
        if domain_dir.name not in DOMAIN_VALUES:
            fail(f"{domain_dir}: unsupported domain directory '{domain_dir.name}'")

        for technique_dir in sorted(path for path in domain_dir.iterdir() if path.is_dir()):
            record = validate_technique_bundle(technique_dir, domain_dir.name, schema_store)
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


def expected_evidence_kind(relative_path: str) -> str:
    return EVIDENCE_KIND_BY_NAME.get(Path(relative_path).name, "support_note")


def validate_evidence(records: list[TechniqueRecord]) -> None:
    for record in records:
        notes_dir = record.technique_dir / "notes"
        actual_note_paths = sorted(
            path.relative_to(record.technique_dir).as_posix()
            for path in notes_dir.rglob("*.md")
        )
        evidence_items = record.frontmatter["evidence"]
        evidence_paths = [item["path"] for item in evidence_items]

        if sorted(evidence_paths) != actual_note_paths:
            fail(
                f"{record.technique_path}: evidence paths do not match notes/ contents: "
                f"frontmatter={sorted(evidence_paths)} notes={actual_note_paths}"
            )

        if len(set(evidence_paths)) != len(evidence_paths):
            fail(f"{record.technique_path}: evidence paths must be unique")

        for item in evidence_items:
            expected_kind = expected_evidence_kind(item["path"])
            if item["kind"] != expected_kind:
                fail(
                    f"{record.technique_path}: evidence '{item['path']}' must use kind '{expected_kind}', "
                    f"found '{item['kind']}'"
                )


def validate_relations(records: list[TechniqueRecord]) -> None:
    known_ids = {record.id for record in records}
    for record in records:
        seen_pairs: set[tuple[str, str]] = set()
        for relation in record.frontmatter["relations"]:
            pair = (relation["type"], relation["target"])
            if relation["target"] == record.id:
                fail(f"{record.technique_path}: relation '{relation['type']}' cannot target itself")
            if relation["target"] not in known_ids:
                fail(
                    f"{record.technique_path}: relation target '{relation['target']}' does not exist"
                )
            if pair in seen_pairs:
                fail(
                    f"{record.technique_path}: duplicate relation '{relation['type']}' -> '{relation['target']}'"
                )
            seen_pairs.add(pair)


def full_catalog_entry(repo_root: Path, record: TechniqueRecord) -> dict[str, Any]:
    frontmatter = record.frontmatter
    return {
        "id": frontmatter["id"],
        "name": frontmatter["name"],
        "domain": frontmatter["domain"],
        "status": frontmatter["status"],
        "summary": frontmatter["summary"],
        "technique_path": record.technique_path.relative_to(repo_root).as_posix(),
        "origin": frontmatter["origin"],
        "owners": frontmatter["owners"],
        "tags": frontmatter["tags"],
        "maturity_score": frontmatter["maturity_score"],
        "rigor_level": frontmatter["rigor_level"],
        "reversibility": frontmatter["reversibility"],
        "review_required": frontmatter["review_required"],
        "validation_strength": frontmatter["validation_strength"],
        "public_safety_reviewed_at": frontmatter["public_safety_reviewed_at"],
        "export_ready": frontmatter["export_ready"],
        "relations": frontmatter["relations"],
        "evidence": frontmatter["evidence"],
    }


def min_catalog_entry(repo_root: Path, record: TechniqueRecord) -> dict[str, Any]:
    frontmatter = record.frontmatter
    return {
        "id": frontmatter["id"],
        "name": frontmatter["name"],
        "domain": frontmatter["domain"],
        "status": frontmatter["status"],
        "summary": frontmatter["summary"],
        "maturity_score": frontmatter["maturity_score"],
        "rigor_level": frontmatter["rigor_level"],
        "reversibility": frontmatter["reversibility"],
        "review_required": frontmatter["review_required"],
        "validation_strength": frontmatter["validation_strength"],
        "export_ready": frontmatter["export_ready"],
        "technique_path": record.technique_path.relative_to(repo_root).as_posix(),
    }


def build_catalog_payloads(
    repo_root: Path, records: list[TechniqueRecord]
) -> tuple[dict[str, Any], dict[str, Any]]:
    sorted_records = sorted(records, key=lambda record: record.id)
    full_catalog = {
        "catalog_version": 1,
        "source_of_truth": "markdown-frontmatter-v2",
        "techniques": [full_catalog_entry(repo_root, record) for record in sorted_records],
    }
    min_catalog = {
        "catalog_version": 1,
        "source_of_truth": "markdown-frontmatter-v2",
        "techniques": [min_catalog_entry(repo_root, record) for record in sorted_records],
    }
    return full_catalog, min_catalog


def write_json_file(path: Path, payload: Any, compact: bool) -> None:
    if compact:
        encoded = json.dumps(payload, ensure_ascii=True, separators=(",", ":"))
    else:
        encoded = json.dumps(payload, ensure_ascii=True, indent=2)
    path.write_text(encoded + "\n", encoding="utf-8")


def validate_catalogs(repo_root: Path, records: list[TechniqueRecord], schema_store: dict[str, Any]) -> None:
    full_path = repo_root / "generated" / "technique_catalog.json"
    min_path = repo_root / "generated" / "technique_catalog.min.json"

    expected_full, expected_min = build_catalog_payloads(repo_root, records)
    actual_full = read_json(full_path)
    actual_min = read_json(min_path)

    if actual_full != expected_full:
        fail(
            f"{full_path}: generated catalog is out of date; run 'python scripts/build_catalog.py'"
        )
    if actual_min != expected_min:
        fail(
            f"{min_path}: generated min catalog is out of date; run 'python scripts/build_catalog.py'"
        )

    min_schema = resolve_schema_ref("index-entry.schema.json", schema_store)
    for index, entry in enumerate(actual_min["techniques"]):
        validate_schema_instance(entry, min_schema, f"{min_path}[{index}]", schema_store)

    projected_min = [
        {
            key: entry[key]
            for key in (
                "id",
                "name",
                "domain",
                "status",
                "summary",
                "maturity_score",
                "rigor_level",
                "reversibility",
                "review_required",
                "validation_strength",
                "export_ready",
                "technique_path",
            )
        }
        for entry in actual_full["techniques"]
    ]
    if projected_min != actual_min["techniques"]:
        fail(f"{min_path}: min catalog must stay a projection of the full catalog")


def validate_repo(repo_root: Path) -> None:
    validate_stage1_files(repo_root)
    schema_store = load_schema_store(repo_root)
    records = collect_techniques(repo_root, schema_store)
    validate_index(repo_root, records)
    validate_evidence(records)
    validate_relations(records)
    validate_catalogs(repo_root, records, schema_store)

    canonical_count = sum(1 for record in records if record.status == "canonical")
    promoted_count = sum(1 for record in records if record.status == "promoted")
    deprecated_count = sum(1 for record in records if record.status == "deprecated")

    print(
        f"[ok] validated {len(records)} technique bundles "
        f"({canonical_count} canonical, {promoted_count} promoted, {deprecated_count} deprecated)"
    )
    print("[ok] validated TECHNIQUE_INDEX.md structure and parity")
    print("[ok] validated frontmatter-v2 schema, evidence coverage, and relations")
    print("[ok] validated generated catalog parity")


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
