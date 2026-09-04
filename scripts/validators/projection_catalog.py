from __future__ import annotations

from .common import *
from .source_contracts import *

NESTED_READER_DOCS_PREFIX = "../../"
NESTED_READER_ROOT_PREFIX = "../../../"
SOURCE_LIFT_READER_GUIDE_PREFIX = "../../source-lift/"
SOURCE_LIFT_READER_ROOT_PREFIX = NESTED_READER_ROOT_PREFIX
REVIEW_GUIDE_PREFIX = "../../review/"
SELECTION_GUIDE_PREFIX = "../../selection/"
KIND_READER_DOCS_PREFIX = NESTED_READER_DOCS_PREFIX
KIND_READER_ROOT_PREFIX = NESTED_READER_ROOT_PREFIX
RUNTIME_READER_DOCS_PREFIX = NESTED_READER_DOCS_PREFIX
RUNTIME_READER_ROOT_PREFIX = NESTED_READER_ROOT_PREFIX
SELECTION_READER_DOCS_PREFIX = NESTED_READER_DOCS_PREFIX
SELECTION_READER_ROOT_PREFIX = NESTED_READER_ROOT_PREFIX
REVIEW_READER_ROOT_PREFIX = NESTED_READER_ROOT_PREFIX
REPO_DOC_READER_DOCS_PREFIX = NESTED_READER_DOCS_PREFIX
REPO_DOC_READER_GUIDE_PREFIX = "../../source-lift/"
REPO_DOC_READER_ROOT_PREFIX = NESTED_READER_ROOT_PREFIX

def full_catalog_entry(repo_root: Path, record: TechniqueRecord) -> dict[str, Any]:
    frontmatter = record.frontmatter
    return {
        "id": frontmatter["id"],
        "name": frontmatter["name"],
        "domain": frontmatter["domain"],
        "kind": frontmatter["kind"],
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
        "kind": frontmatter["kind"],
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

def full_capsule_entry(repo_root: Path, record: TechniqueRecord) -> dict[str, Any]:
    sections_by_heading = capsule_sections_by_heading(record)
    capsule_entry = {
        "id": record.id,
        "name": record.name,
        "summary": record.summary,
        "one_line_intent": summarize_capsule_intent(sections_by_heading["Intent"].markdown),
        "use_when_short": summarize_capsule_use_when(sections_by_heading["When to use"].markdown),
        "do_not_use_short": summarize_capsule_do_not_use(
            sections_by_heading["When not to use"].markdown
        ),
        "inputs_short": summarize_capsule_inputs(sections_by_heading["Inputs"].markdown),
        "outputs_short": summarize_capsule_outputs(sections_by_heading["Outputs"].markdown),
        "core_contract_short": summarize_capsule_contract(sections_by_heading["Contracts"].markdown),
        "main_risk_short": summarize_capsule_risk(sections_by_heading["Risks"].markdown),
        "validation_short": summarize_capsule_validation(sections_by_heading["Validation"].markdown),
        "technique_path": record.technique_path.relative_to(repo_root).as_posix(),
    }

    for key in (
        "one_line_intent",
        "use_when_short",
        "do_not_use_short",
        "inputs_short",
        "outputs_short",
        "core_contract_short",
        "main_risk_short",
        "validation_short",
    ):
        if not capsule_entry[key]:
            fail(f"{record.technique_path}: capsule field '{key}' must not be empty")

    return capsule_entry

def full_section_manifest_entry(repo_root: Path, record: TechniqueRecord) -> dict[str, Any]:
    sections_by_heading = {section.heading: section for section in record.sections}
    return {
        "id": record.id,
        "technique_path": record.technique_path.relative_to(repo_root).as_posix(),
        "sections": [
            {
                "heading": heading,
                "order": order,
                "markdown": sections_by_heading[heading].markdown,
            }
            for order, heading in enumerate(SECTION_LIFT_HEADINGS, start=1)
        ],
    }

def full_section_surface_entry(repo_root: Path, record: TechniqueRecord) -> dict[str, Any]:
    sections_by_heading = {section.heading: section for section in record.sections}
    return {
        "id": record.id,
        "name": record.name,
        "technique_path": record.technique_path.relative_to(repo_root).as_posix(),
        "sections": [
            {
                "key": SECTION_KEY_BY_HEADING[heading],
                "heading": heading,
                "content_markdown": sections_by_heading[heading].markdown,
            }
            for heading in REQUIRED_SECTIONS
        ],
    }

def project_min_section_manifest(full_manifest: dict[str, Any]) -> dict[str, Any]:
    return {
        "manifest_version": full_manifest["manifest_version"],
        "source_of_truth": full_manifest["source_of_truth"],
        "section_scope": full_manifest["section_scope"],
        "techniques": [
            {
                "id": technique["id"],
                "technique_path": technique["technique_path"],
                "sections": [
                    {
                        "heading": section["heading"],
                        "order": section["order"],
                    }
                    for section in technique["sections"]
                ],
            }
            for technique in full_manifest["techniques"]
        ],
    }

def full_checklist_manifest_entry(repo_root: Path, record: TechniqueRecord) -> dict[str, Any]:
    return {
        "id": record.id,
        "technique_path": record.technique_path.relative_to(repo_root).as_posix(),
        "checklists": [
            {
                "check_path": checklist.check_path,
                "title": checklist.title,
                "intro_markdown": checklist.intro_markdown,
                "items": [
                    {
                        "order": order,
                        "text": item.text,
                    }
                    for order, item in enumerate(checklist.items, start=1)
                ],
            }
            for checklist in record.checklists
        ],
    }

def project_min_checklist_manifest(full_manifest: dict[str, Any]) -> dict[str, Any]:
    return {
        "manifest_version": full_manifest["manifest_version"],
        "source_of_truth": full_manifest["source_of_truth"],
        "techniques": [
            {
                "id": technique["id"],
                "technique_path": technique["technique_path"],
                "checklists": [
                    {
                        "check_path": checklist["check_path"],
                        "title": checklist["title"],
                        "item_count": len(checklist["items"]),
                        "items": [
                            {
                                "order": item["order"],
                            }
                            for item in checklist["items"]
                        ],
                    }
                    for checklist in technique["checklists"]
                ],
            }
            for technique in full_manifest["techniques"]
        ],
    }

def full_example_manifest_entry(repo_root: Path, record: TechniqueRecord) -> dict[str, Any]:
    return {
        "id": record.id,
        "technique_path": record.technique_path.relative_to(repo_root).as_posix(),
        "examples": [
            {
                "example_path": example.example_path,
                "title": example.title,
                "body_markdown": example.body_markdown,
            }
            for example in record.examples
        ],
    }

def project_min_example_manifest(full_manifest: dict[str, Any]) -> dict[str, Any]:
    return {
        "manifest_version": full_manifest["manifest_version"],
        "source_of_truth": full_manifest["source_of_truth"],
        "techniques": [
            {
                "id": technique["id"],
                "technique_path": technique["technique_path"],
                "examples": [
                    {
                        "example_path": example["example_path"],
                        "title": example["title"],
                        "body_present": example["body_markdown"] != "",
                    }
                    for example in technique["examples"]
                ],
            }
            for technique in full_manifest["techniques"]
        ],
    }

def typed_note_scopes_payload() -> dict[str, Any]:
    return {
        kind: {
            "title": TYPED_NOTE_TITLES[kind],
            "section_scope": list(TYPED_NOTE_SECTION_SCOPES[kind]),
        }
        for kind in TYPED_NOTE_KIND_ORDER
    }

def full_note_section_payload(section: EvidenceNoteSection, order: int) -> dict[str, Any]:
    payload = {
        "heading": section.heading,
        "order": order,
        "payload_type": section.payload_type,
    }
    if section.payload_type == NOTE_PAYLOAD_FIELDS:
        payload["fields"] = [
            {
                "order": field_order,
                "key": field.key,
                "value_markdown": field.value_markdown,
            }
            for field_order, field in enumerate(section.fields, start=1)
        ]
    elif section.payload_type == NOTE_PAYLOAD_ITEMS:
        payload["items"] = [
            {
                "order": item_order,
                "text": item.text,
            }
            for item_order, item in enumerate(section.items, start=1)
        ]
    else:
        payload["markdown"] = section.markdown
    return payload

def full_evidence_note_manifest_entry(repo_root: Path, record: TechniqueRecord) -> dict[str, Any]:
    return {
        "id": record.id,
        "technique_path": record.technique_path.relative_to(repo_root).as_posix(),
        "notes": [
            {
                "note_path": note.note_path,
                "kind": note.kind,
                "title": note.title,
                "note_shape": note.note_shape,
                **(
                    {
                        "intro_markdown": note.intro_markdown,
                        "sections": [
                            full_note_section_payload(section, order)
                            for order, section in enumerate(note.sections, start=1)
                        ],
                    }
                    if note.note_shape == NOTE_SHAPE_TYPED
                    else {"body_markdown": note.body_markdown}
                ),
            }
            for note in record.notes
        ],
    }

def project_min_evidence_note_manifest(full_manifest: dict[str, Any]) -> dict[str, Any]:
    return {
        "manifest_version": full_manifest["manifest_version"],
        "source_of_truth": full_manifest["source_of_truth"],
        "typed_note_scopes": full_manifest["typed_note_scopes"],
        "techniques": [
            {
                "id": technique["id"],
                "technique_path": technique["technique_path"],
                "notes": [
                    {
                        "note_path": note["note_path"],
                        "kind": note["kind"],
                        "title": note["title"],
                        "note_shape": note["note_shape"],
                        **(
                            {
                                "intro_present": note["intro_markdown"] != "",
                                "sections": [
                                    {
                                        "heading": section["heading"],
                                        "order": section["order"],
                                        "payload_type": section["payload_type"],
                                        **(
                                            {
                                                "fields": [
                                                    {
                                                        "order": field["order"],
                                                        "key": field["key"],
                                                    }
                                                    for field in section["fields"]
                                                ]
                                            }
                                            if section["payload_type"] == NOTE_PAYLOAD_FIELDS
                                            else {}
                                        ),
                                        **(
                                            {
                                                "items": [
                                                    {
                                                        "order": item["order"],
                                                    }
                                                    for item in section["items"]
                                                ]
                                            }
                                            if section["payload_type"] == NOTE_PAYLOAD_ITEMS
                                            else {}
                                        ),
                                        **(
                                            {"markdown_present": section["markdown"] != ""}
                                            if section["payload_type"] == NOTE_PAYLOAD_MARKDOWN
                                            else {}
                                        ),
                                    }
                                    for section in note["sections"]
                                ],
                            }
                            if note["note_shape"] == NOTE_SHAPE_TYPED
                            else {"body_present": note["body_markdown"] != ""}
                        ),
                    }
                    for note in technique["notes"]
                ],
            }
            for technique in full_manifest["techniques"]
        ],
    }

def full_review_template_section_payload(section: ReviewTemplateSection, order: int) -> dict[str, Any]:
    payload = {
        "heading": section.heading,
        "order": order,
        "payload_type": section.payload_type,
    }
    if section.payload_type == REVIEW_TEMPLATE_PAYLOAD_FIELDS:
        payload["fields"] = [
            {
                "order": field_order,
                "key": field.key,
                "value_markdown": field.value_markdown,
            }
            for field_order, field in enumerate(section.fields, start=1)
        ]
    elif section.payload_type == REVIEW_TEMPLATE_PAYLOAD_ITEMS:
        payload["items"] = [
            {
                "order": item_order,
                "text": item.text,
            }
            for item_order, item in enumerate(section.items, start=1)
        ]
    elif section.payload_type == REVIEW_TEMPLATE_PAYLOAD_CHECKBOXES:
        payload["checkboxes"] = [
            {
                "order": checkbox_order,
                "text": checkbox.text,
                "checked": checkbox.checked,
            }
            for checkbox_order, checkbox in enumerate(section.checkboxes, start=1)
        ]
    else:
        payload["markdown"] = section.markdown
    return payload

def full_github_review_template_manifest_entry(template: GitHubReviewTemplate) -> dict[str, Any]:
    payload = {
        "template_id": template.template_id,
        "template_path": template.template_path,
        "template_type": template.template_type,
        "sections": [
            full_review_template_section_payload(section, order)
            for order, section in enumerate(template.sections, start=1)
        ],
    }
    if template.metadata is not None:
        payload["metadata"] = {key: template.metadata[key] for key in REVIEW_TEMPLATE_METADATA_KEYS}
    return payload

def project_min_github_review_template_manifest(full_manifest: dict[str, Any]) -> dict[str, Any]:
    return {
        "manifest_version": full_manifest["manifest_version"],
        "source_of_truth": full_manifest["source_of_truth"],
        "template_scopes": full_manifest["template_scopes"],
        "templates": [
            {
                "template_id": template["template_id"],
                "template_path": template["template_path"],
                "template_type": template["template_type"],
                **({"metadata": template["metadata"]} if "metadata" in template else {}),
                "sections": [
                    {
                        "heading": section["heading"],
                        "order": section["order"],
                        "payload_type": section["payload_type"],
                        **(
                            {
                                "fields": [
                                    {
                                        "order": field["order"],
                                        "key": field["key"],
                                    }
                                    for field in section["fields"]
                                ]
                            }
                            if section["payload_type"] == REVIEW_TEMPLATE_PAYLOAD_FIELDS
                            else {}
                        ),
                        **(
                            {
                                "items": [
                                    {
                                        "order": item["order"],
                                    }
                                    for item in section["items"]
                                ]
                            }
                            if section["payload_type"] == REVIEW_TEMPLATE_PAYLOAD_ITEMS
                            else {}
                        ),
                        **(
                            {
                                "checkboxes": [
                                    {
                                        "order": checkbox["order"],
                                        "checked": checkbox["checked"],
                                    }
                                    for checkbox in section["checkboxes"]
                                ]
                            }
                            if section["payload_type"] == REVIEW_TEMPLATE_PAYLOAD_CHECKBOXES
                            else {}
                        ),
                        **(
                            {"markdown_present": section["markdown"] != ""}
                            if section["payload_type"] == REVIEW_TEMPLATE_PAYLOAD_MARKDOWN
                            else {}
                        ),
                    }
                    for section in template["sections"]
                ],
            }
            for template in full_manifest["templates"]
        ],
    }

def semantic_review_scope_payload() -> dict[str, Any]:
    return {
        "map": {
            "first_section_suffix": "Map",
            "table_header": ["technique", "current role"],
        },
        "seams": {
            "section_heading": "Seam Review",
            "subsection_level": "###",
            "question_prefix": SEMANTIC_REVIEW_QUESTION_PREFIX,
            "outcome_marker": SEMANTIC_REVIEW_OUTCOME_MARKER,
        },
        "findings": {
            "section_heading": "Findings",
            "overall_outcome_prefix": SEMANTIC_REVIEW_OVERALL_OUTCOME_PREFIX,
        },
        "next_step": {
            "section_heading": "Next Step",
        },
    }

def shadow_review_scope_payload() -> dict[str, Any]:
    return {
        "map": {
            "first_section_suffix": "Map",
            "table_header": ["technique", "current role", "current shadow seam"],
        },
        "seams": {
            "section_heading": "Seam Review",
            "subsection_level": "###",
            "question_prefix": SHADOW_REVIEW_QUESTION_PREFIX,
            "outcome_marker": SHADOW_REVIEW_OUTCOME_MARKER,
        },
        "findings": {
            "section_heading": "Findings",
            "overall_outcome_prefix": SHADOW_REVIEW_OVERALL_OUTCOME_PREFIX,
        },
        "next_step": {
            "section_heading": "Next Step",
        },
    }

def repo_doc_surface_groups_payload() -> list[dict[str, str]]:
    return [
        {
            "group": spec["group"],
            "heading": spec["heading"],
            "note": spec["note"],
        }
        for spec in REPO_DOC_SURFACE_GROUP_SPECS
    ]

def full_semantic_review_manifest_entry(review: SemanticReview) -> dict[str, Any]:
    return {
        "review_id": review.review_id,
        "review_path": review.review_path,
        "title": review.title,
        "intro_markdown": review.intro_markdown,
        "map_heading": review.map_heading,
        "map_entries": [
            {
                "order": order,
                "technique_id": entry.technique_id,
                "technique_path": entry.technique_path,
                "current_role": entry.current_role,
            }
            for order, entry in enumerate(review.map_entries, start=1)
        ],
        "seams": [
            {
                "heading": seam.heading,
                "order": order,
                "question": seam.question,
                "analysis_markdown": seam.analysis_markdown,
                "outcome": seam.outcome,
            }
            for order, seam in enumerate(review.seams, start=1)
        ],
        "context_notes": [
            {
                "heading": note.heading,
                "order": order,
                "markdown": note.markdown,
                "outcome": note.outcome,
            }
            for order, note in enumerate(review.context_notes, start=1)
        ],
        "findings": [
            {
                "order": order,
                "text": finding.text,
            }
            for order, finding in enumerate(review.findings, start=1)
        ],
        "overall_outcome": review.overall_outcome,
        "next_step_markdown": review.next_step_markdown,
    }

def full_shadow_review_manifest_entry(review: ShadowReview) -> dict[str, Any]:
    return {
        "review_id": review.review_id,
        "review_path": review.review_path,
        "title": review.title,
        "intro_markdown": review.intro_markdown,
        "map_heading": review.map_heading,
        "map_entries": [
            {
                "order": order,
                "technique_id": entry.technique_id,
                "technique_path": entry.technique_path,
                "current_role": entry.current_role,
                "current_shadow_seam": entry.current_shadow_seam,
            }
            for order, entry in enumerate(review.map_entries, start=1)
        ],
        "seams": [
            {
                "heading": seam.heading,
                "order": order,
                "question": seam.question,
                "analysis_markdown": seam.analysis_markdown,
                "outcome": seam.outcome,
            }
            for order, seam in enumerate(review.seams, start=1)
        ],
        "findings": [
            {
                "order": order,
                "text": finding.text,
            }
            for order, finding in enumerate(review.findings, start=1)
        ],
        "overall_outcome": review.overall_outcome,
        "next_step_markdown": review.next_step_markdown,
    }

def project_min_semantic_review_manifest(full_manifest: dict[str, Any]) -> dict[str, Any]:
    return {
        "manifest_version": full_manifest["manifest_version"],
        "source_of_truth": full_manifest["source_of_truth"],
        "review_scope": full_manifest["review_scope"],
        "reviews": [
            {
                "review_id": review["review_id"],
                "review_path": review["review_path"],
                "title": review["title"],
                "intro_present": review["intro_markdown"] != "",
                "map_heading": review["map_heading"],
                "map_entries": [
                    {
                        "order": entry["order"],
                        "technique_id": entry["technique_id"],
                        "technique_path": entry["technique_path"],
                    }
                    for entry in review["map_entries"]
                ],
                "seams": [
                    {
                        "heading": seam["heading"],
                        "order": seam["order"],
                        "question_present": seam["question"] != "",
                        "outcome": seam["outcome"],
                    }
                    for seam in review["seams"]
                ],
                "context_notes": [
                    {
                        "heading": note["heading"],
                        "order": note["order"],
                        "outcome_present": note["outcome"] is not None,
                        **({"outcome": note["outcome"]} if note["outcome"] is not None else {}),
                    }
                    for note in review["context_notes"]
                ],
                "finding_count": len(review["findings"]),
                "overall_outcome": review["overall_outcome"],
                "next_step_present": review["next_step_markdown"] != "",
            }
            for review in full_manifest["reviews"]
        ],
    }

def project_min_shadow_review_manifest(full_manifest: dict[str, Any]) -> dict[str, Any]:
    return {
        "manifest_version": full_manifest["manifest_version"],
        "source_of_truth": full_manifest["source_of_truth"],
        "review_scope": full_manifest["review_scope"],
        "reviews": [
            {
                "review_id": review["review_id"],
                "review_path": review["review_path"],
                "title": review["title"],
                "intro_present": review["intro_markdown"] != "",
                "map_heading": review["map_heading"],
                "map_entries": [
                    {
                        "order": entry["order"],
                        "technique_id": entry["technique_id"],
                        "technique_path": entry["technique_path"],
                    }
                    for entry in review["map_entries"]
                ],
                "seams": [
                    {
                        "heading": seam["heading"],
                        "order": seam["order"],
                        "question_present": seam["question"] != "",
                        "outcome": seam["outcome"],
                    }
                    for seam in review["seams"]
                ],
                "finding_count": len(review["findings"]),
                "overall_outcome": review["overall_outcome"],
                "next_step_present": review["next_step_markdown"] != "",
            }
            for review in full_manifest["reviews"]
        ],
    }

def full_repo_doc_surface_manifest_entry(surface: RepoDocSurface) -> dict[str, Any]:
    return {
        "doc_id": surface.doc_id,
        "doc_path": surface.doc_path,
        "title": surface.title,
        "surface_group": surface.surface_group,
        "bounded_role": surface.bounded_role,
        "top_level_sections": list(surface.top_level_sections),
    }

def project_min_repo_doc_surface_manifest(full_manifest: dict[str, Any]) -> dict[str, Any]:
    return {
        "manifest_version": full_manifest["manifest_version"],
        "source_of_truth": full_manifest["source_of_truth"],
        "docs": [
            {
                "doc_id": doc["doc_id"],
                "doc_path": doc["doc_path"],
                "title": doc["title"],
                "surface_group": doc["surface_group"],
                "bounded_role": doc["bounded_role"],
                "top_level_sections": doc["top_level_sections"],
            }
            for doc in full_manifest["docs"]
        ],
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

def build_promotion_readiness_payload(repo_root: Path, records: list[TechniqueRecord]) -> dict[str, Any]:
    scoped_records = sorted(
        (record for record in records if record.status in {"canonical", "promoted"}),
        key=lambda record: record.id,
    )
    entries: list[dict[str, Any]] = []
    for record in scoped_records:
        note_kinds = {note.kind for note in record.notes}
        has_canonical_readiness_note = "canonical_readiness" in note_kinds
        has_adverse_effects_review = "adverse_effects_review" in note_kinds
        blockers: list[str] = []
        if record.status == "promoted" and not has_canonical_readiness_note:
            blockers.append("missing_canonical_readiness_note")
        if record.status == "canonical" and not has_adverse_effects_review:
            blockers.append("missing_adverse_effects_review")
        entries.append(
            {
                "technique_id": record.id,
                "technique_name": record.name,
                "status": record.status,
                "export_ready": bool(record.frontmatter.get("export_ready")),
                "review_required": bool(record.frontmatter.get("review_required")),
                "has_canonical_readiness_note": has_canonical_readiness_note,
                "has_adverse_effects_review": has_adverse_effects_review,
                "readiness_passed": len(blockers) == 0,
                "blockers": blockers,
            }
        )

    return {
        "schema_version": 1,
        "layer": "aoa-techniques",
        "scope": "published-non-deprecated",
        "source_of_truth": {
            "catalog": "generated/technique_catalog.min.json",
            "bundles": TECHNIQUE_BUNDLE_SOURCE_GLOB,
            "canonical_readiness_note": "notes/canonical-readiness.md",
            "adverse_effects_review": "notes/adverse-effects-review.md",
        },
        "techniques": entries,
    }

def build_capsule_payload(repo_root: Path, records: list[TechniqueRecord]) -> dict[str, Any]:
    sorted_records = sorted(records, key=lambda record: record.id)
    return {
        "capsule_version": CAPSULE_VERSION,
        "source_of_truth": CAPSULE_SOURCE_OF_TRUTH,
        "techniques": [full_capsule_entry(repo_root, record) for record in sorted_records],
    }

def project_min_capsule_payload(full_payload: dict[str, Any]) -> dict[str, Any]:
    return {
        "capsule_version": full_payload["capsule_version"],
        "source_of_truth": full_payload["source_of_truth"],
        "techniques": [
            {key: entry[key] for key in CAPSULE_MIN_FIELDS} for entry in full_payload["techniques"]
        ],
    }

def build_capsule_payloads(
    repo_root: Path, records: list[TechniqueRecord]
) -> tuple[dict[str, Any], dict[str, Any]]:
    full_payload = build_capsule_payload(repo_root, records)
    return full_payload, project_min_capsule_payload(full_payload)

def build_section_manifest_payloads(
    repo_root: Path, records: list[TechniqueRecord]
) -> tuple[dict[str, Any], dict[str, Any]]:
    sorted_records = sorted(records, key=lambda record: record.id)
    full_manifest = {
        "manifest_version": SECTION_MANIFEST_VERSION,
        "source_of_truth": SECTION_MANIFEST_SOURCE_OF_TRUTH,
        "section_scope": list(SECTION_LIFT_HEADINGS),
        "techniques": [full_section_manifest_entry(repo_root, record) for record in sorted_records],
    }
    return full_manifest, project_min_section_manifest(full_manifest)

def build_section_surface_payload(repo_root: Path, records: list[TechniqueRecord]) -> dict[str, Any]:
    sorted_records = sorted(records, key=lambda record: record.id)
    return {
        "section_version": SECTION_SURFACE_VERSION,
        "source_of_truth": SECTION_SURFACE_SOURCE_OF_TRUTH,
        "techniques": [full_section_surface_entry(repo_root, record) for record in sorted_records],
    }

def build_checklist_manifest_payloads(
    repo_root: Path, records: list[TechniqueRecord]
) -> tuple[dict[str, Any], dict[str, Any]]:
    sorted_records = sorted(records, key=lambda record: record.id)
    full_manifest = {
        "manifest_version": CHECKLIST_MANIFEST_VERSION,
        "source_of_truth": CHECKLIST_MANIFEST_SOURCE_OF_TRUTH,
        "techniques": [full_checklist_manifest_entry(repo_root, record) for record in sorted_records],
    }
    return full_manifest, project_min_checklist_manifest(full_manifest)

def build_example_manifest_payloads(
    repo_root: Path, records: list[TechniqueRecord]
) -> tuple[dict[str, Any], dict[str, Any]]:
    sorted_records = sorted(records, key=lambda record: record.id)
    full_manifest = {
        "manifest_version": EXAMPLE_MANIFEST_VERSION,
        "source_of_truth": EXAMPLE_MANIFEST_SOURCE_OF_TRUTH,
        "techniques": [full_example_manifest_entry(repo_root, record) for record in sorted_records],
    }
    return full_manifest, project_min_example_manifest(full_manifest)

def build_evidence_note_manifest_payloads(
    repo_root: Path, records: list[TechniqueRecord]
) -> tuple[dict[str, Any], dict[str, Any]]:
    sorted_records = sorted(records, key=lambda record: record.id)
    full_manifest = {
        "manifest_version": EVIDENCE_NOTE_MANIFEST_VERSION,
        "source_of_truth": EVIDENCE_NOTE_MANIFEST_SOURCE_OF_TRUTH,
        "typed_note_scopes": typed_note_scopes_payload(),
        "techniques": [
            full_evidence_note_manifest_entry(repo_root, record) for record in sorted_records
        ],
    }
    return full_manifest, project_min_evidence_note_manifest(full_manifest)

def build_github_review_template_manifest_payloads(
    repo_root: Path,
) -> tuple[dict[str, Any], dict[str, Any]]:
    templates = parse_github_review_templates(repo_root)
    full_manifest = {
        "manifest_version": GITHUB_REVIEW_TEMPLATE_MANIFEST_VERSION,
        "source_of_truth": GITHUB_REVIEW_TEMPLATE_MANIFEST_SOURCE_OF_TRUTH,
        "template_scopes": review_template_scopes_payload(),
        "templates": [
            full_github_review_template_manifest_entry(template) for template in templates
        ],
    }
    return full_manifest, project_min_github_review_template_manifest(full_manifest)

def build_semantic_review_manifest_payloads(
    repo_root: Path,
) -> tuple[dict[str, Any], dict[str, Any]]:
    reviews = parse_semantic_reviews(repo_root)
    full_manifest = {
        "manifest_version": SEMANTIC_REVIEW_MANIFEST_VERSION,
        "source_of_truth": SEMANTIC_REVIEW_MANIFEST_SOURCE_OF_TRUTH,
        "review_scope": semantic_review_scope_payload(),
        "reviews": [full_semantic_review_manifest_entry(review) for review in reviews],
    }
    return full_manifest, project_min_semantic_review_manifest(full_manifest)

def build_shadow_review_manifest_payloads(
    repo_root: Path,
) -> tuple[dict[str, Any], dict[str, Any]]:
    reviews = parse_shadow_reviews(repo_root)
    full_manifest = {
        "manifest_version": SHADOW_REVIEW_MANIFEST_VERSION,
        "source_of_truth": SHADOW_REVIEW_MANIFEST_SOURCE_OF_TRUTH,
        "review_scope": shadow_review_scope_payload(),
        "reviews": [full_shadow_review_manifest_entry(review) for review in reviews],
    }
    return full_manifest, project_min_shadow_review_manifest(full_manifest)

def build_repo_doc_surface_manifest_payloads(
    repo_root: Path,
) -> tuple[dict[str, Any], dict[str, Any]]:
    surfaces = parse_repo_doc_surfaces(repo_root)
    full_manifest = {
        "manifest_version": REPO_DOC_SURFACE_MANIFEST_VERSION,
        "source_of_truth": REPO_DOC_SURFACE_MANIFEST_SOURCE_OF_TRUTH,
        "surface_groups": repo_doc_surface_groups_payload(),
        "docs": [full_repo_doc_surface_manifest_entry(surface) for surface in surfaces],
    }
    return full_manifest, project_min_repo_doc_surface_manifest(full_manifest)

def kind_manifest_entry(entry: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": entry["id"],
        "name": entry["name"],
        "domain": entry["domain"],
        "status": entry["status"],
        "summary": entry["summary"],
        "technique_path": entry["technique_path"],
    }

def ordered_domain_counts(entries: list[dict[str, Any]]) -> dict[str, int]:
    counts = {domain: 0 for domain in DOMAIN_ORDER}
    for entry in entries:
        domain = entry["domain"]
        if domain not in counts:
            fail(f"generated catalog contains unsupported domain '{domain}'")
        counts[domain] += 1
    return counts

def ordered_kind_counts(entries: list[dict[str, Any]]) -> dict[str, int]:
    counts = {kind: 0 for kind in KIND_ORDER}
    for entry in entries:
        kind = entry["kind"]
        if kind not in counts:
            fail(f"generated catalog contains unsupported kind '{kind}'")
        counts[kind] += 1
    return counts

def catalog_domain_rank(domain: str) -> int:
    if domain in DOMAIN_ORDER:
        return DOMAIN_ORDER.index(domain)
    return len(DOMAIN_ORDER)

def kind_group_sort_key(entry: dict[str, Any]) -> tuple[int, int, str, str]:
    return (
        catalog_domain_rank(entry["domain"]),
        capsule_status_rank(entry["status"]),
        entry["status"],
        entry["id"],
    )

def project_min_kind_manifest(full_manifest: dict[str, Any]) -> dict[str, Any]:
    return {
        "manifest_version": full_manifest["manifest_version"],
        "source_of_truth": full_manifest["source_of_truth"],
        "selection_order": list(full_manifest["selection_order"]),
        "kinds": [
            {
                "kind": entry["kind"],
                "summary": entry["summary"],
                "counts": entry["counts"],
                "technique_ids": [technique["id"] for technique in entry["techniques"]],
            }
            for entry in full_manifest["kinds"]
        ],
    }

def build_kind_manifest_payloads(
    catalog: dict[str, Any], registry: dict[str, Any]
) -> tuple[dict[str, Any], dict[str, Any]]:
    catalog_entries = catalog.get("techniques")
    if not isinstance(catalog_entries, list):
        fail("generated/technique_catalog.json: techniques must be a list")
    selection_order = registry.get("selection_order")
    if selection_order != list(KIND_ORDER):
        fail("config/technique_kind_registry.yaml: selection_order must match KIND_ORDER exactly")
    registry_values = kind_registry_values_by_id(registry, TECHNIQUE_KIND_REGISTRY_PATH)

    full_manifest = {
        "manifest_version": KIND_MANIFEST_VERSION,
        "source_of_truth": KIND_MANIFEST_SOURCE_OF_TRUTH,
        "selection_order": list(selection_order),
        "kinds": [],
    }

    for kind in selection_order:
        registry_entry = registry_values[kind]
        matching_entries = sorted(
            [entry for entry in catalog_entries if entry.get("kind") == kind],
            key=kind_group_sort_key,
        )
        kind_entries = [kind_manifest_entry(entry) for entry in matching_entries]
        full_manifest["kinds"].append(
            {
                "kind": kind,
                "summary": registry_entry["summary"],
                "choose_when": list(registry_entry["choose_when"]),
                "not_when": list(registry_entry["not_when"]),
                "counts": {
                    "total": len(kind_entries),
                    "canonical": sum(1 for entry in matching_entries if entry["status"] == "canonical"),
                    "promoted": sum(1 for entry in matching_entries if entry["status"] == "promoted"),
                    "by_domain": ordered_domain_counts(matching_entries),
                },
                "techniques": kind_entries,
            }
        )

    return full_manifest, project_min_kind_manifest(full_manifest)

def build_kind_reader_markdown(full_manifest: dict[str, Any]) -> str:
    lines = [
        "# Technique Kinds",
        "",
        "This file is generated from `../../../generated/technique_catalog.json` plus the repo-owned `kind` registry.",
        "Do not edit it by hand; rebuild through [readers AGENTS](../AGENTS.md#validation).",
        "",
        "Use this surface when `domain` already narrowed the owner layer and you need the bounded second cut that answers what primary reusable practice a technique is.",
        "",
        "This surface is kind-first, not promotion-first. It keeps `kind` singular, repo-owned, and subordinate to authored bundle meaning.",
        "",
        "See also:",
        f"- [Technique Kind Guide]({SELECTION_GUIDE_PREFIX}TECHNIQUE_KIND_GUIDE.md)",
        "- [Technique Selection](../selection/TECHNIQUE_SELECTION.md)",
        f"- [Technique Kind Handoff Pack]({SELECTION_GUIDE_PREFIX}TECHNIQUE_KIND_HANDOFF_PACK.md)",
        f"- [Full kind manifest]({KIND_READER_ROOT_PREFIX}generated/technique_kind_manifest.json)",
        f"- [Min kind manifest]({KIND_READER_ROOT_PREFIX}generated/technique_kind_manifest.min.json)",
        f"- [Documentation Map]({KIND_READER_DOCS_PREFIX}README.md)",
        "",
        "## Kind Scope",
        "",
        "| kind | summary | total | canonical | promoted |",
        "|---|---|---|---|---|",
    ]

    for entry in full_manifest["kinds"]:
        counts = entry["counts"]
        lines.append(
            "| "
            f"`{entry['kind']}` | "
            f"{escape_markdown_table_cell(entry['summary'])} | "
            f"`{counts['total']}` | "
            f"`{counts['canonical']}` | "
            f"`{counts['promoted']}` |"
        )

    lines.append("")

    for entry in full_manifest["kinds"]:
        counts = entry["counts"]
        lines.extend(
            [
                f"## `{entry['kind']}`",
                "",
                f"{entry['summary']}",
                "",
                "Choose this when:",
            ]
        )
        lines.extend(f"- {item}" for item in entry["choose_when"])
        lines.extend(["", "Do not use this when:"])
        lines.extend(f"- {item}" for item in entry["not_when"])
        lines.extend(
            [
                "",
                f"Counts: `total` {counts['total']}, `canonical` {counts['canonical']}, `promoted` {counts['promoted']}.",
                "",
                "| domain | entries |",
                "|---|---|",
            ]
        )
        for domain, count in counts["by_domain"].items():
            lines.append(f"| `{domain}` | `{count}` |")

        lines.extend(
            [
                "",
                "| technique | domain | status | summary | source |",
                "|---|---|---|---|---|",
            ]
        )
        for technique in entry["techniques"]:
            lines.append(
                "| "
                f"{selection_technique_link(technique, KIND_READER_ROOT_PREFIX)} | "
                f"`{technique['domain']}` | "
                f"`{technique['status']}` | "
                f"{escape_markdown_table_cell(technique['summary'])} | "
                f"[TECHNIQUE.md]({KIND_READER_ROOT_PREFIX}{technique['technique_path']}) |"
            )
        if not entry["techniques"]:
            lines.append("| _No techniques currently mapped._ | - | - | - | - |")
        lines.append("")

    lines.extend(
        [
            "## Boundaries",
            "",
            "- `domain` stays the first owner and routing axis.",
            "- `kind` stays one bounded primary reusable-practice axis only.",
            "- `tags` remain the freeform nuance layer.",
            "- `family` stays scout-only and does not become frontmatter or schema truth in this wave.",
            "",
        ]
    )
    return "\n".join(lines)

def selection_technique_link(entry: dict[str, Any], relative_prefix: str = "../") -> str:
    return f"[{entry['id']}]({relative_prefix}{entry['technique_path']})"

def record_technique_link(
    repo_root: Path, record: TechniqueRecord, relative_prefix: str = "../"
) -> str:
    technique_path = record.technique_path.relative_to(repo_root).as_posix()
    return f"[{record.id}]({relative_prefix}{technique_path})"

def strip_display_prefix(text: str, prefix: str) -> str:
    if text.startswith(prefix):
        return text[len(prefix) :]
    return text

def capsule_status_rank(status: str) -> int:
    if status == "canonical":
        return 0
    if status == "promoted":
        return 1
    return 2

def kind_rank(kind: str) -> int:
    return KIND_INDEX.get(kind, len(KIND_ORDER))

def selection_entry_sort_key(entry: dict[str, Any]) -> tuple[int, int, str, str]:
    return (
        kind_rank(entry["kind"]),
        capsule_status_rank(entry["status"]),
        entry["status"],
        entry["id"],
    )

def escape_markdown_table_cell(value: str) -> str:
    flattened = re.sub(r"\s*\r?\n\s*", " ", value).strip()
    return flattened.replace("|", r"\|")

def record_sort_key(record: TechniqueRecord) -> tuple[int, int, str, str]:
    if record.domain in DOMAIN_ORDER:
        domain_rank = DOMAIN_ORDER.index(record.domain)
    else:
        domain_rank = len(DOMAIN_ORDER)
    return (domain_rank, capsule_status_rank(record.status), record.status, record.id)

def docs_relative_link(target_path: str) -> str:
    target = PurePosixPath(target_path)
    if target.parts[:1] == ("docs",):
        return PurePosixPath(*target.parts[1:]).as_posix()
    return PurePosixPath("..", *target.parts).as_posix()

def nested_reader_relative_link(target_path: str) -> str:
    target = PurePosixPath(target_path)
    if target.parts[:1] == ("docs",):
        return PurePosixPath("..", "..", *target.parts[1:]).as_posix()
    return PurePosixPath("..", "..", "..", *target.parts).as_posix()

def repo_doc_surface_link(surface: RepoDocSurface) -> str:
    return f"[{surface.title}]({nested_reader_relative_link(surface.doc_path)}) (`{surface.doc_path}`)"

def relation_summary(
    entry: dict[str, Any],
    entries_by_id: dict[str, dict[str, Any]],
    relative_prefix: str = "../",
) -> str:
    grouped: dict[str, list[str]] = {}
    for relation_type in RELATION_TYPE_ORDER:
        grouped[relation_type] = []

    for relation in entry.get("relations", []):
        target = entries_by_id[relation["target"]]
        grouped[relation["type"]].append(selection_technique_link(target, relative_prefix))

    parts: list[str] = []
    for relation_type in RELATION_TYPE_ORDER:
        targets = grouped[relation_type]
        if targets:
            parts.append(f"`{relation_type}` " + ", ".join(targets))
    return "; ".join(parts) if parts else "none"

def note_by_kind(record: TechniqueRecord, kind: str) -> TechniqueNote:
    for note in record.notes:
        if note.kind == kind:
            return note
    fail(f"{record.technique_path}: missing required note kind '{kind}'")

def note_section_by_heading(note: TechniqueNote, heading: str) -> EvidenceNoteSection:
    for section in note.sections:
        if section.heading == heading:
            return section
    fail(f"{note.note_path}: missing required section '{heading}'")

def note_field_value(section: EvidenceNoteSection, key: str, note_path: str) -> str:
    for field in section.fields:
        if field.key == key:
            return field.value_markdown
    fail(f"{note_path}: section '{section.heading}' must include field '{key}'")

def shadow_note_summary(record: TechniqueRecord) -> dict[str, str]:
    note = note_by_kind(record, "adverse_effects_review")
    review_focus = note_section_by_heading(note, "Review focus")
    failure_modes = note_section_by_heading(note, "Failure modes")
    if not failure_modes.items:
        fail(f"{note.note_path}: section 'Failure modes' must include at least one bullet")
    return {
        "current_role": note_field_value(review_focus, "current role", note.note_path),
        "watch_seam": note_field_value(review_focus, "current watch seam", note.note_path),
        "main_failure_mode": failure_modes.items[0].text,
        "note_path": note.note_path,
    }

def technique_source_link(
    repo_root: Path, record: TechniqueRecord, relative_prefix: str = "../"
) -> str:
    technique_path = record.technique_path.relative_to(repo_root).as_posix()
    return f"[TECHNIQUE.md]({relative_prefix}{technique_path})"

def note_kind_title(kind: str) -> str:
    if kind in TYPED_NOTE_TITLES:
        return TYPED_NOTE_TITLES[kind]
    if kind == "support_note":
        return "Support Note"
    return kind.replace("_", " ").title()

def typed_note_scope_signal(kind: str) -> str:
    headings = TYPED_NOTE_SECTION_SCOPES[kind]
    heading_list = ", ".join(f"`{heading}`" for heading in headings)
    return f"`{len(headings)}` fixed sections: {heading_list}"

def note_routing_signal(note: TechniqueNote) -> str:
    if note.note_shape == NOTE_SHAPE_TYPED:
        return f"`{len(note.sections)}` typed sections"
    return "`body_markdown` only"

def build_section_reader_markdown(repo_root: Path, records: list[TechniqueRecord]) -> str:
    sorted_records = sorted(records, key=record_sort_key)
    lines = [
        "# Technique Sections",
        "",
        "This file is generated from authoritative `TECHNIQUE.md` bundles plus the current section manifest payload.",
        "Do not edit it by hand; rebuild through [readers AGENTS](../AGENTS.md#validation).",
        "",
        "Use this surface when you need one bounded answer to which techniques expose a given lifted section heading without opening every bundle first.",
        "",
        "This surface is heading-first. It stays bounded to exactly `SECTION_LIFT_HEADINGS`, preserves their fixed order, and only exposes technique, section order, and source routing. It does not dump section markdown, invent section IDs, or act like search or graph behavior.",
        "",
        "See also:",
        f"- [Technique Section Lift Guide]({SOURCE_LIFT_READER_GUIDE_PREFIX}TECHNIQUE_SECTION_LIFT_GUIDE.md)",
        f"- [Full section manifest]({SOURCE_LIFT_READER_ROOT_PREFIX}generated/technique_section_manifest.json)",
        f"- [Min section manifest]({SOURCE_LIFT_READER_ROOT_PREFIX}generated/technique_section_manifest.min.json)",
        f"- [Documentation Map]({NESTED_READER_DOCS_PREFIX}README.md)",
        f"- [KAG Source Lift Guide]({SOURCE_LIFT_READER_GUIDE_PREFIX}KAG_SOURCE_LIFT_GUIDE.md)",
        "",
        "## Section Scope",
        "",
        "| order | heading | bounded role |",
        "|---|---|---|",
    ]

    for order, heading in enumerate(SECTION_LIFT_HEADINGS, start=1):
        lines.append(
            f"| `{order}` | `{heading}` | Lift the authored `{heading}` section into heading-first routing only. |"
        )

    lines.append("")

    for heading in SECTION_LIFT_HEADINGS:
        lifted_section_order = SECTION_LIFT_HEADINGS.index(heading) + 1
        lines.extend(
            [
                f"## `{heading}`",
                "",
                "| technique | domain | status | section order | source |",
                "|---|---|---|---|---|",
            ]
        )

        for record in sorted_records:
            if not any(section.heading == heading for section in record.sections):
                fail(f"{record.technique_path}: missing required lifted section '{heading}'")

            lines.append(
                "| "
                f"{record_technique_link(repo_root, record, SOURCE_LIFT_READER_ROOT_PREFIX)} - {escape_markdown_table_cell(record.name)} | "
                f"`{record.domain}` | "
                f"`{record.status}` | "
                f"`{lifted_section_order}` | "
                f"{technique_source_link(repo_root, record, SOURCE_LIFT_READER_ROOT_PREFIX)} |"
            )

        lines.append("")

    lines.extend(
        [
            "## Boundaries",
            "",
            "- The meaning remains in the authored `TECHNIQUE.md` bundles.",
            "- This surface is for section routing and lookup only.",
            "- This surface does not become section scoring, a section-ID layer, or search or graph behavior.",
            "",
        ]
    )
    return "\n".join(lines)

def build_checklist_reader_markdown(repo_root: Path, records: list[TechniqueRecord]) -> str:
    lines = [
        "# Technique Checklists",
        "",
        "This file is generated from authoritative `TECHNIQUE.md` bundles plus the current checklist manifest payload.",
        "Do not edit it by hand; rebuild through [readers AGENTS](../AGENTS.md#validation).",
        "",
        "Use this surface when you want a bounded checklist inventory by domain and technique without opening each bundle first.",
        "",
        "This surface stays domain-first and technique-first. It preserves checklist title, intro-presence, item count, check path, and source routing, including techniques that publish more than one checklist.",
        "",
        "See also:",
        f"- [Technique Checklist Lift Guide]({SOURCE_LIFT_READER_GUIDE_PREFIX}TECHNIQUE_CHECKLIST_LIFT_GUIDE.md)",
        f"- [Full checklist manifest]({SOURCE_LIFT_READER_ROOT_PREFIX}generated/technique_checklist_manifest.json)",
        f"- [Min checklist manifest]({SOURCE_LIFT_READER_ROOT_PREFIX}generated/technique_checklist_manifest.min.json)",
        f"- [Documentation Map]({NESTED_READER_DOCS_PREFIX}README.md)",
        f"- [KAG Source Lift Guide]({SOURCE_LIFT_READER_GUIDE_PREFIX}KAG_SOURCE_LIFT_GUIDE.md)",
        "",
    ]

    for domain in DOMAIN_ORDER:
        domain_records = sorted(
            [record for record in records if record.domain == domain],
            key=record_sort_key,
        )
        if not domain_records:
            continue

        lines.extend([f"## `{domain}`", ""])
        for record in domain_records:
            lines.extend(
                [
                    f"### {record_technique_link(repo_root, record, SOURCE_LIFT_READER_ROOT_PREFIX)} - {record.name} (`{record.status}`)",
                    "",
                ]
            )

            if not record.checklists:
                lines.extend(["_No checklists currently published._", ""])
                continue

            lines.extend(
                [
                    "| checklist | intro | items | check path | source |",
                    "|---|---|---|---|---|",
                ]
            )
            for checklist in record.checklists:
                intro_signal = "present" if checklist.intro_markdown else "absent"
                lines.append(
                    "| "
                    f"{escape_markdown_table_cell(checklist.title)} | "
                    f"`{intro_signal}` | "
                    f"`{len(checklist.items)}` | "
                    f"`{checklist.check_path}` | "
                    f"{technique_source_link(repo_root, record, SOURCE_LIFT_READER_ROOT_PREFIX)} |"
                )

            lines.append("")

    lines.extend(
        [
            "## Boundaries",
            "",
            "- The meaning remains in the authored checklist files and source bundles.",
            "- This surface is derived validation knowledge only.",
            "- This surface does not become executable policy, hard-gate semantics, or scoring.",
            "",
        ]
    )
    return "\n".join(lines)

def build_example_reader_markdown(repo_root: Path, records: list[TechniqueRecord]) -> str:
    lines = [
        "# Technique Examples",
        "",
        "This file is generated from authoritative `TECHNIQUE.md` bundles plus the current example manifest payload.",
        "Do not edit it by hand; rebuild through [readers AGENTS](../AGENTS.md#validation).",
        "",
        "Use this surface when you want a bounded example inventory by domain and technique without opening every example body first.",
        "",
        "This surface preserves example title, example path, body-presence, and source routing only. It does not inline full example bodies into the generated reader surface.",
        "",
        "See also:",
        f"- [Technique Example Lift Guide]({SOURCE_LIFT_READER_GUIDE_PREFIX}TECHNIQUE_EXAMPLE_LIFT_GUIDE.md)",
        f"- [Full example manifest]({SOURCE_LIFT_READER_ROOT_PREFIX}generated/technique_example_manifest.json)",
        f"- [Min example manifest]({SOURCE_LIFT_READER_ROOT_PREFIX}generated/technique_example_manifest.min.json)",
        f"- [Documentation Map]({NESTED_READER_DOCS_PREFIX}README.md)",
        f"- [KAG Source Lift Guide]({SOURCE_LIFT_READER_GUIDE_PREFIX}KAG_SOURCE_LIFT_GUIDE.md)",
        "",
    ]

    for domain in DOMAIN_ORDER:
        domain_records = sorted(
            [record for record in records if record.domain == domain],
            key=record_sort_key,
        )
        if not domain_records:
            continue

        lines.extend([f"## `{domain}`", ""])
        for record in domain_records:
            lines.extend(
                [
                    f"### {record_technique_link(repo_root, record, SOURCE_LIFT_READER_ROOT_PREFIX)} - {record.name} (`{record.status}`)",
                    "",
                ]
            )

            if not record.examples:
                lines.extend(["_No examples currently published._", ""])
                continue

            lines.extend(
                [
                    "| example | body | example path | source |",
                    "|---|---|---|---|",
                ]
            )
            for example in record.examples:
                body_signal = "present" if example.body_markdown else "absent"
                lines.append(
                    "| "
                    f"{escape_markdown_table_cell(example.title)} | "
                    f"`{body_signal}` | "
                    f"`{example.example_path}` | "
                    f"{technique_source_link(repo_root, record, SOURCE_LIFT_READER_ROOT_PREFIX)} |"
                )

            lines.append("")

    lines.extend(
        [
            "## Boundaries",
            "",
            "- The meaning remains in the authored example files and source bundles.",
            "- This surface is derived example knowledge only.",
            "- This surface does not become scenario graphs, executable tests, or richer step extraction.",
            "",
        ]
    )
    return "\n".join(lines)

def build_evidence_note_reader_markdown(repo_root: Path, records: list[TechniqueRecord]) -> str:
    notes_by_kind: dict[str, list[tuple[TechniqueRecord, TechniqueNote]]] = {}
    for record in sorted(records, key=record_sort_key):
        for note in record.notes:
            notes_by_kind.setdefault(note.kind, []).append((record, note))

    known_kind_order = list(TYPED_NOTE_KIND_ORDER) + ["support_note"]
    ordered_kinds = [kind for kind in known_kind_order if kind in notes_by_kind]
    ordered_kinds.extend(sorted(kind for kind in notes_by_kind if kind not in known_kind_order))

    lines = [
        "# Evidence Note Surfaces",
        "",
        "This file is generated from authoritative evidence-note markdown plus the current evidence note manifest payload.",
        "Do not edit it by hand; rebuild through [readers AGENTS](../AGENTS.md#validation).",
        "",
        "Use this surface when you need note-kind routing, note-shape awareness, or a bounded inventory of supporting note surfaces without flattening note prose into one reader layer.",
        "",
        "This surface is note-scope first. It only exposes note kind, title, note path, note shape, owning technique, and bounded routing signals such as fixed section scopes or opaque-body handling. It does not flatten note prose, review arguments, or caution language into the reader.",
        "",
        "See also:",
        f"- [Evidence Note Provenance Guide]({SOURCE_LIFT_READER_GUIDE_PREFIX}EVIDENCE_NOTE_PROVENANCE_GUIDE.md)",
        f"- [Full evidence note manifest]({SOURCE_LIFT_READER_ROOT_PREFIX}generated/technique_evidence_note_manifest.json)",
        f"- [Min evidence note manifest]({SOURCE_LIFT_READER_ROOT_PREFIX}generated/technique_evidence_note_manifest.min.json)",
        f"- [Documentation Map]({NESTED_READER_DOCS_PREFIX}README.md)",
        f"- [KAG Source Lift Guide]({SOURCE_LIFT_READER_GUIDE_PREFIX}KAG_SOURCE_LIFT_GUIDE.md)",
        "",
        "## Note Scope",
        "",
        "| note kind | title | note shape | routing signal | entries |",
        "|---|---|---|---|---|",
    ]

    for kind in ordered_kinds:
        if kind in TYPED_NOTE_SECTION_SCOPES:
            note_shape = NOTE_SHAPE_TYPED
            routing_signal = typed_note_scope_signal(kind)
        else:
            note_shape = NOTE_SHAPE_OPAQUE
            routing_signal = "opaque note body only"

        lines.append(
            "| "
            f"`{kind}` | "
            f"{escape_markdown_table_cell(note_kind_title(kind))} | "
            f"`{note_shape}` | "
            f"{escape_markdown_table_cell(routing_signal)} | "
            f"`{len(notes_by_kind[kind])}` |"
        )

    lines.append("")

    for kind in ordered_kinds:
        lines.extend(
            [
                f"## `{kind}` - {note_kind_title(kind)}",
                "",
                "| title | note shape | routing signal | owning technique | note path | source |",
                "|---|---|---|---|---|---|",
            ]
        )

        for record, note in notes_by_kind[kind]:
            lines.append(
                "| "
                f"{escape_markdown_table_cell(note.title)} | "
                f"`{note.note_shape}` | "
                f"{escape_markdown_table_cell(note_routing_signal(note))} | "
                f"{record_technique_link(repo_root, record, SOURCE_LIFT_READER_ROOT_PREFIX)} | "
                f"`{note.note_path}` | "
                f"[Note]({SOURCE_LIFT_READER_ROOT_PREFIX}{note.note_path}) |"
            )

        lines.append("")

    lines.extend(
        [
            "## Boundaries",
            "",
            "- The meaning remains in the authored note markdown.",
            "- This surface is derived provenance and routing knowledge only.",
            "- `adverse_effects_review` stays a typed note role, not generated caution policy or a machine-readable caution verdict engine.",
            "- This surface does not flatten note prose, review arguments, or support-note bodies into one merged reader layer.",
            "",
        ]
    )
    return "\n".join(lines)

def build_capsule_markdown(repo_root: Path, records: list[TechniqueRecord]) -> str:
    records_by_id = {record.id: record for record in records}
    full_payload = build_capsule_payload(repo_root, records)
    entries_by_domain: dict[str, list[tuple[TechniqueRecord, dict[str, Any]]]] = {
        domain: [] for domain in DOMAIN_ORDER
    }

    for entry in full_payload["techniques"]:
        record = records_by_id[entry["id"]]
        entries_by_domain[record.domain].append((record, entry))

    lines = [
        "# Technique Capsules",
        "",
        "This file is generated from authoritative `TECHNIQUE.md` bundles plus the current local capsule payload.",
        "Do not edit it by hand; rebuild through [readers AGENTS](../AGENTS.md#validation).",
        "",
        "Use this surface when one bounded local runtime card is enough to orient on a technique without opening selection, review, or manifest layers first.",
        "",
        "Capsules are derived local runtime cards for lookup only. They are not the source of truth and they do not replace the authored technique bundles.",
        "",
        "See also:",
        f"- [Technique Capsule Guide]({SELECTION_GUIDE_PREFIX}TECHNIQUE_CAPSULE_GUIDE.md)",
        f"- [Full capsule JSON]({RUNTIME_READER_ROOT_PREFIX}generated/technique_capsules.json)",
        f"- [Min capsule JSON]({RUNTIME_READER_ROOT_PREFIX}generated/technique_capsules.min.json)",
        f"- [Documentation Map]({RUNTIME_READER_DOCS_PREFIX}README.md)",
        "",
    ]

    for domain in DOMAIN_ORDER:
        lines.extend([f"## `{domain}`", ""])
        ordered_entries = sorted(
            entries_by_domain[domain],
            key=lambda item: (capsule_status_rank(item[0].status), item[0].status, item[0].id),
        )

        for record, entry in ordered_entries:
            lines.extend(
                [
                    f"### {record_technique_link(repo_root, record, RUNTIME_READER_ROOT_PREFIX)} - {entry['name']} (`{record.status}`)",
                    "",
                    f"- Summary: {entry['summary']}",
                    f"- Intent: {entry['one_line_intent']}",
                    f"- Use when: {strip_display_prefix(entry['use_when_short'], 'Use when ')}",
                    f"- Avoid when: {strip_display_prefix(entry['do_not_use_short'], 'Avoid when ')}",
                    f"- Needs: {strip_display_prefix(entry['inputs_short'], 'Needs ')}",
                    f"- Produces: {strip_display_prefix(entry['outputs_short'], 'Produces ')}",
                    f"- Core contract: {strip_display_prefix(entry['core_contract_short'], 'Core contract: ')}",
                    f"- Main risk: {strip_display_prefix(entry['main_risk_short'], 'Main risk: ')}",
                    f"- Validate by: {strip_display_prefix(entry['validation_short'], 'Validate by checking ')}",
                    f"- Source: [TECHNIQUE.md]({RUNTIME_READER_ROOT_PREFIX}{entry['technique_path']})",
                    "",
                ]
            )

    lines.extend(
        [
            "## Boundaries",
            "",
            "- The source of meaning stays in the authored `TECHNIQUE.md` bundles.",
            "- Capsules stay local runtime lookup aids only; they are not KAG/source-lift surfaces and they do not replace the full bundle.",
            "- This surface is not selection, scoring, or policy routing.",
            "",
        ]
    )

    return "\n".join(lines)

def build_selection_surface_markdown(full_catalog: dict[str, Any]) -> str:
    entries = list(full_catalog["techniques"])
    entries_by_id = {entry["id"]: entry for entry in entries}
    canonical_by_domain: dict[str, list[dict[str, Any]]] = {domain: [] for domain in DOMAIN_ORDER}
    entries_by_domain: dict[str, list[dict[str, Any]]] = {domain: [] for domain in DOMAIN_ORDER}

    for entry in entries:
        domain = entry["domain"]
        entries_by_domain[domain].append(entry)
        if entry["status"] == "canonical":
            canonical_by_domain[domain].append(entry)

    for domain in DOMAIN_ORDER:
        canonical_by_domain[domain].sort(key=selection_entry_sort_key)
        entries_by_domain[domain].sort(key=selection_entry_sort_key)

    export_ready_true = sum(1 for entry in entries if entry["export_ready"])
    total_entries = len(entries)
    evaluation_starters = canonical_by_domain["evaluation"]

    lines = [
        "# Technique Selection",
        "",
        "This file is generated from `../../../generated/technique_catalog.json` and the authoritative markdown frontmatter.",
        "Do not edit it by hand; rebuild through [readers AGENTS](../AGENTS.md#validation).",
        "",
        "Use this surface to make one bounded choice:",
        "1. narrow by `domain` first",
        "2. narrow by `kind` second",
        "3. prefer `canonical` techniques for default use",
        "4. use `validation_strength` as an evidence-breadth signal",
        "5. use direct `relations` as adjacency hints, not graph traversal",
        "",
        "See also:",
        f"- [Start Here]({SELECTION_READER_DOCS_PREFIX}START_HERE.md)",
        f"- [Technique Selection Guide]({SELECTION_GUIDE_PREFIX}TECHNIQUE_SELECTION_GUIDE.md)",
        f"- [TECHNIQUE_INDEX]({SELECTION_READER_ROOT_PREFIX}TECHNIQUE_INDEX.md)",
        f"- [CANONICAL_RUBRIC]({REVIEW_GUIDE_PREFIX}CANONICAL_RUBRIC.md)",
        f"- [Full catalog JSON]({SELECTION_READER_ROOT_PREFIX}generated/technique_catalog.json)",
        f"- [Min catalog JSON]({SELECTION_READER_ROOT_PREFIX}generated/technique_catalog.min.json)",
        "",
        "If you still need repo-level orientation before choosing a technique, open `START_HERE.md` first.",
        "",
        "## Quick Questions",
        "",
        "### I need an evaluation pattern. Where do I start?",
        "",
        "| technique | kind | validation | summary |",
        "|---|---|---|---|",
    ]

    for entry in evaluation_starters:
        lines.append(
            "| "
            f"{selection_technique_link(entry, SELECTION_READER_ROOT_PREFIX)} | "
            f"`{entry['kind']}` | "
            f"`{entry['validation_strength']}` | "
            f"{escape_markdown_table_cell(entry['summary'])} |"
        )

    lines.extend(
        [
            "",
            "### What are the current canonical defaults by domain?",
            "",
            "| domain | canonical defaults |",
            "|---|---|",
        ]
    )

    for domain in DOMAIN_ORDER:
        defaults = ", ".join(
            f"{selection_technique_link(entry, SELECTION_READER_ROOT_PREFIX)} (`{entry['kind']}`)"
            for entry in canonical_by_domain[domain]
        )
        lines.append(f"| `{domain}` | {defaults or '-'} |")

    lines.extend(
        [
            "",
            "### If I choose one technique, what nearby techniques usually go with it?",
            "",
        ]
    )

    for entry in entries:
        lines.append(
            f"- {selection_technique_link(entry, SELECTION_READER_ROOT_PREFIX)}: "
            f"{relation_summary(entry, entries_by_id, SELECTION_READER_ROOT_PREFIX)}"
        )

    lines.extend(
        [
            "",
            "## Browse By Domain",
            "",
            "Within each domain, techniques are ordered by `kind`, then by status, then by ID.",
            "",
        ]
    )

    for domain in DOMAIN_ORDER:
        lines.extend(
            [
                f"### `{domain}`",
                "",
                "| technique | kind | status | validation | rigor | summary |",
                "|---|---|---|---|---|---|",
            ]
        )
        for entry in entries_by_domain[domain]:
            lines.append(
                "| "
                f"{selection_technique_link(entry, SELECTION_READER_ROOT_PREFIX)} | "
                f"`{entry['kind']}` | "
                f"`{entry['status']}` | "
                f"`{entry['validation_strength']}` | "
                f"`{entry['rigor_level']}` | "
                f"{escape_markdown_table_cell(entry['summary'])} |"
            )
        lines.append("")

    lines.extend(
        [
            "## Current Catalog Audit",
            "",
            f"- `export_ready` is currently `true` for {export_ready_true}/{total_entries} techniques.",
            "- For the current corpus, that uniform `true` is intentional: every tracked bundle is considered safe for Stage 1 catalog publication.",
            "- Treat `export_ready` as the current Stage 1 catalog-publication safety floor, not as a meaningful selector yet.",
            "- A future `export_ready: false` should mean one bounded thing only: the markdown bundle may still exist, but structured catalog publication would currently overstate its safety, trustworthiness, or stability.",
            "",
        ]
    )

    return "\n".join(lines)

def build_shadow_patterns_markdown(repo_root: Path, records: list[TechniqueRecord]) -> str:
    records_by_id = {record.id: record for record in records}
    review_doc_links = [
        (Path(spec["review_doc"]).name, nested_reader_relative_link(spec["review_doc"]))
        for spec in SHADOW_WORKING_SET_SPECS
    ]

    lines = [
        "# Shadow Patterns",
        "",
        "This file is generated from authoritative `TECHNIQUE.md` bundles plus typed canonical `adverse_effects_review` notes.",
        "Do not edit it by hand; rebuild through [readers AGENTS](../AGENTS.md#validation).",
        "",
        "Use this surface when the main question is not which technique to choose, but where a canonical technique can quietly make the system worse and which watch seam to inspect first.",
        "",
        "This surface is canonical-only. It stays bounded to authored markdown, typed adverse-effects notes, review-backed working sets, and validator-backed prompts. It does not do scoring, policy routing, or generated caution metadata.",
        "",
        "See also:",
        f"- [Technique Shadow Guide]({REVIEW_GUIDE_PREFIX}TECHNIQUE_SHADOW_GUIDE.md)",
        f"- [Risk And Negative-Effect Lift Guide](../../source-lift/RISK_AND_NEGATIVE_EFFECT_LIFT_GUIDE.md)",
        *[f"- [{name}]({link})" for name, link in review_doc_links],
        "",
        "## Working Sets",
        "",
    ]

    for spec in SHADOW_WORKING_SET_SPECS:
        linked_techniques = ", ".join(
            record_technique_link(repo_root, records_by_id[technique_id], REVIEW_READER_ROOT_PREFIX)
            for technique_id in spec["technique_ids"]
        )
        review_doc_name = Path(spec["review_doc"]).name
        review_doc_link = nested_reader_relative_link(spec["review_doc"])
        lines.extend(
            [
                f"### {spec['title']}",
                "",
                f"- Techniques: {linked_techniques}",
                f"- Review: [{review_doc_name}]({review_doc_link})",
                f"- Why grouped: {spec['note']}",
                "",
                "| technique | current role | watch seam | main failure mode | note |",
                "|---|---|---|---|---|",
            ]
        )

        for technique_id in spec["technique_ids"]:
            record = records_by_id[technique_id]
            summary = shadow_note_summary(record)
            lines.append(
                "| "
                f"{record_technique_link(repo_root, record, REVIEW_READER_ROOT_PREFIX)} | "
                f"{escape_markdown_table_cell(summary['current_role'])} | "
                f"{escape_markdown_table_cell(summary['watch_seam'])} | "
                f"{escape_markdown_table_cell(summary['main_failure_mode'])} | "
                f"[Adverse Effects Review]({REVIEW_READER_ROOT_PREFIX}{summary['note_path']}) |"
            )

        lines.append("")

    lines.extend(
        [
            "## Common Shadow Questions",
            "",
            "| question | inspect first | why |",
            "|---|---|---|",
        ]
    )

    for spec in SHADOW_COMMON_QUESTION_SPECS:
        record = records_by_id[spec["target_id"]]
        lines.append(
            "| "
            f"{escape_markdown_table_cell(spec['prompt'])} | "
            f"{record_technique_link(repo_root, record, REVIEW_READER_ROOT_PREFIX)} | "
            f"{escape_markdown_table_cell(spec['note'])} |"
        )

    lines.extend(
        [
            "",
            "## Boundaries",
            "",
            "- The source of meaning stays in the full technique bundle and its typed adverse-effects review note.",
            "- This surface is a bounded lookup aid for canonical watch seams, not a permission to skip `TECHNIQUE.md`.",
            "- If a question needs scoring, policy tiers, or machine-readable caution exports, that is a later wave.",
            "",
        ]
    )

    return "\n".join(lines)

def build_repo_doc_surfaces_markdown(repo_root: Path) -> str:
    surfaces = parse_repo_doc_surfaces(repo_root)
    surfaces_by_id = {surface.doc_id: surface for surface in surfaces}
    surfaces_by_group: dict[str, list[RepoDocSurface]] = {
        group: [] for group in REPO_DOC_SURFACE_GROUP_ORDER
    }

    for surface in surfaces:
        surfaces_by_group[surface.surface_group].append(surface)

    group_specs = {spec["group"]: spec for spec in REPO_DOC_SURFACE_GROUP_SPECS}

    lines = [
        "# Repo Doc Surfaces",
        "",
        "This file is generated from the authoritative public route, canon-law, contribution, example, and status layer only.",
        "Do not edit it by hand; rebuild through [readers AGENTS](../AGENTS.md#validation).",
        "",
        "Use this surface when the main question is which public repo doc to open next for orientation, canon boundaries, contribution rules, public-safety expectations, direction, obligations, or release/status context.",
        "",
        "It stays bounded to the current authored public route/canon/status source set. It excludes local planning files such as `TODO.md` and `PLANS.md`, plus deeper guide/review docs outside the named bounded source set.",
        "",
        "See also:",
        f"- [Start Here]({REPO_DOC_READER_DOCS_PREFIX}START_HERE.md)",
        f"- [Repo Doc Surface Lift Guide]({REPO_DOC_READER_GUIDE_PREFIX}REPO_DOC_SURFACE_LIFT_GUIDE.md)",
        f"- [Full repo doc surface manifest]({REPO_DOC_READER_ROOT_PREFIX}generated/repo_doc_surface_manifest.json)",
        f"- [Documentation Map]({REPO_DOC_READER_DOCS_PREFIX}README.md)",
        f"- [KAG Source Lift Guide]({REPO_DOC_READER_GUIDE_PREFIX}KAG_SOURCE_LIFT_GUIDE.md)",
        "",
        "## Quick Navigation",
        "",
        "| question | open | why |",
        "|---|---|---|",
    ]

    for spec in REPO_DOC_NAVIGATION_SPECS:
        open_docs = ", ".join(
            repo_doc_surface_link(surfaces_by_id[doc_id]) for doc_id in spec["doc_ids"]
        )
        lines.append(
            "| "
            f"{escape_markdown_table_cell(spec['question'])} | "
            f"{open_docs} | "
            f"{escape_markdown_table_cell(spec['note'])} |"
        )

    lines.append("")

    for group in REPO_DOC_SURFACE_GROUP_ORDER:
        group_spec = group_specs[group]
        lines.extend(
            [
                f"## {group_spec['heading']}",
                "",
                group_spec["note"],
                "",
                "| doc | bounded role | top-level sections |",
                "|---|---|---|",
            ]
        )

        for surface in surfaces_by_group[group]:
            sections_markdown = ", ".join(f"`{heading}`" for heading in surface.top_level_sections)
            lines.append(
                "| "
                f"{repo_doc_surface_link(surface)} | "
                f"{escape_markdown_table_cell(surface.bounded_role)} | "
                f"{escape_markdown_table_cell(sections_markdown)} |"
            )

        lines.append("")

    lines.extend(
        [
            "## Boundaries",
            "",
            "- The source of meaning stays in the authored docs themselves.",
            "- The bounded source set is exactly the 21 authoritative public route/canon/status files named in `REPO_DOC_SURFACE_LIFT_GUIDE.md`.",
            "- This surface and its manifest are routing aids only. They do not become a new source of truth, root-authority replacement, or status-policy engine.",
            "",
        ]
    )

    return "\n".join(lines)

def build_selection_patterns_markdown(full_catalog: dict[str, Any]) -> str:
    entries = list(full_catalog["techniques"])
    entries_by_id = {entry["id"]: entry for entry in entries}
    canonical_by_domain: dict[str, list[dict[str, Any]]] = {domain: [] for domain in DOMAIN_ORDER}

    for entry in entries:
        if entry["status"] == "canonical":
            canonical_by_domain[entry["domain"]].append(entry)
    domain_specs = {spec["domain"]: spec for spec in DOMAIN_START_SPECS}

    lines = [
        "# Selection Patterns",
        "",
        "This file is generated from `../../../generated/technique_catalog.json`, current direct `relations`, validator-backed navigation specs, and review-backed working sets.",
        "Do not edit it by hand; rebuild through [readers AGENTS](../AGENTS.md#validation).",
        "",
        "Use this surface when the flat adjacency list in `TECHNIQUE_SELECTION.md` is not enough and you want one bounded answer to:",
        '- "What nearby technique should I inspect next, and why?"',
        "",
        "This surface uses direct relation navigation, validator-backed starting points and common moves, and review-backed clusters only. It does not do graph search, scoring, or multi-hop reasoning.",
        "",
        "See also:",
        f"- [Start Here]({SELECTION_READER_DOCS_PREFIX}START_HERE.md)",
        f"- [Technique Selection Guide]({SELECTION_GUIDE_PREFIX}TECHNIQUE_SELECTION_GUIDE.md)",
        f"- [Semantic Review Guide]({REVIEW_GUIDE_PREFIX}SEMANTIC_REVIEW_GUIDE.md)",
        "- [Technique Selection](TECHNIQUE_SELECTION.md)",
        f"- [TECHNIQUE_INDEX]({SELECTION_READER_ROOT_PREFIX}TECHNIQUE_INDEX.md)",
        f"- [Full catalog JSON]({SELECTION_READER_ROOT_PREFIX}generated/technique_catalog.json)",
        "",
        "If you still need repo-level orientation before following a working set or common move, open `START_HERE.md` first.",
        "",
        "## Starting Points",
        "",
        "| domain | canonical defaults | start here |",
        "|---|---|---|",
    ]

    for domain in DOMAIN_ORDER:
        defaults = ", ".join(
            selection_technique_link(entry, SELECTION_READER_ROOT_PREFIX)
            for entry in canonical_by_domain[domain]
        )
        spec = domain_specs[domain]
        lines.append(
            f"| `{domain}` | {defaults or '-'} | {escape_markdown_table_cell(spec['note'])} |"
        )

    lines.extend(["", "## Working Sets", ""])

    for spec in WORKING_SET_SPECS:
        linked_techniques = ", ".join(
            selection_technique_link(entries_by_id[technique_id], SELECTION_READER_ROOT_PREFIX)
            for technique_id in spec["technique_ids"]
        )
        review_doc_name = Path(spec["review_doc"]).name
        review_doc_link = nested_reader_relative_link(spec["review_doc"])
        lines.extend(
            [
                f"### {spec['title']}",
                "",
                f"- Techniques: {linked_techniques}",
                f"- Review: [{review_doc_name}]({review_doc_link})",
                f"- Why grouped: {spec['note']}",
                "",
            ]
        )

    lines.extend(
        [
            "## Common Moves",
            "",
            "| situation | inspect next | why |",
            "|---|---|---|",
        ]
    )

    for spec in COMMON_MOVE_SPECS:
        lines.append(
            "| "
            f"{escape_markdown_table_cell(spec['prompt'])} | "
            f"{selection_technique_link(entries_by_id[spec['target_id']], SELECTION_READER_ROOT_PREFIX)} | "
            f"{escape_markdown_table_cell(spec['note'])} |"
        )

    lines.extend(
        [
            "",
            "## Relation Notes",
            "",
            "- `requires` means one technique usually depends on another contract already existing.",
            "- `complements` means two techniques commonly strengthen each other without collapsing into one pattern.",
            "- `used_together_for` means the pair commonly appears in the same operating path, even if one does not strictly depend on the other.",
            "- `shares_contract_with` means neighboring techniques rely on the same bounded contract but still do different work.",
            "- This surface uses direct relation hints only. It does not do graph traversal, ranking, or multi-hop inference.",
            "",
        ]
    )

    return "\n".join(lines)

def write_json_file(path: Path, payload: Any, compact: bool) -> None:
    if compact:
        encoded = json.dumps(payload, ensure_ascii=True, separators=(",", ":"))
    else:
        encoded = json.dumps(payload, ensure_ascii=True, indent=2)
    path.write_text(encoded + "\n", encoding="utf-8")

def write_text_file(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")

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
                "kind",
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

def validate_promotion_readiness_surface(repo_root: Path, records: list[TechniqueRecord]) -> None:
    path = repo_root / "generated" / "technique_promotion_readiness.min.json"
    expected = build_promotion_readiness_payload(repo_root, records)
    actual = read_json(path)

    if actual != expected:
        fail(
            f"{path}: generated promotion readiness surface is out of date; "
            "run 'python scripts/build_promotion_readiness.py'"
        )
    if actual.get("schema_version") != 1:
        fail(f"{path}: must declare schema_version 1")
    if actual.get("layer") != "aoa-techniques":
        fail(f"{path}: must declare layer 'aoa-techniques'")
    if actual.get("scope") != "published-non-deprecated":
        fail(f"{path}: must declare scope 'published-non-deprecated'")
    expected_source_of_truth = {
        "catalog": "generated/technique_catalog.min.json",
        "bundles": TECHNIQUE_BUNDLE_SOURCE_GLOB,
        "canonical_readiness_note": "notes/canonical-readiness.md",
        "adverse_effects_review": "notes/adverse-effects-review.md",
    }
    if actual.get("source_of_truth") != expected_source_of_truth:
        fail(f"{path}: must keep source_of_truth stable")

    entries = actual.get("techniques")
    if not isinstance(entries, list):
        fail(f"{path}: techniques must be a list")

    expected_records = sorted(
        (record for record in records if record.status in {"canonical", "promoted"}),
        key=lambda record: record.id,
    )
    expected_ids = [record.id for record in expected_records]
    actual_ids = [entry.get("technique_id") for entry in entries if isinstance(entry, dict)]
    if actual_ids != expected_ids:
        fail(f"{path}: techniques must cover the published canonical/promoted corpus exactly once")
    if len(actual_ids) != len(set(actual_ids)):
        fail(f"{path}: techniques must not duplicate technique_id")

    records_by_id = {record.id: record for record in expected_records}
    for index, entry in enumerate(entries):
        location = f"{path}[{index}]"
        if not isinstance(entry, dict):
            fail(f"{location}: entry must be an object")
        technique_id = entry.get("technique_id")
        if not isinstance(technique_id, str) or technique_id not in records_by_id:
            fail(f"{location}: technique_id must resolve in the canonical/promoted corpus")
        record = records_by_id[technique_id]
        if entry.get("technique_name") != record.name:
            fail(f"{location}: technique_name must match authored frontmatter")
        if entry.get("status") != record.status:
            fail(f"{location}: status must match authored frontmatter")
        if entry.get("export_ready") is not bool(record.frontmatter.get("export_ready")):
            fail(f"{location}: export_ready must match authored frontmatter")
        if entry.get("review_required") is not bool(record.frontmatter.get("review_required")):
            fail(f"{location}: review_required must match authored frontmatter")

        note_kinds = {note.kind for note in record.notes}
        expected_has_canonical_readiness = "canonical_readiness" in note_kinds
        expected_has_adverse_effects_review = "adverse_effects_review" in note_kinds
        if entry.get("has_canonical_readiness_note") is not expected_has_canonical_readiness:
            fail(f"{location}: has_canonical_readiness_note must reflect bundle notes")
        if entry.get("has_adverse_effects_review") is not expected_has_adverse_effects_review:
            fail(f"{location}: has_adverse_effects_review must reflect bundle notes")

        blockers = entry.get("blockers")
        if not isinstance(blockers, list) or not all(isinstance(item, str) for item in blockers):
            fail(f"{location}: blockers must be a list of strings")
        expected_blockers: list[str] = []
        if record.status == "promoted" and not expected_has_canonical_readiness:
            expected_blockers.append("missing_canonical_readiness_note")
        if record.status == "canonical" and not expected_has_adverse_effects_review:
            expected_blockers.append("missing_adverse_effects_review")
        if blockers != expected_blockers:
            fail(f"{location}: blockers must stay aligned with the current note-backed readiness posture")
        if entry.get("readiness_passed") is not (len(expected_blockers) == 0):
            fail(f"{location}: readiness_passed must reflect whether blockers is empty")

def validate_capsules(repo_root: Path, records: list[TechniqueRecord]) -> None:
    path = repo_root / "generated" / "technique_capsules.json"
    min_path = repo_root / "generated" / "technique_capsules.min.json"
    reader_path = repo_root / "docs" / "readers" / "runtime" / "TECHNIQUE_CAPSULES.md"
    expected_full, expected_min = build_capsule_payloads(repo_root, records)
    expected_reader = build_capsule_markdown(repo_root, records)
    actual = read_json(path)
    actual_min = read_json(min_path)
    actual_reader = read_text(reader_path)

    if actual != expected_full:
        fail(f"{path}: generated capsules are out of date; run 'python scripts/build_capsules.py'")
    if actual_min != expected_min:
        fail(f"{min_path}: generated min capsules are out of date; run 'python scripts/build_capsules.py'")
    if actual_reader != expected_reader:
        fail(
            f"{reader_path}: generated capsule reader surface is out of date; "
            "run 'python scripts/build_capsules.py'"
        )

    projected_min = project_min_capsule_payload(actual)
    if projected_min != actual_min:
        fail(f"{min_path}: min capsules must stay a projection of the full capsule payload")

    catalog = read_json(repo_root / "generated" / "technique_catalog.json")
    capsule_alignment = [
        (entry["id"], entry["name"], entry["summary"], entry["technique_path"])
        for entry in actual["techniques"]
    ]
    catalog_alignment = [
        (entry["id"], entry["name"], entry["summary"], entry["technique_path"])
        for entry in catalog["techniques"]
    ]
    if capsule_alignment != catalog_alignment:
        fail(f"{path}: capsule entries must stay 1:1 aligned with generated/technique_catalog.json")

def validate_section_manifests(repo_root: Path, records: list[TechniqueRecord]) -> None:
    full_path = repo_root / "generated" / "technique_section_manifest.json"
    min_path = repo_root / "generated" / "technique_section_manifest.min.json"
    reader_path = repo_root / "docs" / "readers" / "source-lift" / "TECHNIQUE_SECTIONS.md"

    expected_full, expected_min = build_section_manifest_payloads(repo_root, records)
    expected_reader = build_section_reader_markdown(repo_root, records)
    actual_full = read_json(full_path)
    actual_min = read_json(min_path)
    actual_reader = read_text(reader_path)

    if actual_full != expected_full:
        fail(
            f"{full_path}: generated section manifest is out of date; "
            f"run 'python scripts/build_section_manifest.py'"
        )
    if actual_min != expected_min:
        fail(
            f"{min_path}: generated section min manifest is out of date; "
            f"run 'python scripts/build_section_manifest.py'"
        )
    if actual_reader != expected_reader:
        fail(
            f"{reader_path}: generated section reader surface is out of date; "
            "run 'python scripts/build_section_manifest.py'"
        )

    projected_min = project_min_section_manifest(actual_full)
    if projected_min != actual_min:
        fail(f"{min_path}: min section manifest must stay a projection of the full manifest")

def validate_section_surfaces(repo_root: Path, records: list[TechniqueRecord]) -> None:
    path = repo_root / "generated" / "technique_sections.full.json"
    expected = build_section_surface_payload(repo_root, records)
    actual = read_json(path)

    if actual != expected:
        fail(f"{path}: generated full sections are out of date; run 'python scripts/build_sections.py'")

    catalog = read_json(repo_root / "generated" / "technique_catalog.json")
    capsules = read_json(repo_root / "generated" / "technique_capsules.json")
    manifest = read_json(repo_root / "generated" / "technique_section_manifest.json")

    section_alignment = [
        (entry["id"], entry["name"], entry["technique_path"])
        for entry in actual["techniques"]
    ]
    catalog_alignment = [
        (entry["id"], entry["name"], entry["technique_path"])
        for entry in catalog["techniques"]
    ]
    capsule_alignment = [
        (entry["id"], entry["name"], entry["technique_path"])
        for entry in capsules["techniques"]
    ]
    if section_alignment != catalog_alignment:
        fail(f"{path}: section entries must stay 1:1 aligned with generated/technique_catalog.json")
    if section_alignment != capsule_alignment:
        fail(f"{path}: section entries must stay 1:1 aligned with generated/technique_capsules.json")

    manifest_alignment = [
        (
            entry["id"],
            entry["technique_path"],
            tuple(section["heading"] for section in entry["sections"]),
        )
        for entry in manifest["techniques"]
    ]
    surface_alignment = [
        (
            entry["id"],
            entry["technique_path"],
            tuple(section["heading"] for section in entry["sections"][: len(SECTION_LIFT_HEADINGS)]),
        )
        for entry in actual["techniques"]
    ]
    if surface_alignment != manifest_alignment:
        fail(
            f"{path}: full section surface must preserve the lifted section-map scope from "
            "generated/technique_section_manifest.json"
        )

def validate_checklist_manifests(repo_root: Path, records: list[TechniqueRecord]) -> None:
    full_path = repo_root / "generated" / "technique_checklist_manifest.json"
    min_path = repo_root / "generated" / "technique_checklist_manifest.min.json"
    reader_path = repo_root / "docs" / "readers" / "source-lift" / "TECHNIQUE_CHECKLISTS.md"

    expected_full, expected_min = build_checklist_manifest_payloads(repo_root, records)
    expected_reader = build_checklist_reader_markdown(repo_root, records)
    actual_full = read_json(full_path)
    actual_min = read_json(min_path)
    actual_reader = read_text(reader_path)

    if actual_full != expected_full:
        fail(
            f"{full_path}: generated checklist manifest is out of date; "
            f"run 'python scripts/build_checklist_manifest.py'"
        )
    if actual_min != expected_min:
        fail(
            f"{min_path}: generated checklist min manifest is out of date; "
            f"run 'python scripts/build_checklist_manifest.py'"
        )
    if actual_reader != expected_reader:
        fail(
            f"{reader_path}: generated checklist reader surface is out of date; "
            "run 'python scripts/build_checklist_manifest.py'"
        )

    projected_min = project_min_checklist_manifest(actual_full)
    if projected_min != actual_min:
        fail(f"{min_path}: min checklist manifest must stay a projection of the full manifest")

def validate_example_manifests(repo_root: Path, records: list[TechniqueRecord]) -> None:
    full_path = repo_root / "generated" / "technique_example_manifest.json"
    min_path = repo_root / "generated" / "technique_example_manifest.min.json"
    reader_path = repo_root / "docs" / "readers" / "source-lift" / "TECHNIQUE_EXAMPLES.md"

    expected_full, expected_min = build_example_manifest_payloads(repo_root, records)
    expected_reader = build_example_reader_markdown(repo_root, records)
    actual_full = read_json(full_path)
    actual_min = read_json(min_path)
    actual_reader = read_text(reader_path)

    if actual_full != expected_full:
        fail(
            f"{full_path}: generated example manifest is out of date; "
            f"run 'python scripts/build_example_manifest.py'"
        )
    if actual_min != expected_min:
        fail(
            f"{min_path}: generated example min manifest is out of date; "
            f"run 'python scripts/build_example_manifest.py'"
        )
    if actual_reader != expected_reader:
        fail(
            f"{reader_path}: generated example reader surface is out of date; "
            "run 'python scripts/build_example_manifest.py'"
        )

    projected_min = project_min_example_manifest(actual_full)
    if projected_min != actual_min:
        fail(f"{min_path}: min example manifest must stay a projection of the full manifest")

def validate_evidence_note_manifests(repo_root: Path, records: list[TechniqueRecord]) -> None:
    full_path = repo_root / "generated" / "technique_evidence_note_manifest.json"
    min_path = repo_root / "generated" / "technique_evidence_note_manifest.min.json"
    reader_path = repo_root / "docs" / "readers" / "source-lift" / "EVIDENCE_NOTE_SURFACES.md"

    expected_full, expected_min = build_evidence_note_manifest_payloads(repo_root, records)
    expected_reader = build_evidence_note_reader_markdown(repo_root, records)
    actual_full = read_json(full_path)
    actual_min = read_json(min_path)
    actual_reader = read_text(reader_path)

    if actual_full != expected_full:
        fail(
            f"{full_path}: generated evidence note manifest is out of date; "
            f"run 'python scripts/build_evidence_note_manifest.py'"
        )
    if actual_min != expected_min:
        fail(
            f"{min_path}: generated evidence note min manifest is out of date; "
            f"run 'python scripts/build_evidence_note_manifest.py'"
        )
    if actual_reader != expected_reader:
        fail(
            f"{reader_path}: generated evidence note reader surface is out of date; "
            "run 'python scripts/build_evidence_note_manifest.py'"
        )

    projected_min = project_min_evidence_note_manifest(actual_full)
    if projected_min != actual_min:
        fail(f"{min_path}: min evidence note manifest must stay a projection of the full manifest")

def validate_github_review_template_manifests(repo_root: Path) -> None:
    full_path = repo_root / "generated" / "github_review_template_manifest.json"
    min_path = repo_root / "generated" / "github_review_template_manifest.min.json"

    expected_full, expected_min = build_github_review_template_manifest_payloads(repo_root)
    actual_full = read_json(full_path)
    actual_min = read_json(min_path)

    if actual_full != expected_full:
        fail(
            f"{full_path}: generated GitHub review template manifest is out of date; "
            f"run 'python scripts/build_github_review_template_manifest.py'"
        )
    if actual_min != expected_min:
        fail(
            f"{min_path}: generated GitHub review template min manifest is out of date; "
            f"run 'python scripts/build_github_review_template_manifest.py'"
        )

    projected_min = project_min_github_review_template_manifest(actual_full)
    if projected_min != actual_min:
        fail(
            f"{min_path}: min GitHub review template manifest must stay a projection of the full manifest"
        )

def validate_semantic_review_manifests(repo_root: Path) -> None:
    full_path = repo_root / "generated" / "semantic_review_manifest.json"
    min_path = repo_root / "generated" / "semantic_review_manifest.min.json"

    expected_full, expected_min = build_semantic_review_manifest_payloads(repo_root)
    actual_full = read_json(full_path)
    actual_min = read_json(min_path)

    if actual_full != expected_full:
        fail(
            f"{full_path}: generated semantic review manifest is out of date; "
            f"run 'python scripts/build_semantic_review_manifest.py'"
        )
    if actual_min != expected_min:
        fail(
            f"{min_path}: generated semantic review min manifest is out of date; "
            f"run 'python scripts/build_semantic_review_manifest.py'"
        )

    projected_min = project_min_semantic_review_manifest(actual_full)
    if projected_min != actual_min:
        fail(f"{min_path}: min semantic review manifest must stay a projection of the full manifest")

def validate_shadow_review_manifests(repo_root: Path) -> None:
    full_path = repo_root / "generated" / "shadow_review_manifest.json"
    min_path = repo_root / "generated" / "shadow_review_manifest.min.json"

    expected_full, expected_min = build_shadow_review_manifest_payloads(repo_root)
    actual_full = read_json(full_path)
    actual_min = read_json(min_path)

    if actual_full != expected_full:
        fail(
            f"{full_path}: generated shadow review manifest is out of date; "
            f"run 'python scripts/build_shadow_review_manifest.py'"
        )
    if actual_min != expected_min:
        fail(
            f"{min_path}: generated shadow review min manifest is out of date; "
            f"run 'python scripts/build_shadow_review_manifest.py'"
        )

    projected_min = project_min_shadow_review_manifest(actual_full)
    if projected_min != actual_min:
        fail(f"{min_path}: min shadow review manifest must stay a projection of the full manifest")

def validate_repo_doc_surface_manifests(repo_root: Path) -> None:
    full_path = repo_root / "generated" / "repo_doc_surface_manifest.json"
    min_path = repo_root / "generated" / "repo_doc_surface_manifest.min.json"

    expected_full, expected_min = build_repo_doc_surface_manifest_payloads(repo_root)
    actual_full = read_json(full_path)
    actual_min = read_json(min_path)

    if actual_full != expected_full:
        fail(
            f"{full_path}: generated repo doc surface manifest is out of date; "
            f"run 'python scripts/build_repo_doc_surface_manifest.py'"
        )
    if actual_min != expected_min:
        fail(
            f"{min_path}: generated repo doc surface min manifest is out of date; "
            f"run 'python scripts/build_repo_doc_surface_manifest.py'"
        )

    projected_min = project_min_repo_doc_surface_manifest(actual_full)
    if projected_min != actual_min:
        fail(f"{min_path}: min repo doc surface manifest must stay a projection of the full manifest")

def validate_kind_manifests(repo_root: Path) -> None:
    full_path = repo_root / "generated" / "technique_kind_manifest.json"
    min_path = repo_root / "generated" / "technique_kind_manifest.min.json"
    reader_path = repo_root / "docs" / "readers" / "kind" / "TECHNIQUE_KINDS.md"
    catalog_path = repo_root / "generated" / "technique_catalog.json"

    catalog = read_json(catalog_path)
    registry = load_kind_registry(repo_root)
    expected_full, expected_min = build_kind_manifest_payloads(catalog, registry)
    expected_reader = build_kind_reader_markdown(expected_full)
    actual_full = read_json(full_path)
    actual_min = read_json(min_path)
    actual_reader = read_text(reader_path)

    if actual_full != expected_full:
        fail(
            f"{full_path}: generated kind manifest is out of date; run "
            f"'python scripts/build_kind_manifest.py'"
        )
    if actual_min != expected_min:
        fail(
            f"{min_path}: generated min kind manifest is out of date; run "
            f"'python scripts/build_kind_manifest.py'"
        )
    if actual_reader != expected_reader:
        fail(
            f"{reader_path}: generated kind reader surface is out of date; run "
            f"'python scripts/build_kind_manifest.py'"
        )

    if actual_full.get("manifest_version") != KIND_MANIFEST_VERSION:
        fail(f"{full_path}: manifest_version must be {KIND_MANIFEST_VERSION}")
    if actual_full.get("source_of_truth") != KIND_MANIFEST_SOURCE_OF_TRUTH:
        fail(f"{full_path}: source_of_truth must stay stable")
    if actual_full.get("selection_order") != list(KIND_ORDER):
        fail(f"{full_path}: selection_order must follow the registry order exactly")
    projected_min = project_min_kind_manifest(actual_full)
    if projected_min != actual_min:
        fail(f"{min_path}: min kind manifest must stay a projection of the full manifest")

    kind_entries = actual_full.get("kinds")
    if not isinstance(kind_entries, list):
        fail(f"{full_path}: kinds must be a list")
    if [entry.get("kind") for entry in kind_entries if isinstance(entry, dict)] != list(KIND_ORDER):
        fail(f"{full_path}: kinds must appear exactly once in registry selection order")

    catalog_entries = catalog["techniques"]
    for entry in kind_entries:
        if not isinstance(entry, dict):
            fail(f"{full_path}: each kind entry must be an object")
        counts = entry.get("counts")
        if not isinstance(counts, dict):
            fail(f"{full_path}: kind entry counts must be an object")
        by_domain = counts.get("by_domain")
        if not isinstance(by_domain, dict) or list(by_domain) != list(DOMAIN_ORDER):
            fail(f"{full_path}: counts.by_domain must preserve DOMAIN_ORDER exactly")

        technique_entries = entry.get("techniques")
        if not isinstance(technique_entries, list):
            fail(f"{full_path}: kind entry techniques must be a list")
        expected_entries = [
            kind_manifest_entry(catalog_entry)
            for catalog_entry in sorted(
                [catalog_entry for catalog_entry in catalog_entries if catalog_entry["kind"] == entry["kind"]],
                key=kind_group_sort_key,
            )
        ]
        if technique_entries != expected_entries:
            fail(f"{full_path}: kind entry '{entry['kind']}' must stay aligned with generated/technique_catalog.json")

def validate_selection_surface(repo_root: Path, records: list[TechniqueRecord]) -> None:
    selection_path = repo_root / "docs" / "readers" / "selection" / "TECHNIQUE_SELECTION.md"
    patterns_path = repo_root / "docs" / "readers" / "selection" / "SELECTION_PATTERNS.md"
    shadow_path = repo_root / "docs" / "readers" / "review" / "SHADOW_PATTERNS.md"
    full_path = repo_root / "generated" / "technique_catalog.json"

    validate_selection_working_set_specs(repo_root)
    validate_shadow_working_set_specs(records, repo_root)
    validate_shadow_question_specs(records)

    full_catalog = read_json(full_path)
    expected = build_selection_surface_markdown(full_catalog)
    expected_patterns = build_selection_patterns_markdown(full_catalog)
    expected_shadow = build_shadow_patterns_markdown(repo_root, records)
    actual = read_text(selection_path)
    actual_patterns = read_text(patterns_path)
    actual_shadow = read_text(shadow_path)

    if actual != expected:
        fail(
            f"{selection_path}: generated selection surface is out of date; run 'python scripts/build_catalog.py'"
        )
    if actual_patterns != expected_patterns:
        fail(
            f"{patterns_path}: generated selection patterns surface is out of date; run 'python scripts/build_catalog.py'"
        )
    if actual_shadow != expected_shadow:
        fail(
            f"{shadow_path}: generated shadow patterns surface is out of date; run 'python scripts/build_catalog.py'"
        )

def validate_repo_doc_surface_reader(repo_root: Path) -> None:
    reader_path = repo_root / "docs" / "readers" / "repo" / "REPO_DOC_SURFACES.md"
    expected = build_repo_doc_surfaces_markdown(repo_root)
    actual = read_text(reader_path)

    if actual != expected:
        fail(
            f"{reader_path}: generated repo doc surface is out of date; run "
            "'python scripts/build_repo_doc_surface_manifest.py'"
        )
