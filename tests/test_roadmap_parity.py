from __future__ import annotations

import unittest
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
    def test_roadmap_matches_current_v0_4_0_release_contour(self) -> None:
        roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        technique_index = (REPO_ROOT / "TECHNIQUE_INDEX.md").read_text(encoding="utf-8")

        self.assertIn("Current release: `v0.4.0`", readme)
        self.assertIn("## [0.4.0]", changelog)
        self.assertIn("`v0.4.0`", roadmap)
        self.assertIn("`99` bundles", roadmap)
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


if __name__ == "__main__":
    unittest.main()
