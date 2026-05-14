from __future__ import annotations

import re
import unittest
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[3]

PILOT_BUNDLES = (
    (
        "AOA-T-0080",
        "session-drift-taxonomy",
        "assessment",
        "techniques/agent-workflows/session-drift-taxonomy",
        "techniques/recovery/diagnosis-repair/session-drift-taxonomy",
    ),
    (
        "AOA-T-0081",
        "diagnosis-from-reviewed-evidence",
        "assessment",
        "techniques/agent-workflows/diagnosis-from-reviewed-evidence",
        "techniques/recovery/diagnosis-repair/diagnosis-from-reviewed-evidence",
    ),
    (
        "AOA-T-0082",
        "repair-shape-from-diagnosis",
        "recovery",
        "techniques/agent-workflows/repair-shape-from-diagnosis",
        "techniques/recovery/diagnosis-repair/repair-shape-from-diagnosis",
    ),
    (
        "AOA-T-0083",
        "checkpoint-bound-self-repair",
        "recovery",
        "techniques/agent-workflows/checkpoint-bound-self-repair",
        "techniques/recovery/diagnosis-repair/checkpoint-bound-self-repair",
    ),
)

LIVE_LINK_SURFACES = (
    "mechanics/audit/parts/promotion-readiness-matrix/README.md",
    "mechanics/growth-cycle/parts/stage-technique-anchors/README.md",
    "mechanics/checkpoint/PROVENANCE.md",
    "mechanics/checkpoint/parts/technique-anchors/README.md",
    "mechanics/distillation/parts/agon-candidate-handoff/gates/challenge-claim-practice.md",
    "mechanics/distillation/parts/agon-candidate-handoff/gates/request-evidence-practice.md",
    "mechanics/distillation/parts/technique-reform-ingress/reviews/0054-kind-destination-check.md",
)


def read_frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    if match is None:
        raise AssertionError(f"missing frontmatter in {path}")
    return yaml.safe_load(match.group(1))


class DiagnosisRepairTreePilotTestCase(unittest.TestCase):
    def test_pilot_bundles_live_under_recovery_tree(self) -> None:
        for technique_id, slug, _kind, old_path, new_path in PILOT_BUNDLES:
            with self.subTest(technique_id=technique_id):
                self.assertFalse((REPO_ROOT / old_path).exists())
                self.assertTrue((REPO_ROOT / new_path / "TECHNIQUE.md").is_file())
                self.assertTrue((REPO_ROOT / new_path / "checks").is_dir())
                self.assertTrue((REPO_ROOT / new_path / "examples").is_dir())
                self.assertTrue((REPO_ROOT / new_path / "notes").is_dir())
                self.assertEqual(slug, Path(new_path).name)

    def test_pilot_keeps_frontmatter_facets_unchanged(self) -> None:
        for technique_id, _slug, kind, _old_path, new_path in PILOT_BUNDLES:
            frontmatter = read_frontmatter(REPO_ROOT / new_path / "TECHNIQUE.md")

            with self.subTest(technique_id=technique_id):
                self.assertEqual(technique_id, frontmatter["id"])
                self.assertEqual("agent-workflows", frontmatter["domain"])
                self.assertEqual(kind, frontmatter["kind"])
                self.assertNotIn("tree_path", frontmatter)

    def test_recovery_trunk_has_route_card(self) -> None:
        text = (REPO_ROOT / "techniques" / "recovery" / "AGENTS.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("This is a tree trunk, not a frontmatter domain.", text)
        self.assertIn("diagnosis-repair", text)
        self.assertIn("Do not add `tree_path` frontmatter", text)
        self.assertIn("checkpoint-bound repair posture", text)

    def test_root_legacy_receipt_preserves_old_and_new_paths(self) -> None:
        receipt = (
            REPO_ROOT
            / "legacy"
            / "receipts"
            / "2026-05-04-diagnosis-repair-tree-pilot.md"
        ).read_text(encoding="utf-8")

        for technique_id, _slug, _kind, old_path, new_path in PILOT_BUNDLES:
            with self.subTest(technique_id=technique_id):
                self.assertIn(old_path, receipt)
                self.assertIn(new_path, receipt)

        self.assertIn("They did not pass through root `legacy/`.", receipt)
        self.assertIn("self-improvement", receipt)
        self.assertIn("role-law", receipt)
        self.assertIn("proof-law", receipt)

    def test_live_mechanics_links_point_to_current_paths(self) -> None:
        text = "\n".join(
            (REPO_ROOT / relative_path).read_text(encoding="utf-8")
            for relative_path in LIVE_LINK_SURFACES
        )

        for technique_id, _slug, _kind, old_path, new_path in PILOT_BUNDLES:
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
            / "diagnosis-repair-direct-read-migration-review.md"
        ).read_text(encoding="utf-8")

        for technique_id, _slug, _kind, old_path, new_path in PILOT_BUNDLES:
            with self.subTest(technique_id=technique_id):
                self.assertIn(f"{new_path}/TECHNIQUE.md", review)
                self.assertIn(old_path, review)
                self.assertIn(new_path, review)

    def test_moved_bundle_internal_links_remain_current(self) -> None:
        session_taxonomy = (
            REPO_ROOT
            / "techniques"
            / "recovery"
            / "diagnosis-repair"
            / "session-drift-taxonomy"
            / "TECHNIQUE.md"
        ).read_text(encoding="utf-8")
        checkpoint_repair = (
            REPO_ROOT
            / "techniques"
            / "recovery"
            / "diagnosis-repair"
            / "checkpoint-bound-self-repair"
            / "TECHNIQUE.md"
        ).read_text(encoding="utf-8")

        self.assertIn(
            "../../../governance/decision-routing/owner-layer-triage/TECHNIQUE.md",
            session_taxonomy,
        )
        self.assertIn(
            "../../../agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md",
            checkpoint_repair,
        )


if __name__ == "__main__":
    unittest.main()
