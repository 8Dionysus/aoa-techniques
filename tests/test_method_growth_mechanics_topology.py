from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

ACTIVE_METHOD_GROWTH_SURFACES = (
    "mechanics/method-growth/AGENTS.md",
    "mechanics/method-growth/README.md",
    "mechanics/method-growth/DIRECTION.md",
    "mechanics/method-growth/PARTS.md",
    "mechanics/method-growth/PROVENANCE.md",
    "mechanics/method-growth/LANDING_LOG.md",
    "mechanics/method-growth/ROADMAP.md",
    "mechanics/method-growth/parts/AGENTS.md",
    "mechanics/method-growth/parts/README.md",
)

PART_LOCAL_METHOD_GROWTH_READMES = (
    "mechanics/method-growth/parts/pattern-adoption/README.md",
    "mechanics/method-growth/parts/adoption-boundaries/README.md",
    "mechanics/method-growth/parts/technique-to-skill-handoff/README.md",
    "mechanics/method-growth/parts/retention-checks/README.md",
    "mechanics/method-growth/parts/obsolescence/README.md",
)

OLD_FLAT_METHOD_GROWTH_FILES = (
    "mechanics/method-growth/TECHNIQUE_PATTERN_ADOPTION.md",
    "mechanics/method-growth/TECHNIQUE_ADOPTION_BOUNDARIES.md",
    "mechanics/method-growth/TECHNIQUE_TO_SKILL_HANDOFF.md",
    "mechanics/method-growth/TECHNIQUE_RETENTION_CHECKS.md",
    "mechanics/method-growth/TECHNIQUE_OBSOLESCENCE.md",
)


class MethodGrowthMechanicsTopologyTestCase(unittest.TestCase):
    def test_method_growth_active_surfaces_are_discoverable(self) -> None:
        for relative_path in ACTIVE_METHOD_GROWTH_SURFACES + PART_LOCAL_METHOD_GROWTH_READMES:
            with self.subTest(relative_path=relative_path):
                self.assertTrue((REPO_ROOT / relative_path).is_file())

    def test_method_growth_flat_files_moved_into_owning_parts(self) -> None:
        for relative_path in OLD_FLAT_METHOD_GROWTH_FILES:
            with self.subTest(relative_path=relative_path):
                self.assertFalse((REPO_ROOT / relative_path).exists())

    def test_method_growth_part_map_names_all_current_parts(self) -> None:
        parts = (REPO_ROOT / "mechanics" / "method-growth" / "PARTS.md").read_text(
            encoding="utf-8"
        )
        provenance = (
            REPO_ROOT / "mechanics" / "method-growth" / "PROVENANCE.md"
        ).read_text(encoding="utf-8")

        for part_name in (
            "pattern-adoption",
            "adoption-boundaries",
            "technique-to-skill-handoff",
            "retention-checks",
            "obsolescence",
        ):
            with self.subTest(part_name=part_name):
                self.assertIn(part_name, parts)
                self.assertIn(part_name, provenance)

    def test_request_receipt_points_to_method_growth_parts(self) -> None:
        receipts = (REPO_ROOT / "mechanics" / "REQUEST_RECEIPTS.md").read_text(
            encoding="utf-8"
        )
        method_section = receipts.split("### `ORQ-METHOD-TECHNIQUES-001`", 1)[1].split(
            "### `ORQ-DISTILLATION-TECHNIQUES-001`",
            1,
        )[0]

        self.assertIn("Local status: `mapped-with-local-evidence`", method_section)
        self.assertIn("Pattern Adoption", method_section)
        self.assertIn("Technique To Skill Handoff", method_section)
        self.assertIn("skill acceptance", method_section)
        self.assertIn("technique canon lands only", method_section)


if __name__ == "__main__":
    unittest.main()
