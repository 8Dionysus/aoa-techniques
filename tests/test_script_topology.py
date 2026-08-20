from __future__ import annotations

import importlib
import json
import re
import runpy
import subprocess
import sys
import unittest
from contextlib import contextmanager
from pathlib import Path

from scripts import run_part_local_tests, validation_lanes


REPO_ROOT = Path(__file__).resolve().parents[1]
INVENTORY_PATH = REPO_ROOT / "docs" / "validation" / "script_inventory.json"
IGNORED_SCRIPT_SURFACE_PREFIXES = (
    ".deps/",
    "dist/",
    "seeds/",
)

ALLOWED_ORGAN_LANES = {
    "source/topology",
    "projection/generated",
    "capability/security contract",
    "mechanics/part-local",
    "runtime-policy route",
    "trace/eval route",
    "observability/audit",
    "security/adversarial",
    "release/nightly",
    "compatibility adapter",
    "legacy/advisory",
}

ALLOWED_VALIDATION_LANES = {
    "source_fast",
    "generated",
    "mechanics_part_local",
    "release",
    "nightly",
    "advisory",
}

REQUIRED_ENTRY_FIELDS = {
    "path",
    "family",
    "organ_lane",
    "owner_surface",
    "source_truth",
    "reads",
    "writes",
    "side_effects",
    "validation_lane",
    "ci_inclusion",
    "test_target",
    "disposition",
}

CLI_SMOKE_COMMANDS = (
    (".agents/spark/scripts/validate_spark_lane.py", "--help"),
    ("scripts/ci_gate.py", "--help"),
    ("scripts/technique_intelligence.py", "--help"),
)

SCRIPT_REF_RE = re.compile(r"(?<![\w./-])([\w./-]*scripts/[\w./-]+\.py)")


def load_inventory() -> dict:
    return json.loads(INVENTORY_PATH.read_text(encoding="utf-8"))


def inventory_entries() -> list[dict]:
    return load_inventory()["script_surfaces"]


def inventory_paths() -> set[str]:
    return {entry["path"] for entry in inventory_entries()}


def discovered_script_surfaces() -> set[str]:
    return {
        relative
        for path in REPO_ROOT.rglob("*")
        for relative in [path.relative_to(REPO_ROOT).as_posix()]
        if path.is_file()
        and not relative.startswith(IGNORED_SCRIPT_SURFACE_PREFIXES)
        and "/scripts/" in f"/{relative}"
        and "__pycache__" not in path.parts
        and path.suffix != ".pyc"
    }


def command_script_paths(commands: tuple[tuple[str, ...], ...]) -> set[str]:
    paths: set[str] = set()
    for command in commands:
        for part in command:
            if part.endswith(".py") and "/" in part:
                paths.add(part)
    return paths


def all_lane_command_script_paths() -> set[str]:
    commands = (
        validation_lanes.SOURCE_FAST_COMMAND_SEQUENCE
        + validation_lanes.GENERATED_CHECK_COMMAND_SEQUENCE
        + validation_lanes.MECHANICS_PART_LOCAL_COMMAND_SEQUENCE
        + validation_lanes.RELEASE_CHECK_COMMAND_SEQUENCE
        + validation_lanes.NIGHTLY_COMMAND_SEQUENCE
    )
    return command_script_paths(commands)


def resolve_local_script_ref(doc: Path, raw_ref: str) -> str | None:
    raw_ref = raw_ref.removeprefix("./")
    if raw_ref.startswith("../"):
        resolved = (doc.parent / raw_ref).resolve()
        try:
            return resolved.relative_to(REPO_ROOT).as_posix()
        except ValueError:
            return None
    if raw_ref.startswith((".agents/", "mechanics/", "scripts/")):
        return raw_ref
    return None


@contextmanager
def import_path_for(script_path: Path):
    old_path = list(sys.path)
    sys.path.insert(0, str(script_path.parent))
    sys.path.insert(0, str(REPO_ROOT / "scripts"))
    sys.path.insert(0, str(REPO_ROOT))
    try:
        yield
    finally:
        sys.path[:] = old_path


class ScriptTopologyTests(unittest.TestCase):
    def test_script_inventory_covers_every_active_script_surface(self) -> None:
        inventory = load_inventory()
        entries = inventory["script_surfaces"]
        paths = [entry["path"] for entry in entries]

        self.assertEqual("docs/validation/SCRIPT_TOPOLOGY.md", inventory["owner"])
        self.assertEqual("config/validation_lanes.json", inventory["command_authority"])
        self.assertEqual(len(paths), len(set(paths)))
        self.assertEqual(discovered_script_surfaces(), set(paths))

    def test_script_inventory_entries_are_complete_and_owner_routed(self) -> None:
        for entry in inventory_entries():
            with self.subTest(path=entry.get("path")):
                self.assertEqual(REQUIRED_ENTRY_FIELDS, set(entry))
                self.assertIn(entry["organ_lane"], ALLOWED_ORGAN_LANES)
                self.assertIn(entry["validation_lane"], ALLOWED_VALIDATION_LANES)
                self.assertEqual("keep", entry["disposition"])
                self.assertTrue((REPO_ROOT / entry["path"]).is_file())
                self.assertTrue((REPO_ROOT / entry["owner_surface"]).exists())
                self.assertTrue((REPO_ROOT / entry["test_target"]).exists())
                self.assertIsInstance(entry["source_truth"], list)
                self.assertTrue(entry["source_truth"])
                self.assertIsInstance(entry["reads"], list)
                self.assertTrue(entry["reads"])
                self.assertIsInstance(entry["writes"], list)
                self.assertIsInstance(entry["side_effects"], str)
                self.assertTrue(entry["ci_inclusion"])

    def test_lane_commands_reference_inventoried_scripts_not_hidden_commands(self) -> None:
        command_paths = all_lane_command_script_paths()

        self.assertTrue(command_paths)
        self.assertTrue(command_paths <= inventory_paths())

        source_fast_commands = validation_lanes.SOURCE_FAST_COMMAND_SEQUENCE
        source_fast_paths = command_script_paths(source_fast_commands)
        self.assertNotIn("scripts/release_check.py", source_fast_paths)
        self.assertNotIn("scripts/run_tests.py", source_fast_paths)
        self.assertNotIn("scripts/validate_repo.py", source_fast_paths)
        self.assertFalse(
            {
                path
                for path in source_fast_paths
                if Path(path).name.startswith("build_")
            }
        )

    def test_mechanics_part_local_scripts_are_runner_discovered(self) -> None:
        inventory_part_scripts = {
            entry["path"]
            for entry in inventory_entries()
            if entry["family"] in {"part_local_builder", "part_local_validator"}
        }
        runner_part_scripts = command_script_paths(
            run_part_local_tests.builder_check_commands(REPO_ROOT)
            + run_part_local_tests.validator_commands(REPO_ROOT)
        )

        self.assertEqual(inventory_part_scripts, runner_part_scripts)
        self.assertTrue(runner_part_scripts)

    def test_advisory_observation_tools_are_not_hidden_hard_gates(self) -> None:
        hard_gate_paths = all_lane_command_script_paths()

        for entry in inventory_entries():
            path = entry["path"]
            with self.subTest(path=path):
                if path.endswith("publish_live_receipts.py"):
                    self.assertEqual("advisory", entry["validation_lane"])
                    self.assertIn("appends", entry["side_effects"])
                    self.assertNotIn(path, hard_gate_paths)

    def test_side_effect_boundaries_are_visible(self) -> None:
        for entry in inventory_entries():
            path = entry["path"]
            with self.subTest(path=path):
                if entry["writes"]:
                    self.assertNotIn("validation output only", entry["side_effects"])
                    self.assertNotEqual("source_fast", entry["validation_lane"])
                if entry["validation_lane"] == "source_fast":
                    self.assertEqual([], entry["writes"])
                if entry["family"] == "projection_validator_module":
                    self.assertEqual("projection/generated", entry["organ_lane"])
                    self.assertEqual([], entry["writes"])
                    self.assertIn("projection parity", entry["side_effects"])

    def test_python_scripts_import_without_running_main(self) -> None:
        for entry in inventory_entries():
            path = entry["path"]
            if not path.endswith(".py"):
                continue
            script_path = REPO_ROOT / path
            with self.subTest(path=path):
                with import_path_for(script_path):
                    if path.startswith("scripts/validators/"):
                        module_name = path.removesuffix(".py").replace("/", ".")
                        importlib.import_module(module_name)
                    else:
                        runpy.run_path(
                            str(script_path),
                            run_name=f"__script_inventory_smoke__:{path}",
                        )

    def test_safe_cli_smoke_commands_stay_non_mutating(self) -> None:
        for command in CLI_SMOKE_COMMANDS:
            with self.subTest(command=command):
                result = subprocess.run(
                    (sys.executable, *command),
                    cwd=REPO_ROOT,
                    check=False,
                    capture_output=True,
                    text=True,
                    timeout=15,
                )
                self.assertEqual(
                    0,
                    result.returncode,
                    msg=f"stdout={result.stdout}\nstderr={result.stderr}",
                )

    def test_active_route_docs_do_not_reference_missing_scripts(self) -> None:
        docs = [
            *REPO_ROOT.glob("**/AGENTS.md"),
            *(REPO_ROOT / "docs" / "validation").glob("*.md"),
            *(REPO_ROOT / "docs" / "testing").glob("*.md"),
            REPO_ROOT / "docs" / "RELEASING.md",
        ]
        missing: dict[str, list[str]] = {}

        for doc in sorted(set(docs)):
            relative_doc = doc.relative_to(REPO_ROOT).as_posix()
            if "legacy/" in relative_doc or relative_doc.startswith(
                IGNORED_SCRIPT_SURFACE_PREFIXES
            ):
                continue
            text = doc.read_text(encoding="utf-8")
            refs = {
                ref
                for raw_ref in (
                    match.group(1)
                    for match in SCRIPT_REF_RE.finditer(text)
                    if "__pycache__" not in match.group(1)
                )
                if (ref := resolve_local_script_ref(doc, raw_ref)) is not None
            }
            unresolved = sorted(ref for ref in refs if not (REPO_ROOT / ref).is_file())
            if unresolved:
                missing[relative_doc] = unresolved

        self.assertEqual({}, missing)

    def test_no_tracked_python_cache_residue_under_script_surfaces(self) -> None:
        result = subprocess.run(
            ("git", "ls-files", "*__pycache__*", "*.pyc"),
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
            text=True,
        )

        self.assertEqual("", result.stdout.strip())


if __name__ == "__main__":
    unittest.main()
