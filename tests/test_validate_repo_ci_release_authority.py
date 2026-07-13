from __future__ import annotations

import sys
from pathlib import Path

SUPPORT_DIR = Path(__file__).resolve().parent / "support"
if str(SUPPORT_DIR) not in sys.path:
    sys.path.insert(0, str(SUPPORT_DIR))

from validate_repo_fixtures import *


class ValidateRepoCiReleaseAuthorityTests(unittest.TestCase):
    def test_repo_validation_workflow_uses_source_fast_lane_entrypoint(self) -> None:
        workflow = (REPO_ROOT / ".github" / "workflows" / "repo-validation.yml").read_text(
            encoding="utf-8"
        )

        self.assertIn("python scripts/ci_gate.py --mode source-fast", workflow)
        self.assertIn("python scripts/ci_gate.py --mode generated", workflow)
        self.assertNotIn("python scripts/release_check.py", workflow)
        self.assertNotIn("python scripts/run_tests.py", workflow)
        self.assertNotIn("python scripts/validate_repo.py", workflow)
        self.assertNotIn("python scripts/build_catalog.py", workflow)
        self.assertNotIn("python scripts/build_shadow_review_manifest.py", workflow)
        self.assertNotIn("python scripts/validate_nested_agents.py", workflow)

    def test_release_check_sequence_is_loaded_from_validation_lanes(self) -> None:
        release_check_text = (REPO_ROOT / "scripts" / "release_check.py").read_text(
            encoding="utf-8"
        )

        self.assertEqual(
            validation_lanes.command_sequence_for_lane("release"),
            release_check.release_lane_commands(),
        )
        self.assertNotIn("RELEASE_CHECK_COMMAND_SEQUENCE", release_check_text)
        self.assertNotIn('("python", "scripts/build_catalog.py")', release_check_text)
        self.assertEqual(
            ("git", "status", "--porcelain=v1", "--untracked-files=all"),
            release_check.WORKTREE_SNAPSHOT_COMMAND,
        )
        self.assertEqual(
            ("git", "diff", "--binary", "--no-ext-diff"),
            release_check.TRACKED_DIFF_SNAPSHOT_COMMAND,
        )
        self.assertEqual(
            ("git", "diff", "--cached", "--binary", "--no-ext-diff"),
            release_check.CACHED_DIFF_SNAPSHOT_COMMAND,
        )
        self.assertEqual(("git", "diff", "--exit-code"), release_check.CLEAN_REPO_DIFF_COMMAND)

    def test_release_check_repo_state_detects_tracked_diff_changes_without_status_drift(self) -> None:
        before = release_check.RepoStateSnapshot(
            worktree_status=" M docs/readers/selection/TECHNIQUE_SELECTION.md\n",
            tracked_diff="diff --git a/docs/readers/selection/TECHNIQUE_SELECTION.md b/docs/readers/selection/TECHNIQUE_SELECTION.md\n-old\n+new\n",
            cached_diff="",
        )
        after = release_check.RepoStateSnapshot(
            worktree_status=" M docs/readers/selection/TECHNIQUE_SELECTION.md\n",
            tracked_diff="diff --git a/docs/readers/selection/TECHNIQUE_SELECTION.md b/docs/readers/selection/TECHNIQUE_SELECTION.md\n-older\n+newer\n",
            cached_diff="",
        )

        self.assertTrue(release_check.repo_state_changed(before, after))

    def test_codeowners_is_present_and_scoped_narrowly(self) -> None:
        codeowners = (REPO_ROOT / ".github" / "CODEOWNERS").read_text(encoding="utf-8")
        contributing = (REPO_ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")

        for target in (
            "/.github/ @8Dionysus",
            "/scripts/ @8Dionysus",
            "/stats/ @8Dionysus",
            "/docs/ @8Dionysus",
            "/techniques/ @8Dionysus",
        ):
            self.assertIn(target, codeowners)

        self.assertIn("CODEOWNERS", contributing)

    def test_external_import_and_pr_templates_capture_overlap_and_generated_surface_fields(
        self,
    ) -> None:
        external_import = (
            REPO_ROOT / ".github" / "ISSUE_TEMPLATE" / "external-import-review.md"
        ).read_text(encoding="utf-8")
        technique_proposal = (
            REPO_ROOT / ".github" / "ISSUE_TEMPLATE" / "technique-proposal.md"
        ).read_text(encoding="utf-8")
        pr_template = (REPO_ROOT / ".github" / "PULL_REQUEST_TEMPLATE.md").read_text(
            encoding="utf-8"
        )
        external_origin = (REPO_ROOT / "templates" / "EXTERNAL_ORIGIN.template.md").read_text(
            encoding="utf-8"
        )

        for text in (
            external_import,
            technique_proposal,
            pr_template,
        ):
            self.assertIn("generated surfaces", text)
            self.assertIn("downstream repo impact", text)

        self.assertIn("nearest existing technique or overlap watch", external_import)
        self.assertIn("what stays out of the donor", external_import)
        self.assertIn("nearest existing technique or overlap watch", technique_proposal)
        self.assertIn("what stays out of scope", technique_proposal)
        self.assertIn("what stays out of the donor", pr_template)
        self.assertIn("overlap", pr_template)
        self.assertIn("reusable object extracted", external_origin)
        self.assertIn("what stays out of the donor", external_origin)

    def test_pull_request_template_path_stays_uppercase_only(self) -> None:
        canonical_template = REPO_ROOT / ".github" / "PULL_REQUEST_TEMPLATE.md"
        lowercase_template = REPO_ROOT / ".github" / "pull_request_template.md"
        duplicate_relative_path = Path(".github") / "pull_request_template.md"

        self.assertTrue(canonical_template.is_file())
        self.assertFalse(lowercase_template.exists())
        self.assertTrue(
            validate_repo.path_exists_with_exact_case(
                REPO_ROOT, Path(".github") / "PULL_REQUEST_TEMPLATE.md"
            )
        )
        self.assertFalse(
            validate_repo.path_exists_with_exact_case(
                REPO_ROOT, Path(".github") / "pull_request_template.md"
            )
        )

        with TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            shutil.copytree(REPO_ROOT / ".github", temp_root / ".github")
            self.assertTrue(
                validate_repo.path_exists_with_exact_case(
                    temp_root, Path(".github") / "PULL_REQUEST_TEMPLATE.md"
                )
            )
            self.assertFalse(
                validate_repo.path_exists_with_exact_case(
                    temp_root, duplicate_relative_path
                )
            )
            real_path_exists_with_exact_case = validate_repo.path_exists_with_exact_case

            def fake_path_exists_with_exact_case(repo_root: Path, relative_path: Path) -> bool:
                if repo_root == temp_root and relative_path == duplicate_relative_path:
                    return True
                return real_path_exists_with_exact_case(repo_root, relative_path)

            with patch.object(
                source_contracts,
                "path_exists_with_exact_case",
                side_effect=fake_path_exists_with_exact_case,
            ):
                with self.assertRaisesRegex(
                    validate_repo.ValidationError,
                    r"sole canonical PR template",
                ):
                    validate_repo.parse_github_review_templates(temp_root)

    def test_changelog_tracks_unreleased_without_losing_v020_and_v010_entries(self) -> None:
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn("## [Unreleased]", changelog)
        self.assertIn("## [0.4.0] - 2026-04-10", changelog)
        self.assertIn("## [0.2.0] - 2026-03-23", changelog)
        self.assertIn("## [0.1.0] - 2026-03-17", changelog)


if __name__ == "__main__":
    unittest.main()
