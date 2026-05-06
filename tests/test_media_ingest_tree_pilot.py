from __future__ import annotations

import re
import unittest
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]

PILOT_BUNDLES = (
    (
        "AOA-T-0070",
        "two-stage-document-ocr-pipeline",
        "techniques/agent-workflows/two-stage-document-ocr-pipeline",
        "techniques/ingest/media-ingest/two-stage-document-ocr-pipeline",
    ),
    (
        "AOA-T-0071",
        "template-backed-field-extraction-after-ocr",
        "techniques/agent-workflows/template-backed-field-extraction-after-ocr",
        "techniques/ingest/media-ingest/template-backed-field-extraction-after-ocr",
    ),
    (
        "AOA-T-0072",
        "perceptual-media-dedupe-with-threshold-review",
        "techniques/agent-workflows/perceptual-media-dedupe-with-threshold-review",
        "techniques/ingest/media-ingest/perceptual-media-dedupe-with-threshold-review",
    ),
    (
        "AOA-T-0073",
        "semantic-media-bucketing-with-vision-plus-ocr",
        "techniques/agent-workflows/semantic-media-bucketing-with-vision-plus-ocr",
        "techniques/ingest/media-ingest/semantic-media-bucketing-with-vision-plus-ocr",
    ),
    (
        "AOA-T-0074",
        "telegram-export-normalization-to-local-store",
        "techniques/agent-workflows/telegram-export-normalization-to-local-store",
        "techniques/ingest/media-ingest/telegram-export-normalization-to-local-store",
    ),
)


def read_frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    if match is None:
        raise AssertionError(f"missing frontmatter in {path}")
    return yaml.safe_load(match.group(1))


class MediaIngestTreePilotTestCase(unittest.TestCase):
    def test_pilot_bundles_live_under_ingest_tree(self) -> None:
        for technique_id, slug, old_path, new_path in PILOT_BUNDLES:
            with self.subTest(technique_id=technique_id):
                self.assertFalse((REPO_ROOT / old_path).exists())
                self.assertTrue((REPO_ROOT / new_path / "TECHNIQUE.md").is_file())
                self.assertTrue((REPO_ROOT / new_path / "checks").is_dir())
                self.assertTrue((REPO_ROOT / new_path / "examples").is_dir())
                self.assertTrue((REPO_ROOT / new_path / "notes").is_dir())
                self.assertEqual(slug, Path(new_path).name)

    def test_pilot_keeps_frontmatter_facets_unchanged(self) -> None:
        for technique_id, _slug, _old_path, new_path in PILOT_BUNDLES:
            frontmatter = read_frontmatter(REPO_ROOT / new_path / "TECHNIQUE.md")

            with self.subTest(technique_id=technique_id):
                self.assertEqual(technique_id, frontmatter["id"])
                self.assertEqual("agent-workflows", frontmatter["domain"])
                self.assertEqual("ingest", frontmatter["kind"])
                self.assertNotIn("tree_path", frontmatter)

    def test_ingest_trunk_has_route_card(self) -> None:
        text = (REPO_ROOT / "techniques" / "ingest" / "AGENTS.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("This is a tree trunk, not a frontmatter domain.", text)
        self.assertIn("media-ingest", text)
        self.assertIn("Do not add `tree_path` frontmatter", text)
        self.assertIn("telegram", text.lower())

    def test_root_legacy_receipt_preserves_old_and_new_paths(self) -> None:
        receipt = (
            REPO_ROOT
            / "legacy"
            / "receipts"
            / "2026-05-04-media-ingest-tree-pilot.md"
        ).read_text(encoding="utf-8")

        for technique_id, _slug, old_path, new_path in PILOT_BUNDLES:
            with self.subTest(technique_id=technique_id):
                self.assertIn(old_path, receipt)
                self.assertIn(new_path, receipt)

        self.assertIn("They did not pass through root `legacy/`.", receipt)
        self.assertIn("telegram-account-auth-and-session-bridge", receipt)

    def test_incoming_personal_ingest_links_point_to_current_paths(self) -> None:
        docs_dir = (
            REPO_ROOT / "incoming" / "personal-media-ingest" / "docs"
        )
        text = "\n".join(
            [
                (
                    docs_dir
                    / "EXTERNAL_TECHNIQUE_CANDIDATES_PERSONAL_MEDIA_INGEST.md"
                ).read_text(encoding="utf-8"),
                (
                    docs_dir
                    / "TELEGRAM_ACCOUNT_AUTH_AND_SESSION_BRIDGE_NARROWING_MEMO.md"
                ).read_text(encoding="utf-8"),
            ]
        )

        for technique_id, _slug, old_path, new_path in PILOT_BUNDLES:
            with self.subTest(technique_id=technique_id):
                self.assertIn(f"{new_path}/TECHNIQUE.md", text)
                self.assertNotIn(f"{old_path}/TECHNIQUE.md", text)


if __name__ == "__main__":
    unittest.main()
