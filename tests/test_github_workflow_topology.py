from __future__ import annotations

import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = REPO_ROOT / ".github" / "workflows"
PINNED_CHECKOUT = "actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd"
PINNED_SETUP_PYTHON = "actions/setup-python@a309ff8b426b58ec0e2a45f0f869d46889d02405"


class GitHubWorkflowTopologyTests(unittest.TestCase):
    def workflow_text(self, name: str) -> str:
        return (WORKFLOWS / name).read_text(encoding="utf-8")

    def test_repo_validation_is_growth_safe_and_not_release_freeze(self) -> None:
        workflow = self.workflow_text("repo-validation.yml")

        self.assertIn("pull_request:", workflow)
        self.assertIn("branches:\n      - main", workflow)
        self.assertIn("python scripts/ci_gate.py --mode source-fast", workflow)
        self.assertIn(
            "if: github.event_name == 'push' && github.ref == 'refs/heads/main'",
            workflow,
        )
        self.assertIn("python scripts/ci_gate.py --mode generated", workflow)
        self.assertNotIn("python scripts/ci_gate.py --mode release", workflow)
        self.assertNotIn("python scripts/ci_gate.py --mode nightly", workflow)
        self.assertNotIn("python scripts/release_check.py", workflow)
        self.assertNotIn("python scripts/run_tests.py", workflow)
        self.assertNotIn("python scripts/validate_repo.py", workflow)

    def test_release_and_nightly_have_separate_workflows(self) -> None:
        release = self.workflow_text("release-audit.yml")
        nightly = self.workflow_text("nightly-sentinel.yml")

        self.assertIn('tags:\n      - "v*"', release)
        self.assertIn("workflow_dispatch:", release)
        self.assertIn("python scripts/ci_gate.py --mode release", release)

        self.assertIn("schedule:", nightly)
        self.assertIn("workflow_dispatch:", nightly)
        self.assertIn("python scripts/ci_gate.py --mode nightly", nightly)

        self.assertNotIn("pull_request:", release)
        self.assertNotIn("pull_request:", nightly)

    def test_workflows_use_pinned_actions(self) -> None:
        for workflow_path in sorted(WORKFLOWS.glob("*.yml")):
            text = workflow_path.read_text(encoding="utf-8")
            with self.subTest(workflow=workflow_path.name):
                self.assertIn(PINNED_CHECKOUT, text)
                self.assertIn(PINNED_SETUP_PYTHON, text)
                self.assertNotRegex(text, re.compile(r"actions/checkout@v\d+"))
                self.assertNotRegex(text, re.compile(r"actions/setup-python@v\d+"))

    def test_pull_request_template_names_lanes_not_release_check_as_repo_validation(
        self,
    ) -> None:
        template = (REPO_ROOT / ".github" / "PULL_REQUEST_TEMPLATE.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("source-fast", template)
        self.assertIn("generated, release, and nightly checks", template)
        self.assertNotIn(
            "`Repo Validation` remains aligned with `python scripts/release_check.py`",
            template,
        )


if __name__ == "__main__":
    unittest.main()
