from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]

ACTIVE_RELEASE_SUPPORT_SURFACES = (
    "mechanics/release-support/AGENTS.md",
    "mechanics/release-support/README.md",
    "mechanics/release-support/DIRECTION.md",
    "mechanics/release-support/PARTS.md",
    "mechanics/release-support/PROVENANCE.md",
    "mechanics/release-support/LANDING_LOG.md",
    "mechanics/release-support/ROADMAP.md",
    "mechanics/release-support/parts/AGENTS.md",
    "mechanics/release-support/parts/README.md",
)

PART_LOCAL_RELEASE_SUPPORT_READMES = (
    "mechanics/release-support/parts/installation-techniques/README.md",
    "mechanics/release-support/parts/sovereign-release-techniques/README.md",
)

OLD_FLAT_RELEASE_SUPPORT_FILES = (
    "mechanics/release-support/INSTALLATION_TECHNIQUES.md",
    "mechanics/release-support/SOVEREIGN_RELEASE_TECHNIQUES.md",
)

RELEASE_SUPPORT_CONTRACT_PACKETS = (
    (
        "mechanics/release-support/parts/installation-techniques/schemas/installation_technique_note_v1.json",
        "mechanics/release-support/parts/installation-techniques/examples/installation_technique_note_v1.example.json",
        "schemas/installation_technique_note_v1.json",
        "examples/installation_technique_note_v1.example.json",
    ),
    (
        "mechanics/release-support/parts/sovereign-release-techniques/schemas/sovereign_release_technique_note_v1.json",
        "mechanics/release-support/parts/sovereign-release-techniques/examples/sovereign_release_technique_note_v1.example.json",
        "schemas/sovereign_release_technique_note_v1.json",
        "examples/sovereign_release_technique_note_v1.example.json",
    ),
)


class ReleaseSupportMechanicsTopologyTestCase(unittest.TestCase):
    def test_release_support_active_surfaces_are_discoverable(self) -> None:
        for relative_path in (
            ACTIVE_RELEASE_SUPPORT_SURFACES + PART_LOCAL_RELEASE_SUPPORT_READMES
        ):
            with self.subTest(relative_path=relative_path):
                self.assertTrue((REPO_ROOT / relative_path).is_file())

    def test_release_support_flat_files_moved_into_owning_parts(self) -> None:
        for relative_path in OLD_FLAT_RELEASE_SUPPORT_FILES:
            with self.subTest(relative_path=relative_path):
                self.assertFalse((REPO_ROOT / relative_path).exists())

    def test_release_support_contract_packets_live_under_parts(self) -> None:
        for schema_path, example_path, old_schema_path, old_example_path in (
            RELEASE_SUPPORT_CONTRACT_PACKETS
        ):
            with self.subTest(schema_path=schema_path):
                self.assertTrue((REPO_ROOT / schema_path).is_file())
                self.assertTrue((REPO_ROOT / example_path).is_file())
                self.assertFalse((REPO_ROOT / old_schema_path).exists())
                self.assertFalse((REPO_ROOT / old_example_path).exists())

    def test_release_support_contract_packet_routes_are_documented(self) -> None:
        parts = (
            REPO_ROOT / "mechanics" / "release-support" / "PARTS.md"
        ).read_text(encoding="utf-8")
        provenance = (
            REPO_ROOT / "mechanics" / "release-support" / "PROVENANCE.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "release-support" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")

        self.assertIn("Part-Local Contract Packets", parts)
        self.assertIn("Contract Packet Bridge", provenance)

        for required in (
            "installation_technique_note_v1.json",
            "sovereign_release_technique_note_v1.json",
        ):
            with self.subTest(required=required):
                self.assertIn(required, parts)
                self.assertIn(required, provenance)

        self.assertIn("Contract Packet Part Homes", landing_log)
        self.assertIn("public part-local\n  schema URLs", landing_log)

    def test_release_support_part_map_names_all_current_parts(self) -> None:
        parts = (
            REPO_ROOT / "mechanics" / "release-support" / "PARTS.md"
        ).read_text(encoding="utf-8")
        provenance = (
            REPO_ROOT / "mechanics" / "release-support" / "PROVENANCE.md"
        ).read_text(encoding="utf-8")

        for part_name in (
            "installation-techniques",
            "sovereign-release-techniques",
        ):
            with self.subTest(part_name=part_name):
                self.assertIn(part_name, parts)
                self.assertIn(part_name, provenance)

    def test_release_support_stays_outside_direct_orq_lane(self) -> None:
        receipts = (REPO_ROOT / "mechanics" / "REQUEST_RECEIPTS.md").read_text(
            encoding="utf-8"
        )
        direct_section = receipts.split("## Non-ORQ Center Pressure", 1)[0]
        non_orq_section = receipts.split("## Non-ORQ Center Pressure", 1)[1]

        self.assertNotIn("ORQ-RELEASE-TECHNIQUES", direct_section)
        self.assertIn(
            "### [release-support](release-support/README.md)",
            non_orq_section,
        )
        self.assertIn("Current status: `candidate-only`", non_orq_section)
        self.assertIn(
            "no\n  direct `ORQ-RELEASE-TECHNIQUES-*` request",
            non_orq_section,
        )
        self.assertIn("release authority", non_orq_section)
        self.assertIn("automatic\n  technique promotion", non_orq_section)

    def test_release_support_reference_paths_point_to_part_local_homes(self) -> None:
        old_paths = (
            "mechanics/release-support/INSTALLATION_TECHNIQUES.md",
            "mechanics/release-support/SOVEREIGN_RELEASE_TECHNIQUES.md",
        )
        combined = "\n".join(
            (REPO_ROOT / relative_path).read_text(encoding="utf-8")
            for relative_path in (
                "mechanics/release-support/README.md",
                "mechanics/release-support/DIRECTION.md",
                "mechanics/release-support/PARTS.md",
                "mechanics/release-support/PROVENANCE.md",
                "mechanics/release-support/LANDING_LOG.md",
                "mechanics/release-support/ROADMAP.md",
                "mechanics/release-support/parts/README.md",
                "mechanics/release-support/parts/installation-techniques/README.md",
                "mechanics/release-support/parts/sovereign-release-techniques/README.md",
            )
        )

        for old_path in old_paths:
            with self.subTest(old_path=old_path):
                self.assertNotIn(old_path, combined)

        for part_path in (
            "parts/installation-techniques/README.md",
            "parts/sovereign-release-techniques/README.md",
        ):
            with self.subTest(part_path=part_path):
                self.assertIn(part_path, combined)

    def test_release_support_stop_lines_remain_explicit(self) -> None:
        direction = (
            REPO_ROOT / "mechanics" / "release-support" / "DIRECTION.md"
        ).read_text(encoding="utf-8")
        roadmap = (
            REPO_ROOT / "mechanics" / "release-support" / "ROADMAP.md"
        ).read_text(encoding="utf-8")

        for phrase in (
            "public claim",
            "operator substitution",
            "runtime deployment",
            "rollback execution",
            "Tree-of-Sophia write authority",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, direction)
                self.assertIn(phrase, roadmap)


if __name__ == "__main__":
    unittest.main()
