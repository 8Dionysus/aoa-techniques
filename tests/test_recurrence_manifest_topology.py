from __future__ import annotations

import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CROSS_LAYER_README = "mechanics/distillation/parts/cross-layer-candidate-ledger/README.md"
CROSS_LAYER_REGISTRY = (
    "mechanics/distillation/parts/cross-layer-candidate-ledger/generated/"
    "cross_layer_candidate_registry.min.json"
)
RECURRENCE_MANIFEST = (
    "mechanics/recurrence/parts/live-observation-producers/manifests/recurrence/"
    "component.techniques.canon-and-intake-beacons.json"
)
RECURRENCE_HOOKS = (
    "mechanics/recurrence/parts/live-observation-producers/manifests/recurrence/"
    "hooks/component.techniques.canon-and-intake-beacons.hooks.json"
)
ROOT_RECURRENCE_MANIFEST = (
    "manifests/recurrence/component.techniques.canon-and-intake-beacons.json"
)
ROOT_RECURRENCE_HOOKS = (
    "manifests/recurrence/hooks/component.techniques.canon-and-intake-beacons.hooks.json"
)


class RecurrenceManifestTopologyTestCase(unittest.TestCase):
    def load_manifest(self) -> dict:
        return json.loads((REPO_ROOT / RECURRENCE_MANIFEST).read_text(encoding="utf-8"))

    def test_recurrence_manifests_live_under_observation_producer_part(self) -> None:
        self.assertTrue((REPO_ROOT / RECURRENCE_MANIFEST).is_file())
        self.assertTrue((REPO_ROOT / RECURRENCE_HOOKS).is_file())
        self.assertFalse((REPO_ROOT / ROOT_RECURRENCE_MANIFEST).exists())
        self.assertFalse((REPO_ROOT / ROOT_RECURRENCE_HOOKS).exists())

    def test_cross_layer_registry_is_observation_evidence_not_decision_surface(self) -> None:
        manifest = self.load_manifest()

        self.assertIn(CROSS_LAYER_README, manifest["source_inputs"])
        self.assertIn(CROSS_LAYER_REGISTRY, manifest["source_inputs"])
        self.assertIn(CROSS_LAYER_REGISTRY, manifest["generated_surfaces"])
        self.assertIn(CROSS_LAYER_README, manifest["contract_surfaces"])
        self.assertNotIn(CROSS_LAYER_REGISTRY, manifest["contract_surfaces"])
        self.assertIn(CROSS_LAYER_README, manifest["decision_surfaces"])
        self.assertNotIn(CROSS_LAYER_REGISTRY, manifest["decision_surfaces"])
        self.assertIn(CROSS_LAYER_REGISTRY, manifest["candidate_targets"])

    def test_cross_layer_observation_input_pairs_readme_and_registry(self) -> None:
        manifest = self.load_manifest()
        observation = next(
            item
            for item in manifest["observation_inputs"]
            if item["input_ref"] == "cross-layer-technique-candidates"
        )

        self.assertIn(CROSS_LAYER_README, observation["path_globs"])
        self.assertIn(CROSS_LAYER_REGISTRY, observation["path_globs"])
        self.assertIn("observation input only", observation["notes"])
        self.assertIn("not candidate or promotion authority", observation["notes"])

    def test_beacon_rules_do_not_self_authorize_from_registry(self) -> None:
        manifest = self.load_manifest()
        rules = {rule["beacon_ref"]: rule for rule in manifest["beacon_rules"]}

        self.assertIn(
            "self-authorizing technique creation",
            rules["technique.new_candidate.distillation_pressure"]["notes"],
        )
        self.assertIn(
            "cannot release",
            rules["technique.overlap_hold.guard"]["notes"],
        )

    def test_recurrence_docs_name_registry_stop_line(self) -> None:
        producers = (
            REPO_ROOT
            / "mechanics"
            / "recurrence"
            / "parts"
            / "live-observation-producers"
            / "README.md"
        ).read_text(encoding="utf-8")
        decision = (
            REPO_ROOT
            / "docs"
            / "decisions"
            / "2026-05-01-recurrence-cross-layer-registry-observation.md"
        ).read_text(encoding="utf-8")

        self.assertIn(CROSS_LAYER_REGISTRY, producers)
        self.assertIn("does not authorize promotion", producers)
        self.assertIn("observation evidence only", decision)
        self.assertIn("cannot create candidates", decision)


if __name__ == "__main__":
    unittest.main()
