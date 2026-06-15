from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SUPPORT_DIR = REPO_ROOT / "tests" / "support"
if str(SUPPORT_DIR) not in sys.path:
    sys.path.insert(0, str(SUPPORT_DIR))

import topology_inventory
from scripts import validation_lanes


REQUIRED_NORMALIZED_FIELDS = {
    "path",
    "home",
    "home_scope",
    "family",
    "protects",
    "owner_surface",
    "coverage_authority",
    "lane",
    "mode",
    "runtime_cost",
    "focused_target",
    "failure_route",
}
HOME_SCOPES = {"root", "mechanic-level", "part-local", "agent-lane"}
LANES = {"root-tests", "mechanic-tests", "mechanics-part-local", "spark-agent"}
MODES = {"blocking", "release-only"}
RUNTIME_COSTS = {"fast", "medium", "slow"}
VALIDATE_REPO_OWNER_TEST_FILES = {
    "tests/test_validate_repo_agents_mesh.py",
    "tests/test_validate_repo_ci_release_authority.py",
    "tests/test_validate_repo_compatibility_imports.py",
    "tests/test_validate_repo_generated_drift.py",
    "tests/test_validate_repo_public_hygiene.py",
    "tests/test_validate_repo_questbook_intelligence.py",
    "tests/test_validate_repo_source_contracts.py",
}
DISTILLATION_TOPOLOGY_TEST_FILES = {
    "mechanics/distillation/tests/test_distillation_gate_decisions.py",
    "mechanics/distillation/tests/test_distillation_package_surfaces.py",
    "mechanics/distillation/tests/test_distillation_part_ledgers_handoff.py",
    "mechanics/distillation/tests/test_distillation_reform_ingress_reviews.py",
    "mechanics/distillation/tests/test_distillation_tree_pilot_automation_closeout.py",
    "mechanics/distillation/tests/test_distillation_tree_pilot_capability_wave.py",
    "mechanics/distillation/tests/test_distillation_tree_pilot_history_wave.py",
    "mechanics/distillation/tests/test_distillation_tree_pilot_ingress_wave.py",
    "mechanics/distillation/tests/test_distillation_tree_pilot_runtime_wave.py",
}


class TestTopologyAuthorityTests(unittest.TestCase):
    def test_topology_doc_names_test_home_boundaries(self) -> None:
        text = topology_inventory.TEST_TOPOLOGY_PATH.read_text(encoding="utf-8")
        for required in (
            "root",
            "mechanic-level",
            "part-local",
            "agent-lane",
            "family -> protects -> owner surface -> home scope -> coverage authority",
            "Test files are not command authority.",
            "Blocking command sequences live in",
            "`config/validation_lanes.json`",
            "`scripts/run_tests.py` owns unittest discovery homes",
        ):
            self.assertIn(required, text)

    def test_inventory_covers_every_source_test_file(self) -> None:
        entries = topology_inventory.normalized_inventory_entries()
        inventory_paths = [entry["path"] for entry in entries]

        self.assertEqual(len(inventory_paths), len(set(inventory_paths)))
        self.assertEqual(topology_inventory.discovered_test_files(), set(inventory_paths))

        for entry in entries:
            with self.subTest(path=entry["path"]):
                self.assertTrue(REQUIRED_NORMALIZED_FIELDS.issubset(entry))
                self.assertTrue((REPO_ROOT / entry["path"]).is_file())
                self.assertIn(entry["home_scope"], HOME_SCOPES)
                self.assertIn(entry["lane"], LANES)
                self.assertIn(entry["mode"], MODES)
                self.assertIn(entry["runtime_cost"], RUNTIME_COSTS)
                self.assertFalse(topology_inventory.looks_like_command(entry["focused_target"]))
                self.assertFalse(topology_inventory.looks_like_command(entry["coverage_authority"]))
                self.assertNotIn("command", entry)

    def test_inventory_home_scopes_match_filesystem_topology(self) -> None:
        for entry in topology_inventory.normalized_inventory_entries():
            expected_scope, expected_home = topology_inventory.classify_test_home(entry["path"])
            with self.subTest(path=entry["path"]):
                self.assertEqual(expected_scope, entry["home_scope"])
                self.assertEqual(expected_home, entry["home"])
                self.assertTrue(entry["path"].startswith(f"{entry['home']}/"))

    def test_validate_repo_monolith_is_split_by_owner_surface(self) -> None:
        inventory_paths = {
            entry["path"] for entry in topology_inventory.normalized_inventory_entries()
        }

        self.assertFalse((REPO_ROOT / "tests" / "test_validate_repo.py").exists())
        self.assertTrue(VALIDATE_REPO_OWNER_TEST_FILES <= inventory_paths)
        for relative_path in VALIDATE_REPO_OWNER_TEST_FILES:
            with self.subTest(path=relative_path):
                path = REPO_ROOT / relative_path
                self.assertTrue(path.is_file())
                self.assertLess(len(path.read_text(encoding="utf-8").splitlines()), 1800)

    def test_distillation_topology_monolith_is_split_by_owner_surface(self) -> None:
        entries = {
            entry["path"]: entry for entry in topology_inventory.normalized_inventory_entries()
        }

        self.assertFalse(
            (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "tests"
                / "test_distillation_mechanics_topology.py"
            ).exists()
        )
        self.assertTrue(DISTILLATION_TOPOLOGY_TEST_FILES <= set(entries))
        test_count = 0
        for relative_path in DISTILLATION_TOPOLOGY_TEST_FILES:
            with self.subTest(path=relative_path):
                path = REPO_ROOT / relative_path
                text = path.read_text(encoding="utf-8")
                entry = entries[relative_path]

                self.assertTrue(path.is_file())
                self.assertLess(len(text.splitlines()), 2400)
                self.assertEqual(relative_path, entry["focused_target"])
                self.assertIn("mechanics/distillation", entry["owner_surface"])
                self.assertIn("Fix ", entry["failure_route"])
                test_count += text.count("    def test_")
        self.assertEqual(116, test_count)

    def test_run_tests_covers_root_and_mechanic_level_homes(self) -> None:
        entries = topology_inventory.normalized_inventory_entries()
        expected_homes = {
            entry["home"]
            for entry in entries
            if entry["home_scope"] in {"root", "mechanic-level"}
        }

        self.assertTrue(expected_homes)
        self.assertTrue(expected_homes <= topology_inventory.run_tests_homes())

    def test_lane_system_covers_part_local_and_agent_lane_tests(self) -> None:
        entries = topology_inventory.normalized_inventory_entries()
        part_local_paths = {
            entry["path"] for entry in entries if entry["home_scope"] == "part-local"
        }
        agent_lane_paths = {
            entry["path"] for entry in entries if entry["home_scope"] == "agent-lane"
        }

        self.assertEqual(part_local_paths, topology_inventory.mechanics_part_local_targets())
        self.assertTrue(agent_lane_paths <= topology_inventory.release_lane_test_coverage())

    def test_part_local_lane_covers_related_builder_checks_and_validators(self) -> None:
        entries = topology_inventory.normalized_inventory_entries()
        part_local_homes = {
            self.part_root_from_test_home(entry["home"])
            for entry in entries
            if entry["home_scope"] == "part-local"
        }
        builder_homes = {
            self.home_from_part_local_script(command[1])
            for command in topology_inventory.mechanics_part_local_builder_checks()
        }
        validator_homes = {
            self.home_from_part_local_script(command[1])
            for command in topology_inventory.mechanics_part_local_validators()
        }

        self.assertEqual(part_local_homes, builder_homes)
        self.assertEqual(part_local_homes, validator_homes)

    def test_release_lane_covers_all_inventory_test_files(self) -> None:
        inventory_paths = {
            entry["path"] for entry in topology_inventory.normalized_inventory_entries()
        }
        self.assertTrue(inventory_paths <= topology_inventory.release_lane_test_coverage())

    def test_test_topology_does_not_duplicate_release_command_authority(self) -> None:
        inventory = topology_inventory.load_inventory()
        inventory_text = json.dumps(inventory, sort_keys=True)
        topology_text = topology_inventory.TEST_TOPOLOGY_PATH.read_text(encoding="utf-8")

        self.assertEqual("config/validation_lanes.json", inventory["command_authority"])
        self.assertEqual("scripts/run_tests.py", inventory["runner_authority"])
        self.assertNotIn("command_sequence", inventory_text)
        self.assertNotIn("python ", inventory_text)
        self.assertNotIn("python ", topology_text)

    def test_tests_do_not_store_release_command_sequence(self) -> None:
        release_command_strings = {
            " ".join(command)
            for command in validation_lanes.RELEASE_CHECK_COMMAND_SEQUENCE
        }
        allowed_authority_tests = {
            "tests/test_release_check.py",
            "tests/test_test_topology.py",
            "tests/test_validate_repo_ci_release_authority.py",
            "tests/test_validate_repo_generated_drift.py",
            "tests/test_validation_command_authority.py",
        }
        offenders: list[tuple[str, int]] = []

        for relative_path in sorted(topology_inventory.discovered_test_files()):
            if relative_path in allowed_authority_tests:
                continue
            text = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
            match_count = sum(command in text for command in release_command_strings)
            if match_count >= 3:
                offenders.append((relative_path, match_count))

        self.assertEqual([], offenders)

    @staticmethod
    def home_from_part_local_script(relative_path: str) -> str:
        parts = Path(relative_path).parts
        scripts_index = parts.index("scripts")
        return "/".join(parts[:scripts_index])

    @staticmethod
    def part_root_from_test_home(relative_path: str) -> str:
        parts = Path(relative_path).parts
        tests_index = parts.index("tests")
        return "/".join(parts[:tests_index])


if __name__ == "__main__":
    unittest.main()
