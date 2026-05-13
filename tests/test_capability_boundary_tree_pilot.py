from __future__ import annotations

import re
import unittest
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]

PILOT_BUNDLES = (
    (
        "AOA-T-0040",
        "skill-vs-command-boundary",
        "docs",
        "guardrail",
        "canonical",
        "techniques/docs/skill-vs-command-boundary",
        "techniques/instruction/capability-boundary/skill-vs-command-boundary",
    ),
    (
        "AOA-T-0043",
        "multi-source-primary-input-provenance",
        "docs",
        "guardrail",
        "canonical",
        "techniques/docs/multi-source-primary-input-provenance",
        "techniques/instruction/capability-boundary/multi-source-primary-input-provenance",
    ),
    (
        "AOA-T-0093",
        "recommendation-truth-vs-host-actionability",
        "agent-workflows",
        "guardrail",
        "canonical",
        "techniques/agent-workflows/recommendation-truth-vs-host-actionability",
        "techniques/instruction/capability-boundary/recommendation-truth-vs-host-actionability",
    ),
)

LIVE_LINK_SURFACES = (
    "mechanics/audit/parts/promotion-readiness-matrix/README.md",
    "mechanics/experience/parts/technique-candidate-bridge/README.md",
    "mechanics/distillation/parts/external-candidate-ledger/README.md",
    "mechanics/distillation/parts/cross-layer-candidate-ledger/README.md",
    "mechanics/distillation/parts/cross-layer-candidate-ledger/config/cross_layer_candidate_registry.source.json",
    "mechanics/distillation/parts/agon-candidate-handoff/gates/offer-evidence-reference-practice.md",
    "mechanics/boundary-bridge/PROVENANCE.md",
    "mechanics/boundary-bridge/parts/derived-projection-anchors/README.md",
    "mechanics/boundary-bridge/parts/proof-claim-anchors/README.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/first-kind-ambiguity-review-pack.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/second-kind-ambiguity-review-pack.md",
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


class CapabilityBoundaryTreePilotTestCase(unittest.TestCase):
    def test_pilot_bundles_live_under_instruction_capability_boundary_tree(self) -> None:
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

    def test_instruction_route_card_names_capability_boundary_without_overclaiming(self) -> None:
        text = (REPO_ROOT / "techniques" / "instruction" / "AGENTS.md").read_text(
            encoding="utf-8"
        )
        flat_text = re.sub(r"\s+", " ", text)

        self.assertIn("This is a tree trunk, not a frontmatter domain.", text)
        self.assertIn("capability-boundary/", text)
        self.assertIn("skill-command boundaries", text)
        self.assertIn("primary source priority", flat_text)
        self.assertIn("recommendation/actionability", text)
        self.assertIn("marketplace curation", text)
        self.assertIn("upstream health validation", flat_text)
        self.assertIn("runtime law", text)
        self.assertIn("host inventory", text)
        self.assertIn("agent-role authority", text)
        self.assertIn("Do not add `tree_path` frontmatter", text)

    def test_root_legacy_receipt_preserves_old_and_new_paths(self) -> None:
        receipt = (
            REPO_ROOT
            / "legacy"
            / "receipts"
            / "2026-05-04-capability-boundary-tree-pilot.md"
        ).read_text(encoding="utf-8")

        for technique_id, _slug, _domain, _kind, _status, old_path, new_path in PILOT_BUNDLES:
            with self.subTest(technique_id=technique_id):
                self.assertIn(old_path, receipt)
                self.assertIn(new_path, receipt)

        self.assertIn("They did not pass through root `legacy/`.", receipt)
        self.assertIn("Do not add `tree_path` frontmatter.", receipt)
        self.assertIn("skill marketplace curation", receipt)
        self.assertIn("separate guardrail leaves", receipt)

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
        direct_review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "capability-boundary-direct-read-migration-review.md"
        ).read_text(encoding="utf-8")
        landed_review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "landed-capability-registry-pilot-review.md"
        ).read_text(encoding="utf-8")

        for technique_id, _slug, _domain, _kind, _status, old_path, new_path in PILOT_BUNDLES:
            with self.subTest(technique_id=technique_id):
                self.assertIn(f"{new_path}/TECHNIQUE.md", direct_review)
                self.assertIn(f"{new_path}/TECHNIQUE.md", landed_review)
                self.assertIn(f"| `{technique_id}` | `{old_path}/`", direct_review)
                self.assertIn(f"| `{technique_id}` | `{old_path}/`", landed_review)
                self.assertIn(new_path, direct_review)
                self.assertIn(new_path, landed_review)

    def test_skill_discovery_neighbor_shelf_has_current_landed_paths(self) -> None:
        for relative_path in LATER_MIGRATED_SKILL_DISCOVERY_NEIGHBORS:
            with self.subTest(relative_path=relative_path):
                self.assertTrue((REPO_ROOT / relative_path).is_file())


if __name__ == "__main__":
    unittest.main()
