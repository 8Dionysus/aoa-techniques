#!/usr/bin/env python3
"""Run validation lanes for aoa-techniques CI."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Sequence

try:  # Supports both ``python scripts/ci_gate.py`` and package-style imports.
    from scripts import validation_lanes
except ImportError:  # pragma: no cover - exercised by direct script execution
    import validation_lanes  # type: ignore


REPO_ROOT = Path(__file__).resolve().parents[1]


def resolve_command(command: Sequence[str]) -> tuple[str, ...]:
    if command and command[0] == "python":
        return (sys.executable, *command[1:])
    return tuple(command)


def run_command(command: Sequence[str], repo_root: Path = REPO_ROOT) -> None:
    print(f"[ci-gate] {' '.join(command)}", flush=True)
    subprocess.run(resolve_command(command), cwd=repo_root, check=True)


def capture_command_output(command: Sequence[str], repo_root: Path = REPO_ROOT) -> str:
    result = subprocess.run(
        resolve_command(command),
        cwd=repo_root,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def run_sequence(commands: Sequence[Sequence[str]]) -> None:
    for command in commands:
        run_command(command)


def run_command_groups(groups: Sequence[dict[str, object]]) -> None:
    for group in groups:
        print(f"[ci-gate] generated group: {group['id']}", flush=True)
        run_sequence(group["commands"])  # type: ignore[arg-type]


def run_source_fast() -> None:
    run_sequence(validation_lanes.SOURCE_FAST_COMMAND_SEQUENCE)


def run_generated() -> None:
    before_snapshot = capture_command_output(validation_lanes.GENERATED_DRIFT_SNAPSHOT_COMMAND)
    run_command_groups(validation_lanes.GENERATED_CHECK_COMMAND_GROUPS)
    after_snapshot = capture_command_output(validation_lanes.GENERATED_DRIFT_SNAPSHOT_COMMAND)
    if before_snapshot != after_snapshot:
        print(
            "[ci-gate] generated lane changed generated/read-model drift paths",
            file=sys.stderr,
        )
        raise subprocess.CalledProcessError(
            1,
            validation_lanes.GENERATED_DRIFT_SNAPSHOT_COMMAND,
        )


def run_mechanics_part_local() -> None:
    run_sequence(validation_lanes.MECHANICS_PART_LOCAL_COMMAND_SEQUENCE)


def run_release() -> None:
    run_command(("python", "scripts/release_check.py"))


def run_nightly() -> None:
    run_sequence(validation_lanes.NIGHTLY_COMMAND_SEQUENCE)


def run_advisory() -> None:
    print(
        json.dumps(
            {
                "lane": "advisory",
                "posture": "non_blocking",
                "boundaries": validation_lanes.ADVISORY_BOUNDARIES,
            },
            indent=2,
            sort_keys=True,
        )
    )


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run aoa-techniques validation lanes.")
    parser.add_argument(
        "--mode",
        choices=(
            "source-fast",
            "generated",
            "mechanics-part-local",
            "release",
            "nightly",
            "advisory",
        ),
        required=True,
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        if args.mode == "source-fast":
            run_source_fast()
        elif args.mode == "generated":
            run_generated()
        elif args.mode == "mechanics-part-local":
            run_mechanics_part_local()
        elif args.mode == "release":
            run_release()
        elif args.mode == "nightly":
            run_nightly()
        elif args.mode == "advisory":
            run_advisory()
        else:  # pragma: no cover - argparse enforces choices
            raise ValueError(args.mode)
    except subprocess.CalledProcessError as exc:
        print(f"[ci-gate] command failed with exit code {exc.returncode}", file=sys.stderr)
        return exc.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
