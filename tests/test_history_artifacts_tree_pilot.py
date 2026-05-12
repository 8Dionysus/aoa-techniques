from __future__ import annotations

import re
import unittest
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]

PILOT_BUNDLES = (
    (
        "AOA-T-0044",
        "versionable-session-transcripts",
        "history",
        "artifact",
        "canonical",
        "techniques/history/versionable-session-transcripts",
        "techniques/history/history-artifacts/versionable-session-transcripts",
    ),
    (
        "AOA-T-0053",
        "local-first-session-index",
        "history",
        "artifact",
        "canonical",
        "techniques/history/local-first-session-index",
        "techniques/history/history-artifacts/local-first-session-index",
    ),
    (
        "AOA-T-0026",
        "session-capture-as-repo-artifact",
        "history",
        "artifact",
        "canonical",
        "techniques/history/session-capture-as-repo-artifact",
        "techniques/history/history-artifacts/session-capture-as-repo-artifact",
    ),
    (
        "AOA-T-0045",
        "witness-trace-as-reviewable-artifact",
        "history",
        "artifact",
        "promoted",
        "techniques/history/witness-trace-as-reviewable-artifact",
        "techniques/history/history-artifacts/witness-trace-as-reviewable-artifact",
    ),
    (
        "AOA-T-0066",
        "transcript-replay-artifact",
        "history",
        "artifact",
        "promoted",
        "techniques/history/transcript-replay-artifact",
        "techniques/history/history-artifacts/transcript-replay-artifact",
    ),
    (
        "AOA-T-0067",
        "transcript-linked-code-lineage",
        "history",
        "artifact",
        "promoted",
        "techniques/history/transcript-linked-code-lineage",
        "techniques/history/history-artifacts/transcript-linked-code-lineage",
    ),
)

LIVE_LINK_SURFACES = (
    "mechanics/checkpoint/PROVENANCE.md",
    "mechanics/checkpoint/parts/technique-anchors/README.md",
    "mechanics/audit/parts/external-evidence-ledger/README.md",
    "mechanics/audit/parts/promotion-readiness-matrix/README.md",
    "mechanics/audit/parts/promotion-evidence-runbook/README.md",
    "mechanics/audit/parts/external-evidence-sprint-runbook/README.md",
    "mechanics/distillation/parts/cross-layer-candidate-ledger/README.md",
    "mechanics/distillation/parts/external-candidate-ledger/README.md",
    "techniques/continuity/donor-harvest/session-donor-harvest/TECHNIQUE.md",
    "techniques/governance/approval-evidence/fail-closed-evidence-gate/TECHNIQUE.md",
    "techniques/continuity/handoff-continuation/structured-handoff-before-compaction/TECHNIQUE.md",
    "techniques/continuity/handoff-continuation/channelized-agent-mailbox/TECHNIQUE.md",
    "techniques/continuity/handoff-continuation/git-verified-handoff-claims/TECHNIQUE.md",
    "techniques/ingest/media-ingest/telegram-export-normalization-to-local-store/TECHNIQUE.md",
)

REVIEW_SURFACES_WITH_ACCOUNTING = (
    "mechanics/distillation/parts/technique-reform-ingress/reviews/landed-published-summary-pilot-review.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/history-artifacts-direct-read-migration-review.md",
)


def read_frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    if match is None:
        raise AssertionError(f"missing frontmatter in {path}")
    return yaml.safe_load(match.group(1))


class HistoryArtifactsTreePilotTestCase(unittest.TestCase):
    def test_pilot_bundles_live_under_history_artifacts_tree(self) -> None:
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

    def test_history_route_card_names_shelf_without_overclaiming(self) -> None:
        text = (REPO_ROOT / "techniques" / "history" / "AGENTS.md").read_text(
            encoding="utf-8"
        )
        flat_text = re.sub(r"\s+", " ", text)

        self.assertIn("history-artifacts/", text)
        self.assertIn("session capture", flat_text)
        self.assertIn("transcript packaging", flat_text)
        self.assertIn("derivative local indexing", flat_text)
        self.assertIn("transcript-linked-code-lineage", text)
        self.assertIn("memory objects and recall surfaces still stay outside", text)
        self.assertIn("private transcripts", text)

    def test_root_legacy_receipt_preserves_old_and_new_paths(self) -> None:
        receipt = (
            REPO_ROOT
            / "legacy"
            / "receipts"
            / "2026-05-05-history-artifacts-tree-pilot.md"
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
        self.assertIn("six separate leaf", receipt)
        self.assertIn("private transcript publication", flat_receipt)
        self.assertIn("generic history platform", flat_receipt)

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
