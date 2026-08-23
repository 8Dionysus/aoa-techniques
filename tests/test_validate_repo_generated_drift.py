from __future__ import annotations

import sys
from pathlib import Path

SUPPORT_DIR = Path(__file__).resolve().parent / "support"
if str(SUPPORT_DIR) not in sys.path:
    sys.path.insert(0, str(SUPPORT_DIR))

from validate_repo_fixtures import *


class ValidateRepoGeneratedDriftTests(unittest.TestCase):
    def test_selection_surface_escapes_summary_table_cells(self) -> None:
        full_catalog = {
            "techniques": [
                {
                    "id": "AOA-T-9999",
                    "domain": "evaluation",
                    "kind": "workflow",
                    "status": "canonical",
                    "summary": "Alpha | Beta\nGamma",
                    "validation_strength": "cross_context",
                    "rigor_level": "bounded",
                    "export_ready": True,
                    "relations": [],
                    "technique_path": "techniques/evaluation/demo/TECHNIQUE.md",
                }
            ]
        }

        rendered = validate_repo.build_selection_surface_markdown(full_catalog)

        self.assertIn("Alpha \\| Beta Gamma", rendered)
        self.assertNotIn("Alpha | Beta\nGamma", rendered)

    def test_selection_working_sets_match_linked_semantic_reviews(self) -> None:
        reviews_by_path = {
            review.review_path: tuple(entry.technique_id for entry in review.map_entries)
            for review in validate_repo.parse_semantic_reviews(REPO_ROOT)
        }

        for spec in validate_repo.WORKING_SET_SPECS:
            self.assertIn(spec["review_doc"], reviews_by_path)
            self.assertEqual(tuple(spec["technique_ids"]), reviews_by_path[spec["review_doc"]])

        validate_repo.validate_selection_working_set_specs(REPO_ROOT)

    def test_selection_navigation_specs_are_structurally_valid(self) -> None:
        schema_store = validate_repo.load_schema_store(REPO_ROOT)
        records = validate_repo.collect_techniques(REPO_ROOT, schema_store)
        records_by_id = {record.id: record for record in records}
        canonical_domains = {
            record.domain for record in records if record.status == "canonical"
        }

        self.assertEqual(len(validate_repo.DOMAIN_ORDER), len(validate_repo.DOMAIN_START_SPECS))
        seen_domains: set[str] = set()
        for spec in validate_repo.DOMAIN_START_SPECS:
            domain = spec["domain"]
            self.assertNotIn(domain, seen_domains)
            seen_domains.add(domain)

            lead_ids = tuple(spec["lead_ids"])
            self.assertTrue(lead_ids)
            for technique_id in lead_ids:
                record = records_by_id[technique_id]
                if domain in canonical_domains:
                    self.assertEqual("canonical", record.status)
                else:
                    self.assertIn(record.status, {"canonical", "promoted"})
                self.assertEqual(domain, record.domain)

        self.assertEqual(set(validate_repo.DOMAIN_ORDER), seen_domains)
        self.assertEqual("canonical", records_by_id["AOA-T-0026"].status)
        self.assertEqual("canonical", records_by_id["AOA-T-0027"].status)
        self.assertEqual("canonical", records_by_id["AOA-T-0028"].status)
        self.assertEqual("canonical", records_by_id["AOA-T-0029"].status)
        self.assertEqual("canonical", records_by_id["AOA-T-0030"].status)
        self.assertEqual("canonical", records_by_id["AOA-T-0031"].status)
        self.assertEqual("promoted", records_by_id["AOA-T-0032"].status)

        domain_start_targets = {
            spec["domain"]: tuple(spec["lead_ids"])[0] for spec in validate_repo.DOMAIN_START_SPECS
        }
        for spec in validate_repo.COMMON_MOVE_SPECS:
            target = records_by_id[spec["target_id"]]
            self.assertEqual("canonical", target.status)

            if spec["basis_type"] == validate_repo.COMMON_MOVE_BASIS_DIRECT_RELATION:
                self.assertTrue(spec.get("anchor_ids"))
                for anchor_id in spec["anchor_ids"]:
                    anchor = records_by_id[anchor_id]
                    direct_relation_found = any(
                        relation["target"] == spec["target_id"]
                        for relation in anchor.frontmatter["relations"]
                    ) or any(
                        relation["target"] == anchor_id
                        for relation in target.frontmatter["relations"]
                    )
                    self.assertTrue(direct_relation_found)
                continue

            self.assertEqual(
                validate_repo.COMMON_MOVE_BASIS_DOMAIN_START,
                spec["basis_type"],
            )
            self.assertEqual(
                domain_start_targets[spec["domain"]],
                spec["target_id"],
            )

        validate_repo.validate_selection_navigation_specs(records, REPO_ROOT)

    def test_shadow_specs_are_structurally_valid(self) -> None:
        schema_store = validate_repo.load_schema_store(REPO_ROOT)
        records = validate_repo.collect_techniques(REPO_ROOT, schema_store)
        records_by_id = {record.id: record for record in records}
        shadow_targets = {
            technique_id
            for spec in validate_repo.SHADOW_WORKING_SET_SPECS
            for technique_id in spec["technique_ids"]
        }

        validate_repo.validate_shadow_working_set_specs(records, REPO_ROOT)
        validate_repo.validate_shadow_question_specs(records)

        for spec in validate_repo.SHADOW_WORKING_SET_SPECS:
            self.assertTrue(spec["technique_ids"])
            self.assertTrue((REPO_ROOT / spec["review_doc"]).is_file())
            for technique_id in spec["technique_ids"]:
                record = records_by_id[technique_id]
                self.assertEqual("canonical", record.status)
                self.assertIn(
                    "adverse_effects_review",
                    {note.kind for note in record.notes},
                )

        for spec in validate_repo.SHADOW_COMMON_QUESTION_SPECS:
            record = records_by_id[spec["target_id"]]
            self.assertEqual("canonical", record.status)
            self.assertIn(spec["target_id"], shadow_targets)

    def test_shadow_working_sets_match_linked_shadow_reviews(self) -> None:
        schema_store = validate_repo.load_schema_store(REPO_ROOT)
        records = validate_repo.collect_techniques(REPO_ROOT, schema_store)
        reviews_by_path = {
            review.review_path: tuple(entry.technique_id for entry in review.map_entries)
            for review in validate_repo.parse_shadow_reviews(REPO_ROOT)
        }

        for spec in validate_repo.SHADOW_WORKING_SET_SPECS:
            self.assertIn(spec["review_doc"], reviews_by_path)
            self.assertEqual(tuple(spec["technique_ids"]), reviews_by_path[spec["review_doc"]])

        validate_repo.validate_shadow_working_set_specs(records, REPO_ROOT)

    def test_kind_manifest_matches_builder_projection_and_order(self) -> None:
        catalog = validate_repo.read_json(REPO_ROOT / "generated" / "technique_catalog.json")
        registry = validate_repo.load_kind_registry(REPO_ROOT)
        manifest = validate_repo.read_json(REPO_ROOT / "generated" / "technique_kind_manifest.json")
        min_manifest = validate_repo.read_json(
            REPO_ROOT / "generated" / "technique_kind_manifest.min.json"
        )
        reader = (
            REPO_ROOT / "docs" / "readers" / "kind" / "TECHNIQUE_KINDS.md"
        ).read_text(encoding="utf-8")

        expected_full, expected_min = validate_repo.build_kind_manifest_payloads(catalog, registry)

        self.assertEqual(expected_full, manifest)
        self.assertEqual(expected_min, min_manifest)
        self.assertEqual(validate_repo.build_kind_reader_markdown(expected_full), reader)
        self.assertEqual(list(validate_repo.KIND_ORDER), manifest["selection_order"])
        self.assertEqual(
            list(validate_repo.KIND_ORDER),
            [entry["kind"] for entry in manifest["kinds"]],
        )
        self.assertEqual(
            validate_repo.project_min_kind_manifest(manifest),
            min_manifest,
        )

    def test_kind_manifest_counts_and_catalog_alignment_stay_exact(self) -> None:
        catalog = validate_repo.read_json(REPO_ROOT / "generated" / "technique_catalog.json")
        manifest = validate_repo.read_json(REPO_ROOT / "generated" / "technique_kind_manifest.json")
        catalog_entries = catalog["techniques"]

        for kind_entry in manifest["kinds"]:
            kind = kind_entry["kind"]
            expected_entries = [
                entry
                for entry in sorted(catalog_entries, key=validate_repo.kind_group_sort_key)
                if entry["kind"] == kind
            ]
            expected_ids = [entry["id"] for entry in expected_entries]
            manifest_ids = [entry["id"] for entry in kind_entry["techniques"]]
            counts = kind_entry["counts"]

            self.assertEqual(expected_ids, manifest_ids)
            self.assertEqual(len(expected_entries), counts["total"])
            self.assertEqual(
                sum(1 for entry in expected_entries if entry["status"] == "canonical"),
                counts["canonical"],
            )
            self.assertEqual(
                sum(1 for entry in expected_entries if entry["status"] == "promoted"),
                counts["promoted"],
            )
            self.assertEqual(
                {domain: sum(1 for entry in expected_entries if entry["domain"] == domain) for domain in validate_repo.DOMAIN_ORDER},
                counts["by_domain"],
            )

    def test_docs_boundary_next_step_matches_generated_semantic_manifest(self) -> None:
        expected_phrase = "validator-synchronized with authored semantic reviews"
        review_path = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "semantic"
            / "DOCS_BOUNDARY_SEMANTIC_REVIEW.md"
        )
        review_content = review_path.read_text(encoding="utf-8")
        manifest = validate_repo.read_json(REPO_ROOT / "generated" / "semantic_review_manifest.json")
        manifest_entry = next(
            review
            for review in manifest["reviews"]
            if review["review_path"] == "mechanics/distillation/parts/technique-reform-ingress/reviews/semantic/DOCS_BOUNDARY_SEMANTIC_REVIEW.md"
        )

        self.assertIn(expected_phrase, review_content)
        self.assertIn(expected_phrase, manifest_entry["next_step_markdown"])

    def test_semantic_review_next_steps_match_generated_manifest(self) -> None:
        expected_phrases = {
            "mechanics/distillation/parts/technique-reform-ingress/reviews/semantic/AGENT_WORKFLOWS_CORE_SEMANTIC_REVIEW.md": "keep this review as the canonical-core anchor",
            "mechanics/distillation/parts/technique-reform-ingress/reviews/semantic/PUBLISHED_SUMMARY_SEMANTIC_REVIEW.md": "open a new pilot only if future wording starts collapsing rendering policy back into the published-summary package",
            "mechanics/distillation/parts/technique-reform-ingress/reviews/semantic/EVALUATION_CHAIN_SEMANTIC_REVIEW.md": "open a new pilot only if storage-layout detail starts crowding out rollout semantics",
            "mechanics/distillation/parts/technique-reform-ingress/reviews/semantic/INSTRUCTION_SURFACE_SEMANTIC_REVIEW.md": "The next instruction-surface closure pressure should therefore stay on `AOA-T-0035`",
            "mechanics/distillation/parts/technique-reform-ingress/reviews/semantic/SKILL_SUPPORT_SEMANTIC_REVIEW.md": "keep this review focused on monitoring the documented watch seams around `AOA-T-0015` vs `AOA-T-0017`",
            "mechanics/distillation/parts/technique-reform-ingress/reviews/semantic/KAG_SOURCE_LIFT_SEMANTIC_REVIEW.md": "keep `AOA-T-0019` narrow as the canonical metadata spine",
        }
        manifest = validate_repo.read_json(REPO_ROOT / "generated" / "semantic_review_manifest.json")
        reviews_by_path = {review["review_path"]: review for review in manifest["reviews"]}

        for review_path, expected_phrase in expected_phrases.items():
            with self.subTest(review_path=review_path):
                review_content = (REPO_ROOT / review_path).read_text(encoding="utf-8")
                self.assertIn(expected_phrase, review_content)
                self.assertIn(expected_phrase, reviews_by_path[review_path]["next_step_markdown"])

    def test_selection_patterns_describes_validator_backed_navigation(self) -> None:
        selection_patterns = (
            REPO_ROOT / "docs" / "readers" / "selection" / "SELECTION_PATTERNS.md"
        ).read_text(encoding="utf-8")

        self.assertIn(
            "validator-backed navigation specs, and review-backed working sets",
            selection_patterns,
        )
        self.assertIn(
            "validator-backed starting points and common moves",
            selection_patterns,
        )
        self.assertIn(
            "| I need doc-role separation | [AOA-T-0002]",
            selection_patterns,
        )
        self.assertIn(
            "| I need strict-vs-optional rendering policy | [AOA-T-0011]",
            selection_patterns,
        )
        self.assertIn("START_HERE.md", selection_patterns)
        self.assertIn("Agent-workflows canonical core", selection_patterns)
        self.assertIn("AGENT_WORKFLOWS_CORE_SEMANTIC_REVIEW.md", selection_patterns)
        self.assertIn("KAG/source-lift family", selection_patterns)
        self.assertIn("KAG_SOURCE_LIFT_SEMANTIC_REVIEW.md", selection_patterns)

    def test_shadow_patterns_generated_surface_matches_builder_and_stays_canonical_only(
        self,
    ) -> None:
        schema_store = validate_repo.load_schema_store(REPO_ROOT)
        records = validate_repo.collect_techniques(REPO_ROOT, schema_store)
        shadow_patterns = (
            REPO_ROOT / "docs" / "readers" / "review" / "SHADOW_PATTERNS.md"
        ).read_text(encoding="utf-8")

        self.assertEqual(
            validate_repo.build_shadow_patterns_markdown(REPO_ROOT, records),
            shadow_patterns,
        )
        self.assertIn("Published-summary shadow cluster", shadow_patterns)
        self.assertIn("PUBLISHED_SUMMARY_SHADOW_REVIEW.md", shadow_patterns)
        self.assertIn("validator-backed prompts", shadow_patterns)
        self.assertIn("Evaluation-chain shadow pair", shadow_patterns)
        self.assertIn("EVALUATION_CHAIN_SHADOW_REVIEW.md", shadow_patterns)
        self.assertIn("AOA-T-0003", shadow_patterns)
        self.assertIn("AOA-T-0007", shadow_patterns)
        self.assertIn("AOA-T-0006", shadow_patterns)
        self.assertIn("AOA-T-0008", shadow_patterns)
        self.assertIn("AOA-T-0010", shadow_patterns)
        self.assertIn("AOA-T-0011", shadow_patterns)
        self.assertNotIn("AOA-T-0014", shadow_patterns)
        self.assertNotIn("AOA-T-0022", shadow_patterns)

    def test_shadow_patterns_describes_current_shadow_questions(self) -> None:
        shadow_patterns = (
            REPO_ROOT / "docs" / "readers" / "review" / "SHADOW_PATTERNS.md"
        ).read_text(encoding="utf-8")

        self.assertIn(
            "| I need to check whether the latest summary looks clean while history trust is already broken | [AOA-T-0006]",
            shadow_patterns,
        )
        self.assertIn(
            "| I need to stop remediation output from drifting into integrity or rendering policy | [AOA-T-0008]",
            shadow_patterns,
        )
        self.assertIn(
            "| I need to keep a diagnostic helper from turning into an implicit enforcement gate | [AOA-T-0010]",
            shadow_patterns,
        )
        self.assertIn(
            "| I need optional-source warnings to stay visible without becoming noisy or package-shaped | [AOA-T-0011]",
            shadow_patterns,
        )
        self.assertIn(
            "| I need a summary producer to stay diagnostic instead of collapsing back into log scraping | [AOA-T-0003]",
            shadow_patterns,
        )
        self.assertIn(
            "| I need staged enforcement to stay narrow instead of leaking into hidden strictness | [AOA-T-0007]",
            shadow_patterns,
        )

    def test_shadow_review_manifest_generated_surface_matches_builder(self) -> None:
        expected_full, expected_min = validate_repo.build_shadow_review_manifest_payloads(REPO_ROOT)
        actual_full = validate_repo.read_json(REPO_ROOT / "generated" / "shadow_review_manifest.json")
        actual_min = validate_repo.read_json(REPO_ROOT / "generated" / "shadow_review_manifest.min.json")

        self.assertEqual(expected_full, actual_full)
        self.assertEqual(expected_min, actual_min)
        self.assertEqual(
            validate_repo.project_min_shadow_review_manifest(actual_full),
            actual_min,
        )

    def test_repo_doc_surface_top_level_sections_are_stable(self) -> None:
        surfaces_by_path = {
            surface.doc_path: surface for surface in validate_repo.parse_repo_doc_surfaces(REPO_ROOT)
        }

        self.assertEqual(
            (
                "What This Repository Does",
                "Start Here",
                "Route Modes",
                "Technique Check",
                "Current Contour",
                "Practice Mechanics",
                "Technical Districts",
                "Machine Companions",
                "Working Rule",
            ),
            surfaces_by_path["README.md"].top_level_sections,
        )
        self.assertEqual(
            (
                "Purpose",
                "Authority Boundary",
                "Mission",
                "What This Repository Owns",
                "Routed To Stronger Owners",
                "Canon Discipline",
                "Review Rule",
            ),
            surfaces_by_path["CHARTER.md"].top_level_sections,
        )
        self.assertEqual(
            (
                "Root Principle",
                "Docs-Root Principle",
                "Allowed Root Surfaces",
                "Surfaces That Should Not Live In Root",
                "Decision Procedure Before Adding A Root File",
                "Current Root Decisions",
                "Final Rule",
            ),
            surfaces_by_path["docs/ROOT_SURFACE_LAW.md"].top_level_sections,
        )

        self.assertEqual(
            (
                "Core Contract",
                "Standalone Portability Target",
                "Small-Agent Target",
                "Scale Target",
                "Not A Skill",
                "Authoring Checks",
                "Distillation Rule",
                "Template And Capsule Implication",
                "Review Outcome",
            ),
            surfaces_by_path["docs/TECHNIQUE_ATOM_CONTRACT.md"].top_level_sections,
        )
        self.assertEqual(
            (
                "Purpose",
                "Topology Law",
                "Axis Stack",
                "Current Axes",
                "Future Axes",
                "Relation Topology",
                "Growth Rules",
                "Mechanics Interface",
                "Next Honest Build Path",
            ),
            surfaces_by_path["docs/TECHNIQUE_TOPOLOGY_CONTRACT.md"].top_level_sections,
        )
        self.assertEqual(
            (
                "Purpose",
                "Tree Law",
                "Tree Stack",
                "Current Trunks",
                "Tree Versus Facets",
                "Path Change Rules",
                "Leaf Bundle Rules",
                "Generated Projection Path",
                "Stop Lines",
                "Current Closeout",
                "Next Honest Build Path",
            ),
            surfaces_by_path["docs/TECHNIQUE_TREE_CONTRACT.md"].top_level_sections,
        )
        self.assertEqual(
            (
                "Authority",
                "Update Rule",
                "Current Direction",
                "Current Checked Contour",
                "Horizon: Root Clarity",
                "Horizon: Technique Atom",
                "Horizon: Corpus Topology",
                "Horizon: Corpus Tree",
                "Horizon: Small-Agent Usability",
                "Horizon: Mechanics To Canon",
                "Horizon: Evidence And Promotion",
                "Horizon: Standalone Portability",
                "Horizon: Generated Companions",
                "When The Time Comes",
                "Standing Direction",
            ),
            surfaces_by_path["ROADMAP.md"].top_level_sections,
        )
        self.assertEqual(
            (
                "Update trigger",
                "Frontier",
                "Near",
                "Latent / parked",
                "Harvest candidates",
                "Backing files",
                "Rule",
            ),
            surfaces_by_path["QUESTBOOK.md"].top_level_sections,
        )
        self.assertEqual(
            (
                "What This Repo Is",
                "If You Need One Technique Now",
                "If You Need To Understand Maturity And Review",
                "If You Need Derived Surfaces",
                "Current Corpus Posture",
                "Repo-Only Operating Contract",
                "When To Leave This Repo",
                "Release And Validation",
            ),
            surfaces_by_path["docs/START_HERE.md"].top_level_sections,
        )
        self.assertEqual(
            (
                "Why This Repo Exists",
                "Ontology Spine Inheritance",
                "Method And Neighboring Layers",
                "Boundary Reminder",
            ),
            surfaces_by_path["docs/ECOSYSTEM_CONTEXT.md"].top_level_sections,
        )
        self.assertEqual(
            (
                "Start Here",
                "Root Docs",
                "Districts",
                "Reader Routes",
                "Lift Anchors",
                "Claim Routes",
                "Change Routes",
                "Recommended Reading Paths",
                "Adjacent Routes",
                "Notes",
            ),
            surfaces_by_path["docs/README.md"].top_level_sections,
        )
        self.assertEqual(
            (
                "[Unreleased]",
                "[0.6.2] - 2026-08-23",
                "[0.6.1] - 2026-08-23",
                "[0.6.0] - 2026-08-22",
                "[0.5.0] - 2026-07-13",
                "[0.4.5] - 2026-05-18",
                "[0.4.2] - 2026-04-23",
                "[0.4.1] - 2026-04-19",
                "[0.4.0] - 2026-04-10",
                "[0.3.0] - 2026-04-01",
                "[0.2.0] - 2026-03-23",
                "[0.1.0] - 2026-03-17",
            ),
            surfaces_by_path["CHANGELOG.md"].top_level_sections,
        )

    def test_repo_doc_surface_manifest_generated_surface_matches_builder(self) -> None:
        validate_repo.validate_repo_doc_surface_manifests(REPO_ROOT)
        expected_full, expected_min = validate_repo.build_repo_doc_surface_manifest_payloads(
            REPO_ROOT
        )
        actual_full = validate_repo.read_json(
            REPO_ROOT / "generated" / "repo_doc_surface_manifest.json"
        )
        actual_min = validate_repo.read_json(
            REPO_ROOT / "generated" / "repo_doc_surface_manifest.min.json"
        )

        self.assertEqual(expected_full, actual_full)
        self.assertEqual(expected_min, actual_min)
        self.assertEqual(
            validate_repo.project_min_repo_doc_surface_manifest(actual_full),
            actual_min,
        )
        self.assertEqual(
            list(validate_repo.REPO_DOC_SURFACE_GROUP_ORDER),
            [group["group"] for group in actual_full["surface_groups"]],
        )
        self.assertEqual(20, len(actual_full["docs"]))
        docs_by_id = {doc["doc_id"]: doc for doc in actual_full["docs"]}
        self.assertEqual("entrypoint/map", docs_by_id["ecosystem_context"]["surface_group"])
        self.assertEqual("canon/authority", docs_by_id["charter"]["surface_group"])
        self.assertEqual("status/release", docs_by_id["roadmap"]["surface_group"])

    def test_repo_doc_surfaces_generated_reader_matches_builder_and_stays_bounded(self) -> None:
        validate_repo.validate_repo_doc_surface_reader(REPO_ROOT)
        repo_doc_surfaces = (
            REPO_ROOT / "docs" / "readers" / "repo" / "REPO_DOC_SURFACES.md"
        ).read_text(encoding="utf-8")

        self.assertEqual(
            validate_repo.build_repo_doc_surfaces_markdown(REPO_ROOT),
            repo_doc_surfaces,
        )
        self.assertIn("Entrypoint / Map", repo_doc_surfaces)
        self.assertIn("Canon / Authority", repo_doc_surfaces)
        self.assertIn("Contribution / Policy", repo_doc_surfaces)
        self.assertNotIn("Walkthrough / Context", repo_doc_surfaces)
        self.assertIn("Status / Release", repo_doc_surfaces)
        self.assertIn("README.md", repo_doc_surfaces)
        self.assertIn("CHARTER.md", repo_doc_surfaces)
        self.assertIn("docs/START_HERE.md", repo_doc_surfaces)
        self.assertIn("docs/ROOT_SURFACE_LAW.md", repo_doc_surfaces)
        self.assertIn("ROADMAP.md", repo_doc_surfaces)
        self.assertIn("QUESTBOOK.md", repo_doc_surfaces)
        self.assertIn("docs/RELEASING.md", repo_doc_surfaces)
        self.assertIn("repo_doc_surface_manifest.json", repo_doc_surfaces)
        self.assertNotIn("](../TODO.md)", repo_doc_surfaces)
        self.assertNotIn("](../PLANS.md)", repo_doc_surfaces)
        self.assertNotIn("PUBLISHED_SUMMARY_SHADOW_REVIEW.md", repo_doc_surfaces)

    def test_repo_doc_surfaces_are_discoverable_from_docs_root_changelog_kag_and_release_docs(
        self,
    ) -> None:
        docs_readme = (REPO_ROOT / "docs" / "README.md").read_text(encoding="utf-8")
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        kag_source_guide = (
            REPO_ROOT / "docs" / "source-lift" / "KAG_SOURCE_LIFT_GUIDE.md"
        ).read_text(encoding="utf-8")
        review_readme = (REPO_ROOT / "docs" / "review" / "README.md").read_text(
            encoding="utf-8"
        )
        releasing = (REPO_ROOT / "docs" / "RELEASING.md").read_text(encoding="utf-8")

        self.assertIn("START_HERE.md", docs_readme)
        self.assertIn("ECOSYSTEM_CONTEXT.md", docs_readme)
        self.assertIn("docs/START_HERE.md", readme)
        self.assertIn("docs/ECOSYSTEM_CONTEXT.md", readme)
        self.assertIn("docs/START_HERE.md", changelog)
        self.assertIn("START_HERE.md", kag_source_guide)
        self.assertIn("START_HERE.md", releasing)
        self.assertIn("REPO_DOC_SURFACES.md", docs_readme)
        self.assertIn("repo_doc_surface_manifest.json", docs_readme)
        self.assertIn("20 authoritative public route/canon/status files", docs_readme)
        self.assertIn("REPO_DOC_SURFACE_LIFT_GUIDE.md", docs_readme)
        self.assertIn("review packet route", docs_readme)
        self.assertIn("Distillation Review Packet Atlas", review_readme)
        self.assertIn("KAG_SOURCE_LIFT_SEMANTIC_REVIEW.md", kag_source_guide)
        self.assertIn("docs/readers/repo/REPO_DOC_SURFACES.md", readme)
        self.assertIn("generated/repo_doc_surface_manifest.min.json", readme)
        self.assertIn("REPO_DOC_SURFACES.md", changelog)
        self.assertIn("repo_doc_surface_manifest.json", changelog)
        self.assertIn("REPO_DOC_SURFACE_LIFT_GUIDE.md", changelog)
        self.assertIn("repo_doc_surface_manifest.json", kag_source_guide)
        self.assertIn("REPO_DOC_SURFACE_LIFT_GUIDE.md", kag_source_guide)
        self.assertIn("REPO_DOC_SURFACES.md", kag_source_guide)
        self.assertIn("`release` lane", releasing)
        self.assertIn("`generated` lane, `catalog` group", releasing)
        self.assertIn("`generated` lane, `kag_export` group", releasing)
        self.assertIn("Shadow review", releasing)

    def test_topology_scout_axis_registry_stays_below_frontmatter_truth(self) -> None:
        registry = validate_repo.load_topology_axes_registry(REPO_ROOT)
        registry_text = (REPO_ROOT / validate_repo.TECHNIQUE_TOPOLOGY_AXES_PATH).read_text(
            encoding="utf-8"
        )
        start_here = (REPO_ROOT / "docs" / "START_HERE.md").read_text(
            encoding="utf-8"
        )
        roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        decision = (
            REPO_ROOT
            / "docs"
            / "decisions"
            / "AOA-TECH-D-0042-topology-scout-axis-registry.md"
        ).read_text(encoding="utf-8")

        validate_repo.validate_topology_axes_registry(REPO_ROOT)
        self.assertEqual("technique_topology_scout_axes", registry["axis_name"])
        self.assertEqual("scout-foundation", registry["status"])
        self.assertEqual(["domain", "kind"], registry["frontmatter_truth_axes"])
        self.assertIn(
            "does not add required frontmatter fields",
            registry["authority_note"],
        )
        self.assertIn(
            "must not remap bundle meaning automatically",
            registry["authority_note"],
        )

        axes = {axis["id"]: axis for axis in registry["axes"]}
        self.assertEqual(set(validate_repo.TOPOLOGY_SCOUT_AXIS_ORDER), set(axes))
        self.assertEqual("exactly-one", axes["execution_profile"]["cardinality"])
        for axis_id in ("capability_class", "substrate", "risk_posture"):
            self.assertEqual("one-or-more", axes[axis_id]["cardinality"])

        self.assertIn("small-agent", [value["id"] for value in axes["execution_profile"]["values"]])
        self.assertIn("public-share", [value["id"] for value in axes["risk_posture"]["values"]])
        self.assertIn("human-approval-surfaces", [value["id"] for value in axes["substrate"]["values"]])
        self.assertIn("learn-from-artifact", [value["id"] for value in axes["capability_class"]["values"]])

        self.assertIn("not frontmatter truth", start_here)
        self.assertIn("mechanics/distillation/parts/technique-reform-ingress/config/technique_topology_axes.yaml", roadmap)
        self.assertIn("not add required frontmatter fields", registry_text)
        self.assertIn("below bundle frontmatter", decision)

    def test_topology_scout_report_is_builder_aligned_and_non_authoritative(self) -> None:
        catalog = validate_repo.read_json(REPO_ROOT / "generated" / "technique_catalog.json")
        axis_registry = validate_repo.load_topology_axes_registry(REPO_ROOT)
        kind_overlay = validate_repo.load_kind_overlay(REPO_ROOT)
        report = validate_repo.read_json(REPO_ROOT / validate_repo.TECHNIQUE_REFORM_REPORTS_DIR / "technique_topology_scout.json")
        report_markdown = (
            REPO_ROOT / validate_repo.TECHNIQUE_REFORM_REPORTS_DIR / "technique_topology_scout.md"
        ).read_text(encoding="utf-8")

        expected_report = validate_repo.build_topology_scout_payload(
            catalog, axis_registry, kind_overlay
        )
        expected_markdown = validate_repo.build_topology_scout_markdown(expected_report)

        self.assertEqual(expected_report, report)
        self.assertEqual(expected_markdown, report_markdown)
        self.assertEqual("scout-only-non-authoritative", report["status"])
        self.assertEqual(validate_repo.TOPOLOGY_SCOUT_AUTHORITY_NOTE, report["authority_note"])
        self.assertEqual(["domain", "kind"], report["frontmatter_truth_axes"])
        self.assertEqual(list(validate_repo.TOPOLOGY_SCOUT_AXIS_ORDER), report["axis_order"])
        self.assertEqual(107, len(report["techniques"]))
        self.assertIn("non-authoritative", report_markdown)
        self.assertIn("bundle frontmatter remains stronger", report_markdown)
        for axis in validate_repo.TOPOLOGY_SCOUT_AXIS_ORDER:
            self.assertIn(axis, report["axis_value_counts"])

    def test_tree_projection_report_is_builder_aligned_and_non_authoritative(self) -> None:
        catalog = validate_repo.read_json(REPO_ROOT / "generated" / "technique_catalog.json")
        kind_overlay = validate_repo.load_kind_overlay(REPO_ROOT)
        report = validate_repo.read_json(REPO_ROOT / validate_repo.TECHNIQUE_REFORM_REPORTS_DIR / "technique_tree_projection.json")
        report_markdown = (
            REPO_ROOT / validate_repo.TECHNIQUE_REFORM_REPORTS_DIR / "technique_tree_projection.md"
        ).read_text(encoding="utf-8")

        expected_report = validate_repo.build_tree_projection_payload(catalog, kind_overlay)
        expected_markdown = validate_repo.build_tree_projection_markdown(expected_report)

        self.assertEqual(expected_report, report)
        self.assertEqual(expected_markdown, report_markdown)
        self.assertEqual("projection-only-non-authoritative", report["status"])
        self.assertEqual(validate_repo.TREE_PROJECTION_AUTHORITY_NOTE, report["authority_note"])
        self.assertEqual(["domain", "kind"], report["frontmatter_truth_axes"])
        self.assertEqual(
            validate_repo.TREE_PROJECTION_TARGET_PATH_SHAPE,
            report["target_path_shape"],
        )
        self.assertEqual(107, len(report["techniques"]))
        self.assertIn("non-authoritative", report_markdown)
        self.assertIn("not source truth for bundle meaning", report_markdown)
        self.assertIn("pilot-candidate", report["review_status_counts"])
        self.assertIn("split-review-needed", report["review_status_counts"])
        self.assertIn("singleton-hold", report["review_status_counts"])
        self.assertEqual(
            "candidate",
            next(
                entry
                for entry in report["techniques"]
                if entry["id"] == "AOA-T-0089"
            )["review_status"],
        )
        self.assertEqual(
            "techniques/governance/promotion-boundary/quest-unit-promotion-review/TECHNIQUE.md",
            next(
                entry
                for entry in report["techniques"]
                if entry["id"] == "AOA-T-0089"
            )["proposed_future_path"],
        )
        self.assertEqual(
            "techniques/governance/automation-readiness/automation-fit-matrix/TECHNIQUE.md",
            next(
                entry
                for entry in report["techniques"]
                if entry["id"] == "AOA-T-0086"
            )["proposed_future_path"],
        )
        self.assertEqual(
            "candidate",
            next(
                entry
                for entry in report["techniques"]
                if entry["id"] == "AOA-T-0101"
            )["review_status"],
        )
        self.assertEqual(
            "techniques/governance/practice-adoption-lifecycle/local-pattern-adoption-gate/TECHNIQUE.md",
            next(
                entry
                for entry in report["techniques"]
                if entry["id"] == "AOA-T-0101"
            )["proposed_future_path"],
        )
        tool_gateway_entry = next(
            entry
            for entry in report["techniques"]
            if entry["family"] == "tool-gateway"
        )
        self.assertEqual("candidate", tool_gateway_entry["review_status"])
        self.assertEqual(
            "techniques/tool-use/tool-gateway/mcp-gateway-proxy/TECHNIQUE.md",
            tool_gateway_entry["proposed_future_path"],
        )

    def test_section_reader_generated_surface_matches_builder_and_preserves_scope_order(
        self,
    ) -> None:
        schema_store = validate_repo.load_schema_store(REPO_ROOT)
        records = validate_repo.collect_techniques(REPO_ROOT, schema_store)
        rendered = (
            REPO_ROOT / "docs" / "readers" / "source-lift" / "TECHNIQUE_SECTIONS.md"
        ).read_text(encoding="utf-8")

        validate_repo.validate_section_manifests(REPO_ROOT, records)
        self.assertEqual(validate_repo.build_section_reader_markdown(REPO_ROOT, records), rendered)
        self.assertEqual(
            validate_repo.SECTION_LIFT_HEADINGS,
            tuple(re.findall(r"^## `(.+?)`$", rendered, flags=re.MULTILINE)),
        )
        self.assertIn("## Section Scope", rendered)
        when_to_use_block = rendered.split("## `When to use`", 1)[1].split("\n## `", 1)[0]
        self.assertIn("AOA-T-0016", when_to_use_block)
        self.assertNotIn("| `4` |", when_to_use_block)
        self.assertIn("| `2` |", when_to_use_block)
        self.assertNotIn(
            "Reduce unsafe, opaque, or non-reviewable agent changes by requiring a visible workflow before and after apply.",
            rendered,
        )
        self.assertNotIn("## `Public sanitization notes`", rendered)

    def test_full_section_surface_matches_builder_and_stays_aligned(self) -> None:
        schema_store = validate_repo.load_schema_store(REPO_ROOT)
        records = validate_repo.collect_techniques(REPO_ROOT, schema_store)
        actual = validate_repo.read_json(REPO_ROOT / "generated" / "technique_sections.full.json")
        expected = validate_repo.build_section_surface_payload(REPO_ROOT, records)

        validate_repo.validate_section_surfaces(REPO_ROOT, records)
        self.assertEqual(expected, actual)
        self.assertEqual(1, actual["section_version"])
        self.assertEqual(
            list(validate_repo.REQUIRED_SECTIONS),
            actual["source_of_truth"]["sections"],
        )
        first_entry = actual["techniques"][0]
        self.assertEqual(
            tuple(validate_repo.SECTION_KEY_BY_HEADING[heading] for heading in validate_repo.REQUIRED_SECTIONS),
            tuple(section["key"] for section in first_entry["sections"]),
        )

    def test_section_manifest_remains_map_while_full_section_surface_carries_payload(self) -> None:
        manifest = validate_repo.read_json(REPO_ROOT / "generated" / "technique_section_manifest.json")
        full_sections = validate_repo.read_json(REPO_ROOT / "generated" / "technique_sections.full.json")

        self.assertEqual(list(validate_repo.SECTION_LIFT_HEADINGS), manifest["section_scope"])
        self.assertEqual(10, len(manifest["techniques"][0]["sections"]))
        self.assertEqual(len(validate_repo.REQUIRED_SECTIONS), len(full_sections["techniques"][0]["sections"]))
        self.assertEqual(
            {"heading", "order", "markdown"},
            set(manifest["techniques"][0]["sections"][0]),
        )
        self.assertEqual(
            {"key", "heading", "content_markdown"},
            set(full_sections["techniques"][0]["sections"][0]),
        )

    def test_checklist_reader_generated_surface_matches_builder_and_stays_ordered(self) -> None:
        schema_store = validate_repo.load_schema_store(REPO_ROOT)
        records = validate_repo.collect_techniques(REPO_ROOT, schema_store)
        rendered = (
            REPO_ROOT / "docs" / "readers" / "source-lift" / "TECHNIQUE_CHECKLISTS.md"
        ).read_text(encoding="utf-8")

        validate_repo.validate_checklist_manifests(REPO_ROOT, records)
        self.assertEqual(validate_repo.build_checklist_reader_markdown(REPO_ROOT, records), rendered)
        self.assertIn("| checklist | intro | items | check path | source |", rendered)

        domain_positions = [rendered.index(f"## `{domain}`") for domain in validate_repo.DOMAIN_ORDER]
        self.assertEqual(sorted(domain_positions), domain_positions)

        for domain in validate_repo.DOMAIN_ORDER:
            ordered_records = sorted(
                [record for record in records if record.domain == domain],
                key=validate_repo.record_sort_key,
            )
            heading_positions = [
                rendered.index(
                    f"### {validate_repo.record_technique_link(REPO_ROOT, record, validate_repo.SOURCE_LIFT_READER_ROOT_PREFIX)} - {record.name} (`{record.status}`)"
                )
                for record in ordered_records
            ]
            self.assertEqual(sorted(heading_positions), heading_positions)

    def test_checklist_reader_builder_supports_multiple_checklists_per_technique(self) -> None:
        technique_dir = REPO_ROOT / "techniques" / "demo"
        record = validate_repo.TechniqueRecord(
            technique_dir=technique_dir,
            technique_path=technique_dir / "TECHNIQUE.md",
            id="AOA-T-9999",
            name="demo-technique",
            domain="docs",
            kind="artifact",
            status="promoted",
            summary="demo",
            frontmatter={},
            body="",
            sections=(),
            checklists=(
                validate_repo.TechniqueChecklist(
                    check_path="techniques/demo/checks/first.md",
                    title="First Checklist",
                    intro_markdown="short intro",
                    items=(validate_repo.ChecklistItem(text="one"),),
                ),
                validate_repo.TechniqueChecklist(
                    check_path="techniques/demo/checks/second.md",
                    title="Second Checklist",
                    intro_markdown="",
                    items=(
                        validate_repo.ChecklistItem(text="one"),
                        validate_repo.ChecklistItem(text="two"),
                    ),
                ),
            ),
            examples=(),
            notes=(),
        )

        rendered = validate_repo.build_checklist_reader_markdown(REPO_ROOT, [record])

        self.assertIn("First Checklist", rendered)
        self.assertIn("Second Checklist", rendered)
        self.assertIn("`present`", rendered)
        self.assertIn("`absent`", rendered)
        self.assertIn("`1`", rendered)
        self.assertIn("`2`", rendered)

    def test_example_reader_generated_surface_matches_builder_and_stays_bounded(self) -> None:
        schema_store = validate_repo.load_schema_store(REPO_ROOT)
        records = validate_repo.collect_techniques(REPO_ROOT, schema_store)
        rendered = (
            REPO_ROOT / "docs" / "readers" / "source-lift" / "TECHNIQUE_EXAMPLES.md"
        ).read_text(encoding="utf-8")

        validate_repo.validate_example_manifests(REPO_ROOT, records)
        self.assertEqual(validate_repo.build_example_reader_markdown(REPO_ROOT, records), rendered)
        self.assertIn("| example | body | example path | source |", rendered)
        self.assertIn("minimal-change-flow.md", rendered)
        self.assertNotIn(
            "This example shows the technique as a reusable outline for a small, reviewable change.",
            rendered,
        )

        domain_positions = [rendered.index(f"## `{domain}`") for domain in validate_repo.DOMAIN_ORDER]
        self.assertEqual(sorted(domain_positions), domain_positions)

    def test_evidence_note_reader_generated_surface_matches_builder_and_stays_bounded(
        self,
    ) -> None:
        schema_store = validate_repo.load_schema_store(REPO_ROOT)
        records = validate_repo.collect_techniques(REPO_ROOT, schema_store)
        rendered = (
            REPO_ROOT
            / "docs"
            / "readers"
            / "source-lift"
            / "EVIDENCE_NOTE_SURFACES.md"
        ).read_text(encoding="utf-8")

        validate_repo.validate_evidence_note_manifests(REPO_ROOT, records)
        self.assertEqual(
            validate_repo.build_evidence_note_reader_markdown(REPO_ROOT, records),
            rendered,
        )
        self.assertIn("## Note Scope", rendered)
        self.assertIn("`adverse_effects_review`", rendered)
        self.assertIn("`typed_sections`", rendered)
        self.assertIn("opaque note body only", rendered)
        self.assertNotIn(
            "validation becomes symbolic while the workflow still reports success",
            rendered,
        )

    def test_kag_source_readers_are_discoverable_from_docs_root_changelog_kag_and_release_docs(
        self,
    ) -> None:
        docs_readme = (REPO_ROOT / "docs" / "README.md").read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        kag_source_guide = (
            REPO_ROOT / "docs" / "source-lift" / "KAG_SOURCE_LIFT_GUIDE.md"
        ).read_text(encoding="utf-8")
        releasing = (REPO_ROOT / "docs" / "RELEASING.md").read_text(encoding="utf-8")
        evidence_guide = (
            REPO_ROOT / "docs" / "source-lift" / "EVIDENCE_NOTE_PROVENANCE_GUIDE.md"
        ).read_text(encoding="utf-8")

        for target in (
            "TECHNIQUE_SECTIONS.md",
            "TECHNIQUE_SECTION_LIFT_GUIDE.md",
            "TECHNIQUE_CHECKLISTS.md",
            "TECHNIQUE_CHECKLIST_LIFT_GUIDE.md",
            "TECHNIQUE_EXAMPLES.md",
            "TECHNIQUE_EXAMPLE_LIFT_GUIDE.md",
            "EVIDENCE_NOTE_SURFACES.md",
            "technique_section_manifest.json",
            "technique_checklist_manifest.json",
            "technique_example_manifest.json",
            "technique_evidence_note_manifest.json",
        ):
            self.assertIn(target, docs_readme)

        for target in (
            "TECHNIQUE_SECTIONS.md",
            "TECHNIQUE_SECTION_LIFT_GUIDE.md",
            "TECHNIQUE_CHECKLISTS.md",
            "TECHNIQUE_CHECKLIST_LIFT_GUIDE.md",
            "TECHNIQUE_EXAMPLES.md",
            "TECHNIQUE_EXAMPLE_LIFT_GUIDE.md",
            "EVIDENCE_NOTE_SURFACES.md",
            "EVIDENCE_NOTE_PROVENANCE_GUIDE.md",
        ):
            self.assertIn(target, changelog)

        for target in (
            "TECHNIQUE_SECTIONS.md",
            "TECHNIQUE_SECTION_LIFT_GUIDE.md",
            "TECHNIQUE_CHECKLISTS.md",
            "TECHNIQUE_CHECKLIST_LIFT_GUIDE.md",
            "TECHNIQUE_EXAMPLES.md",
            "TECHNIQUE_EXAMPLE_LIFT_GUIDE.md",
            "EVIDENCE_NOTE_SURFACES.md",
        ):
            self.assertIn(target, kag_source_guide)

        for target in (
            "`generated` lane, `kag_export` group",
            "docs/source-lift/KAG_EXPORT.md",
            "generated/kag_export.json",
            "generated/kag_export.min.json",
            "`generated` lane, `catalog` group",
            "docs/readers/source-lift/TECHNIQUE_SECTIONS.md",
            "docs/readers/source-lift/TECHNIQUE_CHECKLISTS.md",
            "docs/readers/source-lift/TECHNIQUE_EXAMPLES.md",
            "docs/readers/source-lift/EVIDENCE_NOTE_SURFACES.md",
            "TECHNIQUE_SECTION_LIFT_GUIDE.md",
            "TECHNIQUE_CHECKLIST_LIFT_GUIDE.md",
            "TECHNIQUE_EXAMPLE_LIFT_GUIDE.md",
            "EVIDENCE_NOTE_PROVENANCE_GUIDE.md",
        ):
            self.assertIn(target, releasing)

        self.assertIn("EVIDENCE_NOTE_SURFACES.md", evidence_guide)
        self.assertIn("authoritative contract doc", evidence_guide)

    def test_capsule_surfaces_are_discoverable_from_docs_root_readme_changelog_and_release_docs(
        self,
    ) -> None:
        docs_readme = (REPO_ROOT / "docs" / "README.md").read_text(encoding="utf-8")
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        releasing = (REPO_ROOT / "docs" / "RELEASING.md").read_text(encoding="utf-8")

        self.assertIn("TECHNIQUE_CAPSULES.md", docs_readme)
        self.assertIn("TECHNIQUE_CAPSULE_GUIDE.md", docs_readme)
        self.assertIn("technique_capsules.json", docs_readme)
        self.assertIn("technique_capsules.min.json", docs_readme)
        self.assertIn("docs/readers/runtime/TECHNIQUE_CAPSULES.md", readme)
        self.assertIn("TECHNIQUE_CAPSULES.md", changelog)
        self.assertIn("TECHNIQUE_CAPSULE_GUIDE.md", changelog)
        self.assertIn("technique_capsules.min.json", changelog)
        self.assertIn("TECHNIQUE_CAPSULES.md", (REPO_ROOT / "docs" / "START_HERE.md").read_text(encoding="utf-8"))
        self.assertIn("`generated` lane, `catalog` group", releasing)
        self.assertIn("`release` lane", releasing)
        self.assertIn("generated/technique_capsules.min.json", releasing)
        self.assertIn("docs/readers/runtime/TECHNIQUE_CAPSULES.md", releasing)

    def test_family_scout_reports_are_builder_aligned_and_explicitly_non_authoritative(
        self,
    ) -> None:
        catalog = validate_repo.read_json(REPO_ROOT / "generated" / "technique_catalog.json")
        registry = validate_repo.load_kind_registry(REPO_ROOT)
        family_scout = validate_repo.load_family_scout(REPO_ROOT)
        kind_overlay = validate_repo.load_kind_overlay(REPO_ROOT)
        report = validate_repo.read_json(REPO_ROOT / validate_repo.TECHNIQUE_REFORM_REPORTS_DIR / "technique_family_scout.json")
        report_markdown = (
            REPO_ROOT / validate_repo.TECHNIQUE_REFORM_REPORTS_DIR / "technique_family_scout.md"
        ).read_text(encoding="utf-8")
        audit_markdown = (
            REPO_ROOT / validate_repo.TECHNIQUE_REFORM_REPORTS_DIR / "kind_ambiguity_audit.md"
        ).read_text(encoding="utf-8")

        expected_report = validate_repo.build_family_scout_payload(
            catalog, family_scout, kind_overlay
        )
        expected_markdown = validate_repo.build_family_scout_markdown(expected_report)
        expected_audit = validate_repo.build_kind_ambiguity_audit_markdown(
            catalog, registry, family_scout, kind_overlay
        )

        self.assertEqual(expected_report, report)
        self.assertEqual(expected_markdown, report_markdown)
        self.assertEqual(expected_audit, audit_markdown)
        self.assertEqual("scout-only-non-authoritative", report["status"])
        self.assertEqual(validate_repo.FAMILY_SCOUT_AUTHORITY_NOTE, report["authority_note"])
        self.assertIn("non-authoritative", report_markdown)
        self.assertIn("weaker than bundle frontmatter", report_markdown)
        self.assertIn("non-authoritative", audit_markdown)
        for seam_heading in (
            "## `workflow` vs `guardrail`",
            "## `validation` vs `assessment`",
            "## `artifact` vs `lift`",
            "## `composition` vs `distribution`",
            "## `handoff` vs `workflow`",
        ):
            self.assertIn(seam_heading, audit_markdown)
        for verdict in ("`keep current kind`", "`revisit later`", "`candidate remap`"):
            self.assertIn(verdict, audit_markdown)

    def test_shadow_surface_is_discoverable_from_docs_root_and_changelog(self) -> None:
        docs_readme = (REPO_ROOT / "docs" / "README.md").read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        shadow_packets = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "shadow"
            / "README.md"
        ).read_text(encoding="utf-8")

        self.assertIn("Shadow Patterns", docs_readme)
        self.assertIn("shadow_review_manifest.json", docs_readme)
        self.assertIn("review packet route", docs_readme)
        self.assertIn("PUBLISHED_SUMMARY_SHADOW_REVIEW.md", shadow_packets)
        self.assertIn("EVALUATION_CHAIN_SHADOW_REVIEW.md", shadow_packets)
        self.assertIn("docs/readers/review/SHADOW_PATTERNS.md", changelog)
        self.assertIn("PUBLISHED_SUMMARY_SHADOW_REVIEW.md", changelog)
        self.assertIn("shadow_review_manifest.json", changelog)
        self.assertIn("EVALUATION_CHAIN_SHADOW_REVIEW.md", changelog)

    def test_shadow_wave_bundle_is_present_in_index_catalog_and_selection_surface(self) -> None:
        technique_index = (REPO_ROOT / "TECHNIQUE_INDEX.md").read_text(encoding="utf-8")
        selection = (REPO_ROOT / "docs" / "readers" / "selection" / "TECHNIQUE_SELECTION.md").read_text(
            encoding="utf-8"
        )
        catalog = validate_repo.read_json(REPO_ROOT / "generated" / "technique_catalog.json")
        entry = next(entry for entry in catalog["techniques"] if entry["id"] == "AOA-T-0022")

        self.assertEqual("docs", entry["domain"])
        self.assertEqual("lift", entry["kind"])
        self.assertEqual("promoted", entry["status"])
        self.assertIn("risk-and-negative-effect-lift", technique_index)
        self.assertIn("AOA-T-0022", selection)
        self.assertIn("risk-and-negative-effect-lift", selection)

    def test_evidence_note_manifest_includes_adverse_effects_review_scope_and_entries(self) -> None:
        manifest = validate_repo.read_json(REPO_ROOT / "generated" / "technique_evidence_note_manifest.json")
        scope = manifest["typed_note_scopes"]["adverse_effects_review"]
        adverse_note_count = sum(
            1
            for technique in manifest["techniques"]
            for note in technique["notes"]
            if note["kind"] == "adverse_effects_review"
        )

        self.assertEqual("Adverse Effects Review", scope["title"])
        self.assertEqual(
            [
                "Technique",
                "Review focus",
                "Failure modes",
                "Negative effects",
                "Misuse patterns",
                "Detection signals",
                "Mitigations",
                "Recommendation",
            ],
            scope["section_scope"],
        )
        self.assertEqual(98, adverse_note_count)

    def test_full_capsule_entry_requires_all_capsule_sections(self) -> None:
        technique_dir = REPO_ROOT / "techniques" / "demo"
        technique_path = technique_dir / "TECHNIQUE.md"
        record = validate_repo.TechniqueRecord(
            technique_dir=technique_dir,
            technique_path=technique_path,
            id="AOA-T-9999",
            name="demo-technique",
            domain="docs",
            kind="artifact",
            status="promoted",
            summary="Short demo summary.",
            frontmatter={},
            body="",
            sections=(validate_repo.TechniqueSection(heading="Intent", markdown="Keep the workflow reviewable."),),
            checklists=(),
            examples=(),
            notes=(),
        )

        with self.assertRaises(validate_repo.ValidationError):
            validate_repo.full_capsule_entry(REPO_ROOT, record)

    def test_full_capsule_entry_derives_bounded_runtime_card_fields(self) -> None:
        technique_dir = REPO_ROOT / "techniques" / "demo"
        technique_path = technique_dir / "TECHNIQUE.md"
        record = validate_repo.TechniqueRecord(
            technique_dir=technique_dir,
            technique_path=technique_path,
            id="AOA-T-9999",
            name="demo-technique",
            domain="docs",
            kind="artifact",
            status="promoted",
            summary="Short demo summary.",
            frontmatter={},
            body="",
            sections=(
                validate_repo.TechniqueSection(
                    heading="Intent",
                    markdown="Keep changes reviewable and explicit through every applied step while avoiding silent drift.",
                ),
                validate_repo.TechniqueSection(
                    heading="When to use",
                    markdown="- repositories with repeated workflow churn\n- teams that need a compact operational card",
                ),
                validate_repo.TechniqueSection(
                    heading="When not to use",
                    markdown="- one-off notes with no reusable workflow\n- cases where the bundle should be read in full first",
                ),
                validate_repo.TechniqueSection(
                    heading="Inputs",
                    markdown="- a bounded change request\n- touched surfaces\n- a named verification plan",
                ),
                validate_repo.TechniqueSection(
                    heading="Outputs",
                    markdown="- one stable runtime card\n- a smaller next-read hint\n- a bounded validation reminder",
                ),
                validate_repo.TechniqueSection(
                    heading="Contracts",
                    markdown="- the card stays derived from source markdown\n- the short form does not replace the bundle",
                ),
                validate_repo.TechniqueSection(
                    heading="Risks",
                    markdown="""### Failure modes

- teams trust the card more than the source bundle

### Negative effects

- shorthand can flatten nuance

### Misuse patterns

- contributors hand-edit the card

### Detection signals

- the card keeps drifting from the authored sections

### Mitigations

- regenerate after source edits
""",
                ),
                validate_repo.TechniqueSection(
                    heading="Validation",
                    markdown="Verify the technique by confirming that:\n- the card stays short\n- the card stays derived\n- readers can still route back to the full bundle",
                ),
            ),
            checklists=(),
            examples=(),
            notes=(),
        )

        capsule = validate_repo.full_capsule_entry(REPO_ROOT, record)

        self.assertEqual("Short demo summary.", capsule["summary"])
        self.assertEqual("techniques/demo/TECHNIQUE.md", capsule["technique_path"])
        self.assertFalse(capsule["one_line_intent"].startswith("Intent: "))
        self.assertTrue(capsule["use_when_short"].startswith("Use when "))
        self.assertTrue(capsule["do_not_use_short"].startswith("Avoid when "))
        self.assertTrue(capsule["inputs_short"].startswith("Needs "))
        self.assertTrue(capsule["outputs_short"].startswith("Produces "))
        self.assertTrue(capsule["core_contract_short"].startswith("Core contract: "))
        self.assertTrue(capsule["validation_short"].startswith("Validate by checking "))
        self.assertNotEqual(
            "Keep changes reviewable and explicit through every applied step while avoiding silent drift.",
            capsule["one_line_intent"],
        )
        self.assertNotEqual(
            "- repositories with repeated workflow churn\n- teams that need a compact operational card",
            capsule["use_when_short"],
        )
        self.assertNotEqual(
            """### Failure modes

- teams trust the card more than the source bundle

### Negative effects

- shorthand can flatten nuance

### Misuse patterns

- contributors hand-edit the card

### Detection signals

- the card keeps drifting from the authored sections

### Mitigations

- regenerate after source edits
""".strip(),
            capsule["main_risk_short"],
        )

    def test_capsule_payload_is_deterministic_and_matches_generated_file(self) -> None:
        schema_store = validate_repo.load_schema_store(REPO_ROOT)
        records = validate_repo.collect_techniques(REPO_ROOT, schema_store)

        forward_payload = validate_repo.build_capsule_payload(REPO_ROOT, records)
        reverse_payload = validate_repo.build_capsule_payload(REPO_ROOT, list(reversed(records)))
        expected_full, expected_min = validate_repo.build_capsule_payloads(REPO_ROOT, records)
        generated_payload = validate_repo.read_json(REPO_ROOT / "generated" / "technique_capsules.json")
        generated_min_payload = validate_repo.read_json(
            REPO_ROOT / "generated" / "technique_capsules.min.json"
        )
        catalog = validate_repo.read_json(REPO_ROOT / "generated" / "technique_catalog.json")

        self.assertEqual(forward_payload, reverse_payload)
        self.assertEqual(forward_payload, expected_full)
        self.assertEqual(forward_payload, generated_payload)
        self.assertEqual(expected_min, generated_min_payload)
        self.assertEqual(
            [
                (entry["id"], entry["name"], entry["summary"], entry["technique_path"])
                for entry in generated_payload["techniques"]
            ],
            [
                (entry["id"], entry["name"], entry["summary"], entry["technique_path"])
                for entry in catalog["techniques"]
            ],
        )

    def test_capsule_min_payload_stays_exact_projection_of_full_payload(self) -> None:
        full_payload = validate_repo.read_json(REPO_ROOT / "generated" / "technique_capsules.json")
        min_payload = validate_repo.read_json(REPO_ROOT / "generated" / "technique_capsules.min.json")

        self.assertEqual(validate_repo.project_min_capsule_payload(full_payload), min_payload)
        self.assertEqual(full_payload["capsule_version"], min_payload["capsule_version"])
        self.assertEqual(full_payload["source_of_truth"], min_payload["source_of_truth"])

        expected_keys = list(validate_repo.CAPSULE_MIN_FIELDS)
        for entry in min_payload["techniques"]:
            self.assertEqual(expected_keys, list(entry.keys()))

    def test_capsule_reader_surface_matches_generated_file_and_respects_ordering(self) -> None:
        schema_store = validate_repo.load_schema_store(REPO_ROOT)
        records = validate_repo.collect_techniques(REPO_ROOT, schema_store)
        rendered = validate_repo.build_capsule_markdown(REPO_ROOT, records)
        generated = (
            REPO_ROOT / "docs" / "readers" / "runtime" / "TECHNIQUE_CAPSULES.md"
        ).read_text(encoding="utf-8")

        self.assertEqual(rendered, generated)

        domain_positions = [rendered.index(f"## `{domain}`") for domain in validate_repo.DOMAIN_ORDER]
        self.assertEqual(sorted(domain_positions), domain_positions)

        for index, domain in enumerate(validate_repo.DOMAIN_ORDER):
            start = rendered.index(f"## `{domain}`")
            if index + 1 < len(validate_repo.DOMAIN_ORDER):
                end = rendered.index(f"## `{validate_repo.DOMAIN_ORDER[index + 1]}`")
                domain_block = rendered[start:end]
            else:
                domain_block = rendered[start:]

            actual_ids = [
                line.split("[", 1)[1].split("]", 1)[0]
                for line in domain_block.splitlines()
                if line.startswith("### [AOA-T-")
            ]
            expected_ids = [
                record.id
                for record in sorted(
                    (record for record in records if record.domain == domain),
                    key=lambda record: (
                        validate_repo.capsule_status_rank(record.status),
                        record.status,
                        record.id,
                    ),
                )
            ]

            self.assertEqual(expected_ids, actual_ids)

        self.assertIn("This surface is not selection, scoring, or policy routing.", rendered)
        self.assertIn("Technique Capsule Guide", rendered)
        self.assertNotIn("KAG Source Lift Guide", rendered)

    def test_short_capsule_fallback_preserves_prefixes(self) -> None:
        self.assertTrue(
            validate_repo.summarize_capsule_use_when("triage drift").startswith("Use when ")
        )
        self.assertTrue(
            validate_repo.summarize_capsule_do_not_use("strict gate").startswith("Avoid when ")
        )
        self.assertTrue(
            validate_repo.summarize_capsule_inputs("- clean logs").startswith("Needs ")
        )
        self.assertTrue(
            validate_repo.summarize_capsule_outputs("- bounded report").startswith("Produces ")
        )
        self.assertTrue(
            validate_repo.summarize_capsule_contract("- keep scope narrow").startswith(
                "Core contract: "
            )
        )
        self.assertTrue(
            validate_repo.summarize_capsule_risk(
                """### Failure modes

- silent drift

### Negative effects

- extra noise

### Misuse patterns

- widened gate

### Detection signals

- review mismatch

### Mitigations

- narrow contract
"""
            ).startswith("Main risk: ")
        )
        self.assertTrue(
            validate_repo.summarize_capsule_validation("- one clean check").startswith(
                "Validate by checking "
            )
        )

    def test_capsule_markdown_items_preserve_wrapped_bullets(self) -> None:
        self.assertEqual(
            [
                "local rebuilds go green against workspace state while CI still reads older or pinned sibling refs and fails",
                "repo-native validators also stay green",
            ],
            validate_repo.capsule_markdown_items(
                """- local rebuilds go green against workspace state while CI still reads older or
  pinned sibling refs and fails
- repo-native validators also stay green"""
            ),
        )

        risk_short = validate_repo.summarize_capsule_risk(
            """### Failure modes

- local rebuilds go green against workspace state while CI still reads older or
  pinned sibling refs and fails

### Negative effects

- extra setup overhead

### Misuse patterns

- workspace-only validation
"""
        )
        validation_short = validate_repo.summarize_capsule_validation(
            """Verify the technique by confirming that:

- the owner-side goal and stop condition were explicit before the
  PR landed
- the owner repository merged the bounded change"""
        )

        self.assertIn("older or pinned", risk_short)
        self.assertNotIn("older or.", risk_short)
        self.assertIn("before the PR landed", validation_short)


if __name__ == "__main__":
    unittest.main()
