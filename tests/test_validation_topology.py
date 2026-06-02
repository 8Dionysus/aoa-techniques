from __future__ import annotations

import json
import unittest
from pathlib import Path

from scripts import run_part_local_tests


REPO_ROOT = Path(__file__).resolve().parents[1]
LANES_PATH = REPO_ROOT / "config" / "validation_lanes.json"
INVENTORY_PATH = REPO_ROOT / "docs" / "validation" / "validator_inventory.json"

EXPECTED_LANES = {
    "source_fast",
    "generated",
    "mechanics_part_local",
    "release",
    "nightly",
    "advisory",
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


class ValidationTopologyTests(unittest.TestCase):
    def test_manifest_defines_owner_surface_lanes_without_wholesale_runtime_copy(
        self,
    ) -> None:
        manifest = load_json(LANES_PATH)
        lanes = manifest["lanes"]

        self.assertEqual(EXPECTED_LANES, set(lanes))
        self.assertNotIn("export", lanes)
        self.assertNotIn("runtime", lanes)
        self.assertNotIn("export_full", manifest["command_sequences"])
        self.assertNotIn("runtime_generated_check", manifest["command_sequences"])

        for lane_id in EXPECTED_LANES - {"advisory"}:
            lane = lanes[lane_id]
            with self.subTest(lane=lane_id):
                self.assertEqual("blocking", lane["posture"])
                self.assertIn(lane["command_sequence"], manifest["command_sequences"])

        advisory = lanes["advisory"]
        self.assertEqual("non_blocking", advisory["posture"])
        self.assertNotIn("command_sequence", advisory)
        self.assertIn("boundaries", advisory)
        self.assertIn("export/runtime", {item["surface"] for item in advisory["boundaries"]})

        release_commands = {
            tuple(command) for command in manifest["command_sequences"]["release_check"]
        }
        self.assertIn(
            ("python", "scripts/ci_gate.py", "--mode", "mechanics-part-local"),
            release_commands,
        )

    def test_validator_inventory_matches_manifest_lanes(self) -> None:
        manifest = load_json(LANES_PATH)
        inventory = load_json(INVENTORY_PATH)
        inventory_lanes = {lane["id"]: lane for lane in inventory["lanes"]}

        self.assertEqual(EXPECTED_LANES, set(inventory_lanes))
        self.assertEqual("config/validation_lanes.json", inventory["command_authority"])

        for lane_id, lane in manifest["lanes"].items():
            with self.subTest(lane=lane_id):
                inventory_lane = inventory_lanes[lane_id]
                self.assertEqual(lane["label"], inventory_lane["label"])
                expected_mode = "non_blocking" if lane["posture"] == "non_blocking" else "blocking"
                self.assertEqual(expected_mode, inventory_lane["mode"])
                if lane["posture"] == "blocking":
                    self.assertEqual(
                        lane["command_sequence"],
                        inventory_lane["command_sequence"],
                    )
                self.assertIn("failure_route", inventory_lane)

    def test_validation_docs_name_all_lanes_and_owner_boundaries(self) -> None:
        topology = (REPO_ROOT / "docs" / "validation" / "VALIDATOR_TOPOLOGY.md").read_text(
            encoding="utf-8"
        )
        authority = (REPO_ROOT / "docs" / "validation" / "COMMAND_AUTHORITY.md").read_text(
            encoding="utf-8"
        )

        for label in (
            "source-fast",
            "generated",
            "mechanics/part-local",
            "release",
            "nightly",
            "advisory",
        ):
            with self.subTest(label=label):
                self.assertIn(label, topology)
                self.assertIn(label, authority)

        self.assertIn("Do not copy `aoa-skills` export/runtime lanes wholesale", topology)
        self.assertIn("does not own skill portable export", topology)
        self.assertIn("eval verdict layer", topology)
        self.assertIn("runtime policy engine", topology)

    def test_mechanics_part_local_lane_covers_discovered_part_tests(self) -> None:
        manifest = load_json(LANES_PATH)
        mechanics_sequence = {
            tuple(command) for command in manifest["command_sequences"]["mechanics_part_local"]
        }

        discovered = sorted(
            path.relative_to(REPO_ROOT).as_posix()
            for path in REPO_ROOT.glob("mechanics/*/parts/*/tests/test*.py")
        )
        self.assertGreater(len(discovered), 0)
        self.assertIn(("python", "scripts/run_part_local_tests.py"), mechanics_sequence)
        self.assertEqual(
            discovered,
            [
                path.relative_to(REPO_ROOT).as_posix()
                for path in run_part_local_tests.discovered_part_local_test_files(REPO_ROOT)
            ],
        )
        self.assertEqual(
            {
                self._part_home_for_test(relative_path)
                for relative_path in discovered
            },
            {
                self._part_home_for_script(command[1])
                for command in run_part_local_tests.builder_check_commands(REPO_ROOT)
            },
        )
        self.assertEqual(
            {
                self._part_home_for_test(relative_path)
                for relative_path in discovered
            },
            {
                self._part_home_for_script(command[1])
                for command in run_part_local_tests.validator_commands(REPO_ROOT)
            },
        )

    @staticmethod
    def _part_home_for_test(relative_path: str) -> str:
        parts = Path(relative_path).parts
        return "/".join(parts[: parts.index("tests")])

    @staticmethod
    def _part_home_for_script(relative_path: str) -> str:
        parts = Path(relative_path).parts
        return "/".join(parts[: parts.index("scripts")])

    def test_docs_validation_district_is_indexed_and_agent_mesh_registered(self) -> None:
        current_surface_index = (
            REPO_ROOT / "docs" / "guardrails" / "CURRENT_SURFACE_INDEX.md"
        ).read_text(encoding="utf-8")
        thematic_protocol = (
            REPO_ROOT / "docs" / "guardrails" / "THEMATIC_DISTRICT_PROTOCOL.md"
        ).read_text(encoding="utf-8")
        agents_mesh = load_json(REPO_ROOT / "config" / "agents_mesh.json")

        self.assertIn("docs/validation/", current_surface_index)
        self.assertIn("docs/validation/", thematic_protocol)
        self.assertIn(
            "docs/validation/AGENTS.md",
            agents_mesh["canonical_cards"],
        )


if __name__ == "__main__":
    unittest.main()
