from __future__ import annotations

import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

try:  # Supports both ``python scripts/release_check.py`` and package-style imports.
    from scripts import validation_lanes
except ImportError:  # pragma: no cover - exercised by direct script execution
    import validation_lanes  # type: ignore

RELEASE_LANE_ID = "release"
WORKTREE_SNAPSHOT_COMMAND = ("git", "status", "--porcelain=v1", "--untracked-files=all")
TRACKED_DIFF_SNAPSHOT_COMMAND = ("git", "diff", "--binary", "--no-ext-diff")
CACHED_DIFF_SNAPSHOT_COMMAND = ("git", "diff", "--cached", "--binary", "--no-ext-diff")
CLEAN_REPO_DIFF_COMMAND = ("git", "diff", "--exit-code")


@dataclass(frozen=True)
class RepoStateSnapshot:
    worktree_status: str
    tracked_diff: str
    cached_diff: str


def resolve_command(command: tuple[str, ...]) -> tuple[str, ...]:
    if command and command[0] == "python":
        return (sys.executable, *command[1:])
    return command


def run_command(command: tuple[str, ...], repo_root: Path) -> None:
    print(f"[run] {' '.join(command)}")
    subprocess.run(resolve_command(command), cwd=repo_root, check=True)


def capture_command_output(command: tuple[str, ...], repo_root: Path) -> str:
    result = subprocess.run(
        command,
        cwd=repo_root,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def capture_repo_state(repo_root: Path) -> RepoStateSnapshot:
    return RepoStateSnapshot(
        worktree_status=capture_command_output(WORKTREE_SNAPSHOT_COMMAND, repo_root),
        tracked_diff=capture_command_output(TRACKED_DIFF_SNAPSHOT_COMMAND, repo_root),
        cached_diff=capture_command_output(CACHED_DIFF_SNAPSHOT_COMMAND, repo_root),
    )


def release_lane_commands() -> tuple[validation_lanes.Command, ...]:
    return validation_lanes.command_sequence_for_lane(RELEASE_LANE_ID)


def normalized_worktree_status(snapshot: RepoStateSnapshot) -> str:
    if snapshot.tracked_diff.strip() or snapshot.cached_diff.strip():
        return snapshot.worktree_status
    return "".join(
        line
        for line in snapshot.worktree_status.splitlines(keepends=True)
        if line.startswith("?? ")
    )


def repo_state_changed(before: RepoStateSnapshot, after: RepoStateSnapshot) -> bool:
    return (
        normalized_worktree_status(before) != normalized_worktree_status(after)
        or before.tracked_diff != after.tracked_diff
        or before.cached_diff != after.cached_diff
    )


def repo_started_without_tracked_diff(snapshot: RepoStateSnapshot) -> bool:
    return not snapshot.tracked_diff.strip() and not snapshot.cached_diff.strip()


def run_release_lane(commands: tuple[validation_lanes.Command, ...], repo_root: Path) -> None:
    for command in commands:
        run_command(command, repo_root)


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    release_commands = release_lane_commands()
    before_state = capture_repo_state(repo_root)

    run_release_lane(release_commands, repo_root)

    after_state = capture_repo_state(repo_root)
    final_state = after_state
    if repo_state_changed(before_state, after_state):
        print("[info] worktree changed during release check; rerunning once to confirm stable outputs")
        run_release_lane(release_commands, repo_root)

        stabilized_state = capture_repo_state(repo_root)
        if repo_state_changed(after_state, stabilized_state):
            print("[error] release check did not stabilize the worktree snapshot", file=sys.stderr)
            print("[after first pass]", file=sys.stderr)
            print(after_state, file=sys.stderr)
            print("[after second pass]", file=sys.stderr)
            print(stabilized_state, file=sys.stderr)
            return 1
        final_state = stabilized_state

    if repo_started_without_tracked_diff(before_state) and repo_state_changed(
        before_state, final_state
    ):
        print(
            "[error] release check changed the worktree snapshot despite starting without tracked diff",
            file=sys.stderr,
        )
        print("[before release check]", file=sys.stderr)
        print(before_state, file=sys.stderr)
        print("[after release check]", file=sys.stderr)
        print(final_state, file=sys.stderr)
        return 1

    if not before_state.worktree_status.strip():
        run_command(CLEAN_REPO_DIFF_COMMAND, repo_root)

    print("[ok] release check completed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
