from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable

from scripts import run_part_local_tests, run_tests, validation_lanes


REPO_ROOT = Path(__file__).resolve().parents[2]
INVENTORY_PATH = REPO_ROOT / "docs" / "testing" / "test_inventory.json"
TEST_TOPOLOGY_PATH = REPO_ROOT / "docs" / "testing" / "TEST_TOPOLOGY.md"
TEST_FILE_PATTERN = "test*.py"
COMMAND_PREFIXES = ("python", "git", "bash", "sh", "pytest", "uv", "make")


def load_inventory() -> dict[str, Any]:
    return json.loads(INVENTORY_PATH.read_text(encoding="utf-8"))


def normalized_inventory_entries() -> list[dict[str, Any]]:
    inventory = load_inventory()
    entries: list[dict[str, Any]] = []
    for home in inventory["homes"]:
        inherited = {
            "home": home["home"],
            "home_scope": home["home_scope"],
            "coverage_authority": home["coverage_authority"],
            "lane": home["lane"],
            "mode": home["mode"],
        }
        for file_entry in home["files"]:
            entries.append({**inherited, **file_entry})
    return entries


def discovered_test_files(repo_root: Path = REPO_ROOT) -> set[str]:
    files: set[str] = set()
    for path in repo_root.rglob(TEST_FILE_PATTERN):
        rel_parts = path.relative_to(repo_root).parts
        if ".git" in rel_parts or "__pycache__" in rel_parts:
            continue
        if path.suffix != ".py":
            continue
        files.add(path.relative_to(repo_root).as_posix())
    return files


def classify_test_home(relative_path: str) -> tuple[str, str]:
    parts = Path(relative_path).parts
    if parts[0] == "tests":
        return "root", "tests"
    if parts[:3] == (".agents", "spark", "tests"):
        return "agent-lane", ".agents/spark/tests"
    if parts[0] == "mechanics":
        test_index = parts.index("tests")
        home = "/".join(parts[: test_index + 1])
        if "parts" in parts[:test_index]:
            return "part-local", home
        return "mechanic-level", home
    raise ValueError(f"{relative_path}: unsupported test home")


def run_tests_homes() -> set[str]:
    return {path.as_posix() for path in run_tests.TEST_DIRS}


def mechanics_part_local_targets() -> set[str]:
    targets: set[str] = set()
    for command in validation_lanes.MECHANICS_PART_LOCAL_COMMAND_SEQUENCE:
        if command == ("python", "scripts/run_part_local_tests.py"):
            targets.update(
                path.relative_to(REPO_ROOT).as_posix()
                for path in run_part_local_tests.discovered_part_local_test_files(REPO_ROOT)
            )
        if tuple(command[:4]) == ("python", "-m", "pytest", "-q"):
            targets.update(arg for arg in command[4:] if arg.endswith(".py"))
    return targets


def mechanics_part_local_builder_checks() -> set[tuple[str, ...]]:
    commands: set[tuple[str, ...]] = set()
    for command in validation_lanes.MECHANICS_PART_LOCAL_COMMAND_SEQUENCE:
        if command == ("python", "scripts/run_part_local_tests.py"):
            commands.update(run_part_local_tests.builder_check_commands(REPO_ROOT))
        elif len(command) == 3 and command[0] == "python" and command[2] == "--check":
            commands.add(command)
    return commands


def mechanics_part_local_validators() -> set[tuple[str, ...]]:
    commands: set[tuple[str, ...]] = set()
    for command in validation_lanes.MECHANICS_PART_LOCAL_COMMAND_SEQUENCE:
        if command == ("python", "scripts/run_part_local_tests.py"):
            commands.update(run_part_local_tests.validator_commands(REPO_ROOT))
        elif (
            len(command) == 2
            and command[0] == "python"
            and "/parts/" in command[1]
            and "/scripts/validate_" in command[1]
        ):
            commands.add(command)
    return commands


def discovered_part_local_test_files() -> set[str]:
    return {
        path.relative_to(REPO_ROOT).as_posix()
        for path in run_part_local_tests.discovered_part_local_test_files(REPO_ROOT)
    }


def release_lane_test_coverage() -> set[str]:
    return covered_test_files(validation_lanes.RELEASE_CHECK_COMMAND_SEQUENCE)


def covered_test_files(commands: Iterable[tuple[str, ...]]) -> set[str]:
    covered: set[str] = set()
    for command in commands:
        if command == ("python", "scripts/run_tests.py"):
            covered.update(files_under_homes(run_tests_homes()))
        elif command == ("python", "scripts/ci_gate.py", "--mode", "mechanics-part-local"):
            covered.update(covered_test_files(validation_lanes.MECHANICS_PART_LOCAL_COMMAND_SEQUENCE))
        elif command == ("python", "scripts/run_part_local_tests.py"):
            covered.update(discovered_part_local_test_files())
        elif tuple(command[:4]) == ("python", "-m", "pytest", "-q"):
            for target in command[4:]:
                covered.update(files_for_target(target))
        elif tuple(command[:4]) == ("python", "-m", "unittest", "discover"):
            if "-s" in command:
                source_dir = command[command.index("-s") + 1]
                covered.update(files_for_target(source_dir))
    return covered


def files_under_homes(homes: Iterable[str]) -> set[str]:
    files: set[str] = set()
    for home in homes:
        files.update(files_for_target(home))
    return files


def files_for_target(target: str) -> set[str]:
    path = REPO_ROOT / target
    if path.is_file():
        return {Path(target).as_posix()}
    if path.is_dir():
        return {
            candidate.relative_to(REPO_ROOT).as_posix()
            for candidate in path.glob(TEST_FILE_PATTERN)
            if candidate.is_file()
        }
    return set()


def looks_like_command(value: str) -> bool:
    return value.strip().split(maxsplit=1)[0] in COMMAND_PREFIXES if value.strip() else False
