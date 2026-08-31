from __future__ import annotations

import re
import unittest
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[3]

PILOT_BUNDLES = (
    (
        "AOA-T-0051",
        "commit-triggered-background-review",
        "workflow",
        "techniques/agent-workflows/commit-triggered-background-review",
        "techniques/continuity/review-compaction/commit-triggered-background-review",
    ),
    (
        "AOA-T-0052",
        "review-findings-compaction",
        "workflow",
        "techniques/agent-workflows/review-findings-compaction",
        "techniques/continuity/review-compaction/review-findings-compaction",
    ),
    (
        "AOA-T-0054",
        "compaction-resilient-skill-loading",
        "recovery",
        "techniques/agent-workflows/compaction-resilient-skill-loading",
        "techniques/continuity/review-compaction/compaction-resilient-skill-loading",
    ),
)


def read_frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    if match is None:
        raise AssertionError(f"missing frontmatter in {path}")
    return yaml.safe_load(match.group(1))


class ReviewCompactionTreePilotTestCase(unittest.TestCase):
    def test_pilot_bundles_live_under_continuity_tree(self) -> None:
        for technique_id, slug, _kind, old_path, new_path in PILOT_BUNDLES:
            with self.subTest(technique_id=technique_id):
                self.assertFalse((REPO_ROOT / old_path).exists())
                self.assertTrue((REPO_ROOT / new_path / "TECHNIQUE.md").is_file())
                self.assertTrue((REPO_ROOT / new_path / "checks").is_dir())
                self.assertTrue((REPO_ROOT / new_path / "examples").is_dir())
                self.assertTrue((REPO_ROOT / new_path / "notes").is_dir())
                self.assertEqual(slug, Path(new_path).name)

    def test_pilot_keeps_frontmatter_facets_unchanged(self) -> None:
        for technique_id, _slug, expected_kind, _old_path, new_path in PILOT_BUNDLES:
            frontmatter = read_frontmatter(REPO_ROOT / new_path / "TECHNIQUE.md")

            with self.subTest(technique_id=technique_id):
                self.assertEqual(technique_id, frontmatter["id"])
                self.assertEqual("agent-workflows", frontmatter["domain"])
                self.assertEqual(expected_kind, frontmatter["kind"])
                self.assertNotIn("tree_path", frontmatter)

    def test_continuity_trunk_has_route_card(self) -> None:
        text = (REPO_ROOT / "techniques" / "continuity" / "AGENTS.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("shared placement applies", text)
        self.assertIn("review-compaction", text)
        self.assertIn("path placement follows the parent contract", text)

    def test_root_legacy_receipt_preserves_old_and_new_paths(self) -> None:
        receipt = (
            REPO_ROOT
            / "legacy"
            / "receipts"
            / "2026-05-04-review-compaction-tree-pilot.md"
        ).read_text(encoding="utf-8")

        for technique_id, _slug, _kind, old_path, new_path in PILOT_BUNDLES:
            with self.subTest(technique_id=technique_id):
                self.assertIn(old_path, receipt)
                self.assertIn(new_path, receipt)

        self.assertIn("They did not pass through root `legacy/`.", receipt)


if __name__ == "__main__":
    unittest.main()
