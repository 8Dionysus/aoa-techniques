from __future__ import annotations

import re
import unittest
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]

PILOT_BUNDLES = (
    (
        "AOA-T-0041",
        "skill-marketplace-curation",
        "docs",
        "discovery",
        "promoted",
        "techniques/docs/skill-marketplace-curation",
        "techniques/instruction/skill-discovery/skill-marketplace-curation",
    ),
    (
        "AOA-T-0042",
        "upstream-skill-health-checking",
        "evaluation",
        "validation",
        "promoted",
        "techniques/evaluation/upstream-skill-health-checking",
        "techniques/instruction/skill-discovery/upstream-skill-health-checking",
    ),
)

LIVE_LINK_SURFACES = (
    "incoming/chat-wave-1a-registry-discovery/docs/EXTERNAL_TECHNIQUE_CANDIDATES_CHAT_WAVE_1A.md",
    "incoming/chat-wave-1b-tool-proxy-runtime/docs/PREFLIGHT_REPUTATION_CHECK_NARROWING_MEMO.md",
    "mechanics/audit/parts/promotion-readiness-matrix/README.md",
    "mechanics/distillation/parts/external-candidate-ledger/README.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/capability-boundary-direct-read-migration-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-capability-boundary-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-capability-registry-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/skill-discovery-direct-read-migration-review.md",
    "techniques/tool-use/tool-gateway/mcp-gateway-proxy/TECHNIQUE.md",
    "techniques/tool-use/tool-gateway/mcp-gateway-proxy/notes/canonical-readiness.md",
    "techniques/tool-use/tool-gateway/mcp-gateway-proxy/notes/second-context-adaptation.md",
    "techniques/proof/owner-truth-closeout/pinned-validation-matrix-before-generated-publish/TECHNIQUE.md",
    "techniques/instruction/capability-boundary/recommendation-truth-vs-host-actionability/TECHNIQUE.md",
    "techniques/instruction/capability-registry/capability-discovery/TECHNIQUE.md",
    "techniques/instruction/capability-registry/capability-discovery/notes/canonical-readiness.md",
    "techniques/instruction/capability-registry/versioned-agent-registry-contract/TECHNIQUE.md",
    "techniques/instruction/capability-registry/versioned-agent-registry-contract/notes/canonical-readiness.md",
)

LEGACY_RAW_RECEIPTS_WITH_HISTORICAL_PATHS = (
    "mechanics/distillation/legacy/raw/EXTERNAL_CANDIDATE_LEDGER_2026-05-01_PRE_PRUNE.md",
)


def read_frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    if match is None:
        raise AssertionError(f"missing frontmatter in {path}")
    return yaml.safe_load(match.group(1))


class SkillDiscoveryTreePilotTestCase(unittest.TestCase):
    def test_pilot_bundles_live_under_instruction_skill_discovery_tree(self) -> None:
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

    def test_instruction_route_card_names_skill_discovery_without_overclaiming(self) -> None:
        text = (REPO_ROOT / "techniques" / "instruction" / "AGENTS.md").read_text(
            encoding="utf-8"
        )
        flat_text = re.sub(r"\s+", " ", text)

        self.assertIn("This is a tree trunk, not a frontmatter domain.", text)
        self.assertIn("skill-discovery/", text)
        self.assertIn("curated skill discovery", flat_text)
        self.assertIn("pre-surface upstream source readiness", flat_text)
        self.assertIn("installer behavior", flat_text)
        self.assertIn("sync substrate", flat_text)
        self.assertIn("trust scoring", flat_text)
        self.assertIn("security scanning", flat_text)
        self.assertIn("runtime law", flat_text)
        self.assertIn("agent-role authority", flat_text)
        self.assertIn("Do not add `tree_path` frontmatter", text)

    def test_docs_and_evaluation_route_cards_no_longer_name_moved_representatives(self) -> None:
        docs = (REPO_ROOT / "techniques" / "docs" / "AGENTS.md").read_text(
            encoding="utf-8"
        )
        evaluation = (
            REPO_ROOT / "techniques" / "evaluation" / "AGENTS.md"
        ).read_text(encoding="utf-8")

        self.assertNotIn("skill-marketplace-curation", docs)
        self.assertNotIn("upstream-skill-health-checking", evaluation)

    def test_root_legacy_receipt_preserves_old_and_new_paths(self) -> None:
        receipt = (
            REPO_ROOT
            / "legacy"
            / "receipts"
            / "2026-05-05-skill-discovery-tree-pilot.md"
        ).read_text(encoding="utf-8")

        for technique_id, _slug, _domain, _kind, _status, old_path, new_path in PILOT_BUNDLES:
            with self.subTest(technique_id=technique_id):
                self.assertIn(old_path, receipt)
                self.assertIn(new_path, receipt)

        self.assertIn("They did not pass through root `legacy/`.", receipt)
        self.assertIn("Do not add `tree_path` frontmatter.", receipt)
        self.assertIn("installer behavior", receipt)
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
        review = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
            / "skill-discovery-direct-read-migration-review.md"
        ).read_text(encoding="utf-8")

        for technique_id, _slug, _domain, _kind, _status, old_path, new_path in PILOT_BUNDLES:
            with self.subTest(technique_id=technique_id):
                self.assertIn(f"{new_path}/TECHNIQUE.md", review)
                self.assertIn(f"| `{technique_id}` | `{old_path}/`", review)
                self.assertIn(new_path, review)

    def test_legacy_raw_keeps_historical_paths_as_receipt_evidence(self) -> None:
        text = "\n".join(
            (REPO_ROOT / relative_path).read_text(encoding="utf-8")
            for relative_path in LEGACY_RAW_RECEIPTS_WITH_HISTORICAL_PATHS
        )

        for _technique_id, _slug, _domain, _kind, _status, old_path, _new_path in PILOT_BUNDLES:
            with self.subTest(old_path=old_path):
                self.assertIn(f"{old_path}/TECHNIQUE.md", text)


if __name__ == "__main__":
    unittest.main()
