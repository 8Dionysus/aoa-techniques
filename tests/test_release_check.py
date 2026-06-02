from __future__ import annotations

import unittest
from contextlib import redirect_stderr
from io import StringIO
from unittest.mock import patch

from scripts import release_check


class ReleaseCheckStabilizerTests(unittest.TestCase):
    def test_release_lane_commands_resolve_release_lane_from_loader(self) -> None:
        commands = (("python", "scripts/example.py"),)

        with patch.object(
            release_check.validation_lanes,
            "command_sequence_for_lane",
            return_value=commands,
        ) as command_sequence_for_lane:
            self.assertEqual(commands, release_check.release_lane_commands())

        command_sequence_for_lane.assert_called_once_with("release")

    def test_repo_state_ignores_status_only_tracked_marker_without_diff(self) -> None:
        before = release_check.RepoStateSnapshot("", "", "")
        status_only = release_check.RepoStateSnapshot(" M generated/file.json\n", "", "")
        untracked = release_check.RepoStateSnapshot("?? generated/tmp.json\n", "", "")
        tracked = release_check.RepoStateSnapshot(" M generated/file.json\n", "diff", "")

        self.assertFalse(release_check.repo_state_changed(before, status_only))
        self.assertTrue(release_check.repo_state_changed(before, untracked))
        self.assertTrue(release_check.repo_state_changed(before, tracked))

    def test_repo_started_without_tracked_diff_allows_existing_untracked_files(self) -> None:
        untracked_only = release_check.RepoStateSnapshot("?? seed.zip\n", "", "")
        dirty_tracked = release_check.RepoStateSnapshot(" M generated/file.json\n", "diff", "")
        dirty_cached = release_check.RepoStateSnapshot("M  generated/file.json\n", "", "diff")

        self.assertTrue(release_check.repo_started_without_tracked_diff(untracked_only))
        self.assertFalse(release_check.repo_started_without_tracked_diff(dirty_tracked))
        self.assertFalse(release_check.repo_started_without_tracked_diff(dirty_cached))

    def test_main_runs_release_lane_and_clean_diff_check_when_initially_clean(self) -> None:
        commands = (("python", "scripts/example.py"), ("git", "status"))
        before = release_check.RepoStateSnapshot("", "", "")
        after = release_check.RepoStateSnapshot("", "", "")
        calls: list[tuple[str, ...]] = []

        def fake_run(command: tuple[str, ...], repo_root: object) -> None:
            calls.append(command)

        with (
            patch.object(release_check, "release_lane_commands", return_value=commands),
            patch.object(release_check, "capture_repo_state", side_effect=[before, after]),
            patch.object(release_check, "run_command", side_effect=fake_run),
        ):
            self.assertEqual(0, release_check.main())

        self.assertEqual([*commands, release_check.CLEAN_REPO_DIFF_COMMAND], calls)

    def test_main_does_not_run_clean_diff_check_when_initially_dirty(self) -> None:
        commands = (("python", "scripts/example.py"),)
        before = release_check.RepoStateSnapshot(" M file\n", "tracked-a", "")
        after = release_check.RepoStateSnapshot(" M file\n", "tracked-a", "")
        calls: list[tuple[str, ...]] = []

        def fake_run(command: tuple[str, ...], repo_root: object) -> None:
            calls.append(command)

        with (
            patch.object(release_check, "release_lane_commands", return_value=commands),
            patch.object(release_check, "capture_repo_state", side_effect=[before, after]),
            patch.object(release_check, "run_command", side_effect=fake_run),
        ):
            self.assertEqual(0, release_check.main())

        self.assertEqual([*commands], calls)

    def test_main_reruns_once_when_worktree_changes_then_stabilizes(self) -> None:
        commands = (("python", "scripts/example.py"), ("python", "scripts/other.py"))
        before = release_check.RepoStateSnapshot(" M file\n", "tracked-a", "")
        after_first = release_check.RepoStateSnapshot(" M file\n", "tracked-b", "")
        after_second = release_check.RepoStateSnapshot(" M file\n", "tracked-b", "")
        calls: list[tuple[str, ...]] = []

        def fake_run(command: tuple[str, ...], repo_root: object) -> None:
            calls.append(command)

        with (
            patch.object(release_check, "release_lane_commands", return_value=commands),
            patch.object(
                release_check,
                "capture_repo_state",
                side_effect=[before, after_first, after_second],
            ),
            patch.object(release_check, "run_command", side_effect=fake_run),
        ):
            self.assertEqual(0, release_check.main())

        self.assertEqual([*commands, *commands], calls)

    def test_main_fails_when_second_pass_does_not_stabilize(self) -> None:
        commands = (("python", "scripts/example.py"),)
        before = release_check.RepoStateSnapshot(" M file\n", "tracked-a", "")
        after_first = release_check.RepoStateSnapshot(" M file\n", "tracked-b", "")
        after_second = release_check.RepoStateSnapshot(" M file\n", "tracked-c", "")

        with (
            patch.object(release_check, "release_lane_commands", return_value=commands),
            patch.object(
                release_check,
                "capture_repo_state",
                side_effect=[before, after_first, after_second],
            ),
            patch.object(release_check, "run_command"),
            redirect_stderr(StringIO()) as stderr,
        ):
            self.assertEqual(1, release_check.main())

        self.assertIn("release check did not stabilize the worktree snapshot", stderr.getvalue())

    def test_main_fails_when_initially_clean_release_lane_creates_stable_drift(self) -> None:
        commands = (("python", "scripts/example.py"),)
        before = release_check.RepoStateSnapshot("", "", "")
        after_first = release_check.RepoStateSnapshot("?? generated/tmp.json\n", "", "")
        after_second = release_check.RepoStateSnapshot("?? generated/tmp.json\n", "", "")

        with (
            patch.object(release_check, "release_lane_commands", return_value=commands),
            patch.object(
                release_check,
                "capture_repo_state",
                side_effect=[before, after_first, after_second],
            ),
            patch.object(release_check, "run_command"),
            redirect_stderr(StringIO()) as stderr,
        ):
            self.assertEqual(1, release_check.main())

        self.assertIn(
            "release check changed the worktree snapshot despite starting without tracked diff",
            stderr.getvalue(),
        )


if __name__ == "__main__":
    unittest.main()
