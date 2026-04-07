from __future__ import annotations

import json
import re
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from jsonschema import Draft202012Validator

from scripts import release_check, validate_repo


REPO_ROOT = Path(__file__).resolve().parents[1]


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def build_required_section_body(
    headings: tuple[str, ...] = validate_repo.REQUIRED_SECTIONS,
) -> str:
    chunks: list[str] = []
    for heading in headings:
        if heading == "Risks":
            markdown = """### Failure modes

- misses the main failure

### Negative effects

- adds avoidable friction

### Misuse patterns

- expands the pattern casually

### Detection signals

- drift shows up in review

### Mitigations

- narrow the contract again"""
        else:
            markdown = f"Bounded content for {heading.lower()}."
        chunks.append(f"## {heading}\n\n{markdown}")
    return "\n\n".join(chunks)


class ValidateRepoRegressionTests(unittest.TestCase):
    def test_repo_validation_workflow_uses_bounded_release_entrypoint(self) -> None:
        workflow = (REPO_ROOT / ".github" / "workflows" / "repo-validation.yml").read_text(
            encoding="utf-8"
        )

        self.assertIn("python scripts/release_check.py", workflow)
        self.assertNotIn("python -m unittest discover -s tests", workflow)
        self.assertNotIn("python scripts/validate_repo.py", workflow)
        self.assertNotIn("python scripts/build_catalog.py", workflow)
        self.assertNotIn("python scripts/build_shadow_review_manifest.py", workflow)
        self.assertNotIn("python scripts/validate_nested_agents.py", workflow)

    def test_release_check_sequence_matches_documented_repo_build_path(self) -> None:
        self.assertEqual(
            (
                ("python", "scripts/build_repo_doc_surface_manifest.py"),
                ("python", "scripts/build_catalog.py"),
                ("python", "scripts/build_capsules.py"),
                ("python", "scripts/build_sections.py"),
                ("python", "scripts/build_section_manifest.py"),
                ("python", "scripts/build_checklist_manifest.py"),
                ("python", "scripts/build_example_manifest.py"),
                ("python", "scripts/build_evidence_note_manifest.py"),
                ("python", "scripts/build_github_review_template_manifest.py"),
                ("python", "scripts/build_semantic_review_manifest.py"),
                ("python", "scripts/build_shadow_review_manifest.py"),
                ("python", "scripts/build_promotion_readiness.py"),
                ("python", "scripts/build_kag_export.py"),
                ("python", "-m", "unittest", "discover", "-s", "tests"),
                ("python", "scripts/validate_nested_agents.py"),
                ("python", "scripts/validate_repo.py"),
            ),
            release_check.RELEASE_CHECK_COMMAND_SEQUENCE,
        )
        self.assertEqual(
            ("git", "status", "--porcelain=v1", "--untracked-files=all"),
            release_check.WORKTREE_SNAPSHOT_COMMAND,
        )
        self.assertEqual(
            ("git", "diff", "--binary", "--no-ext-diff"),
            release_check.TRACKED_DIFF_SNAPSHOT_COMMAND,
        )
        self.assertEqual(
            ("git", "diff", "--cached", "--binary", "--no-ext-diff"),
            release_check.CACHED_DIFF_SNAPSHOT_COMMAND,
        )
        self.assertEqual(("git", "diff", "--exit-code"), release_check.CLEAN_REPO_DIFF_COMMAND)

    def test_release_check_repo_state_detects_tracked_diff_changes_without_status_drift(self) -> None:
        before = release_check.RepoStateSnapshot(
            worktree_status=" M docs/TECHNIQUE_SELECTION.md\n",
            tracked_diff="diff --git a/docs/TECHNIQUE_SELECTION.md b/docs/TECHNIQUE_SELECTION.md\n-old\n+new\n",
            cached_diff="",
        )
        after = release_check.RepoStateSnapshot(
            worktree_status=" M docs/TECHNIQUE_SELECTION.md\n",
            tracked_diff="diff --git a/docs/TECHNIQUE_SELECTION.md b/docs/TECHNIQUE_SELECTION.md\n-older\n+newer\n",
            cached_diff="",
        )

        self.assertTrue(release_check.repo_state_changed(before, after))

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
        self.assertEqual("promoted", records_by_id["AOA-T-0026"].status)
        self.assertEqual("promoted", records_by_id["AOA-T-0027"].status)
        self.assertEqual("canonical", records_by_id["AOA-T-0028"].status)
        self.assertEqual("promoted", records_by_id["AOA-T-0029"].status)
        self.assertEqual("promoted", records_by_id["AOA-T-0030"].status)
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

    def test_public_hygiene_rejects_internal_host_suffix_urls(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            docs_dir = repo_root / "docs"
            docs_dir.mkdir(parents=True)
            (docs_dir / "public.md").write_text(
                "See https://grafana.internal/dashboard for details.\n",
                encoding="utf-8",
            )

            with self.assertRaises(validate_repo.ValidationError):
                validate_repo.validate_public_hygiene(repo_root)

    def test_public_hygiene_rejects_rfc1918_urls(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            docs_dir = repo_root / "docs"
            docs_dir.mkdir(parents=True)
            (docs_dir / "public.md").write_text(
                "See https://10.0.0.5/status for details.\n",
                encoding="utf-8",
            )

            with self.assertRaises(validate_repo.ValidationError):
                validate_repo.validate_public_hygiene(repo_root)

    def test_public_hygiene_scans_root_non_markdown_files(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            (repo_root / "PUBLIC.txt").write_text(
                "See https://router.corp/status for details.\n",
                encoding="utf-8",
            )

            with self.assertRaises(validate_repo.ValidationError):
                validate_repo.validate_public_hygiene(repo_root)

    def test_validate_sections_rejects_reordered_required_sections(self) -> None:
        reordered_headings = list(validate_repo.REQUIRED_SECTIONS)
        reordered_headings[0], reordered_headings[1] = reordered_headings[1], reordered_headings[0]
        body = build_required_section_body(tuple(reordered_headings))

        with self.assertRaises(validate_repo.ValidationError):
            validate_repo.validate_sections(body, Path("TECHNIQUE.md"))

    def test_validate_sections_rejects_duplicate_required_section(self) -> None:
        duplicated_headings = validate_repo.REQUIRED_SECTIONS + ("Intent",)
        body = build_required_section_body(duplicated_headings)

        with self.assertRaises(validate_repo.ValidationError):
            validate_repo.validate_sections(body, Path("TECHNIQUE.md"))


class TechniqueContentSmokeTests(unittest.TestCase):
    def test_external_import_runbook_is_discoverable_and_operator_complete(self) -> None:
        start_here = (REPO_ROOT / "docs" / "START_HERE.md").read_text(encoding="utf-8")
        docs_readme = (REPO_ROOT / "docs" / "README.md").read_text(encoding="utf-8")
        contributing = (REPO_ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
        root_readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        runbook = (REPO_ROOT / "docs" / "EXTERNAL_IMPORT_RUNBOOK.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("External Import Runbook", start_here)
        self.assertIn("External Import Runbook", docs_readme)
        self.assertIn("docs/EXTERNAL_IMPORT_RUNBOOK.md", contributing)
        self.assertIn("docs/EXTERNAL_IMPORT_RUNBOOK.md", root_readme)
        for target in (
            "nearest existing technique or overlap watch",
            "what stays out of the donor",
            "expected evidence notes",
            "expected generated surfaces",
            "downstream repo impact",
            "python scripts/release_check.py",
            "protect `main`",
            "templates/ORIGIN_EVIDENCE.template.md",
            "templates/ADAPTATION_NOTE.template.md",
            "templates/EXTERNAL_REVIEW.template.md",
        ):
            self.assertIn(target, runbook)

    def test_evidence_note_templates_are_discoverable_from_contributing_and_provenance_guide(
        self,
    ) -> None:
        contributing = (REPO_ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
        evidence_guide = (
            REPO_ROOT / "docs" / "EVIDENCE_NOTE_PROVENANCE_GUIDE.md"
        ).read_text(encoding="utf-8")

        self.assertIn("templates/", contributing)
        for template_name in (
            "ORIGIN_EVIDENCE.template.md",
            "ADAPTATION_NOTE.template.md",
            "PROMOTION_NOTE.template.md",
            "ADVERSE_EFFECTS_REVIEW.template.md",
            "EXTERNAL_ORIGIN.template.md",
            "EXTERNAL_REVIEW.template.md",
        ):
            self.assertIn(template_name, evidence_guide)

    def test_codeowners_is_present_and_scoped_narrowly(self) -> None:
        codeowners = (REPO_ROOT / ".github" / "CODEOWNERS").read_text(encoding="utf-8")
        contributing = (REPO_ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")

        for target in (
            "/.github/ @8Dionysus",
            "/scripts/ @8Dionysus",
            "/docs/ @8Dionysus",
            "/techniques/ @8Dionysus",
        ):
            self.assertIn(target, codeowners)

        self.assertIn("CODEOWNERS", contributing)

    def test_external_import_and_pr_templates_capture_overlap_and_generated_surface_fields(
        self,
    ) -> None:
        external_import = (
            REPO_ROOT / ".github" / "ISSUE_TEMPLATE" / "external-import-review.md"
        ).read_text(encoding="utf-8")
        technique_proposal = (
            REPO_ROOT / ".github" / "ISSUE_TEMPLATE" / "technique-proposal.md"
        ).read_text(encoding="utf-8")
        pr_template = (REPO_ROOT / ".github" / "PULL_REQUEST_TEMPLATE.md").read_text(
            encoding="utf-8"
        )
        external_origin = (REPO_ROOT / "templates" / "EXTERNAL_ORIGIN.template.md").read_text(
            encoding="utf-8"
        )

        for text in (
            external_import,
            technique_proposal,
            pr_template,
        ):
            self.assertIn("generated surfaces", text)
            self.assertIn("downstream repo impact", text)

        self.assertIn("nearest existing technique or overlap watch", external_import)
        self.assertIn("what stays out of the donor", external_import)
        self.assertIn("nearest existing technique or overlap watch", technique_proposal)
        self.assertIn("what stays out of scope", technique_proposal)
        self.assertIn("what stays out of the donor", pr_template)
        self.assertIn("overlap", pr_template)
        self.assertIn("reusable object extracted", external_origin)
        self.assertIn("what stays out of the donor", external_origin)

    def test_evidence_note_guide_references_current_note_templates(self) -> None:
        guide = (REPO_ROOT / "docs" / "EVIDENCE_NOTE_PROVENANCE_GUIDE.md").read_text(
            encoding="utf-8"
        )

        for target in (
            "ORIGIN_EVIDENCE.template.md",
            "ADAPTATION_NOTE.template.md",
            "PROMOTION_NOTE.template.md",
            "ADVERSE_EFFECTS_REVIEW.template.md",
            "EXTERNAL_ORIGIN.template.md",
            "EXTERNAL_REVIEW.template.md",
        ):
            self.assertIn(target, guide)
            self.assertTrue((REPO_ROOT / "templates" / target).is_file())

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
        self.assertEqual(90, len(technique_paths))

        for technique_path in technique_paths:
            _frontmatter, body = validate_repo.split_frontmatter(technique_path)
            validate_repo.validate_sections(body, technique_path)

    def test_kag_source_lift_family_status_split_stays_bounded(self) -> None:
        catalog = validate_repo.read_json(REPO_ROOT / "generated" / "technique_catalog.json")
        entries_by_id = {entry["id"]: entry for entry in catalog["techniques"]}
        expected_statuses = {
            "AOA-T-0018": "canonical",
            "AOA-T-0019": "canonical",
            "AOA-T-0020": "promoted",
            "AOA-T-0021": "canonical",
            "AOA-T-0022": "promoted",
        }

        for technique_id, expected_status in expected_statuses.items():
            with self.subTest(technique_id=technique_id):
                entry = entries_by_id[technique_id]
                self.assertEqual("docs", entry["domain"])
                self.assertEqual(expected_status, entry["status"])

    def test_corpus_status_split_and_domain_set_remain_bounded(self) -> None:
        catalog = validate_repo.read_json(REPO_ROOT / "generated" / "technique_catalog.json")
        status_counts: dict[str, int] = {}
        domain_values = {entry["domain"] for entry in catalog["techniques"]}

        for entry in catalog["techniques"]:
            status_counts[entry["status"]] = status_counts.get(entry["status"], 0) + 1

        self.assertEqual({"agent-workflows", "docs", "evaluation", "history"}, domain_values)
        self.assertEqual(25, status_counts["canonical"])
        self.assertEqual(65, status_counts["promoted"])

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

        self.assertEqual(25, len(canonical_records))

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
            "docs/AGENT_WORKFLOWS_CORE_SEMANTIC_REVIEW.md": "keep this review as the canonical-core anchor",
            "docs/PUBLISHED_SUMMARY_SEMANTIC_REVIEW.md": "open a new pilot only if future wording starts collapsing rendering policy back into the published-summary package",
            "docs/EVALUATION_CHAIN_SEMANTIC_REVIEW.md": "open a new pilot only if storage-layout detail starts crowding out rollout semantics",
            "docs/INSTRUCTION_SURFACE_SEMANTIC_REVIEW.md": "one future live managed-target propagation context for `AOA-T-0027`",
            "docs/SKILL_SUPPORT_SEMANTIC_REVIEW.md": "keep this review focused on monitoring the documented watch seams around `AOA-T-0015` vs `AOA-T-0017`",
            "docs/KAG_SOURCE_LIFT_SEMANTIC_REVIEW.md": "keep `AOA-T-0019` narrow as the canonical metadata spine",
        }
        manifest = validate_repo.read_json(REPO_ROOT / "generated" / "semantic_review_manifest.json")
        reviews_by_path = {review["review_path"]: review for review in manifest["reviews"]}

        for review_path, expected_phrase in expected_phrases.items():
            with self.subTest(review_path=review_path):
                review_content = (REPO_ROOT / review_path).read_text(encoding="utf-8")
                self.assertIn(expected_phrase, review_content)
                self.assertIn(expected_phrase, reviews_by_path[review_path]["next_step_markdown"])

    def test_changelog_tracks_unreleased_without_losing_v020_and_v010_entries(self) -> None:
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("## [Unreleased]", changelog)
        self.assertIn("## [0.2.0] - 2026-03-23", changelog)
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
        self.assertIn("START_HERE.md", selection_patterns)
        self.assertIn("Agent-workflows canonical core", selection_patterns)
        self.assertIn("AGENT_WORKFLOWS_CORE_SEMANTIC_REVIEW.md", selection_patterns)
        self.assertIn("KAG/source-lift family", selection_patterns)
        self.assertIn("KAG_SOURCE_LIFT_SEMANTIC_REVIEW.md", selection_patterns)

    def test_start_here_routes_repo_only_reading_paths(self) -> None:
        start_here = (REPO_ROOT / "docs" / "START_HERE.md").read_text(encoding="utf-8")

        for target in (
            "plan-diff-apply-verify-report/TECHNIQUE.md",
            "TECHNIQUE_SELECTION_GUIDE.md",
            "TECHNIQUE_SELECTION.md",
            "SELECTION_PATTERNS.md",
            "TECHNIQUE_INDEX.md",
            "TECHNIQUE_CAPSULES.md",
            "REPO_DOC_SURFACES.md",
            "KAG_SOURCE_LIFT_GUIDE.md",
            "SEMANTIC_REVIEW_GUIDE.md",
            "LONG_GAP_CANON_DESIGN.md",
            "EXTERNAL_EVIDENCE_SPRINT_RUNBOOK.md",
            "EXTERNAL_EVIDENCE_LEDGER.md",
            "CROSS_LAYER_TECHNIQUE_CANDIDATES.md",
            "aoa-skills",
            "aoa-evals",
            "aoa-routing",
            "25 canonical",
            "65 promoted",
            "external-dependency-first promoted techniques",
            "future-import-wave promoted techniques",
            "chat-wave promoted techniques",
            "personal-ingest-wave promoted techniques",
            "session-harvest-wave promoted techniques",
            "automation-opportunity-wave promoted techniques",
            "internal-origin promoted techniques",
            "AOA-T-0005",
            "latest canonical promotions:",
            "current closest promoted queue item: `AOA-T-0032`",
            "AOA-T-0020",
            "AOA-T-0022",
            "AOA-T-0028",
            "AOA-T-0031",
            "AOA-T-0027",
            "AOA-T-0024",
            "AOA-T-0025",
            "AOA-T-0029",
            "AOA-T-0030",
            "AOA-T-0033",
            "AOA-T-0032",
            "AOA-T-0035",
            "AOA-T-0036",
            "AOA-T-0037",
            "AOA-T-0038",
            "AOA-T-0039",
            "AOA-T-0040",
            "AOA-T-0041",
            "AOA-T-0042",
            "AOA-T-0043",
            "AOA-T-0044",
            "AOA-T-0045",
            "AOA-T-0046",
            "AOA-T-0047",
            "AOA-T-0048",
            "AOA-T-0049",
            "AOA-T-0050",
            "AOA-T-0051",
            "AOA-T-0052",
            "AOA-T-0053",
            "AOA-T-0054",
            "AOA-T-0055",
            "AOA-T-0056",
            "AOA-T-0057",
            "AOA-T-0058",
            "AOA-T-0059",
            "AOA-T-0060",
            "AOA-T-0061",
            "AOA-T-0062",
            "AOA-T-0063",
            "AOA-T-0064",
            "AOA-T-0065",
            "AOA-T-0066",
            "AOA-T-0067",
            "AOA-T-0068",
            "AOA-T-0069",
            "AOA-T-0070",
            "AOA-T-0071",
            "AOA-T-0072",
            "AOA-T-0073",
            "AOA-T-0074",
            "AOA-T-0075",
            "AOA-T-0076",
            "AOA-T-0077",
            "AOA-T-0078",
            "AOA-T-0079",
            "AOA-T-0080",
            "AOA-T-0081",
            "AOA-T-0082",
            "AOA-T-0083",
            "AOA-T-0084",
            "AOA-T-0085",
            "AOA-T-0086",
            "AOA-T-0087",
            "AOA-T-0088",
            "AOA-T-0089",
            "AOA-T-0090",
            "AOA-T-0032",
            "AOA-T-0026",
            "python scripts/validate_repo.py",
            "python -m unittest discover -s tests",
            "python scripts/release_check.py",
            "git status -sb",
        ):
            self.assertIn(target, start_here)

    def test_root_readme_surfaces_concrete_bundle_and_current_verify_routes(self) -> None:
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn(
            "techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md",
            readme,
        )
        self.assertIn("python scripts/validate_repo.py", readme)
        self.assertIn("python -m unittest discover -s tests", readme)
        self.assertIn("python scripts/release_check.py", readme)
        self.assertIn("git status -sb", readme)
        self.assertLess(
            readme.index("techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md"),
            readme.index("docs/README.md"),
        )

    def test_external_evidence_surfaces_are_discoverable_and_operator_complete(self) -> None:
        start_here = (REPO_ROOT / "docs" / "START_HERE.md").read_text(encoding="utf-8")
        docs_readme = (REPO_ROOT / "docs" / "README.md").read_text(encoding="utf-8")
        root_readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        roadmap = (REPO_ROOT / "docs" / "DEEP_AUDIT_ROADMAP.md").read_text(encoding="utf-8")
        runbook = (REPO_ROOT / "docs" / "EXTERNAL_EVIDENCE_SPRINT_RUNBOOK.md").read_text(
            encoding="utf-8"
        )
        ledger = (REPO_ROOT / "docs" / "EXTERNAL_EVIDENCE_LEDGER.md").read_text(
            encoding="utf-8"
        )

        for content in (start_here, docs_readme, roadmap):
            self.assertIn("EXTERNAL_EVIDENCE_SPRINT_RUNBOOK.md", content)
            self.assertIn("EXTERNAL_EVIDENCE_LEDGER.md", content)

        self.assertIn("docs/EXTERNAL_EVIDENCE_SPRINT_RUNBOOK.md", root_readme)
        self.assertIn("docs/EXTERNAL_EVIDENCE_LEDGER.md", root_readme)

        for target in (
            "AOA-T-0032",
            "AOA-T-0026",
            "AOA-T-0036",
            "one technique bundle at a time",
            "do not rerun a false-positive lane unless a new public signal exists",
            "python scripts/release_check.py",
            "External Evidence Ledger",
        ):
            self.assertIn(target, runbook)

        for target in (
            "AOA-T-0018",
            "AOA-T-0013",
            "AOA-T-0034",
            "AOA-T-0023",
            "AOA-T-0032",
            "AOA-T-0026",
            "AOA-T-0036",
            "OpenAI Codex issue `#2765`",
            "OpenDAX",
            "Promotion Readiness Matrix",
        ):
            self.assertIn(target, ledger)

    def test_cross_layer_candidates_surface_is_discoverable_from_repo_entrypoints(self) -> None:
        root_readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        docs_readme = (REPO_ROOT / "docs" / "README.md").read_text(encoding="utf-8")
        start_here = (REPO_ROOT / "docs" / "START_HERE.md").read_text(encoding="utf-8")
        roadmap = (REPO_ROOT / "docs" / "DEEP_AUDIT_ROADMAP.md").read_text(encoding="utf-8")

        for content in (root_readme, docs_readme, start_here, roadmap):
            self.assertIn("CROSS_LAYER_TECHNIQUE_CANDIDATES.md", content)

    def test_external_candidates_doc_tracks_clean_top4_wave_backlog(self) -> None:
        candidates = (REPO_ROOT / "docs" / "EXTERNAL_TECHNIQUE_CANDIDATES.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("remaining `13` external donor-derived candidates", candidates)
        self.assertIn("`1` future import here", candidates)
        self.assertIn("AOA-T-0038", candidates)
        self.assertIn("AOA-T-0041", candidates)
        self.assertIn("AOA-T-0042", candidates)
        self.assertIn("AOA-T-0043", candidates)
        self.assertIn("AOA-T-0044", candidates)
        self.assertIn("AOA-T-0045", candidates)
        self.assertIn("AOA-T-0029", candidates)
        self.assertIn("AOA-T-0030", candidates)
        self.assertIn("AOA-T-0031", candidates)
        self.assertIn("AOA-T-0032", candidates)
        self.assertIn("project_memory_bootstrap", candidates)

    def test_cross_layer_candidates_doc_accounts_for_full_seed_donor_matrix(self) -> None:
        candidates = (
            REPO_ROOT / "docs" / "CROSS_LAYER_TECHNIQUE_CANDIDATES.md"
        ).read_text(encoding="utf-8")

        self.assertIn("full `24` technique-shaped candidate names", candidates)
        self.assertIn("`6` already staged elsewhere", candidates)
        self.assertIn("`10` landed from this wave map", candidates)
        self.assertIn("`0` future import here", candidates)
        self.assertIn("`2` hold because overlap", candidates)
        self.assertIn("`3` needs layer incubation before distillation here", candidates)
        self.assertIn("`3` substrate or architecture pattern, not yet a technique", candidates)

        rows = re.findall(r"^\| `([^`]+)` \|", candidates, flags=re.MULTILINE)
        self.assertEqual(24, len(rows))
        self.assertEqual(24, len(set(rows)))
        self.assertIn("AOA-T-0040", candidates)
        self.assertIn("AOA-T-0041", candidates)
        self.assertIn("AOA-T-0042", candidates)
        self.assertIn("AOA-T-0043", candidates)
        self.assertIn("AOA-T-0044", candidates)
        self.assertIn("AOA-T-0045", candidates)

        for target in (
            "skill-marketplace-curation",
            "versionable-session-transcripts",
            "review-gated-history-derived-instructions",
            "phase-synchronized-agent-handoff",
            "versioned-agent-registry-contract",
            "bounded-specialist-generation",
            "review-gated-execution-history-distillation",
            "one-command-service-lifecycle",
            "upstream-skill-health-checking",
            "skill-vs-command-boundary",
            "witness-trace-as-reviewable-artifact",
            "profile-preset-composition",
            "render-truth-before-startup",
            "contextual-host-doctor",
            "baseline-first-additive-profile-benchmarks",
            "multi-source-primary-input-provenance",
            "progressive-skill-discovery",
            "bounded-counterpart-edge-projection",
            "temperature-gated-writeback",
            "checkpoint-cohort-rollout",
            "witness-to-compost-promotion",
            "model-tier-state-machine",
            "cross-service-sla-normalization",
            "bridge-ready-retrieval-axis",
        ):
            self.assertIn(target, rows)

    def test_phase_sync_seed_has_bounded_narrowing_slice(self) -> None:
        candidates = (REPO_ROOT / "docs" / "EXTERNAL_TECHNIQUE_CANDIDATES.md").read_text(
            encoding="utf-8"
        )

        for target in (
            "## Current Narrowing Slice: `phase_sync_for_agents`",
            "`phase-synchronized-agent-handoff`",
            "### Current donor read stays no-go",
            "public evidence refresh checked on `2026-03-23` across the GitHub README and `agentwise-docs.vercel.app` home",
            "one explicit handoff artifact or status packet",
            "public donor signals currently visible are `phase-based synchronization across all agents` and `Phase Controller`",
            "`Smart Model Router`",
            "`SharedContextServer`",
            "named phase boundary: partial only",
            "handoff packet: missing",
            "continuation permission: missing",
            "stop, return, or escalation rule: missing",
            "`checkpoint`, `handoff`, and `packet` still do not appear in the public GitHub README or docs home",
            "model routing",
            "shared context server or token optimization",
            "AOA-T-0001",
            "AOA-T-0023",
            "bounded-specialist-generation",
            "`notes/external-origin.md`",
            "`notes/external-import-review.md`",
        ):
            self.assertIn(target, candidates)

    def test_external_candidates_doc_describes_swarm_execution_roles(self) -> None:
        candidates = (REPO_ROOT / "docs" / "EXTERNAL_TECHNIQUE_CANDIDATES.md").read_text(
            encoding="utf-8"
        )

        for target in (
            "the main agent owns wave boundaries, final wording, the cross-doc sequence, shared generated-surface sync, and `python scripts/release_check.py`",
            "execution role: keep [AOA-T-0038]",
            "execution role: keep [AOA-T-0041]",
            "[AOA-T-0043]",
            "[AOA-T-0044]",
            "[AOA-T-0045]",
            "execution role: keep [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) as the post-capture transcript-shaping anchor",
            "Shared generated surfaces should be synchronized only after the bundle draft is merge-ready, and only by the main agent.",
        ):
            self.assertIn(target, candidates)

    def test_cross_layer_candidates_doc_describes_exact_wave_execution_order(self) -> None:
        candidates = (
            REPO_ROOT / "docs" / "CROSS_LAYER_TECHNIQUE_CANDIDATES.md"
        ).read_text(encoding="utf-8")

        for target in (
            "1. `profile-preset-composition`",
            "2. `render-truth-before-startup`",
            "3. `contextual-host-doctor`",
            "4. `one-command-service-lifecycle`",
            "5. `baseline-first-additive-profile-benchmarks`",
            "1. `skill-vs-command-boundary`",
            "2. `skill-marketplace-curation`",
            "3. `upstream-skill-health-checking`",
            "4. `multi-source-primary-input-provenance`",
            "if `multi-source-primary-input-provenance` starts sounding like bridge architecture or retrieval ranking",
            "1. `versionable-session-transcripts` (landed as [AOA-T-0044]",
            "2. `witness-trace-as-reviewable-artifact` (landed as [AOA-T-0045]",
            "`AOA-T-0026` keeps ownership of whether sessions are captured",
            "[AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) now owns transcript versionability, readable packaging, redactable export, and comparison-ready transcript shaping over an already-saved artifact",
            "[AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) now owns witness export, citation, and review-packet discipline over an already-saved artifact instead of witness runtime behavior or memory writeback",
            "if a draft still needs `save sessions locally` or `derive future instructions` to explain its value",
            "Wave C is now fully landed across the external and cross-layer intake surfaces",
        ):
            self.assertIn(target, candidates)

    def test_deep_audit_roadmap_describes_swarm_future_import_execution_pack(self) -> None:
        roadmap = (REPO_ROOT / "docs" / "DEEP_AUDIT_ROADMAP.md").read_text(
            encoding="utf-8"
        )

        for target in (
            "main agent owns wave boundaries, final wording, intake/roadmap sync, shared generated surfaces, and `python scripts/release_check.py`",
            "Wave A: `profile-preset-composition`, `render-truth-before-startup`, `contextual-host-doctor`, `one-command-service-lifecycle`, `baseline-first-additive-profile-benchmarks`",
            "Wave B: `skill-vs-command-boundary`, `skill-marketplace-curation`, `upstream-skill-health-checking`, `multi-source-primary-input-provenance`",
            "[AOA-T-0041]",
            "[AOA-T-0042]",
            "[AOA-T-0043]",
            "[AOA-T-0044]",
            "[AOA-T-0045]",
            "minimum packet shape: `phase/checkpoint`, `done`, `blocked`, `next action`, `next owner`, `entry/exit condition`, and `stop/return/escalation`",
            "[AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) keeps ownership of session capture, project-scoped persistence, and local-first artifact availability itself",
            "selected conversations saved into one Markdown document, review or edit before saving, and timestamped transcript artifacts ready for code review or knowledge sharing",
            "any future transcript-history sibling still fails the seam if its value proposition is merely `save sessions locally` instead of shaping or packaging an already-saved transcript for review",
            "[AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) now owns export/review/citation discipline for one structured witness trace plus summary without becoming a new memory-object kind",
            "any future witness-history sibling still fails the seam if it needs runtime witness generation, memory writeback, or future-instruction derivation to explain its value",
            "the latest public `agentwise` read exposes `phase-based synchronization across all agents` and `Phase Controller`",
            "donor evidence refresh checked on `2026-03-23` still reaches only a partial phase-boundary signal",
            "public GitHub README and docs home still do not expose `checkpoint`, `handoff`, or `packet`",
        ):
            self.assertIn(target, roadmap)

    def test_kag_source_lift_family_has_second_context_and_readiness_notes(self) -> None:
        catalog = validate_repo.read_json(REPO_ROOT / "generated" / "technique_catalog.json")
        entries_by_id = {entry["id"]: entry for entry in catalog["techniques"]}

        expected_ids = (
            "AOA-T-0018",
            "AOA-T-0019",
            "AOA-T-0020",
            "AOA-T-0021",
            "AOA-T-0022",
        )

        for technique_id in expected_ids:
            with self.subTest(technique_id=technique_id):
                evidence = {
                    item["kind"]: item["path"] for item in entries_by_id[technique_id]["evidence"]
                }
                self.assertEqual("notes/origin-evidence.md", evidence["origin_evidence"])
                self.assertEqual("notes/second-context-adaptation.md", evidence["second_context"])
                self.assertEqual("notes/canonical-readiness.md", evidence["canonical_readiness"])

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

        self.assertEqual(12, len(surfaces))
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
                "Surface Types",
                "Recommended Reading Paths",
                "Companion Repository Surfaces",
                "Notes",
            ),
            surfaces_by_path["docs/README.md"].top_level_sections,
        )
        self.assertEqual(
            (
                "[Unreleased]",
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
        self.assertEqual(12, len(actual_full["docs"]))
        docs_by_id = {doc["doc_id"]: doc for doc in actual_full["docs"]}
        self.assertEqual(
            "entrypoint/map",
            docs_by_id["ecosystem_context"]["surface_group"],
        )

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
        self.assertIn("docs/START_HERE.md", repo_doc_surfaces)
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

        self.assertIn("START_HERE.md", docs_readme)
        self.assertIn("ECOSYSTEM_CONTEXT.md", docs_readme)
        self.assertIn("docs/START_HERE.md", readme)
        self.assertIn("docs/ECOSYSTEM_CONTEXT.md", readme)
        self.assertIn("docs/START_HERE.md", changelog)
        self.assertIn("START_HERE.md", kag_source_guide)
        self.assertIn("START_HERE.md", releasing)
        self.assertIn("REPO_DOC_SURFACES.md", docs_readme)
        self.assertIn("repo_doc_surface_manifest.json", docs_readme)
        self.assertIn("12 authoritative repo docs/status files", docs_readme)
        self.assertIn("REPO_DOC_SURFACE_LIFT_GUIDE.md", docs_readme)
        self.assertIn("KAG_SOURCE_LIFT_SEMANTIC_REVIEW.md", docs_readme)
        self.assertIn("KAG_SOURCE_LIFT_SEMANTIC_REVIEW.md", readme)
        self.assertIn("KAG_SOURCE_LIFT_SEMANTIC_REVIEW.md", kag_source_guide)
        self.assertIn("docs/REPO_DOC_SURFACES.md", readme)
        self.assertIn("generated/repo_doc_surface_manifest.json", readme)
        self.assertIn("docs/REPO_DOC_SURFACE_LIFT_GUIDE.md", readme)
        self.assertIn("REPO_DOC_SURFACES.md", changelog)
        self.assertIn("repo_doc_surface_manifest.json", changelog)
        self.assertIn("REPO_DOC_SURFACE_LIFT_GUIDE.md", changelog)
        self.assertIn("repo_doc_surface_manifest.json", kag_source_guide)
        self.assertIn("REPO_DOC_SURFACE_LIFT_GUIDE.md", kag_source_guide)
        self.assertIn("REPO_DOC_SURFACES.md", kag_source_guide)
        self.assertIn("python scripts/release_check.py", readme)
        self.assertIn("python scripts/validate_repo.py", readme)
        self.assertIn("python -m unittest discover -s tests", readme)
        self.assertIn("python scripts/release_check.py", releasing)
        self.assertIn("python scripts/build_repo_doc_surface_manifest.py", releasing)
        self.assertIn("python scripts/build_kag_export.py", releasing)
        self.assertIn("python scripts/build_shadow_review_manifest.py", releasing)

    def test_selection_and_semantic_review_guides_are_discoverable_and_validator_backed(self) -> None:
        docs_readme = (REPO_ROOT / "docs" / "README.md").read_text(encoding="utf-8")
        selection = (REPO_ROOT / "docs" / "TECHNIQUE_SELECTION.md").read_text(encoding="utf-8")
        patterns = (REPO_ROOT / "docs" / "SELECTION_PATTERNS.md").read_text(encoding="utf-8")

        self.assertIn("docs/TECHNIQUE_SELECTION_GUIDE.md", validate_repo.REQUIRED_SELECTION_FILES)
        self.assertIn(
            "docs/SEMANTIC_REVIEW_GUIDE.md",
            validate_repo.REQUIRED_SEMANTIC_REVIEW_GUIDE_FILES,
        )
        self.assertIn("TECHNIQUE_SELECTION_GUIDE.md", docs_readme)
        self.assertIn("SEMANTIC_REVIEW_GUIDE.md", docs_readme)
        self.assertIn("Technique Selection Guide", selection)
        self.assertIn("Technique Selection Guide", patterns)
        self.assertIn("Semantic Review Guide", patterns)

    def test_docs_readme_reader_paths_match_current_entrypoint_contract(self) -> None:
        docs_readme = (REPO_ROOT / "docs" / "README.md").read_text(encoding="utf-8")

        self.assertIn(
            "1. [README](../README.md)\n2. [Start Here](START_HERE.md)\n3. [TECHNIQUE_INDEX](../TECHNIQUE_INDEX.md)\n4. [Technique Selection](TECHNIQUE_SELECTION.md)",
            docs_readme,
        )
        self.assertIn("12 authoritative repo docs/status files", docs_readme)
        self.assertIn("one family guide such as", docs_readme)
        self.assertIn("one reader or manifest such as", docs_readme)
        self.assertIn("one reusable lift bundle in `../techniques/docs/`", docs_readme)

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
            "docs/KAG_EXPORT.md",
            "docs/TECHNIQUE_SECTIONS.md",
            "docs/TECHNIQUE_SECTION_LIFT_GUIDE.md",
            "docs/TECHNIQUE_CHECKLISTS.md",
            "docs/TECHNIQUE_CHECKLIST_LIFT_GUIDE.md",
            "docs/TECHNIQUE_EXAMPLES.md",
            "docs/TECHNIQUE_EXAMPLE_LIFT_GUIDE.md",
            "docs/EVIDENCE_NOTE_SURFACES.md",
            "generated/kag_export.json",
            "generated/kag_export.min.json",
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
            "python scripts/build_kag_export.py",
            "docs/KAG_EXPORT.md",
            "generated/kag_export.json",
            "generated/kag_export.min.json",
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
        self.assertIn("TECHNIQUE_CAPSULES.md", (REPO_ROOT / "docs" / "START_HERE.md").read_text(encoding="utf-8"))
        self.assertIn("python scripts/build_capsules.py", releasing)
        self.assertIn("python scripts/release_check.py", releasing)
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
        self.assertIn("TECHNIQUE_SELECTION_GUIDE.md", docs_readme)
        self.assertIn("SEMANTIC_REVIEW_GUIDE.md", docs_readme)
        self.assertIn("AGENT_WORKFLOWS_CORE_SEMANTIC_REVIEW.md", docs_readme)
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
        self.assertEqual(25, adverse_note_count)

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


class ValidateQuestbookSurfaceTests(unittest.TestCase):
    def write_valid_surface(self, repo_root: Path) -> None:
        write_text(
            repo_root / "QUESTBOOK.md",
            (REPO_ROOT / "QUESTBOOK.md").read_text(encoding="utf-8"),
        )
        write_text(
            repo_root / "docs" / "QUESTBOOK_TECHNIQUE_INTEGRATION.md",
            (REPO_ROOT / "docs" / "QUESTBOOK_TECHNIQUE_INTEGRATION.md").read_text(
                encoding="utf-8"
            ),
        )
        write_text(
            repo_root / "schemas" / "quest.schema.json",
            (REPO_ROOT / "schemas" / "quest.schema.json").read_text(encoding="utf-8"),
        )
        write_text(
            repo_root / "schemas" / "quest_dispatch.schema.json",
            (REPO_ROOT / "schemas" / "quest_dispatch.schema.json").read_text(encoding="utf-8"),
        )
        for quest_path in sorted((REPO_ROOT / "quests").glob("AOA-TECH-Q-*.yaml")):
            quest_id = quest_path.stem
            write_text(
                repo_root / "quests" / f"{quest_id}.yaml",
                (REPO_ROOT / "quests" / f"{quest_id}.yaml").read_text(encoding="utf-8"),
            )
        write_text(
            repo_root / "generated" / "quest_catalog.min.json",
            (REPO_ROOT / "generated" / "quest_catalog.min.json").read_text(
                encoding="utf-8"
            ),
        )
        write_text(
            repo_root / "generated" / "quest_dispatch.min.json",
            (REPO_ROOT / "generated" / "quest_dispatch.min.json").read_text(
                encoding="utf-8"
            ),
        )
        write_text(
            repo_root / "generated" / "quest_catalog.min.example.json",
            (REPO_ROOT / "generated" / "quest_catalog.min.example.json").read_text(
                encoding="utf-8"
            ),
        )
        write_text(
            repo_root / "generated" / "quest_dispatch.min.example.json",
            (REPO_ROOT / "generated" / "quest_dispatch.min.example.json").read_text(
                encoding="utf-8"
            ),
        )

    def test_valid_questbook_surface_passes(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir) / "aoa-techniques"
            self.write_valid_surface(repo_root)

            validate_repo.validate_questbook_surface(repo_root)

    def test_additive_second_wave_quest_is_projected(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir) / "aoa-techniques"
            self.write_valid_surface(repo_root)

            catalog_ids = [
                entry["id"] for entry in validate_repo.build_quest_catalog_projection(repo_root)
            ]
            dispatch_ids = [
                entry["id"] for entry in validate_repo.build_quest_dispatch_projection(repo_root)
            ]

        self.assertIn("AOA-TECH-Q-0005", catalog_ids)
        self.assertIn("AOA-TECH-Q-0005", dispatch_ids)

    def test_missing_quest_file_fails(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir) / "aoa-techniques"
            self.write_valid_surface(repo_root)
            (repo_root / "quests" / "AOA-TECH-Q-0003.yaml").unlink()

            with self.assertRaisesRegex(
                validate_repo.ValidationError,
                "AOA-TECH-Q-0003.yaml: missing required file",
            ):
                validate_repo.validate_questbook_surface(repo_root)

    def test_wrong_repo_value_fails(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir) / "aoa-techniques"
            self.write_valid_surface(repo_root)
            write_text(
                repo_root / "quests" / "AOA-TECH-Q-0002.yaml",
                (repo_root / "quests" / "AOA-TECH-Q-0002.yaml")
                .read_text(encoding="utf-8")
                .replace("repo: aoa-techniques", "repo: aoa-skills"),
            )

            with self.assertRaisesRegex(
                validate_repo.ValidationError,
                "repo must be 'aoa-techniques'",
            ):
                validate_repo.validate_questbook_surface(repo_root)

    def test_dispatch_example_drift_fails(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir) / "aoa-techniques"
            self.write_valid_surface(repo_root)
            write_text(
                repo_root / "generated" / "quest_dispatch.min.example.json",
                (repo_root / "generated" / "quest_dispatch.min.example.json")
                .read_text(encoding="utf-8")
                .replace(
                    '"source_path": "quests/AOA-TECH-Q-0004.yaml"',
                    '"source_path": "quests/AOA-TECH-Q-9999.yaml"',
                ),
            )

            with self.assertRaisesRegex(
                validate_repo.ValidationError,
                "example dispatch must stay aligned",
            ):
                validate_repo.validate_questbook_surface(repo_root)

    def test_missing_live_catalog_fails(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir) / "aoa-techniques"
            self.write_valid_surface(repo_root)
            (repo_root / "generated" / "quest_catalog.min.json").unlink()

            with self.assertRaisesRegex(
                validate_repo.ValidationError,
                "quest_catalog.min.json: missing required file",
            ):
                validate_repo.validate_questbook_surface(repo_root)

    def test_fixture_live_catalog_drift_fails(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir) / "aoa-techniques"
            self.write_valid_surface(repo_root)
            write_text(
                repo_root / "generated" / "quest_catalog.min.example.json",
                (repo_root / "generated" / "quest_catalog.min.example.json")
                .read_text(encoding="utf-8")
                .replace(
                    '"source_path": "quests/AOA-TECH-Q-0004.yaml"',
                    '"source_path": "quests/AOA-TECH-Q-9999.yaml"',
                ),
            )

            with self.assertRaisesRegex(
                validate_repo.ValidationError,
                "example catalog must stay aligned",
            ):
                validate_repo.validate_questbook_surface(repo_root)

    def test_live_dispatch_drift_fails(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir) / "aoa-techniques"
            self.write_valid_surface(repo_root)
            write_text(
                repo_root / "generated" / "quest_dispatch.min.json",
                (repo_root / "generated" / "quest_dispatch.min.json")
                .read_text(encoding="utf-8")
                .replace(
                    '"source_path":"quests/AOA-TECH-Q-0004.yaml"',
                    '"source_path":"quests/AOA-TECH-Q-9999.yaml"',
                ),
            )

            with self.assertRaisesRegex(
                validate_repo.ValidationError,
                "quest_dispatch.min.json: dispatch entry 'AOA-TECH-Q-0004' must stay aligned",
            ):
                validate_repo.validate_questbook_surface(repo_root)

    def test_missing_activation_fails_with_validation_error(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir) / "aoa-techniques"
            self.write_valid_surface(repo_root)
            quest_path = repo_root / "quests" / "AOA-TECH-Q-0001.yaml"
            quest_text = quest_path.read_text(encoding="utf-8")
            write_text(
                quest_path,
                quest_text[: quest_text.index("activation:")]
                + quest_text[quest_text.index("anchor_ref:") :],
            )

            with self.assertRaisesRegex(
                validate_repo.ValidationError,
                "quests/AOA-TECH-Q-0001.yaml: quest must define object field 'activation'",
            ):
                validate_repo.validate_questbook_surface(repo_root)

    def test_live_dispatch_optional_field_must_match_schema(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir) / "aoa-techniques"
            self.write_valid_surface(repo_root)
            dispatch_path = repo_root / "generated" / "quest_dispatch.min.json"
            dispatch_payload = json.loads(dispatch_path.read_text(encoding="utf-8"))
            dispatch_payload[0]["fallback_tier"] = None
            write_text(dispatch_path, json.dumps(dispatch_payload, indent=2) + "\n")

            with self.assertRaisesRegex(
                validate_repo.ValidationError,
                "generated/quest_dispatch.min.json\\[0\\]\\.fallback_tier: value must be a string",
            ):
                validate_repo.validate_questbook_surface(repo_root)

    def test_example_dispatch_optional_field_must_match_schema(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir) / "aoa-techniques"
            self.write_valid_surface(repo_root)
            dispatch_path = repo_root / "generated" / "quest_dispatch.min.example.json"
            dispatch_payload = json.loads(dispatch_path.read_text(encoding="utf-8"))
            dispatch_payload[0]["wrapper_class"] = None
            write_text(dispatch_path, json.dumps(dispatch_payload, indent=2) + "\n")

            with self.assertRaisesRegex(
                validate_repo.ValidationError,
                "generated/quest_dispatch.min.example.json\\[0\\]\\.wrapper_class: value must be a string",
            ):
                validate_repo.validate_questbook_surface(repo_root)


class TechniqueFeatSchemaTests(unittest.TestCase):
    def test_example_payload_matches_feat_schema(self) -> None:
        schema = json.loads(
            (REPO_ROOT / "schemas" / "technique_feat_catalog.schema.json").read_text(
                encoding="utf-8"
            )
        )
        payload = json.loads(
            (REPO_ROOT / "generated" / "technique_feat_cards.min.example.json").read_text(
                encoding="utf-8"
            )
        )

        Draft202012Validator.check_schema(schema)
        Draft202012Validator(schema).validate(payload)


if __name__ == "__main__":
    unittest.main()
