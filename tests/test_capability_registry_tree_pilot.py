from __future__ import annotations

import re
import unittest
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]

PILOT_BUNDLES = (
    (
        "AOA-T-0025",
        "capability-spec-versioning",
        "artifact",
        "canonical",
        "techniques/docs/capability-spec-versioning",
        "techniques/instruction/capability-registry/capability-spec-versioning",
    ),
    (
        "AOA-T-0063",
        "versioned-agent-registry-contract",
        "artifact",
        "promoted",
        "techniques/docs/versioned-agent-registry-contract",
        "techniques/instruction/capability-registry/versioned-agent-registry-contract",
    ),
    (
        "AOA-T-0064",
        "capability-discovery",
        "discovery",
        "promoted",
        "techniques/docs/capability-discovery",
        "techniques/instruction/capability-registry/capability-discovery",
    ),
)

LIVE_LINK_SURFACES = (
    "mechanics/audit/parts/promotion-readiness-matrix/README.md",
    "incoming/chat-registry-discovery/docs/EXTERNAL_TECHNIQUE_CANDIDATES_CHAT_REGISTRY_DISCOVERY.md",
    "incoming/chat-registry-discovery/docs/SEMANTIC_LINKAGE_RECORDS_NARROWING_MEMO.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-docs-boundary-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/capability-registry-direct-read-migration-review.md",
)

LATER_MIGRATED_SKILL_DISCOVERY_NEIGHBORS = (
    "techniques/instruction/skill-discovery/skill-marketplace-curation/TECHNIQUE.md",
    "techniques/instruction/skill-discovery/upstream-skill-health-checking/TECHNIQUE.md",
)


def read_frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    if match is None:
        raise AssertionError(f"missing frontmatter in {path}")
    return yaml.safe_load(match.group(1))


class CapabilityRegistryTreePilotTestCase(unittest.TestCase):
    def test_pilot_bundles_live_under_instruction_capability_registry_tree(self) -> None:
        for technique_id, slug, _kind, _status, old_path, new_path in PILOT_BUNDLES:
            with self.subTest(technique_id=technique_id):
                self.assertFalse((REPO_ROOT / old_path).exists())
                self.assertTrue((REPO_ROOT / new_path / "TECHNIQUE.md").is_file())
                self.assertTrue((REPO_ROOT / new_path / "checks").is_dir())
                self.assertTrue((REPO_ROOT / new_path / "examples").is_dir())
                self.assertTrue((REPO_ROOT / new_path / "notes").is_dir())
                self.assertEqual(slug, Path(new_path).name)

    def test_pilot_keeps_frontmatter_facets_unchanged(self) -> None:
        for technique_id, _slug, kind, status, _old_path, new_path in PILOT_BUNDLES:
            frontmatter = read_frontmatter(REPO_ROOT / new_path / "TECHNIQUE.md")

            with self.subTest(technique_id=technique_id):
                self.assertEqual(technique_id, frontmatter["id"])
                self.assertEqual("docs", frontmatter["domain"])
                self.assertEqual(kind, frontmatter["kind"])
                self.assertEqual(status, frontmatter["status"])
                self.assertNotIn("tree_path", frontmatter)

    def test_instruction_route_card_names_capability_registry_without_overclaiming(self) -> None:
        text = (REPO_ROOT / "techniques" / "instruction" / "AGENTS.md").read_text(
            encoding="utf-8"
        )
        flat_text = re.sub(r"\s+", " ", text)

        self.assertIn("This is a tree trunk, not a frontmatter domain.", text)
        self.assertIn("capability-registry/", text)
        self.assertIn("capability specs", text)
        self.assertIn("registry-facing entries", text)
        self.assertIn("discovery query", text)
        self.assertIn("registry product doctrine", flat_text)
        self.assertIn("runtime resolution", text)
        self.assertIn("skill acceptance", text)
        self.assertIn("Do not add `tree_path` frontmatter", text)

    def test_root_legacy_receipt_preserves_old_and_new_paths(self) -> None:
        receipt = (
            REPO_ROOT
            / "legacy"
            / "receipts"
            / "2026-05-04-capability-registry-tree-pilot.md"
        ).read_text(encoding="utf-8")

        for technique_id, _slug, _kind, _status, old_path, new_path in PILOT_BUNDLES:
            with self.subTest(technique_id=technique_id):
                self.assertIn(old_path, receipt)
                self.assertIn(new_path, receipt)

        self.assertIn("They did not pass through root `legacy/`.", receipt)
        self.assertIn("Do not add `tree_path` frontmatter.", receipt)
        self.assertIn("registry product doctrine", receipt)
        self.assertIn("separate leaf bundles", receipt)

    def test_live_links_point_to_current_paths(self) -> None:
        text = "\n".join(
            (REPO_ROOT / relative_path).read_text(encoding="utf-8")
            for relative_path in LIVE_LINK_SURFACES
        )

        for technique_id, _slug, _kind, _status, old_path, new_path in PILOT_BUNDLES:
            with self.subTest(technique_id=technique_id):
                self.assertIn(f"{new_path}/TECHNIQUE.md", text)
                self.assertNotIn(f"{old_path}/TECHNIQUE.md", text)

    def test_review_sources_point_to_current_paths_but_keep_pilot_accounting(self) -> None:
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "capability-registry-direct-read-migration-review.md"
        ).read_text(encoding="utf-8")

        for technique_id, _slug, _kind, _status, old_path, new_path in PILOT_BUNDLES:
            with self.subTest(technique_id=technique_id):
                self.assertIn(f"{new_path}/TECHNIQUE.md", review)
                self.assertIn(f"| `{technique_id}` | `{old_path}/`", review)
                self.assertIn(new_path, review)

    def test_neighbor_shelves_keep_current_paths_after_later_pilots(self) -> None:
        for relative_path in LATER_MIGRATED_SKILL_DISCOVERY_NEIGHBORS:
            with self.subTest(relative_path=relative_path):
                self.assertTrue((REPO_ROOT / relative_path).is_file())


if __name__ == "__main__":
    unittest.main()
