from __future__ import annotations

import sys
import unittest
from pathlib import Path


SUPPORT_DIR = Path(__file__).resolve().parent / "support"
if str(SUPPORT_DIR) not in sys.path:
    sys.path.insert(0, str(SUPPORT_DIR))

from distillation_topology_fixtures import *  # noqa: F403


class DistillationGateDecisionsTests(unittest.TestCase):
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
                / "AOA-TECH-D-0004-distillation-active-parts-split.md"
            ).read_text(encoding="utf-8")

            self.assertIn("Distillation Active Parts Split", decision)
            self.assertIn("mechanics/distillation/parts/", decision)
            self.assertIn("No candidate verdicts, ledger counts, or technique statuses", decision)

    def test_external_candidate_registry_decision_is_discoverable(self) -> None:
            decision = (
                REPO_ROOT
                / "docs"
                / "decisions"
                / "AOA-TECH-D-0006-distillation-external-candidate-registry.md"
            ).read_text(encoding="utf-8")

            self.assertIn("Distillation External Candidate Registry", decision)
            self.assertIn("generated compact index is validation evidence only", decision)
            self.assertIn("normal bundle review path", decision)

    def test_cross_layer_candidate_registry_decision_is_discoverable(self) -> None:
            decision = (
                REPO_ROOT
                / "docs"
                / "decisions"
                / "AOA-TECH-D-0005-distillation-cross-layer-candidate-registry.md"
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
                / "AOA-TECH-D-0007-distillation-gate-alignment.md"
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
                / "AOA-TECH-D-0024-distillation-agon-candidate-handoff.md"
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
                / "AOA-TECH-D-0010-mechanics-boundary-language-correction.md"
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
