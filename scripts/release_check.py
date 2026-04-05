from __future__ import annotations

import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


RELEASE_CHECK_COMMAND_SEQUENCE = (
    ("python", "scripts/build_repo_doc_surface_manifest.py"),
    ("python", "scripts/build_catalog.py"),
    ("python", "scripts/build_capsules.py"),
    ("python", "scripts/build_sections.py"),
    ("python", "scripts/build_section_manifest.py"),
    ("python", "scripts/build_checklist_manifest.py"),
    ("python", "scripts/build_example_manifest.py"),
    ("python", "scripts/build_evidence_note_manifest.py"),
    ("python", "scripts/build_github_review_template_manifest.py"),
    ("python", "scripts/build_semantic_review_manifest.py"),
    ("python", "scripts/build_shadow_review_manifest.py"),
    ("python", "scripts/build_kag_export.py"),
    ("python", "-m", "unittest", "discover", "-s", "tests"),
    ("python", "scripts/validate_nested_agents.py"),
    ("python", "scripts/validate_repo.py"),
)
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


def repo_state_changed(before: RepoStateSnapshot, after: RepoStateSnapshot) -> bool:
    return before != after


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    before_state = capture_repo_state(repo_root)

    for command in RELEASE_CHECK_COMMAND_SEQUENCE:
        run_command(command, repo_root)

    after_state = capture_repo_state(repo_root)
    if repo_state_changed(before_state, after_state):
        print("[info] worktree changed during release check; rerunning once to confirm stable outputs")
        for command in RELEASE_CHECK_COMMAND_SEQUENCE:
            run_command(command, repo_root)

        stabilized_state = capture_repo_state(repo_root)
        if repo_state_changed(after_state, stabilized_state):
            print("[error] release check did not stabilize the worktree snapshot", file=sys.stderr)
            print("[after first pass]", file=sys.stderr)
            print(after_state, file=sys.stderr)
            print("[after second pass]", file=sys.stderr)
            print(stabilized_state, file=sys.stderr)
            return 1

    if not before_state.worktree_status.strip():
        run_command(CLEAN_REPO_DIFF_COMMAND, repo_root)

    print("[ok] release check completed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
