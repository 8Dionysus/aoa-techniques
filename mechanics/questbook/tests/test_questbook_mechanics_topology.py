from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]

ACTIVE_QUESTBOOK_SURFACES = (
    "mechanics/questbook/AGENTS.md",
    "mechanics/questbook/README.md",
    "mechanics/questbook/DIRECTION.md",
    "mechanics/questbook/PARTS.md",
    "mechanics/questbook/PROVENANCE.md",
    "mechanics/questbook/LANDING_LOG.md",
    "mechanics/questbook/ROADMAP.md",
    "mechanics/questbook/parts/AGENTS.md",
    "mechanics/questbook/parts/README.md",
)

PART_LOCAL_QUESTBOOK_READMES = (
    "mechanics/questbook/parts/source-index-anchors/README.md",
    "mechanics/questbook/parts/technique-obligation-anchors/README.md",
    "mechanics/questbook/parts/harvest-promotion-anchors/README.md",
)


class QuestbookMechanicsTopologyTestCase(unittest.TestCase):
    def test_questbook_active_surfaces_are_discoverable(self) -> None:
        for relative_path in ACTIVE_QUESTBOOK_SURFACES + PART_LOCAL_QUESTBOOK_READMES:
            with self.subTest(relative_path=relative_path):
                self.assertTrue((REPO_ROOT / relative_path).is_file())

    def test_questbook_part_map_names_all_current_parts(self) -> None:
        parts = (REPO_ROOT / "mechanics" / "questbook" / "PARTS.md").read_text(
            encoding="utf-8"
        )
        provenance = (
            REPO_ROOT / "mechanics" / "questbook" / "PROVENANCE.md"
        ).read_text(encoding="utf-8")

        for part_name in (
            "source-index-anchors",
            "technique-obligation-anchors",
            "harvest-promotion-anchors",
        ):
            with self.subTest(part_name=part_name):
                self.assertIn(part_name, parts)
                self.assertIn(part_name, provenance)

    def test_questbook_is_visible_in_mechanics_map(self) -> None:
        agents = (REPO_ROOT / "mechanics" / "AGENTS.md").read_text(
            encoding="utf-8"
        )
        readme = (REPO_ROOT / "mechanics" / "README.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("questbook", agents)
        self.assertIn("[questbook](questbook/README.md)", readme)
        self.assertIn("canon hardening", readme)

    def test_questbook_stays_outside_direct_orq_lane(self) -> None:
        receipts = (REPO_ROOT / "mechanics" / "REQUEST_RECEIPTS.md").read_text(
            encoding="utf-8"
        )
        direct_section = receipts.split("## Non-ORQ Center Pressure", 1)[0]
        non_orq_section = receipts.split("## Non-ORQ Center Pressure", 1)[1]
        compact_non_orq = " ".join(non_orq_section.split())

        self.assertNotIn("ORQ-QUESTBOOK-TECHNIQUES", direct_section)
        self.assertIn("### [questbook](questbook/README.md)", non_orq_section)
        self.assertIn("Current status: `candidate-only`", non_orq_section)
        self.assertIn(
            "direct `ORQ-QUESTBOOK-TECHNIQUES-*` request",
            compact_non_orq,
        )
        for phrase in (
            "second roadmap",
            "private scratchpad",
            "raw donor backlog",
            "owner acceptance",
            "closure proof",
            "proof verdicts",
            "playbook choreography",
            "memory canon",
            "routing authority",
            "generated quest views as source truth",
            "RPG playable reading authority",
            "automatic technique promotion",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, compact_non_orq)

    def test_source_index_anchors_preserve_source_projection_split(self) -> None:
        anchors = (
            REPO_ROOT
            / "mechanics"
            / "questbook"
            / "parts"
            / "source-index-anchors"
            / "README.md"
        ).read_text(encoding="utf-8")

        for expected in (
            "QUESTBOOK.md",
            "quests/<lane>/<state>/",
            "work_quest_v1",
            "quest_markdown_contract_v1",
            "quest.schema.json",
            "quest_dispatch.schema.json",
            "quest_catalog.min.json",
            "quest_dispatch.min.json",
            "generated quest views as source truth",
            "owner acceptance",
            "automatic technique promotion",
        ):
            with self.subTest(expected=expected):
                self.assertIn(expected, anchors)

    def test_technique_obligation_anchors_point_to_local_homes(self) -> None:
        anchors = (
            REPO_ROOT
            / "mechanics"
            / "questbook"
            / "parts"
            / "technique-obligation-anchors"
            / "README.md"
        ).read_text(encoding="utf-8")

        for expected in (
            "Growth-cycle Questbook Integration",
            "Promotion Readiness Matrix",
            "Distillation Cross-layer Candidate Ledger",
            "Donor Refinery",
            "Technique Feat Model",
            "Promotion Readiness Incubation",
            "aoa-evals",
            "aoa-playbooks",
            "aoa-memo",
            "aoa-sdk",
        ):
            with self.subTest(expected=expected):
                self.assertIn(expected, anchors)

    def test_harvest_promotion_anchors_point_to_bundle_local_homes(self) -> None:
        anchors = (
            REPO_ROOT
            / "mechanics"
            / "questbook"
            / "parts"
            / "harvest-promotion-anchors"
            / "README.md"
        ).read_text(encoding="utf-8")

        for technique_id in (
            "AOA-T-0075",
            "AOA-T-0076",
            "AOA-T-0077",
            "AOA-T-0078",
            "AOA-T-0089",
            "AOA-T-0090",
            "AOA-T-0085",
        ):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, anchors)

        self.assertIn("does not change technique status", anchors)
        self.assertIn("techniques/**/TECHNIQUE.md", anchors)

    def test_questbook_legacy_scaffold_marks_empty_raw_inventory(self) -> None:
        provenance = (
            REPO_ROOT / "mechanics" / "questbook" / "PROVENANCE.md"
        ).read_text(encoding="utf-8")
        compact_provenance = " ".join(provenance.split())
        legacy_dir = REPO_ROOT / "mechanics" / "questbook" / "legacy"
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
                    (REPO_ROOT / "mechanics" / "questbook" / relative_path).is_file()
                )

        self.assertEqual(["README.md"], raw_files)
        self.assertIn("legacy scaffold", provenance)
        self.assertIn("current raw inventory is empty", provenance)
        self.assertIn("no local pre-split Questbook", compact_provenance)

    def test_questbook_stop_lines_remain_explicit(self) -> None:
        direction = (
            REPO_ROOT / "mechanics" / "questbook" / "DIRECTION.md"
        ).read_text(encoding="utf-8")
        roadmap = (REPO_ROOT / "mechanics" / "questbook" / "ROADMAP.md").read_text(
            encoding="utf-8"
        )
        compact_direction = " ".join(direction.split())
        compact_roadmap = " ".join(roadmap.split())

        for phrase in (
            "second roadmap",
            "private scratchpad",
            "raw donor backlog",
            "generated quest views as source truth",
            "closure proof",
            "proof verdicts",
            "playbook choreography",
            "memory canon",
            "routing authority",
            "RPG playable reading authority",
            "owner acceptance",
            "automatic technique promotion",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, compact_direction)
                self.assertIn(phrase, compact_roadmap)

    def test_questbook_package_does_not_move_source_surfaces(self) -> None:
        readme = (REPO_ROOT / "mechanics" / "questbook" / "README.md").read_text(
            encoding="utf-8"
        )
        roadmap = (REPO_ROOT / "mechanics" / "questbook" / "ROADMAP.md").read_text(
            encoding="utf-8"
        )

        self.assertTrue((REPO_ROOT / "QUESTBOOK.md").is_file())
        self.assertTrue(
            (
                REPO_ROOT
                / "quests"
                / "techniques"
                / "captured"
                / "AOA-TECH-Q-0003.yaml"
            ).is_file()
        )
        self.assertTrue((REPO_ROOT / "quests" / "README.md").is_file())
        self.assertTrue((REPO_ROOT / "schemas" / "quest.schema.json").is_file())
        self.assertTrue((REPO_ROOT / "generated" / "quest_catalog.min.json").is_file())
        self.assertIn("Do not move `QUESTBOOK.md`, root `quests/`", roadmap)
        self.assertIn("already-landed local Questbook source", readme)


if __name__ == "__main__":
    unittest.main()
