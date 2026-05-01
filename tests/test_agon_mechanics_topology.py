from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

PART_LOCAL_AGON_ARTIFACTS = (
    "mechanics/agon/parts/move-technique-bridge/config/agon_technique_binding_candidates.seed.json",
    "mechanics/agon/parts/move-technique-bridge/generated/agon_technique_binding_candidates.min.json",
    "mechanics/agon/parts/move-technique-bridge/examples/agon_technique_binding_candidate.example.json",
    "mechanics/agon/parts/move-technique-bridge/schemas/agon-technique-binding-candidate.schema.json",
    "mechanics/agon/parts/move-technique-bridge/scripts/build_agon_technique_binding_candidates.py",
    "mechanics/agon/parts/move-technique-bridge/scripts/validate_agon_technique_binding_candidates.py",
    "mechanics/agon/parts/move-technique-bridge/tests/test_agon_technique_binding_candidates.py",
    "mechanics/agon/parts/epistemic-technique-candidates/config/agon_epistemic_technique_candidates.seed.json",
    "mechanics/agon/parts/epistemic-technique-candidates/generated/agon_epistemic_technique_candidates.min.json",
    "mechanics/agon/parts/epistemic-technique-candidates/examples/agon_epistemic_technique_candidate.example.json",
    "mechanics/agon/parts/epistemic-technique-candidates/schemas/agon-epistemic-technique-candidate.schema.json",
    "mechanics/agon/parts/epistemic-technique-candidates/schemas/agon-epistemic-technique-candidate-registry.schema.json",
    "mechanics/agon/parts/epistemic-technique-candidates/scripts/build_agon_epistemic_technique_candidates.py",
    "mechanics/agon/parts/epistemic-technique-candidates/scripts/validate_agon_epistemic_technique_candidates.py",
    "mechanics/agon/parts/epistemic-technique-candidates/tests/test_agon_epistemic_technique_candidates.py",
    "mechanics/agon/parts/recurrence-adapter/manifests/recurrence/component.agon.technique-binding-surfaces.json",
    "mechanics/agon/parts/recurrence-adapter/manifests/recurrence/component.agon.epistemic-technique-candidates.json",
    "mechanics/agon/parts/recurrence-adapter/manifests/recurrence/hooks/component.agon.technique-binding-surfaces.hooks.json",
    "mechanics/agon/parts/recurrence-adapter/manifests/recurrence/hooks/component.agon.epistemic-technique-candidates.hooks.json",
)

ROOT_AGON_ARTIFACTS = (
    "config/agon_technique_binding_candidates.seed.json",
    "config/agon_epistemic_technique_candidates.seed.json",
    "generated/agon_technique_binding_candidates.min.json",
    "generated/agon_epistemic_technique_candidates.min.json",
    "examples/agon_technique_binding_candidate.example.json",
    "examples/agon_epistemic_technique_candidate.example.json",
    "schemas/agon-technique-binding-candidate.schema.json",
    "schemas/agon-epistemic-technique-candidate.schema.json",
    "schemas/agon-epistemic-technique-candidate-registry.schema.json",
    "scripts/build_agon_technique_binding_candidates.py",
    "scripts/validate_agon_technique_binding_candidates.py",
    "scripts/build_agon_epistemic_technique_candidates.py",
    "scripts/validate_agon_epistemic_technique_candidates.py",
    "tests/test_agon_technique_binding_candidates.py",
    "tests/test_agon_epistemic_technique_candidates.py",
    "manifests/recurrence/component.agon.technique-binding-surfaces.json",
    "manifests/recurrence/component.agon.epistemic-technique-candidates.json",
    "manifests/recurrence/hooks/component.agon.technique-binding-surfaces.hooks.json",
    "manifests/recurrence/hooks/component.agon.epistemic-technique-candidates.hooks.json",
)


class AgonMechanicsTopologyTestCase(unittest.TestCase):
    def test_agon_artifacts_live_under_owning_parts(self) -> None:
        for relative_path in PART_LOCAL_AGON_ARTIFACTS:
            with self.subTest(relative_path=relative_path):
                self.assertTrue((REPO_ROOT / relative_path).is_file())

    def test_agon_artifacts_do_not_remain_in_root_technical_districts(self) -> None:
        for relative_path in ROOT_AGON_ARTIFACTS:
            with self.subTest(relative_path=relative_path):
                self.assertFalse((REPO_ROOT / relative_path).exists())

    def test_part_local_artifact_decision_is_discoverable(self) -> None:
        decision = (
            REPO_ROOT / "docs" / "decisions" / "2026-05-01-agon-part-local-artifacts.md"
        ).read_text(encoding="utf-8")
        self.assertIn("Move Agon-owned technical artifacts into part-local homes", decision)
        self.assertIn("mechanics/agon/parts/move-technique-bridge/", decision)
        self.assertIn("mechanics/agon/parts/epistemic-technique-candidates/", decision)
        self.assertIn("mechanics/agon/parts/recurrence-adapter/", decision)


if __name__ == "__main__":
    unittest.main()
