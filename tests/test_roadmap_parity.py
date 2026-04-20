from __future__ import annotations

import json
import unittest
from collections import Counter
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


CURRENT_RELEASE_TECHNIQUES = (
    ("AOA-T-0091", "techniques/agent-workflows/workspace-root-ingress-and-mutation-gate/TECHNIQUE.md"),
    ("AOA-T-0092", "techniques/agent-workflows/audit-to-closeout-proof-loop/TECHNIQUE.md"),
    ("AOA-T-0093", "techniques/agent-workflows/recommendation-truth-vs-host-actionability/TECHNIQUE.md"),
    ("AOA-T-0094", "techniques/docs/canonical-owner-with-validated-mirror/TECHNIQUE.md"),
    ("AOA-T-0095", "techniques/agent-workflows/github-only-owner-endcap-with-reality-sync/TECHNIQUE.md"),
    ("AOA-T-0096", "techniques/agent-workflows/pinned-validation-matrix-before-generated-publish/TECHNIQUE.md"),
    ("AOA-T-0097", "techniques/system-recovery/degrade-reground-recover/TECHNIQUE.md"),
    ("AOA-T-0098", "techniques/validation-patterns/receipt-first-failure-analysis/TECHNIQUE.md"),
    ("AOA-T-0099", "techniques/system-recovery/isolated-service-stop-on-shared-substrate/TECHNIQUE.md"),
)


CURRENT_RELEASE_SURFACES = (
    "generated/technique_promotion_readiness.min.json",
    "scripts/publish_live_receipts.py",
    "docs/VIA_NEGATIVA_CHECKLIST.md",
)


class RoadmapParityTestCase(unittest.TestCase):
    def test_promotion_readiness_matrix_matches_generated_promoted_corpus(self) -> None:
        catalog = json.loads((REPO_ROOT / "generated/technique_catalog.min.json").read_text(encoding="utf-8"))
        techniques = catalog["techniques"]
        status_counts = Counter(technique["status"] for technique in techniques)
        promoted_count = status_counts["promoted"]

        readiness_matrix = (REPO_ROOT / "docs/PROMOTION_READINESS_MATRIX.md").read_text(encoding="utf-8")

        self.assertEqual(promoted_count, 75)
        self.assertIn(f"current promoted corpus: `{promoted_count}` techniques", readiness_matrix)
        self.assertIn("`49` promoted techniques are explicitly categorized", readiness_matrix)
        self.assertIn("`26` newer `v0.4`", readiness_matrix)
        self.assertIn("`v0.4 matrix-expansion lane` | `26`", readiness_matrix)
        self.assertIn("`AOA-T-0075` through `AOA-T-0100`", readiness_matrix)

    def test_roadmap_matches_current_v0_4_0_release_contour(self) -> None:
        roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        technique_index = (REPO_ROOT / "TECHNIQUE_INDEX.md").read_text(encoding="utf-8")

        self.assertIn("Current release: `v0.4.1`", readme)
        self.assertIn("## [0.4.0]", changelog)
        self.assertIn("`v0.4.1`", roadmap)
        self.assertIn("`100` bundles", roadmap)
        self.assertIn("Roadmap drift", roadmap)
        self.assertIn("does not change technique status", roadmap)

        for technique_id, technique_path in CURRENT_RELEASE_TECHNIQUES:
            with self.subTest(technique=technique_id):
                self.assertTrue((REPO_ROOT / technique_path).is_file())
                self.assertIn(technique_id, technique_index)
                self.assertIn(technique_id, roadmap)
                self.assertIn(technique_path, roadmap)

        for surface in CURRENT_RELEASE_SURFACES:
            with self.subTest(surface=surface):
                self.assertTrue((REPO_ROOT / surface).is_file())
                self.assertIn(surface, readme)

    def test_roadmap_names_agon_wave4_companion_bridge_surfaces(self) -> None:
        roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")

        for relative_path in (
            "docs/AGON_MOVE_TECHNIQUE_BRIDGE.md",
            "docs/AGON_WAVE4_TECHNIQUE_LANDING.md",
            "generated/agon_technique_binding_candidates.min.json",
            "config/agon_technique_binding_candidates.seed.json",
            "scripts/build_agon_technique_binding_candidates.py",
            "scripts/validate_agon_technique_binding_candidates.py",
            "tests/test_agon_technique_binding_candidates.py",
        ):
            self.assertTrue((REPO_ROOT / relative_path).is_file())

        self.assertIn("AGON_MOVE_TECHNIQUE_BRIDGE", roadmap)
        self.assertIn("generated/agon_technique_binding_candidates.min.json", roadmap)
        self.assertIn("requested_not_landed", roadmap)
        self.assertIn("docs/AGON_MOVE_TECHNIQUE_BRIDGE.md", readme)


if __name__ == "__main__":
    unittest.main()
