from __future__ import annotations

import re
import unittest
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]

PILOT_BUNDLES = (
    (
        "AOA-T-0006",
        "latest-alias-plus-history-copy",
        "evaluation",
        "artifact",
        "canonical",
        "techniques/evaluation/latest-alias-plus-history-copy",
        "techniques/proof/published-summary/latest-alias-plus-history-copy",
    ),
    (
        "AOA-T-0008",
        "published-summary-remediation-snapshot",
        "evaluation",
        "lift",
        "canonical",
        "techniques/evaluation/published-summary-remediation-snapshot",
        "techniques/proof/published-summary/published-summary-remediation-snapshot",
    ),
    (
        "AOA-T-0010",
        "telemetry-integrity-snapshot",
        "evaluation",
        "validation",
        "canonical",
        "techniques/evaluation/telemetry-integrity-snapshot",
        "techniques/proof/published-summary/telemetry-integrity-snapshot",
    ),
    (
        "AOA-T-0011",
        "required-vs-optional-source-rendering",
        "evaluation",
        "guardrail",
        "canonical",
        "techniques/evaluation/required-vs-optional-source-rendering",
        "techniques/proof/published-summary/required-vs-optional-source-rendering",
    ),
)

LIVE_LINK_SURFACES = (
    "docs/PUBLISHED_SUMMARY_SEMANTIC_REVIEW.md",
    "docs/PUBLISHED_SUMMARY_SHADOW_REVIEW.md",
    "docs/EVALUATION_CHAIN_SEMANTIC_REVIEW.md",
    "incoming/chat-history-lineage-governed-actions/docs/AGENT_READINESS_TELEMETRY_NARROWING_MEMO.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/first-kind-ambiguity-review-pack.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/second-kind-ambiguity-review-pack.md",
)

REVIEW_SURFACES_WITH_ACCOUNTING = (
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-evaluation-chain-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/published-summary-direct-read-migration-review.md",
)


def read_frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    if match is None:
        raise AssertionError(f"missing frontmatter in {path}")
    return yaml.safe_load(match.group(1))


class PublishedSummaryTreePilotTestCase(unittest.TestCase):
    def test_pilot_bundles_live_under_proof_published_summary_tree(self) -> None:
        for (
            technique_id,
            slug,
            _domain,
            _kind,
            _status,
            old_path,
            new_path,
        ) in PILOT_BUNDLES:
            with self.subTest(technique_id=technique_id):
                self.assertFalse((REPO_ROOT / old_path).exists())
                self.assertTrue((REPO_ROOT / new_path / "TECHNIQUE.md").is_file())
                self.assertTrue((REPO_ROOT / new_path / "checks").is_dir())
                self.assertTrue((REPO_ROOT / new_path / "examples").is_dir())
                self.assertTrue((REPO_ROOT / new_path / "notes").is_dir())
                self.assertEqual(slug, Path(new_path).name)

    def test_pilot_keeps_frontmatter_facets_unchanged(self) -> None:
        for (
            technique_id,
            _slug,
            domain,
            kind,
            status,
            _old_path,
            new_path,
        ) in PILOT_BUNDLES:
            frontmatter = read_frontmatter(REPO_ROOT / new_path / "TECHNIQUE.md")

            with self.subTest(technique_id=technique_id):
                self.assertEqual(technique_id, frontmatter["id"])
                self.assertEqual(domain, frontmatter["domain"])
                self.assertEqual(kind, frontmatter["kind"])
                self.assertEqual(status, frontmatter["status"])
                self.assertNotIn("tree_path", frontmatter)

    def test_proof_route_card_names_published_summary_without_overclaiming(self) -> None:
        text = (REPO_ROOT / "techniques" / "proof" / "AGENTS.md").read_text(
            encoding="utf-8"
        )
        flat_text = re.sub(r"\s+", " ", text)

        self.assertIn("published-summary/", text)
        self.assertIn("stable latest alias storage", flat_text)
        self.assertIn("bounded remediation snapshots", flat_text)
        self.assertIn("diagnostic integrity snapshots", flat_text)
        self.assertIn("required-versus-optional summary-source rendering", flat_text)
        self.assertIn("dashboard ownership", text)
        self.assertIn("runtime storage policy", text)
        self.assertIn("generic reporting platform", text)
        self.assertIn("aoa-evals", text)

    def test_evaluation_route_card_no_longer_names_moved_representatives(self) -> None:
        evaluation = (
            REPO_ROOT / "techniques" / "evaluation" / "AGENTS.md"
        ).read_text(encoding="utf-8")

        self.assertNotIn("latest-alias-plus-history-copy", evaluation)
        self.assertNotIn("published-summary-remediation-snapshot", evaluation)
        self.assertNotIn("telemetry-integrity-snapshot", evaluation)
        self.assertNotIn("required-vs-optional-source-rendering", evaluation)
        self.assertNotIn("contextual-host-doctor", evaluation)
        self.assertNotIn("baseline-first-additive-profile-benchmarks", evaluation)
        self.assertIn("No active leaf bundles currently live directly here", evaluation)
        self.assertIn("techniques/execution/", evaluation)

    def test_root_legacy_receipt_preserves_old_and_new_paths(self) -> None:
        receipt = (
            REPO_ROOT
            / "legacy"
            / "receipts"
            / "2026-05-05-published-summary-tree-pilot.md"
        ).read_text(encoding="utf-8")
        flat_receipt = re.sub(r"\s+", " ", receipt)

        for (
            technique_id,
            _slug,
            _domain,
            _kind,
            _status,
            old_path,
            new_path,
        ) in PILOT_BUNDLES:
            with self.subTest(technique_id=technique_id):
                self.assertIn(old_path, receipt)
                self.assertIn(new_path, receipt)

        self.assertIn("They did not pass through root `legacy/`.", receipt)
        self.assertIn("Do not add `tree_path` frontmatter.", receipt)
        self.assertIn("dashboard ownership", flat_receipt)
        self.assertIn("runtime storage policy", flat_receipt)
        self.assertIn("separate leaf bundles", receipt)
        self.assertIn("AOA-T-0011", receipt)

    def test_live_links_point_to_current_paths(self) -> None:
        text = "\n".join(
            (REPO_ROOT / relative_path).read_text(encoding="utf-8")
            for relative_path in LIVE_LINK_SURFACES
        )

        for (
            technique_id,
            _slug,
            _domain,
            _kind,
            _status,
            old_path,
            new_path,
        ) in PILOT_BUNDLES:
            with self.subTest(technique_id=technique_id):
                if technique_id == "AOA-T-0006" or technique_id == "AOA-T-0008":
                    self.assertIn(f"{new_path}/TECHNIQUE.md", text)
                if technique_id in {"AOA-T-0010", "AOA-T-0011"}:
                    self.assertIn(f"{new_path}/TECHNIQUE.md", text)
                self.assertNotIn(f"{old_path}/TECHNIQUE.md", text)

    def test_review_sources_point_to_current_paths_but_keep_pilot_accounting(self) -> None:
        review_texts = "\n".join(
            (REPO_ROOT / relative_path).read_text(encoding="utf-8")
            for relative_path in REVIEW_SURFACES_WITH_ACCOUNTING
        )

        for (
            technique_id,
            _slug,
            _domain,
            _kind,
            _status,
            old_path,
            new_path,
        ) in PILOT_BUNDLES:
            with self.subTest(technique_id=technique_id):
                self.assertIn(f"{new_path}/TECHNIQUE.md", review_texts)
                self.assertIn(f"| `{technique_id}` | `{old_path}/`", review_texts)
                self.assertIn(new_path, review_texts)


if __name__ == "__main__":
    unittest.main()
