from __future__ import annotations

from .common import *
from .projection_parity import *
from .questbook import *
from .public_hygiene import *
from .source_contracts import *

def validate_repo(repo_root: Path) -> None:
    validate_stage1_files(repo_root)
    validate_selection_files(repo_root)
    validate_semantic_review_guide_files(repo_root)
    validate_kag_source_reader_files(repo_root)
    validate_capsule_surface_files(repo_root)
    validate_repo_doc_surface_files(repo_root)
    validate_kag_export_files(repo_root)
    validate_kind_doctrine_files(repo_root)
    validate_kind_data_files(repo_root)
    validate_kind_surface_files(repo_root)
    validate_kind_report_files(repo_root)
    validate_tree_report_files(repo_root)
    schema_store = load_schema_store(repo_root)
    validate_kind_axis_alignment(repo_root, schema_store)
    records = collect_techniques(repo_root, schema_store)
    validate_family_scout_alignment(repo_root)
    validate_topology_axes_registry(repo_root)
    validate_kind_overlay(repo_root, records)
    validate_selection_navigation_specs(records, repo_root)
    validate_repo_doc_navigation_specs(repo_root)
    validate_index(repo_root, records)
    validate_evidence(records)
    validate_relations(records)
    validate_catalogs(repo_root, records, schema_store)
    validate_promotion_readiness_surface(repo_root, records)
    validate_capsules(repo_root, records)
    validate_section_surfaces(repo_root, records)
    validate_section_manifests(repo_root, records)
    validate_checklist_manifests(repo_root, records)
    validate_example_manifests(repo_root, records)
    validate_evidence_note_manifests(repo_root, records)
    validate_github_review_template_manifests(repo_root)
    validate_semantic_review_manifests(repo_root)
    validate_shadow_review_manifests(repo_root)
    validate_repo_doc_surface_manifests(repo_root)
    validate_kind_manifests(repo_root)
    validate_kind_scout_reports(repo_root)
    validate_topology_scout_reports(repo_root)
    validate_tree_projection_reports(repo_root)
    validate_selection_surface(repo_root, records)
    validate_repo_doc_surface_reader(repo_root)
    validate_kag_export(repo_root, records)
    validate_technique_intelligence(repo_root, records, schema_store)
    validate_questbook_surface(repo_root)
    validate_public_hygiene(repo_root)

    canonical_count = sum(1 for record in records if record.status == "canonical")
    promoted_count = sum(1 for record in records if record.status == "promoted")
    deprecated_count = sum(1 for record in records if record.status == "deprecated")

    print(
        f"[ok] validated {len(records)} technique bundles "
        f"({canonical_count} canonical, {promoted_count} promoted, {deprecated_count} deprecated)"
    )
    print("[ok] validated TECHNIQUE_INDEX.md structure and parity")
    print("[ok] validated frontmatter kind axis, schema parity, evidence coverage, and relations")
    print("[ok] validated generated catalog parity")
    print("[ok] validated generated promotion readiness parity")
    print("[ok] validated generated capsule parity and reader surface")
    print("[ok] validated generated full section surface parity")
    print("[ok] validated generated section manifest parity and reader surface")
    print("[ok] validated generated checklist manifest parity and reader surface")
    print("[ok] validated generated example manifest parity and reader surface")
    print("[ok] validated generated evidence note manifest parity and reader surface")
    print("[ok] validated generated GitHub review template manifest parity")
    print("[ok] validated generated semantic review manifest parity")
    print("[ok] validated generated shadow review manifest parity")
    print("[ok] validated generated repo doc surface manifest parity")
    print("[ok] validated generated kind manifest parity and reader surface")
    print("[ok] validated topology scout axis registry")
    print("[ok] validated kind-overlay family scout and ambiguity audit parity")
    print("[ok] validated topology scout projection parity")
    print("[ok] validated tree projection parity")
    print("[ok] validated generated selection and shadow surface parity")
    print("[ok] validated generated repo doc surface parity")
    print("[ok] validated generated source-owned KAG export parity")
    print("[ok] validated generated Technique Intelligence registry, DAG, and reader parity")
    print("[ok] validated questbook source-proof surface")
    print("[ok] validated selection navigation specs, repo doc routing specs, review-backed working sets, shadow specs, and bounded public hygiene")


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    try:
        validate_repo(repo_root)
    except ValidationError as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
