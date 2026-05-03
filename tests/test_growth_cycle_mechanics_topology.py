from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

ACTIVE_GROWTH_CYCLE_SURFACES = (
    "mechanics/growth-cycle/AGENTS.md",
    "mechanics/growth-cycle/README.md",
    "mechanics/growth-cycle/DIRECTION.md",
    "mechanics/growth-cycle/PARTS.md",
    "mechanics/growth-cycle/PROVENANCE.md",
    "mechanics/growth-cycle/LANDING_LOG.md",
    "mechanics/growth-cycle/ROADMAP.md",
    "mechanics/growth-cycle/parts/AGENTS.md",
    "mechanics/growth-cycle/parts/README.md",
)

PART_LOCAL_GROWTH_CYCLE_READMES = (
    "mechanics/growth-cycle/parts/mastery-harvest/README.md",
    "mechanics/growth-cycle/parts/technique-feat-model/README.md",
    "mechanics/growth-cycle/parts/questbook-integration/README.md",
    "mechanics/growth-cycle/parts/promotion-readiness-incubation/README.md",
)

OLD_FLAT_GROWTH_CYCLE_FILES = (
    "mechanics/growth-cycle/MASTERY_HARVEST_POSTURE.md",
    "mechanics/growth-cycle/TECHNIQUE_FEAT_MODEL.md",
    "mechanics/growth-cycle/QUESTBOOK_TECHNIQUE_INTEGRATION.md",
    "mechanics/growth-cycle/REVIEWED_CLOSEOUT_PROMOTION_READINESS_INCUBATION.md",
)


class GrowthCycleMechanicsTopologyTestCase(unittest.TestCase):
    def test_growth_cycle_active_surfaces_are_discoverable(self) -> None:
        for relative_path in ACTIVE_GROWTH_CYCLE_SURFACES + PART_LOCAL_GROWTH_CYCLE_READMES:
            with self.subTest(relative_path=relative_path):
                self.assertTrue((REPO_ROOT / relative_path).is_file())

    def test_growth_cycle_flat_files_moved_into_owning_parts(self) -> None:
        for relative_path in OLD_FLAT_GROWTH_CYCLE_FILES:
            with self.subTest(relative_path=relative_path):
                self.assertFalse((REPO_ROOT / relative_path).exists())

    def test_growth_cycle_part_map_names_all_current_parts(self) -> None:
        parts = (REPO_ROOT / "mechanics" / "growth-cycle" / "PARTS.md").read_text(
            encoding="utf-8"
        )
        provenance = (
            REPO_ROOT / "mechanics" / "growth-cycle" / "PROVENANCE.md"
        ).read_text(encoding="utf-8")

        for part_name in (
            "mastery-harvest",
            "technique-feat-model",
            "questbook-integration",
            "promotion-readiness-incubation",
        ):
            with self.subTest(part_name=part_name):
                self.assertIn(part_name, parts)
                self.assertIn(part_name, provenance)

    def test_growth_cycle_stays_outside_direct_orq_lane(self) -> None:
        receipts = (REPO_ROOT / "mechanics" / "REQUEST_RECEIPTS.md").read_text(
            encoding="utf-8"
        )
        direct_section = receipts.split("## Non-ORQ Center Pressure", 1)[0]
        non_orq_section = receipts.split("## Non-ORQ Center Pressure", 1)[1]

        self.assertNotIn("ORQ-GROWTHCYCLE-TECHNIQUES", direct_section)
        self.assertIn("### [growth-cycle](growth-cycle/README.md)", non_orq_section)
        self.assertIn("Current status: `candidate-only`", non_orq_section)
        self.assertIn("no\n  direct `ORQ-GROWTHCYCLE-TECHNIQUES-*` request", non_orq_section)

    def test_growth_cycle_reference_paths_point_to_part_local_homes(self) -> None:
        expected_paths = (
            "mechanics/growth-cycle/parts/technique-feat-model/README.md",
            "mechanics/growth-cycle/parts/promotion-readiness-incubation/README.md",
        )

        for relative_path in (
            "README.md",
            "docs/README.md",
            "docs/AGENTS_ROOT_REFERENCE.md",
            "quests/techniques/captured/AOA-TECH-Q-0005.yaml",
            "quests/techniques/captured/AOA-TECH-Q-0007.yaml",
            "scripts/validate_repo.py",
            "tests/test_validate_repo.py",
        ):
            content = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
            with self.subTest(relative_path=relative_path):
                self.assertNotIn("mechanics/growth-cycle/TECHNIQUE_FEAT_MODEL.md", content)
                self.assertNotIn(
                    "mechanics/growth-cycle/REVIEWED_CLOSEOUT_PROMOTION_READINESS_INCUBATION.md",
                    content,
                )
                self.assertNotIn(
                    "mechanics/growth-cycle/QUESTBOOK_TECHNIQUE_INTEGRATION.md",
                    content,
                )

        combined = "\n".join(
            (REPO_ROOT / relative_path).read_text(encoding="utf-8")
            for relative_path in (
                "README.md",
                "docs/README.md",
                "docs/AGENTS_ROOT_REFERENCE.md",
                "quests/techniques/captured/AOA-TECH-Q-0005.yaml",
                "quests/techniques/captured/AOA-TECH-Q-0007.yaml",
                "scripts/validate_repo.py",
            )
        )
        for expected_path in expected_paths:
            with self.subTest(expected_path=expected_path):
                self.assertIn(expected_path, combined)

        validator = (REPO_ROOT / "scripts" / "validate_repo.py").read_text(
            encoding="utf-8"
        )
        self.assertIn('"parts"', validator)
        self.assertIn('"questbook-integration"', validator)

    def test_mechanics_roadmaps_are_not_silently_ignored(self) -> None:
        gitignore = (REPO_ROOT / ".gitignore").read_text(encoding="utf-8")

        self.assertIn("ROADMAP.md", gitignore)
        self.assertIn("!mechanics/*/ROADMAP.md", gitignore)


if __name__ == "__main__":
    unittest.main()
