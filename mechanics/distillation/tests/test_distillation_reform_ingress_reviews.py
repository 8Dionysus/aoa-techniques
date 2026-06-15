from __future__ import annotations

import sys
import unittest
from pathlib import Path


SUPPORT_DIR = Path(__file__).resolve().parent / "support"
if str(SUPPORT_DIR) not in sys.path:
    sys.path.insert(0, str(SUPPORT_DIR))

from distillation_topology_fixtures import *  # noqa: F403


class DistillationReformIngressReviewsTests(unittest.TestCase):
    def test_reform_context_excludes_individual_review_packets(self) -> None:
        review_root = (
            REPO_ROOT
            / "mechanics"
            / "distillation"
            / "parts"
            / "technique-reform-ingress"
            / "reviews"
        )
        source_paths = set(distillation_reform_context_paths())
        individual_review_packets = set(review_root.glob("*.md")) - {review_root / "README.md"}

        self.assertIn(review_root / "README.md", source_paths)
        self.assertTrue(individual_review_packets)
        self.assertTrue(individual_review_packets.isdisjoint(source_paths))

    def test_technique_reform_ingress_is_bounded_before_schema_change(self) -> None:
            ingress = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "README.md"
            ).read_text(encoding="utf-8")
            decision = (
                REPO_ROOT
                / "docs"
                / "decisions"
                / "AOA-TECH-D-0035-technique-reform-ingress-packet.md"
            ).read_text(encoding="utf-8")

            self.assertIn("not a schema migration", ingress)
            self.assertIn("public corpus: `107` bundles, `98` canonical, `9` promoted", ingress)
            self.assertIn("authoritative frontmatter axes: `domain`, `kind`", ingress)
            self.assertIn("first_narrowing_frontier", ingress)
            for axis in (
                "family",
                "capability_class",
                "substrate",
                "execution_profile",
                "risk_posture",
            ):
                self.assertIn(axis, ingress)
            self.assertIn("Do not add new required frontmatter fields", ingress)
            self.assertIn("Do not add new `kind` values from handoff cues", ingress)
            self.assertIn("prevents generated evidence", decision)
            self.assertIn("remapping bundle meaning", decision)

    def test_technique_reform_review_pack_preserves_scout_boundary(self) -> None:
            ingress = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "README.md"
            ).read_text(encoding="utf-8")
            review = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "first-topology-scout-review-pack.md"
            ).read_text(encoding="utf-8")

            self.assertIn("topology scout review pack", ingress)
            self.assertIn("not a schema migration", review)
            self.assertIn("Technique Topology Scout", review)
            self.assertIn("`107` techniques", review)
            self.assertIn("`orchestration-required` has `52`", review)
            self.assertIn("`small-agent` has `36`", review)
            self.assertIn("`medium-agent` has `19`", review)
            self.assertIn("`read-only` appears on `65`", review)
            self.assertIn("`mutating` on `25`", review)
            self.assertIn("does not remap any bundle", review)
            self.assertIn("direct bundle reading", review)
            self.assertIn("kind ambiguity review pack", review)

    def test_kind_ambiguity_review_pack_uses_direct_bundle_reading(self) -> None:
            review = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "first-kind-ambiguity-review-pack.md"
            ).read_text(encoding="utf-8")

            self.assertIn("first shortlist remap wave closed", review)
            self.assertIn("did not change bundle frontmatter by itself", review)
            self.assertIn("direct-read", review)
            self.assertIn("`AOA-T-0005`", review)
            self.assertIn("second shortlist remap landed", review)
            self.assertIn("`AOA-T-0085`", review)
            self.assertIn("first shortlist remap landed", review)
            self.assertIn("`AOA-T-0052`", review)
            self.assertIn("final shortlist remap landed", review)
            self.assertIn("Keep `guardrail`", review)
            self.assertIn("Keep `lift`", review)
            self.assertIn("Keep `assessment`", review)
            self.assertIn("Do not change frontmatter from this review alone", review)
            self.assertIn("fresh kind ambiguity read", review)

    def test_second_kind_ambiguity_review_pack_routes_0054_without_remap(self) -> None:
            ingress = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "README.md"
            ).read_text(encoding="utf-8")
            review = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "second-kind-ambiguity-review-pack.md"
            ).read_text(encoding="utf-8")

            self.assertIn("Second Kind Ambiguity Review Pack", review)
            self.assertIn("updated `mechanics/distillation/parts/technique-reform-ingress/reports/kind_ambiguity_audit.md`", review)
            self.assertIn("does not change frontmatter", review)
            self.assertIn("`AOA-T-0054`", review)
            self.assertIn("compaction-resilient-skill-loading", review)
            self.assertIn("`handoff`", review)
            self.assertIn("`workflow`", review)
            self.assertIn("`recovery`", review)
            self.assertIn("destination check", review)
            self.assertIn("first shortlist remap wave is closed", review)
            self.assertIn("Keep `guardrail`", review)
            self.assertIn("Keep `lift`", review)
            self.assertIn("Keep `assessment`", review)
            self.assertIn("Second Kind Ambiguity Review Pack", ingress)
            self.assertIn("`AOA-T-0054`", ingress)
            self.assertIn("0054-kind-destination-check", review)

    def test_0085_kind_remap_landed_without_status_change(self) -> None:
            catalog = json.loads(
                (REPO_ROOT / "generated" / "technique_catalog.json").read_text(
                    encoding="utf-8"
                )
            )
            technique = next(
                entry for entry in catalog["techniques"] if entry["id"] == "AOA-T-0085"
            )
            decision = (
                REPO_ROOT
                / "docs"
                / "decisions"
                / "AOA-TECH-D-0039-0085-kind-remap.md"
            ).read_text(encoding="utf-8")

            self.assertEqual("agent-workflows", technique["domain"])
            self.assertEqual("lift", technique["kind"])
            self.assertEqual("canonical", technique["status"])
            self.assertIn("Remap `AOA-T-0085` from `artifact` to `lift`", decision)
            self.assertIn("classification correction only", decision)

    def test_0005_kind_remap_landed_without_status_change(self) -> None:
            catalog = json.loads(
                (REPO_ROOT / "generated" / "technique_catalog.json").read_text(
                    encoding="utf-8"
                )
            )
            technique = next(
                entry for entry in catalog["techniques"] if entry["id"] == "AOA-T-0005"
            )
            decision = (
                REPO_ROOT
                / "docs"
                / "decisions"
                / "AOA-TECH-D-0036-0005-kind-remap.md"
            ).read_text(encoding="utf-8")

            self.assertEqual("agent-workflows", technique["domain"])
            self.assertEqual("workflow", technique["kind"])
            self.assertEqual("promoted", technique["status"])
            self.assertIn("Remap `AOA-T-0005` from `guardrail` to `workflow`", decision)
            self.assertIn("classification correction only", decision)

    def test_0052_kind_remap_remains_classification_only_after_later_promotion(self) -> None:
            catalog = json.loads(
                (REPO_ROOT / "generated" / "technique_catalog.json").read_text(
                    encoding="utf-8"
                )
            )
            technique = next(
                entry for entry in catalog["techniques"] if entry["id"] == "AOA-T-0052"
            )
            decision = (
                REPO_ROOT
                / "docs"
                / "decisions"
                / "AOA-TECH-D-0037-0052-kind-remap.md"
            ).read_text(encoding="utf-8")

            self.assertEqual("agent-workflows", technique["domain"])
            self.assertEqual("workflow", technique["kind"])
            self.assertEqual("canonical", technique["status"])
            self.assertIn("Remap `AOA-T-0052` from `handoff` to `workflow`", decision)
            self.assertIn("classification correction only", decision)
            self.assertIn("`validation`", decision)
            self.assertIn("`lift`", decision)

    def test_0054_kind_remap_remains_classification_only_after_later_promotion(self) -> None:
            catalog = json.loads(
                (REPO_ROOT / "generated" / "technique_catalog.json").read_text(
                    encoding="utf-8"
                )
            )
            technique = next(
                entry for entry in catalog["techniques"] if entry["id"] == "AOA-T-0054"
            )
            decision = (
                REPO_ROOT
                / "docs"
                / "decisions"
                / "AOA-TECH-D-0038-0054-kind-remap.md"
            ).read_text(encoding="utf-8")
            destination_check = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "0054-kind-destination-check.md"
            ).read_text(encoding="utf-8")

            self.assertEqual("agent-workflows", technique["domain"])
            self.assertEqual("recovery", technique["kind"])
            self.assertEqual("canonical", technique["status"])
            self.assertIn("Remap `AOA-T-0054` from `handoff` to `recovery`", decision)
            self.assertIn("classification correction only", decision)
            self.assertIn("`workflow`", decision)
            self.assertIn("Remap `AOA-T-0054` from `handoff` to `recovery`", destination_check)
            self.assertIn("`AOA-T-0057`", destination_check)

    def test_post_0054_kind_audit_hold_review_closes_remap_lane(self) -> None:
            ingress = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "README.md"
            ).read_text(encoding="utf-8")
            reviews_index = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "README.md"
            ).read_text(encoding="utf-8")
            review = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "post-0054-kind-audit-hold-review.md"
            ).read_text(encoding="utf-8")
            roadmap = read_distillation_reform_context()

            self.assertIn("Post-0054 Kind Audit Hold Review", review)
            self.assertIn("No new `kind` frontmatter candidate", review)
            self.assertIn("remap lane closed", review)
            self.assertIn("family shelf review", review)
            self.assertIn("Do not reopen a candidate merely because", review)
            self.assertIn("`workflow` vs `guardrail`", review)
            self.assertIn("`validation` vs `assessment`", review)
            self.assertIn("`artifact` vs `lift`", review)
            self.assertIn("`handoff` vs `workflow`", review)
            self.assertIn("post-0054-kind-audit-hold-review", reviews_index)
            self.assertIn("Post-0054 Kind Audit Hold Review", ingress)
            self.assertIn("family shelf review", roadmap)

    def test_family_shelf_review_pack_prepares_tree_projection_without_migration(self) -> None:
            ingress = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "README.md"
            ).read_text(encoding="utf-8")
            reviews_index = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "README.md"
            ).read_text(encoding="utf-8")
            review = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "first-family-shelf-review-pack.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()

            self.assertIn("First Family Shelf Review Pack", review)
            self.assertIn("review-pack-landed", review)
            self.assertIn("not frontmatter truth", review)
            self.assertIn("not path migration", review)
            self.assertIn("`26` scout families", review)
            self.assertIn("Stable Shelf Candidates", review)
            self.assertIn("Boundary Watch", review)
            self.assertIn("Split Pressure", review)
            self.assertIn("singleton-hold", review)
            self.assertIn("`automation-governance`", review)
            self.assertIn("split-review-needed", review)
            self.assertIn("non-authoritative tree projection", review)
            self.assertIn("Do not add `family` frontmatter", review)
            self.assertIn("Do not move bundle directories", review)
            self.assertIn("proposed `trunk`", review)
            self.assertIn("proposed `shelf`", review)
            for trunk in (
                "`execution`",
                "`instruction`",
                "`proof`",
                "`continuity`",
                "`governance`",
                "`knowledge-lift`",
                "`ingest`",
                "`recovery`",
                "`history`",
                "`tool-use`",
            ):
                with self.subTest(trunk=trunk):
                    self.assertIn(trunk, review)

            self.assertIn("first-family-shelf-review-pack", reviews_index)
            self.assertIn("family shelf review: landed", ingress)
            self.assertIn("non-authoritative tree projection", ingress)
            self.assertIn("First Family Shelf Review Pack", ingress)
            self.assertIn("first family shelf review pack", distillation_roadmap)
            self.assertIn("technique_tree_projection.md", root_roadmap)
            self.assertIn("family shelf review", tree_contract)

    def test_tree_projection_review_pack_selects_direct_read_pilot_without_migration(self) -> None:
            ingress = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "README.md"
            ).read_text(encoding="utf-8")
            reviews_index = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "README.md"
            ).read_text(encoding="utf-8")
            review = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "first-tree-projection-review-pack.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()

            self.assertIn("First Tree Projection Review Pack", review)
            self.assertIn("review-pack-landed", review)
            self.assertIn("not path migration", review)
            self.assertIn("not `tree_path` frontmatter", review)
            self.assertIn("all `107` current bundles", review)
            self.assertIn("`34` `pilot-candidate`", review)
            self.assertIn("`41` `candidate`", review)
            self.assertIn("`22` `boundary-watch`", review)
            self.assertIn("| `split-review-needed` | `9` |", review)
            self.assertIn("| `singleton-hold` | `1` |", review)
            self.assertIn("Choose `review-compaction`", review)
            self.assertIn("`AOA-T-0051`", review)
            self.assertIn("`AOA-T-0052`", review)
            self.assertIn("`AOA-T-0054`", review)
            self.assertIn("Backup Pilot", review)
            self.assertIn("Do not move `review-compaction` from this review alone", review)
            self.assertIn("direct-read migration review", review)

            self.assertIn("first-tree-projection-review-pack", reviews_index)
            self.assertIn("tree projection: landed", ingress)
            self.assertIn("first tree projection review: landed", ingress)
            self.assertIn("review-compaction", ingress)
            self.assertIn("direct-read migration review", distillation_roadmap)
            self.assertIn("review-compaction", root_roadmap)
            self.assertIn("mechanics/distillation/parts/technique-reform-ingress/reports/technique_tree_projection.md", tree_contract)


if __name__ == "__main__":
    unittest.main()
