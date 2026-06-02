from __future__ import annotations

import sys
from pathlib import Path

SUPPORT_DIR = Path(__file__).resolve().parent / "support"
if str(SUPPORT_DIR) not in sys.path:
    sys.path.insert(0, str(SUPPORT_DIR))

from validate_repo_fixtures import *


class ValidateRepoSourceContractTests(unittest.TestCase):
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

    def test_topology_ui_substrate_does_not_match_short_substrings(self) -> None:
        self.assertNotIn("ui", validate_repo.TOPOLOGY_KEYWORD_RULES["substrate"]["ui"])
        self.assertEqual(
            [],
            validate_repo.matched_keywords(
                "build guide for bounded docs",
                validate_repo.TOPOLOGY_KEYWORD_RULES["substrate"]["ui"],
            ),
        )

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

    def test_expected_parent_domain_accepts_legacy_domain_layout(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            technique_dir = repo_root / "techniques" / "agent-workflows" / "demo"
            technique_dir.mkdir(parents=True)

            self.assertEqual(
                "agent-workflows",
                validate_repo.expected_parent_domain_for_technique(repo_root, technique_dir),
            )

    def test_expected_parent_domain_accepts_tree_trunk_layout(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            technique_dir = (
                repo_root
                / "techniques"
                / "continuity"
                / "review-compaction"
                / "demo"
            )
            technique_dir.mkdir(parents=True)

            self.assertIsNone(
                validate_repo.expected_parent_domain_for_technique(repo_root, technique_dir)
            )

    def test_expected_parent_domain_rejects_unsupported_tree_root(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            technique_dir = repo_root / "techniques" / "misc" / "review-compaction" / "demo"
            technique_dir.mkdir(parents=True)

            with self.assertRaises(validate_repo.ValidationError):
                validate_repo.expected_parent_domain_for_technique(repo_root, technique_dir)

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

    def test_validate_sections_accepts_optional_template_sections_in_fixed_slots(self) -> None:
        body = build_required_section_body(validate_repo.TECHNIQUE_SECTION_ORDER)

        validate_repo.validate_sections(body, Path("TECHNIQUE.md"))

    def test_validate_sections_rejects_optional_template_section_out_of_order(self) -> None:
        headings = list(validate_repo.REQUIRED_SECTIONS)
        headings.insert(4, "Atomic move")
        body = build_required_section_body(tuple(headings))

        with self.assertRaises(validate_repo.ValidationError):
            validate_repo.validate_sections(body, Path("TECHNIQUE.md"))

    def test_validate_sections_rejects_duplicate_optional_template_section(self) -> None:
        headings = ("Intent", "Atomic move", "Atomic move") + validate_repo.REQUIRED_SECTIONS[1:]
        body = build_required_section_body(headings)

        with self.assertRaises(validate_repo.ValidationError):
            validate_repo.validate_sections(body, Path("TECHNIQUE.md"))

    def test_validate_sections_ignores_fenced_markdown_headings(self) -> None:
        body = build_required_section_body().replace(
            "Bounded content for example.",
            "```md\n## Example inside code\n### Not a subsection either\n```\n\nBounded content for example.",
        )

        validate_repo.validate_sections(body, Path("TECHNIQUE.md"))

    def test_external_import_runbook_is_discoverable_and_operator_complete(self) -> None:
        start_here = (REPO_ROOT / "docs" / "START_HERE.md").read_text(encoding="utf-8")
        docs_readme = (REPO_ROOT / "docs" / "README.md").read_text(encoding="utf-8")
        mechanics_readme = (REPO_ROOT / "mechanics" / "README.md").read_text(encoding="utf-8")
        contributing = (REPO_ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
        runbook = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "external-import-runbook"
            / "README.md"
        ).read_text(encoding="utf-8")

        self.assertIn("mechanics/README.md", start_here)
        self.assertIn("Mechanics", docs_readme)
        self.assertIn("External Import Runbook", mechanics_readme)
        self.assertIn("mechanics/distillation/parts/external-import-runbook/README.md", mechanics_readme)
        self.assertIn("mechanics/distillation/parts/external-import-runbook/README.md", contributing)
        for target in (
            "nearest existing technique or overlap watch",
            "what stays out of the donor",
            "expected evidence notes",
            "expected generated surfaces",
            "downstream repo impact",
            "[AGENTS](../../../../AGENTS.md#validation)",
            "[RELEASING](../../../../docs/RELEASING.md)",
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
            REPO_ROOT / "docs" / "source-lift" / "EVIDENCE_NOTE_PROVENANCE_GUIDE.md"
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

    def test_evidence_note_guide_references_current_note_templates(self) -> None:
        guide = (
            REPO_ROOT / "docs" / "source-lift" / "EVIDENCE_NOTE_PROVENANCE_GUIDE.md"
        ).read_text(encoding="utf-8")

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
        shadow_guide = (
            REPO_ROOT / "docs" / "review" / "TECHNIQUE_SHADOW_GUIDE.md"
        ).read_text(encoding="utf-8")
        risk_guide = (
            REPO_ROOT / "docs" / "source-lift" / "RISK_AND_NEGATIVE_EFFECT_LIFT_GUIDE.md"
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
        self.assertEqual(107, len(technique_paths))

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
        kind_values = {entry["kind"] for entry in catalog["techniques"]}

        for entry in catalog["techniques"]:
            status_counts[entry["status"]] = status_counts.get(entry["status"], 0) + 1

        self.assertEqual(
            {
                "agent-workflows",
                "docs",
                "evaluation",
                "system-recovery",
                "validation-patterns",
                "history",
            },
            domain_values,
        )
        self.assertEqual(validate_repo.KIND_VALUES, kind_values)
        self.assertEqual(98, status_counts["canonical"])
        self.assertEqual(9, status_counts["promoted"])

    def test_telemetry_guardrail_status_language_is_consistent(self) -> None:
        technique = (
            REPO_ROOT
            / "techniques"
            / "proof"
            / "published-summary"
            / "telemetry-integrity-snapshot"
            / "TECHNIQUE.md"
        ).read_text(encoding="utf-8")
        checklist = (
            REPO_ROOT
            / "techniques"
            / "proof"
            / "published-summary"
            / "telemetry-integrity-snapshot"
            / "checks"
            / "telemetry-integrity-checklist.md"
        ).read_text(encoding="utf-8")
        minimal_example = (
            REPO_ROOT
            / "techniques"
            / "proof"
            / "published-summary"
            / "telemetry-integrity-snapshot"
            / "examples"
            / "minimal-telemetry-integrity-snapshot.md"
        ).read_text(encoding="utf-8")
        object_store_example = (
            REPO_ROOT
            / "techniques"
            / "proof"
            / "published-summary"
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
            / "instruction"
            / "docs-boundary"
            / "source-of-truth-layout"
            / "checks"
            / "doc-role-checklist.md"
        ).read_text(encoding="utf-8")
        technique = (
            REPO_ROOT
            / "techniques"
            / "instruction"
            / "docs-boundary"
            / "source-of-truth-layout"
            / "TECHNIQUE.md"
        ).read_text(encoding="utf-8")

        self.assertIn("delegated external runbook", checklist)
        self.assertIn("delegated external tracker", checklist)
        self.assertIn("delegated external planning surface", checklist)
        self.assertIn("delegated elsewhere", technique)

    def test_canonical_bundles_have_adverse_effects_reviews_and_promoted_bundles_do_not(self) -> None:
        schema_store = validate_repo.load_schema_store(REPO_ROOT)
        records = validate_repo.collect_techniques(REPO_ROOT, schema_store)
        canonical_records = [record for record in records if record.status == "canonical"]
        promoted_records = [record for record in records if record.status == "promoted"]

        self.assertEqual(98, len(canonical_records))

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

    def test_start_here_routes_repo_only_reading_paths(self) -> None:
        start_here = (REPO_ROOT / "docs" / "START_HERE.md").read_text(encoding="utf-8")

        for target in (
            "plan-diff-apply-verify-report/TECHNIQUE.md",
            "TECHNIQUE_SELECTION_GUIDE.md",
            "TECHNIQUE_KIND_GUIDE.md",
            "TECHNIQUE_KIND_HANDOFF_PACK.md",
            "TECHNIQUE_SELECTION.md",
            "SELECTION_PATTERNS.md",
            "TECHNIQUE_INDEX.md",
            "TECHNIQUE_CAPSULES.md",
            "REPO_DOC_SURFACES.md",
            "KAG_SOURCE_LIFT_GUIDE.md",
            "SEMANTIC_REVIEW_GUIDE.md",
            "mechanics/README.md",
            "mechanics/audit/README.md",
            "mechanics/distillation/README.md",
            "aoa-skills",
            "aoa-evals",
            "aoa-routing",
            "current corpus posture is generated",
            "../generated/technique_catalog.min.json",
            "domain/kind/status split",
            "machine-readable corpus view",
            "../AGENTS.md#validation",
            "RELEASING.md",
            "owning command surface",
        ):
            self.assertIn(target, start_here)

    def test_external_evidence_surfaces_are_discoverable_and_operator_complete(self) -> None:
        start_here = (REPO_ROOT / "docs" / "START_HERE.md").read_text(encoding="utf-8")
        docs_readme = (REPO_ROOT / "docs" / "README.md").read_text(encoding="utf-8")
        mechanics_readme = (REPO_ROOT / "mechanics" / "README.md").read_text(encoding="utf-8")
        runbook = (
            REPO_ROOT
            / "mechanics"
            / "audit"
            / "parts"
            / "external-evidence-sprint-runbook"
            / "README.md"
        ).read_text(encoding="utf-8")
        ledger = (
            REPO_ROOT
            / "mechanics"
            / "audit"
            / "parts"
            / "external-evidence-ledger"
            / "README.md"
        ).read_text(encoding="utf-8")

        self.assertIn("mechanics/README.md", start_here)
        self.assertIn("mechanics/README.md", docs_readme)
        self.assertIn("parts/external-evidence-sprint-runbook/README.md", mechanics_readme)
        self.assertIn("parts/external-evidence-ledger/README.md", mechanics_readme)

        for target in (
            "AOA-T-0032",
            "AOA-T-0026",
            "AOA-T-0036",
            "one technique bundle at a time",
            "do not rerun a false-positive lane unless a new public signal exists",
            "[AGENTS](../../../../AGENTS.md#validation)",
            "[RELEASING](../../../../docs/RELEASING.md)",
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
        docs_readme = (REPO_ROOT / "docs" / "README.md").read_text(encoding="utf-8")
        start_here = (REPO_ROOT / "docs" / "START_HERE.md").read_text(encoding="utf-8")
        mechanics_readme = (REPO_ROOT / "mechanics" / "README.md").read_text(encoding="utf-8")

        self.assertIn("mechanics/README.md", docs_readme)
        self.assertIn("mechanics/distillation/README.md", start_here)
        self.assertIn(
            "mechanics/distillation/parts/cross-layer-candidate-ledger/README.md",
            mechanics_readme,
        )

    def test_external_candidates_doc_tracks_clean_top4_wave_backlog(self) -> None:
        candidates = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "external-candidate-ledger"
            / "README.md"
        ).read_text(encoding="utf-8")

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
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "cross-layer-candidate-ledger"
            / "README.md"
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
        candidates = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "external-candidate-ledger"
            / "README.md"
        ).read_text(encoding="utf-8")
        receipt = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "legacy"
            / "raw"
            / "EXTERNAL_CANDIDATE_LEDGER_2026-05-01_PRE_PRUNE.md"
        ).read_text(encoding="utf-8")

        for target in (
            "## Current Active Lane",
            "`phase_sync_for_agents`",
            "`phase-synchronized-agent-handoff`",
            "standalone handoff contract",
            "phase boundary, packet, continuation permission, and stop/return/escalation rule",
            "routing, shared context server behavior",
            "shared context server behavior",
            "AOA-T-0001",
            "AOA-T-0023",
            "bounded-specialist-generation",
            "## Reopen Gate",
            "Atom/topology gate",
            "Boundary/portability gate",
        ):
            self.assertIn(target, candidates)

        for target in (
            "## Current Narrowing Slice: `phase_sync_for_agents`",
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
            "`notes/external-origin.md`",
            "`notes/external-import-review.md`",
        ):
            self.assertIn(target, receipt)

    def test_external_candidates_doc_describes_swarm_execution_roles(self) -> None:
        candidates = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "external-candidate-ledger"
            / "README.md"
        ).read_text(encoding="utf-8")
        receipt = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "legacy"
            / "raw"
            / "EXTERNAL_CANDIDATE_LEDGER_2026-05-01_PRE_PRUNE.md"
        ).read_text(encoding="utf-8")

        for target in (
            "old wave notes are no longer active execution instructions",
            "landed anchors remain useful for route memory",
            "Wave A external anchor",
            "Wave B external anchor",
            "Wave C external anchor",
            "use the preserved raw receipt",
        ):
            self.assertIn(target, candidates)

        for target in (
            "the main agent owns wave boundaries, final wording, the cross-doc sequence, shared generated-surface sync, and `python scripts/release_check.py`",
            "execution role: keep [AOA-T-0038]",
            "execution role: keep [AOA-T-0041]",
            "[AOA-T-0043]",
            "[AOA-T-0044]",
            "[AOA-T-0045]",
            "execution role: keep [AOA-T-0044](../../../../techniques/history/versionable-session-transcripts/TECHNIQUE.md) as the post-capture transcript-shaping anchor",
            "Shared generated surfaces should be synchronized only after the bundle draft is merge-ready, and only by the main agent.",
        ):
            self.assertIn(target, receipt)

    def test_cross_layer_candidates_doc_describes_exact_wave_execution_order(self) -> None:
        candidates = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "cross-layer-candidate-ledger"
            / "README.md"
        ).read_text(encoding="utf-8")
        receipt = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "legacy"
            / "raw"
            / "CROSS_LAYER_CANDIDATE_LEDGER_2026-05-01_PRE_PRUNE.md"
        ).read_text(encoding="utf-8")

        for target in (
            "## Landed Wave Anchors",
            "If future work needs exact wave execution order, use the preserved raw receipt.",
            "[AOA-T-0044](../../../../techniques/history/history-artifacts/versionable-session-transcripts/TECHNIQUE.md)",
            "[AOA-T-0045](../../../../techniques/history/history-artifacts/witness-trace-as-reviewable-artifact/TECHNIQUE.md)",
            "[AOA-T-0026](../../../../techniques/history/history-artifacts/session-capture-as-repo-artifact/TECHNIQUE.md)",
        ):
            self.assertIn(target, candidates)

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
            "[AOA-T-0044](../../../../techniques/history/versionable-session-transcripts/TECHNIQUE.md) now owns transcript versionability, readable packaging, redactable export, and comparison-ready transcript shaping over an already-saved artifact",
            "[AOA-T-0045](../../../../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) now owns witness export, citation, and review-packet discipline over an already-saved artifact instead of witness runtime behavior or memory writeback",
            "if a draft still needs `save sessions locally` or `derive future instructions` to explain its value",
            "Wave C is now fully landed across the external and cross-layer intake surfaces",
        ):
            self.assertIn(target, receipt)

    def test_deep_audit_roadmap_describes_swarm_future_import_execution_pack(self) -> None:
        roadmap = (
            REPO_ROOT
            / "mechanics"
            / "audit"
            / "legacy"
            / "raw"
            / "ROOT_CLOSURE_AUDIT_ROADMAP_2026-05-03.md"
        ).read_text(encoding="utf-8")

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
            "[AOA-T-0026](techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) keeps ownership of session capture, project-scoped persistence, and local-first artifact availability itself",
            "selected conversations saved into one Markdown document, review or edit before saving, and timestamped transcript artifacts ready for code review or knowledge sharing",
            "any future transcript-history sibling still fails the seam if its value proposition is merely `save sessions locally` instead of shaping or packaging an already-saved transcript for review",
            "[AOA-T-0045](techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) now owns export/review/citation discipline for one structured witness trace plus summary without becoming a new memory-object kind",
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

    def test_shadow_review_docs_follow_bounded_contract(self) -> None:
        reviews = validate_repo.parse_shadow_reviews(REPO_ROOT)
        reviews_by_path = {review.review_path: review for review in reviews}

        self.assertEqual(
            {
                "mechanics/distillation/parts/technique-reform-ingress/reviews/shadow/PUBLISHED_SUMMARY_SHADOW_REVIEW.md",
                "mechanics/distillation/parts/technique-reform-ingress/reviews/shadow/EVALUATION_CHAIN_SHADOW_REVIEW.md",
            },
            set(reviews_by_path),
        )
        self.assertEqual("Pair Map", reviews_by_path["mechanics/distillation/parts/technique-reform-ingress/reviews/shadow/EVALUATION_CHAIN_SHADOW_REVIEW.md"].map_heading)
        self.assertEqual(
            "Cluster Map",
            reviews_by_path["mechanics/distillation/parts/technique-reform-ingress/reviews/shadow/PUBLISHED_SUMMARY_SHADOW_REVIEW.md"].map_heading,
        )
        self.assertTrue(reviews_by_path["mechanics/distillation/parts/technique-reform-ingress/reviews/shadow/EVALUATION_CHAIN_SHADOW_REVIEW.md"].seams)
        self.assertEqual(
            "`clear`",
            reviews_by_path["mechanics/distillation/parts/technique-reform-ingress/reviews/shadow/EVALUATION_CHAIN_SHADOW_REVIEW.md"].overall_outcome,
        )

    def test_repo_doc_surface_specs_are_bounded_and_structurally_valid(self) -> None:
        validate_repo.validate_repo_doc_surface_specs(REPO_ROOT)
        validate_repo.validate_repo_doc_navigation_specs(REPO_ROOT)
        surfaces = validate_repo.parse_repo_doc_surfaces(REPO_ROOT)
        source_paths = {surface.doc_path for surface in surfaces}

        self.assertEqual(20, len(surfaces))
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
                "WALKTHROUGH.md",
                "docs/source-lift/KAG_SOURCE_LIFT_GUIDE.md",
                "mechanics/distillation/parts/technique-reform-ingress/reviews/semantic/PUBLISHED_SUMMARY_SEMANTIC_REVIEW.md",
                "mechanics/distillation/parts/technique-reform-ingress/reviews/shadow/PUBLISHED_SUMMARY_SHADOW_REVIEW.md",
            }.isdisjoint(source_paths)
        )
        self.assertTrue(
            {
                "CHARTER.md",
                "DESIGN.md",
                "DESIGN.AGENTS.md",
                "ROADMAP.md",
                "QUESTBOOK.md",
                "docs/ROOT_SURFACE_LAW.md",
                "docs/TECHNIQUE_ATOM_CONTRACT.md",
                "docs/TECHNIQUE_TOPOLOGY_CONTRACT.md",
                "docs/TECHNIQUE_TREE_CONTRACT.md",
            }.issubset(source_paths)
        )
        for surface in surfaces:
            self.assertTrue(surface.top_level_sections)

    def test_decisions_district_has_local_route_and_template(self) -> None:
        docs_readme = (REPO_ROOT / "docs" / "README.md").read_text(encoding="utf-8")
        decisions_readme = (
            REPO_ROOT / "docs" / "decisions" / "README.md"
        ).read_text(encoding="utf-8")
        decisions_agents = (
            REPO_ROOT / "docs" / "decisions" / "AGENTS.md"
        ).read_text(encoding="utf-8")
        decision_template = (
            REPO_ROOT / "docs" / "decisions" / "TEMPLATE.md"
        ).read_text(encoding="utf-8")
        root_slimming_decision = (
            REPO_ROOT
            / "docs"
            / "decisions"
            / "AOA-TECH-D-0053-root-md-surface-slimming.md"
        ).read_text(encoding="utf-8")

        self.assertIn("decisions/README.md", docs_readme)
        self.assertIn("Decision records explain why", decisions_readme)
        self.assertIn("Current source surfaces define what", decisions_readme)
        self.assertIn("TEMPLATE.md", decisions_agents)
        for heading in (
            "## Options considered",
            "## Source surfaces",
            "## Follow-up route",
        ):
            self.assertIn(heading, decision_template)
            self.assertIn(heading, root_slimming_decision)

    def test_kind_guide_and_handoff_pack_are_discoverable_from_root_docs_and_release_entrypoints(
        self,
    ) -> None:
        docs_readme = (REPO_ROOT / "docs" / "README.md").read_text(encoding="utf-8")
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        start_here = (REPO_ROOT / "docs" / "START_HERE.md").read_text(encoding="utf-8")
        releasing = (REPO_ROOT / "docs" / "RELEASING.md").read_text(encoding="utf-8")

        self.assertIn("TECHNIQUE_KIND_GUIDE.md", docs_readme)
        self.assertIn("TECHNIQUE_KIND_GUIDE.md", start_here)
        self.assertIn("docs/selection/TECHNIQUE_KIND_GUIDE.md", readme)
        self.assertIn("TECHNIQUE_KIND_GUIDE.md", releasing)
        self.assertIn("TECHNIQUE_KIND_HANDOFF_PACK.md", docs_readme)
        self.assertIn("docs/selection/TECHNIQUE_KIND_HANDOFF_PACK.md", readme)
        self.assertIn("`generated` lane, `catalog` group", releasing)
        self.assertIn("generated/technique_kind_manifest.json", releasing)
        self.assertIn("generated/technique_kind_manifest.min.json", releasing)

    def test_technique_atom_contract_is_discoverable_and_template_backed(self) -> None:
        atom_contract = (REPO_ROOT / "docs" / "TECHNIQUE_ATOM_CONTRACT.md").read_text(
            encoding="utf-8"
        )
        decision = (
            REPO_ROOT
            / "docs"
            / "decisions"
            / "AOA-TECH-D-0017-technique-atom-contract.md"
        ).read_text(encoding="utf-8")
        template = (REPO_ROOT / "templates" / "TECHNIQUE.template.md").read_text(
            encoding="utf-8"
        )
        agents = (REPO_ROOT / "AGENTS.md").read_text(encoding="utf-8")
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        start_here = (REPO_ROOT / "docs" / "START_HERE.md").read_text(
            encoding="utf-8"
        )
        docs_readme = (REPO_ROOT / "docs" / "README.md").read_text(encoding="utf-8")

        for target in (
            "one atomic executable move",
            "2-4B model",
            "`1000+` techniques",
            "A skill can orchestrate. A technique should not.",
            "small enough to execute once selected",
            "Capsules should preserve that executable center",
        ):
            self.assertIn(target, atom_contract)

        for surface_name, surface in (
            ("AGENTS.md", agents),
            ("README.md", readme),
            ("docs/START_HERE.md", start_here),
            ("docs/README.md", docs_readme),
        ):
            with self.subTest(surface=surface_name):
                self.assertIn("TECHNIQUE_ATOM_CONTRACT.md", surface)

        self.assertIn("## Atomic move", template)
        self.assertIn("## Small-agent execution shape", template)
        self.assertIn("one atomic executable move", decision)
        self.assertIn("broad mini-skills", decision)

    def test_technique_topology_contract_defines_faceted_classification(self) -> None:
        topology = (REPO_ROOT / "docs" / "TECHNIQUE_TOPOLOGY_CONTRACT.md").read_text(
            encoding="utf-8"
        )
        decision = (
            REPO_ROOT
            / "docs"
            / "decisions"
            / "AOA-TECH-D-0018-technique-topology-contract.md"
        ).read_text(encoding="utf-8")
        atom_contract = (REPO_ROOT / "docs" / "TECHNIQUE_ATOM_CONTRACT.md").read_text(
            encoding="utf-8"
        )
        domain_map = (REPO_ROOT / "docs" / "DOMAIN_MAP.md").read_text(encoding="utf-8")
        kind_guide = (
            REPO_ROOT / "docs" / "selection" / "TECHNIQUE_KIND_GUIDE.md"
        ).read_text(encoding="utf-8")
        selection_guide = (
            REPO_ROOT / "docs" / "selection" / "TECHNIQUE_SELECTION_GUIDE.md"
        ).read_text(encoding="utf-8")
        capsule_guide = (
            REPO_ROOT / "docs" / "selection" / "TECHNIQUE_CAPSULE_GUIDE.md"
        ).read_text(encoding="utf-8")
        template = (REPO_ROOT / "templates" / "TECHNIQUE.template.md").read_text(
            encoding="utf-8"
        )
        agents = (REPO_ROOT / "AGENTS.md").read_text(encoding="utf-8")
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        start_here = (REPO_ROOT / "docs" / "START_HERE.md").read_text(
            encoding="utf-8"
        )
        docs_readme = (REPO_ROOT / "docs" / "README.md").read_text(encoding="utf-8")
        family_scout = validate_repo.read_yaml(
            REPO_ROOT / validate_repo.TECHNIQUE_FAMILY_SCOUT_PATH
        )
        topology_axes = validate_repo.read_yaml(
            REPO_ROOT / validate_repo.TECHNIQUE_TOPOLOGY_AXES_PATH
        )

        for target in (
            "Classification is faceted, not a single tree.",
            "`domain` | authoritative frontmatter",
            "`kind` | authoritative frontmatter",
            "`family` | scout-only",
            "`capability_class` | design axis",
            "`substrate` | design axis",
            "`execution_profile` | design axis",
            "`risk_posture` | design axis",
            "`mechanics/distillation/parts/technique-reform-ingress/config/technique_topology_axes.yaml`",
            "`mechanics/distillation/parts/technique-reform-ingress/reports/technique_topology_scout.md`",
            "coding, documentation, validation, recovery, history, media, tool use",
            "The goal is a corpus that can grow very large",
        ):
            self.assertIn(target, topology)

        for surface in (
            atom_contract,
            domain_map,
            kind_guide,
            selection_guide,
            capsule_guide,
        ):
            self.assertIn("TECHNIQUE_TOPOLOGY_CONTRACT.md", surface)

        for surface_name, surface in (
            ("AGENTS.md", agents),
            ("README.md", readme),
            ("docs/START_HERE.md", start_here),
            ("docs/README.md", docs_readme),
        ):
            with self.subTest(surface=surface_name):
                self.assertIn("TECHNIQUE_TOPOLOGY_CONTRACT.md", surface)

        self.assertIn("## Topology fit", template)
        self.assertEqual("scout-foundation", family_scout["status"])
        self.assertIn(
            "Use family as a library shelf",
            "\n".join(family_scout["core_rules"]),
        )
        self.assertEqual("scout-foundation", topology_axes["status"])
        self.assertEqual(["domain", "kind"], topology_axes["frontmatter_truth_axes"])
        self.assertEqual(
            list(validate_repo.TOPOLOGY_SCOUT_AXIS_ORDER),
            [axis["id"] for axis in topology_axes["axes"]],
        )
        self.assertIn("faceted rather than a single tree", decision)

    def test_selection_and_semantic_review_guides_are_discoverable_and_validator_backed(self) -> None:
        docs_readme = (REPO_ROOT / "docs" / "README.md").read_text(encoding="utf-8")
        selection = (
            REPO_ROOT / "docs" / "readers" / "selection" / "TECHNIQUE_SELECTION.md"
        ).read_text(encoding="utf-8")
        patterns = (
            REPO_ROOT / "docs" / "readers" / "selection" / "SELECTION_PATTERNS.md"
        ).read_text(encoding="utf-8")

        self.assertIn("docs/selection/TECHNIQUE_SELECTION_GUIDE.md", validate_repo.REQUIRED_SELECTION_FILES)
        self.assertIn(
            "docs/review/SEMANTIC_REVIEW_GUIDE.md",
            validate_repo.REQUIRED_SEMANTIC_REVIEW_GUIDE_FILES,
        )
        self.assertIn("TECHNIQUE_SELECTION_GUIDE.md", docs_readme)
        self.assertIn("SEMANTIC_REVIEW_GUIDE.md", docs_readme)
        self.assertIn("Technique Selection Guide", selection)
        self.assertIn("narrow by `kind` second", selection)
        self.assertIn("| technique | kind | status | validation | rigor | summary |", selection)
        self.assertIn("Technique Selection Guide", patterns)
        self.assertIn("Semantic Review Guide", patterns)

    def test_docs_readme_reader_paths_match_current_entrypoint_contract(self) -> None:
        docs_readme = (REPO_ROOT / "docs" / "README.md").read_text(encoding="utf-8")

        self.assertIn(
            "1. [README](../README.md)\n2. [Charter](../CHARTER.md)\n3. [Start Here](START_HERE.md)\n4. [TECHNIQUE_INDEX](../TECHNIQUE_INDEX.md)\n5. [Technique Selection](readers/selection/TECHNIQUE_SELECTION.md)",
            docs_readme,
        )
        self.assertIn("20 authoritative public route/canon/status files", docs_readme)
        self.assertIn("one family guide such as", docs_readme)
        self.assertIn("one reader or manifest such as", docs_readme)
        self.assertIn(
            "one reusable lift bundle in `../techniques/knowledge-lift/kag-source-lift/`",
            docs_readme,
        )

    def test_docs_readme_and_guides_link_to_reusable_lift_family(self) -> None:
        docs_readme = (REPO_ROOT / "docs" / "README.md").read_text(encoding="utf-8")
        kag_source_guide = (
            REPO_ROOT / "docs" / "source-lift" / "KAG_SOURCE_LIFT_GUIDE.md"
        ).read_text(encoding="utf-8")
        shadow_guide = (
            REPO_ROOT / "docs" / "review" / "TECHNIQUE_SHADOW_GUIDE.md"
        ).read_text(encoding="utf-8")
        risk_guide = (
            REPO_ROOT / "docs" / "source-lift" / "RISK_AND_NEGATIVE_EFFECT_LIFT_GUIDE.md"
        ).read_text(encoding="utf-8")
        metadata_guide = (
            REPO_ROOT / "docs" / "source-lift" / "FRONTMATTER_METADATA_SPINE_GUIDE.md"
        ).read_text(encoding="utf-8")
        provenance_guide = (
            REPO_ROOT / "docs" / "source-lift" / "EVIDENCE_NOTE_PROVENANCE_GUIDE.md"
        ).read_text(encoding="utf-8")
        relation_guide = (
            REPO_ROOT / "docs" / "source-lift" / "BOUNDED_RELATION_LIFT_GUIDE.md"
        ).read_text(encoding="utf-8")
        semantic_packets = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "semantic"
            / "README.md"
        ).read_text(encoding="utf-8")
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

        self.assertIn("markdown-technique-section-lift", docs_readme)
        self.assertIn("frontmatter-metadata-spine", docs_readme)
        self.assertIn("evidence-note-provenance-lift", docs_readme)
        self.assertIn("bounded-relation-lift-for-kag", docs_readme)
        self.assertIn("risk-and-negative-effect-lift", docs_readme)
        self.assertIn("TECHNIQUE_SELECTION_GUIDE.md", docs_readme)
        self.assertIn("SEMANTIC_REVIEW_GUIDE.md", docs_readme)
        self.assertIn("review packet route", docs_readme)
        self.assertIn("technique_capsules.json", docs_readme)
        self.assertIn("shadow_review_manifest.json", docs_readme)
        self.assertIn("SHADOW_PATTERNS.md", docs_readme)
        self.assertIn("AGENT_WORKFLOWS_CORE_SEMANTIC_REVIEW.md", semantic_packets)
        self.assertIn("PUBLISHED_SUMMARY_SHADOW_REVIEW.md", shadow_packets)
        self.assertIn("EVALUATION_CHAIN_SHADOW_REVIEW.md", shadow_packets)
        self.assertIn("markdown-technique-section-lift", kag_source_guide)
        self.assertIn("risk-and-negative-effect-lift", kag_source_guide)
        self.assertIn("shadow_review_manifest.json", kag_source_guide)
        self.assertIn("risk-and-negative-effect-lift", shadow_guide)
        self.assertIn("risk-and-negative-effect-lift", risk_guide)
        self.assertIn("frontmatter-metadata-spine", metadata_guide)
        self.assertIn("evidence-note-provenance-lift", provenance_guide)
        self.assertIn("adverse_effects_review", provenance_guide)
        self.assertIn("bounded-relation-lift-for-kag", relation_guide)


if __name__ == "__main__":
    unittest.main()
