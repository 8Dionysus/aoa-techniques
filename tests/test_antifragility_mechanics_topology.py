from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

ACTIVE_ANTIFRAGILITY_SURFACES = (
    "mechanics/antifragility/AGENTS.md",
    "mechanics/antifragility/README.md",
    "mechanics/antifragility/DIRECTION.md",
    "mechanics/antifragility/PARTS.md",
    "mechanics/antifragility/PROVENANCE.md",
    "mechanics/antifragility/LANDING_LOG.md",
    "mechanics/antifragility/ROADMAP.md",
    "mechanics/antifragility/parts/AGENTS.md",
    "mechanics/antifragility/parts/README.md",
    "mechanics/antifragility/legacy/AGENTS.md",
    "mechanics/antifragility/legacy/README.md",
    "mechanics/antifragility/legacy/INDEX.md",
    "mechanics/antifragility/legacy/DISTILLATION_LOG.md",
    "mechanics/antifragility/legacy/raw/README.md",
)

PART_LOCAL_ANTIFRAGILITY_READMES = (
    "mechanics/antifragility/parts/chaos-wave-program/README.md",
    "mechanics/antifragility/parts/recovery-practice-bridge/README.md",
)

OLD_FLAT_ANTIFRAGILITY_FILES = (
    "mechanics/antifragility/CHAOS_WAVE1_PROGRAM.md",
)


class AntifragilityMechanicsTopologyTestCase(unittest.TestCase):
    def test_antifragility_active_surfaces_are_discoverable(self) -> None:
        for relative_path in (
            ACTIVE_ANTIFRAGILITY_SURFACES + PART_LOCAL_ANTIFRAGILITY_READMES
        ):
            with self.subTest(relative_path=relative_path):
                self.assertTrue((REPO_ROOT / relative_path).is_file())

    def test_antifragility_flat_file_moved_into_legacy_raw(self) -> None:
        for relative_path in OLD_FLAT_ANTIFRAGILITY_FILES:
            with self.subTest(relative_path=relative_path):
                self.assertFalse((REPO_ROOT / relative_path).exists())

        self.assertTrue(
            (
                REPO_ROOT
                / "mechanics"
                / "antifragility"
                / "legacy"
                / "raw"
                / "CHAOS_WAVE1_PROGRAM.md"
            ).is_file()
        )

    def test_antifragility_part_map_names_all_current_parts(self) -> None:
        parts = (REPO_ROOT / "mechanics" / "antifragility" / "PARTS.md").read_text(
            encoding="utf-8"
        )
        provenance = (
            REPO_ROOT / "mechanics" / "antifragility" / "PROVENANCE.md"
        ).read_text(encoding="utf-8")

        for part_name in (
            "chaos-wave-program",
            "recovery-practice-bridge",
        ):
            with self.subTest(part_name=part_name):
                self.assertIn(part_name, parts)
                self.assertIn(part_name, provenance)

    def test_antifragility_stays_outside_direct_orq_lane(self) -> None:
        receipts = (REPO_ROOT / "mechanics" / "REQUEST_RECEIPTS.md").read_text(
            encoding="utf-8"
        )
        direct_section = receipts.split("## Non-ORQ Center Pressure", 1)[0]
        non_orq_section = receipts.split("## Non-ORQ Center Pressure", 1)[1]

        self.assertNotIn("ORQ-ANTIFRAGILITY-TECHNIQUES", direct_section)
        self.assertIn(
            "### [antifragility](antifragility/README.md)",
            non_orq_section,
        )
        self.assertIn("Current status: `candidate-only`", non_orq_section)
        self.assertIn(
            "no\n  direct `ORQ-ANTIFRAGILITY-TECHNIQUES-*` request",
            non_orq_section,
        )
        self.assertIn("one-score health", non_orq_section)
        self.assertIn("automatic\n  technique promotion", non_orq_section)

    def test_antifragility_reference_paths_point_to_active_part_home(self) -> None:
        old_path = "mechanics/antifragility/CHAOS_WAVE1_PROGRAM.md"
        combined = "\n".join(
            (REPO_ROOT / relative_path).read_text(encoding="utf-8")
            for relative_path in (
                "docs/README.md",
                "mechanics/antifragility/README.md",
                "mechanics/antifragility/DIRECTION.md",
                "mechanics/antifragility/PARTS.md",
                "mechanics/antifragility/PROVENANCE.md",
                "mechanics/antifragility/LANDING_LOG.md",
                "mechanics/antifragility/ROADMAP.md",
                "mechanics/antifragility/parts/README.md",
                "mechanics/antifragility/parts/chaos-wave-program/README.md",
                "mechanics/antifragility/parts/recovery-practice-bridge/README.md",
            )
        )

        self.assertNotIn(old_path, combined)
        self.assertIn(
            "mechanics/antifragility/parts/chaos-wave-program/README.md",
            combined,
        )
        self.assertIn("parts/chaos-wave-program/README.md", combined)
        self.assertIn("parts/recovery-practice-bridge/README.md", combined)

    def test_antifragility_stop_lines_remain_explicit(self) -> None:
        direction = (
            REPO_ROOT / "mechanics" / "antifragility" / "DIRECTION.md"
        ).read_text(encoding="utf-8")
        roadmap = (
            REPO_ROOT / "mechanics" / "antifragility" / "ROADMAP.md"
        ).read_text(encoding="utf-8")

        for phrase in (
            "one-score health",
            "deletion",
            "owner-local cleanup authority",
            "proof verdict",
            "runtime self-healing",
            "automatic technique promotion",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, direction)
                self.assertIn(phrase, roadmap)

    def test_antifragility_recovery_bridge_names_current_anchors(self) -> None:
        bridge = (
            REPO_ROOT
            / "mechanics"
            / "antifragility"
            / "parts"
            / "recovery-practice-bridge"
            / "README.md"
        ).read_text(encoding="utf-8")

        for expected in (
            "AOA-T-0097",
            "AOA-T-0098",
            "AOA-T-0099",
            "AOA-T-0100",
            "antifragility-recovery",
            "techniques/**/TECHNIQUE.md",
        ):
            with self.subTest(expected=expected):
                self.assertIn(expected, bridge)


if __name__ == "__main__":
    unittest.main()
