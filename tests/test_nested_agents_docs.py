from __future__ import annotations

from tempfile import TemporaryDirectory
import unittest
from pathlib import Path

from scripts import validate_nested_agents

REPO_ROOT = Path(__file__).resolve().parents[1]


def materialize_valid_agents(repo_root: Path) -> None:
    for spec in validate_nested_agents.REQUIRED_DOCS:
        path = repo_root / spec.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            "# AGENTS.md\n\n" + "\n".join(f"- {snippet}" for snippet in spec.required_snippets) + "\n",
            encoding="utf-8",
        )


class NestedAgentsDocsTests(unittest.TestCase):
    def test_required_nested_agents_docs_exist_and_include_expected_snippets(self) -> None:
        self.assertEqual([], validate_nested_agents.validate(REPO_ROOT))

    def test_validator_reports_missing_file(self) -> None:
        with TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            materialize_valid_agents(temp_root)
            missing_path = temp_root / "techniques" / "history" / "AGENTS.md"
            missing_path.unlink()
            issues = validate_nested_agents.validate(temp_root)

        self.assertIn("techniques/history/AGENTS.md: file is missing", issues)

    def test_validator_reports_missing_snippet(self) -> None:
        with TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            materialize_valid_agents(temp_root)
            target = temp_root / "templates" / "AGENTS.md"
            original_text = target.read_text(encoding="utf-8")
            target.write_text(
                original_text.replace("`PROMOTION_NOTE.template.md`", "`REMOVED.template.md`"),
                encoding="utf-8",
            )
            issues = validate_nested_agents.validate(temp_root)

        self.assertIn(
            "templates/AGENTS.md: missing snippet '`PROMOTION_NOTE.template.md`'",
            issues,
        )


if __name__ == "__main__":
    unittest.main()
