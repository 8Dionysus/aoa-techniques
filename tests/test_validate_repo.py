from __future__ import annotations

import re
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from scripts import validate_repo


REPO_ROOT = Path(__file__).resolve().parents[1]


class ValidateRepoRegressionTests(unittest.TestCase):
    def test_expected_evidence_kind_maps_adverse_effects_review_filename(self) -> None:
        self.assertEqual(
            "adverse_effects_review",
            validate_repo.expected_evidence_kind("notes/adverse-effects-review.md"),
        )

    def test_parse_frontmatter_keeps_colon_scalars_as_strings(self) -> None:
        frontmatter = """owners:
  - 8Dionysus
tags:
  - team:ml
  - v1:beta
  - https://example.com/x
relations:
  - type: requires
    target: AOA-T-0001
"""

        parsed = validate_repo.parse_frontmatter(frontmatter, Path("TECHNIQUE.md"))

        self.assertEqual(parsed["tags"], ["team:ml", "v1:beta", "https://example.com/x"])
        self.assertEqual(parsed["relations"], [{"type": "requires", "target": "AOA-T-0001"}])

    def test_validate_support_references_accepts_local_bundle_paths(self) -> None:
        with TemporaryDirectory() as temp_dir:
            technique_dir = Path(temp_dir) / "technique"
            note_path = technique_dir / "notes" / "local-note.md"
            note_path.parent.mkdir(parents=True)
            note_path.write_text("# note\n", encoding="utf-8")

            validate_repo.validate_support_references(
                "See `notes/local-note.md` for details.",
                technique_dir,
                technique_dir / "TECHNIQUE.md",
            )

    def test_validate_support_references_rejects_bundle_escape(self) -> None:
        with TemporaryDirectory() as temp_dir:
            technique_dir = Path(temp_dir) / "technique"
            (technique_dir / "notes").mkdir(parents=True)
            escaped_note = Path(temp_dir) / "other-technique" / "notes" / "escaped.md"
            escaped_note.parent.mkdir(parents=True)
            escaped_note.write_text("# escaped\n", encoding="utf-8")

            with self.assertRaises(validate_repo.ValidationError):
                validate_repo.validate_support_references(
                    "See `notes/../../other-technique/notes/escaped.md` for details.",
                    technique_dir,
                    technique_dir / "TECHNIQUE.md",
                )

    def test_selection_surface_escapes_summary_table_cells(self) -> None:
        full_catalog = {
            "techniques": [
                {
                    "id": "AOA-T-9999",
                    "domain": "evaluation",
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
                self.assertEqual("canonical", record.status)
                self.assertEqual(domain, record.domain)

        self.assertEqual(set(validate_repo.DOMAIN_ORDER), seen_domains)

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

    def test_validate_risks_markdown_accepts_fixed_subsection_order(self) -> None:
        validate_repo.validate_risks_markdown(
            """### Failure modes

- misses the main failure

### Negative effects

- adds avoidable friction

### Misuse patterns

- expands the pattern casually

### Detection signals

- drift shows up in review

### Mitigations

- narrow the contract again
""",
            Path("TECHNIQUE.md"),
        )

    def test_validate_risks_markdown_rejects_flat_bullets(self) -> None:
        with self.assertRaises(validate_repo.ValidationError):
            validate_repo.validate_risks_markdown(
                "- still a flat bullet list\n- without fixed subsections\n",
                Path("TECHNIQUE.md"),
            )

    def test_parse_notes_accepts_adverse_effects_review_typed_shape(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            technique_dir = repo_root / "technique"
            notes_dir = technique_dir / "notes"
            notes_dir.mkdir(parents=True)
            (notes_dir / "adverse-effects-review.md").write_text(
                """# Adverse Effects Review

## Technique
- id: AOA-T-9999
- name: demo-technique

## Review focus
- current role: bounded canonical default
- current watch seam: keep the caution supplement downstream from Risks

## Failure modes
- the note drifts away from the source markdown

## Negative effects
- reviewers stop reading the main bundle

## Misuse patterns
- teams treat the note as policy metadata

## Detection signals
- the note becomes the only cited caution source

## Mitigations
- route meaning back to Risks

## Recommendation
- keep the canonical bundle and use this note as one bounded watch surface
""",
                encoding="utf-8",
            )

            notes = validate_repo.parse_notes(repo_root, technique_dir)

            self.assertEqual(1, len(notes))
            self.assertEqual("adverse_effects_review", notes[0].kind)
            self.assertEqual("Adverse Effects Review", notes[0].title)
            self.assertEqual(
                tuple(validate_repo.TYPED_NOTE_SECTION_SCOPES["adverse_effects_review"]),
                tuple(section.heading for section in notes[0].sections),
            )

    def test_public_hygiene_allows_public_github_urls(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            docs_dir = repo_root / "docs"
            docs_dir.mkdir(parents=True)
            (docs_dir / "provenance.md").write_text(
                "Source: https://github.com/example/public-technique\n",
                encoding="utf-8",
            )

            validate_repo.validate_public_hygiene(repo_root)

    def test_public_hygiene_rejects_blocked_patterns_on_scanned_surfaces(self) -> None:
        blocked_cases = (
            "D:\\private-repo\\docs\\secret.md",
            "/Users/alice/private-notes.md",
            "See http://localhost:3000/status for details.",
            "Loopback host 127.0.0.1 should not appear here.",
            "ghp_exampletokenvalue",
            "gho_exampletokenvalue",
            "AKIAEXAMPLEKEY",
            "BEGIN OPENSSH PRIVATE KEY",
        )

        for blocked_text in blocked_cases:
            with self.subTest(blocked_text=blocked_text):
                with TemporaryDirectory() as temp_dir:
                    repo_root = Path(temp_dir)
                    docs_dir = repo_root / "docs"
                    docs_dir.mkdir(parents=True)
                    (docs_dir / "public.md").write_text(blocked_text + "\n", encoding="utf-8")

                    with self.assertRaises(validate_repo.ValidationError):
                        validate_repo.validate_public_hygiene(repo_root)


class TechniqueContentSmokeTests(unittest.TestCase):
    def test_shadow_and_caution_guides_match_current_enforced_contract(self) -> None:
        shadow_guide = (REPO_ROOT / "docs" / "TECHNIQUE_SHADOW_GUIDE.md").read_text(
            encoding="utf-8"
        )
        risk_guide = (
            REPO_ROOT / "docs" / "RISK_AND_NEGATIVE_EFFECT_LIFT_GUIDE.md"
        ).read_text(encoding="utf-8")

        self.assertIn("The current repository now requires", shadow_guide)
        self.assertNotIn("does not add schema fields, validator rules", shadow_guide)
        self.assertNotIn("no repo-wide retrofit of existing bundles", shadow_guide)
        self.assertNotIn("no canonical-only `notes/adverse-effects-review.md` requirement yet", shadow_guide)
        self.assertIn("no generated caution outputs or caution IDs", shadow_guide)
        self.assertIn(
            "enforcing the current markdown-first `Risks` contract",
            risk_guide,
        )
        self.assertNotIn(
            "does not add shadow fields, generated caution outputs, or validator logic",
            risk_guide,
        )
        self.assertNotIn("no bundle retrofits in the same wave", risk_guide)
        self.assertNotIn("no canonical-only `adverse-effects-review` requirement yet", risk_guide)
        self.assertIn("no generated caution outputs", risk_guide)

    def test_all_published_techniques_use_richer_risks_contract(self) -> None:
        technique_paths = sorted((REPO_ROOT / "techniques").glob("**/TECHNIQUE.md"))
        self.assertEqual(22, len(technique_paths))

        for technique_path in technique_paths:
            _frontmatter, body = validate_repo.split_frontmatter(technique_path)
            validate_repo.validate_sections(body, technique_path)

    def test_kag_quartet_lands_as_promoted_docs_family(self) -> None:
        catalog = validate_repo.read_json(REPO_ROOT / "generated" / "technique_catalog.json")
        entries_by_id = {entry["id"]: entry for entry in catalog["techniques"]}
        expected_ids = (
            "AOA-T-0018",
            "AOA-T-0019",
            "AOA-T-0020",
            "AOA-T-0021",
        )

        for technique_id in expected_ids:
            with self.subTest(technique_id=technique_id):
                entry = entries_by_id[technique_id]
                self.assertEqual("docs", entry["domain"])
                self.assertEqual("promoted", entry["status"])

    def test_corpus_status_split_and_domain_set_remain_bounded(self) -> None:
        catalog = validate_repo.read_json(REPO_ROOT / "generated" / "technique_catalog.json")
        status_counts: dict[str, int] = {}
        domain_values = {entry["domain"] for entry in catalog["techniques"]}

        for entry in catalog["techniques"]:
            status_counts[entry["status"]] = status_counts.get(entry["status"], 0) + 1

        self.assertEqual({"agent-workflows", "docs", "evaluation"}, domain_values)
        self.assertEqual(13, status_counts["canonical"])
        self.assertEqual(9, status_counts["promoted"])

    def test_telemetry_guardrail_status_language_is_consistent(self) -> None:
        technique = (
            REPO_ROOT
            / "techniques"
            / "evaluation"
            / "telemetry-integrity-snapshot"
            / "TECHNIQUE.md"
        ).read_text(encoding="utf-8")
        checklist = (
            REPO_ROOT
            / "techniques"
            / "evaluation"
            / "telemetry-integrity-snapshot"
            / "checks"
            / "telemetry-integrity-checklist.md"
        ).read_text(encoding="utf-8")
        minimal_example = (
            REPO_ROOT
            / "techniques"
            / "evaluation"
            / "telemetry-integrity-snapshot"
            / "examples"
            / "minimal-telemetry-integrity-snapshot.md"
        ).read_text(encoding="utf-8")
        object_store_example = (
            REPO_ROOT
            / "techniques"
            / "evaluation"
            / "telemetry-integrity-snapshot"
            / "examples"
            / "object-store-telemetry-integrity-snapshot.md"
        ).read_text(encoding="utf-8")

        self.assertIn("`ok`, `attention`, or `not_available`", technique)
        self.assertIn("`ok`, `attention`, or `not_available`", checklist)
        self.assertIn('"utc_guardrail_status": "not_available"', minimal_example)
        self.assertIn('"cadence_consistency_status": "not_available"', object_store_example)

    def test_source_of_truth_checklist_supports_delegated_homes(self) -> None:
        checklist = (
            REPO_ROOT
            / "techniques"
            / "docs"
            / "source-of-truth-layout"
            / "checks"
            / "doc-role-checklist.md"
        ).read_text(encoding="utf-8")
        technique = (
            REPO_ROOT
            / "techniques"
            / "docs"
            / "source-of-truth-layout"
            / "TECHNIQUE.md"
        ).read_text(encoding="utf-8")

        self.assertIn("delegated external runbook", checklist)
        self.assertIn("delegated external tracker", checklist)
        self.assertIn("delegated external planning surface", checklist)
        self.assertIn("delegated elsewhere", technique)

    def test_canonical_readiness_notes_do_not_use_windows_absolute_paths(self) -> None:
        note_paths = [
            REPO_ROOT
            / "techniques"
            / "evaluation"
            / "latest-alias-plus-history-copy"
            / "notes"
            / "canonical-readiness.md",
            REPO_ROOT
            / "techniques"
            / "evaluation"
            / "published-summary-remediation-snapshot"
            / "notes"
            / "canonical-readiness.md",
            REPO_ROOT
            / "techniques"
            / "evaluation"
            / "required-vs-optional-source-rendering"
            / "notes"
            / "canonical-readiness.md",
            REPO_ROOT
            / "techniques"
            / "evaluation"
            / "telemetry-integrity-snapshot"
            / "notes"
            / "canonical-readiness.md",
        ]

        for note_path in note_paths:
            content = note_path.read_text(encoding="utf-8")
            self.assertNotIn("D:\\", content)
            self.assertIn("atm10-agent/docs/", content)

    def test_canonical_bundles_have_adverse_effects_reviews_and_promoted_bundles_do_not(self) -> None:
        schema_store = validate_repo.load_schema_store(REPO_ROOT)
        records = validate_repo.collect_techniques(REPO_ROOT, schema_store)
        canonical_records = [record for record in records if record.status == "canonical"]
        promoted_records = [record for record in records if record.status == "promoted"]

        self.assertEqual(13, len(canonical_records))

        for record in canonical_records:
            self.assertEqual("adverse_effects_review", record.frontmatter["evidence"][-1]["kind"])
            self.assertEqual(
                "notes/adverse-effects-review.md",
                record.frontmatter["evidence"][-1]["path"],
            )

        for record in promoted_records:
            self.assertNotIn(
                "adverse_effects_review",
                {item["kind"] for item in record.frontmatter["evidence"]},
            )

    def test_docs_boundary_next_step_matches_generated_semantic_manifest(self) -> None:
        expected_phrase = "validator-synchronized with authored semantic reviews"
        review_path = REPO_ROOT / "docs" / "DOCS_BOUNDARY_SEMANTIC_REVIEW.md"
        review_content = review_path.read_text(encoding="utf-8")
        manifest = validate_repo.read_json(REPO_ROOT / "generated" / "semantic_review_manifest.json")
        manifest_entry = next(
            review
            for review in manifest["reviews"]
            if review["review_path"] == "docs/DOCS_BOUNDARY_SEMANTIC_REVIEW.md"
        )

        self.assertIn(expected_phrase, review_content)
        self.assertIn(expected_phrase, manifest_entry["next_step_markdown"])

    def test_semantic_review_next_steps_match_generated_manifest(self) -> None:
        expected_phrases = {
            "docs/PUBLISHED_SUMMARY_SEMANTIC_REVIEW.md": "open a new pilot only if future wording starts collapsing rendering policy back into the published-summary package",
            "docs/EVALUATION_CHAIN_SEMANTIC_REVIEW.md": "open a new pilot only if storage-layout detail starts crowding out rollout semantics",
            "docs/INSTRUCTION_SURFACE_SEMANTIC_REVIEW.md": "stronger live multi-target reuse evidence for `AOA-T-0013`",
            "docs/SKILL_SUPPORT_SEMANTIC_REVIEW.md": "monitoring the documented watch seams around `AOA-T-0015` vs `AOA-T-0017` and `AOA-T-0016` drift toward generic architecture formalism",
        }
        manifest = validate_repo.read_json(REPO_ROOT / "generated" / "semantic_review_manifest.json")
        reviews_by_path = {review["review_path"]: review for review in manifest["reviews"]}

        for review_path, expected_phrase in expected_phrases.items():
            with self.subTest(review_path=review_path):
                review_content = (REPO_ROOT / review_path).read_text(encoding="utf-8")
                self.assertIn(expected_phrase, review_content)
                self.assertIn(expected_phrase, reviews_by_path[review_path]["next_step_markdown"])

    def test_changelog_tracks_unreleased_without_losing_v010_entry(self) -> None:
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("## [Unreleased]", changelog)
        self.assertIn("## [0.1.0] - 2026-03-17", changelog)

    def test_selection_patterns_describes_validator_backed_navigation(self) -> None:
        selection_patterns = (REPO_ROOT / "docs" / "SELECTION_PATTERNS.md").read_text(
            encoding="utf-8"
        )

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

    def test_shadow_patterns_generated_surface_matches_builder_and_stays_canonical_only(
        self,
    ) -> None:
        schema_store = validate_repo.load_schema_store(REPO_ROOT)
        records = validate_repo.collect_techniques(REPO_ROOT, schema_store)
        shadow_patterns = (REPO_ROOT / "docs" / "SHADOW_PATTERNS.md").read_text(
            encoding="utf-8"
        )

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
        shadow_patterns = (REPO_ROOT / "docs" / "SHADOW_PATTERNS.md").read_text(
            encoding="utf-8"
        )

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

    def test_shadow_review_docs_follow_bounded_contract(self) -> None:
        reviews = validate_repo.parse_shadow_reviews(REPO_ROOT)
        reviews_by_path = {review.review_path: review for review in reviews}

        self.assertEqual(
            {
                "docs/PUBLISHED_SUMMARY_SHADOW_REVIEW.md",
                "docs/EVALUATION_CHAIN_SHADOW_REVIEW.md",
            },
            set(reviews_by_path),
        )
        self.assertEqual("Pair Map", reviews_by_path["docs/EVALUATION_CHAIN_SHADOW_REVIEW.md"].map_heading)
        self.assertEqual(
            "Cluster Map",
            reviews_by_path["docs/PUBLISHED_SUMMARY_SHADOW_REVIEW.md"].map_heading,
        )
        self.assertTrue(reviews_by_path["docs/EVALUATION_CHAIN_SHADOW_REVIEW.md"].seams)
        self.assertEqual(
            "`clear`",
            reviews_by_path["docs/EVALUATION_CHAIN_SHADOW_REVIEW.md"].overall_outcome,
        )

    def test_repo_doc_surface_specs_are_bounded_and_structurally_valid(self) -> None:
        validate_repo.validate_repo_doc_surface_specs(REPO_ROOT)
        validate_repo.validate_repo_doc_navigation_specs(REPO_ROOT)
        surfaces = validate_repo.parse_repo_doc_surfaces(REPO_ROOT)
        source_paths = {surface.doc_path for surface in surfaces}

        self.assertEqual(10, len(surfaces))
        self.assertEqual(
            {spec["doc_path"] for spec in validate_repo.REPO_DOC_SURFACE_SPECS},
            source_paths,
        )
        self.assertEqual(
            set(validate_repo.REPO_DOC_SURFACE_GROUP_ORDER),
            {surface.surface_group for surface in surfaces},
        )
        self.assertTrue(
            {
                "TODO.md",
                "PLANS.md",
                "ROADMAP.md",
                "docs/KAG_SOURCE_LIFT_GUIDE.md",
                "docs/PUBLISHED_SUMMARY_SEMANTIC_REVIEW.md",
                "docs/PUBLISHED_SUMMARY_SHADOW_REVIEW.md",
            }.isdisjoint(source_paths)
        )
        for surface in surfaces:
            self.assertTrue(surface.top_level_sections)

    def test_repo_doc_surface_top_level_sections_are_stable(self) -> None:
        surfaces_by_path = {
            surface.doc_path: surface for surface in validate_repo.parse_repo_doc_surfaces(REPO_ROOT)
        }

        self.assertEqual(
            (
                "Start here",
                "Quick routes",
                "Deeper routes",
                "What belongs here",
                "Core principles",
                "Maturity model",
                "Repository structure",
                "Intended users",
                "What a good technique includes",
                "Contribution model",
                "License",
            ),
            surfaces_by_path["README.md"].top_level_sections,
        )
        self.assertEqual(
            (
                "Start Here",
                "Surface Types",
                "Recommended Reading Paths",
                "Companion Repository Surfaces",
                "Notes",
            ),
            surfaces_by_path["docs/README.md"].top_level_sections,
        )
        self.assertEqual(
            ("[Unreleased]", "[0.1.0] - 2026-03-17"),
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
        self.assertEqual(10, len(actual_full["docs"]))

    def test_repo_doc_surfaces_generated_reader_matches_builder_and_stays_bounded(self) -> None:
        validate_repo.validate_repo_doc_surface_reader(REPO_ROOT)
        repo_doc_surfaces = (REPO_ROOT / "docs" / "REPO_DOC_SURFACES.md").read_text(
            encoding="utf-8"
        )

        self.assertEqual(
            validate_repo.build_repo_doc_surfaces_markdown(REPO_ROOT),
            repo_doc_surfaces,
        )
        self.assertIn("Entrypoint / Map", repo_doc_surfaces)
        self.assertIn("Contribution / Policy", repo_doc_surfaces)
        self.assertIn("Walkthrough / Context", repo_doc_surfaces)
        self.assertIn("Status / Release", repo_doc_surfaces)
        self.assertIn("README.md", repo_doc_surfaces)
        self.assertIn("docs/RELEASING.md", repo_doc_surfaces)
        self.assertIn("repo_doc_surface_manifest.json", repo_doc_surfaces)
        self.assertNotIn("](../TODO.md)", repo_doc_surfaces)
        self.assertNotIn("](../PLANS.md)", repo_doc_surfaces)
        self.assertNotIn("](../ROADMAP.md)", repo_doc_surfaces)
        self.assertNotIn("PUBLISHED_SUMMARY_SHADOW_REVIEW.md", repo_doc_surfaces)

    def test_repo_doc_surfaces_are_discoverable_from_docs_root_changelog_kag_and_release_docs(
        self,
    ) -> None:
        docs_readme = (REPO_ROOT / "docs" / "README.md").read_text(encoding="utf-8")
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        kag_source_guide = (REPO_ROOT / "docs" / "KAG_SOURCE_LIFT_GUIDE.md").read_text(
            encoding="utf-8"
        )
        releasing = (REPO_ROOT / "docs" / "RELEASING.md").read_text(encoding="utf-8")

        self.assertIn("REPO_DOC_SURFACES.md", docs_readme)
        self.assertIn("repo_doc_surface_manifest.json", docs_readme)
        self.assertIn("REPO_DOC_SURFACE_LIFT_GUIDE.md", docs_readme)
        self.assertIn("docs/REPO_DOC_SURFACES.md", readme)
        self.assertIn("generated/repo_doc_surface_manifest.json", readme)
        self.assertIn("docs/REPO_DOC_SURFACE_LIFT_GUIDE.md", readme)
        self.assertIn("REPO_DOC_SURFACES.md", changelog)
        self.assertIn("repo_doc_surface_manifest.json", changelog)
        self.assertIn("REPO_DOC_SURFACE_LIFT_GUIDE.md", changelog)
        self.assertIn("repo_doc_surface_manifest.json", kag_source_guide)
        self.assertIn("REPO_DOC_SURFACE_LIFT_GUIDE.md", kag_source_guide)
        self.assertIn("REPO_DOC_SURFACES.md", kag_source_guide)
        self.assertIn("python scripts/build_repo_doc_surface_manifest.py", releasing)
        self.assertIn("python scripts/build_shadow_review_manifest.py", releasing)

    def test_section_reader_generated_surface_matches_builder_and_preserves_scope_order(
        self,
    ) -> None:
        schema_store = validate_repo.load_schema_store(REPO_ROOT)
        records = validate_repo.collect_techniques(REPO_ROOT, schema_store)
        rendered = (REPO_ROOT / "docs" / "TECHNIQUE_SECTIONS.md").read_text(encoding="utf-8")

        validate_repo.validate_section_manifests(REPO_ROOT, records)
        self.assertEqual(validate_repo.build_section_reader_markdown(REPO_ROOT, records), rendered)
        self.assertEqual(
            validate_repo.SECTION_LIFT_HEADINGS,
            tuple(re.findall(r"^## `(.+?)`$", rendered, flags=re.MULTILINE)),
        )
        self.assertIn("## Section Scope", rendered)
        self.assertNotIn(
            "Reduce unsafe, opaque, or non-reviewable agent changes by requiring a visible workflow before and after apply.",
            rendered,
        )
        self.assertNotIn("## `Public sanitization notes`", rendered)

    def test_checklist_reader_generated_surface_matches_builder_and_stays_ordered(self) -> None:
        schema_store = validate_repo.load_schema_store(REPO_ROOT)
        records = validate_repo.collect_techniques(REPO_ROOT, schema_store)
        rendered = (REPO_ROOT / "docs" / "TECHNIQUE_CHECKLISTS.md").read_text(encoding="utf-8")

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
                    f"### {validate_repo.record_technique_link(REPO_ROOT, record)} - {record.name} (`{record.status}`)"
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
        rendered = (REPO_ROOT / "docs" / "TECHNIQUE_EXAMPLES.md").read_text(encoding="utf-8")

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
        rendered = (REPO_ROOT / "docs" / "EVIDENCE_NOTE_SURFACES.md").read_text(
            encoding="utf-8"
        )

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

    def test_kag_source_readers_are_discoverable_from_docs_root_readme_changelog_kag_and_release_docs(
        self,
    ) -> None:
        docs_readme = (REPO_ROOT / "docs" / "README.md").read_text(encoding="utf-8")
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        kag_source_guide = (REPO_ROOT / "docs" / "KAG_SOURCE_LIFT_GUIDE.md").read_text(
            encoding="utf-8"
        )
        releasing = (REPO_ROOT / "docs" / "RELEASING.md").read_text(encoding="utf-8")
        evidence_guide = (
            REPO_ROOT / "docs" / "EVIDENCE_NOTE_PROVENANCE_GUIDE.md"
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
            "docs/TECHNIQUE_SECTIONS.md",
            "docs/TECHNIQUE_SECTION_LIFT_GUIDE.md",
            "docs/TECHNIQUE_CHECKLISTS.md",
            "docs/TECHNIQUE_CHECKLIST_LIFT_GUIDE.md",
            "docs/TECHNIQUE_EXAMPLES.md",
            "docs/TECHNIQUE_EXAMPLE_LIFT_GUIDE.md",
            "docs/EVIDENCE_NOTE_SURFACES.md",
            "generated/technique_section_manifest.json",
            "generated/technique_checklist_manifest.json",
            "generated/technique_example_manifest.json",
            "generated/technique_evidence_note_manifest.json",
        ):
            self.assertIn(target, readme)

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
            "python scripts/build_section_manifest.py",
            "python scripts/build_checklist_manifest.py",
            "python scripts/build_example_manifest.py",
            "python scripts/build_evidence_note_manifest.py",
            "docs/TECHNIQUE_SECTIONS.md",
            "docs/TECHNIQUE_CHECKLISTS.md",
            "docs/TECHNIQUE_EXAMPLES.md",
            "docs/EVIDENCE_NOTE_SURFACES.md",
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
        self.assertIn("docs/TECHNIQUE_CAPSULES.md", readme)
        self.assertIn("docs/TECHNIQUE_CAPSULE_GUIDE.md", readme)
        self.assertIn("generated/technique_capsules.json", readme)
        self.assertIn("generated/technique_capsules.min.json", readme)
        self.assertIn("TECHNIQUE_CAPSULES.md", changelog)
        self.assertIn("TECHNIQUE_CAPSULE_GUIDE.md", changelog)
        self.assertIn("technique_capsules.min.json", changelog)
        self.assertIn("python scripts/build_capsules.py", releasing)
        self.assertIn("generated/technique_capsules.min.json", releasing)
        self.assertIn("docs/TECHNIQUE_CAPSULES.md", releasing)

    def test_docs_readme_and_guides_link_to_reusable_lift_family(self) -> None:
        docs_readme = (REPO_ROOT / "docs" / "README.md").read_text(encoding="utf-8")
        kag_source_guide = (REPO_ROOT / "docs" / "KAG_SOURCE_LIFT_GUIDE.md").read_text(
            encoding="utf-8"
        )
        shadow_guide = (REPO_ROOT / "docs" / "TECHNIQUE_SHADOW_GUIDE.md").read_text(
            encoding="utf-8"
        )
        risk_guide = (
            REPO_ROOT / "docs" / "RISK_AND_NEGATIVE_EFFECT_LIFT_GUIDE.md"
        ).read_text(encoding="utf-8")
        metadata_guide = (
            REPO_ROOT / "docs" / "FRONTMATTER_METADATA_SPINE_GUIDE.md"
        ).read_text(encoding="utf-8")
        provenance_guide = (
            REPO_ROOT / "docs" / "EVIDENCE_NOTE_PROVENANCE_GUIDE.md"
        ).read_text(encoding="utf-8")
        relation_guide = (
            REPO_ROOT / "docs" / "BOUNDED_RELATION_LIFT_GUIDE.md"
        ).read_text(encoding="utf-8")

        self.assertIn("markdown-technique-section-lift", docs_readme)
        self.assertIn("frontmatter-metadata-spine", docs_readme)
        self.assertIn("evidence-note-provenance-lift", docs_readme)
        self.assertIn("bounded-relation-lift-for-kag", docs_readme)
        self.assertIn("risk-and-negative-effect-lift", docs_readme)
        self.assertIn("technique_capsules.json", docs_readme)
        self.assertIn("shadow_review_manifest.json", docs_readme)
        self.assertIn("SHADOW_PATTERNS.md", docs_readme)
        self.assertIn("PUBLISHED_SUMMARY_SHADOW_REVIEW.md", docs_readme)
        self.assertIn("EVALUATION_CHAIN_SHADOW_REVIEW.md", docs_readme)
        self.assertIn("markdown-technique-section-lift", kag_source_guide)
        self.assertIn("risk-and-negative-effect-lift", kag_source_guide)
        self.assertIn("shadow_review_manifest.json", kag_source_guide)
        self.assertIn("risk-and-negative-effect-lift", shadow_guide)
        self.assertIn("risk-and-negative-effect-lift", risk_guide)
        self.assertIn("frontmatter-metadata-spine", metadata_guide)
        self.assertIn("evidence-note-provenance-lift", provenance_guide)
        self.assertIn("adverse_effects_review", provenance_guide)
        self.assertIn("bounded-relation-lift-for-kag", relation_guide)

    def test_shadow_surface_is_discoverable_from_root_docs_and_changelog(self) -> None:
        docs_readme = (REPO_ROOT / "docs" / "README.md").read_text(encoding="utf-8")
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Shadow Patterns", docs_readme)
        self.assertIn("Published-Summary Shadow Review", docs_readme)
        self.assertIn("Evaluation-Chain Shadow Review", docs_readme)
        self.assertIn("shadow_review_manifest.json", docs_readme)
        self.assertIn("docs/SHADOW_PATTERNS.md", readme)
        self.assertIn("docs/PUBLISHED_SUMMARY_SHADOW_REVIEW.md", readme)
        self.assertIn("generated/shadow_review_manifest.json", readme)
        self.assertIn("docs/EVALUATION_CHAIN_SHADOW_REVIEW.md", readme)
        self.assertIn("docs/SHADOW_PATTERNS.md", changelog)
        self.assertIn("PUBLISHED_SUMMARY_SHADOW_REVIEW.md", changelog)
        self.assertIn("shadow_review_manifest.json", changelog)
        self.assertIn("EVALUATION_CHAIN_SHADOW_REVIEW.md", changelog)

    def test_shadow_wave_bundle_is_present_in_index_catalog_and_selection_surface(self) -> None:
        technique_index = (REPO_ROOT / "TECHNIQUE_INDEX.md").read_text(encoding="utf-8")
        selection = (REPO_ROOT / "docs" / "TECHNIQUE_SELECTION.md").read_text(
            encoding="utf-8"
        )
        catalog = validate_repo.read_json(REPO_ROOT / "generated" / "technique_catalog.json")
        entry = next(entry for entry in catalog["techniques"] if entry["id"] == "AOA-T-0022")

        self.assertEqual("docs", entry["domain"])
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
        self.assertEqual(13, adverse_note_count)

    def test_full_capsule_entry_requires_all_capsule_sections(self) -> None:
        technique_dir = REPO_ROOT / "techniques" / "demo"
        technique_path = technique_dir / "TECHNIQUE.md"
        record = validate_repo.TechniqueRecord(
            technique_dir=technique_dir,
            technique_path=technique_path,
            id="AOA-T-9999",
            name="demo-technique",
            domain="docs",
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
        generated = (REPO_ROOT / "docs" / "TECHNIQUE_CAPSULES.md").read_text(encoding="utf-8")

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


if __name__ == "__main__":
    unittest.main()
