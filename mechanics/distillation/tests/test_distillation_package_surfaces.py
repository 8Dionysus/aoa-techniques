from __future__ import annotations

import sys
import unittest
from pathlib import Path


SUPPORT_DIR = Path(__file__).resolve().parent / "support"
if str(SUPPORT_DIR) not in sys.path:
    sys.path.insert(0, str(SUPPORT_DIR))

from distillation_topology_fixtures import *  # noqa: F403


class DistillationPackageSurfacesTests(unittest.TestCase):
    def test_distillation_active_surfaces_are_discoverable(self) -> None:
            for relative_path in (
                ACTIVE_DISTILLATION_SURFACES
                + RAW_DISTILLATION_RECEIPTS
                + PART_LOCAL_EXTERNAL_CANDIDATE_REGISTRY_ARTIFACTS
                + PART_LOCAL_CROSS_LAYER_CANDIDATE_REGISTRY_ARTIFACTS
                + PART_LOCAL_AGON_CANDIDATE_HANDOFF_ARTIFACTS
                + PART_LOCAL_TECHNIQUE_REFORM_INGRESS_ARTIFACTS
            ):
                with self.subTest(relative_path=relative_path):
                    self.assertTrue((REPO_ROOT / relative_path).is_file())

    def test_distillation_flat_files_moved_into_owning_parts(self) -> None:
            for relative_path in PART_LOCAL_DISTILLATION_READMES:
                with self.subTest(relative_path=relative_path):
                    self.assertTrue((REPO_ROOT / relative_path).is_file())

            for relative_path in OLD_FLAT_DISTILLATION_FILES:
                with self.subTest(relative_path=relative_path):
                    self.assertFalse((REPO_ROOT / relative_path).exists())

    def test_technique_reform_scout_inputs_live_under_ingress_part(self) -> None:
            part_root = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
            )
            expected_files = (
                part_root / "config" / "technique_family_scout.yaml",
                part_root / "config" / "technique_topology_axes.yaml",
                part_root / "data" / "technique_kind_overlay.yaml",
                part_root / "data" / "technique_kind_overlay.csv",
            )
            old_root_files = (
                REPO_ROOT / "config" / "technique_family_scout.yaml",
                REPO_ROOT / "config" / "technique_topology_axes.yaml",
                REPO_ROOT / "data" / "technique_kind_overlay.yaml",
                REPO_ROOT / "data" / "technique_kind_overlay.csv",
            )

            self.assertTrue((REPO_ROOT / "config" / "technique_kind_registry.yaml").is_file())
            for expected_file in expected_files:
                with self.subTest(expected_file=expected_file):
                    self.assertTrue(expected_file.is_file())
            for old_root_file in old_root_files:
                with self.subTest(old_root_file=old_root_file):
                    self.assertFalse(old_root_file.exists())

    def test_technique_reform_scout_input_routes_are_documented(self) -> None:
            part_readme = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "README.md"
            ).read_text(encoding="utf-8")
            parts = (REPO_ROOT / "mechanics" / "distillation" / "PARTS.md").read_text(
                encoding="utf-8"
            )
            provenance = (
                REPO_ROOT / "mechanics" / "distillation" / "PROVENANCE.md"
            ).read_text(encoding="utf-8")
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")

            for required in (
                "config/technique_family_scout.yaml",
                "config/technique_topology_axes.yaml",
                "data/technique_kind_overlay.yaml",
            ):
                with self.subTest(required=required):
                    self.assertIn(required, part_readme)

            self.assertIn("scout config", parts)
            self.assertIn("overlay data", parts)
            self.assertIn("part-local family/topology scout inputs", provenance)
            self.assertIn("Technique reform scout input homes", landing_log)
            self.assertIn("root `config/technique_kind_registry.yaml` remains", landing_log)

    def test_technique_reform_one_owner_scripts_live_under_ingress_part(self) -> None:
            part_scripts = (
                "mechanics/distillation/parts/technique-reform-ingress/scripts/build_topology_scout.py",
                "mechanics/distillation/parts/technique-reform-ingress/scripts/build_tree_projection.py",
            )
            old_root_scripts = (
                "scripts/build_topology_scout.py",
                "scripts/build_tree_projection.py",
            )

            for relative_path in part_scripts:
                with self.subTest(relative_path=relative_path):
                    self.assertTrue((REPO_ROOT / relative_path).is_file())

            for relative_path in old_root_scripts:
                with self.subTest(relative_path=relative_path):
                    self.assertFalse((REPO_ROOT / relative_path).exists())

            parts = (REPO_ROOT / "mechanics" / "distillation" / "PARTS.md").read_text(
                encoding="utf-8"
            )
            provenance = (
                REPO_ROOT / "mechanics" / "distillation" / "PROVENANCE.md"
            ).read_text(encoding="utf-8")
            scripts_agents = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "scripts"
                / "AGENTS.md"
            ).read_text(encoding="utf-8")

            self.assertIn("scout scripts", parts)
            self.assertIn("part-local scout scripts", provenance)
            self.assertIn("one-owner technique-reform report builders", scripts_agents)

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
                "agon-candidate-handoff",
                "technique-reform-ingress",
                "long-gap-reentry",
            ):
                with self.subTest(part_name=part_name):
                    self.assertIn(part_name, parts)
                    self.assertIn(part_name, provenance)


if __name__ == "__main__":
    unittest.main()
