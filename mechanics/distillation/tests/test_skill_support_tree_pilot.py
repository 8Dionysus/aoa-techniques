from __future__ import annotations

import re
import unittest
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[3]

PILOT_BUNDLES = (
    (
        "AOA-T-0016",
        "bounded-context-map",
        "docs",
        "artifact",
        "canonical",
        "techniques/docs/bounded-context-map",
        "techniques/proof/skill-support/bounded-context-map",
    ),
    (
        "AOA-T-0015",
        "contract-test-design",
        "evaluation",
        "validation",
        "canonical",
        "techniques/evaluation/contract-test-design",
        "techniques/proof/skill-support/contract-test-design",
    ),
    (
        "AOA-T-0017",
        "property-invariants",
        "evaluation",
        "validation",
        "canonical",
        "techniques/evaluation/property-invariants",
        "techniques/proof/skill-support/property-invariants",
    ),
)

LIVE_LINK_SURFACES = (
    "mechanics/distillation/parts/technique-reform-ingress/reviews/semantic/SKILL_SUPPORT_SEMANTIC_REVIEW.md",
    "docs/readers/selection/SELECTION_PATTERNS.md",
    "docs/readers/selection/TECHNIQUE_SELECTION.md",
    "mechanics/boundary-bridge/PROVENANCE.md",
    "mechanics/boundary-bridge/parts/owner-boundary-anchors/README.md",
    "mechanics/boundary-bridge/parts/proof-claim-anchors/README.md",
    "mechanics/rpg/PROVENANCE.md",
    "mechanics/rpg/parts/source-boundary-anchors/README.md",
)

REVIEW_SURFACES_WITH_ACCOUNTING = (
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-skill-discovery-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/skill-support-direct-read-migration-review.md",
)

def read_frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    if match is None:
        raise AssertionError(f"missing frontmatter in {path}")
    return yaml.safe_load(match.group(1))


class SkillSupportTreePilotTestCase(unittest.TestCase):
    def test_pilot_bundles_live_under_proof_skill_support_tree(self) -> None:
        for technique_id, slug, _domain, _kind, _status, old_path, new_path in PILOT_BUNDLES:
            with self.subTest(technique_id=technique_id):
                self.assertFalse((REPO_ROOT / old_path).exists())
                self.assertTrue((REPO_ROOT / new_path / "TECHNIQUE.md").is_file())
                self.assertTrue((REPO_ROOT / new_path / "checks").is_dir())
                self.assertTrue((REPO_ROOT / new_path / "examples").is_dir())
                self.assertTrue((REPO_ROOT / new_path / "notes").is_dir())
                self.assertEqual(slug, Path(new_path).name)

    def test_pilot_keeps_frontmatter_facets_unchanged(self) -> None:
        for technique_id, _slug, domain, kind, status, _old_path, new_path in PILOT_BUNDLES:
            frontmatter = read_frontmatter(REPO_ROOT / new_path / "TECHNIQUE.md")

            with self.subTest(technique_id=technique_id):
                self.assertEqual(technique_id, frontmatter["id"])
                self.assertEqual(domain, frontmatter["domain"])
                self.assertEqual(kind, frontmatter["kind"])
                self.assertEqual(status, frontmatter["status"])
                self.assertNotIn("tree_path", frontmatter)

    def test_proof_route_card_names_skill_support_without_overclaiming(self) -> None:
        text = (REPO_ROOT / "techniques" / "proof" / "AGENTS.md").read_text(
            encoding="utf-8"
        )
        flat_text = re.sub(r"\s+", " ", text)

        self.assertIn("skill-support/", text)
        self.assertIn("proof verdict authority", text)
        self.assertIn("aoa-evals", text)
        self.assertIn("bounded-context vocabulary", flat_text)
        self.assertIn("consumer-visible contract validation", flat_text)
        self.assertIn("invariant-oriented coverage", flat_text)
        self.assertIn("Do not widen a proof technique", text)

    def test_docs_and_evaluation_route_cards_no_longer_name_moved_representatives(self) -> None:
        docs = (REPO_ROOT / "techniques" / "docs" / "AGENTS.md").read_text(
            encoding="utf-8"
        )
        evaluation = (
            REPO_ROOT / "techniques" / "evaluation" / "AGENTS.md"
        ).read_text(encoding="utf-8")

        self.assertNotIn("bounded-context-map", docs)
        self.assertNotIn("contract-test-design", evaluation)
        self.assertNotIn("property-invariants", evaluation)

    def test_root_legacy_receipt_preserves_old_and_new_paths(self) -> None:
        receipt = (
            REPO_ROOT
            / "legacy"
            / "receipts"
            / "2026-05-05-skill-support-tree-pilot.md"
        ).read_text(encoding="utf-8")

        for technique_id, _slug, _domain, _kind, _status, old_path, new_path in PILOT_BUNDLES:
            with self.subTest(technique_id=technique_id):
                self.assertIn(old_path, receipt)
                self.assertIn(new_path, receipt)

        self.assertIn("They did not pass through root `legacy/`.", receipt)
        self.assertIn("Do not add `tree_path` frontmatter.", receipt)
        self.assertIn("proof authority", receipt)
        self.assertIn("separate leaf bundles", receipt)

    def test_live_links_point_to_current_paths(self) -> None:
        text = "\n".join(
            (REPO_ROOT / relative_path).read_text(encoding="utf-8")
            for relative_path in LIVE_LINK_SURFACES
        )

        for technique_id, _slug, _domain, _kind, _status, old_path, new_path in PILOT_BUNDLES:
            with self.subTest(technique_id=technique_id):
                self.assertIn(f"{new_path}/TECHNIQUE.md", text)
                self.assertNotIn(f"{old_path}/TECHNIQUE.md", text)

    def test_review_sources_point_to_current_paths_but_keep_pilot_accounting(self) -> None:
        review_texts = "\n".join(
            (REPO_ROOT / relative_path).read_text(encoding="utf-8")
            for relative_path in REVIEW_SURFACES_WITH_ACCOUNTING
        )

        for technique_id, _slug, _domain, _kind, _status, old_path, new_path in PILOT_BUNDLES:
            with self.subTest(technique_id=technique_id):
                self.assertIn(f"{new_path}/TECHNIQUE.md", review_texts)
                self.assertIn(f"| `{technique_id}` | `{old_path}/`", review_texts)
                self.assertIn(new_path, review_texts)

if __name__ == "__main__":
    unittest.main()
