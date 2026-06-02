from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[1]
PART_LOCAL_TEST_GLOB = "mechanics/*/parts/*/tests/test*.py"


def discovered_part_local_test_files(repo_root: Path = REPO_ROOT) -> tuple[Path, ...]:
    return tuple(sorted(repo_root.glob(PART_LOCAL_TEST_GLOB)))


def part_home_for_test(test_path: Path) -> Path:
    parts = test_path.parts
    test_index = parts.index("tests")
    return Path(*parts[:test_index])


def discovered_part_homes(repo_root: Path = REPO_ROOT) -> tuple[Path, ...]:
    homes = {
        part_home_for_test(path.relative_to(repo_root))
        for path in discovered_part_local_test_files(repo_root)
    }
    return tuple(sorted(homes))


def builder_check_commands(repo_root: Path = REPO_ROOT) -> tuple[tuple[str, ...], ...]:
    commands: list[tuple[str, ...]] = []
    for home in discovered_part_homes(repo_root):
        for script_path in sorted((repo_root / home / "scripts").glob("build_*.py")):
            commands.append(("python", script_path.relative_to(repo_root).as_posix(), "--check"))
    return tuple(commands)


def validator_commands(repo_root: Path = REPO_ROOT) -> tuple[tuple[str, ...], ...]:
    commands: list[tuple[str, ...]] = []
    for home in discovered_part_homes(repo_root):
        for script_path in sorted((repo_root / home / "scripts").glob("validate_*.py")):
            commands.append(("python", script_path.relative_to(repo_root).as_posix()))
    return tuple(commands)


def pytest_command(repo_root: Path = REPO_ROOT) -> tuple[str, ...]:
    test_files = tuple(
        path.relative_to(repo_root).as_posix()
        for path in discovered_part_local_test_files(repo_root)
    )
    if not test_files:
        return ()
    return ("python", "-m", "pytest", "-q", *test_files)


def coverage_commands(repo_root: Path = REPO_ROOT) -> tuple[tuple[str, ...], ...]:
    commands: list[tuple[str, ...]] = []
    pytest = pytest_command(repo_root)
    if pytest:
        commands.append(pytest)
    commands.extend(builder_check_commands(repo_root))
    commands.extend(validator_commands(repo_root))
    return tuple(commands)


def resolve_command(command: tuple[str, ...]) -> tuple[str, ...]:
    if command and command[0] == "python":
        return (sys.executable, *command[1:])
    return command


def run_commands(commands: Iterable[tuple[str, ...]], repo_root: Path = REPO_ROOT) -> int:
    ran = 0
    for command in commands:
        print(f"[part-local] {' '.join(command)}", flush=True)
        subprocess.run(resolve_command(command), cwd=repo_root, check=True)
        ran += 1
    return ran


def main() -> int:
    test_files = discovered_part_local_test_files(REPO_ROOT)
    if not test_files:
        print("[error] no part-local pytest files were discovered", file=sys.stderr)
        return 1

    commands = coverage_commands(REPO_ROOT)
    if not builder_check_commands(REPO_ROOT):
        print("[error] no part-local builder --check commands were discovered", file=sys.stderr)
        return 1

    run_commands(commands, REPO_ROOT)
    print(f"[ok] completed part-local pytest and builder/validator coverage across {len(test_files)} test files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
