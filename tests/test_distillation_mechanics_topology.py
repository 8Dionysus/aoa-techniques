from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

ACTIVE_DISTILLATION_SURFACES = (
    "mechanics/distillation/AGENTS.md",
    "mechanics/distillation/README.md",
    "mechanics/distillation/DIRECTION.md",
    "mechanics/distillation/PARTS.md",
    "mechanics/distillation/PROVENANCE.md",
    "mechanics/distillation/LANDING_LOG.md",
    "mechanics/distillation/ROADMAP.md",
    "mechanics/distillation/parts/AGENTS.md",
    "mechanics/distillation/parts/README.md",
    "mechanics/distillation/legacy/AGENTS.md",
    "mechanics/distillation/legacy/README.md",
    "mechanics/distillation/legacy/INDEX.md",
    "mechanics/distillation/legacy/DISTILLATION_LOG.md",
    "mechanics/distillation/legacy/raw/README.md",
)

RAW_DISTILLATION_RECEIPTS = (
    "mechanics/distillation/legacy/raw/EXTERNAL_CANDIDATE_LEDGER_2026-05-01_PRE_PRUNE.md",
    "mechanics/distillation/legacy/raw/CROSS_LAYER_CANDIDATE_LEDGER_2026-05-01_PRE_PRUNE.md",
)

PART_LOCAL_DISTILLATION_READMES = (
    "mechanics/distillation/parts/donor-refinery/README.md",
    "mechanics/distillation/parts/external-import-runbook/README.md",
    "mechanics/distillation/parts/external-candidate-ledger/README.md",
    "mechanics/distillation/parts/cross-layer-candidate-ledger/README.md",
    "mechanics/distillation/parts/agon-candidate-handoff/README.md",
    "mechanics/distillation/parts/technique-reform-ingress/README.md",
    "mechanics/distillation/parts/long-gap-reentry/README.md",
)

PART_LOCAL_EXTERNAL_CANDIDATE_REGISTRY_ARTIFACTS = (
    "mechanics/distillation/parts/external-candidate-ledger/config/external_candidate_registry.seed.json",
    "mechanics/distillation/parts/external-candidate-ledger/generated/external_candidate_registry.min.json",
    "mechanics/distillation/parts/external-candidate-ledger/schemas/external-candidate-registry-entry.schema.json",
    "mechanics/distillation/parts/external-candidate-ledger/schemas/external-candidate-registry.schema.json",
    "mechanics/distillation/parts/external-candidate-ledger/examples/external_candidate_registry_entry.example.json",
    "mechanics/distillation/parts/external-candidate-ledger/scripts/build_external_candidate_registry.py",
    "mechanics/distillation/parts/external-candidate-ledger/scripts/validate_external_candidate_registry.py",
    "mechanics/distillation/parts/external-candidate-ledger/tests/test_external_candidate_registry.py",
)

PART_LOCAL_CROSS_LAYER_CANDIDATE_REGISTRY_ARTIFACTS = (
    "mechanics/distillation/parts/cross-layer-candidate-ledger/config/cross_layer_candidate_registry.seed.json",
    "mechanics/distillation/parts/cross-layer-candidate-ledger/generated/cross_layer_candidate_registry.min.json",
    "mechanics/distillation/parts/cross-layer-candidate-ledger/schemas/cross-layer-candidate-registry-entry.schema.json",
    "mechanics/distillation/parts/cross-layer-candidate-ledger/schemas/cross-layer-candidate-registry.schema.json",
    "mechanics/distillation/parts/cross-layer-candidate-ledger/examples/cross_layer_candidate_registry_entry.example.json",
    "mechanics/distillation/parts/cross-layer-candidate-ledger/scripts/build_cross_layer_candidate_registry.py",
    "mechanics/distillation/parts/cross-layer-candidate-ledger/scripts/validate_cross_layer_candidate_registry.py",
    "mechanics/distillation/parts/cross-layer-candidate-ledger/tests/test_cross_layer_candidate_registry.py",
)

PART_LOCAL_AGON_CANDIDATE_HANDOFF_ARTIFACTS = (
    "mechanics/distillation/parts/agon-candidate-handoff/config/agon_candidate_handoff.seed.json",
    "mechanics/distillation/parts/agon-candidate-handoff/gates/README.md",
    "mechanics/distillation/parts/agon-candidate-handoff/gates/bundle-reviews/README.md",
    "mechanics/distillation/parts/agon-candidate-handoff/gates/bundle-reviews/request-evidence-bundle-readiness-review.md",
    "mechanics/distillation/parts/agon-candidate-handoff/gates/checklists/README.md",
    "mechanics/distillation/parts/agon-candidate-handoff/gates/checklists/request-evidence-gate-checklist.md",
    "mechanics/distillation/parts/agon-candidate-handoff/gates/evidence-notes/README.md",
    "mechanics/distillation/parts/agon-candidate-handoff/gates/evidence-notes/request-evidence-gate-evidence-note.md",
    "mechanics/distillation/parts/agon-candidate-handoff/gates/examples/README.md",
    "mechanics/distillation/parts/agon-candidate-handoff/gates/examples/request-evidence-minimal-public-safe.md",
    "mechanics/distillation/parts/agon-candidate-handoff/gates/request-evidence-practice.md",
    "mechanics/distillation/parts/agon-candidate-handoff/generated/agon_candidate_handoff.min.json",
    "mechanics/distillation/parts/agon-candidate-handoff/schemas/agon-candidate-handoff-entry.schema.json",
    "mechanics/distillation/parts/agon-candidate-handoff/schemas/agon-candidate-handoff.schema.json",
    "mechanics/distillation/parts/agon-candidate-handoff/examples/agon_candidate_handoff_entry.example.json",
    "mechanics/distillation/parts/agon-candidate-handoff/scripts/build_agon_candidate_handoff.py",
    "mechanics/distillation/parts/agon-candidate-handoff/scripts/validate_agon_candidate_handoff.py",
    "mechanics/distillation/parts/agon-candidate-handoff/tests/test_agon_candidate_handoff.py",
)

PART_LOCAL_TECHNIQUE_REFORM_INGRESS_ARTIFACTS = (
    "mechanics/distillation/parts/technique-reform-ingress/reviews/README.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/first-topology-scout-review-pack.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/first-kind-ambiguity-review-pack.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/second-kind-ambiguity-review-pack.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/0054-kind-destination-check.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/post-0054-kind-audit-hold-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/first-family-shelf-review-pack.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/first-tree-projection-review-pack.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/review-compaction-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-review-compaction-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/handoff-continuation-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-handoff-continuation-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/media-ingest-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-media-ingest-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/diagnosis-repair-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-diagnosis-repair-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/instruction-surface-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-instruction-surface-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/kag-source-lift-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-kag-source-lift-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/docs-boundary-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-docs-boundary-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/capability-registry-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-capability-registry-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/capability-boundary-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-capability-boundary-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/skill-discovery-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-skill-discovery-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/skill-support-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-skill-support-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/evaluation-chain-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-evaluation-chain-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/published-summary-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-published-summary-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/history-artifacts-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/donor-harvest-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-donor-harvest-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/decision-routing-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-decision-routing-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/approval-evidence-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-approval-evidence-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/review-evidence-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-automation-readiness-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/promotion-boundary-direct-read-migration-review.md",
)

OLD_FLAT_DISTILLATION_FILES = (
    "mechanics/distillation/DONOR_REFINERY_RUBRIC.md",
    "mechanics/distillation/EXTERNAL_IMPORT_RUNBOOK.md",
    "mechanics/distillation/EXTERNAL_TECHNIQUE_CANDIDATES.md",
    "mechanics/distillation/CROSS_LAYER_TECHNIQUE_CANDIDATES.md",
    "mechanics/distillation/LONG_GAP_CANON_DESIGN.md",
)


class DistillationMechanicsTopologyTestCase(unittest.TestCase):
    def test_distillation_active_surfaces_are_discoverable(self) -> None:
        for relative_path in (
            ACTIVE_DISTILLATION_SURFACES
            + RAW_DISTILLATION_RECEIPTS
            + PART_LOCAL_EXTERNAL_CANDIDATE_REGISTRY_ARTIFACTS
            + PART_LOCAL_CROSS_LAYER_CANDIDATE_REGISTRY_ARTIFACTS
            + PART_LOCAL_AGON_CANDIDATE_HANDOFF_ARTIFACTS
            + PART_LOCAL_TECHNIQUE_REFORM_INGRESS_ARTIFACTS
        ):
            with self.subTest(relative_path=relative_path):
                self.assertTrue((REPO_ROOT / relative_path).is_file())

    def test_distillation_flat_files_moved_into_owning_parts(self) -> None:
        for relative_path in PART_LOCAL_DISTILLATION_READMES:
            with self.subTest(relative_path=relative_path):
                self.assertTrue((REPO_ROOT / relative_path).is_file())

        for relative_path in OLD_FLAT_DISTILLATION_FILES:
            with self.subTest(relative_path=relative_path):
                self.assertFalse((REPO_ROOT / relative_path).exists())

    def test_distillation_part_map_names_all_current_parts(self) -> None:
        parts = (REPO_ROOT / "mechanics" / "distillation" / "PARTS.md").read_text(
            encoding="utf-8"
        )
        provenance = (
            REPO_ROOT / "mechanics" / "distillation" / "PROVENANCE.md"
        ).read_text(encoding="utf-8")

        for part_name in (
            "donor-refinery",
            "external-import-runbook",
            "external-candidate-ledger",
            "cross-layer-candidate-ledger",
            "agon-candidate-handoff",
            "technique-reform-ingress",
            "long-gap-reentry",
        ):
            with self.subTest(part_name=part_name):
                self.assertIn(part_name, parts)
                self.assertIn(part_name, provenance)

    def test_part_local_ledgers_preserve_current_accounting(self) -> None:
        external = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "external-candidate-ledger"
            / "README.md"
        ).read_text(encoding="utf-8")
        cross_layer = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "cross-layer-candidate-ledger"
            / "README.md"
        ).read_text(encoding="utf-8")

        self.assertIn("remaining `13` external donor-derived candidates", external)
        self.assertIn("full `24` technique-shaped candidate names", cross_layer)
        self.assertIn("`10` landed from this wave map", cross_layer)
        self.assertIn("remaining `18` candidates here", cross_layer)
        self.assertIn("## Landed Wave Anchors", cross_layer)
        self.assertNotIn("## Current Wave Program", cross_layer)

        rows = re.findall(r"^\| `([^`]+)` \|", cross_layer, flags=re.MULTILINE)
        self.assertEqual(24, len(rows))
        self.assertEqual(24, len(set(rows)))

    def test_external_candidate_ledger_marks_missing_seed_sources(self) -> None:
        external = (
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

        self.assertIn("## Source Status", external)
        self.assertIn("historical source\nlabels", external)
        self.assertIn("did not find checked-out", external)
        self.assertIn("seeds/seed_4.txt", external)
        self.assertIn("seeds/seed_6.txt", external)
        self.assertIn("remaining `13` external donor-derived candidates", receipt)
        self.assertNotIn("## Source Status", receipt)

    def test_external_candidate_registry_preserves_current_accounting(self) -> None:
        registry = json.loads(
            (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "external-candidate-ledger"
                / "generated"
                / "external_candidate_registry.min.json"
            ).read_text(encoding="utf-8")
        )

        self.assertEqual(13, registry["total_candidates"])
        self.assertEqual(["phase_sync_for_agents"], registry["active_narrowing_lanes"])
        self.assertEqual(1, registry["ledger_status_counts"]["future_import_here"])
        self.assertEqual(4, registry["ledger_status_counts"]["hold_because_overlap"])
        self.assertEqual(5, registry["gate_status_counts"]["layer_incubation"])
        self.assertIn("does not create bundles", registry["stop_line"])

    def test_cross_layer_candidate_registry_preserves_current_accounting(self) -> None:
        registry = json.loads(
            (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "cross-layer-candidate-ledger"
                / "generated"
                / "cross_layer_candidate_registry.min.json"
            ).read_text(encoding="utf-8")
        )

        self.assertEqual(24, registry["total_candidates"])
        self.assertEqual([], registry["future_import_lanes"])
        self.assertEqual(6, registry["summary_counts"]["already_staged_elsewhere"])
        self.assertEqual(10, registry["summary_counts"]["landed_from_wave_map"])
        self.assertEqual(2, registry["ledger_status_counts"]["hold_because_overlap"])
        self.assertEqual(
            3, registry["ledger_status_counts"]["needs_layer_incubation_before_distillation_here"]
        )
        self.assertEqual(3, registry["gate_status_counts"]["not_technique_shaped"])
        self.assertEqual({"A": 5, "B": 3, "C": 2}, registry["wave_counts"])
        self.assertIn("recurrence promotion authority", registry["stop_line"])

    def test_agon_candidate_handoff_registry_preserves_source_coverage(self) -> None:
        registry = json.loads(
            (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "agon-candidate-handoff"
                / "generated"
                / "agon_candidate_handoff.min.json"
            ).read_text(encoding="utf-8")
        )

        self.assertEqual(22, registry["total_candidates"])
        self.assertEqual(
            {
                "epistemic-technique-candidates": 10,
                "move-technique-bridge": 12,
            },
            registry["source_counts"],
        )
        self.assertEqual(
            {
                "first_narrowing_watch": 11,
                "owner_route_hold": 1,
                "source_boundary_hold": 10,
            },
            registry["distillation_lane_counts"],
        )
        self.assertIn(
            "candidate:aoa-techniques:agon/request-evidence-practice",
            registry["first_narrowing_watch"],
        )
        self.assertEqual(
            {
                "bundle_readiness_reviews": 3,
                "gate_cards": 3,
                "gate_checklists": 3,
                "gate_evidence_notes": 3,
                "gate_examples": 3,
                "technique_bundles": 3,
            },
            registry["gate_pipeline_counts"],
        )
        self.assertEqual(8, registry["first_narrowing_frontier_counts"]["total"])
        self.assertEqual(
            [
                "probe_trace",
                "localize_contradiction",
                "deny_closure",
                "inference_chain_attack_practice",
                "explanatory_power_comparison_practice",
                "concept_boundary_probe_practice",
                "counterfactual_pressure_practice",
                "false_consensus_breaking_practice",
            ],
            [row["source_label"] for row in registry["first_narrowing_frontier"]],
        )
        self.assertEqual(
            {
                "Tree-of-Sophia": 1,
                "aoa-agents": 1,
                "aoa-evals": 4,
                "aoa-memo": 1,
                "aoa-routing": 1,
            },
            registry["first_narrowing_frontier_counts"]["by_nearest_wrong_owner"],
        )
        self.assertEqual(
            {
                "candidate:aoa-techniques:agon/challenge-claim-practice": "mechanics/distillation/parts/agon-candidate-handoff/gates/challenge-claim-practice.md",
                "candidate:aoa-techniques:agon/request-evidence-practice": "mechanics/distillation/parts/agon-candidate-handoff/gates/request-evidence-practice.md",
                "candidate:aoa-techniques:agon/offer-evidence-reference-practice": "mechanics/distillation/parts/agon-candidate-handoff/gates/offer-evidence-reference-practice.md",
            },
            registry["gate_cards"],
        )
        self.assertEqual(
            {
                "candidate:aoa-techniques:agon/challenge-claim-practice": "mechanics/distillation/parts/agon-candidate-handoff/gates/examples/challenge-claim-minimal-public-safe.md",
                "candidate:aoa-techniques:agon/request-evidence-practice": "mechanics/distillation/parts/agon-candidate-handoff/gates/examples/request-evidence-minimal-public-safe.md",
                "candidate:aoa-techniques:agon/offer-evidence-reference-practice": "mechanics/distillation/parts/agon-candidate-handoff/gates/examples/offer-evidence-reference-minimal-public-safe.md",
            },
            registry["gate_examples"],
        )
        self.assertEqual(
            {
                "candidate:aoa-techniques:agon/challenge-claim-practice": "mechanics/distillation/parts/agon-candidate-handoff/gates/checklists/challenge-claim-gate-checklist.md",
                "candidate:aoa-techniques:agon/request-evidence-practice": "mechanics/distillation/parts/agon-candidate-handoff/gates/checklists/request-evidence-gate-checklist.md",
                "candidate:aoa-techniques:agon/offer-evidence-reference-practice": "mechanics/distillation/parts/agon-candidate-handoff/gates/checklists/offer-evidence-reference-gate-checklist.md",
            },
            registry["gate_checklists"],
        )
        self.assertEqual(
            {
                "candidate:aoa-techniques:agon/challenge-claim-practice": "mechanics/distillation/parts/agon-candidate-handoff/gates/evidence-notes/challenge-claim-gate-evidence-note.md",
                "candidate:aoa-techniques:agon/request-evidence-practice": "mechanics/distillation/parts/agon-candidate-handoff/gates/evidence-notes/request-evidence-gate-evidence-note.md",
                "candidate:aoa-techniques:agon/offer-evidence-reference-practice": "mechanics/distillation/parts/agon-candidate-handoff/gates/evidence-notes/offer-evidence-reference-gate-evidence-note.md",
            },
            registry["gate_evidence_notes"],
        )
        self.assertEqual(
            {
                "candidate:aoa-techniques:agon/challenge-claim-practice": "mechanics/distillation/parts/agon-candidate-handoff/gates/bundle-reviews/challenge-claim-bundle-readiness-review.md",
                "candidate:aoa-techniques:agon/request-evidence-practice": "mechanics/distillation/parts/agon-candidate-handoff/gates/bundle-reviews/request-evidence-bundle-readiness-review.md",
                "candidate:aoa-techniques:agon/offer-evidence-reference-practice": "mechanics/distillation/parts/agon-candidate-handoff/gates/bundle-reviews/offer-evidence-reference-bundle-readiness-review.md",
            },
            registry["bundle_readiness_reviews"],
        )
        self.assertEqual(
            {
                "candidate:aoa-techniques:agon/challenge-claim-practice": "techniques/proof/review-evidence/single-locus-claim-challenge/TECHNIQUE.md",
                "candidate:aoa-techniques:agon/request-evidence-practice": "techniques/proof/review-evidence/single-missing-evidence-request/TECHNIQUE.md",
                "candidate:aoa-techniques:agon/offer-evidence-reference-practice": "techniques/proof/review-evidence/single-scoped-evidence-reference/TECHNIQUE.md",
            },
            registry["technique_bundles"],
        )
        self.assertIn(
            "agon.tech.epistemic.doctrine_revision_review_practice",
            registry["owner_route_holds"],
        )
        self.assertIn("does not define Agon law", registry["stop_line"])

    def test_agon_candidate_gate_cards_are_bounded_and_link_clean(self) -> None:
        gate_root = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "agon-candidate-handoff"
            / "gates"
        )

        for gate_path in sorted(gate_root.rglob("*.md")):
            text = gate_path.read_text(encoding="utf-8")
            with self.subTest(gate_path=gate_path.relative_to(gate_root)):
                for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
                    if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                        continue
                    target_path = target.split("#", 1)[0]
                    if not target_path:
                        continue
                    resolved = (gate_path.parent / target_path).resolve()
                    self.assertTrue(
                        resolved.is_relative_to(REPO_ROOT.resolve()),
                        f"{gate_path.name} link leaves repo: {target}",
                    )
                    self.assertTrue(
                        resolved.exists(),
                        f"{gate_path.name} has broken link: {target}",
                    )

                if gate_path.name == "README.md":
                    continue
                self.assertIn("not a technique bundle", text)
                self.assertIn("Do not define Agon", text)
                self.assertIn("Do not issue proof", text)
                self.assertNotIn("gate-card-landed, promoted", text)

                if "examples" in gate_path.parts:
                    self.assertIn("Public Safety", text)
                    if gate_path.name == "request-evidence-minimal-public-safe.md":
                        self.assertIn("one missing evidence object", text)
                        self.assertIn("Return condition", text)
                    if gate_path.name == "offer-evidence-reference-minimal-public-safe.md":
                        self.assertIn("one evidence reference", text)
                        self.assertIn("Review condition", text)
                    if gate_path.name == "challenge-claim-minimal-public-safe.md":
                        self.assertIn("one challenged claim", text)
                        self.assertIn("Vulnerable locus", text)
                    self.assertIn("no private logs", text)
                if "checklists" in gate_path.parts:
                    self.assertIn("Pass Conditions", text)
                    self.assertIn("Fail Conditions", text)
                    if gate_path.name == "request-evidence-gate-checklist.md":
                        self.assertIn("exactly one missing evidence object", text)
                    if gate_path.name == "offer-evidence-reference-gate-checklist.md":
                        self.assertIn("exactly one evidence reference", text)
                    if gate_path.name == "challenge-claim-gate-checklist.md":
                        self.assertIn("exactly one target claim", text)
                if "evidence-notes" in gate_path.parts:
                    self.assertIn("Evidence Read", text)
                    self.assertIn("What This Does Not Support", text)
                    self.assertIn("ready for bundle-readiness review", text)
                if "bundle-reviews" in gate_path.parts:
                    self.assertIn("Verdict", text)
                    self.assertIn("ready for one-bundle draft", text)
                    if gate_path.name == "request-evidence-bundle-readiness-review.md":
                        self.assertIn("draft kind: `guardrail`", text)
                    if gate_path.name == "offer-evidence-reference-bundle-readiness-review.md":
                        self.assertIn("draft kind: `artifact`", text)
                        self.assertIn("Reform Thread", text)
                    self.assertIn("What This Does Not Support", text)

    def test_agon_first_narrowing_frontier_review_matches_remaining_candidates(self) -> None:
        frontier = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "agon-candidate-handoff"
            / "gates"
            / "frontier"
            / "first-narrowing-frontier-review.md"
        ).read_text(encoding="utf-8")

        self.assertIn("Remaining ungated first-narrowing candidates: `8`", frontier)
        for source_label in (
            "probe_trace",
            "localize_contradiction",
            "deny_closure",
            "inference_chain_attack_practice",
            "explanatory_power_comparison_practice",
            "concept_boundary_probe_practice",
            "counterfactual_pressure_practice",
            "false_consensus_breaking_practice",
        ):
            self.assertIn(f"`{source_label}`", frontier)
        self.assertNotIn("| `challenge_claim` |", frontier)
        self.assertNotIn("| `request_evidence` |", frontier)
        self.assertNotIn("| `offer_evidence_reference` |", frontier)
        self.assertIn("not a technique bundle", frontier)
        self.assertIn("Do not define Agon", frontier)
        self.assertIn("Do not issue proof", frontier)

    def test_technique_reform_ingress_is_bounded_before_schema_change(self) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        decision = (
            REPO_ROOT
            / "docs"
            / "decisions"
            / "2026-05-03-technique-reform-ingress-packet.md"
        ).read_text(encoding="utf-8")

        self.assertIn("not a schema migration", ingress)
        self.assertIn("public corpus: `107` bundles, `25` canonical, `82` promoted", ingress)
        self.assertIn("authoritative frontmatter axes: `domain`, `kind`", ingress)
        self.assertIn("first_narrowing_frontier", ingress)
        for axis in (
            "family",
            "capability_class",
            "substrate",
            "execution_profile",
            "risk_posture",
        ):
            self.assertIn(axis, ingress)
        self.assertIn("Do not add new required frontmatter fields", ingress)
        self.assertIn("Do not add new `kind` values from handoff cues", ingress)
        self.assertIn("prevents generated evidence", decision)
        self.assertIn("remapping bundle meaning", decision)

    def test_technique_reform_review_pack_preserves_scout_boundary(self) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "first-topology-scout-review-pack.md"
        ).read_text(encoding="utf-8")

        self.assertIn("topology scout review pack", ingress)
        self.assertIn("not a schema migration", review)
        self.assertIn("Technique Topology Scout", review)
        self.assertIn("`107` techniques", review)
        self.assertIn("`orchestration-required` has `52`", review)
        self.assertIn("`small-agent` has `36`", review)
        self.assertIn("`medium-agent` has `19`", review)
        self.assertIn("`read-only` appears on `65`", review)
        self.assertIn("`mutating` on `25`", review)
        self.assertIn("does not remap any bundle", review)
        self.assertIn("direct bundle reading", review)
        self.assertIn("kind ambiguity review pack", review)

    def test_kind_ambiguity_review_pack_uses_direct_bundle_reading(self) -> None:
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "first-kind-ambiguity-review-pack.md"
        ).read_text(encoding="utf-8")

        self.assertIn("first shortlist remap wave closed", review)
        self.assertIn("did not change bundle frontmatter by itself", review)
        self.assertIn("direct-read", review)
        self.assertIn("`AOA-T-0005`", review)
        self.assertIn("second shortlist remap landed", review)
        self.assertIn("`AOA-T-0085`", review)
        self.assertIn("first shortlist remap landed", review)
        self.assertIn("`AOA-T-0052`", review)
        self.assertIn("final shortlist remap landed", review)
        self.assertIn("Keep `guardrail`", review)
        self.assertIn("Keep `lift`", review)
        self.assertIn("Keep `assessment`", review)
        self.assertIn("Do not change frontmatter from this review alone", review)
        self.assertIn("fresh kind ambiguity read", review)

    def test_second_kind_ambiguity_review_pack_routes_0054_without_remap(self) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "second-kind-ambiguity-review-pack.md"
        ).read_text(encoding="utf-8")

        self.assertIn("Second Kind Ambiguity Review Pack", review)
        self.assertIn("updated `reports/kind_ambiguity_audit.md`", review)
        self.assertIn("does not change frontmatter", review)
        self.assertIn("`AOA-T-0054`", review)
        self.assertIn("compaction-resilient-skill-loading", review)
        self.assertIn("`handoff`", review)
        self.assertIn("`workflow`", review)
        self.assertIn("`recovery`", review)
        self.assertIn("destination check", review)
        self.assertIn("first shortlist remap wave is closed", review)
        self.assertIn("Keep `guardrail`", review)
        self.assertIn("Keep `lift`", review)
        self.assertIn("Keep `assessment`", review)
        self.assertIn("Second Kind Ambiguity Review Pack", ingress)
        self.assertIn("`AOA-T-0054`", ingress)
        self.assertIn("0054-kind-destination-check", review)

    def test_0085_kind_remap_landed_without_status_change(self) -> None:
        catalog = json.loads(
            (REPO_ROOT / "generated" / "technique_catalog.json").read_text(
                encoding="utf-8"
            )
        )
        technique = next(
            entry for entry in catalog["techniques"] if entry["id"] == "AOA-T-0085"
        )
        decision = (
            REPO_ROOT
            / "docs"
            / "decisions"
            / "2026-05-04-0085-kind-remap.md"
        ).read_text(encoding="utf-8")

        self.assertEqual("agent-workflows", technique["domain"])
        self.assertEqual("lift", technique["kind"])
        self.assertEqual("promoted", technique["status"])
        self.assertIn("Remap `AOA-T-0085` from `artifact` to `lift`", decision)
        self.assertIn("classification correction only", decision)

    def test_0005_kind_remap_landed_without_status_change(self) -> None:
        catalog = json.loads(
            (REPO_ROOT / "generated" / "technique_catalog.json").read_text(
                encoding="utf-8"
            )
        )
        technique = next(
            entry for entry in catalog["techniques"] if entry["id"] == "AOA-T-0005"
        )
        decision = (
            REPO_ROOT
            / "docs"
            / "decisions"
            / "2026-05-04-0005-kind-remap.md"
        ).read_text(encoding="utf-8")

        self.assertEqual("agent-workflows", technique["domain"])
        self.assertEqual("workflow", technique["kind"])
        self.assertEqual("promoted", technique["status"])
        self.assertIn("Remap `AOA-T-0005` from `guardrail` to `workflow`", decision)
        self.assertIn("classification correction only", decision)

    def test_0052_kind_remap_landed_without_status_change(self) -> None:
        catalog = json.loads(
            (REPO_ROOT / "generated" / "technique_catalog.json").read_text(
                encoding="utf-8"
            )
        )
        technique = next(
            entry for entry in catalog["techniques"] if entry["id"] == "AOA-T-0052"
        )
        decision = (
            REPO_ROOT
            / "docs"
            / "decisions"
            / "2026-05-04-0052-kind-remap.md"
        ).read_text(encoding="utf-8")

        self.assertEqual("agent-workflows", technique["domain"])
        self.assertEqual("workflow", technique["kind"])
        self.assertEqual("promoted", technique["status"])
        self.assertIn("Remap `AOA-T-0052` from `handoff` to `workflow`", decision)
        self.assertIn("classification correction only", decision)
        self.assertIn("`validation`", decision)
        self.assertIn("`lift`", decision)

    def test_0054_kind_remap_landed_without_status_change(self) -> None:
        catalog = json.loads(
            (REPO_ROOT / "generated" / "technique_catalog.json").read_text(
                encoding="utf-8"
            )
        )
        technique = next(
            entry for entry in catalog["techniques"] if entry["id"] == "AOA-T-0054"
        )
        decision = (
            REPO_ROOT
            / "docs"
            / "decisions"
            / "2026-05-04-0054-kind-remap.md"
        ).read_text(encoding="utf-8")
        destination_check = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "0054-kind-destination-check.md"
        ).read_text(encoding="utf-8")

        self.assertEqual("agent-workflows", technique["domain"])
        self.assertEqual("recovery", technique["kind"])
        self.assertEqual("promoted", technique["status"])
        self.assertIn("Remap `AOA-T-0054` from `handoff` to `recovery`", decision)
        self.assertIn("classification correction only", decision)
        self.assertIn("`workflow`", decision)
        self.assertIn("Remap `AOA-T-0054` from `handoff` to `recovery`", destination_check)
        self.assertIn("`AOA-T-0057`", destination_check)

    def test_post_0054_kind_audit_hold_review_closes_remap_lane(self) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "post-0054-kind-audit-hold-review.md"
        ).read_text(encoding="utf-8")
        roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")

        self.assertIn("Post-0054 Kind Audit Hold Review", review)
        self.assertIn("No new `kind` frontmatter candidate", review)
        self.assertIn("remap lane closed", review)
        self.assertIn("family shelf review", review)
        self.assertIn("Do not reopen a candidate merely because", review)
        self.assertIn("`workflow` vs `guardrail`", review)
        self.assertIn("`validation` vs `assessment`", review)
        self.assertIn("`artifact` vs `lift`", review)
        self.assertIn("`handoff` vs `workflow`", review)
        self.assertIn("post-0054-kind-audit-hold-review", reviews_index)
        self.assertIn("Post-0054 Kind Audit Hold Review", ingress)
        self.assertIn("family shelf review", roadmap)

    def test_family_shelf_review_pack_prepares_tree_projection_without_migration(self) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "first-family-shelf-review-pack.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")

        self.assertIn("First Family Shelf Review Pack", review)
        self.assertIn("review-pack-landed", review)
        self.assertIn("not frontmatter truth", review)
        self.assertIn("not path migration", review)
        self.assertIn("`26` scout families", review)
        self.assertIn("Stable Shelf Candidates", review)
        self.assertIn("Boundary Watch", review)
        self.assertIn("Split Pressure", review)
        self.assertIn("singleton-hold", review)
        self.assertIn("`automation-governance`", review)
        self.assertIn("split-review-needed", review)
        self.assertIn("non-authoritative tree projection", review)
        self.assertIn("Do not add `family` frontmatter", review)
        self.assertIn("Do not move bundle directories", review)
        self.assertIn("proposed `trunk`", review)
        self.assertIn("proposed `shelf`", review)
        for trunk in (
            "`execution`",
            "`instruction`",
            "`proof`",
            "`continuity`",
            "`governance`",
            "`knowledge-lift`",
            "`ingest`",
            "`recovery`",
            "`history`",
            "`tool-use`",
        ):
            with self.subTest(trunk=trunk):
                self.assertIn(trunk, review)

        self.assertIn("first-family-shelf-review-pack", reviews_index)
        self.assertIn("family shelf review: landed", ingress)
        self.assertIn("non-authoritative tree projection", ingress)
        self.assertIn("First Family Shelf Review Pack", ingress)
        self.assertIn("first family shelf review pack", distillation_roadmap)
        self.assertIn("technique_tree_projection.md", root_roadmap)
        self.assertIn("family shelf review", tree_contract)

    def test_tree_projection_review_pack_selects_direct_read_pilot_without_migration(self) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "first-tree-projection-review-pack.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")

        self.assertIn("First Tree Projection Review Pack", review)
        self.assertIn("review-pack-landed", review)
        self.assertIn("not path migration", review)
        self.assertIn("not `tree_path` frontmatter", review)
        self.assertIn("all `107` current bundles", review)
        self.assertIn("`34` `pilot-candidate`", review)
        self.assertIn("`41` `candidate`", review)
        self.assertIn("`22` `boundary-watch`", review)
        self.assertIn("| `split-review-needed` | `9` |", review)
        self.assertIn("| `singleton-hold` | `1` |", review)
        self.assertIn("Choose `review-compaction`", review)
        self.assertIn("`AOA-T-0051`", review)
        self.assertIn("`AOA-T-0052`", review)
        self.assertIn("`AOA-T-0054`", review)
        self.assertIn("Backup Pilot", review)
        self.assertIn("Do not move `review-compaction` from this review alone", review)
        self.assertIn("direct-read migration review", review)

        self.assertIn("first-tree-projection-review-pack", reviews_index)
        self.assertIn("tree projection: landed", ingress)
        self.assertIn("first tree projection review: landed", ingress)
        self.assertIn("review-compaction", ingress)
        self.assertIn("direct-read migration review", distillation_roadmap)
        self.assertIn("review-compaction", root_roadmap)
        self.assertIn("reports/technique_tree_projection.md", tree_contract)

    def test_review_compaction_pilot_migration_is_landed_after_direct_read(self) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "review-compaction-direct-read-migration-review.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")

        self.assertIn("Review-Compaction Direct-Read Migration Review", review)
        self.assertIn("accepted-for-first-migration-pilot", review)
        self.assertIn("not path migration", review)
        self.assertIn("not `tree_path` frontmatter", review)
        self.assertIn("AOA-T-0051", review)
        self.assertIn("AOA-T-0052", review)
        self.assertIn("AOA-T-0054", review)
        self.assertIn("commit-triggered-background-review", review)
        self.assertIn("review-findings-compaction", review)
        self.assertIn("compaction-resilient-skill-loading", review)
        self.assertIn("techniques/continuity/review-compaction/", review)
        self.assertIn("The move is clearer than current placement", review)
        self.assertIn("Move exactly these three bundles", review)
        self.assertIn("Do not move files from this review pack alone", review)
        self.assertIn("Do not add `family` or `tree_path` frontmatter", review)
        self.assertIn("Create a minimal `techniques/continuity/AGENTS.md`", review)
        self.assertIn("Run `python scripts/release_check.py`", review)

        self.assertIn("review-compaction-direct-read-migration-review", reviews_index)
        self.assertIn("review-compaction direct-read review: landed", ingress)
        self.assertIn("accepted-for-first-migration-pilot", ingress)
        self.assertIn("The first pilot migration has moved exactly", ingress)
        self.assertIn("techniques/continuity/review-compaction/", ingress)
        self.assertIn("review-compaction direct-read migration review is landed", distillation_roadmap)
        self.assertIn("first pilot migration", distillation_roadmap)
        self.assertIn("first landed pilot moved `AOA-T-0051`", root_roadmap)
        self.assertIn("current landed pilot review", tree_contract)

    def test_landed_review_compaction_pilot_review_selects_next_direct_read_shelf(self) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "landed-review-compaction-pilot-review.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")

        self.assertIn("Landed Review-Compaction Pilot Review", review)
        self.assertIn("pilot-validated", review)
        self.assertIn("not path migration", review)
        self.assertIn("not `tree_path` frontmatter", review)
        self.assertIn("The pilot improved browsability", review)
        self.assertIn("Root `legacy/receipts/`", review)
        self.assertIn("Choose `handoff-continuation`", review)
        self.assertIn("AOA-T-0056", review)
        self.assertIn("AOA-T-0062", review)
        self.assertIn("Do not move `handoff-continuation` from this review alone", review)
        self.assertIn("Run a direct-read migration review for `handoff-continuation`", review)

        self.assertIn("landed-review-compaction-pilot-review", reviews_index)
        self.assertIn("landed review-compaction pilot review: landed", ingress)
        self.assertIn("pilot-validated", ingress)
        self.assertIn("handoff-continuation", ingress)
        self.assertIn("direct-read migration review", distillation_roadmap)
        self.assertIn("Landed review-compaction pilot review", landing_log)
        self.assertIn("handoff-continuation", root_roadmap)
        self.assertIn("Landed Review-Compaction Pilot Review", tree_contract)

    def test_handoff_continuation_direct_read_review_accepts_second_pilot_without_migration(self) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "handoff-continuation-direct-read-migration-review.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Handoff-Continuation Direct-Read Migration Review", review)
        self.assertIn("accepted-for-second-migration-pilot", review)
        self.assertIn("not path migration", review)
        self.assertIn("not `tree_path` frontmatter", review)
        for technique_id in (
            "AOA-T-0056",
            "AOA-T-0057",
            "AOA-T-0058",
            "AOA-T-0059",
            "AOA-T-0060",
            "AOA-T-0061",
            "AOA-T-0062",
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)
        for slug in (
            "channelized-agent-mailbox",
            "structured-handoff-before-compaction",
            "receipt-confirmed-handoff-packet",
            "git-verified-handoff-claims",
            "session-opening-ritual-before-work",
            "cross-repo-resource-map-bootstrap",
            "episode-bounded-agent-loop",
        ):
            with self.subTest(slug=slug):
                self.assertIn(slug, review)

        self.assertIn("The move is clearer than current placement", review)
        self.assertIn("Move exactly these seven bundles", review)
        self.assertIn("techniques/continuity/handoff-continuation/", review)
        self.assertIn("Do not move files from this review pack alone", review)
        self.assertIn("Do not add `family` or `tree_path` frontmatter", review)
        self.assertIn("Run the second pilot migration", review)
        self.assertIn("run `python scripts/release_check.py`", review)

        self.assertIn("handoff-continuation-direct-read-migration-review", reviews_index)
        self.assertIn("handoff-continuation direct-read review: landed", ingress)
        self.assertIn("accepted-for-second-migration-pilot", ingress)
        self.assertIn("handoff-continuation migration: landed", ingress)
        self.assertIn("handoff-continuation` direct-read migration review is now landed", distillation_roadmap)
        self.assertIn("Handoff-continuation direct-read migration review", landing_log)
        self.assertIn("second landed pilot moved `AOA-T-0056` through `AOA-T-0062`", root_roadmap)
        self.assertIn("Handoff-Continuation Direct-Read Migration Review", tree_contract)
        self.assertIn("accepted the `handoff-continuation` direct-read migration review", changelog)

    def test_handoff_continuation_tree_pilot_migration_is_landed_after_direct_read(self) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("handoff-continuation migration: landed", ingress)
        self.assertIn("techniques/continuity/handoff-continuation/", ingress)
        self.assertIn("without frontmatter changes", ingress)
        self.assertIn("media-ingest direct-read review: landed", ingress)
        self.assertIn("accepted-for-third-migration-pilot", ingress)
        self.assertIn("second pilot migration is", distillation_roadmap)
        self.assertIn("Handoff-continuation tree pilot migration", landing_log)
        self.assertIn("legacy/receipts/2026-05-04-handoff-continuation-tree-pilot.md", landing_log)
        self.assertIn("second landed pilot moved `AOA-T-0056` through `AOA-T-0062`", root_roadmap)
        self.assertIn("Handoff-Continuation Direct-Read Migration Review", tree_contract)
        self.assertIn("2026-05-04-handoff-continuation-tree-pilot.md", tree_contract)
        self.assertIn("moved `AOA-T-0056` through `AOA-T-0062`", changelog)

    def test_landed_handoff_continuation_pilot_review_selects_media_ingest(self) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "landed-handoff-continuation-pilot-review.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        incoming_wave2 = (
            REPO_ROOT
            / "incoming"
            / "chat-wave-2-graph-review-mailbox"
            / "docs"
            / "EXTERNAL_TECHNIQUE_CANDIDATES_CHAT_WAVE_2.md"
        ).read_text(encoding="utf-8")
        incoming_wave3 = (
            REPO_ROOT
            / "incoming"
            / "chat-wave-3-handoff-bounded-continuation"
            / "docs"
            / "EXTERNAL_TECHNIQUE_CANDIDATES_CHAT_WAVE_3.md"
        ).read_text(encoding="utf-8")

        self.assertIn("Landed Handoff-Continuation Pilot Review", review)
        self.assertIn("pilot-validated", review)
        self.assertIn("not path migration", review)
        self.assertIn("not `tree_path` frontmatter", review)
        self.assertIn("Accept the landed `handoff-continuation` pilot", review)
        self.assertIn("staging links", review)
        self.assertIn("Choose `media-ingest`", review)
        for technique_id in (
            "AOA-T-0070",
            "AOA-T-0071",
            "AOA-T-0072",
            "AOA-T-0073",
            "AOA-T-0074",
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)

        self.assertIn("Do not move `media-ingest` from this review alone", review)
        self.assertIn("Run a direct-read migration review for `media-ingest`", review)
        self.assertIn("landed-handoff-continuation-pilot-review", reviews_index)
        self.assertIn("landed handoff-continuation pilot review: landed", ingress)
        self.assertIn("media-ingest", ingress)
        self.assertIn("`media-ingest` direct-read review is now", distillation_roadmap)
        self.assertIn("Landed handoff-continuation pilot review", landing_log)
        self.assertIn("selected\n  `media-ingest`", changelog)
        self.assertIn(
            "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
            root_roadmap,
        )
        self.assertIn("Landed Handoff-Continuation Pilot Review", tree_contract)
        self.assertIn("techniques/continuity/handoff-continuation/channelized-agent-mailbox/TECHNIQUE.md", incoming_wave2)
        self.assertIn("techniques/continuity/handoff-continuation/episode-bounded-agent-loop/TECHNIQUE.md", incoming_wave3)
        self.assertNotIn(
            "techniques/agent-workflows/channelized-agent-mailbox/TECHNIQUE.md",
            incoming_wave2,
        )
        self.assertNotIn(
            "techniques/agent-workflows/episode-bounded-agent-loop/TECHNIQUE.md",
            incoming_wave3,
        )

    def test_media_ingest_direct_read_review_accepts_third_pilot(self) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "media-ingest-direct-read-migration-review.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Media-Ingest Direct-Read Migration Review", review)
        self.assertIn("accepted-for-third-migration-pilot", review)
        self.assertIn("not path migration", review)
        self.assertIn("not\n`tree_path` frontmatter", review)
        self.assertIn("Accept `media-ingest` as the third migration pilot", review)
        for technique_id in (
            "AOA-T-0070",
            "AOA-T-0071",
            "AOA-T-0072",
            "AOA-T-0073",
            "AOA-T-0074",
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)

        self.assertIn("Telegram Edge", review)
        self.assertIn("telegram-account-auth-and-session-bridge", review)
        self.assertIn("Move exactly these five bundles", review)
        self.assertIn("techniques/ingest/media-ingest/", review)
        self.assertIn("Do not move files from this review pack alone", review)
        self.assertIn("Do not add `family` or `tree_path` frontmatter", review)
        self.assertIn("Run the third pilot migration", review)

        self.assertIn("media-ingest-direct-read-migration-review", reviews_index)
        self.assertIn("media-ingest direct-read review: landed", ingress)
        self.assertIn("accepted-for-third-migration-pilot", ingress)
        self.assertIn("media-ingest migration: landed", ingress)
        self.assertIn("third pilot migration", ingress)
        self.assertIn("media-ingest` direct-read review is now", distillation_roadmap)
        self.assertIn("third pilot\n   migration is landed", distillation_roadmap)
        self.assertIn("Media-ingest direct-read migration review", landing_log)
        self.assertIn("Media-ingest tree pilot migration", landing_log)
        self.assertIn("accepted the `media-ingest` direct-read migration review", changelog)
        self.assertIn("moved `AOA-T-0070` through `AOA-T-0074`", changelog)
        self.assertIn("first non-continuity migrated shelf", root_roadmap)
        self.assertIn("third landed pilot, the first non-continuity", root_roadmap)
        self.assertIn("Media-Ingest Direct-Read Migration Review", tree_contract)
        self.assertIn("2026-05-04-media-ingest-tree-pilot.md", tree_contract)
        self.assertTrue(
            (
                REPO_ROOT
                / "techniques"
                / "ingest"
                / "media-ingest"
                / "two-stage-document-ocr-pipeline"
                / "TECHNIQUE.md"
            ).is_file()
        )

    def test_landed_media_ingest_pilot_review_selects_diagnosis_repair(self) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "landed-media-ingest-pilot-review.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Landed Media-Ingest Pilot Review", review)
        self.assertIn("pilot-validated", review)
        self.assertIn("not path migration", review)
        self.assertIn("not `tree_path` frontmatter", review)
        self.assertIn("Accept the landed `media-ingest` pilot", review)
        self.assertIn("first non-continuity trunk test", review)
        self.assertIn("Telegram edge remained bounded", review)
        self.assertIn("Choose `diagnosis-repair`", review)
        for technique_id in (
            "AOA-T-0080",
            "AOA-T-0081",
            "AOA-T-0082",
            "AOA-T-0083",
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)

        self.assertIn("Do not move `diagnosis-repair` from this review alone", review)
        self.assertIn("Run a direct-read migration review for `diagnosis-repair`", review)
        self.assertIn("landed-media-ingest-pilot-review", reviews_index)
        self.assertIn("landed media-ingest pilot review: landed", ingress)
        self.assertIn("diagnosis-repair", ingress)
        self.assertIn("diagnosis-repair` is now", distillation_roadmap)
        self.assertIn("Landed media-ingest pilot review", landing_log)
        self.assertIn("selected\n  `diagnosis-repair`", changelog)
        self.assertIn(
            "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
            root_roadmap,
        )
        self.assertIn("Landed Media-Ingest Pilot Review", tree_contract)
        self.assertIn("techniques/recovery/diagnosis-repair/", tree_contract)

    def test_diagnosis_repair_direct_read_review_accepts_fourth_pilot(self) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "diagnosis-repair-direct-read-migration-review.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Diagnosis-Repair Direct-Read Migration Review", review)
        self.assertIn("accepted-for-fourth-migration-pilot", review)
        self.assertIn("not path migration", review)
        self.assertIn("not\n`tree_path` frontmatter", review)
        self.assertIn("Accept `diagnosis-repair` as the fourth migration pilot", review)
        for technique_id in (
            "AOA-T-0080",
            "AOA-T-0081",
            "AOA-T-0082",
            "AOA-T-0083",
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)

        self.assertIn("Mixed Kind Stress", review)
        self.assertIn("Move exactly these four bundles", review)
        self.assertIn("techniques/recovery/diagnosis-repair/", review)
        self.assertIn("Do not move files from this review pack alone", review)
        self.assertIn("Do not add `family` or `tree_path` frontmatter", review)
        self.assertIn("Run the fourth pilot migration", review)

        self.assertIn("diagnosis-repair-direct-read-migration-review", reviews_index)
        self.assertIn("diagnosis-repair direct-read review: landed", ingress)
        self.assertIn("accepted-for-fourth-migration-pilot", ingress)
        self.assertIn("diagnosis-repair migration: landed", ingress)
        self.assertIn("fourth pilot migration", ingress)
        self.assertIn("accepted-for-fourth-migration-pilot", distillation_roadmap)
        self.assertIn("fourth pilot migration is", distillation_roadmap)
        self.assertIn("techniques/recovery/diagnosis-repair/", distillation_roadmap)
        self.assertIn("Diagnosis-repair direct-read migration review", landing_log)
        self.assertIn("Diagnosis-repair tree pilot migration", landing_log)
        self.assertIn("accepted the `diagnosis-repair` direct-read migration review", changelog)
        self.assertIn("moved `AOA-T-0080` through `AOA-T-0083`", changelog)
        self.assertIn("fourth landed pilot", root_roadmap)
        self.assertIn(
            "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
            root_roadmap,
        )
        self.assertIn("Diagnosis-Repair Direct-Read Migration Review", tree_contract)
        self.assertIn("AOA-T-0080` through `AOA-T-0083", tree_contract)
        self.assertIn("2026-05-04-diagnosis-repair-tree-pilot.md", tree_contract)
        self.assertTrue(
            (
                REPO_ROOT
                / "techniques"
                / "recovery"
                / "diagnosis-repair"
                / "session-drift-taxonomy"
                / "TECHNIQUE.md"
            ).is_file()
        )

    def test_landed_diagnosis_repair_pilot_review_selects_instruction_surface(self) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "landed-diagnosis-repair-pilot-review.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Landed Diagnosis-Repair Pilot Review", review)
        self.assertIn("pilot-validated", review)
        self.assertIn("not path migration", review)
        self.assertIn("not `tree_path` frontmatter", review)
        self.assertIn("Accept the landed `diagnosis-repair` pilot", review)
        self.assertIn("first recovery trunk test", review)
        self.assertIn("Choose `instruction-surface`", review)
        for technique_id in (
            "AOA-T-0012",
            "AOA-T-0013",
            "AOA-T-0024",
            "AOA-T-0027",
            "AOA-T-0029",
            "AOA-T-0030",
            "AOA-T-0035",
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)

        self.assertIn("Why not `kag-source-lift` first", review)
        self.assertIn("Do not move `instruction-surface` from this review alone", review)
        self.assertIn(
            "Run a direct-read migration review for `instruction-surface`",
            review,
        )
        self.assertIn("landed-diagnosis-repair-pilot-review", reviews_index)
        self.assertIn("landed diagnosis-repair pilot review: landed", ingress)
        self.assertIn("instruction-surface", ingress)
        self.assertIn("instruction-surface direct-read review: landed", ingress)
        self.assertIn("Landed Diagnosis-Repair Pilot Review", ingress)
        self.assertIn("`instruction-surface` is now chosen", distillation_roadmap)
        self.assertIn("accepted-for-fifth-migration-pilot", distillation_roadmap)
        self.assertIn("Landed diagnosis-repair pilot review", landing_log)
        self.assertIn("selected\n  `instruction-surface`", changelog)
        self.assertIn(
            "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
            root_roadmap,
        )
        self.assertIn("Landed Diagnosis-Repair Pilot Review", tree_contract)
        self.assertIn("instruction-surface", tree_contract)

    def test_instruction_surface_direct_read_review_accepts_fifth_pilot(self) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "instruction-surface-direct-read-migration-review.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Instruction-Surface Direct-Read Migration Review", review)
        self.assertIn("accepted-for-fifth-migration-pilot", review)
        self.assertIn("not path migration", review)
        self.assertIn("not\n`tree_path` frontmatter", review)
        self.assertIn("Accept `instruction-surface` as the fifth migration pilot", review)
        for technique_id in (
            "AOA-T-0012",
            "AOA-T-0013",
            "AOA-T-0024",
            "AOA-T-0027",
            "AOA-T-0029",
            "AOA-T-0030",
            "AOA-T-0035",
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)

        self.assertIn("Profile Edge", review)
        self.assertIn("Move exactly these seven bundles", review)
        self.assertIn("techniques/instruction/instruction-surface/", review)
        self.assertIn("Do not move files from this review pack alone", review)
        self.assertIn("Do not add `family` or `tree_path` frontmatter", review)
        self.assertIn("Run the fifth pilot migration", review)

        self.assertIn("instruction-surface-direct-read-migration-review", reviews_index)
        self.assertIn("instruction-surface direct-read review: landed", ingress)
        self.assertIn("accepted-for-fifth-migration-pilot", ingress)
        self.assertIn("instruction-surface migration: landed", ingress)
        self.assertIn("fifth pilot migration", ingress)
        self.assertIn("accepted-for-fifth-migration-pilot", distillation_roadmap)
        self.assertIn("fifth pilot migration is", distillation_roadmap)
        self.assertIn("techniques/instruction/instruction-surface/", distillation_roadmap)
        self.assertIn("Instruction-surface direct-read migration review", landing_log)
        self.assertIn("Instruction-surface tree pilot migration", landing_log)
        self.assertIn(
            "accepted the `instruction-surface` direct-read migration review",
            changelog,
        )
        self.assertIn("moved `AOA-T-0012`, `AOA-T-0013", changelog)
        self.assertIn(
            "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
            root_roadmap,
        )
        self.assertIn("Instruction-Surface Direct-Read Migration Review", tree_contract)
        self.assertIn("AOA-T-0012`, `AOA-T-0013", tree_contract)
        self.assertIn("2026-05-04-instruction-surface-tree-pilot.md", tree_contract)
        self.assertTrue(
            (
                REPO_ROOT
                / "techniques"
                / "instruction"
                / "instruction-surface"
                / "deterministic-context-composition"
                / "TECHNIQUE.md"
            ).is_file()
        )
        self.assertFalse(
            (
                REPO_ROOT
                / "techniques"
                / "docs"
                / "deterministic-context-composition"
            ).exists()
        )

    def test_landed_instruction_surface_pilot_review_selects_kag_source_lift(self) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "landed-instruction-surface-pilot-review.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Landed Instruction-Surface Pilot Review", review)
        self.assertIn("pilot-validated", review)
        self.assertIn("not path migration", review)
        self.assertIn("not `tree_path` frontmatter", review)
        self.assertIn("Accept the landed `instruction-surface` pilot", review)
        self.assertIn("first instruction trunk test", review)
        self.assertIn("Choose `kag-source-lift`", review)
        for technique_id in (
            "AOA-T-0018",
            "AOA-T-0019",
            "AOA-T-0020",
            "AOA-T-0021",
            "AOA-T-0022",
            "AOA-T-0046",
            "AOA-T-0047",
            "AOA-T-0048",
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)

        self.assertIn("Why not `docs-boundary` first", review)
        self.assertIn("Do not move `kag-source-lift` from this review alone", review)
        self.assertIn("Do not treat `knowledge-lift` as `aoa-kag`", review)
        self.assertIn("Run a direct-read migration review for `kag-source-lift`", review)

        self.assertIn("landed-instruction-surface-pilot-review", reviews_index)
        self.assertIn("landed instruction-surface pilot review: landed", ingress)
        self.assertIn("kag-source-lift", ingress)
        self.assertIn("next direct-read migration review", ingress)
        self.assertIn("`kag-source-lift` is now chosen", distillation_roadmap)
        self.assertIn("Landed instruction-surface pilot review", landing_log)
        self.assertIn("selected\n  `kag-source-lift`", changelog)
        self.assertIn(
            "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
            root_roadmap,
        )
        self.assertIn("Landed Instruction-Surface Pilot Review", tree_contract)
        self.assertIn("knowledge-lift", tree_contract)
        self.assertIn("kag-source-lift", tree_contract)

    def test_kag_source_lift_direct_read_review_accepts_sixth_pilot(self) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "kag-source-lift-direct-read-migration-review.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Kag-Source-Lift Direct-Read Migration Review", review)
        self.assertIn("accepted-for-sixth-migration-pilot", review)
        self.assertIn("not path migration", review)
        self.assertIn("not\n`tree_path` frontmatter", review)
        self.assertIn("Accept `kag-source-lift` as the sixth migration pilot", review)
        for technique_id in (
            "AOA-T-0018",
            "AOA-T-0019",
            "AOA-T-0020",
            "AOA-T-0021",
            "AOA-T-0022",
            "AOA-T-0046",
            "AOA-T-0047",
            "AOA-T-0048",
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)

        self.assertIn("Source-Lift Chain", review)
        self.assertIn("KAG Name Edge", review)
        self.assertIn("Move exactly these eight bundles", review)
        self.assertIn("techniques/knowledge-lift/kag-source-lift/", review)
        self.assertIn("Do not move files from this review pack alone", review)
        self.assertIn("Do not add `family` or `tree_path` frontmatter", review)
        self.assertIn("Do not treat `knowledge-lift` as `aoa-kag`", review)
        self.assertIn("Run the sixth pilot migration", review)

        self.assertIn("kag-source-lift-direct-read-migration-review", reviews_index)
        self.assertIn("kag-source-lift direct-read review: landed", ingress)
        self.assertIn("accepted-for-sixth-migration-pilot", ingress)
        self.assertIn("kag-source-lift migration: landed", ingress)
        self.assertIn("The sixth pilot migration is now landed", ingress)
        self.assertIn("accepted-for-sixth-migration-pilot", distillation_roadmap)
        self.assertIn("The sixth pilot migration is now", distillation_roadmap)
        self.assertIn("Kag-source-lift direct-read migration review", landing_log)
        self.assertIn("Kag-source-lift tree pilot migration", landing_log)
        self.assertIn("accepted the `kag-source-lift` direct-read migration review", changelog)
        self.assertIn("moved `AOA-T-0018`, `AOA-T-0019", changelog)
        self.assertIn(
            "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
            root_roadmap,
        )
        self.assertIn("Kag-Source-Lift Direct-Read Migration Review", tree_contract)
        self.assertIn("AOA-T-0018`, `AOA-T-0019", tree_contract)
        self.assertIn("2026-05-04-kag-source-lift-tree-pilot.md", tree_contract)

    def test_kag_source_lift_tree_pilot_migration_is_landed_after_direct_read(self) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("kag-source-lift migration: landed", ingress)
        self.assertIn("techniques/knowledge-lift/kag-source-lift/", ingress)
        self.assertIn("without frontmatter changes", ingress)
        self.assertIn("landed `kag-source-lift` pilot review", ingress)
        self.assertIn("sixth pilot migration is now", distillation_roadmap)
        self.assertIn("techniques/knowledge-lift/kag-source-lift/", distillation_roadmap)
        self.assertIn("Kag-source-lift tree pilot migration", landing_log)
        self.assertIn("legacy/receipts/2026-05-04-kag-source-lift-tree-pilot.md", landing_log)
        self.assertIn("sixth landed pilot moved `AOA-T-0018`", root_roadmap)
        self.assertIn(
            "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
            root_roadmap,
        )
        self.assertIn("2026-05-04-kag-source-lift-tree-pilot.md", tree_contract)
        self.assertIn("moved `AOA-T-0018`, `AOA-T-0019", changelog)
        self.assertTrue(
            (
                REPO_ROOT
                / "techniques"
                / "knowledge-lift"
                / "kag-source-lift"
                / "frontmatter-metadata-spine"
                / "TECHNIQUE.md"
            ).is_file()
        )
        self.assertFalse(
            (
                REPO_ROOT
                / "techniques"
                / "docs"
                / "frontmatter-metadata-spine"
            ).exists()
        )

    def test_landed_kag_source_lift_pilot_review_selects_docs_boundary(self) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "landed-kag-source-lift-pilot-review.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Landed Kag-Source-Lift Pilot Review", review)
        self.assertIn("pilot-validated", review)
        self.assertIn("not path migration", review)
        self.assertIn("not `tree_path` frontmatter", review)
        self.assertIn("Accept the landed `kag-source-lift` pilot", review)
        self.assertIn("first `knowledge-lift` trunk test", review)
        self.assertIn("Choose `docs-boundary`", review)
        for technique_id in (
            "AOA-T-0018",
            "AOA-T-0019",
            "AOA-T-0020",
            "AOA-T-0021",
            "AOA-T-0022",
            "AOA-T-0046",
            "AOA-T-0047",
            "AOA-T-0048",
            "AOA-T-0002",
            "AOA-T-0009",
            "AOA-T-0034",
            "AOA-T-0033",
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)

        self.assertIn("KAG Name Edge", review)
        self.assertIn("Do not move `docs-boundary` from this review alone", review)
        self.assertIn("Do not treat `knowledge-lift` as `aoa-kag`", review)
        self.assertIn("Run a direct-read migration review for `docs-boundary`", review)

        self.assertIn("landed-kag-source-lift-pilot-review", reviews_index)
        self.assertIn("landed kag-source-lift pilot review: landed", ingress)
        self.assertIn("docs-boundary", ingress)
        self.assertIn("direct-read migration review", ingress)
        self.assertIn("`docs-boundary` for the next", distillation_roadmap)
        self.assertIn("Landed kag-source-lift pilot review", landing_log)
        self.assertIn("selected\n  `docs-boundary`", changelog)
        self.assertIn(
            "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
            root_roadmap,
        )
        self.assertIn("Landed Kag-Source-Lift Pilot Review", tree_contract)
        self.assertIn("docs-boundary", tree_contract)

    def test_docs_boundary_direct_read_review_accepts_seventh_pilot(self) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "docs-boundary-direct-read-migration-review.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Docs-Boundary Direct-Read Migration Review", review)
        self.assertIn("accepted-for-seventh-migration-pilot", review)
        self.assertIn("not path migration", review)
        self.assertIn("not\n`tree_path` frontmatter", review)
        self.assertIn("Accept `docs-boundary` as the seventh migration pilot", review)
        for technique_id in (
            "AOA-T-0002",
            "AOA-T-0009",
            "AOA-T-0034",
            "AOA-T-0033",
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)

        self.assertIn("Boundary Chain", review)
        self.assertIn("Instruction Trunk Fit", review)
        self.assertIn("Mixed Kind Stress", review)
        self.assertIn("Move exactly these four bundles", review)
        self.assertIn("techniques/instruction/docs-boundary/", review)
        self.assertIn("Do not move files from this review pack alone", review)
        self.assertIn("Do not add `family` or `tree_path` frontmatter", review)
        self.assertIn("Do not turn `docs-boundary` into source-of-truth governance", review)
        self.assertIn("Run the seventh pilot migration", review)

        self.assertIn("docs-boundary-direct-read-migration-review", reviews_index)
        self.assertIn("docs-boundary direct-read review: landed", ingress)
        self.assertIn("accepted-for-seventh-migration-pilot", ingress)
        self.assertIn("docs-boundary migration: landed", ingress)
        self.assertIn("accepted-for-seventh-migration-pilot", distillation_roadmap)
        self.assertIn("The seventh pilot migration is now landed", distillation_roadmap)
        self.assertIn("Docs-boundary direct-read migration review", landing_log)
        self.assertIn("accepted the `docs-boundary` direct-read migration review", changelog)
        self.assertIn("moved `AOA-T-0002`, `AOA-T-0009", changelog)
        self.assertIn(
            "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
            root_roadmap,
        )
        self.assertIn("Docs-Boundary Direct-Read Migration Review", tree_contract)
        self.assertIn("AOA-T-0002`, `AOA-T-0009", tree_contract)
        self.assertIn("2026-05-04-docs-boundary-tree-pilot.md", tree_contract)
        self.assertTrue(
            (
                REPO_ROOT
                / "techniques"
                / "instruction"
                / "docs-boundary"
                / "source-of-truth-layout"
                / "TECHNIQUE.md"
            ).is_file()
        )
        self.assertFalse(
            (
                REPO_ROOT
                / "techniques"
                / "docs"
                / "source-of-truth-layout"
            ).exists()
        )

    def test_docs_boundary_tree_pilot_migration_is_landed_after_direct_read(self) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("docs-boundary migration: landed", ingress)
        self.assertIn("techniques/instruction/docs-boundary/", ingress)
        self.assertIn("without frontmatter changes", ingress)
        self.assertIn("landed docs-boundary pilot review", ingress)
        self.assertIn("seventh pilot migration is now landed", distillation_roadmap)
        self.assertIn("techniques/instruction/docs-boundary/", distillation_roadmap)
        self.assertIn("Docs-boundary tree pilot migration", landing_log)
        self.assertIn("legacy/receipts/2026-05-04-docs-boundary-tree-pilot.md", landing_log)
        self.assertIn("seventh landed pilot moved `AOA-T-0002`", root_roadmap)
        self.assertIn(
            "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
            root_roadmap,
        )
        self.assertIn("2026-05-04-docs-boundary-tree-pilot.md", tree_contract)
        self.assertIn("moved `AOA-T-0002`, `AOA-T-0009", changelog)
        self.assertTrue(
            (
                REPO_ROOT
                / "techniques"
                / "instruction"
                / "docs-boundary"
                / "decision-rationale-recording"
                / "TECHNIQUE.md"
            ).is_file()
        )
        self.assertFalse(
            (
                REPO_ROOT
                / "techniques"
                / "docs"
                / "decision-rationale-recording"
            ).exists()
        )

    def test_landed_docs_boundary_pilot_review_selects_capability_registry(
        self,
    ) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "landed-docs-boundary-pilot-review.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Landed Docs-Boundary Pilot Review", review)
        self.assertIn("pilot-validated", review)
        self.assertIn("not path migration", review)
        self.assertIn("not `tree_path` frontmatter", review)
        self.assertIn("Accept the landed `docs-boundary` pilot", review)
        self.assertIn(
            "second successful shelf under the `instruction` trunk",
            review,
        )
        self.assertIn("Choose `capability-registry`", review)
        for technique_id in (
            "AOA-T-0002",
            "AOA-T-0009",
            "AOA-T-0034",
            "AOA-T-0033",
            "AOA-T-0025",
            "AOA-T-0063",
            "AOA-T-0064",
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)

        self.assertIn(
            "Do not move `capability-registry` from this review alone",
            review,
        )
        self.assertIn("registry product doctrine", review)
        self.assertIn(
            "Run a direct-read migration review for `capability-registry`",
            review,
        )

        self.assertIn("landed-docs-boundary-pilot-review", reviews_index)
        self.assertIn("landed docs-boundary pilot review: landed", ingress)
        self.assertIn("capability-registry", ingress)
        self.assertIn("direct-read migration review", ingress)
        self.assertIn("`capability-registry` for the next", distillation_roadmap)
        self.assertIn(
            "eighth pilot migration is landed",
            distillation_roadmap,
        )
        self.assertIn("Landed docs-boundary pilot review", landing_log)
        self.assertIn("second successful instruction trunk shelf", landing_log)
        self.assertIn("selected\n  `capability-registry`", changelog)
        self.assertIn(
            "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
            root_roadmap,
        )
        self.assertIn("Landed Docs-Boundary Pilot Review", tree_contract)
        self.assertIn("capability-registry", tree_contract)

    def test_capability_registry_direct_read_review_accepts_eighth_pilot(
        self,
    ) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "capability-registry-direct-read-migration-review.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Capability-Registry Direct-Read Migration Review", review)
        self.assertIn("accepted-for-eighth-migration-pilot", review)
        self.assertIn("not path migration", review)
        self.assertIn("not\n`tree_path` frontmatter", review)
        self.assertIn("Accept `capability-registry` as the eighth", review)
        self.assertIn("spec-entry-query chain", review)
        self.assertIn("Direct Bundle Read", review)
        for technique_id in ("AOA-T-0025", "AOA-T-0063", "AOA-T-0064"):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)

        self.assertIn("Move exactly these three bundles", review)
        self.assertIn("techniques/instruction/capability-registry/", review)
        self.assertIn("Do not move files from this review pack alone", review)
        self.assertIn("Do not add `tree_path`", review)
        self.assertIn("registry product doctrine", review)
        self.assertIn("Do not collapse the three leaves into one technique", review)
        self.assertIn("Run the eighth pilot migration", review)

        self.assertIn("capability-registry-direct-read-migration-review", reviews_index)
        self.assertIn("capability-registry direct-read review: landed", ingress)
        self.assertIn("accepted-for-eighth-migration-pilot", ingress)
        self.assertIn("capability-registry migration: landed", ingress)
        self.assertIn("accepted-for-eighth-migration-pilot", distillation_roadmap)
        self.assertIn("eighth pilot migration is landed", distillation_roadmap)
        self.assertIn("Capability-registry direct-read migration review", landing_log)
        self.assertIn("Capability-registry tree pilot migration", landing_log)
        self.assertIn("spec-entry-query chain", landing_log)
        self.assertIn(
            "accepted the `capability-registry` direct-read migration review",
            changelog,
        )
        self.assertIn(
            "moved `AOA-T-0025`, `AOA-T-0063`, and `AOA-T-0064` into",
            changelog,
        )
        self.assertIn(
            "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
            root_roadmap,
        )
        self.assertIn("Capability-Registry Direct-Read Migration Review", tree_contract)
        self.assertIn("2026-05-04-capability-registry-tree-pilot.md", tree_contract)
        self.assertIn("AOA-T-0025`, `AOA-T-0063", tree_contract)
        self.assertTrue(
            (
                REPO_ROOT
                / "techniques"
                / "instruction"
                / "capability-registry"
                / "capability-spec-versioning"
                / "TECHNIQUE.md"
            ).is_file()
        )
        self.assertFalse(
            (
                REPO_ROOT
                / "techniques"
                / "docs"
                / "capability-spec-versioning"
            ).exists()
        )

    def test_landed_capability_registry_pilot_review_selects_capability_boundary(
        self,
    ) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "landed-capability-registry-pilot-review.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Landed Capability-Registry Pilot Review", review)
        self.assertIn("pilot-validated", review)
        self.assertIn("choose `capability-boundary`", review)
        self.assertIn("not path migration", review)
        self.assertIn("third successful shelf under the `instruction` trunk", review)
        self.assertIn("What The Eighth Pilot Proved", review)
        self.assertIn("Ninth Shelf Choice", review)
        for technique_id in ("AOA-T-0040", "AOA-T-0043", "AOA-T-0093"):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)

        self.assertIn("Projected shelf", review)
        self.assertIn("techniques/instruction/capability-boundary/", review)
        self.assertIn("Why direct-read first", review)
        self.assertIn(
            "Do not move `capability-boundary` from this review alone",
            review,
        )
        self.assertIn("Do not add `tree_path`", review)
        self.assertIn("Run a direct-read migration review for `capability-boundary`", review)

        self.assertIn("landed-capability-registry-pilot-review", reviews_index)
        self.assertIn("landed capability-registry pilot review: landed", ingress)
        self.assertIn("capability-boundary", ingress)
        self.assertIn("direct-read migration review", ingress)
        self.assertIn("capability-boundary` for the next direct-read", distillation_roadmap)
        self.assertIn("ninth pilot migration is now landed exactly", distillation_roadmap)
        self.assertIn("Landed capability-registry pilot review", landing_log)
        self.assertIn("third successful instruction trunk shelf", landing_log)
        self.assertIn(
            "accepted the landed `capability-registry` pilot review",
            changelog,
        )
        self.assertIn(
            "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
            root_roadmap,
        )
        self.assertIn("Landed Capability-Registry Pilot Review", tree_contract)
        self.assertIn("capability-boundary", tree_contract)
        self.assertFalse(
            (
                REPO_ROOT
                / "techniques"
                / "docs"
                / "skill-vs-command-boundary"
                / "TECHNIQUE.md"
            ).is_file()
        )
        self.assertTrue(
            (
                REPO_ROOT
                / "techniques"
                / "instruction"
                / "capability-boundary"
                / "skill-vs-command-boundary"
                / "TECHNIQUE.md"
            ).is_file()
        )
        self.assertFalse(
            (
                REPO_ROOT
                / "techniques"
                / "agent-workflows"
                / "recommendation-truth-vs-host-actionability"
                / "TECHNIQUE.md"
            ).is_file()
        )
        self.assertTrue(
            (
                REPO_ROOT
                / "techniques"
                / "instruction"
                / "capability-boundary"
                / "recommendation-truth-vs-host-actionability"
                / "TECHNIQUE.md"
            ).is_file()
        )

    def test_capability_boundary_direct_read_review_accepts_ninth_pilot(
        self,
    ) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "capability-boundary-direct-read-migration-review.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Capability-Boundary Direct-Read Migration Review", review)
        self.assertIn("accepted-for-ninth-migration-pilot", review)
        self.assertIn("not path migration", review)
        self.assertIn("not\n`tree_path` frontmatter", review)
        self.assertIn("Accept `capability-boundary` as the ninth", review)
        self.assertIn("Direct Bundle Read", review)
        for technique_id in ("AOA-T-0040", "AOA-T-0043", "AOA-T-0093"):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)

        self.assertIn("all three are promoted guardrails", review.lower())
        self.assertIn("Instruction Trunk Fit", review)
        self.assertIn("Boundary Watch Accepted", review)
        self.assertIn("Move exactly these three bundles", review)
        self.assertIn("techniques/instruction/capability-boundary/", review)
        self.assertIn("skill-discovery` should wait", review)
        self.assertIn("Do not move files from this review pack alone", review)
        self.assertIn("Do not add `tree_path`", review)
        self.assertIn("Do not collapse the three leaves", review)
        self.assertIn("Run the ninth pilot migration", review)

        self.assertIn("capability-boundary-direct-read-migration-review", reviews_index)
        self.assertIn("capability-boundary direct-read review: landed", ingress)
        self.assertIn("accepted-for-ninth-migration-pilot", ingress)
        self.assertIn("Capability-boundary direct-read migration review", landing_log)
        self.assertIn("shared capability-boundary guardrail cluster", landing_log)
        self.assertIn("accepted-for-ninth-migration-pilot", distillation_roadmap)
        self.assertIn("ninth pilot migration is now landed exactly", distillation_roadmap)
        self.assertIn(
            "accepted the `capability-boundary` direct-read migration review",
            changelog,
        )
        self.assertIn(
            "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
            root_roadmap,
        )
        self.assertIn("Capability-Boundary Direct-Read Migration Review", tree_contract)
        self.assertIn("AOA-T-0040`, `AOA-T-0043`, and `AOA-T-0093", tree_contract)
        self.assertFalse(
            (
                REPO_ROOT
                / "techniques"
                / "docs"
                / "skill-vs-command-boundary"
                / "TECHNIQUE.md"
            ).is_file()
        )
        self.assertTrue(
            (
                REPO_ROOT
                / "techniques"
                / "instruction"
                / "capability-boundary"
                / "skill-vs-command-boundary"
                / "TECHNIQUE.md"
            ).is_file()
        )
        self.assertFalse(
            (
                REPO_ROOT
                / "techniques"
                / "agent-workflows"
                / "recommendation-truth-vs-host-actionability"
                / "TECHNIQUE.md"
            ).is_file()
        )
        self.assertTrue(
            (
                REPO_ROOT
                / "techniques"
                / "instruction"
                / "capability-boundary"
                / "recommendation-truth-vs-host-actionability"
                / "TECHNIQUE.md"
            ).is_file()
        )

    def test_capability_boundary_tree_pilot_migration_is_recorded(self) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        receipt = (
            REPO_ROOT
            / "legacy"
            / "receipts"
            / "2026-05-04-capability-boundary-tree-pilot.md"
        ).read_text(encoding="utf-8")

        self.assertIn("capability-boundary migration: landed exactly", ingress)
        self.assertIn("Capability-Boundary Tree Pilot Receipt", ingress)
        self.assertIn("Capability-boundary tree pilot migration", landing_log)
        self.assertIn("ninth pilot migration is now landed exactly", distillation_roadmap)
        self.assertIn(
            "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
            root_roadmap,
        )
        self.assertIn("ninth pilot migration moves exactly", tree_contract)
        self.assertIn("2026-05-04-capability-boundary-tree-pilot.md", tree_contract)
        self.assertIn("moved `AOA-T-0040`, `AOA-T-0043`, and `AOA-T-0093`", changelog)
        self.assertIn("They did not pass through root `legacy/`.", receipt)
        self.assertIn("Do not add `tree_path` frontmatter.", receipt)

        for relative_path in (
            "techniques/instruction/capability-boundary/skill-vs-command-boundary/TECHNIQUE.md",
            "techniques/instruction/capability-boundary/multi-source-primary-input-provenance/TECHNIQUE.md",
            "techniques/instruction/capability-boundary/recommendation-truth-vs-host-actionability/TECHNIQUE.md",
        ):
            with self.subTest(relative_path=relative_path):
                self.assertTrue((REPO_ROOT / relative_path).is_file())

    def test_landed_capability_boundary_pilot_review_selects_skill_discovery(
        self,
    ) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "landed-capability-boundary-pilot-review.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Landed Capability-Boundary Pilot Review", review)
        self.assertIn("pilot-validated", review)
        self.assertIn("fourth successful shelf under the `instruction` trunk", review)
        self.assertIn("What The Ninth Pilot Proved", review)
        self.assertIn("Tenth Shelf Choice", review)
        self.assertIn("Choose `skill-discovery`", review)
        self.assertIn("AOA-T-0041", review)
        self.assertIn("AOA-T-0042", review)
        self.assertIn("techniques/instruction/skill-discovery/", review)
        self.assertIn("Why direct-read first", review)
        self.assertIn("Do not move `skill-discovery` from this review alone", review)
        self.assertIn("Do not add `tree_path`", review)
        self.assertIn("Run a direct-read migration review for `skill-discovery`", review)

        self.assertIn("landed-capability-boundary-pilot-review", reviews_index)
        self.assertIn("landed capability-boundary pilot review: landed", ingress)
        self.assertIn("skill-discovery` chosen", ingress)
        self.assertIn("Landed capability-boundary pilot review", landing_log)
        self.assertIn("fourth successful instruction trunk shelf", landing_log)
        self.assertIn("skill-discovery` for the next direct-read", distillation_roadmap)
        self.assertIn(
            "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
            root_roadmap,
        )
        self.assertIn("Landed Capability-Boundary Pilot Review", tree_contract)
        self.assertIn("Skill-Discovery Direct-Read Migration Review", tree_contract)
        self.assertIn(
            "accepted the landed `capability-boundary` pilot review",
            changelog,
        )
        self.assertFalse(
            (
                REPO_ROOT
                / "techniques"
                / "docs"
                / "skill-marketplace-curation"
                / "TECHNIQUE.md"
            ).is_file()
        )
        self.assertFalse(
            (
                REPO_ROOT
                / "techniques"
                / "evaluation"
                / "upstream-skill-health-checking"
                / "TECHNIQUE.md"
            ).is_file()
        )
        self.assertTrue(
            (
                REPO_ROOT
                / "techniques"
                / "instruction"
                / "skill-discovery"
            ).exists()
        )

    def test_skill_discovery_direct_read_review_accepts_tenth_pilot(
        self,
    ) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "skill-discovery-direct-read-migration-review.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        flat_distillation_roadmap = " ".join(distillation_roadmap.split())

        self.assertIn("Skill-Discovery Direct-Read Migration Review", review)
        self.assertIn("accepted-for-tenth-migration-pilot", review)
        self.assertIn("not path migration", review)
        self.assertIn("not\n`tree_path` frontmatter", review)
        self.assertIn("Accept `skill-discovery` as the tenth", review)
        self.assertIn("Direct Bundle Read", review)
        for technique_id in ("AOA-T-0041", "AOA-T-0042"):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)

        self.assertIn("techniques/docs/skill-marketplace-curation/", review)
        self.assertIn(
            "techniques/evaluation/upstream-skill-health-checking/",
            review,
        )
        self.assertIn("Instruction Trunk Fit", review)
        self.assertIn("Boundary Watch Accepted", review)
        self.assertIn("Move exactly these two bundles", review)
        self.assertIn("techniques/instruction/skill-discovery/", review)
        self.assertIn("Do not move files from this review pack alone", review)
        self.assertIn("Do not add `tree_path`", review)
        self.assertIn("Do not collapse curated marketplace discoverability", review)
        self.assertIn("Run the tenth pilot migration", review)

        self.assertIn("skill-discovery-direct-read-migration-review", reviews_index)
        self.assertIn("skill-discovery direct-read review: landed", ingress)
        self.assertIn("accepted-for-tenth-migration-pilot", ingress)
        self.assertIn("Skill-discovery direct-read migration review", landing_log)
        self.assertIn("shared skill-surfacing shelf", landing_log)
        self.assertIn("accepted-for-tenth-migration-pilot", distillation_roadmap)
        self.assertIn("tenth pilot migration is now landed exactly", flat_distillation_roadmap)
        self.assertIn(
            "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
            root_roadmap,
        )
        self.assertIn("Skill-Discovery Direct-Read Migration Review", tree_contract)
        self.assertIn("AOA-T-0041` and `AOA-T-0042", tree_contract)
        self.assertIn("2026-05-05-skill-discovery-tree-pilot.md", tree_contract)
        self.assertIn(
            "accepted the `skill-discovery` direct-read migration review",
            changelog,
        )
        self.assertIn("moved `AOA-T-0041` and `AOA-T-0042`", changelog)
        self.assertFalse(
            (
                REPO_ROOT
                / "techniques"
                / "docs"
                / "skill-marketplace-curation"
                / "TECHNIQUE.md"
            ).is_file()
        )
        self.assertFalse(
            (
                REPO_ROOT
                / "techniques"
                / "evaluation"
                / "upstream-skill-health-checking"
                / "TECHNIQUE.md"
            ).is_file()
        )
        self.assertTrue(
            (
                REPO_ROOT
                / "techniques"
                / "instruction"
                / "skill-discovery"
            ).exists()
        )

    def test_landed_skill_discovery_pilot_review_selects_skill_support(
        self,
    ) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "landed-skill-discovery-pilot-review.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        flat_distillation_roadmap = " ".join(distillation_roadmap.split())
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Landed Skill-Discovery Pilot Review", review)
        self.assertIn("pilot-validated", review)
        self.assertIn("fifth successful shelf under the `instruction` trunk", review)
        self.assertIn("What The Tenth Pilot Proved", review)
        self.assertIn("Remaining Weaknesses", review)
        self.assertIn("Eleventh Shelf Choice", review)
        self.assertIn("Choose `skill-support`", review)
        for technique_id in ("AOA-T-0016", "AOA-T-0015", "AOA-T-0017"):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)

        self.assertIn("techniques/proof/skill-support/", review)
        self.assertIn("Do not move `skill-support` from this review alone", review)
        self.assertIn("Do not add `tree_path`", review)
        self.assertIn("Run a direct-read migration review for `skill-support`", review)
        self.assertIn("landed-skill-discovery-pilot-review", reviews_index)
        self.assertIn("landed skill-discovery pilot review: landed", ingress)
        self.assertIn("skill-support` chosen", ingress)
        self.assertIn("Landed skill-discovery pilot review", landing_log)
        self.assertIn("fifth successful instruction trunk shelf", landing_log)
        self.assertIn(
            "skill-support` for the next direct-read",
            flat_distillation_roadmap,
        )
        self.assertIn(
            "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
            root_roadmap,
        )
        self.assertIn("Landed Skill-Discovery Pilot Review", tree_contract)
        self.assertIn("chooses `skill-support`", tree_contract)
        self.assertIn(
            "accepted the landed `skill-discovery` pilot review",
            changelog,
        )
        self.assertTrue(
            (
                REPO_ROOT
                / "techniques"
                / "proof"
                / "skill-support"
                / "bounded-context-map"
                / "TECHNIQUE.md"
            ).is_file()
        )
        self.assertTrue(
            (
                REPO_ROOT
                / "techniques"
                / "proof"
                / "skill-support"
                / "contract-test-design"
                / "TECHNIQUE.md"
            ).is_file()
        )
        self.assertTrue(
            (
                REPO_ROOT
                / "techniques"
                / "proof"
                / "skill-support"
                / "property-invariants"
                / "TECHNIQUE.md"
            ).is_file()
        )
        for old_parts in (
            ("docs", "bounded-context-map"),
            ("evaluation", "contract-test-design"),
            ("evaluation", "property-invariants"),
        ):
            with self.subTest(old_parts=old_parts):
                self.assertFalse(
                    (REPO_ROOT / "techniques" / old_parts[0] / old_parts[1]).exists()
                )

        self.assertTrue(
            (
                REPO_ROOT
                / "techniques"
                / "proof"
                / "skill-support"
            ).exists()
        )

    def test_skill_support_direct_read_migration_review_accepts_eleventh_pilot(
        self,
    ) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "skill-support-direct-read-migration-review.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Skill-Support Direct-Read Migration Review", review)
        self.assertIn("accepted-for-eleventh-migration-pilot", review)
        self.assertIn("not path migration", review)
        self.assertIn("not\n`tree_path` frontmatter", review)
        self.assertIn("Accept `skill-support` as the eleventh", review)
        self.assertIn("Direct Bundle Read", review)
        self.assertIn("Why The Shelf Holds", review)
        self.assertIn("Proof Trunk Fit", review)
        self.assertIn("Boundary Watch Accepted", review)
        for technique_id in ("AOA-T-0016", "AOA-T-0015", "AOA-T-0017"):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)

        self.assertIn("techniques/docs/bounded-context-map/", review)
        self.assertIn("techniques/evaluation/contract-test-design/", review)
        self.assertIn("techniques/evaluation/property-invariants/", review)
        self.assertIn("techniques/proof/skill-support/", review)
        self.assertIn("Move exactly these three bundles", review)
        self.assertIn("Do not move files from this review pack alone", review)
        self.assertIn("Do not add `tree_path`", review)
        self.assertIn("Do not treat `skill-support` as proof authority", review)
        self.assertIn("Run the eleventh pilot migration", review)

        self.assertIn("skill-support-direct-read-migration-review", reviews_index)
        self.assertIn("skill-support direct-read review: landed", ingress)
        self.assertIn("accepted-for-eleventh-migration-pilot", ingress)
        self.assertIn("Skill-support direct-read migration review", landing_log)
        self.assertIn("Skill-support tree pilot migration", landing_log)
        self.assertIn("proof-side support triangle", landing_log)
        self.assertIn("accepted-for-eleventh-migration-pilot", distillation_roadmap)
        self.assertIn(
            "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
            root_roadmap,
        )
        self.assertIn("Skill-Support Direct-Read Migration Review", tree_contract)
        self.assertIn("AOA-T-0016`, `AOA-T-0015`, and `AOA-T-0017", tree_contract)
        self.assertIn(
            "accepted the `skill-support` direct-read migration review",
            changelog,
        )
        self.assertTrue(
            (
                REPO_ROOT
                / "techniques"
                / "proof"
                / "skill-support"
                / "bounded-context-map"
                / "TECHNIQUE.md"
            ).is_file()
        )
        self.assertTrue(
            (
                REPO_ROOT
                / "techniques"
                / "proof"
                / "skill-support"
                / "contract-test-design"
                / "TECHNIQUE.md"
            ).is_file()
        )
        self.assertTrue(
            (
                REPO_ROOT
                / "techniques"
                / "proof"
                / "skill-support"
                / "property-invariants"
                / "TECHNIQUE.md"
            ).is_file()
        )
        self.assertTrue((REPO_ROOT / "techniques" / "proof" / "skill-support").exists())

    def test_skill_support_tree_pilot_migration_lands_eleventh_shelf(self) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        receipt = (
            REPO_ROOT
            / "legacy"
            / "receipts"
            / "2026-05-05-skill-support-tree-pilot.md"
        ).read_text(encoding="utf-8")
        proof_route = (
            REPO_ROOT / "techniques" / "proof" / "AGENTS.md"
        ).read_text(encoding="utf-8")

        self.assertIn("skill-support migration: landed exactly", ingress)
        self.assertIn("Skill-Support Tree Pilot Receipt", ingress)
        self.assertIn("migration is now landed exactly", distillation_roadmap)
        self.assertIn("Skill-support tree pilot migration", landing_log)
        self.assertIn(
            "Review the landed `evaluation-chain` pilot",
            root_roadmap,
        )
        self.assertIn("eleventh pilot migration moves exactly", tree_contract)
        self.assertIn("2026-05-05-skill-support-tree-pilot.md", tree_contract)
        self.assertIn(
            "moved `AOA-T-0016`, `AOA-T-0015`, and `AOA-T-0017`",
            changelog,
        )
        self.assertIn("techniques/proof/skill-support/", receipt)
        self.assertIn("skill-support/", proof_route)
        self.assertIn("proof verdict authority", proof_route)

        for new_path in (
            "techniques/proof/skill-support/bounded-context-map/TECHNIQUE.md",
            "techniques/proof/skill-support/contract-test-design/TECHNIQUE.md",
            "techniques/proof/skill-support/property-invariants/TECHNIQUE.md",
        ):
            with self.subTest(new_path=new_path):
                self.assertTrue((REPO_ROOT / new_path).is_file())

        for old_path in (
            "techniques/docs/bounded-context-map",
            "techniques/evaluation/contract-test-design",
            "techniques/evaluation/property-invariants",
        ):
            with self.subTest(old_path=old_path):
                self.assertFalse((REPO_ROOT / old_path).exists())

    def test_landed_skill_support_pilot_review_selects_evaluation_chain(
        self,
    ) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "landed-skill-support-pilot-review.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        flat_distillation_roadmap = " ".join(distillation_roadmap.split())
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Landed Skill-Support Pilot Review", review)
        self.assertIn("pilot-validated", review)
        self.assertIn("first successful shelf under the `proof` trunk", review)
        self.assertIn("What The Eleventh Pilot Proved", review)
        self.assertIn("Remaining Weaknesses", review)
        self.assertIn("Twelfth Shelf Choice", review)
        self.assertIn("Choose `evaluation-chain`", review)
        for technique_id in (
            "AOA-T-0003",
            "AOA-T-0007",
            "AOA-T-0032",
            "AOA-T-0016",
            "AOA-T-0015",
            "AOA-T-0017",
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)

        self.assertIn("techniques/proof/evaluation-chain/", review)
        self.assertIn("Do not move `evaluation-chain` from this review alone", review)
        self.assertIn("Do not add `tree_path`", review)
        self.assertIn("Run a direct-read migration review for `evaluation-chain`", review)
        self.assertIn("landed-skill-support-pilot-review", reviews_index)
        self.assertIn("landed skill-support pilot review: landed", ingress)
        self.assertIn("evaluation-chain` chosen", ingress)
        self.assertIn("Landed skill-support pilot review", landing_log)
        self.assertIn("first successful proof trunk shelf", landing_log)
        self.assertIn("evaluation-chain` for the next direct-read", flat_distillation_roadmap)
        self.assertIn(
            "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
            root_roadmap,
        )
        self.assertIn("Landed Skill-Support Pilot Review", tree_contract)
        self.assertIn("chooses `evaluation-chain`", tree_contract)
        self.assertIn(
            "accepted the landed `skill-support` pilot review",
            changelog,
        )
        self.assertTrue(
            (
                REPO_ROOT
                / "techniques"
                / "proof"
                / "evaluation-chain"
                / "contract-first-smoke-summary"
                / "TECHNIQUE.md"
            ).is_file()
        )
        self.assertTrue(
            (
                REPO_ROOT
                / "techniques"
                / "proof"
                / "evaluation-chain"
                / "signal-first-gate-promotion"
                / "TECHNIQUE.md"
            ).is_file()
        )
        self.assertTrue(
            (
                REPO_ROOT
                / "techniques"
                / "proof"
                / "evaluation-chain"
                / "context-report-for-ci"
                / "TECHNIQUE.md"
            ).is_file()
        )
        for old_slug in (
            "contract-first-smoke-summary",
            "signal-first-gate-promotion",
            "context-report-for-ci",
        ):
            with self.subTest(old_slug=old_slug):
                self.assertFalse(
                    (REPO_ROOT / "techniques" / "evaluation" / old_slug).exists()
                )

    def test_evaluation_chain_direct_read_migration_review_accepts_twelfth_pilot(
        self,
    ) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "evaluation-chain-direct-read-migration-review.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Evaluation-Chain Direct-Read Migration Review", review)
        self.assertIn("accepted-for-twelfth-migration-pilot", review)
        self.assertIn("not path migration", review)
        self.assertIn("not\n`tree_path` frontmatter", review)
        self.assertIn("Accept `evaluation-chain` as the twelfth", review)
        self.assertIn("Direct Bundle Read", review)
        self.assertIn("Why The Shelf Holds", review)
        self.assertIn("Proof Trunk Fit", review)
        self.assertIn("Boundary Watch Accepted", review)
        for technique_id in ("AOA-T-0003", "AOA-T-0007", "AOA-T-0032"):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)

        self.assertIn("techniques/evaluation/contract-first-smoke-summary/", review)
        self.assertIn("techniques/evaluation/signal-first-gate-promotion/", review)
        self.assertIn("techniques/evaluation/context-report-for-ci/", review)
        self.assertIn("techniques/proof/evaluation-chain/", review)
        self.assertIn("Move exactly these three bundles", review)
        self.assertIn("Do not move files from this review pack alone", review)
        self.assertIn("Do not add `tree_path`", review)
        self.assertIn("Do not treat `evaluation-chain` as CI ownership", review)
        self.assertIn("Do not promote `AOA-T-0032`", review)
        self.assertIn("Run the twelfth pilot migration", review)

        self.assertIn("evaluation-chain-direct-read-migration-review", reviews_index)
        self.assertIn("evaluation-chain direct-read review: landed", ingress)
        self.assertIn("accepted-for-twelfth-migration-pilot", ingress)
        self.assertIn("Evaluation-chain direct-read migration review", landing_log)
        self.assertIn("proof-facing chain", landing_log)
        self.assertIn("accepted-for-twelfth-migration-pilot", distillation_roadmap)
        self.assertIn(
            "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
            root_roadmap,
        )
        self.assertIn("Evaluation-Chain Direct-Read Migration Review", tree_contract)
        self.assertIn("AOA-T-0003`, `AOA-T-0007`, and `AOA-T-0032", tree_contract)
        self.assertIn(
            "accepted the `evaluation-chain` direct-read migration review",
            changelog,
        )
        self.assertTrue(
            (
                REPO_ROOT
                / "techniques"
                / "proof"
                / "evaluation-chain"
                / "contract-first-smoke-summary"
                / "TECHNIQUE.md"
            ).is_file()
        )
        self.assertTrue(
            (
                REPO_ROOT
                / "techniques"
                / "proof"
                / "evaluation-chain"
                / "signal-first-gate-promotion"
                / "TECHNIQUE.md"
            ).is_file()
        )
        self.assertTrue(
            (
                REPO_ROOT
                / "techniques"
                / "proof"
                / "evaluation-chain"
                / "context-report-for-ci"
                / "TECHNIQUE.md"
            ).is_file()
        )
        for old_slug in (
            "contract-first-smoke-summary",
            "signal-first-gate-promotion",
            "context-report-for-ci",
        ):
            with self.subTest(old_slug=old_slug):
                self.assertFalse(
                    (REPO_ROOT / "techniques" / "evaluation" / old_slug).exists()
                )

    def test_evaluation_chain_tree_pilot_migration_lands_twelfth_shelf(
        self,
    ) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        receipt = (
            REPO_ROOT
            / "legacy"
            / "receipts"
            / "2026-05-05-evaluation-chain-tree-pilot.md"
        ).read_text(encoding="utf-8")
        proof_route = (
            REPO_ROOT / "techniques" / "proof" / "AGENTS.md"
        ).read_text(encoding="utf-8")

        self.assertIn("evaluation-chain migration: landed exactly", ingress)
        self.assertIn("Evaluation-Chain Tree Pilot Receipt", ingress)
        self.assertIn("twelfth pilot migration is now landed exactly", distillation_roadmap)
        self.assertIn("Evaluation-chain tree pilot migration", landing_log)
        self.assertIn("twelfth landed pilot moved `AOA-T-0003`", root_roadmap)
        self.assertIn("Review the landed `evaluation-chain` pilot", root_roadmap)
        self.assertIn("twelfth pilot migration moves exactly", tree_contract)
        self.assertIn("2026-05-05-evaluation-chain-tree-pilot.md", tree_contract)
        self.assertIn(
            "moved `AOA-T-0003`, `AOA-T-0007`, and `AOA-T-0032`",
            changelog,
        )
        self.assertIn("techniques/proof/evaluation-chain/", receipt)
        self.assertIn("evaluation-chain/", proof_route)
        self.assertIn("CI ownership", proof_route)

        for new_path in (
            "techniques/proof/evaluation-chain/contract-first-smoke-summary/TECHNIQUE.md",
            "techniques/proof/evaluation-chain/signal-first-gate-promotion/TECHNIQUE.md",
            "techniques/proof/evaluation-chain/context-report-for-ci/TECHNIQUE.md",
        ):
            with self.subTest(new_path=new_path):
                self.assertTrue((REPO_ROOT / new_path).is_file())

        for old_path in (
            "techniques/evaluation/contract-first-smoke-summary",
            "techniques/evaluation/signal-first-gate-promotion",
            "techniques/evaluation/context-report-for-ci",
        ):
            with self.subTest(old_path=old_path):
                self.assertFalse((REPO_ROOT / old_path).exists())

    def test_landed_evaluation_chain_pilot_review_selects_published_summary(
        self,
    ) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "landed-evaluation-chain-pilot-review.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Landed Evaluation-Chain Pilot Review", review)
        self.assertIn("pilot-validated", review)
        self.assertIn("second successful shelf under the `proof` trunk", review)
        self.assertIn("What The Twelfth Pilot Proved", review)
        self.assertIn("Remaining Weaknesses", review)
        self.assertIn("Thirteenth Shelf Choice", review)
        self.assertIn("Choose `published-summary`", review)
        for technique_id in (
            "AOA-T-0003",
            "AOA-T-0007",
            "AOA-T-0032",
            "AOA-T-0006",
            "AOA-T-0008",
            "AOA-T-0010",
            "AOA-T-0011",
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)

        self.assertIn("techniques/proof/published-summary/", review)
        self.assertIn("Do not move `published-summary` from this review alone", review)
        self.assertIn("Do not add `tree_path`", review)
        self.assertIn("Do not treat `published-summary` as proof authority", review)
        self.assertIn("Run a direct-read migration review for `published-summary`", review)
        self.assertIn("landed-evaluation-chain-pilot-review", reviews_index)
        self.assertIn("landed evaluation-chain pilot review: landed", ingress)
        self.assertIn("published-summary` chosen", ingress)
        self.assertIn("Landed evaluation-chain pilot review", landing_log)
        self.assertIn("second successful proof trunk shelf", landing_log)
        self.assertIn("published-summary` direct-read review", distillation_roadmap)
        self.assertIn("published-summary` pilot before choosing", root_roadmap)
        self.assertIn("Landed Evaluation-Chain Pilot Review", tree_contract)
        self.assertIn("chooses `published-summary`", tree_contract)
        self.assertIn(
            "accepted the landed `evaluation-chain` pilot review",
            changelog,
        )

        for old_path, current_path in (
            (
                "techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md",
                "techniques/proof/published-summary/latest-alias-plus-history-copy/TECHNIQUE.md",
            ),
            (
                "techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md",
                "techniques/proof/published-summary/published-summary-remediation-snapshot/TECHNIQUE.md",
            ),
            (
                "techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md",
                "techniques/proof/published-summary/telemetry-integrity-snapshot/TECHNIQUE.md",
            ),
            (
                "techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md",
                "techniques/proof/published-summary/required-vs-optional-source-rendering/TECHNIQUE.md",
            ),
        ):
            with self.subTest(old_path=old_path):
                self.assertFalse((REPO_ROOT / old_path).exists())
                self.assertTrue((REPO_ROOT / current_path).is_file())

        self.assertTrue((REPO_ROOT / "techniques" / "proof" / "published-summary").is_dir())

    def test_published_summary_direct_read_review_accepts_thirteenth_pilot(
        self,
    ) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "published-summary-direct-read-migration-review.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Published-Summary Direct-Read Migration Review", review)
        self.assertIn("accepted-for-thirteenth-migration-pilot", review)
        self.assertIn("not path migration", review)
        self.assertIn("not\n`tree_path` frontmatter", review)
        self.assertIn("Accept `published-summary` as the thirteenth", review)
        self.assertIn("Direct Bundle Read", review)
        self.assertIn("Why The Shelf Holds", review)
        self.assertIn("Proof Trunk Fit", review)
        self.assertIn("Boundary Watch Accepted", review)
        for technique_id in (
            "AOA-T-0006",
            "AOA-T-0008",
            "AOA-T-0010",
            "AOA-T-0011",
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)

        for old_path in (
            "techniques/evaluation/latest-alias-plus-history-copy/",
            "techniques/evaluation/published-summary-remediation-snapshot/",
            "techniques/evaluation/telemetry-integrity-snapshot/",
            "techniques/evaluation/required-vs-optional-source-rendering/",
        ):
            with self.subTest(old_path=old_path):
                self.assertIn(old_path, review)

        self.assertIn("techniques/proof/published-summary/", review)
        self.assertIn("Move exactly these four bundles", review)
        self.assertIn("Do not move files from this review pack alone", review)
        self.assertIn("Do not add `tree_path`", review)
        self.assertIn("Do not treat `published-summary` as telemetry owner doctrine", review)
        self.assertIn("Do not let `AOA-T-0011` become only a package appendix", review)
        self.assertIn("Run the thirteenth pilot migration", review)
        self.assertIn("published-summary-direct-read-migration-review", reviews_index)
        self.assertIn("published-summary direct-read review: landed", ingress)
        self.assertIn("accepted-for-thirteenth-migration-pilot", ingress)
        self.assertIn("Published-summary direct-read migration review", landing_log)
        self.assertIn("proof-facing package", landing_log)
        self.assertIn("accepted-for-thirteenth-migration-pilot", distillation_roadmap)
        self.assertIn("published-summary` pilot before choosing", root_roadmap)
        self.assertIn("Published-Summary Direct-Read Migration Review", tree_contract)
        self.assertIn("AOA-T-0006`, `AOA-T-0008`, `AOA-T-0010`, and `AOA-T-0011", tree_contract)
        self.assertIn(
            "accepted the `published-summary` direct-read migration review",
            changelog,
        )

        for old_path, current_path in (
            (
                "techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md",
                "techniques/proof/published-summary/latest-alias-plus-history-copy/TECHNIQUE.md",
            ),
            (
                "techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md",
                "techniques/proof/published-summary/published-summary-remediation-snapshot/TECHNIQUE.md",
            ),
            (
                "techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md",
                "techniques/proof/published-summary/telemetry-integrity-snapshot/TECHNIQUE.md",
            ),
            (
                "techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md",
                "techniques/proof/published-summary/required-vs-optional-source-rendering/TECHNIQUE.md",
            ),
        ):
            with self.subTest(current_path=current_path):
                self.assertFalse((REPO_ROOT / old_path).exists())
                self.assertTrue((REPO_ROOT / current_path).is_file())

        self.assertTrue((REPO_ROOT / "techniques" / "proof" / "published-summary").is_dir())

    def test_landed_published_summary_review_selects_history_artifacts(self) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "landed-published-summary-pilot-review.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Landed Published-Summary Pilot Review", review)
        self.assertIn("pilot-validated", review)
        self.assertIn("third successful shelf under the `proof` trunk", review)
        self.assertIn("What The Thirteenth Pilot Proved", review)
        self.assertIn("Remaining Weaknesses", review)
        self.assertIn("Fourteenth Shelf Choice", review)
        self.assertIn("Choose `history-artifacts`", review)
        for technique_id in (
            "AOA-T-0006",
            "AOA-T-0008",
            "AOA-T-0010",
            "AOA-T-0011",
            "AOA-T-0044",
            "AOA-T-0053",
            "AOA-T-0026",
            "AOA-T-0045",
            "AOA-T-0066",
            "AOA-T-0067",
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)

        self.assertIn("techniques/proof/published-summary/", review)
        self.assertIn("Do not move `history-artifacts` from this review alone", review)
        self.assertIn("Do not add `tree_path`", review)
        self.assertIn("Do not treat `history-artifacts` as memory doctrine", review)
        self.assertIn("private transcript publication", review)
        self.assertIn("repo\n  analytics", review)
        self.assertIn("Run a direct-read migration review for `history-artifacts`", review)
        self.assertIn("landed-published-summary-pilot-review", reviews_index)
        self.assertIn("landed published-summary pilot review: landed", ingress)
        self.assertIn("history-artifacts` chosen", ingress)
        self.assertIn("Landed published-summary pilot review", landing_log)
        self.assertIn("third successful proof trunk shelf", landing_log)
        self.assertIn("history-artifacts` direct-read review", distillation_roadmap)
        self.assertIn("published-summary` pilot before choosing", root_roadmap)
        self.assertIn("Run the `history-artifacts` direct-read migration review", root_roadmap)
        self.assertIn("Landed Published-Summary Pilot Review", tree_contract)
        self.assertIn("chooses `history-artifacts`", tree_contract)
        self.assertIn(
            "accepted the landed `published-summary` pilot review",
            changelog,
        )

        for old_path, current_path in (
            (
                "techniques/history/versionable-session-transcripts/TECHNIQUE.md",
                "techniques/history/history-artifacts/versionable-session-transcripts/TECHNIQUE.md",
            ),
            (
                "techniques/history/local-first-session-index/TECHNIQUE.md",
                "techniques/history/history-artifacts/local-first-session-index/TECHNIQUE.md",
            ),
            (
                "techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md",
                "techniques/history/history-artifacts/session-capture-as-repo-artifact/TECHNIQUE.md",
            ),
            (
                "techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md",
                "techniques/history/history-artifacts/witness-trace-as-reviewable-artifact/TECHNIQUE.md",
            ),
            (
                "techniques/history/transcript-replay-artifact/TECHNIQUE.md",
                "techniques/history/history-artifacts/transcript-replay-artifact/TECHNIQUE.md",
            ),
            (
                "techniques/history/transcript-linked-code-lineage/TECHNIQUE.md",
                "techniques/history/history-artifacts/transcript-linked-code-lineage/TECHNIQUE.md",
            ),
        ):
            with self.subTest(current_path=current_path):
                self.assertFalse((REPO_ROOT / old_path).exists())
                self.assertTrue((REPO_ROOT / current_path).is_file())

        self.assertTrue((REPO_ROOT / "techniques" / "history" / "history-artifacts").is_dir())

    def test_history_artifacts_direct_read_review_accepts_fourteenth_pilot(
        self,
    ) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "history-artifacts-direct-read-migration-review.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("History-Artifacts Direct-Read Migration Review", review)
        self.assertIn("accepted-for-fourteenth-migration-pilot", review)
        self.assertIn("not path migration", review)
        self.assertIn("not\n`tree_path` frontmatter", review)
        self.assertIn("Accept `history-artifacts` as the fourteenth", review)
        self.assertIn("Direct Bundle Read", review)
        self.assertIn("Why The Shelf Holds", review)
        self.assertIn("Split Decision", review)
        self.assertIn("History Trunk Fit", review)
        self.assertIn("Boundary Watch Accepted", review)
        self.assertIn("Proposed Move", review)
        for technique_id in (
            "AOA-T-0044",
            "AOA-T-0053",
            "AOA-T-0026",
            "AOA-T-0045",
            "AOA-T-0066",
            "AOA-T-0067",
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)

        for current_path in (
            "techniques/history/versionable-session-transcripts/",
            "techniques/history/local-first-session-index/",
            "techniques/history/session-capture-as-repo-artifact/",
            "techniques/history/witness-trace-as-reviewable-artifact/",
            "techniques/history/transcript-replay-artifact/",
            "techniques/history/transcript-linked-code-lineage/",
        ):
            with self.subTest(current_path=current_path):
                self.assertIn(current_path, review)

        self.assertIn("techniques/history/history-artifacts/", review)
        self.assertIn("Move exactly these six bundles", review)
        self.assertIn("Do not move files from this review pack alone", review)
        self.assertIn("Do not add `tree_path`", review)
        self.assertIn("Do not treat `history-artifacts` as memory doctrine", review)
        self.assertIn("hidden capture policy", review)
        self.assertIn("repo analytics", review)
        self.assertIn("Run the fourteenth pilot migration", review)
        self.assertIn("history-artifacts-direct-read-migration-review", reviews_index)
        self.assertIn("history-artifacts direct-read review: landed", ingress)
        self.assertIn("accepted-for-fourteenth-migration-pilot", ingress)
        self.assertIn("History-artifacts direct-read migration review", landing_log)
        self.assertIn("fourteenth bounded migration pilot", landing_log)
        self.assertIn("accepted-for-fourteenth-migration-pilot", distillation_roadmap)
        self.assertIn(
            "Run the `history-artifacts` direct-read migration review",
            root_roadmap,
        )
        self.assertIn("Review the landed `history-artifacts` pilot", root_roadmap)
        self.assertIn("History-Artifacts Direct-Read Migration Review", tree_contract)
        self.assertIn(
            "fourteenth pilot migration moves exactly those six bundles",
            tree_contract,
        )
        self.assertIn(
            "accepted the `history-artifacts` direct-read migration review",
            changelog,
        )

        for current_path, future_path in (
            (
                "techniques/history/versionable-session-transcripts/TECHNIQUE.md",
                "techniques/history/history-artifacts/versionable-session-transcripts/TECHNIQUE.md",
            ),
            (
                "techniques/history/local-first-session-index/TECHNIQUE.md",
                "techniques/history/history-artifacts/local-first-session-index/TECHNIQUE.md",
            ),
            (
                "techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md",
                "techniques/history/history-artifacts/session-capture-as-repo-artifact/TECHNIQUE.md",
            ),
            (
                "techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md",
                "techniques/history/history-artifacts/witness-trace-as-reviewable-artifact/TECHNIQUE.md",
            ),
            (
                "techniques/history/transcript-replay-artifact/TECHNIQUE.md",
                "techniques/history/history-artifacts/transcript-replay-artifact/TECHNIQUE.md",
            ),
            (
                "techniques/history/transcript-linked-code-lineage/TECHNIQUE.md",
                "techniques/history/history-artifacts/transcript-linked-code-lineage/TECHNIQUE.md",
            ),
        ):
            with self.subTest(current_path=current_path):
                self.assertFalse((REPO_ROOT / current_path).exists())
                self.assertTrue((REPO_ROOT / future_path).is_file())

        self.assertTrue((REPO_ROOT / "techniques" / "history" / "history-artifacts").is_dir())

    def test_history_artifacts_tree_pilot_migration_is_recorded(self) -> None:
        history_agents = (
            REPO_ROOT / "techniques" / "history" / "AGENTS.md"
        ).read_text(encoding="utf-8")
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        receipt = (
            REPO_ROOT
            / "legacy"
            / "receipts"
            / "2026-05-05-history-artifacts-tree-pilot.md"
        ).read_text(encoding="utf-8")
        legacy_index = (REPO_ROOT / "legacy" / "INDEX.md").read_text(
            encoding="utf-8"
        )
        receipts_index = (
            REPO_ROOT / "legacy" / "receipts" / "README.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        flat_history_distillation_roadmap = " ".join(distillation_roadmap.split())
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("history-artifacts/", history_agents)
        self.assertIn("memory objects and recall surfaces still stay outside", history_agents)
        self.assertIn("private transcripts", history_agents)
        self.assertIn("transcript-linked-code-lineage", history_agents)
        self.assertIn("history-artifacts migration: landed", ingress)
        self.assertIn("History-Artifacts Tree Pilot Receipt", receipt)
        self.assertIn("They did not pass through root `legacy/`.", receipt)
        self.assertIn("Do not add `tree_path` frontmatter.", receipt)
        self.assertIn("six separate leaf", receipt)
        self.assertIn("generic history platform", receipt)
        self.assertIn("twenty-six receipts", legacy_index)
        self.assertIn("2026-05-05-history-artifacts-tree-pilot.md", legacy_index)
        self.assertIn("twenty-six technique tree pilot receipts", receipts_index)
        self.assertIn("History-artifacts tree pilot migration", landing_log)
        self.assertIn("kept capture, transcript packaging", landing_log)
        self.assertIn(
            "fourteenth pilot migration is now landed",
            flat_history_distillation_roadmap,
        )
        self.assertIn("fourteenth landed pilot moved", root_roadmap)
        self.assertIn("Review the landed `history-artifacts` pilot", root_roadmap)
        self.assertIn("2026-05-05-history-artifacts-tree-pilot", tree_contract)
        self.assertIn("moved `AOA-T-0044`", changelog)

        for technique_id, old_path, new_path in (
            (
                "AOA-T-0044",
                "techniques/history/versionable-session-transcripts/",
                "techniques/history/history-artifacts/versionable-session-transcripts/",
            ),
            (
                "AOA-T-0053",
                "techniques/history/local-first-session-index/",
                "techniques/history/history-artifacts/local-first-session-index/",
            ),
            (
                "AOA-T-0026",
                "techniques/history/session-capture-as-repo-artifact/",
                "techniques/history/history-artifacts/session-capture-as-repo-artifact/",
            ),
            (
                "AOA-T-0045",
                "techniques/history/witness-trace-as-reviewable-artifact/",
                "techniques/history/history-artifacts/witness-trace-as-reviewable-artifact/",
            ),
            (
                "AOA-T-0066",
                "techniques/history/transcript-replay-artifact/",
                "techniques/history/history-artifacts/transcript-replay-artifact/",
            ),
            (
                "AOA-T-0067",
                "techniques/history/transcript-linked-code-lineage/",
                "techniques/history/history-artifacts/transcript-linked-code-lineage/",
            ),
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, receipt)
                self.assertIn(old_path, receipt)
                self.assertIn(new_path, receipt)
                self.assertFalse((REPO_ROOT / old_path).exists())
                self.assertTrue(
                    (REPO_ROOT / new_path / "TECHNIQUE.md").is_file()
                )

    def test_landed_history_artifacts_review_selects_antifragility_recovery(
        self,
    ) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "landed-history-artifacts-pilot-review.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Landed History-Artifacts Pilot Review", review)
        self.assertIn("pilot-validated", review)
        self.assertIn("first successful shelf under the `history` trunk", review)
        self.assertIn("What The Fourteenth Pilot Proved", review)
        self.assertIn("Remaining Weaknesses", review)
        self.assertIn("Fifteenth Shelf Choice", review)
        self.assertIn("Choose `recovery/antifragility-recovery`", review)

        for technique_id in (
            "AOA-T-0044",
            "AOA-T-0053",
            "AOA-T-0026",
            "AOA-T-0045",
            "AOA-T-0066",
            "AOA-T-0067",
            "AOA-T-0097",
            "AOA-T-0099",
            "AOA-T-0100",
            "AOA-T-0098",
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)

        self.assertIn("techniques/history/history-artifacts/", review)
        self.assertIn(
            "Do not move `recovery/antifragility-recovery` from this review alone",
            review,
        )
        self.assertIn("Do not add `tree_path`", review)
        self.assertIn("Do not treat `history-artifacts` as memory doctrine", review)
        self.assertIn(
            "Do not treat `recovery/antifragility-recovery` as incident response",
            review,
        )
        self.assertIn("validation-patterns erasure", review)
        self.assertIn(
            "Run a direct-read migration review for `recovery/antifragility-recovery`",
            review,
        )
        self.assertIn("landed-history-artifacts-pilot-review", reviews_index)
        self.assertIn("landed history-artifacts pilot review: landed", ingress)
        self.assertIn("recovery/antifragility-recovery` chosen", ingress)
        self.assertIn("Landed history-artifacts pilot review", landing_log)
        self.assertIn("first successful history trunk shelf", landing_log)
        self.assertIn("validation-patterns\n  erasure", landing_log)
        self.assertIn(
            "recovery/antifragility-recovery` for the next direct-read",
            distillation_roadmap,
        )
        self.assertIn(
            "history-artifacts` pilot before choosing any fifteenth shelf",
            root_roadmap,
        )
        self.assertIn(
            "Run the `recovery/antifragility-recovery` direct-read migration review",
            root_roadmap,
        )
        self.assertIn("Landed History-Artifacts Pilot Review", tree_contract)
        self.assertIn("chooses\n`recovery/antifragility-recovery`", tree_contract)
        self.assertIn(
            "accepted the landed `history-artifacts` pilot review",
            changelog,
        )

        for current_path, future_path in (
            (
                "techniques/system-recovery/degrade-reground-recover/TECHNIQUE.md",
                "techniques/recovery/antifragility-recovery/degrade-reground-recover/TECHNIQUE.md",
            ),
            (
                "techniques/system-recovery/isolated-service-stop-on-shared-substrate/TECHNIQUE.md",
                "techniques/recovery/antifragility-recovery/isolated-service-stop-on-shared-substrate/TECHNIQUE.md",
            ),
            (
                "techniques/system-recovery/stress-receipt-reground-closeout/TECHNIQUE.md",
                "techniques/recovery/antifragility-recovery/stress-receipt-reground-closeout/TECHNIQUE.md",
            ),
            (
                "techniques/validation-patterns/receipt-first-failure-analysis/TECHNIQUE.md",
                "techniques/recovery/antifragility-recovery/receipt-first-failure-analysis/TECHNIQUE.md",
            ),
        ):
            with self.subTest(current_path=current_path):
                self.assertFalse((REPO_ROOT / current_path).exists())
                self.assertTrue((REPO_ROOT / future_path).is_file())

        self.assertTrue((REPO_ROOT / "techniques" / "history" / "history-artifacts").is_dir())

    def test_antifragility_recovery_direct_read_review_accepts_fifteenth_pilot(
        self,
    ) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "antifragility-recovery-direct-read-migration-review.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Antifragility-Recovery Direct-Read Migration Review", review)
        self.assertIn("accepted-for-fifteenth-migration-pilot", review)
        self.assertIn("not path migration", review)
        self.assertIn("not\n`tree_path` frontmatter", review)
        self.assertIn("Accept `recovery/antifragility-recovery`", review)
        self.assertIn("Direct Bundle Read", review)
        self.assertIn("Why The Shelf Holds", review)
        self.assertIn("Cross-Domain Decision", review)
        self.assertIn("Recovery Trunk Fit", review)
        self.assertIn("Boundary Watch Accepted", review)
        self.assertIn("Proposed Move", review)

        for technique_id in (
            "AOA-T-0097",
            "AOA-T-0099",
            "AOA-T-0100",
            "AOA-T-0098",
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)

        for current_path in (
            "techniques/system-recovery/degrade-reground-recover/",
            "techniques/system-recovery/isolated-service-stop-on-shared-substrate/",
            "techniques/system-recovery/stress-receipt-reground-closeout/",
            "techniques/validation-patterns/receipt-first-failure-analysis/",
        ):
            with self.subTest(current_path=current_path):
                self.assertIn(current_path, review)

        self.assertIn("techniques/recovery/antifragility-recovery/", review)
        self.assertIn("Move exactly these four bundles", review)
        self.assertIn("Do not move files from this review pack alone", review)
        self.assertIn("Do not add `tree_path`", review)
        self.assertIn("Do not change `domain` or `kind`", review)
        self.assertIn("Do not erase `AOA-T-0098` as a validation pattern", review)
        self.assertIn("Run the fifteenth pilot migration", review)
        self.assertIn(
            "antifragility-recovery-direct-read-migration-review",
            reviews_index,
        )
        self.assertIn("antifragility-recovery direct-read review: landed", ingress)
        self.assertIn("accepted-for-fifteenth-migration-pilot", ingress)
        self.assertIn(
            "Antifragility-recovery direct-read migration review",
            landing_log,
        )
        self.assertIn("validation-shaped leaf", landing_log)
        self.assertIn("accepted-for-fifteenth-migration-pilot", distillation_roadmap)
        self.assertIn("AOA-T-0098` as `domain: validation-patterns`", distillation_roadmap)
        self.assertIn(
            "Run the `recovery/antifragility-recovery` direct-read migration review",
            root_roadmap,
        )
        self.assertIn("accepted exactly `AOA-T-0097`", root_roadmap)
        self.assertIn(
            "Antifragility-Recovery Direct-Read Migration Review",
            tree_contract,
        )
        self.assertIn("preserving `AOA-T-0098`", tree_contract)
        self.assertIn(
            "accepted the `antifragility-recovery` direct-read migration review",
            changelog,
        )

        for current_path, future_path in (
            (
                "techniques/system-recovery/degrade-reground-recover/TECHNIQUE.md",
                "techniques/recovery/antifragility-recovery/degrade-reground-recover/TECHNIQUE.md",
            ),
            (
                "techniques/system-recovery/isolated-service-stop-on-shared-substrate/TECHNIQUE.md",
                "techniques/recovery/antifragility-recovery/isolated-service-stop-on-shared-substrate/TECHNIQUE.md",
            ),
            (
                "techniques/system-recovery/stress-receipt-reground-closeout/TECHNIQUE.md",
                "techniques/recovery/antifragility-recovery/stress-receipt-reground-closeout/TECHNIQUE.md",
            ),
            (
                "techniques/validation-patterns/receipt-first-failure-analysis/TECHNIQUE.md",
                "techniques/recovery/antifragility-recovery/receipt-first-failure-analysis/TECHNIQUE.md",
            ),
        ):
            with self.subTest(current_path=current_path):
                self.assertFalse((REPO_ROOT / current_path).exists())
                self.assertTrue((REPO_ROOT / future_path).is_file())

    def test_antifragility_recovery_tree_pilot_migration_is_recorded(self) -> None:
        recovery_agents = (
            REPO_ROOT / "techniques" / "recovery" / "AGENTS.md"
        ).read_text(encoding="utf-8")
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        receipt = (
            REPO_ROOT
            / "legacy"
            / "receipts"
            / "2026-05-05-antifragility-recovery-tree-pilot.md"
        ).read_text(encoding="utf-8")
        legacy_index = (REPO_ROOT / "legacy" / "INDEX.md").read_text(
            encoding="utf-8"
        )
        receipts_index = (
            REPO_ROOT / "legacy" / "receipts" / "README.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("antifragility-recovery/", recovery_agents)
        self.assertIn("validation-shaped leaves", recovery_agents)
        self.assertIn("runtime self-healing", recovery_agents)
        self.assertIn("antifragility-recovery migration: landed", ingress)
        self.assertIn("Antifragility-Recovery Tree Pilot Receipt", receipt)
        self.assertIn("They did not pass through root `legacy/`.", receipt)
        self.assertIn("Preserve `AOA-T-0098` as `domain: validation-patterns`", receipt)
        self.assertIn("Do not add `tree_path` frontmatter.", receipt)
        self.assertIn("four separate leaf bundles", receipt)
        self.assertIn("generic resilience platform", receipt)
        self.assertIn("twenty-six receipts", legacy_index)
        self.assertIn("2026-05-05-antifragility-recovery-tree-pilot.md", legacy_index)
        self.assertIn("twenty-six technique tree pilot receipts", receipts_index)
        self.assertIn("Antifragility-recovery tree pilot migration", landing_log)
        self.assertIn("preserved `AOA-T-0098`", landing_log)
        self.assertIn("fifteenth pilot migration is now landed", distillation_roadmap)
        self.assertIn("fifteenth landed pilot moved", root_roadmap)
        self.assertIn("Review the landed `antifragility-recovery` pilot", root_roadmap)
        self.assertIn("2026-05-05-antifragility-recovery-tree-pilot", tree_contract)
        self.assertIn("review the landed", tree_contract)
        self.assertIn("`antifragility-recovery` pilot", tree_contract)
        self.assertIn("moved `AOA-T-0097`", changelog)

        for technique_id, old_path, new_path in (
            (
                "AOA-T-0097",
                "techniques/system-recovery/degrade-reground-recover/",
                "techniques/recovery/antifragility-recovery/degrade-reground-recover/",
            ),
            (
                "AOA-T-0099",
                "techniques/system-recovery/isolated-service-stop-on-shared-substrate/",
                "techniques/recovery/antifragility-recovery/isolated-service-stop-on-shared-substrate/",
            ),
            (
                "AOA-T-0100",
                "techniques/system-recovery/stress-receipt-reground-closeout/",
                "techniques/recovery/antifragility-recovery/stress-receipt-reground-closeout/",
            ),
            (
                "AOA-T-0098",
                "techniques/validation-patterns/receipt-first-failure-analysis/",
                "techniques/recovery/antifragility-recovery/receipt-first-failure-analysis/",
            ),
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, receipt)
                self.assertIn(old_path, receipt)
                self.assertIn(new_path, receipt)
                self.assertFalse((REPO_ROOT / old_path).exists())
                self.assertTrue(
                    (REPO_ROOT / new_path / "TECHNIQUE.md").is_file()
                )

    def test_landed_antifragility_recovery_review_selects_ready_work_graphs(
        self,
    ) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "landed-antifragility-recovery-pilot-review.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Landed Antifragility-Recovery Pilot Review", review)
        self.assertIn("pilot-validated", review)
        self.assertIn("choose `execution/ready-work-graphs`", review)
        self.assertIn("second successful shelf under the `recovery` trunk", review)
        self.assertIn("AOA-T-0098` remains `domain: validation-patterns`", review)
        self.assertIn("What The Fifteenth Pilot Proved", review)
        self.assertIn("Remaining Weaknesses", review)
        self.assertIn("Sixteenth Shelf Choice", review)
        self.assertIn("Why direct-read first", review)
        self.assertIn("Do not move `execution/ready-work-graphs`", review)
        self.assertIn("do not move any files until that", review)
        self.assertIn("review lands", review)
        self.assertIn("landed-antifragility-recovery-pilot-review", reviews_index)
        self.assertIn("landed antifragility-recovery pilot review: landed", ingress)
        self.assertIn("execution/ready-work-graphs", ingress)
        self.assertIn("Landed antifragility-recovery pilot review", landing_log)
        self.assertIn("second successful recovery trunk", landing_log)
        self.assertIn("shelf after `diagnosis-repair`", landing_log)
        self.assertIn("The landed `antifragility-recovery` pilot review is now complete", distillation_roadmap)
        self.assertIn("Run the `execution/ready-work-graphs` direct-read", root_roadmap)
        self.assertIn("Landed Antifragility-Recovery Pilot Review", tree_contract)
        self.assertIn("chooses `execution/ready-work-graphs`", tree_contract)
        self.assertIn(
            "accepted the landed `antifragility-recovery` pilot review",
            changelog,
        )

        for technique_id, path in (
            (
                "AOA-T-0097",
                "techniques/recovery/antifragility-recovery/degrade-reground-recover/TECHNIQUE.md",
            ),
            (
                "AOA-T-0099",
                "techniques/recovery/antifragility-recovery/isolated-service-stop-on-shared-substrate/TECHNIQUE.md",
            ),
            (
                "AOA-T-0100",
                "techniques/recovery/antifragility-recovery/stress-receipt-reground-closeout/TECHNIQUE.md",
            ),
            (
                "AOA-T-0098",
                "techniques/recovery/antifragility-recovery/receipt-first-failure-analysis/TECHNIQUE.md",
            ),
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)
                self.assertTrue((REPO_ROOT / path).is_file())

        for old_path, current_dir, current_path in (
            (
                "techniques/agent-workflows/dependency-aware-task-graph/",
                "techniques/execution/ready-work-graphs/dependency-aware-task-graph/",
                "techniques/execution/ready-work-graphs/dependency-aware-task-graph/TECHNIQUE.md",
            ),
            (
                "techniques/agent-workflows/ready-work-from-blocker-graph/",
                "techniques/execution/ready-work-graphs/ready-work-from-blocker-graph/",
                "techniques/execution/ready-work-graphs/ready-work-from-blocker-graph/TECHNIQUE.md",
            ),
            (
                "techniques/agent-workflows/requirements-design-tasks-ladder/",
                "techniques/execution/ready-work-graphs/requirements-design-tasks-ladder/",
                "techniques/execution/ready-work-graphs/requirements-design-tasks-ladder/TECHNIQUE.md",
            ),
        ):
            with self.subTest(old_path=old_path):
                self.assertIn(old_path, review)
                self.assertIn(current_dir, review)
                self.assertFalse((REPO_ROOT / old_path).exists())
                self.assertTrue((REPO_ROOT / current_path).is_file())

    def test_ready_work_graphs_direct_read_review_accepts_sixteenth_pilot(
        self,
    ) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "ready-work-graphs-direct-read-migration-review.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Ready-Work-Graphs Direct-Read Migration Review", review)
        self.assertIn("accepted-for-sixteenth-migration-pilot", review)
        self.assertIn("not path migration", review)
        self.assertIn("Accept `execution/ready-work-graphs`", review)
        self.assertIn("Direct Bundle Read", review)
        self.assertIn("Watch Line For `AOA-T-0055`", review)
        self.assertIn("Execution Trunk Fit", review)
        self.assertIn("Boundary Watch Accepted", review)
        self.assertIn("Proposed Move", review)
        self.assertIn("Move exactly these three bundles", review)
        self.assertIn("Do not move files from this review pack alone", review)
        self.assertIn("Do not change `domain` or `kind`", review)
        self.assertIn("Run the sixteenth pilot migration", review)
        self.assertIn(
            "ready-work-graphs-direct-read-migration-review",
            reviews_index,
        )
        self.assertIn("ready-work-graphs direct-read review: landed", ingress)
        self.assertIn("accepted-for-sixteenth-migration-pilot", ingress)
        self.assertIn(
            "Ready-work-graphs direct-read migration review",
            landing_log,
        )
        self.assertIn("AOA-T-0055` as a watch-line readiness ladder", landing_log)
        self.assertIn("accepted-for-sixteenth-migration-pilot", distillation_roadmap)
        self.assertIn("Review the landed `intent-chain` pilot", root_roadmap)
        self.assertIn("Ready-Work-Graphs Direct-Read Migration Review", tree_contract)
        self.assertIn("preserving\n`AOA-T-0055` as a readiness ladder", tree_contract)
        self.assertIn(
            "accepted the `ready-work-graphs` direct-read migration review",
            changelog,
        )

        for technique_id, old_path, current_path in (
            (
                "AOA-T-0049",
                "techniques/agent-workflows/dependency-aware-task-graph/TECHNIQUE.md",
                "techniques/execution/ready-work-graphs/dependency-aware-task-graph/TECHNIQUE.md",
            ),
            (
                "AOA-T-0050",
                "techniques/agent-workflows/ready-work-from-blocker-graph/TECHNIQUE.md",
                "techniques/execution/ready-work-graphs/ready-work-from-blocker-graph/TECHNIQUE.md",
            ),
            (
                "AOA-T-0055",
                "techniques/agent-workflows/requirements-design-tasks-ladder/TECHNIQUE.md",
                "techniques/execution/ready-work-graphs/requirements-design-tasks-ladder/TECHNIQUE.md",
            ),
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)
                self.assertIn(old_path.rsplit("/", 1)[0] + "/", review)
                self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                self.assertFalse((REPO_ROOT / old_path).exists())
                self.assertTrue((REPO_ROOT / current_path).is_file())

    def test_ready_work_graphs_tree_pilot_migration_landed(self) -> None:
        receipt = (
            REPO_ROOT
            / "legacy"
            / "receipts"
            / "2026-05-05-ready-work-graphs-tree-pilot.md"
        ).read_text(encoding="utf-8")
        execution_agents = (
            REPO_ROOT / "techniques" / "execution" / "AGENTS.md"
        ).read_text(encoding="utf-8")
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Ready-Work-Graphs Tree Pilot Receipt", receipt)
        self.assertIn("sixteenth authored path migration", receipt)
        self.assertIn("Preserve `AOA-T-0055` as a readiness ladder", receipt)
        self.assertIn("This is a tree trunk, not a frontmatter domain", execution_agents)
        self.assertIn("ready-work-graphs/", execution_agents)
        self.assertIn("ready-work-graphs migration: landed", ingress)
        self.assertIn("Ready-work-graphs tree pilot migration", landing_log)
        self.assertIn("sixteenth pilot migration is\n   now landed", distillation_roadmap)
        self.assertIn("sixteenth landed pilot moved", root_roadmap)
        self.assertIn("2026-05-05-ready-work-graphs-tree-pilot", tree_contract)
        self.assertIn("moved `AOA-T-0049`", changelog)

        for technique_id, old_path, current_path in (
            (
                "AOA-T-0049",
                "techniques/agent-workflows/dependency-aware-task-graph/",
                "techniques/execution/ready-work-graphs/dependency-aware-task-graph/",
            ),
            (
                "AOA-T-0050",
                "techniques/agent-workflows/ready-work-from-blocker-graph/",
                "techniques/execution/ready-work-graphs/ready-work-from-blocker-graph/",
            ),
            (
                "AOA-T-0055",
                "techniques/agent-workflows/requirements-design-tasks-ladder/",
                "techniques/execution/ready-work-graphs/requirements-design-tasks-ladder/",
            ),
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, receipt)
                self.assertIn(old_path, receipt)
                self.assertIn(current_path, receipt)
                self.assertFalse((REPO_ROOT / old_path).exists())
                self.assertTrue((REPO_ROOT / current_path / "TECHNIQUE.md").is_file())

    def test_landed_ready_work_graphs_review_selects_intent_chain(self) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "landed-ready-work-graphs-pilot-review.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Landed Ready-Work-Graphs Pilot Review", review)
        self.assertIn("pilot-validated", review)
        self.assertIn("choose `execution/intent-chain`", review)
        self.assertIn("first successful shelf under the `execution` trunk", review)
        self.assertIn("AOA-T-0055` remains the shelf watch line", review)
        self.assertIn("What The Sixteenth Pilot Proved", review)
        self.assertIn("Remaining Weaknesses", review)
        self.assertIn("Seventeenth Shelf Choice", review)
        self.assertIn("Why direct-read first", review)
        self.assertIn("Do not move `execution/intent-chain`", review)
        self.assertIn("do not move any\nfiles until that", review)
        self.assertIn("review lands", review)
        self.assertIn("landed-ready-work-graphs-pilot-review", reviews_index)
        self.assertIn("landed ready-work-graphs pilot review: landed", ingress)
        self.assertIn("execution/intent-chain", ingress)
        self.assertIn("Landed ready-work-graphs pilot review", landing_log)
        self.assertIn("first successful execution trunk shelf", landing_log)
        self.assertIn("execution/intent-chain` for the next", landing_log)
        self.assertIn("The landed `ready-work-graphs` pilot review is now complete", distillation_roadmap)
        self.assertIn("Review the landed `intent-chain` pilot", root_roadmap)
        self.assertIn("Landed Ready-Work-Graphs Pilot Review", tree_contract)
        self.assertIn("chooses `execution/intent-chain`", tree_contract)
        self.assertIn(
            "accepted the landed `ready-work-graphs` pilot review",
            changelog,
        )

        for technique_id, path in (
            (
                "AOA-T-0049",
                "techniques/execution/ready-work-graphs/dependency-aware-task-graph/TECHNIQUE.md",
            ),
            (
                "AOA-T-0050",
                "techniques/execution/ready-work-graphs/ready-work-from-blocker-graph/TECHNIQUE.md",
            ),
            (
                "AOA-T-0055",
                "techniques/execution/ready-work-graphs/requirements-design-tasks-ladder/TECHNIQUE.md",
            ),
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)
                self.assertTrue((REPO_ROOT / path).is_file())

        for old_dir, current_dir, current_path in (
            (
                "techniques/agent-workflows/intent-plan-dry-run-contract-chain/",
                "techniques/execution/intent-chain/intent-plan-dry-run-contract-chain/",
                "techniques/execution/intent-chain/intent-plan-dry-run-contract-chain/TECHNIQUE.md",
            ),
            (
                "techniques/agent-workflows/new-intent-rollout-checklist/",
                "techniques/execution/intent-chain/new-intent-rollout-checklist/",
                "techniques/execution/intent-chain/new-intent-rollout-checklist/TECHNIQUE.md",
            ),
        ):
            with self.subTest(old_dir=old_dir):
                self.assertIn(old_dir, review)
                self.assertIn(current_dir, review)
                self.assertIn(current_path, review)
                self.assertFalse((REPO_ROOT / old_dir).exists())
                self.assertTrue((REPO_ROOT / current_path).is_file())

    def test_intent_chain_direct_read_review_accepts_seventeenth_pilot(self) -> None:
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "intent-chain-direct-read-migration-review.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Intent-Chain Direct-Read Migration Review", review)
        self.assertIn("accepted-for-seventeenth-migration-pilot", review)
        self.assertIn("Accept `execution/intent-chain`", review)
        self.assertIn("Move exactly `AOA-T-0004` and `AOA-T-0005`", review)
        self.assertIn("not path migration", review)
        self.assertIn("Direct Bundle Read", review)
        self.assertIn("Why The Earlier Small-Shelf Hold No Longer Blocks", review)
        self.assertIn("Execution Trunk Fit", review)
        self.assertIn("Proposed Move", review)
        self.assertIn("Do not move files from this review pack alone", review)
        self.assertIn("Do not promote `AOA-T-0005` to canonical", review)
        self.assertIn(
            "router ownership, API contract authority,\n  runtime dispatch",
            review,
        )
        self.assertIn("Run the seventeenth migration pilot", review)
        self.assertIn("intent-chain-direct-read-migration-review", reviews_index)
        self.assertIn("intent-chain direct-read review: landed", ingress)
        self.assertIn("accepted-for-seventeenth-migration-pilot", ingress)
        self.assertIn("Intent-chain direct-read migration review", landing_log)
        self.assertIn("AOA-T-0004` as the base artifact-first intent chain", landing_log)
        self.assertIn("AOA-T-0005` as `status: promoted`", landing_log)
        self.assertIn("accepted-for-seventeenth-migration-pilot", distillation_roadmap)
        self.assertIn("Review the landed `intent-chain` pilot", root_roadmap)
        self.assertIn("Intent-Chain Direct-Read Migration Review", tree_contract)
        self.assertIn("preserves `AOA-T-0005` as promoted", tree_contract)
        self.assertIn(
            "accepted the `intent-chain` direct-read migration review",
            changelog,
        )

        for technique_id, old_path, current_path in (
            (
                "AOA-T-0004",
                "techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md",
                "techniques/execution/intent-chain/intent-plan-dry-run-contract-chain/TECHNIQUE.md",
            ),
            (
                "AOA-T-0005",
                "techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md",
                "techniques/execution/intent-chain/new-intent-rollout-checklist/TECHNIQUE.md",
            ),
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)
                self.assertIn(old_path.rsplit("/", 1)[0] + "/", review)
                self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                self.assertFalse((REPO_ROOT / old_path).exists())
                self.assertTrue((REPO_ROOT / current_path).is_file())

    def test_intent_chain_tree_pilot_migration_landed(self) -> None:
        receipt = (
            REPO_ROOT
            / "legacy"
            / "receipts"
            / "2026-05-05-intent-chain-tree-pilot.md"
        ).read_text(encoding="utf-8")
        execution_agents = (
            REPO_ROOT / "techniques" / "execution" / "AGENTS.md"
        ).read_text(encoding="utf-8")
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Intent-Chain Tree Pilot Receipt", receipt)
        self.assertIn("Seventeenth authored path migration", receipt)
        self.assertIn("AOA-T-0005` stayed `promoted`", receipt)
        self.assertIn("intent-chain/", execution_agents)
        self.assertIn("router ownership", execution_agents)
        self.assertIn("API contract\nauthority", execution_agents)
        self.assertIn("intent-chain migration: landed", ingress)
        self.assertIn("Intent-chain tree pilot migration", landing_log)
        self.assertIn("seventeenth pilot migration is now\n   landed", distillation_roadmap)
        self.assertIn("seventeenth pilot without moving files", root_roadmap)
        self.assertIn("Review the landed `intent-chain` pilot", root_roadmap)
        self.assertIn("2026-05-05-intent-chain-tree-pilot", tree_contract)
        self.assertIn("moved `AOA-T-0004`", changelog)

        for technique_id, old_path, current_path in (
            (
                "AOA-T-0004",
                "techniques/agent-workflows/intent-plan-dry-run-contract-chain/",
                "techniques/execution/intent-chain/intent-plan-dry-run-contract-chain/",
            ),
            (
                "AOA-T-0005",
                "techniques/agent-workflows/new-intent-rollout-checklist/",
                "techniques/execution/intent-chain/new-intent-rollout-checklist/",
            ),
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, receipt)
                self.assertIn(old_path, receipt)
                self.assertIn(current_path, receipt)
                self.assertFalse((REPO_ROOT / old_path).exists())
                self.assertTrue((REPO_ROOT / current_path / "TECHNIQUE.md").is_file())

    def test_landed_intent_chain_review_selects_agent_workflows_core(self) -> None:
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "landed-intent-chain-pilot-review.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Landed Intent-Chain Pilot Review", review)
        self.assertIn("second successful shelf under the `execution` trunk", review)
        self.assertIn("`AOA-T-0005` can stay promoted after path migration", review)
        self.assertIn("Choose `execution/agent-workflows-core`", review)
        self.assertIn("current projected five-leaf shelf", review)
        self.assertIn("whether the shell-facing cluster should\nsplit", review)
        self.assertIn("Do not move `execution/agent-workflows-core`", review)
        self.assertIn("landed-intent-chain-pilot-review", reviews_index)
        self.assertIn("landed intent-chain pilot review: landed", ingress)
        self.assertIn("execution/agent-workflows-core", ingress)
        self.assertIn("Landed intent-chain pilot review", landing_log)
        self.assertIn("second successful execution trunk shelf", landing_log)
        self.assertIn("The landed `intent-chain` pilot review is now complete", distillation_roadmap)
        self.assertIn(
            "Run the `execution/agent-workflows-core` direct-read",
            root_roadmap,
        )
        self.assertIn("Landed Intent-Chain Pilot Review", tree_contract)
        self.assertIn("execution/agent-workflows-core", tree_contract)
        self.assertIn(
            "accepted the landed `intent-chain` pilot review",
            changelog,
        )

        for technique_id, old_path, current_path in (
            (
                "AOA-T-0001",
                "techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md",
                "techniques/execution/agent-workflows-core/plan-diff-apply-verify-report/TECHNIQUE.md",
            ),
            (
                "AOA-T-0014",
                "techniques/agent-workflows/tdd-slice/TECHNIQUE.md",
                "techniques/execution/agent-workflows-core/tdd-slice/TECHNIQUE.md",
            ),
            (
                "AOA-T-0023",
                "techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md",
                "techniques/execution/agent-workflows-core/stateless-single-shot-agent/TECHNIQUE.md",
            ),
            (
                "AOA-T-0028",
                "techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md",
                "techniques/execution/agent-workflows-core/confirmation-gated-mutating-action/TECHNIQUE.md",
            ),
            (
                "AOA-T-0031",
                "techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md",
                "techniques/execution/agent-workflows-core/shell-composable-agent-invocation/TECHNIQUE.md",
            ),
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)
                self.assertIn(old_path.rsplit("/", 1)[0] + "/", review)
                self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                self.assertFalse((REPO_ROOT / old_path).exists())
                self.assertTrue((REPO_ROOT / current_path).is_file())

    def test_agent_workflows_core_direct_read_review_accepts_eighteenth_pilot(
        self,
    ) -> None:
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "agent-workflows-core-direct-read-migration-review.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Agent-Workflows-Core Direct-Read Migration Review", review)
        self.assertIn("accepted-for-eighteenth-migration-pilot", review)
        self.assertIn("Accept `execution/agent-workflows-core`", review)
        self.assertIn("visible, bounded, reviewable agent work", review)
        self.assertIn("Do not remap `AOA-T-0028` from `guardrail`", review)
        self.assertIn("Run the eighteenth migration pilot", review)
        self.assertIn("agent-workflows-core-direct-read-migration-review", reviews_index)
        self.assertIn("agent-workflows-core direct-read review: landed", ingress)
        self.assertIn("accepted-for-eighteenth-migration-pilot", ingress)
        self.assertIn("Agent-workflows-core direct-read migration review", landing_log)
        self.assertIn("preserved `AOA-T-0028` as `kind: guardrail`", landing_log)
        self.assertIn("accepted-for-eighteenth-migration-pilot", distillation_roadmap)
        self.assertIn("eighteenth pilot migration moved", root_roadmap)
        self.assertIn("Agent-Workflows-Core Direct-Read Migration Review", tree_contract)
        self.assertIn("preserves\n`AOA-T-0028` as `guardrail`", tree_contract)
        self.assertIn(
            "accepted the `agent-workflows-core` direct-read migration review",
            changelog,
        )

        for technique_id, old_path, current_path in (
            (
                "AOA-T-0001",
                "techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md",
                "techniques/execution/agent-workflows-core/plan-diff-apply-verify-report/TECHNIQUE.md",
            ),
            (
                "AOA-T-0014",
                "techniques/agent-workflows/tdd-slice/TECHNIQUE.md",
                "techniques/execution/agent-workflows-core/tdd-slice/TECHNIQUE.md",
            ),
            (
                "AOA-T-0023",
                "techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md",
                "techniques/execution/agent-workflows-core/stateless-single-shot-agent/TECHNIQUE.md",
            ),
            (
                "AOA-T-0028",
                "techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md",
                "techniques/execution/agent-workflows-core/confirmation-gated-mutating-action/TECHNIQUE.md",
            ),
            (
                "AOA-T-0031",
                "techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md",
                "techniques/execution/agent-workflows-core/shell-composable-agent-invocation/TECHNIQUE.md",
            ),
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)
                self.assertIn(old_path.rsplit("/", 1)[0] + "/", review)
                self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                self.assertFalse((REPO_ROOT / old_path).exists())
                self.assertTrue((REPO_ROOT / current_path).is_file())

    def test_agent_workflows_core_tree_pilot_migration_landed(self) -> None:
        receipt = (
            REPO_ROOT
            / "legacy"
            / "receipts"
            / "2026-05-05-agent-workflows-core-tree-pilot.md"
        ).read_text(encoding="utf-8")
        execution_agents = (
            REPO_ROOT / "techniques" / "execution" / "AGENTS.md"
        ).read_text(encoding="utf-8")
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Agent-Workflows-Core Tree Pilot Receipt", receipt)
        self.assertIn("Eighteenth authored path migration", receipt)
        self.assertIn("AOA-T-0028` stayed `kind: guardrail`", receipt)
        self.assertIn("AOA-T-0031` stayed `kind: composition`", receipt)
        self.assertIn("agent-workflows-core/", execution_agents)
        self.assertIn("generic agent doctrine, shell policy", execution_agents)
        self.assertIn("agent-workflows-core migration: landed", ingress)
        self.assertIn("Agent-workflows-core tree pilot migration", landing_log)
        self.assertIn("eighteenth pilot migration is now\n   landed", distillation_roadmap)
        self.assertIn("eighteenth pilot without moving files", root_roadmap)
        self.assertIn("Review the landed `agent-workflows-core` pilot", root_roadmap)
        self.assertIn("2026-05-05-agent-workflows-core-tree-pilot", tree_contract)
        self.assertIn("moved `AOA-T-0001`", changelog)

        for technique_id, old_path, current_path in (
            (
                "AOA-T-0001",
                "techniques/agent-workflows/plan-diff-apply-verify-report/",
                "techniques/execution/agent-workflows-core/plan-diff-apply-verify-report/",
            ),
            (
                "AOA-T-0014",
                "techniques/agent-workflows/tdd-slice/",
                "techniques/execution/agent-workflows-core/tdd-slice/",
            ),
            (
                "AOA-T-0023",
                "techniques/agent-workflows/stateless-single-shot-agent/",
                "techniques/execution/agent-workflows-core/stateless-single-shot-agent/",
            ),
            (
                "AOA-T-0028",
                "techniques/agent-workflows/confirmation-gated-mutating-action/",
                "techniques/execution/agent-workflows-core/confirmation-gated-mutating-action/",
            ),
            (
                "AOA-T-0031",
                "techniques/agent-workflows/shell-composable-agent-invocation/",
                "techniques/execution/agent-workflows-core/shell-composable-agent-invocation/",
            ),
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, receipt)
                self.assertIn(old_path, receipt)
                self.assertIn(current_path, receipt)
                self.assertFalse((REPO_ROOT / old_path).exists())
                self.assertTrue((REPO_ROOT / current_path / "TECHNIQUE.md").is_file())

    def test_landed_agent_workflows_core_review_selects_donor_harvest(
        self,
    ) -> None:
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "landed-agent-workflows-core-pilot-review.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Landed Agent-Workflows-Core Pilot Review", review)
        self.assertIn("third successful shelf under the `execution` trunk", review)
        self.assertIn("mixed `workflow` / `guardrail` / `composition`", review)
        self.assertIn("Choose `continuity/donor-harvest`", review)
        self.assertIn("Do not move `continuity/donor-harvest`", review)
        self.assertIn("memory authority, playbook quest authority", review)
        self.assertIn(
            "Run a direct-read migration review for `continuity/donor-harvest`",
            review,
        )
        self.assertIn("landed-agent-workflows-core-pilot-review", reviews_index)
        self.assertIn("landed agent-workflows-core pilot review: landed", ingress)
        self.assertIn("continuity/donor-harvest", ingress)
        self.assertIn("Landed agent-workflows-core pilot review", landing_log)
        self.assertIn("third successful execution trunk", landing_log)
        self.assertIn("continuity/donor-harvest` for the next", landing_log)
        self.assertIn("The landed `agent-workflows-core` pilot\n   review", distillation_roadmap)
        self.assertIn(
            "Run the `continuity/donor-harvest` direct-read",
            root_roadmap,
        )
        self.assertIn("Landed Agent-Workflows-Core Pilot Review", tree_contract)
        self.assertIn("chooses `continuity/donor-harvest`", tree_contract)
        self.assertIn(
            "accepted the landed `agent-workflows-core` pilot review",
            changelog,
        )

        for technique_id, current_path, future_path in (
            (
                "AOA-T-0075",
                "techniques/agent-workflows/session-donor-harvest/TECHNIQUE.md",
                "techniques/continuity/donor-harvest/session-donor-harvest/TECHNIQUE.md",
            ),
            (
                "AOA-T-0077",
                "techniques/agent-workflows/harvest-packet-contract/TECHNIQUE.md",
                "techniques/continuity/donor-harvest/harvest-packet-contract/TECHNIQUE.md",
            ),
            (
                "AOA-T-0084",
                "techniques/agent-workflows/progression-evidence-lift/TECHNIQUE.md",
                "techniques/continuity/donor-harvest/progression-evidence-lift/TECHNIQUE.md",
            ),
            (
                "AOA-T-0085",
                "techniques/agent-workflows/multi-axis-quest-overlay/TECHNIQUE.md",
                "techniques/continuity/donor-harvest/multi-axis-quest-overlay/TECHNIQUE.md",
            ),
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)
                self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                self.assertIn(future_path.rsplit("/", 1)[0] + "/", review)
                self.assertFalse((REPO_ROOT / current_path).exists())
                self.assertTrue((REPO_ROOT / future_path).is_file())

    def test_donor_harvest_direct_read_review_accepts_nineteenth_pilot(
        self,
    ) -> None:
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "donor-harvest-direct-read-migration-review.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Donor-Harvest Direct-Read Migration Review", review)
        self.assertIn("accepted-for-nineteenth-migration-pilot", review)
        self.assertIn("Accept `continuity/donor-harvest`", review)
        self.assertIn("Do not move files from this review pack alone", review)
        self.assertIn("memory authority, playbook quest authority", review)
        self.assertIn("Run the nineteenth migration pilot", review)
        self.assertIn("donor-harvest-direct-read-migration-review", reviews_index)
        self.assertIn("donor-harvest direct-read review: landed", ingress)
        self.assertIn("accepted-for-nineteenth-migration-pilot", ingress)
        self.assertIn("Donor-harvest direct-read migration review", landing_log)
        self.assertIn("accepted-for-nineteenth-migration-pilot", distillation_roadmap)
        self.assertIn("nineteenth pilot migration moved", root_roadmap)
        self.assertIn("Donor-Harvest Direct-Read Migration Review", tree_contract)
        self.assertIn(
            "accepted the `donor-harvest` direct-read migration review",
            changelog,
        )

        for technique_id, current_path, future_path in (
            (
                "AOA-T-0075",
                "techniques/agent-workflows/session-donor-harvest/TECHNIQUE.md",
                "techniques/continuity/donor-harvest/session-donor-harvest/TECHNIQUE.md",
            ),
            (
                "AOA-T-0077",
                "techniques/agent-workflows/harvest-packet-contract/TECHNIQUE.md",
                "techniques/continuity/donor-harvest/harvest-packet-contract/TECHNIQUE.md",
            ),
            (
                "AOA-T-0084",
                "techniques/agent-workflows/progression-evidence-lift/TECHNIQUE.md",
                "techniques/continuity/donor-harvest/progression-evidence-lift/TECHNIQUE.md",
            ),
            (
                "AOA-T-0085",
                "techniques/agent-workflows/multi-axis-quest-overlay/TECHNIQUE.md",
                "techniques/continuity/donor-harvest/multi-axis-quest-overlay/TECHNIQUE.md",
            ),
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)
                self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                self.assertIn(future_path.rsplit("/", 1)[0] + "/", review)
                self.assertFalse((REPO_ROOT / current_path).exists())
                self.assertTrue((REPO_ROOT / future_path).is_file())

    def test_donor_harvest_tree_pilot_migration_landed(self) -> None:
        receipt = (
            REPO_ROOT
            / "legacy"
            / "receipts"
            / "2026-05-05-donor-harvest-tree-pilot.md"
        ).read_text(encoding="utf-8")
        continuity_agents = (
            REPO_ROOT / "techniques" / "continuity" / "AGENTS.md"
        ).read_text(encoding="utf-8")
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        legacy_index = (REPO_ROOT / "legacy" / "INDEX.md").read_text(
            encoding="utf-8"
        )
        receipts_index = (
            REPO_ROOT / "legacy" / "receipts" / "README.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Donor-Harvest Tree Pilot Receipt", receipt)
        self.assertIn("Nineteenth authored path migration", receipt)
        self.assertIn("AOA-T-0077` stayed `kind: handoff`", receipt)
        self.assertIn("AOA-T-0075`, `AOA-T-0084`, and `AOA-T-0085` stayed", receipt)
        self.assertIn("donor-harvest/", continuity_agents)
        self.assertIn("without granting memory, playbook, or progression authority", continuity_agents)
        self.assertIn("donor-harvest migration: landed", ingress)
        self.assertIn("Donor-harvest tree pilot migration", landing_log)
        self.assertIn("legacy/receipts/2026-05-05-donor-harvest-tree-pilot.md", landing_log)
        self.assertIn("nineteenth pilot migration is now landed", distillation_roadmap)
        self.assertIn("Review the landed `donor-harvest` pilot", root_roadmap)
        self.assertIn("2026-05-05-donor-harvest-tree-pilot", tree_contract)
        self.assertIn("twenty-six receipts", legacy_index)
        self.assertIn("2026-05-05-donor-harvest-tree-pilot.md", legacy_index)
        self.assertIn("twenty-six technique tree pilot receipts", receipts_index)
        self.assertIn("moved `AOA-T-0075`", changelog)

        for technique_id, old_path, new_path in (
            (
                "AOA-T-0075",
                "techniques/agent-workflows/session-donor-harvest/",
                "techniques/continuity/donor-harvest/session-donor-harvest/",
            ),
            (
                "AOA-T-0077",
                "techniques/agent-workflows/harvest-packet-contract/",
                "techniques/continuity/donor-harvest/harvest-packet-contract/",
            ),
            (
                "AOA-T-0084",
                "techniques/agent-workflows/progression-evidence-lift/",
                "techniques/continuity/donor-harvest/progression-evidence-lift/",
            ),
            (
                "AOA-T-0085",
                "techniques/agent-workflows/multi-axis-quest-overlay/",
                "techniques/continuity/donor-harvest/multi-axis-quest-overlay/",
            ),
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, receipt)
                self.assertIn(old_path, receipt)
                self.assertIn(new_path, receipt)
                self.assertFalse((REPO_ROOT / old_path).exists())
                self.assertTrue((REPO_ROOT / new_path / "TECHNIQUE.md").is_file())

    def test_landed_donor_harvest_review_selects_decision_routing(self) -> None:
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "landed-donor-harvest-pilot-review.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Landed Donor-Harvest Pilot Review", review)
        self.assertIn("third successful shelf under the `continuity` trunk", review)
        self.assertIn("Choose `governance/decision-routing`", review)
        self.assertIn("Do not move `governance/decision-routing`", review)
        self.assertIn("no governance route card was created", landing_log)
        self.assertIn(
            "Run a direct-read migration review for `governance/decision-routing`",
            review,
        )
        self.assertIn("landed-donor-harvest-pilot-review", reviews_index)
        self.assertIn("landed donor-harvest pilot review: landed", ingress)
        self.assertIn("governance/decision-routing", ingress)
        self.assertIn("Landed donor-harvest pilot review", landing_log)
        self.assertIn("third successful continuity trunk", landing_log)
        self.assertIn("The landed\n   `donor-harvest` pilot review", distillation_roadmap)
        self.assertIn("chooses `governance/decision-routing`", root_roadmap)
        self.assertIn("Landed Donor-Harvest Pilot Review", tree_contract)
        self.assertIn("chooses `governance/decision-routing`", tree_contract)
        self.assertIn(
            "accepted the landed `donor-harvest` pilot review",
            changelog,
        )
        self.assertTrue(
            (REPO_ROOT / "techniques" / "governance" / "AGENTS.md").is_file()
        )

        for technique_id, current_path, future_path in (
            (
                "AOA-T-0076",
                "techniques/agent-workflows/owner-layer-triage/TECHNIQUE.md",
                "techniques/governance/decision-routing/owner-layer-triage/TECHNIQUE.md",
            ),
            (
                "AOA-T-0078",
                "techniques/agent-workflows/decision-fork-cards/TECHNIQUE.md",
                "techniques/governance/decision-routing/decision-fork-cards/TECHNIQUE.md",
            ),
            (
                "AOA-T-0079",
                "techniques/agent-workflows/risk-passport-lift/TECHNIQUE.md",
                "techniques/governance/decision-routing/risk-passport-lift/TECHNIQUE.md",
            ),
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)
                self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                self.assertIn(future_path.rsplit("/", 1)[0] + "/", review)
                self.assertFalse((REPO_ROOT / current_path).exists())
                self.assertTrue((REPO_ROOT / future_path).is_file())

    def test_decision_routing_direct_read_review_accepts_twentieth_pilot(
        self,
    ) -> None:
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "decision-routing-direct-read-migration-review.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Decision-Routing Direct-Read Migration Review", review)
        self.assertIn("accepted-for-twentieth-migration-pilot", review)
        self.assertIn("Accept `governance/decision-routing`", review)
        self.assertIn("Do not move files from this review pack alone", review)
        self.assertIn("AoA constitutional authority", review)
        self.assertIn("Run the twentieth migration pilot", review)
        self.assertIn("decision-routing-direct-read-migration-review", reviews_index)
        self.assertIn("decision-routing direct-read review: landed", ingress)
        self.assertIn("accepted-for-twentieth-migration-pilot", ingress)
        self.assertIn("Decision-routing direct-read migration review", landing_log)
        self.assertIn("accepted-for-twentieth-migration-pilot", distillation_roadmap)
        self.assertIn("twentieth pilot without moving files", root_roadmap)
        self.assertIn("Decision-Routing Direct-Read Migration Review", tree_contract)
        self.assertIn(
            "accepted the `decision-routing` direct-read migration review",
            changelog,
        )
        self.assertTrue(
            (REPO_ROOT / "techniques" / "governance" / "AGENTS.md").is_file()
        )

        for technique_id, current_path, future_path in (
            (
                "AOA-T-0076",
                "techniques/agent-workflows/owner-layer-triage/TECHNIQUE.md",
                "techniques/governance/decision-routing/owner-layer-triage/TECHNIQUE.md",
            ),
            (
                "AOA-T-0078",
                "techniques/agent-workflows/decision-fork-cards/TECHNIQUE.md",
                "techniques/governance/decision-routing/decision-fork-cards/TECHNIQUE.md",
            ),
            (
                "AOA-T-0079",
                "techniques/agent-workflows/risk-passport-lift/TECHNIQUE.md",
                "techniques/governance/decision-routing/risk-passport-lift/TECHNIQUE.md",
            ),
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)
                self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                self.assertIn(future_path.rsplit("/", 1)[0] + "/", review)
                self.assertFalse((REPO_ROOT / current_path).exists())
                self.assertTrue((REPO_ROOT / future_path).is_file())

    def test_decision_routing_tree_pilot_migration_landed(self) -> None:
        receipt = (
            REPO_ROOT
            / "legacy"
            / "receipts"
            / "2026-05-05-decision-routing-tree-pilot.md"
        ).read_text(encoding="utf-8")
        governance_agents = (
            REPO_ROOT / "techniques" / "governance" / "AGENTS.md"
        ).read_text(encoding="utf-8")
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        legacy_index = (REPO_ROOT / "legacy" / "INDEX.md").read_text(
            encoding="utf-8"
        )
        receipts_index = (
            REPO_ROOT / "legacy" / "receipts" / "README.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Decision-Routing Tree Pilot Receipt", receipt)
        self.assertIn("Twentieth authored path migration", receipt)
        self.assertIn("`kind` stayed unchanged as `assessment`", receipt)
        self.assertIn("stayed `promoted`", receipt)
        self.assertIn("decision-routing/", governance_agents)
        self.assertIn(
            "Do not turn a governance technique into AoA constitutional authority",
            governance_agents,
        )
        self.assertIn("decision-routing migration: landed", ingress)
        self.assertIn("Decision-routing tree pilot migration", landing_log)
        self.assertIn(
            "legacy/receipts/2026-05-05-decision-routing-tree-pilot.md",
            landing_log,
        )
        self.assertIn(
            "twentieth pilot migration is now landed",
            distillation_roadmap,
        )
        self.assertIn("Review the landed `decision-routing` pilot", root_roadmap)
        self.assertIn("2026-05-05-decision-routing-tree-pilot", tree_contract)
        self.assertIn("twenty-six receipts", legacy_index)
        self.assertIn(
            "2026-05-05-decision-routing-tree-pilot.md",
            legacy_index,
        )
        self.assertIn("twenty-six technique tree pilot receipts", receipts_index)
        self.assertIn("moved `AOA-T-0076`", changelog)

        for technique_id, old_path, new_path in (
            (
                "AOA-T-0076",
                "techniques/agent-workflows/owner-layer-triage/",
                "techniques/governance/decision-routing/owner-layer-triage/",
            ),
            (
                "AOA-T-0078",
                "techniques/agent-workflows/decision-fork-cards/",
                "techniques/governance/decision-routing/decision-fork-cards/",
            ),
            (
                "AOA-T-0079",
                "techniques/agent-workflows/risk-passport-lift/",
                "techniques/governance/decision-routing/risk-passport-lift/",
            ),
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, receipt)
                self.assertIn(old_path, receipt)
                self.assertIn(new_path, receipt)
                self.assertFalse((REPO_ROOT / old_path).exists())
                self.assertTrue((REPO_ROOT / new_path / "TECHNIQUE.md").is_file())

    def test_landed_decision_routing_review_selects_approval_evidence(
        self,
    ) -> None:
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "landed-decision-routing-pilot-review.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Landed Decision-Routing Pilot Review", review)
        self.assertIn(
            "first successful shelf under the `governance` trunk",
            review,
        )
        self.assertIn("Choose `governance/approval-evidence`", review)
        self.assertIn("Do not move `governance/approval-evidence`", review)
        self.assertIn(
            "Run a direct-read migration review for `governance/approval-evidence`",
            review,
        )
        self.assertIn("landed-decision-routing-pilot-review", reviews_index)
        self.assertIn("landed decision-routing pilot review: landed", ingress)
        self.assertIn("governance/approval-evidence", ingress)
        self.assertIn("Landed decision-routing pilot review", landing_log)
        self.assertIn("first successful\n  governance trunk shelf", landing_log)
        self.assertIn("no `governance/approval-evidence` route card", landing_log)
        self.assertIn(
            "landed `decision-routing` review is\n   now complete",
            distillation_roadmap,
        )
        self.assertIn("chooses `governance/approval-evidence`", root_roadmap)
        self.assertIn(
            "Run the `governance/approval-evidence` direct-read",
            root_roadmap,
        )
        self.assertIn("Landed Decision-Routing Pilot Review", tree_contract)
        self.assertIn(
            "directly read `AOA-T-0068` and `AOA-T-0069`",
            tree_contract,
        )
        self.assertIn(
            "accepted the landed `decision-routing` pilot review",
            changelog,
        )
        self.assertTrue(
            (
                REPO_ROOT / "techniques" / "governance" / "approval-evidence"
            ).is_dir()
        )

        for technique_id, current_path, future_path in (
            (
                "AOA-T-0068",
                "techniques/agent-workflows/fail-closed-evidence-gate/TECHNIQUE.md",
                "techniques/governance/approval-evidence/fail-closed-evidence-gate/TECHNIQUE.md",
            ),
            (
                "AOA-T-0069",
                "techniques/agent-workflows/approval-bound-durable-jobs/TECHNIQUE.md",
                "techniques/governance/approval-evidence/approval-bound-durable-jobs/TECHNIQUE.md",
            ),
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)
                self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                self.assertIn(future_path.rsplit("/", 1)[0] + "/", review)
                self.assertFalse((REPO_ROOT / current_path).exists())
                self.assertTrue((REPO_ROOT / future_path).is_file())

    def test_approval_evidence_direct_read_review_accepts_twenty_first_pilot(
        self,
    ) -> None:
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "approval-evidence-direct-read-migration-review.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Approval-Evidence Direct-Read Migration Review", review)
        self.assertIn("accepted-for-twenty-first-migration-pilot", review)
        self.assertIn("Accept `governance/approval-evidence`", review)
        self.assertIn("Do not move files from this review pack alone", review)
        self.assertIn("approval policy", review)
        self.assertIn("Run the twenty-first migration pilot", review)
        self.assertIn("approval-evidence-direct-read-migration-review", reviews_index)
        self.assertIn("approval-evidence direct-read review: landed", ingress)
        self.assertIn("accepted-for-twenty-first-migration-pilot", ingress)
        self.assertIn("Approval-evidence direct-read migration review", landing_log)
        self.assertIn("accepted-for-twenty-first-migration-pilot", distillation_roadmap)
        self.assertIn("twenty-first pilot without moving files", root_roadmap)
        self.assertIn("twenty-first pilot migration moved those two bundles", root_roadmap)
        self.assertIn("Approval-Evidence Direct-Read Migration Review", tree_contract)
        self.assertIn("2026-05-05-approval-evidence-tree-pilot", tree_contract)
        self.assertIn(
            "accepted the `approval-evidence` direct-read migration review",
            changelog,
        )
        self.assertTrue(
            (
                REPO_ROOT / "techniques" / "governance" / "approval-evidence"
            ).is_dir()
        )

        for technique_id, current_path, future_path in (
            (
                "AOA-T-0068",
                "techniques/agent-workflows/fail-closed-evidence-gate/TECHNIQUE.md",
                "techniques/governance/approval-evidence/fail-closed-evidence-gate/TECHNIQUE.md",
            ),
            (
                "AOA-T-0069",
                "techniques/agent-workflows/approval-bound-durable-jobs/TECHNIQUE.md",
                "techniques/governance/approval-evidence/approval-bound-durable-jobs/TECHNIQUE.md",
            ),
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)
                self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                self.assertIn(future_path.rsplit("/", 1)[0] + "/", review)
                self.assertFalse((REPO_ROOT / current_path).exists())
                self.assertTrue((REPO_ROOT / future_path).is_file())

    def test_approval_evidence_tree_pilot_migration_landed(self) -> None:
        receipt = (
            REPO_ROOT
            / "legacy"
            / "receipts"
            / "2026-05-05-approval-evidence-tree-pilot.md"
        ).read_text(encoding="utf-8")
        governance_agents = (
            REPO_ROOT / "techniques" / "governance" / "AGENTS.md"
        ).read_text(encoding="utf-8")
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        legacy_index = (REPO_ROOT / "legacy" / "INDEX.md").read_text(
            encoding="utf-8"
        )
        receipts_index = (
            REPO_ROOT / "legacy" / "receipts" / "README.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Approval-Evidence Tree Pilot Receipt", receipt)
        self.assertIn("Twenty-first authored path migration", receipt)
        self.assertIn("`kind` stayed unchanged as `guardrail`", receipt)
        self.assertIn("`kind` stayed unchanged as `handoff`", receipt)
        self.assertIn("stayed `promoted`", receipt)
        self.assertIn("approval-evidence/", governance_agents)
        self.assertIn("scheduler doctrine", governance_agents)
        self.assertIn("approval-evidence migration: landed", ingress)
        self.assertIn("Approval-evidence tree pilot migration", landing_log)
        self.assertIn(
            "legacy/receipts/2026-05-05-approval-evidence-tree-pilot.md",
            landing_log,
        )
        self.assertIn(
            "twenty-first pilot migration is now landed",
            distillation_roadmap,
        )
        self.assertIn(
            "Review the landed `governance/approval-evidence` pilot",
            root_roadmap,
        )
        self.assertIn("2026-05-05-approval-evidence-tree-pilot", tree_contract)
        self.assertIn("twenty-six receipts", legacy_index)
        self.assertIn(
            "2026-05-05-approval-evidence-tree-pilot.md",
            legacy_index,
        )
        self.assertIn("twenty-six technique tree pilot receipts", receipts_index)
        self.assertIn("moved `AOA-T-0068`", changelog)

        for technique_id, old_path, new_path in (
            (
                "AOA-T-0068",
                "techniques/agent-workflows/fail-closed-evidence-gate/",
                "techniques/governance/approval-evidence/fail-closed-evidence-gate/",
            ),
            (
                "AOA-T-0069",
                "techniques/agent-workflows/approval-bound-durable-jobs/",
                "techniques/governance/approval-evidence/approval-bound-durable-jobs/",
            ),
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, receipt)
                self.assertIn(old_path, receipt)
                self.assertIn(new_path, receipt)
                self.assertFalse((REPO_ROOT / old_path).exists())
                self.assertTrue((REPO_ROOT / new_path / "TECHNIQUE.md").is_file())

    def test_landed_approval_evidence_review_selects_review_evidence(
        self,
    ) -> None:
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "landed-approval-evidence-pilot-review.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Landed Approval-Evidence Pilot Review", review)
        self.assertIn("second successful shelf under the `governance` trunk", review)
        self.assertIn("Choose `proof/review-evidence`", review)
        self.assertIn("Do not move `proof/review-evidence`", review)
        self.assertIn("proof verdict authority", review)
        self.assertIn(
            "Run a direct-read migration review for `proof/review-evidence`",
            review,
        )
        self.assertIn("landed-approval-evidence-pilot-review", reviews_index)
        self.assertIn("landed approval-evidence pilot review: landed", ingress)
        self.assertIn("proof/review-evidence", ingress)
        self.assertIn("Landed approval-evidence pilot review", landing_log)
        self.assertIn("Review-evidence tree pilot migration", landing_log)
        self.assertIn(
            "landed `approval-evidence` review is now complete",
            distillation_roadmap,
        )
        self.assertIn(
            "Review the landed `execution/runtime-truth-lifecycle` pilot",
            root_roadmap,
        )
        self.assertIn("Landed Approval-Evidence Pilot Review", tree_contract)
        self.assertIn(
            "Review-Evidence Direct-Read Migration Review",
            tree_contract,
        )
        self.assertIn(
            "accepted the landed `approval-evidence` pilot review",
            changelog,
        )
        self.assertTrue(
            (
                REPO_ROOT / "techniques" / "proof" / "review-evidence"
            ).is_dir()
        )

        for technique_id, current_path, future_path in (
            (
                "AOA-T-0105",
                "techniques/agent-workflows/single-missing-evidence-request/TECHNIQUE.md",
                "techniques/proof/review-evidence/single-missing-evidence-request/TECHNIQUE.md",
            ),
            (
                "AOA-T-0107",
                "techniques/agent-workflows/single-locus-claim-challenge/TECHNIQUE.md",
                "techniques/proof/review-evidence/single-locus-claim-challenge/TECHNIQUE.md",
            ),
            (
                "AOA-T-0106",
                "techniques/docs/single-scoped-evidence-reference/TECHNIQUE.md",
                "techniques/proof/review-evidence/single-scoped-evidence-reference/TECHNIQUE.md",
            ),
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)
                self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                self.assertIn(future_path.rsplit("/", 1)[0] + "/", review)
                self.assertFalse((REPO_ROOT / current_path).exists())
                self.assertTrue((REPO_ROOT / future_path).is_file())

    def test_review_evidence_direct_read_review_accepts_twenty_second_pilot(
        self,
    ) -> None:
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "review-evidence-direct-read-migration-review.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Review-Evidence Direct-Read Migration Review", review)
        self.assertIn("accepted-for-twenty-second-migration-pilot", review)
        self.assertIn("Accept `proof/review-evidence`", review)
        self.assertIn("Do not move files from this review pack alone", review)
        self.assertIn("proof verdict authority", review)
        self.assertIn("source-truth transfer", review)
        self.assertIn("Run the twenty-second migration pilot", review)
        self.assertIn("review-evidence-direct-read-migration-review", reviews_index)
        self.assertIn("review-evidence direct-read review: landed", ingress)
        self.assertIn("accepted-for-twenty-second-migration-pilot", ingress)
        self.assertIn("Review-evidence direct-read migration review", landing_log)
        self.assertIn("Review-evidence tree pilot migration", landing_log)
        self.assertIn(
            "The `review-evidence` direct-read review is now landed",
            distillation_roadmap,
        )
        self.assertIn(
            "Review the landed `execution/runtime-truth-lifecycle` pilot",
            root_roadmap,
        )
        self.assertIn("Review-Evidence Direct-Read Migration Review", tree_contract)
        self.assertIn("2026-05-05-review-evidence-tree-pilot", tree_contract)
        self.assertIn(
            "twenty-second pilot migration moves exactly those three bundles",
            tree_contract,
        )
        self.assertIn(
            "accepted the `review-evidence` direct-read migration review",
            changelog,
        )
        self.assertTrue(
            (
                REPO_ROOT / "techniques" / "proof" / "review-evidence"
            ).is_dir()
        )

        for technique_id, current_path, future_path in (
            (
                "AOA-T-0107",
                "techniques/agent-workflows/single-locus-claim-challenge/TECHNIQUE.md",
                "techniques/proof/review-evidence/single-locus-claim-challenge/TECHNIQUE.md",
            ),
            (
                "AOA-T-0105",
                "techniques/agent-workflows/single-missing-evidence-request/TECHNIQUE.md",
                "techniques/proof/review-evidence/single-missing-evidence-request/TECHNIQUE.md",
            ),
            (
                "AOA-T-0106",
                "techniques/docs/single-scoped-evidence-reference/TECHNIQUE.md",
                "techniques/proof/review-evidence/single-scoped-evidence-reference/TECHNIQUE.md",
            ),
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)
                self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                self.assertIn(future_path.rsplit("/", 1)[0] + "/", review)
                self.assertFalse((REPO_ROOT / current_path).exists())
                self.assertTrue((REPO_ROOT / future_path).is_file())

    def test_review_evidence_tree_pilot_migration_landed(self) -> None:
        receipt = (
            REPO_ROOT
            / "legacy"
            / "receipts"
            / "2026-05-05-review-evidence-tree-pilot.md"
        ).read_text(encoding="utf-8")
        proof_agents = (REPO_ROOT / "techniques" / "proof" / "AGENTS.md").read_text(
            encoding="utf-8"
        )
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        legacy_index = (REPO_ROOT / "legacy" / "INDEX.md").read_text(
            encoding="utf-8"
        )
        receipts_index = (
            REPO_ROOT / "legacy" / "receipts" / "README.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Review-Evidence Tree Pilot Receipt", receipt)
        self.assertIn("Twenty-second authored path migration", receipt)
        self.assertIn("`kind` stayed unchanged as `guardrail`", receipt)
        self.assertIn("`kind` stayed unchanged as `artifact`", receipt)
        self.assertIn("stayed `promoted`", receipt)
        self.assertIn("review-evidence/", proof_agents)
        self.assertIn("evidence adequacy scoring", proof_agents)
        self.assertIn("review-evidence migration: landed", ingress)
        self.assertIn("Review-evidence tree pilot migration", landing_log)
        self.assertIn(
            "legacy/receipts/2026-05-05-review-evidence-tree-pilot.md",
            landing_log,
        )
        self.assertIn(
            "twenty-second pilot migration is now landed",
            distillation_roadmap,
        )
        self.assertIn(
            "Review the landed `execution/runtime-truth-lifecycle` pilot",
            root_roadmap,
        )
        self.assertIn("2026-05-05-review-evidence-tree-pilot", tree_contract)
        self.assertIn("twenty-six receipts", legacy_index)
        self.assertIn(
            "2026-05-05-review-evidence-tree-pilot.md",
            legacy_index,
        )
        self.assertIn("twenty-six technique tree pilot receipts", receipts_index)
        self.assertIn("moved `AOA-T-0107`", changelog)

        for technique_id, old_path, new_path in (
            (
                "AOA-T-0107",
                "techniques/agent-workflows/single-locus-claim-challenge/",
                "techniques/proof/review-evidence/single-locus-claim-challenge/",
            ),
            (
                "AOA-T-0105",
                "techniques/agent-workflows/single-missing-evidence-request/",
                "techniques/proof/review-evidence/single-missing-evidence-request/",
            ),
            (
                "AOA-T-0106",
                "techniques/docs/single-scoped-evidence-reference/",
                "techniques/proof/review-evidence/single-scoped-evidence-reference/",
            ),
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, receipt)
                self.assertIn(old_path, receipt)
                self.assertIn(new_path, receipt)
                self.assertFalse((REPO_ROOT / old_path).exists())
                self.assertTrue((REPO_ROOT / new_path / "TECHNIQUE.md").is_file())

    def test_landed_review_evidence_pilot_review_selects_runtime_truth_lifecycle(
        self,
    ) -> None:
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "landed-review-evidence-pilot-review.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Landed Review-Evidence Pilot Review", review)
        self.assertIn("fourth successful shelf under the `proof` trunk", review)
        self.assertIn("Choose `execution/runtime-truth-lifecycle`", review)
        self.assertIn("Do not move `execution/runtime-truth-lifecycle`", review)
        self.assertIn("abyss-stack` runtime law", review)
        self.assertIn(
            "Run a direct-read migration review for `execution/runtime-truth-lifecycle`",
            review,
        )
        self.assertIn("landed-review-evidence-pilot-review", reviews_index)
        self.assertIn("landed review-evidence pilot review: landed", ingress)
        self.assertIn("execution/runtime-truth-lifecycle", ingress)
        self.assertIn("Landed review-evidence pilot review", landing_log)
        self.assertIn(
            "landed `review-evidence` review is now complete",
            distillation_roadmap,
        )
        self.assertIn(
            "Review the landed `execution/runtime-truth-lifecycle` pilot",
            root_roadmap,
        )
        self.assertIn("Landed Review-Evidence Pilot Review", tree_contract)
        self.assertIn(
            "execution/runtime-truth-lifecycle",
            tree_contract,
        )
        self.assertIn(
            "accepted the landed `review-evidence` pilot review",
            changelog,
        )

        for technique_id, current_path, future_path in (
            (
                "AOA-T-0036",
                "techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md",
                "techniques/execution/runtime-truth-lifecycle/render-truth-before-startup/TECHNIQUE.md",
            ),
            (
                "AOA-T-0038",
                "techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md",
                "techniques/execution/runtime-truth-lifecycle/one-command-service-lifecycle/TECHNIQUE.md",
            ),
            (
                "AOA-T-0037",
                "techniques/evaluation/contextual-host-doctor/TECHNIQUE.md",
                "techniques/execution/runtime-truth-lifecycle/contextual-host-doctor/TECHNIQUE.md",
            ),
            (
                "AOA-T-0039",
                "techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md",
                "techniques/execution/runtime-truth-lifecycle/baseline-first-additive-profile-benchmarks/TECHNIQUE.md",
            ),
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)
                self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                self.assertIn(future_path.rsplit("/", 1)[0] + "/", review)
                self.assertFalse((REPO_ROOT / current_path).exists())
                self.assertTrue((REPO_ROOT / future_path).is_file())

    def test_runtime_truth_lifecycle_direct_read_review_accepts_twenty_third_pilot(
        self,
    ) -> None:
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "runtime-truth-lifecycle-direct-read-migration-review.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Runtime-Truth-Lifecycle Direct-Read Migration Review", review)
        self.assertIn("accepted-for-twenty-third-migration-pilot", review)
        self.assertIn("Accept `execution/runtime-truth-lifecycle`", review)
        self.assertIn("Do not move files from this review pack alone", review)
        self.assertIn("abyss-stack` runtime law", review)
        self.assertIn("benchmark-suite governance", review)
        self.assertIn("Run the twenty-third migration pilot", review)
        self.assertIn(
            "runtime-truth-lifecycle-direct-read-migration-review",
            reviews_index,
        )
        self.assertIn(
            "runtime-truth-lifecycle direct-read review: landed",
            ingress,
        )
        self.assertIn(
            "accepted-for-twenty-third-migration-pilot",
            ingress,
        )
        self.assertIn(
            "Runtime-truth-lifecycle direct-read migration review",
            landing_log,
        )
        self.assertIn(
            "`runtime-truth-lifecycle`\n   direct-read review is now landed",
            distillation_roadmap,
        )
        self.assertIn(
            "Review the landed `execution/runtime-truth-lifecycle` pilot",
            root_roadmap,
        )
        self.assertIn(
            "Runtime-Truth-Lifecycle Direct-Read Migration Review",
            tree_contract,
        )
        self.assertIn(
            "twenty-third pilot migration moves exactly those four bundles",
            tree_contract,
        )
        self.assertIn(
            "accepted the `runtime-truth-lifecycle` direct-read migration review",
            changelog,
        )

        for technique_id, current_path, future_path in (
            (
                "AOA-T-0036",
                "techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md",
                "techniques/execution/runtime-truth-lifecycle/render-truth-before-startup/TECHNIQUE.md",
            ),
            (
                "AOA-T-0038",
                "techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md",
                "techniques/execution/runtime-truth-lifecycle/one-command-service-lifecycle/TECHNIQUE.md",
            ),
            (
                "AOA-T-0037",
                "techniques/evaluation/contextual-host-doctor/TECHNIQUE.md",
                "techniques/execution/runtime-truth-lifecycle/contextual-host-doctor/TECHNIQUE.md",
            ),
            (
                "AOA-T-0039",
                "techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md",
                "techniques/execution/runtime-truth-lifecycle/baseline-first-additive-profile-benchmarks/TECHNIQUE.md",
            ),
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)
                self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                self.assertIn(future_path.rsplit("/", 1)[0] + "/", review)
                self.assertFalse((REPO_ROOT / current_path).exists())
                self.assertTrue((REPO_ROOT / future_path).is_file())

    def test_runtime_truth_lifecycle_tree_pilot_migration_landed(self) -> None:
        receipt = (
            REPO_ROOT
            / "legacy"
            / "receipts"
            / "2026-05-05-runtime-truth-lifecycle-tree-pilot.md"
        ).read_text(encoding="utf-8")
        execution_agents = (
            REPO_ROOT / "techniques" / "execution" / "AGENTS.md"
        ).read_text(encoding="utf-8")
        agent_workflows_agents = (
            REPO_ROOT / "techniques" / "agent-workflows" / "AGENTS.md"
        ).read_text(encoding="utf-8")
        evaluation_agents = (
            REPO_ROOT / "techniques" / "evaluation" / "AGENTS.md"
        ).read_text(encoding="utf-8")
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        legacy_index = (REPO_ROOT / "legacy" / "INDEX.md").read_text(
            encoding="utf-8"
        )
        receipts_index = (
            REPO_ROOT / "legacy" / "receipts" / "README.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Runtime-Truth-Lifecycle Tree Pilot Receipt", receipt)
        self.assertIn("Twenty-third authored path migration", receipt)
        self.assertIn("`kind` stayed unchanged as `composition`", receipt)
        self.assertIn("`kind` stayed unchanged as `workflow`", receipt)
        self.assertIn("`kind` stayed unchanged as `validation`", receipt)
        self.assertIn("runtime-truth-lifecycle/", execution_agents)
        self.assertIn("benchmark-suite governance", execution_agents)
        self.assertNotIn("render-truth-before-startup", agent_workflows_agents)
        self.assertNotIn("one-command-service-lifecycle", agent_workflows_agents)
        self.assertIn("No active leaf bundles currently live directly here", evaluation_agents)
        self.assertIn("runtime-truth-lifecycle migration: landed", ingress)
        self.assertIn("Runtime-truth-lifecycle tree pilot migration", landing_log)
        self.assertIn(
            "2026-05-05-runtime-truth-lifecycle-tree-pilot",
            landing_log,
        )
        self.assertIn(
            "twenty-third pilot\n   migration is now landed",
            distillation_roadmap,
        )
        self.assertIn(
            "Review the landed `execution/runtime-truth-lifecycle` pilot",
            root_roadmap,
        )
        self.assertIn(
            "2026-05-05-runtime-truth-lifecycle-tree-pilot",
            tree_contract,
        )
        self.assertIn("twenty-six receipts", legacy_index)
        self.assertIn(
            "2026-05-05-runtime-truth-lifecycle-tree-pilot.md",
            legacy_index,
        )
        self.assertIn("twenty-six technique tree pilot receipts", receipts_index)
        self.assertIn("moved `AOA-T-0036`", changelog)

        for technique_id, old_path, new_path in (
            (
                "AOA-T-0036",
                "techniques/agent-workflows/render-truth-before-startup/",
                "techniques/execution/runtime-truth-lifecycle/render-truth-before-startup/",
            ),
            (
                "AOA-T-0038",
                "techniques/agent-workflows/one-command-service-lifecycle/",
                "techniques/execution/runtime-truth-lifecycle/one-command-service-lifecycle/",
            ),
            (
                "AOA-T-0037",
                "techniques/evaluation/contextual-host-doctor/",
                "techniques/execution/runtime-truth-lifecycle/contextual-host-doctor/",
            ),
            (
                "AOA-T-0039",
                "techniques/evaluation/baseline-first-additive-profile-benchmarks/",
                "techniques/execution/runtime-truth-lifecycle/baseline-first-additive-profile-benchmarks/",
            ),
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, receipt)
                self.assertIn(old_path, receipt)
                self.assertIn(new_path, receipt)
                self.assertFalse((REPO_ROOT / old_path).exists())
                self.assertTrue((REPO_ROOT / new_path / "TECHNIQUE.md").is_file())

    def test_landed_runtime_truth_lifecycle_pilot_review_selects_owner_truth_closeout(
        self,
    ) -> None:
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "landed-runtime-truth-lifecycle-pilot-review.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Landed Runtime-Truth-Lifecycle Pilot Review", review)
        self.assertIn("fourth successful shelf under the `execution` trunk", review)
        self.assertIn("Choose `proof/owner-truth-closeout`", review)
        self.assertIn("Do not move `proof/owner-truth-closeout`", review)
        self.assertIn("root `AGENTS.md` law", review)
        self.assertIn(
            "Run a direct-read migration review for `proof/owner-truth-closeout`",
            review,
        )
        self.assertIn("landed-runtime-truth-lifecycle-pilot-review", reviews_index)
        self.assertIn(
            "landed runtime-truth-lifecycle pilot review: landed",
            ingress,
        )
        self.assertIn("proof/owner-truth-closeout", ingress)
        self.assertIn("Landed runtime-truth-lifecycle pilot review", landing_log)
        self.assertIn(
            "landed `runtime-truth-lifecycle`\n   pilot review is now complete",
            distillation_roadmap,
        )
        self.assertIn(
            "Run the `proof/owner-truth-closeout` direct-read migration review",
            root_roadmap,
        )
        self.assertIn(
            "Landed Runtime-Truth-Lifecycle Pilot Review",
            tree_contract,
        )
        self.assertIn("proof/owner-truth-closeout", tree_contract)
        self.assertIn(
            "accepted the landed `runtime-truth-lifecycle` pilot review",
            changelog,
        )

        for technique_id, current_path, future_path in (
            (
                "AOA-T-0091",
                "techniques/agent-workflows/workspace-root-ingress-and-mutation-gate/TECHNIQUE.md",
                "techniques/proof/owner-truth-closeout/workspace-root-ingress-and-mutation-gate/TECHNIQUE.md",
            ),
            (
                "AOA-T-0092",
                "techniques/agent-workflows/audit-to-closeout-proof-loop/TECHNIQUE.md",
                "techniques/proof/owner-truth-closeout/audit-to-closeout-proof-loop/TECHNIQUE.md",
            ),
            (
                "AOA-T-0095",
                "techniques/agent-workflows/github-only-owner-endcap-with-reality-sync/TECHNIQUE.md",
                "techniques/proof/owner-truth-closeout/github-only-owner-endcap-with-reality-sync/TECHNIQUE.md",
            ),
            (
                "AOA-T-0096",
                "techniques/agent-workflows/pinned-validation-matrix-before-generated-publish/TECHNIQUE.md",
                "techniques/proof/owner-truth-closeout/pinned-validation-matrix-before-generated-publish/TECHNIQUE.md",
            ),
            (
                "AOA-T-0094",
                "techniques/docs/canonical-owner-with-validated-mirror/TECHNIQUE.md",
                "techniques/proof/owner-truth-closeout/canonical-owner-with-validated-mirror/TECHNIQUE.md",
            ),
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)
                self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                self.assertIn(future_path.rsplit("/", 1)[0] + "/", review)
                self.assertFalse((REPO_ROOT / current_path).exists())
                self.assertTrue((REPO_ROOT / future_path).is_file())

    def test_owner_truth_closeout_direct_read_review_accepts_twenty_fourth_pilot(
        self,
    ) -> None:
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "owner-truth-closeout-direct-read-migration-review.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Owner-Truth-Closeout Direct-Read Migration Review", review)
        self.assertIn("accepted-for-twenty-fourth-migration-pilot", review)
        self.assertIn("Accept `proof/owner-truth-closeout`", review)
        self.assertIn("Do not move files from this review pack alone", review)
        self.assertIn("root `AGENTS.md` law", review)
        self.assertIn("public-share approval policy", review)
        self.assertIn("Run the twenty-fourth migration pilot", review)
        self.assertIn(
            "owner-truth-closeout-direct-read-migration-review",
            reviews_index,
        )
        self.assertIn("owner-truth-closeout direct-read review: landed", ingress)
        self.assertIn("accepted-for-twenty-fourth-migration-pilot", ingress)
        self.assertIn(
            "Owner-truth-closeout direct-read migration review",
            landing_log,
        )
        self.assertIn(
            "The owner-truth-closeout direct-read review is now\n   landed",
            distillation_roadmap,
        )
        self.assertIn(
            "Migrate exactly `AOA-T-0091`, `AOA-T-0092`, `AOA-T-0095`, "
            "`AOA-T-0096`, and `AOA-T-0094` into "
            "`techniques/proof/owner-truth-closeout/`",
            root_roadmap,
        )
        self.assertIn(
            "Owner-Truth-Closeout Direct-Read Migration Review",
            tree_contract,
        )
        self.assertIn(
            "twenty-fourth pilot migration moves exactly those five bundles",
            tree_contract,
        )
        self.assertIn(
            "accepted the `owner-truth-closeout` direct-read migration review",
            changelog,
        )

        for technique_id, current_path, future_path in (
            (
                "AOA-T-0091",
                "techniques/agent-workflows/workspace-root-ingress-and-mutation-gate/TECHNIQUE.md",
                "techniques/proof/owner-truth-closeout/workspace-root-ingress-and-mutation-gate/TECHNIQUE.md",
            ),
            (
                "AOA-T-0092",
                "techniques/agent-workflows/audit-to-closeout-proof-loop/TECHNIQUE.md",
                "techniques/proof/owner-truth-closeout/audit-to-closeout-proof-loop/TECHNIQUE.md",
            ),
            (
                "AOA-T-0095",
                "techniques/agent-workflows/github-only-owner-endcap-with-reality-sync/TECHNIQUE.md",
                "techniques/proof/owner-truth-closeout/github-only-owner-endcap-with-reality-sync/TECHNIQUE.md",
            ),
            (
                "AOA-T-0096",
                "techniques/agent-workflows/pinned-validation-matrix-before-generated-publish/TECHNIQUE.md",
                "techniques/proof/owner-truth-closeout/pinned-validation-matrix-before-generated-publish/TECHNIQUE.md",
            ),
            (
                "AOA-T-0094",
                "techniques/docs/canonical-owner-with-validated-mirror/TECHNIQUE.md",
                "techniques/proof/owner-truth-closeout/canonical-owner-with-validated-mirror/TECHNIQUE.md",
            ),
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)
                self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                self.assertIn(future_path.rsplit("/", 1)[0] + "/", review)
                self.assertFalse((REPO_ROOT / current_path).exists())
                self.assertTrue((REPO_ROOT / future_path).is_file())

    def test_owner_truth_closeout_tree_pilot_migration_landed(self) -> None:
        receipt = (
            REPO_ROOT
            / "legacy"
            / "receipts"
            / "2026-05-05-owner-truth-closeout-tree-pilot.md"
        ).read_text(encoding="utf-8")
        proof_agents = (REPO_ROOT / "techniques" / "proof" / "AGENTS.md").read_text(
            encoding="utf-8"
        )
        agent_workflows_agents = (
            REPO_ROOT / "techniques" / "agent-workflows" / "AGENTS.md"
        ).read_text(encoding="utf-8")
        docs_agents = (REPO_ROOT / "techniques" / "docs" / "AGENTS.md").read_text(
            encoding="utf-8"
        )
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        legacy_index = (REPO_ROOT / "legacy" / "INDEX.md").read_text(
            encoding="utf-8"
        )
        receipts_index = (
            REPO_ROOT / "legacy" / "receipts" / "README.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Owner-Truth-Closeout Tree Pilot Receipt", receipt)
        self.assertIn("Twenty-fourth authored path migration", receipt)
        self.assertIn("`domain` stayed unchanged as `agent-workflows`", receipt)
        self.assertIn("`domain` stayed unchanged as `docs`", receipt)
        self.assertIn("`kind` stayed unchanged as `guardrail`", receipt)
        self.assertIn("`kind` stayed unchanged as `workflow`", receipt)
        self.assertIn("`kind` stayed unchanged as `validation`", receipt)
        self.assertIn("`kind` stayed unchanged as `distribution`", receipt)
        self.assertIn("owner-truth-closeout/", proof_agents)
        self.assertIn("public-share approval policy", proof_agents)
        self.assertNotIn("workspace-root-ingress-and-mutation-gate", agent_workflows_agents)
        self.assertIn("No active leaf bundles currently live directly here", docs_agents)
        self.assertIn("owner-truth-closeout migration: landed", ingress)
        self.assertIn("Owner-truth-closeout tree pilot migration", landing_log)
        self.assertIn(
            "2026-05-05-owner-truth-closeout-tree-pilot",
            landing_log,
        )
        self.assertIn(
            "twenty-fourth\n   pilot migration is now landed",
            distillation_roadmap,
        )
        self.assertIn(
            "Review the landed `proof/owner-truth-closeout` pilot",
            root_roadmap,
        )
        self.assertIn(
            "2026-05-05-owner-truth-closeout-tree-pilot",
            tree_contract,
        )
        self.assertIn("twenty-six receipts", legacy_index)
        self.assertIn(
            "2026-05-05-owner-truth-closeout-tree-pilot.md",
            legacy_index,
        )
        self.assertIn("twenty-six technique tree pilot receipts", receipts_index)
        self.assertIn("moved `AOA-T-0091`", changelog)

        for technique_id, old_path, new_path in (
            (
                "AOA-T-0091",
                "techniques/agent-workflows/workspace-root-ingress-and-mutation-gate/",
                "techniques/proof/owner-truth-closeout/workspace-root-ingress-and-mutation-gate/",
            ),
            (
                "AOA-T-0092",
                "techniques/agent-workflows/audit-to-closeout-proof-loop/",
                "techniques/proof/owner-truth-closeout/audit-to-closeout-proof-loop/",
            ),
            (
                "AOA-T-0095",
                "techniques/agent-workflows/github-only-owner-endcap-with-reality-sync/",
                "techniques/proof/owner-truth-closeout/github-only-owner-endcap-with-reality-sync/",
            ),
            (
                "AOA-T-0096",
                "techniques/agent-workflows/pinned-validation-matrix-before-generated-publish/",
                "techniques/proof/owner-truth-closeout/pinned-validation-matrix-before-generated-publish/",
            ),
            (
                "AOA-T-0094",
                "techniques/docs/canonical-owner-with-validated-mirror/",
                "techniques/proof/owner-truth-closeout/canonical-owner-with-validated-mirror/",
            ),
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, receipt)
                self.assertIn(old_path, receipt)
                self.assertIn(new_path, receipt)
                self.assertFalse((REPO_ROOT / old_path).exists())
                self.assertTrue((REPO_ROOT / new_path / "TECHNIQUE.md").is_file())

    def test_landed_owner_truth_closeout_pilot_review_selects_automation_governance(
        self,
    ) -> None:
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "landed-owner-truth-closeout-pilot-review.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Landed Owner-Truth-Closeout Pilot Review", review)
        self.assertIn("fifth successful shelf under the `proof` trunk", review)
        self.assertIn("Choose `governance/automation-governance`", review)
        self.assertIn("direct-read split review", review)
        self.assertIn("Do not move `governance/automation-governance`", review)
        self.assertIn("split-review-needed", review)
        self.assertIn("skill acceptance", review)
        self.assertIn(
            "Run a direct-read split review for `governance/automation-governance`",
            review,
        )
        self.assertIn(
            "landed-owner-truth-closeout-pilot-review",
            reviews_index,
        )
        self.assertIn(
            "landed owner-truth-closeout pilot review: landed",
            ingress,
        )
        self.assertIn("governance/automation-governance", ingress)
        self.assertIn("Landed owner-truth-closeout pilot review", landing_log)
        self.assertIn(
            "landed `owner-truth-closeout` pilot\n   review is now complete",
            distillation_roadmap,
        )
        self.assertIn(
            "Run the `governance/automation-governance` direct-read split review",
            root_roadmap,
        )
        self.assertIn(
            "Owner-Truth-Closeout Pilot Review",
            tree_contract,
        )
        self.assertIn(
            "nine\nprojected automation-governance leaves",
            tree_contract,
        )
        self.assertIn(
            "accepted the landed `owner-truth-closeout` pilot review",
            changelog,
        )

        for technique_id, current_path, future_path, current_exists, future_exists in (
            (
                "AOA-T-0086",
                "techniques/agent-workflows/automation-fit-matrix/TECHNIQUE.md",
                "techniques/governance/automation-governance/automation-fit-matrix/TECHNIQUE.md",
                False,
                False,
            ),
            (
                "AOA-T-0087",
                "techniques/agent-workflows/human-loop-to-seed-lift/TECHNIQUE.md",
                "techniques/governance/automation-governance/human-loop-to-seed-lift/TECHNIQUE.md",
                False,
                False,
            ),
            (
                "AOA-T-0088",
                "techniques/agent-workflows/approval-sensitivity-check/TECHNIQUE.md",
                "techniques/governance/automation-governance/approval-sensitivity-check/TECHNIQUE.md",
                False,
                False,
            ),
            (
                "AOA-T-0089",
                "techniques/agent-workflows/quest-unit-promotion-review/TECHNIQUE.md",
                "techniques/governance/automation-governance/quest-unit-promotion-review/TECHNIQUE.md",
                False,
                False,
            ),
            (
                "AOA-T-0090",
                "techniques/agent-workflows/nearest-wrong-target-rejection/TECHNIQUE.md",
                "techniques/governance/automation-governance/nearest-wrong-target-rejection/TECHNIQUE.md",
                False,
                False,
            ),
            (
                "AOA-T-0101",
                "techniques/agent-workflows/local-pattern-adoption-gate/TECHNIQUE.md",
                "techniques/governance/automation-governance/local-pattern-adoption-gate/TECHNIQUE.md",
                True,
                False,
            ),
            (
                "AOA-T-0102",
                "techniques/agent-workflows/skill-proposal-handoff-packet/TECHNIQUE.md",
                "techniques/governance/automation-governance/skill-proposal-handoff-packet/TECHNIQUE.md",
                False,
                False,
            ),
            (
                "AOA-T-0103",
                "techniques/agent-workflows/adopted-practice-retention-review/TECHNIQUE.md",
                "techniques/governance/automation-governance/adopted-practice-retention-review/TECHNIQUE.md",
                True,
                False,
            ),
            (
                "AOA-T-0104",
                "techniques/agent-workflows/superseded-practice-obsolescence-route/TECHNIQUE.md",
                "techniques/governance/automation-governance/superseded-practice-obsolescence-route/TECHNIQUE.md",
                True,
                False,
            ),
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)
                self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                self.assertIn(future_path.rsplit("/", 1)[0] + "/", review)
                self.assertEqual(current_exists, (REPO_ROOT / current_path).is_file())
                self.assertEqual(future_exists, (REPO_ROOT / future_path).is_file())

    def test_automation_governance_direct_read_split_review_rejects_bulk_shelf(
        self,
    ) -> None:
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "automation-governance-direct-read-split-review.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Automation-Governance Direct-Read Split Review", review)
        self.assertIn("split-required-before-migration", review)
        self.assertIn(
            "Reject `governance/automation-governance` as one bulk migration shelf",
            review,
        )
        self.assertIn("governance/automation-readiness", review)
        self.assertIn("governance/promotion-boundary", review)
        self.assertIn("governance/practice-adoption-lifecycle", review)
        self.assertIn("Do not move any `automation-governance` bundle", review)
        self.assertIn("Run a split-expansion closeout", review)
        self.assertIn(
            "automation-governance-direct-read-split-review",
            reviews_index,
        )
        self.assertIn(
            "automation-governance direct-read split review: landed",
            ingress,
        )
        self.assertIn("split-required-before-migration", ingress)
        self.assertIn(
            "Automation-governance direct-read split review",
            landing_log,
        )
        self.assertIn(
            "automation-governance\n   direct-read split review is now landed",
            distillation_roadmap,
        )
        self.assertIn(
            "Run the automation-governance split-expansion closeout",
            root_roadmap,
        )
        self.assertIn(
            "Automation-Governance Direct-Read Split Review",
            tree_contract,
        )
        self.assertIn(
            "rejected one bulk `governance/automation-governance` shelf",
            changelog,
        )

        for technique_id, current_path, future_path, current_exists, future_exists in (
            (
                "AOA-T-0086",
                "techniques/agent-workflows/automation-fit-matrix/TECHNIQUE.md",
                "techniques/governance/automation-readiness/automation-fit-matrix/TECHNIQUE.md",
                False,
                True,
            ),
            (
                "AOA-T-0087",
                "techniques/agent-workflows/human-loop-to-seed-lift/TECHNIQUE.md",
                "techniques/governance/automation-readiness/human-loop-to-seed-lift/TECHNIQUE.md",
                False,
                True,
            ),
            (
                "AOA-T-0088",
                "techniques/agent-workflows/approval-sensitivity-check/TECHNIQUE.md",
                "techniques/governance/automation-readiness/approval-sensitivity-check/TECHNIQUE.md",
                False,
                True,
            ),
            (
                "AOA-T-0089",
                "techniques/agent-workflows/quest-unit-promotion-review/TECHNIQUE.md",
                "techniques/governance/promotion-boundary/quest-unit-promotion-review/TECHNIQUE.md",
                False,
                True,
            ),
            (
                "AOA-T-0090",
                "techniques/agent-workflows/nearest-wrong-target-rejection/TECHNIQUE.md",
                "techniques/governance/promotion-boundary/nearest-wrong-target-rejection/TECHNIQUE.md",
                False,
                True,
            ),
            (
                "AOA-T-0102",
                "techniques/agent-workflows/skill-proposal-handoff-packet/TECHNIQUE.md",
                "techniques/governance/promotion-boundary/skill-proposal-handoff-packet/TECHNIQUE.md",
                False,
                True,
            ),
            (
                "AOA-T-0101",
                "techniques/agent-workflows/local-pattern-adoption-gate/TECHNIQUE.md",
                "techniques/governance/practice-adoption-lifecycle/local-pattern-adoption-gate/TECHNIQUE.md",
                True,
                False,
            ),
            (
                "AOA-T-0103",
                "techniques/agent-workflows/adopted-practice-retention-review/TECHNIQUE.md",
                "techniques/governance/practice-adoption-lifecycle/adopted-practice-retention-review/TECHNIQUE.md",
                True,
                False,
            ),
            (
                "AOA-T-0104",
                "techniques/agent-workflows/superseded-practice-obsolescence-route/TECHNIQUE.md",
                "techniques/governance/practice-adoption-lifecycle/superseded-practice-obsolescence-route/TECHNIQUE.md",
                True,
                False,
            ),
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)
                self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                self.assertIn(future_path.rsplit("/", 1)[0] + "/", review)
                self.assertEqual(current_exists, (REPO_ROOT / current_path).is_file())
                self.assertEqual(future_exists, (REPO_ROOT / future_path).is_file())

    def test_automation_governance_split_expansion_closeout_activates_candidate_a(
        self,
    ) -> None:
        closeout = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "automation-governance-split-expansion-closeout.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Automation-Governance Split Expansion Closeout", closeout)
        self.assertIn("split-expanded", closeout)
        self.assertIn("no path migration", closeout)
        self.assertIn("Candidate A", closeout)
        self.assertIn("governance/automation-readiness", closeout)
        self.assertIn("governance/promotion-boundary", closeout)
        self.assertIn("governance/practice-adoption-lifecycle", closeout)
        self.assertIn("Do not move files from this closeout", closeout)
        self.assertIn(
            "Run a direct-read review for Candidate A",
            closeout,
        )
        self.assertIn(
            "automation-governance-split-expansion-closeout",
            reviews_index,
        )
        self.assertIn(
            "automation-governance split expansion closeout: landed",
            ingress,
        )
        self.assertIn("split-expanded", ingress)
        self.assertIn(
            "Automation-governance split expansion closeout",
            landing_log,
        )
        self.assertIn(
            "automation-governance split\n   expansion closeout is now landed",
            distillation_roadmap,
        )
        self.assertIn(
            "Run the `governance/automation-readiness` direct-read review",
            root_roadmap,
        )
        self.assertIn(
            "Automation-Governance Split Expansion Closeout",
            tree_contract,
        )
        self.assertIn(
            "landed the automation-governance split expansion closeout",
            changelog,
        )

        for current_path, future_path in (
            (
                "techniques/agent-workflows/automation-fit-matrix/TECHNIQUE.md",
                "techniques/governance/automation-readiness/automation-fit-matrix/TECHNIQUE.md",
            ),
            (
                "techniques/agent-workflows/human-loop-to-seed-lift/TECHNIQUE.md",
                "techniques/governance/automation-readiness/human-loop-to-seed-lift/TECHNIQUE.md",
            ),
            (
                "techniques/agent-workflows/approval-sensitivity-check/TECHNIQUE.md",
                "techniques/governance/automation-readiness/approval-sensitivity-check/TECHNIQUE.md",
            ),
        ):
            with self.subTest(current_path=current_path):
                self.assertFalse((REPO_ROOT / current_path).exists())
                self.assertTrue((REPO_ROOT / future_path).is_file())

    def test_automation_readiness_direct_read_review_accepts_twenty_fifth_pilot(
        self,
    ) -> None:
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "automation-readiness-direct-read-migration-review.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Automation-Readiness Direct-Read Migration Review", review)
        self.assertIn("accepted-for-twenty-fifth-migration-pilot", review)
        self.assertIn("Accept `governance/automation-readiness`", review)
        self.assertIn("Candidate B and Candidate C stay out", review)
        self.assertIn("Run the twenty-fifth migration pilot", review)
        self.assertIn(
            "automation-readiness-direct-read-migration-review",
            reviews_index,
        )
        self.assertIn(
            "automation-readiness direct-read review: landed",
            ingress,
        )
        self.assertIn(
            "accepted-for-twenty-fifth-migration-pilot",
            ingress,
        )
        self.assertIn(
            "Automation-readiness direct-read migration review",
            landing_log,
        )
        self.assertIn(
            "automation-readiness direct-read review is now landed",
            distillation_roadmap,
        )
        self.assertIn(
            "Migrate exactly `AOA-T-0086`, `AOA-T-0087`, and `AOA-T-0088`",
            root_roadmap,
        )
        self.assertIn(
            "automation-readiness` direct-read\nreview accepts",
            root_roadmap,
        )
        self.assertIn(
            "Automation-Readiness Direct-Read Migration Review",
            tree_contract,
        )
        self.assertIn(
            "migration should move exactly those three bundles",
            tree_contract,
        )
        self.assertIn(
            "accepted the `automation-readiness` direct-read migration review",
            changelog,
        )

        for technique_id, current_path, future_path in (
            (
                "AOA-T-0086",
                "techniques/agent-workflows/automation-fit-matrix/TECHNIQUE.md",
                "techniques/governance/automation-readiness/automation-fit-matrix/TECHNIQUE.md",
            ),
            (
                "AOA-T-0087",
                "techniques/agent-workflows/human-loop-to-seed-lift/TECHNIQUE.md",
                "techniques/governance/automation-readiness/human-loop-to-seed-lift/TECHNIQUE.md",
            ),
            (
                "AOA-T-0088",
                "techniques/agent-workflows/approval-sensitivity-check/TECHNIQUE.md",
                "techniques/governance/automation-readiness/approval-sensitivity-check/TECHNIQUE.md",
            ),
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)
                self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                self.assertIn(future_path.rsplit("/", 1)[0] + "/", review)
                self.assertFalse((REPO_ROOT / current_path).exists())
                self.assertTrue((REPO_ROOT / future_path).is_file())

    def test_automation_readiness_tree_pilot_migration_landed(self) -> None:
        receipt = (
            REPO_ROOT
            / "legacy"
            / "receipts"
            / "2026-05-05-automation-readiness-tree-pilot.md"
        ).read_text(encoding="utf-8")
        governance_agents = (
            REPO_ROOT / "techniques" / "governance" / "AGENTS.md"
        ).read_text(encoding="utf-8")
        agent_workflows_agents = (
            REPO_ROOT / "techniques" / "agent-workflows" / "AGENTS.md"
        ).read_text(encoding="utf-8")
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        legacy_index = (REPO_ROOT / "legacy" / "INDEX.md").read_text(
            encoding="utf-8"
        )
        receipts_index = (
            REPO_ROOT / "legacy" / "receipts" / "README.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Automation-Readiness Tree Pilot Receipt", receipt)
        self.assertIn("Twenty-fifth authored path migration", receipt)
        self.assertIn("`domain` stayed unchanged as `agent-workflows`", receipt)
        self.assertIn("`kind` stayed unchanged as `assessment`", receipt)
        self.assertIn("automation-readiness/", governance_agents)
        self.assertIn("automation-fit", governance_agents)
        self.assertNotIn("automation-fit-matrix", agent_workflows_agents)
        self.assertIn("automation-readiness migration: landed", ingress)
        self.assertIn("Automation-readiness tree pilot migration", landing_log)
        self.assertIn(
            "2026-05-05-automation-readiness-tree-pilot",
            landing_log,
        )
        self.assertIn(
            "twenty-fifth pilot\n   migration is now landed",
            distillation_roadmap,
        )
        self.assertIn(
            "Review the landed `governance/automation-readiness` pilot",
            root_roadmap,
        )
        self.assertIn(
            "2026-05-05-automation-readiness-tree-pilot",
            tree_contract,
        )
        self.assertIn("twenty-six receipts", legacy_index)
        self.assertIn(
            "2026-05-05-automation-readiness-tree-pilot.md",
            legacy_index,
        )
        self.assertIn("twenty-six technique tree pilot receipts", receipts_index)
        self.assertIn("moved `AOA-T-0086`", changelog)

        for technique_id, old_path, new_path in (
            (
                "AOA-T-0086",
                "techniques/agent-workflows/automation-fit-matrix/",
                "techniques/governance/automation-readiness/automation-fit-matrix/",
            ),
            (
                "AOA-T-0087",
                "techniques/agent-workflows/human-loop-to-seed-lift/",
                "techniques/governance/automation-readiness/human-loop-to-seed-lift/",
            ),
            (
                "AOA-T-0088",
                "techniques/agent-workflows/approval-sensitivity-check/",
                "techniques/governance/automation-readiness/approval-sensitivity-check/",
            ),
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, receipt)
                self.assertIn(old_path, receipt)
                self.assertIn(new_path, receipt)
                self.assertFalse((REPO_ROOT / old_path).exists())
                self.assertTrue((REPO_ROOT / new_path / "TECHNIQUE.md").is_file())

    def test_landed_automation_readiness_pilot_review_routes_candidate_b(
        self,
    ) -> None:
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "landed-automation-readiness-pilot-review.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Landed Automation-Readiness Pilot Review", review)
        self.assertIn("pilot-validated", review)
        self.assertIn(
            "The landed `governance/automation-readiness` shelf holds.",
            review,
        )
        self.assertIn("generated tree projection keeps", review)
        self.assertIn("Run a direct-read review for Candidate B", review)
        self.assertIn("governance/promotion-boundary", review)
        self.assertIn(
            "landed-automation-readiness-pilot-review",
            reviews_index,
        )
        self.assertIn(
            "landed automation-readiness pilot review: landed",
            ingress,
        )
        self.assertIn("Landed automation-readiness pilot review", landing_log)
        self.assertIn(
            "automation-readiness` pilot review is now complete",
            distillation_roadmap,
        )
        self.assertIn(
            "Run the `governance/promotion-boundary` direct-read review",
            root_roadmap,
        )
        self.assertIn("Landed Automation-Readiness Pilot Review", tree_contract)
        self.assertIn(
            "accepted the landed `automation-readiness` pilot review",
            changelog,
        )

        for old_path, new_path in (
            (
                "techniques/agent-workflows/automation-fit-matrix/TECHNIQUE.md",
                "techniques/governance/automation-readiness/automation-fit-matrix/TECHNIQUE.md",
            ),
            (
                "techniques/agent-workflows/human-loop-to-seed-lift/TECHNIQUE.md",
                "techniques/governance/automation-readiness/human-loop-to-seed-lift/TECHNIQUE.md",
            ),
            (
                "techniques/agent-workflows/approval-sensitivity-check/TECHNIQUE.md",
                "techniques/governance/automation-readiness/approval-sensitivity-check/TECHNIQUE.md",
            ),
        ):
            with self.subTest(new_path=new_path):
                self.assertFalse((REPO_ROOT / old_path).exists())
                self.assertTrue((REPO_ROOT / new_path).is_file())

        for current_path, future_path in (
            (
                "techniques/agent-workflows/quest-unit-promotion-review/TECHNIQUE.md",
                "techniques/governance/promotion-boundary/quest-unit-promotion-review/TECHNIQUE.md",
            ),
            (
                "techniques/agent-workflows/nearest-wrong-target-rejection/TECHNIQUE.md",
                "techniques/governance/promotion-boundary/nearest-wrong-target-rejection/TECHNIQUE.md",
            ),
            (
                "techniques/agent-workflows/skill-proposal-handoff-packet/TECHNIQUE.md",
                "techniques/governance/promotion-boundary/skill-proposal-handoff-packet/TECHNIQUE.md",
            ),
        ):
            with self.subTest(current_path=current_path):
                self.assertFalse((REPO_ROOT / current_path).exists())
                self.assertTrue((REPO_ROOT / future_path).is_file())

    def test_promotion_boundary_direct_read_review_accepts_twenty_sixth_pilot(
        self,
    ) -> None:
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "promotion-boundary-direct-read-migration-review.md"
        ).read_text(encoding="utf-8")
        reviews_index = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "README.md"
        ).read_text(encoding="utf-8")
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Promotion-Boundary Direct-Read Migration Review", review)
        self.assertIn("accepted-for-twenty-sixth-migration-pilot", review)
        self.assertIn("Accept `governance/promotion-boundary`", review)
        self.assertIn("Candidate C remains queued", review)
        self.assertIn("Run the twenty-sixth migration pilot", review)
        self.assertIn(
            "promotion-boundary-direct-read-migration-review",
            reviews_index,
        )
        self.assertIn(
            "promotion-boundary direct-read review: landed",
            ingress,
        )
        self.assertIn(
            "accepted-for-twenty-sixth-migration-pilot",
            ingress,
        )
        self.assertIn(
            "Promotion-boundary direct-read migration review",
            landing_log,
        )
        self.assertIn(
            "promotion-boundary direct-read review is now\n   landed",
            distillation_roadmap,
        )
        self.assertIn(
            "Previous Candidate B migration breadcrumb preserved",
            root_roadmap,
        )
        self.assertIn(
            "Promotion-Boundary Direct-Read Migration Review",
            tree_contract,
        )
        self.assertIn(
            "migration should move exactly those\nthree bundles",
            tree_contract,
        )
        self.assertIn(
            "accepted the `promotion-boundary` direct-read migration review",
            changelog,
        )

        for technique_id, current_path, future_path in (
            (
                "AOA-T-0089",
                "techniques/agent-workflows/quest-unit-promotion-review/TECHNIQUE.md",
                "techniques/governance/promotion-boundary/quest-unit-promotion-review/TECHNIQUE.md",
            ),
            (
                "AOA-T-0090",
                "techniques/agent-workflows/nearest-wrong-target-rejection/TECHNIQUE.md",
                "techniques/governance/promotion-boundary/nearest-wrong-target-rejection/TECHNIQUE.md",
            ),
            (
                "AOA-T-0102",
                "techniques/agent-workflows/skill-proposal-handoff-packet/TECHNIQUE.md",
                "techniques/governance/promotion-boundary/skill-proposal-handoff-packet/TECHNIQUE.md",
            ),
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, review)
                self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                self.assertIn(future_path.rsplit("/", 1)[0] + "/", review)
                self.assertFalse((REPO_ROOT / current_path).exists())
                self.assertTrue((REPO_ROOT / future_path).is_file())

        for current_path, future_path in (
            (
                "techniques/agent-workflows/local-pattern-adoption-gate/TECHNIQUE.md",
                "techniques/governance/practice-adoption-lifecycle/local-pattern-adoption-gate/TECHNIQUE.md",
            ),
            (
                "techniques/agent-workflows/adopted-practice-retention-review/TECHNIQUE.md",
                "techniques/governance/practice-adoption-lifecycle/adopted-practice-retention-review/TECHNIQUE.md",
            ),
            (
                "techniques/agent-workflows/superseded-practice-obsolescence-route/TECHNIQUE.md",
                "techniques/governance/practice-adoption-lifecycle/superseded-practice-obsolescence-route/TECHNIQUE.md",
            ),
        ):
            with self.subTest(current_path=current_path):
                self.assertTrue((REPO_ROOT / current_path).is_file())
                self.assertFalse((REPO_ROOT / future_path).exists())

    def test_promotion_boundary_tree_pilot_migration_landed(self) -> None:
        receipt = (
            REPO_ROOT
            / "legacy"
            / "receipts"
            / "2026-05-05-promotion-boundary-tree-pilot.md"
        ).read_text(encoding="utf-8")
        governance_agents = (
            REPO_ROOT / "techniques" / "governance" / "AGENTS.md"
        ).read_text(encoding="utf-8")
        agent_workflows_agents = (
            REPO_ROOT / "techniques" / "agent-workflows" / "AGENTS.md"
        ).read_text(encoding="utf-8")
        ingress = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "README.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")
        distillation_roadmap = (
            REPO_ROOT / "mechanics" / "distillation" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        root_roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        legacy_index = (REPO_ROOT / "legacy" / "INDEX.md").read_text(
            encoding="utf-8"
        )
        receipts_index = (
            REPO_ROOT / "legacy" / "receipts" / "README.md"
        ).read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("Promotion-Boundary Tree Pilot Receipt", receipt)
        self.assertIn("Twenty-sixth authored path migration", receipt)
        self.assertIn("`domain` stayed unchanged as `agent-workflows`", receipt)
        self.assertIn("`kind` stayed unchanged as `assessment`", receipt)
        self.assertIn("`kind: guardrail`", landing_log)
        self.assertIn("`kind: handoff`", landing_log)
        self.assertIn("promotion-boundary/", governance_agents)
        self.assertIn("nearest-wrong-target", governance_agents)
        self.assertNotIn("quest-unit-promotion-review", agent_workflows_agents)
        self.assertIn("promotion-boundary migration: landed", ingress)
        self.assertIn("Promotion-boundary tree pilot migration", landing_log)
        self.assertIn(
            "2026-05-05-promotion-boundary-tree-pilot",
            landing_log,
        )
        self.assertIn(
            "twenty-sixth pilot\n   migration is now landed",
            distillation_roadmap,
        )
        self.assertIn(
            "Review the landed `governance/promotion-boundary` pilot",
            root_roadmap,
        )
        self.assertIn(
            "2026-05-05-promotion-boundary-tree-pilot",
            tree_contract,
        )
        self.assertIn("twenty-six receipts", legacy_index)
        self.assertIn(
            "2026-05-05-promotion-boundary-tree-pilot.md",
            legacy_index,
        )
        self.assertIn("twenty-six technique tree pilot receipts", receipts_index)
        self.assertIn("moved `AOA-T-0089`", changelog)

        for technique_id, old_path, new_path in (
            (
                "AOA-T-0089",
                "techniques/agent-workflows/quest-unit-promotion-review/",
                "techniques/governance/promotion-boundary/quest-unit-promotion-review/",
            ),
            (
                "AOA-T-0090",
                "techniques/agent-workflows/nearest-wrong-target-rejection/",
                "techniques/governance/promotion-boundary/nearest-wrong-target-rejection/",
            ),
            (
                "AOA-T-0102",
                "techniques/agent-workflows/skill-proposal-handoff-packet/",
                "techniques/governance/promotion-boundary/skill-proposal-handoff-packet/",
            ),
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, receipt)
                self.assertIn(old_path, receipt)
                self.assertIn(new_path, receipt)
                self.assertFalse((REPO_ROOT / old_path).exists())
                self.assertTrue((REPO_ROOT / new_path / "TECHNIQUE.md").is_file())

    def test_cross_layer_candidate_ledger_has_preserved_pre_prune_receipt(self) -> None:
        active = (
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
        legacy_index = (
            REPO_ROOT / "mechanics" / "distillation" / "legacy" / "INDEX.md"
        ).read_text(encoding="utf-8")
        legacy_log = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "legacy"
            / "DISTILLATION_LOG.md"
        ).read_text(encoding="utf-8")

        self.assertIn("CROSS_LAYER_CANDIDATE_LEDGER_2026-05-01_PRE_PRUNE.md", active)
        self.assertIn("## Current Wave Program", receipt)
        self.assertIn("1. `profile-preset-composition`", receipt)
        self.assertIn("1. `skill-vs-command-boundary`", receipt)
        self.assertIn("1. `versionable-session-transcripts`", receipt)
        self.assertIn("CROSS_LAYER_CANDIDATE_LEDGER_2026-05-01_PRE_PRUNE.md", legacy_index)
        self.assertIn("Cross-layer candidate ledger active compaction", legacy_log)

    def test_distillation_active_parts_decision_is_discoverable(self) -> None:
        decision = (
            REPO_ROOT
            / "docs"
            / "decisions"
            / "2026-05-01-distillation-active-parts-split.md"
        ).read_text(encoding="utf-8")

        self.assertIn("Distillation Active Parts Split", decision)
        self.assertIn("mechanics/distillation/parts/", decision)
        self.assertIn("No candidate verdicts, ledger counts, or technique statuses", decision)

    def test_external_candidate_registry_decision_is_discoverable(self) -> None:
        decision = (
            REPO_ROOT
            / "docs"
            / "decisions"
            / "2026-05-01-distillation-external-candidate-registry.md"
        ).read_text(encoding="utf-8")

        self.assertIn("Distillation External Candidate Registry", decision)
        self.assertIn("generated compact index is validation evidence only", decision)
        self.assertIn("normal bundle review path", decision)

    def test_cross_layer_candidate_registry_decision_is_discoverable(self) -> None:
        decision = (
            REPO_ROOT
            / "docs"
            / "decisions"
            / "2026-05-01-distillation-cross-layer-candidate-registry.md"
        ).read_text(encoding="utf-8")

        self.assertIn("Distillation Cross-Layer Candidate Registry", decision)
        self.assertIn("without compacting the README in this pass", decision)
        self.assertIn("recurrence and later compaction work", decision)

    def test_distillation_gate_packet_is_named_across_active_parts(self) -> None:
        donor_refinery = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "donor-refinery"
            / "README.md"
        ).read_text(encoding="utf-8")
        external_runbook = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "external-import-runbook"
            / "README.md"
        ).read_text(encoding="utf-8")

        for text in (donor_refinery, external_runbook):
            with self.subTest(surface=text.splitlines()[0]):
                self.assertIn("Atom/Topology", text)
                self.assertIn("Boundary", text)
                self.assertIn("atomic_move_note", text)
                self.assertIn("atomic_move_status", text)
                self.assertIn("capability_class", text)
                self.assertIn("execution_profile", text)
                self.assertIn("risk_posture", text)
                self.assertIn("higher_law", text)
                self.assertIn("local_route", text)
                self.assertIn("bridge_stop_line", text)

        for verdict in (
            "pass_to_import_runbook",
            "ledger_hold",
            "overlap_hold",
            "layer_incubation",
            "not_technique_shaped",
        ):
            with self.subTest(verdict=verdict):
                self.assertIn(verdict, donor_refinery)

    def test_distillation_reopen_gates_preserve_registry_authority_boundary(self) -> None:
        external = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "external-candidate-ledger"
            / "README.md"
        ).read_text(encoding="utf-8")
        cross_layer = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "cross-layer-candidate-ledger"
            / "README.md"
        ).read_text(encoding="utf-8")

        for text in (external, cross_layer):
            with self.subTest(surface=text.splitlines()[0]):
                self.assertIn("## Reopen Gate", text)
                self.assertIn("Atom/topology gate", text)
                self.assertIn("Boundary/portability gate", text)
                self.assertIn("atomic_move_note", text)
                self.assertIn("atomic_move_status", text)
                self.assertIn("higher_law", text)
                self.assertIn("local_route", text)
                self.assertIn("bridge_stop_line", text)
                self.assertIn("generated registry", text)

        self.assertIn("inherited external rows reopen", cross_layer)
        self.assertIn("landed rows do not reopen as candidates", cross_layer)

    def test_distillation_gate_alignment_decision_is_discoverable(self) -> None:
        decision = (
            REPO_ROOT
            / "docs"
            / "decisions"
            / "2026-05-01-distillation-gate-alignment.md"
        ).read_text(encoding="utf-8")

        self.assertIn("Distillation Gate Alignment", decision)
        self.assertIn("gate packet", decision)
        self.assertIn("atom/topology", decision)
        self.assertIn("boundary/portability", decision)
        self.assertIn("generated registries remain", decision)
        self.assertIn("evidence only", decision)

    def test_distillation_agon_handoff_decision_is_discoverable(self) -> None:
        decision = (
            REPO_ROOT
            / "docs"
            / "decisions"
            / "2026-05-03-distillation-agon-candidate-handoff.md"
        ).read_text(encoding="utf-8")

        self.assertIn("Distillation Agon Candidate Handoff", decision)
        self.assertIn("cover all `22`", decision)
        self.assertIn("current Agon technique-side candidates", decision)
        self.assertIn("Agon remains the source route", decision)
        self.assertIn("The generated handoff index is evidence only", decision)

    def test_mechanics_boundary_language_correction_is_discoverable(self) -> None:
        decision = (
            REPO_ROOT
            / "docs"
            / "decisions"
            / "2026-05-01-mechanics-boundary-language-correction.md"
        ).read_text(encoding="utf-8")

        mechanics_readme = (REPO_ROOT / "mechanics" / "README.md").read_text(
            encoding="utf-8"
        )
        agon_readme = (
            REPO_ROOT / "mechanics" / "agon" / "README.md"
        ).read_text(encoding="utf-8")
        audit_direction = (
            REPO_ROOT / "mechanics" / "audit" / "DIRECTION.md"
        ).read_text(encoding="utf-8")

        self.assertIn("Mechanics Boundary Language Correction", decision)
        self.assertIn("not an instruction to copy", decision)
        self.assertNotIn("## Law, Local Form, Bridges", mechanics_readme)
        self.assertNotIn("### Law, local route, bridge", agon_readme)
        self.assertNotIn("## Law, Local Route, Bridge", audit_direction)


if __name__ == "__main__":
    unittest.main()
