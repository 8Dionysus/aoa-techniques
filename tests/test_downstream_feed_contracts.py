from __future__ import annotations

import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator


REPO_ROOT = Path(__file__).resolve().parents[1]
GENERATED_DIR = REPO_ROOT / "generated"
SCHEMAS_DIR = REPO_ROOT / "schemas"


def load_json(relative_path: str) -> dict:
    return json.loads((REPO_ROOT / relative_path).read_text(encoding="utf-8"))


class DownstreamFeedContractsTests(unittest.TestCase):
    def test_expected_downstream_feeds_exist(self) -> None:
        for relative_path in (
            "generated/technique_catalog.min.json",
            "generated/technique_capsules.json",
            "generated/technique_sections.full.json",
            "generated/repo_doc_surface_manifest.min.json",
            "generated/technique_feat_cards.min.example.json",
            "schemas/technique_feat_catalog.schema.json",
        ):
            with self.subTest(path=relative_path):
                self.assertTrue((REPO_ROOT / relative_path).is_file())

    def test_catalog_capsules_and_sections_share_ids_and_paths(self) -> None:
        catalog = load_json("generated/technique_catalog.min.json")
        capsules = load_json("generated/technique_capsules.json")
        sections = load_json("generated/technique_sections.full.json")

        catalog_pairs = [
            (entry["id"], entry["technique_path"]) for entry in catalog["techniques"]
        ]
        capsule_pairs = [
            (entry["id"], entry["technique_path"]) for entry in capsules["techniques"]
        ]
        section_pairs = [
            (entry["id"], entry["technique_path"]) for entry in sections["techniques"]
        ]

        self.assertEqual(catalog["catalog_version"], 1)
        self.assertEqual(capsules["capsule_version"], 1)
        self.assertEqual(sections["section_version"], 1)
        self.assertEqual(catalog["source_of_truth"], "markdown-frontmatter-v2")
        self.assertEqual(
            capsules["source_of_truth"],
            "frontmatter-summary+markdown-technique-capsules-v1",
        )
        self.assertEqual(
            sections["source_of_truth"]["technique_markdown"],
            "techniques/*/*/TECHNIQUE.md",
        )
        self.assertIn("sections", sections["source_of_truth"])
        self.assertEqual(catalog_pairs, capsule_pairs)
        self.assertEqual(catalog_pairs, section_pairs)

        for entry in catalog["techniques"]:
            self.assertIn("summary", entry)
            self.assertIn("validation_strength", entry)
            self.assertIn("review_required", entry)

    def test_repo_doc_surface_manifest_is_router_safe(self) -> None:
        manifest = load_json("generated/repo_doc_surface_manifest.min.json")

        self.assertEqual(manifest["manifest_version"], 1)
        self.assertEqual(manifest["source_of_truth"], "markdown-repo-doc-surfaces-v1")

        docs = manifest["docs"]
        self.assertTrue(docs)
        self.assertEqual(len({entry["doc_id"] for entry in docs}), len(docs))
        self.assertEqual(len({entry["doc_path"] for entry in docs}), len(docs))

        for entry in docs:
            self.assertTrue(
                entry["doc_path"] == "README.md"
                or entry["doc_path"].startswith("docs/")
                or entry["doc_path"].endswith(".md")
            )
            self.assertTrue(entry["top_level_sections"])

    def test_technique_feat_example_validates_against_schema(self) -> None:
        schema = json.loads(
            (SCHEMAS_DIR / "technique_feat_catalog.schema.json").read_text(encoding="utf-8")
        )
        payload = json.loads(
            (GENERATED_DIR / "technique_feat_cards.min.example.json").read_text(
                encoding="utf-8"
            )
        )

        Draft202012Validator.check_schema(schema)
        Draft202012Validator(schema).validate(payload)


if __name__ == "__main__":
    unittest.main()
