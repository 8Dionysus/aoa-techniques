from __future__ import annotations

import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

ACTIVE_DISTILLATION_SURFACES = (
    "mechanics/distillation/AGENTS.md",
    "mechanics/distillation/README.md",
    "mechanics/distillation/DIRECTION.md",
    "mechanics/distillation/PARTS.md",
    "mechanics/distillation/PROVENANCE.md",
    "mechanics/distillation/LANDING_LOG.md",
    "mechanics/distillation/ROADMAP.md",
    "mechanics/distillation/parts/AGENTS.md",
    "mechanics/distillation/parts/README.md",
    "mechanics/distillation/legacy/AGENTS.md",
    "mechanics/distillation/legacy/README.md",
    "mechanics/distillation/legacy/INDEX.md",
    "mechanics/distillation/legacy/DISTILLATION_LOG.md",
    "mechanics/distillation/legacy/raw/README.md",
)

RAW_DISTILLATION_RECEIPTS = (
    "mechanics/distillation/legacy/raw/EXTERNAL_CANDIDATE_LEDGER_2026-05-01_PRE_PRUNE.md",
)

PART_LOCAL_DISTILLATION_READMES = (
    "mechanics/distillation/parts/donor-refinery/README.md",
    "mechanics/distillation/parts/external-import-runbook/README.md",
    "mechanics/distillation/parts/external-candidate-ledger/README.md",
    "mechanics/distillation/parts/cross-layer-candidate-ledger/README.md",
    "mechanics/distillation/parts/long-gap-reentry/README.md",
)

OLD_FLAT_DISTILLATION_FILES = (
    "mechanics/distillation/DONOR_REFINERY_RUBRIC.md",
    "mechanics/distillation/EXTERNAL_IMPORT_RUNBOOK.md",
    "mechanics/distillation/EXTERNAL_TECHNIQUE_CANDIDATES.md",
    "mechanics/distillation/CROSS_LAYER_TECHNIQUE_CANDIDATES.md",
    "mechanics/distillation/LONG_GAP_CANON_DESIGN.md",
)


class DistillationMechanicsTopologyTestCase(unittest.TestCase):
    def test_distillation_active_surfaces_are_discoverable(self) -> None:
        for relative_path in ACTIVE_DISTILLATION_SURFACES + RAW_DISTILLATION_RECEIPTS:
            with self.subTest(relative_path=relative_path):
                self.assertTrue((REPO_ROOT / relative_path).is_file())

    def test_distillation_flat_files_moved_into_owning_parts(self) -> None:
        for relative_path in PART_LOCAL_DISTILLATION_READMES:
            with self.subTest(relative_path=relative_path):
                self.assertTrue((REPO_ROOT / relative_path).is_file())

        for relative_path in OLD_FLAT_DISTILLATION_FILES:
            with self.subTest(relative_path=relative_path):
                self.assertFalse((REPO_ROOT / relative_path).exists())

    def test_distillation_part_map_names_all_current_parts(self) -> None:
        parts = (REPO_ROOT / "mechanics" / "distillation" / "PARTS.md").read_text(
            encoding="utf-8"
        )
        provenance = (
            REPO_ROOT / "mechanics" / "distillation" / "PROVENANCE.md"
        ).read_text(encoding="utf-8")

        for part_name in (
            "donor-refinery",
            "external-import-runbook",
            "external-candidate-ledger",
            "cross-layer-candidate-ledger",
            "long-gap-reentry",
        ):
            with self.subTest(part_name=part_name):
                self.assertIn(part_name, parts)
                self.assertIn(part_name, provenance)

    def test_part_local_ledgers_preserve_current_accounting(self) -> None:
        external = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "external-candidate-ledger"
            / "README.md"
        ).read_text(encoding="utf-8")
        cross_layer = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "cross-layer-candidate-ledger"
            / "README.md"
        ).read_text(encoding="utf-8")

        self.assertIn("remaining `13` external donor-derived candidates", external)
        self.assertIn("full `24` technique-shaped candidate names", cross_layer)
        self.assertIn("`10` landed from this wave map", cross_layer)

        rows = re.findall(r"^\| `([^`]+)` \|", cross_layer, flags=re.MULTILINE)
        self.assertEqual(24, len(rows))
        self.assertEqual(24, len(set(rows)))

    def test_external_candidate_ledger_marks_missing_seed_sources(self) -> None:
        external = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "external-candidate-ledger"
            / "README.md"
        ).read_text(encoding="utf-8")
        receipt = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "legacy"
            / "raw"
            / "EXTERNAL_CANDIDATE_LEDGER_2026-05-01_PRE_PRUNE.md"
        ).read_text(encoding="utf-8")

        self.assertIn("## Source Status", external)
        self.assertIn("historical source\nlabels", external)
        self.assertIn("did not find checked-out", external)
        self.assertIn("seeds/seed_4.txt", external)
        self.assertIn("seeds/seed_6.txt", external)
        self.assertIn("remaining `13` external donor-derived candidates", receipt)
        self.assertNotIn("## Source Status", receipt)

    def test_distillation_active_parts_decision_is_discoverable(self) -> None:
        decision = (
            REPO_ROOT
            / "docs"
            / "decisions"
            / "2026-05-01-distillation-active-parts-split.md"
        ).read_text(encoding="utf-8")

        self.assertIn("Distillation Active Parts Split", decision)
        self.assertIn("mechanics/distillation/parts/", decision)
        self.assertIn("No candidate verdicts, ledger counts, or technique statuses", decision)


if __name__ == "__main__":
    unittest.main()
