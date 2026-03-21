from __future__ import annotations

import subprocess
import sys
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
    ("python", "-m", "unittest", "discover", "-s", "tests"),
    ("python", "scripts/validate_repo.py"),
)
WORKTREE_SNAPSHOT_COMMAND = ("git", "status", "--porcelain=v1", "--untracked-files=all")
CLEAN_REPO_DIFF_COMMAND = ("git", "diff", "--exit-code")


def resolve_command(command: tuple[str, ...]) -> tuple[str, ...]:
    if command and command[0] == "python":
        return (sys.executable, *command[1:])
    return command


def run_command(command: tuple[str, ...], repo_root: Path) -> None:
    print(f"[run] {' '.join(command)}")
    subprocess.run(resolve_command(command), cwd=repo_root, check=True)


def capture_worktree_snapshot(repo_root: Path) -> str:
    result = subprocess.run(
        WORKTREE_SNAPSHOT_COMMAND,
        cwd=repo_root,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    before_snapshot = capture_worktree_snapshot(repo_root)

    for command in RELEASE_CHECK_COMMAND_SEQUENCE:
        run_command(command, repo_root)

    after_snapshot = capture_worktree_snapshot(repo_root)
    if after_snapshot != before_snapshot:
        print("[info] worktree changed during release check; rerunning once to confirm stable outputs")
        for command in RELEASE_CHECK_COMMAND_SEQUENCE:
            run_command(command, repo_root)

        stabilized_snapshot = capture_worktree_snapshot(repo_root)
        if stabilized_snapshot != after_snapshot:
            print("[error] release check did not stabilize the worktree snapshot", file=sys.stderr)
            print("[after first pass]", file=sys.stderr)
            print(after_snapshot or "<clean>", file=sys.stderr)
            print("[after second pass]", file=sys.stderr)
            print(stabilized_snapshot or "<clean>", file=sys.stderr)
            return 1
        after_snapshot = stabilized_snapshot

    if not before_snapshot.strip():
        run_command(CLEAN_REPO_DIFF_COMMAND, repo_root)

    print("[ok] release check completed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
