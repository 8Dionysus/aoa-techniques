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
                "candidate:aoa-techniques:agon/challenge-claim-practice": "techniques/agent-workflows/single-locus-claim-challenge/TECHNIQUE.md",
                "candidate:aoa-techniques:agon/request-evidence-practice": "techniques/agent-workflows/single-missing-evidence-request/TECHNIQUE.md",
                "candidate:aoa-techniques:agon/offer-evidence-reference-practice": "techniques/docs/single-scoped-evidence-reference/TECHNIQUE.md",
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
        self.assertIn("landed `review-compaction` pilot", root_roadmap)
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
        self.assertIn("exactly those seven bundles", ingress)
        self.assertIn("handoff-continuation` direct-read migration review is now landed", distillation_roadmap)
        self.assertIn("Handoff-continuation direct-read migration review", landing_log)
        self.assertIn("second direct-read review accepted `handoff-continuation`", root_roadmap)
        self.assertIn("Handoff-Continuation Direct-Read Migration Review", tree_contract)
        self.assertIn("accepted the `handoff-continuation` direct-read migration review", changelog)

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
