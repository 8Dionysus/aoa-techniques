from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

ACTIVE_RECURRENCE_SURFACES = (
    "mechanics/recurrence/AGENTS.md",
    "mechanics/recurrence/README.md",
    "mechanics/recurrence/DIRECTION.md",
    "mechanics/recurrence/PARTS.md",
    "mechanics/recurrence/PROVENANCE.md",
    "mechanics/recurrence/LANDING_LOG.md",
    "mechanics/recurrence/ROADMAP.md",
    "mechanics/recurrence/parts/AGENTS.md",
    "mechanics/recurrence/parts/README.md",
)

PART_LOCAL_RECURRENCE_READMES = (
    "mechanics/recurrence/parts/live-observation-producers/README.md",
    "mechanics/recurrence/parts/review-decision-closure/README.md",
)

PART_LOCAL_LIVE_OBSERVATION_SCRIPT_ARTIFACTS = (
    "mechanics/recurrence/parts/live-observation-producers/scripts/AGENTS.md",
    "mechanics/recurrence/parts/live-observation-producers/scripts/publish_live_receipts.py",
)

OLD_FLAT_RECURRENCE_FILES = (
    "mechanics/recurrence/RECURRENCE_LIVE_OBSERVATION_PRODUCERS.md",
    "mechanics/recurrence/RECURRENCE_REVIEW_DECISION_CLOSURE.md",
    "scripts/publish_live_receipts.py",
)


class RecurrenceMechanicsTopologyTestCase(unittest.TestCase):
    def test_recurrence_active_surfaces_are_discoverable(self) -> None:
        for relative_path in (
            ACTIVE_RECURRENCE_SURFACES
            + PART_LOCAL_RECURRENCE_READMES
            + PART_LOCAL_LIVE_OBSERVATION_SCRIPT_ARTIFACTS
        ):
            with self.subTest(relative_path=relative_path):
                self.assertTrue((REPO_ROOT / relative_path).is_file())

    def test_recurrence_flat_files_moved_into_owning_parts(self) -> None:
        for relative_path in OLD_FLAT_RECURRENCE_FILES:
            with self.subTest(relative_path=relative_path):
                self.assertFalse((REPO_ROOT / relative_path).exists())

    def test_recurrence_part_map_names_all_current_parts(self) -> None:
        parts = (REPO_ROOT / "mechanics" / "recurrence" / "PARTS.md").read_text(
            encoding="utf-8"
        )
        provenance = (
            REPO_ROOT / "mechanics" / "recurrence" / "PROVENANCE.md"
        ).read_text(encoding="utf-8")

        for part_name in (
            "live-observation-producers",
            "review-decision-closure",
        ):
            with self.subTest(part_name=part_name):
                self.assertIn(part_name, parts)
                self.assertIn(part_name, provenance)

    def test_recurrence_stays_outside_direct_orq_lane(self) -> None:
        receipts = (REPO_ROOT / "mechanics" / "REQUEST_RECEIPTS.md").read_text(
            encoding="utf-8"
        )
        direct_section = receipts.split("## Non-ORQ Center Pressure", 1)[0]
        non_orq_section = receipts.split("## Non-ORQ Center Pressure", 1)[1]

        self.assertNotIn("ORQ-RECURRENCE-TECHNIQUES", direct_section)
        self.assertIn("### [recurrence](recurrence/README.md)", non_orq_section)
        self.assertIn("Current status: `candidate-only`", non_orq_section)
        self.assertIn(
            "no direct\n  `ORQ-RECURRENCE-TECHNIQUES-*` request",
            non_orq_section,
        )
        self.assertIn("automatic technique promotion", non_orq_section)

    def test_recurrence_reference_paths_point_to_part_local_homes(self) -> None:
        old_paths = (
            "mechanics/recurrence/RECURRENCE_LIVE_OBSERVATION_PRODUCERS.md",
            "mechanics/recurrence/RECURRENCE_REVIEW_DECISION_CLOSURE.md",
        )
        combined = "\n".join(
            (REPO_ROOT / relative_path).read_text(encoding="utf-8")
            for relative_path in (
                "mechanics/recurrence/README.md",
                "mechanics/recurrence/DIRECTION.md",
                "mechanics/recurrence/PARTS.md",
                "mechanics/recurrence/PROVENANCE.md",
                "mechanics/recurrence/LANDING_LOG.md",
                "mechanics/recurrence/ROADMAP.md",
                "mechanics/recurrence/parts/README.md",
                "mechanics/recurrence/parts/live-observation-producers/README.md",
                "mechanics/recurrence/parts/review-decision-closure/README.md",
            )
        )

        for old_path in old_paths:
            with self.subTest(old_path=old_path):
                self.assertNotIn(old_path, combined)

        for part_path in (
            "parts/live-observation-producers/README.md",
            "parts/review-decision-closure/README.md",
            "parts/live-observation-producers/scripts/publish_live_receipts.py",
        ):
            with self.subTest(part_path=part_path):
                self.assertIn(part_path, combined)


if __name__ == "__main__":
    unittest.main()
