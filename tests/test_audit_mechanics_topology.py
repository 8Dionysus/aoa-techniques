from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

ACTIVE_AUDIT_SURFACES = (
    "mechanics/audit/AGENTS.md",
    "mechanics/audit/README.md",
    "mechanics/audit/DIRECTION.md",
    "mechanics/audit/PARTS.md",
    "mechanics/audit/PROVENANCE.md",
    "mechanics/audit/LANDING_LOG.md",
    "mechanics/audit/ROADMAP.md",
    "mechanics/audit/parts/AGENTS.md",
    "mechanics/audit/parts/README.md",
    "mechanics/audit/legacy/AGENTS.md",
    "mechanics/audit/legacy/README.md",
    "mechanics/audit/legacy/INDEX.md",
    "mechanics/audit/legacy/DISTILLATION_LOG.md",
    "mechanics/audit/legacy/raw/README.md",
)

PART_LOCAL_AUDIT_READMES = (
    "mechanics/audit/parts/promotion-readiness-matrix/README.md",
    "mechanics/audit/parts/promotion-wave-a-runbook/README.md",
    "mechanics/audit/parts/external-evidence-sprint-runbook/README.md",
    "mechanics/audit/parts/external-evidence-ledger/README.md",
)

OLD_FLAT_AUDIT_FILES = (
    "mechanics/audit/PROMOTION_READINESS_MATRIX.md",
    "mechanics/audit/PROMOTION_WAVE_A_RUNBOOK.md",
    "mechanics/audit/EXTERNAL_EVIDENCE_SPRINT_RUNBOOK.md",
    "mechanics/audit/EXTERNAL_EVIDENCE_LEDGER.md",
)


class AuditMechanicsTopologyTestCase(unittest.TestCase):
    def test_audit_active_surfaces_are_discoverable(self) -> None:
        for relative_path in ACTIVE_AUDIT_SURFACES + PART_LOCAL_AUDIT_READMES:
            with self.subTest(relative_path=relative_path):
                self.assertTrue((REPO_ROOT / relative_path).is_file())

    def test_audit_flat_files_moved_into_owning_parts(self) -> None:
        for relative_path in PART_LOCAL_AUDIT_READMES:
            with self.subTest(relative_path=relative_path):
                self.assertTrue((REPO_ROOT / relative_path).is_file())

        for relative_path in OLD_FLAT_AUDIT_FILES:
            with self.subTest(relative_path=relative_path):
                self.assertFalse((REPO_ROOT / relative_path).exists())

    def test_audit_part_map_names_all_current_parts(self) -> None:
        parts = (REPO_ROOT / "mechanics" / "audit" / "PARTS.md").read_text(
            encoding="utf-8"
        )
        provenance = (
            REPO_ROOT / "mechanics" / "audit" / "PROVENANCE.md"
        ).read_text(encoding="utf-8")

        for part_name in (
            "promotion-readiness-matrix",
            "promotion-wave-a-runbook",
            "external-evidence-sprint-runbook",
            "external-evidence-ledger",
        ):
            with self.subTest(part_name=part_name):
                self.assertIn(part_name, parts)
                self.assertIn(part_name, provenance)

    def test_audit_part_local_links_use_active_paths(self) -> None:
        readiness = (
            REPO_ROOT
            / "mechanics"
            / "audit"
            / "parts"
            / "promotion-readiness-matrix"
            / "README.md"
        ).read_text(encoding="utf-8")
        sprint = (
            REPO_ROOT
            / "mechanics"
            / "audit"
            / "parts"
            / "external-evidence-sprint-runbook"
            / "README.md"
        ).read_text(encoding="utf-8")
        ledger = (
            REPO_ROOT
            / "mechanics"
            / "audit"
            / "parts"
            / "external-evidence-ledger"
            / "README.md"
        ).read_text(encoding="utf-8")

        self.assertIn("../promotion-wave-a-runbook/README.md", readiness)
        self.assertIn("../promotion-readiness-matrix/README.md", sprint)
        self.assertIn("../external-evidence-ledger/README.md", sprint)
        self.assertIn("../external-evidence-sprint-runbook/README.md", ledger)
        self.assertIn("../../../../techniques/", readiness)
        self.assertIn("../../../../techniques/", ledger)

    def test_audit_current_posture_survived_split(self) -> None:
        readiness = (
            REPO_ROOT
            / "mechanics"
            / "audit"
            / "parts"
            / "promotion-readiness-matrix"
            / "README.md"
        ).read_text(encoding="utf-8")
        wave = (
            REPO_ROOT
            / "mechanics"
            / "audit"
            / "parts"
            / "promotion-wave-a-runbook"
            / "README.md"
        ).read_text(encoding="utf-8")
        ledger = (
            REPO_ROOT
            / "mechanics"
            / "audit"
            / "parts"
            / "external-evidence-ledger"
            / "README.md"
        ).read_text(encoding="utf-8")

        self.assertIn("current promoted corpus: `82` techniques", readiness)
        self.assertIn("`82` promoted techniques are explicitly categorized", readiness)
        self.assertIn("Wave 0 matrix expansion is closed", readiness)
        self.assertIn("`v0.4 matrix-expansion lane` | `0`", readiness)
        self.assertIn("Pack 40 - Method-Growth Extraction Family", readiness)
        self.assertIn("Pack 41 - Agon Handoff Extraction Family", readiness)
        self.assertIn("no status flips during the first pass", wave)
        self.assertIn("Active Lead Ledger", ledger)
        self.assertIn("AOA-T-0032", ledger)

    def test_audit_legacy_and_decision_are_discoverable(self) -> None:
        legacy_index = (
            REPO_ROOT / "mechanics" / "audit" / "legacy" / "INDEX.md"
        ).read_text(encoding="utf-8")
        legacy_log = (
            REPO_ROOT / "mechanics" / "audit" / "legacy" / "DISTILLATION_LOG.md"
        ).read_text(encoding="utf-8")
        decision = (
            REPO_ROOT
            / "docs"
            / "decisions"
            / "2026-05-01-audit-active-parts-split.md"
        ).read_text(encoding="utf-8")

        self.assertIn("Flat `PROMOTION_READINESS_MATRIX.md`", legacy_index)
        self.assertIn("Flat files moved into active parts", legacy_log)
        self.assertIn("Audit Active Parts Split", decision)
        self.assertIn("No promotion posture", decision)


if __name__ == "__main__":
    unittest.main()
