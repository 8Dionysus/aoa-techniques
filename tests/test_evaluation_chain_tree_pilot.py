from __future__ import annotations

import re
import unittest
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]

PILOT_BUNDLES = (
    (
        "AOA-T-0003",
        "contract-first-smoke-summary",
        "evaluation",
        "validation",
        "canonical",
        "techniques/evaluation/contract-first-smoke-summary",
        "techniques/proof/evaluation-chain/contract-first-smoke-summary",
    ),
    (
        "AOA-T-0007",
        "signal-first-gate-promotion",
        "evaluation",
        "guardrail",
        "canonical",
        "techniques/evaluation/signal-first-gate-promotion",
        "techniques/proof/evaluation-chain/signal-first-gate-promotion",
    ),
    (
        "AOA-T-0032",
        "context-report-for-ci",
        "evaluation",
        "validation",
        "promoted",
        "techniques/evaluation/context-report-for-ci",
        "techniques/proof/evaluation-chain/context-report-for-ci",
    ),
)

LIVE_LINK_SURFACES = (
    "mechanics/distillation/parts/technique-reform-ingress/reviews/semantic/EVALUATION_CHAIN_SEMANTIC_REVIEW.md",
    "mechanics/distillation/parts/agon-candidate-handoff/gates/request-evidence-practice.md",
    "mechanics/distillation/parts/external-candidate-ledger/README.md",
)

REVIEW_SURFACES_WITH_ACCOUNTING = (
    "mechanics/distillation/parts/technique-reform-ingress/reviews/evaluation-chain-direct-read-migration-review.md",
)


def read_frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    if match is None:
        raise AssertionError(f"missing frontmatter in {path}")
    return yaml.safe_load(match.group(1))


class EvaluationChainTreePilotTestCase(unittest.TestCase):
    def test_pilot_bundles_live_under_proof_evaluation_chain_tree(self) -> None:
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

    def test_proof_route_card_names_evaluation_chain_without_overclaiming(self) -> None:
        text = (REPO_ROOT / "techniques" / "proof" / "AGENTS.md").read_text(
            encoding="utf-8"
        )
        flat_text = re.sub(r"\s+", " ", text)

        self.assertIn("evaluation-chain/", text)
        self.assertIn("machine-readable validation summaries", flat_text)
        self.assertIn("staged signal promotion", flat_text)
        self.assertIn("read-only CI context reporting", flat_text)
        self.assertIn("CI ownership", text)
        self.assertIn("proof verdict law", text)
        self.assertIn("aoa-evals", text)

    def test_evaluation_route_card_no_longer_names_moved_representatives(self) -> None:
        evaluation = (
            REPO_ROOT / "techniques" / "evaluation" / "AGENTS.md"
        ).read_text(encoding="utf-8")

        self.assertNotIn("contract-first-smoke-summary", evaluation)
        self.assertNotIn("signal-first-gate-promotion", evaluation)
        self.assertNotIn("context-report-for-ci", evaluation)
        self.assertNotIn("contextual-host-doctor", evaluation)
        self.assertIn("No active leaf bundles currently live directly here", evaluation)
        self.assertIn("techniques/execution/", evaluation)

    def test_root_legacy_receipt_preserves_old_and_new_paths(self) -> None:
        receipt = (
            REPO_ROOT
            / "legacy"
            / "receipts"
            / "2026-05-05-evaluation-chain-tree-pilot.md"
        ).read_text(encoding="utf-8")

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
        self.assertIn("CI ownership", receipt)
        self.assertIn("separate leaf bundles", receipt)
        self.assertIn("Keep `AOA-T-0032` promoted", receipt)

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
                if technique_id in {"AOA-T-0003", "AOA-T-0007", "AOA-T-0032"}:
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
