from __future__ import annotations

import sys
import unittest
from pathlib import Path


SUPPORT_DIR = Path(__file__).resolve().parent / "support"
if str(SUPPORT_DIR) not in sys.path:
    sys.path.insert(0, str(SUPPORT_DIR))

from distillation_topology_fixtures import *  # noqa: F403


class DistillationPartLedgersHandoffTests(unittest.TestCase):
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
                        self.assertRegex(text, r"draft kind: `[^`]+`")
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


if __name__ == "__main__":
    unittest.main()
