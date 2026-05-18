from __future__ import annotations

import re
import unittest
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[3]

PILOT_BUNDLES = (
    (
        "AOA-T-0018",
        "markdown-technique-section-lift",
        "canonical",
        "techniques/docs/markdown-technique-section-lift",
        "techniques/knowledge-lift/kag-source-lift/markdown-technique-section-lift",
    ),
    (
        "AOA-T-0019",
        "frontmatter-metadata-spine",
        "canonical",
        "techniques/docs/frontmatter-metadata-spine",
        "techniques/knowledge-lift/kag-source-lift/frontmatter-metadata-spine",
    ),
    (
        "AOA-T-0020",
        "evidence-note-provenance-lift",
        "promoted",
        "techniques/docs/evidence-note-provenance-lift",
        "techniques/knowledge-lift/kag-source-lift/evidence-note-provenance-lift",
    ),
    (
        "AOA-T-0021",
        "bounded-relation-lift-for-kag",
        "canonical",
        "techniques/docs/bounded-relation-lift-for-kag",
        "techniques/knowledge-lift/kag-source-lift/bounded-relation-lift-for-kag",
    ),
    (
        "AOA-T-0022",
        "risk-and-negative-effect-lift",
        "promoted",
        "techniques/docs/risk-and-negative-effect-lift",
        "techniques/knowledge-lift/kag-source-lift/risk-and-negative-effect-lift",
    ),
    (
        "AOA-T-0046",
        "repo-doc-surface-lift",
        "canonical",
        "techniques/docs/repo-doc-surface-lift",
        "techniques/knowledge-lift/kag-source-lift/repo-doc-surface-lift",
    ),
    (
        "AOA-T-0047",
        "github-review-template-lift",
        "promoted",
        "techniques/docs/github-review-template-lift",
        "techniques/knowledge-lift/kag-source-lift/github-review-template-lift",
    ),
    (
        "AOA-T-0048",
        "semantic-review-surface-lift",
        "canonical",
        "techniques/docs/semantic-review-surface-lift",
        "techniques/knowledge-lift/kag-source-lift/semantic-review-surface-lift",
    ),
)

LIVE_LINK_SURFACES = (
    "docs/source-lift/KAG_SOURCE_LIFT_GUIDE.md",
    "docs/source-lift/REPO_DOC_SURFACE_LIFT_GUIDE.md",
    "docs/README.md",
    "docs/source-lift/EVIDENCE_NOTE_PROVENANCE_GUIDE.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/semantic/KAG_SOURCE_LIFT_SEMANTIC_REVIEW.md",
    "docs/review/TECHNIQUE_SHADOW_GUIDE.md",
    "docs/source-lift/FRONTMATTER_METADATA_SPINE_GUIDE.md",
    "docs/source-lift/BOUNDED_RELATION_LIFT_GUIDE.md",
    "docs/source-lift/RISK_AND_NEGATIVE_EFFECT_LIFT_GUIDE.md",
    "docs/source-lift/TECHNIQUE_SECTION_LIFT_GUIDE.md",
    "mechanics/boundary-bridge/PROVENANCE.md",
    "mechanics/boundary-bridge/parts/derived-projection-anchors/README.md",
    "mechanics/audit/parts/external-evidence-ledger/README.md",
    "mechanics/audit/parts/external-evidence-sprint-runbook/README.md",
    "mechanics/audit/parts/promotion-readiness-matrix/README.md",
    "mechanics/audit/parts/promotion-evidence-runbook/README.md",
    "mechanics/distillation/parts/cross-layer-candidate-ledger/README.md",
    "mechanics/distillation/parts/long-gap-reentry/README.md",
    "incoming/chat-registry-discovery/docs/SEMANTIC_LINKAGE_RECORDS_CLOSEOUT_MEMO.md",
)

UNMOVED_DOCS_SHELVES = (
    "techniques/proof/review-evidence/single-scoped-evidence-reference/TECHNIQUE.md",
)

LATER_MIGRATED_SKILL_DISCOVERY_NEIGHBOR = (
    "techniques/instruction/skill-discovery/skill-marketplace-curation/TECHNIQUE.md"
)

LATER_MIGRATED_SKILL_SUPPORT_NEIGHBOR = (
    "techniques/proof/skill-support/bounded-context-map/TECHNIQUE.md"
)


def read_frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    if match is None:
        raise AssertionError(f"missing frontmatter in {path}")
    return yaml.safe_load(match.group(1))


class KagSourceLiftTreePilotTestCase(unittest.TestCase):
    def test_pilot_bundles_live_under_knowledge_lift_tree(self) -> None:
        for technique_id, slug, _status, old_path, new_path in PILOT_BUNDLES:
            with self.subTest(technique_id=technique_id):
                self.assertFalse((REPO_ROOT / old_path).exists())
                self.assertTrue((REPO_ROOT / new_path / "TECHNIQUE.md").is_file())
                self.assertTrue((REPO_ROOT / new_path / "checks").is_dir())
                self.assertTrue((REPO_ROOT / new_path / "examples").is_dir())
                self.assertTrue((REPO_ROOT / new_path / "notes").is_dir())
                self.assertEqual(slug, Path(new_path).name)

    def test_pilot_keeps_frontmatter_facets_unchanged(self) -> None:
        for technique_id, _slug, status, _old_path, new_path in PILOT_BUNDLES:
            frontmatter = read_frontmatter(REPO_ROOT / new_path / "TECHNIQUE.md")

            with self.subTest(technique_id=technique_id):
                self.assertEqual(technique_id, frontmatter["id"])
                self.assertEqual("docs", frontmatter["domain"])
                self.assertEqual("lift", frontmatter["kind"])
                self.assertEqual(status, frontmatter["status"])
                self.assertNotIn("tree_path", frontmatter)

    def test_knowledge_lift_trunk_has_route_card(self) -> None:
        text = (REPO_ROOT / "techniques" / "knowledge-lift" / "AGENTS.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("This is a tree trunk, not a frontmatter domain.", text)
        self.assertIn("kag-source-lift/", text)
        self.assertIn("Do not add `tree_path` frontmatter", text)
        self.assertIn("aoa-kag", text)
        self.assertIn("graph semantics", text.replace("\n", " "))
        self.assertIn("generated source-of-truth replacement", text)

    def test_root_legacy_receipt_preserves_old_and_new_paths(self) -> None:
        receipt = (
            REPO_ROOT
            / "legacy"
            / "receipts"
            / "2026-05-04-kag-source-lift-tree-pilot.md"
        ).read_text(encoding="utf-8")

        for technique_id, _slug, _status, old_path, new_path in PILOT_BUNDLES:
            with self.subTest(technique_id=technique_id):
                self.assertIn(old_path, receipt)
                self.assertIn(new_path, receipt)

        self.assertIn("They did not pass through root `legacy/`.", receipt)
        self.assertIn("Do not add `tree_path` frontmatter.", receipt)
        self.assertIn("KAG owner doctrine", receipt)
        self.assertIn("generated source of truth", receipt)
        self.assertIn("automatic verdict", receipt)

    def test_live_links_point_to_current_paths(self) -> None:
        text = "\n".join(
            (REPO_ROOT / relative_path).read_text(encoding="utf-8")
            for relative_path in LIVE_LINK_SURFACES
        )

        for technique_id, _slug, _status, old_path, new_path in PILOT_BUNDLES:
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
            / "kag-source-lift-direct-read-migration-review.md"
        ).read_text(encoding="utf-8")

        for technique_id, _slug, _status, old_path, new_path in PILOT_BUNDLES:
            with self.subTest(technique_id=technique_id):
                self.assertIn(f"{new_path}/TECHNIQUE.md", review)
                self.assertIn(f"| `{technique_id}` | `{old_path}/`", review)
                self.assertIn(new_path, review)

    def test_neighbor_shelves_were_not_moved_with_the_pilot(self) -> None:
        for relative_path in UNMOVED_DOCS_SHELVES:
            with self.subTest(relative_path=relative_path):
                self.assertTrue((REPO_ROOT / relative_path).is_file())

        self.assertTrue((REPO_ROOT / LATER_MIGRATED_SKILL_DISCOVERY_NEIGHBOR).is_file())
        self.assertTrue((REPO_ROOT / LATER_MIGRATED_SKILL_SUPPORT_NEIGHBOR).is_file())


if __name__ == "__main__":
    unittest.main()
