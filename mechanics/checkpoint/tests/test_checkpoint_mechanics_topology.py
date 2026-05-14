from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]

ACTIVE_CHECKPOINT_SURFACES = (
    "mechanics/checkpoint/AGENTS.md",
    "mechanics/checkpoint/README.md",
    "mechanics/checkpoint/DIRECTION.md",
    "mechanics/checkpoint/PARTS.md",
    "mechanics/checkpoint/PROVENANCE.md",
    "mechanics/checkpoint/LANDING_LOG.md",
    "mechanics/checkpoint/ROADMAP.md",
    "mechanics/checkpoint/parts/AGENTS.md",
    "mechanics/checkpoint/parts/README.md",
)

PART_LOCAL_CHECKPOINT_READMES = (
    "mechanics/checkpoint/parts/phase-handoff-candidate/README.md",
    "mechanics/checkpoint/parts/technique-anchors/README.md",
)


class CheckpointMechanicsTopologyTestCase(unittest.TestCase):
    def test_checkpoint_active_surfaces_are_discoverable(self) -> None:
        for relative_path in ACTIVE_CHECKPOINT_SURFACES + PART_LOCAL_CHECKPOINT_READMES:
            with self.subTest(relative_path=relative_path):
                self.assertTrue((REPO_ROOT / relative_path).is_file())

    def test_checkpoint_part_map_names_all_current_parts(self) -> None:
        parts = (REPO_ROOT / "mechanics" / "checkpoint" / "PARTS.md").read_text(
            encoding="utf-8"
        )
        provenance = (
            REPO_ROOT / "mechanics" / "checkpoint" / "PROVENANCE.md"
        ).read_text(encoding="utf-8")

        for part_name in ("phase-handoff-candidate", "technique-anchors"):
            with self.subTest(part_name=part_name):
                self.assertIn(part_name, parts)
                self.assertIn(part_name, provenance)

    def test_checkpoint_stays_outside_direct_orq_lane(self) -> None:
        receipts = (REPO_ROOT / "mechanics" / "REQUEST_RECEIPTS.md").read_text(
            encoding="utf-8"
        )
        direct_section = receipts.split("## Non-ORQ Center Pressure", 1)[0]
        non_orq_section = receipts.split("## Non-ORQ Center Pressure", 1)[1]

        self.assertNotIn("ORQ-CHECKPOINT-TECHNIQUES", direct_section)
        self.assertIn("### [checkpoint](checkpoint/README.md)", non_orq_section)
        self.assertIn("Current status: `candidate-only`", non_orq_section)
        self.assertIn(
            "direct `ORQ-CHECKPOINT-TECHNIQUES-*` request",
            non_orq_section,
        )
        for phrase in (
            "checkpoint implementation\n  authority",
            "memory canon",
            "proof verdicts",
            "runtime activation",
            "owner\n  acceptance",
            "hidden scheduler behavior",
            "autonomous self-repair",
            "automatic\n  technique promotion",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, non_orq_section)

    def test_phase_handoff_candidate_preserves_gate(self) -> None:
        candidate = (
            REPO_ROOT
            / "mechanics"
            / "checkpoint"
            / "parts"
            / "phase-handoff-candidate"
            / "README.md"
        ).read_text(encoding="utf-8")

        for phrase in (
            "phase_sync_for_agents",
            "phase-synchronized-agent-handoff",
            "future_import_here",
            "phase boundary",
            "handoff packet",
            "continuation permission",
            "stop/return/escalation rule",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, candidate)

    def test_technique_anchors_point_to_bundle_local_homes(self) -> None:
        anchors = (
            REPO_ROOT
            / "mechanics"
            / "checkpoint"
            / "parts"
            / "technique-anchors"
            / "README.md"
        ).read_text(encoding="utf-8")

        for technique_id in (
            "AOA-T-0057",
            "AOA-T-0058",
            "AOA-T-0062",
            "AOA-T-0083",
            "AOA-T-0026",
            "AOA-T-0045",
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, anchors)

        self.assertIn("does not change technique status", anchors)
        self.assertIn("techniques/**/TECHNIQUE.md", anchors)

    def test_checkpoint_legacy_scaffold_marks_empty_raw_inventory(self) -> None:
        provenance = (
            REPO_ROOT / "mechanics" / "checkpoint" / "PROVENANCE.md"
        ).read_text(encoding="utf-8")
        compact_provenance = " ".join(provenance.split())
        legacy_dir = REPO_ROOT / "mechanics" / "checkpoint" / "legacy"
        raw_files = sorted(
            path.name for path in (legacy_dir / "raw").iterdir() if path.is_file()
        )

        for relative_path in (
            "legacy/AGENTS.md",
            "legacy/README.md",
            "legacy/INDEX.md",
            "legacy/DISTILLATION_LOG.md",
            "legacy/raw/README.md",
        ):
            with self.subTest(relative_path=relative_path):
                self.assertTrue(
                    (REPO_ROOT / "mechanics" / "checkpoint" / relative_path).is_file()
                )

        self.assertEqual(["README.md"], raw_files)
        self.assertIn("legacy scaffold", provenance)
        self.assertIn("current raw inventory is empty", provenance)
        self.assertIn("no local pre-split checkpoint", compact_provenance)

    def test_checkpoint_stop_lines_remain_explicit(self) -> None:
        direction = (
            REPO_ROOT / "mechanics" / "checkpoint" / "DIRECTION.md"
        ).read_text(encoding="utf-8")
        roadmap = (REPO_ROOT / "mechanics" / "checkpoint" / "ROADMAP.md").read_text(
            encoding="utf-8"
        )
        compact_direction = " ".join(direction.split())
        compact_roadmap = " ".join(roadmap.split())

        for phrase in (
            "checkpoint implementation authority",
            "memory canon",
            "proof verdicts",
            "runtime activation",
            "owner acceptance",
            "hidden scheduler",
            "autonomous self-repair",
            "automatic technique promotion",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, compact_direction)
                self.assertIn(phrase, compact_roadmap)


if __name__ == "__main__":
    unittest.main()
