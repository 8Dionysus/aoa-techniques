from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

ROOT_LEGACY_FILES = (
    "legacy/AGENTS.md",
    "legacy/README.md",
    "legacy/INDEX.md",
    "legacy/raw/README.md",
    "legacy/archive/README.md",
    "legacy/receipts/README.md",
)


class RootLegacyTopologyTestCase(unittest.TestCase):
    def test_root_legacy_scaffold_files_exist(self) -> None:
        for relative_path in ROOT_LEGACY_FILES:
            with self.subTest(relative_path=relative_path):
                self.assertTrue((REPO_ROOT / relative_path).is_file())

    def test_root_legacy_inventory_is_indexed(self) -> None:
        index = (REPO_ROOT / "legacy" / "INDEX.md").read_text(encoding="utf-8")
        self.assertIn("Current root legacy inventory:", index)
        self.assertIn("Do not add placeholder receipts", index)
        self.assertIn("legacy/receipts/2026-05-04-review-compaction-tree-pilot.md", index)
        self.assertIn("legacy/receipts/2026-05-04-handoff-continuation-tree-pilot.md", index)
        self.assertIn("legacy/receipts/2026-05-04-media-ingest-tree-pilot.md", index)
        self.assertIn("legacy/receipts/2026-05-04-diagnosis-repair-tree-pilot.md", index)
        self.assertIn("legacy/receipts/2026-05-04-instruction-surface-tree-pilot.md", index)
        self.assertIn("legacy/receipts/2026-05-04-kag-source-lift-tree-pilot.md", index)
        self.assertIn("legacy/receipts/2026-05-04-docs-boundary-tree-pilot.md", index)
        self.assertIn("legacy/receipts/2026-05-04-capability-registry-tree-pilot.md", index)
        self.assertIn("legacy/receipts/2026-05-04-capability-boundary-tree-pilot.md", index)
        self.assertIn("legacy/receipts/2026-05-05-skill-discovery-tree-pilot.md", index)
        self.assertIn("legacy/receipts/2026-05-05-skill-support-tree-pilot.md", index)
        self.assertIn("legacy/receipts/2026-05-05-evaluation-chain-tree-pilot.md", index)
        self.assertIn("legacy/receipts/2026-05-05-published-summary-tree-pilot.md", index)
        self.assertIn("legacy/receipts/2026-05-05-history-artifacts-tree-pilot.md", index)
        self.assertIn("legacy/receipts/2026-05-05-antifragility-recovery-tree-pilot.md", index)
        self.assertIn("legacy/receipts/2026-05-05-ready-work-graphs-tree-pilot.md", index)
        self.assertIn("legacy/receipts/2026-05-05-intent-chain-tree-pilot.md", index)
        self.assertIn("legacy/receipts/2026-05-05-agent-workflows-core-tree-pilot.md", index)
        self.assertIn("legacy/receipts/2026-05-05-donor-harvest-tree-pilot.md", index)
        self.assertIn("legacy/receipts/2026-05-05-decision-routing-tree-pilot.md", index)

        expected_files = {
            "raw": ["README.md"],
            "archive": ["README.md"],
            "receipts": [
                "2026-05-04-capability-boundary-tree-pilot.md",
                "2026-05-04-capability-registry-tree-pilot.md",
                "2026-05-04-diagnosis-repair-tree-pilot.md",
                "2026-05-04-docs-boundary-tree-pilot.md",
                "2026-05-04-handoff-continuation-tree-pilot.md",
                "2026-05-04-instruction-surface-tree-pilot.md",
                "2026-05-04-kag-source-lift-tree-pilot.md",
                "2026-05-04-media-ingest-tree-pilot.md",
                "2026-05-04-review-compaction-tree-pilot.md",
                "2026-05-05-agent-workflows-core-tree-pilot.md",
                "2026-05-05-antifragility-recovery-tree-pilot.md",
                "2026-05-05-decision-routing-tree-pilot.md",
                "2026-05-05-donor-harvest-tree-pilot.md",
                "2026-05-05-evaluation-chain-tree-pilot.md",
                "2026-05-05-history-artifacts-tree-pilot.md",
                "2026-05-05-intent-chain-tree-pilot.md",
                "2026-05-05-published-summary-tree-pilot.md",
                "2026-05-05-ready-work-graphs-tree-pilot.md",
                "2026-05-05-skill-discovery-tree-pilot.md",
                "2026-05-05-skill-support-tree-pilot.md",
                "README.md",
            ],
        }

        for directory, expected in expected_files.items():
            legacy_dir = REPO_ROOT / "legacy" / directory
            files = sorted(path.name for path in legacy_dir.iterdir() if path.is_file())

            with self.subTest(directory=directory):
                self.assertEqual(expected, files)

    def test_root_legacy_boundary_language_is_explicit(self) -> None:
        combined = "\n".join(
            (REPO_ROOT / relative_path).read_text(encoding="utf-8")
            for relative_path in ROOT_LEGACY_FILES
        )

        required_fragments = (
            "not a second `incoming/`",
            "not active technique canon",
            "Do not move active technique bundles",
            "public-safe",
            "INDEX.md",
        )

        for fragment in required_fragments:
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, combined)

    def test_root_routes_name_legacy_without_turning_it_into_canon(self) -> None:
        route_files = (
            "AGENTS.md",
            "README.md",
            "docs/ROOT_SURFACE_LAW.md",
            "docs/TECHNIQUE_TREE_CONTRACT.md",
            "docs/START_HERE.md",
            "docs/README.md",
        )

        for relative_path in route_files:
            text = (REPO_ROOT / relative_path).read_text(encoding="utf-8")

            with self.subTest(relative_path=relative_path):
                self.assertIn("legacy", text)

        tree_contract = (
            REPO_ROOT / "docs" / "TECHNIQUE_TREE_CONTRACT.md"
        ).read_text(encoding="utf-8")
        self.assertIn(
            "Do not move active technique bundles through root `legacy/`",
            tree_contract,
        )

    def test_root_legacy_does_not_hold_active_or_generated_surfaces(self) -> None:
        legacy_root = REPO_ROOT / "legacy"
        unexpected = []
        for path in legacy_root.rglob("*"):
            if not path.is_file():
                continue
            if path.name == "TECHNIQUE.md" or path.suffix in {".json", ".yaml", ".yml"}:
                unexpected.append(path.relative_to(REPO_ROOT).as_posix())

        self.assertEqual([], unexpected)


if __name__ == "__main__":
    unittest.main()
