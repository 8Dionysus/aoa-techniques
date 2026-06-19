from __future__ import annotations

from .common import *
from .source_contracts import *

def build_kag_export_payloads(
    repo_root: Path, records: list[TechniqueRecord]
) -> tuple[dict[str, Any], dict[str, Any]]:
    records_by_id = {record.id: record for record in records}
    record = records_by_id.get(KAG_EXPORT_TECHNIQUE_ID)
    if record is None:
        fail(f"{repo_root}: missing required KAG export technique '{KAG_EXPORT_TECHNIQUE_ID}'")

    section_headings = {section.heading for section in record.sections}
    expected_headings = {
        "Intent",
        "Inputs",
        "Outputs",
        "Contracts",
        "Risks",
        "Validation",
    }
    if not expected_headings.issubset(section_headings):
        fail(
            f"{record.technique_path}: missing required headings for KAG export "
            f"{sorted(expected_headings - section_headings)}"
        )

    raw_relations = record.frontmatter.get("relations")
    if not isinstance(raw_relations, list) or not raw_relations:
        fail(f"{record.technique_path}: KAG export technique must keep non-empty relations")
    direct_relations: list[dict[str, str]] = []
    for relation in raw_relations:
        if not isinstance(relation, dict):
            fail(f"{record.technique_path}: KAG export relation entries must be objects")
        relation_type = relation.get("type")
        target_id = relation.get("target")
        if not isinstance(relation_type, str) or not relation_type:
            fail(f"{record.technique_path}: KAG export relation type must be a non-empty string")
        if not isinstance(target_id, str) or not target_id:
            fail(f"{record.technique_path}: KAG export relation target must be a non-empty string")
        target_record = records_by_id.get(target_id)
        if target_record is None:
            fail(f"{record.technique_path}: KAG export relation target '{target_id}' is missing")
        direct_relations.append(
            {
                "relation_type": relation_type,
                "target_ref": f"aoa-techniques/{target_record.technique_path.relative_to(repo_root).as_posix()}",
            }
        )

    payload = {
        "owner_repo": "aoa-techniques",
        "kind": "technique",
        "object_id": record.id,
        "primary_question": KAG_EXPORT_PRIMARY_QUESTION,
        "summary_50": KAG_EXPORT_SUMMARY_50,
        "summary_200": KAG_EXPORT_SUMMARY_200,
        "source_inputs": [
            {
                "repo": "aoa-techniques",
                "source_class": "technique_bundle",
                "role": "primary",
            }
        ],
        "entry_surface": {
            "repo": "aoa-techniques",
            "path": "generated/technique_capsules.json",
            "match_key": "id",
            "match_value": record.id,
        },
        "section_handles": list(KAG_EXPORT_SECTION_HANDLES),
        "direct_relations": direct_relations,
        "provenance_note": KAG_EXPORT_PROVENANCE_NOTE,
        "non_identity_boundary": KAG_EXPORT_NON_IDENTITY_BOUNDARY,
        "artifact_identity": KAG_EXPORT_ARTIFACT_IDENTITY,
    }
    return payload, payload

def validate_kag_export(repo_root: Path, records: list[TechniqueRecord]) -> None:
    full_path = repo_root / "generated" / "kag_export.json"
    min_path = repo_root / "generated" / "kag_export.min.json"

    expected_full, expected_min = build_kag_export_payloads(repo_root, records)
    actual_full = read_json(full_path)
    actual_min = read_json(min_path)

    if actual_full != expected_full:
        fail(
            f"{full_path}: generated KAG export is out of date; "
            "run 'python scripts/build_kag_export.py'"
        )
    if actual_min != expected_min:
        fail(
            f"{min_path}: generated compact KAG export is out of date; "
            "run 'python scripts/build_kag_export.py'"
        )
    if actual_full != actual_min:
        fail(f"{min_path}: compact KAG export must stay identical to the bounded full export")
