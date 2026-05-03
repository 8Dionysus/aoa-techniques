from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

LEGACY_SCAFFOLD_MECHANICS = (
    "boundary-bridge",
    "checkpoint",
    "experience",
    "growth-cycle",
    "method-growth",
    "questbook",
    "recurrence",
    "release-support",
    "rpg",
)

SCAFFOLD_FILES = (
    "legacy/AGENTS.md",
    "legacy/README.md",
    "legacy/INDEX.md",
    "legacy/DISTILLATION_LOG.md",
    "legacy/raw/README.md",
)


class MechanicsLegacyScaffoldTestCase(unittest.TestCase):
    def test_scaffold_files_exist_for_mechanics_without_raw_receipts(self) -> None:
        for mechanic in LEGACY_SCAFFOLD_MECHANICS:
            with self.subTest(mechanic=mechanic):
                for relative_path in SCAFFOLD_FILES:
                    self.assertTrue(
                        (REPO_ROOT / "mechanics" / mechanic / relative_path).is_file()
                    )

    def test_scaffold_raw_inventory_is_empty_except_readme(self) -> None:
        for mechanic in LEGACY_SCAFFOLD_MECHANICS:
            raw_dir = REPO_ROOT / "mechanics" / mechanic / "legacy" / "raw"
            raw_files = sorted(path.name for path in raw_dir.iterdir() if path.is_file())

            with self.subTest(mechanic=mechanic):
                self.assertEqual(["README.md"], raw_files)

    def test_scaffold_provenance_points_to_legacy_without_absence_language(self) -> None:
        banned_fragments = (
            "does not create `legacy/raw/`",
            "can add `legacy/`",
            "no `legacy/raw/` directory",
        )

        for mechanic in LEGACY_SCAFFOLD_MECHANICS:
            provenance = (
                REPO_ROOT / "mechanics" / mechanic / "PROVENANCE.md"
            ).read_text(encoding="utf-8")
            landing_log = (
                REPO_ROOT / "mechanics" / mechanic / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")

            with self.subTest(mechanic=mechanic):
                self.assertIn("legacy scaffold", provenance)
                self.assertIn("current raw inventory is empty", provenance)
                self.assertIn("Legacy Scaffold Bridge", landing_log)
                for banned in banned_fragments:
                    self.assertNotIn(banned, provenance)

    def test_scaffold_legacy_surfaces_preserve_bridge_contract(self) -> None:
        for mechanic in LEGACY_SCAFFOLD_MECHANICS:
            legacy_root = REPO_ROOT / "mechanics" / mechanic / "legacy"
            combined = "\n".join(
                (legacy_root / relative_path).read_text(encoding="utf-8")
                for relative_path in (
                    "AGENTS.md",
                    "README.md",
                    "INDEX.md",
                    "DISTILLATION_LOG.md",
                    "raw/README.md",
                )
            )

            with self.subTest(mechanic=mechanic):
                self.assertIn("source-to-active accounting", combined)
                self.assertIn("Current raw inventory: none preserved", combined)
                self.assertIn("../PROVENANCE.md", combined)
                self.assertIn("Do not add placeholder receipts", combined)


if __name__ == "__main__":
    unittest.main()
