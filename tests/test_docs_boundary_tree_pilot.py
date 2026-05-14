from __future__ import annotations

import re
import unittest
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]

PILOT_BUNDLES = (
    (
        "AOA-T-0002",
        "source-of-truth-layout",
        "artifact",
        "canonical",
        "techniques/docs/source-of-truth-layout",
        "techniques/instruction/docs-boundary/source-of-truth-layout",
    ),
    (
        "AOA-T-0009",
        "lightweight-status-snapshot",
        "artifact",
        "canonical",
        "techniques/docs/lightweight-status-snapshot",
        "techniques/instruction/docs-boundary/lightweight-status-snapshot",
    ),
    (
        "AOA-T-0034",
        "public-safe-artifact-sanitization",
        "guardrail",
        "canonical",
        "techniques/docs/public-safe-artifact-sanitization",
        "techniques/instruction/docs-boundary/public-safe-artifact-sanitization",
    ),
    (
        "AOA-T-0033",
        "decision-rationale-recording",
        "artifact",
        "canonical",
        "techniques/docs/decision-rationale-recording",
        "techniques/instruction/docs-boundary/decision-rationale-recording",
    ),
)

LIVE_LINK_SURFACES = (
    "docs/REPO_DOC_SURFACE_LIFT_GUIDE.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/semantic/DOCS_BOUNDARY_SEMANTIC_REVIEW.md",
    "docs/SELECTION_PATTERNS.md",
    "docs/TECHNIQUE_SELECTION.md",
    "mechanics/audit/parts/external-evidence-ledger/README.md",
    "mechanics/audit/parts/promotion-readiness-matrix/README.md",
    "mechanics/audit/parts/promotion-evidence-runbook/README.md",
    "mechanics/experience/parts/technique-candidate-bridge/README.md",
    "mechanics/distillation/parts/agon-candidate-handoff/gates/offer-evidence-reference-practice.md",
    "techniques/proof/review-evidence/single-scoped-evidence-reference/TECHNIQUE.md",
    "techniques/knowledge-lift/kag-source-lift/semantic-review-surface-lift/examples/minimal-semantic-review-surface-lift.md",
)

UNMOVED_DOCS_BUNDLES = (
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


class DocsBoundaryTreePilotTestCase(unittest.TestCase):
    def test_pilot_bundles_live_under_instruction_docs_boundary_tree(self) -> None:
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

    def test_instruction_route_card_names_docs_boundary_without_overclaiming(self) -> None:
        text = (REPO_ROOT / "techniques" / "instruction" / "AGENTS.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("This is a tree trunk, not a frontmatter domain.", text)
        self.assertIn("instruction-surface/", text)
        self.assertIn("docs-boundary/", text)
        self.assertIn("document truth", text)
        self.assertIn("public-share", text)
        self.assertIn("governance, approval, proof, runtime", text)
        self.assertIn("Do not add `tree_path` frontmatter", text)

    def test_root_legacy_receipt_preserves_old_and_new_paths(self) -> None:
        receipt = (
            REPO_ROOT
            / "legacy"
            / "receipts"
            / "2026-05-04-docs-boundary-tree-pilot.md"
        ).read_text(encoding="utf-8")

        for technique_id, _slug, _kind, _status, old_path, new_path in PILOT_BUNDLES:
            with self.subTest(technique_id=technique_id):
                self.assertIn(old_path, receipt)
                self.assertIn(new_path, receipt)

        self.assertIn("They did not pass through root `legacy/`.", receipt)
        self.assertIn("Do not add `tree_path` frontmatter.", receipt)
        self.assertIn("source-of-truth governance", receipt)
        self.assertIn("architecture taxonomy", receipt)

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
            / "docs-boundary-direct-read-migration-review.md"
        ).read_text(encoding="utf-8")

        for technique_id, _slug, _kind, _status, old_path, new_path in PILOT_BUNDLES:
            with self.subTest(technique_id=technique_id):
                self.assertIn(f"{new_path}/TECHNIQUE.md", review)
                self.assertIn(f"| `{technique_id}` | `{old_path}/`", review)
                self.assertIn(new_path, review)

    def test_neighbor_docs_bundles_were_not_moved_with_the_pilot(self) -> None:
        for relative_path in UNMOVED_DOCS_BUNDLES:
            with self.subTest(relative_path=relative_path):
                self.assertTrue((REPO_ROOT / relative_path).is_file())

        self.assertTrue((REPO_ROOT / LATER_MIGRATED_SKILL_DISCOVERY_NEIGHBOR).is_file())
        self.assertTrue((REPO_ROOT / LATER_MIGRATED_SKILL_SUPPORT_NEIGHBOR).is_file())


if __name__ == "__main__":
    unittest.main()
