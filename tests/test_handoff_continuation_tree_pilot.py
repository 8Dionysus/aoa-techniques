from __future__ import annotations

import re
import unittest
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]

PILOT_BUNDLES = (
    (
        "AOA-T-0056",
        "channelized-agent-mailbox",
        "handoff",
        "techniques/agent-workflows/channelized-agent-mailbox",
        "techniques/continuity/handoff-continuation/channelized-agent-mailbox",
    ),
    (
        "AOA-T-0057",
        "structured-handoff-before-compaction",
        "handoff",
        "techniques/agent-workflows/structured-handoff-before-compaction",
        "techniques/continuity/handoff-continuation/structured-handoff-before-compaction",
    ),
    (
        "AOA-T-0058",
        "receipt-confirmed-handoff-packet",
        "handoff",
        "techniques/agent-workflows/receipt-confirmed-handoff-packet",
        "techniques/continuity/handoff-continuation/receipt-confirmed-handoff-packet",
    ),
    (
        "AOA-T-0059",
        "git-verified-handoff-claims",
        "handoff",
        "techniques/agent-workflows/git-verified-handoff-claims",
        "techniques/continuity/handoff-continuation/git-verified-handoff-claims",
    ),
    (
        "AOA-T-0060",
        "session-opening-ritual-before-work",
        "handoff",
        "techniques/agent-workflows/session-opening-ritual-before-work",
        "techniques/continuity/handoff-continuation/session-opening-ritual-before-work",
    ),
    (
        "AOA-T-0061",
        "cross-repo-resource-map-bootstrap",
        "handoff",
        "techniques/agent-workflows/cross-repo-resource-map-bootstrap",
        "techniques/continuity/handoff-continuation/cross-repo-resource-map-bootstrap",
    ),
    (
        "AOA-T-0062",
        "episode-bounded-agent-loop",
        "handoff",
        "techniques/agent-workflows/episode-bounded-agent-loop",
        "techniques/continuity/handoff-continuation/episode-bounded-agent-loop",
    ),
)


def read_frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    if match is None:
        raise AssertionError(f"missing frontmatter in {path}")
    return yaml.safe_load(match.group(1))


class HandoffContinuationTreePilotTestCase(unittest.TestCase):
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

    def test_continuity_trunk_names_both_pilot_shelves(self) -> None:
        text = (REPO_ROOT / "techniques" / "continuity" / "AGENTS.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("This is a tree trunk, not a frontmatter domain.", text)
        self.assertIn("review-compaction", text)
        self.assertIn("handoff-continuation", text)
        self.assertIn("Do not add `tree_path` frontmatter", text)

    def test_root_legacy_receipt_preserves_old_and_new_paths(self) -> None:
        receipt = (
            REPO_ROOT
            / "legacy"
            / "receipts"
            / "2026-05-04-handoff-continuation-tree-pilot.md"
        ).read_text(encoding="utf-8")

        for technique_id, _slug, _kind, old_path, new_path in PILOT_BUNDLES:
            with self.subTest(technique_id=technique_id):
                self.assertIn(old_path, receipt)
                self.assertIn(new_path, receipt)

        self.assertIn("They did not pass through root `legacy/`.", receipt)


if __name__ == "__main__":
    unittest.main()
