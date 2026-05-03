from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

ACTIVE_RPG_SURFACES = (
    "mechanics/rpg/AGENTS.md",
    "mechanics/rpg/README.md",
    "mechanics/rpg/DIRECTION.md",
    "mechanics/rpg/PARTS.md",
    "mechanics/rpg/PROVENANCE.md",
    "mechanics/rpg/LANDING_LOG.md",
    "mechanics/rpg/ROADMAP.md",
    "mechanics/rpg/parts/AGENTS.md",
    "mechanics/rpg/parts/README.md",
)

PART_LOCAL_RPG_READMES = (
    "mechanics/rpg/parts/source-boundary-anchors/README.md",
    "mechanics/rpg/parts/feat-progression-anchors/README.md",
    "mechanics/rpg/parts/quest-overlay-anchors/README.md",
    "mechanics/rpg/parts/owner-handoff-anchors/README.md",
)


class RPGMechanicsTopologyTestCase(unittest.TestCase):
    def test_rpg_active_surfaces_are_discoverable(self) -> None:
        for relative_path in ACTIVE_RPG_SURFACES + PART_LOCAL_RPG_READMES:
            with self.subTest(relative_path=relative_path):
                self.assertTrue((REPO_ROOT / relative_path).is_file())

    def test_rpg_part_map_names_all_current_parts(self) -> None:
        parts = (REPO_ROOT / "mechanics" / "rpg" / "PARTS.md").read_text(
            encoding="utf-8"
        )
        provenance = (REPO_ROOT / "mechanics" / "rpg" / "PROVENANCE.md").read_text(
            encoding="utf-8"
        )

        for part_name in (
            "source-boundary-anchors",
            "feat-progression-anchors",
            "quest-overlay-anchors",
            "owner-handoff-anchors",
        ):
            with self.subTest(part_name=part_name):
                self.assertIn(part_name, parts)
                self.assertIn(part_name, provenance)

    def test_rpg_is_visible_in_mechanics_map(self) -> None:
        agents = (REPO_ROOT / "mechanics" / "AGENTS.md").read_text(
            encoding="utf-8"
        )
        readme = (REPO_ROOT / "mechanics" / "README.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("boundary-bridge, questbook, and RPG", agents)
        self.assertIn("[rpg](rpg/README.md)", readme)
        self.assertIn("quest-overlay", readme)
        self.assertIn("owner-handoff", readme)

    def test_rpg_stays_outside_direct_orq_lane(self) -> None:
        receipts = (REPO_ROOT / "mechanics" / "REQUEST_RECEIPTS.md").read_text(
            encoding="utf-8"
        )
        direct_section = receipts.split("## Non-ORQ Center Pressure", 1)[0]
        non_orq_section = receipts.split("## Non-ORQ Center Pressure", 1)[1]
        compact_non_orq = " ".join(non_orq_section.split())

        self.assertNotIn("ORQ-RPG-TECHNIQUES", direct_section)
        self.assertIn("### [rpg](rpg/README.md)", non_orq_section)
        self.assertIn("Current status: `candidate-only`", non_orq_section)
        self.assertIn("direct `ORQ-RPG-TECHNIQUES-*` request", compact_non_orq)

        for phrase in (
            "hidden ontology",
            "runtime ledger state",
            "role canon",
            "skill truth",
            "playbook choreography",
            "proof verdicts",
            "quest closure",
            "memory canon",
            "chronicle authority",
            "routing authority",
            "owner acceptance",
            "universal scoring",
            "automatic technique promotion",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, compact_non_orq)

    def test_source_boundary_anchors_preserve_owner_truth(self) -> None:
        anchors = (
            REPO_ROOT
            / "mechanics"
            / "rpg"
            / "parts"
            / "source-boundary-anchors"
            / "README.md"
        ).read_text(encoding="utf-8")

        for expected in (
            "AOA-T-0016",
            "AOA-T-0076",
            "AOA-T-0090",
            "mechanics/boundary-bridge/",
            "owner truth",
            "hidden ontology",
            "nearest wrong authority claim",
        ):
            with self.subTest(expected=expected):
                self.assertIn(expected, anchors)

    def test_feat_progression_anchors_stay_reader_only(self) -> None:
        anchors = (
            REPO_ROOT
            / "mechanics"
            / "rpg"
            / "parts"
            / "feat-progression-anchors"
            / "README.md"
        ).read_text(encoding="utf-8")

        for expected in (
            "AOA-T-0084",
            "Technique Feat Model",
            "generated/technique_feat_cards.min.example.json",
            "techniques/**/TECHNIQUE.md",
            "does not change technique status",
            "one universal score",
            "automatic promotion",
        ):
            with self.subTest(expected=expected):
                self.assertIn(expected, anchors)

    def test_quest_overlay_anchors_do_not_take_quest_or_memory_authority(self) -> None:
        anchors = (
            REPO_ROOT
            / "mechanics"
            / "rpg"
            / "parts"
            / "quest-overlay-anchors"
            / "README.md"
        ).read_text(encoding="utf-8")

        for expected in (
            "AOA-T-0085",
            "AOA-T-0089",
            "AOA-T-0078",
            "Questbook",
            "quests/",
            "quest closure",
            "campaign choreography",
            "memory canon",
            "routing authority",
        ):
            with self.subTest(expected=expected):
                self.assertIn(expected, anchors)

    def test_owner_handoff_anchors_name_stronger_owners(self) -> None:
        anchors = (
            REPO_ROOT
            / "mechanics"
            / "rpg"
            / "parts"
            / "owner-handoff-anchors"
            / "README.md"
        ).read_text(encoding="utf-8")

        for expected in (
            "aoa-agents",
            "aoa-skills",
            "aoa-playbooks",
            "aoa-evals",
            "aoa-memo",
            "abyss-stack",
            "aoa-stats",
            "quests/",
            "techniques/**/TECHNIQUE.md",
            "owner acceptance",
        ):
            with self.subTest(expected=expected):
                self.assertIn(expected, anchors)

    def test_rpg_legacy_scaffold_marks_empty_raw_inventory(self) -> None:
        provenance = (REPO_ROOT / "mechanics" / "rpg" / "PROVENANCE.md").read_text(
            encoding="utf-8"
        )
        legacy_dir = REPO_ROOT / "mechanics" / "rpg" / "legacy"
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
                    (REPO_ROOT / "mechanics" / "rpg" / relative_path).is_file()
                )

        self.assertEqual(["README.md"], raw_files)
        self.assertIn("legacy scaffold", provenance)
        self.assertIn("current raw inventory is empty", provenance)
        self.assertIn("no local pre-split RPG", provenance)

    def test_rpg_stop_lines_remain_explicit(self) -> None:
        direction = (REPO_ROOT / "mechanics" / "rpg" / "DIRECTION.md").read_text(
            encoding="utf-8"
        )
        roadmap = (REPO_ROOT / "mechanics" / "rpg" / "ROADMAP.md").read_text(
            encoding="utf-8"
        )
        compact_direction = " ".join(direction.split())
        compact_roadmap = " ".join(roadmap.split())

        for phrase in (
            "hidden ontology",
            "runtime ledger state",
            "role canon",
            "skill execution truth",
            "playbook choreography",
            "proof verdicts",
            "quest closure",
            "memory canon",
            "chronicle authority",
            "routing authority",
            "owner acceptance",
            "universal power score",
            "automatic technique promotion",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, compact_direction)
                self.assertIn(phrase, compact_roadmap)


if __name__ == "__main__":
    unittest.main()
