from __future__ import annotations

import sys
import unittest
from pathlib import Path


SUPPORT_DIR = Path(__file__).resolve().parent / "support"
if str(SUPPORT_DIR) not in sys.path:
    sys.path.insert(0, str(SUPPORT_DIR))

from distillation_topology_fixtures import *  # noqa: F403


class DistillationTreePilotCapabilityWaveTests(unittest.TestCase):
    def test_capability_registry_direct_read_review_accepts_eighth_pilot(
            self,
        ) -> None:
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
                / "capability-registry-direct-read-migration-review.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Capability-Registry Direct-Read Migration Review", review)
            self.assertIn("accepted-for-eighth-migration-pilot", review)
            self.assertIn("not path migration", review)
            self.assertIn("not\n`tree_path` frontmatter", review)
            self.assertIn("Accept `capability-registry` as the eighth", review)
            self.assertIn("spec-entry-query chain", review)
            self.assertIn("Direct Bundle Read", review)
            for technique_id in ("AOA-T-0025", "AOA-T-0063", "AOA-T-0064"):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)

            self.assertIn("Move exactly these three bundles", review)
            self.assertIn("techniques/instruction/capability-registry/", review)
            self.assertIn("Do not move files from this review pack alone", review)
            self.assertIn("Do not add `tree_path`", review)
            self.assertIn("registry product doctrine", review)
            self.assertIn("Do not collapse the three leaves into one technique", review)
            self.assertIn("Run the eighth pilot migration", review)

            self.assertIn("capability-registry-direct-read-migration-review", reviews_index)
            self.assertIn("capability-registry direct-read review: landed", ingress)
            self.assertIn("accepted-for-eighth-migration-pilot", ingress)
            self.assertIn("capability-registry migration: landed", ingress)
            self.assertIn("accepted-for-eighth-migration-pilot", distillation_roadmap)
            self.assertIn("eighth pilot migration is landed", distillation_roadmap)
            self.assertIn("Capability-registry direct-read migration review", landing_log)
            self.assertIn("Capability-registry tree pilot migration", landing_log)
            self.assertIn("spec-entry-query chain", landing_log)
            self.assertIn(
                "accepted the `capability-registry` direct-read migration review",
                changelog,
            )
            self.assertIn(
                "moved `AOA-T-0025`, `AOA-T-0063`, and `AOA-T-0064` into",
                changelog,
            )
            self.assertIn(
                "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
                root_roadmap,
            )
            self.assertIn("Capability-Registry Direct-Read Migration Review", tree_contract)
            self.assertIn("2026-05-04-capability-registry-tree-pilot.md", tree_contract)
            self.assertIn("AOA-T-0025`, `AOA-T-0063", tree_contract)
            self.assertTrue(
                (
                    REPO_ROOT
                    / "techniques"
                    / "instruction"
                    / "capability-registry"
                    / "capability-spec-versioning"
                    / "TECHNIQUE.md"
                ).is_file()
            )
            self.assertFalse(
                (
                    REPO_ROOT
                    / "techniques"
                    / "docs"
                    / "capability-spec-versioning"
                ).exists()
            )

    def test_landed_capability_registry_pilot_review_selects_capability_boundary(
            self,
        ) -> None:
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
                / "landed-capability-registry-pilot-review.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Landed Capability-Registry Pilot Review", review)
            self.assertIn("pilot-validated", review)
            self.assertIn("choose `capability-boundary`", review)
            self.assertIn("not path migration", review)
            self.assertIn("third successful shelf under the `instruction` trunk", review)
            self.assertIn("What The Eighth Pilot Proved", review)
            self.assertIn("Ninth Shelf Choice", review)
            for technique_id in ("AOA-T-0040", "AOA-T-0043", "AOA-T-0093"):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)

            self.assertIn("Projected shelf", review)
            self.assertIn("techniques/instruction/capability-boundary/", review)
            self.assertIn("Why direct-read first", review)
            self.assertIn(
                "Do not move `capability-boundary` from this review alone",
                review,
            )
            self.assertIn("Do not add `tree_path`", review)
            self.assertIn("Run a direct-read migration review for `capability-boundary`", review)

            self.assertIn("landed-capability-registry-pilot-review", reviews_index)
            self.assertIn("landed capability-registry pilot review: landed", ingress)
            self.assertIn("capability-boundary", ingress)
            self.assertIn("direct-read migration review", ingress)
            self.assertIn("capability-boundary` for the next direct-read", distillation_roadmap)
            self.assertIn("ninth pilot migration is now landed exactly", distillation_roadmap)
            self.assertIn("Landed capability-registry pilot review", landing_log)
            self.assertIn("third successful instruction trunk shelf", landing_log)
            self.assertIn(
                "accepted the landed `capability-registry` pilot review",
                changelog,
            )
            self.assertIn(
                "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
                root_roadmap,
            )
            self.assertIn("Landed Capability-Registry Pilot Review", tree_contract)
            self.assertIn("capability-boundary", tree_contract)
            self.assertFalse(
                (
                    REPO_ROOT
                    / "techniques"
                    / "docs"
                    / "skill-vs-command-boundary"
                    / "TECHNIQUE.md"
                ).is_file()
            )
            self.assertTrue(
                (
                    REPO_ROOT
                    / "techniques"
                    / "instruction"
                    / "capability-boundary"
                    / "skill-vs-command-boundary"
                    / "TECHNIQUE.md"
                ).is_file()
            )
            self.assertFalse(
                (
                    REPO_ROOT
                    / "techniques"
                    / "agent-workflows"
                    / "recommendation-truth-vs-host-actionability"
                    / "TECHNIQUE.md"
                ).is_file()
            )
            self.assertTrue(
                (
                    REPO_ROOT
                    / "techniques"
                    / "instruction"
                    / "capability-boundary"
                    / "recommendation-truth-vs-host-actionability"
                    / "TECHNIQUE.md"
                ).is_file()
            )

    def test_capability_boundary_direct_read_review_accepts_ninth_pilot(
            self,
        ) -> None:
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
                / "capability-boundary-direct-read-migration-review.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Capability-Boundary Direct-Read Migration Review", review)
            self.assertIn("accepted-for-ninth-migration-pilot", review)
            self.assertIn("not path migration", review)
            self.assertIn("not\n`tree_path` frontmatter", review)
            self.assertIn("Accept `capability-boundary` as the ninth", review)
            self.assertIn("Direct Bundle Read", review)
            for technique_id in ("AOA-T-0040", "AOA-T-0043", "AOA-T-0093"):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)

            self.assertIn("all three are promoted guardrails", review.lower())
            self.assertIn("Instruction Trunk Fit", review)
            self.assertIn("Boundary Watch Accepted", review)
            self.assertIn("Move exactly these three bundles", review)
            self.assertIn("techniques/instruction/capability-boundary/", review)
            self.assertIn("skill-discovery` should wait", review)
            self.assertIn("Do not move files from this review pack alone", review)
            self.assertIn("Do not add `tree_path`", review)
            self.assertIn("Do not collapse the three leaves", review)
            self.assertIn("Run the ninth pilot migration", review)

            self.assertIn("capability-boundary-direct-read-migration-review", reviews_index)
            self.assertIn("capability-boundary direct-read review: landed", ingress)
            self.assertIn("accepted-for-ninth-migration-pilot", ingress)
            self.assertIn("Capability-boundary direct-read migration review", landing_log)
            self.assertIn("shared capability-boundary guardrail cluster", landing_log)
            self.assertIn("accepted-for-ninth-migration-pilot", distillation_roadmap)
            self.assertIn("ninth pilot migration is now landed exactly", distillation_roadmap)
            self.assertIn(
                "accepted the `capability-boundary` direct-read migration review",
                changelog,
            )
            self.assertIn(
                "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
                root_roadmap,
            )
            self.assertIn("Capability-Boundary Direct-Read Migration Review", tree_contract)
            self.assertIn("AOA-T-0040`, `AOA-T-0043`, and `AOA-T-0093", tree_contract)
            self.assertFalse(
                (
                    REPO_ROOT
                    / "techniques"
                    / "docs"
                    / "skill-vs-command-boundary"
                    / "TECHNIQUE.md"
                ).is_file()
            )
            self.assertTrue(
                (
                    REPO_ROOT
                    / "techniques"
                    / "instruction"
                    / "capability-boundary"
                    / "skill-vs-command-boundary"
                    / "TECHNIQUE.md"
                ).is_file()
            )
            self.assertFalse(
                (
                    REPO_ROOT
                    / "techniques"
                    / "agent-workflows"
                    / "recommendation-truth-vs-host-actionability"
                    / "TECHNIQUE.md"
                ).is_file()
            )
            self.assertTrue(
                (
                    REPO_ROOT
                    / "techniques"
                    / "instruction"
                    / "capability-boundary"
                    / "recommendation-truth-vs-host-actionability"
                    / "TECHNIQUE.md"
                ).is_file()
            )

    def test_capability_boundary_tree_pilot_migration_is_recorded(self) -> None:
            ingress = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "README.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
            receipt = (
                REPO_ROOT
                / "legacy"
                / "receipts"
                / "2026-05-04-capability-boundary-tree-pilot.md"
            ).read_text(encoding="utf-8")

            self.assertIn("capability-boundary migration: landed exactly", ingress)
            self.assertIn("Capability-Boundary Tree Pilot Receipt", ingress)
            self.assertIn("Capability-boundary tree pilot migration", landing_log)
            self.assertIn("ninth pilot migration is now landed exactly", distillation_roadmap)
            self.assertIn(
                "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
                root_roadmap,
            )
            self.assertIn("ninth pilot migration moves exactly", tree_contract)
            self.assertIn("2026-05-04-capability-boundary-tree-pilot.md", tree_contract)
            self.assertIn("moved `AOA-T-0040`, `AOA-T-0043`, and `AOA-T-0093`", changelog)
            self.assertIn("They did not pass through root `legacy/`.", receipt)
            self.assertIn("Do not add `tree_path` frontmatter.", receipt)

            for relative_path in (
                "techniques/instruction/capability-boundary/skill-vs-command-boundary/TECHNIQUE.md",
                "techniques/instruction/capability-boundary/multi-source-primary-input-provenance/TECHNIQUE.md",
                "techniques/instruction/capability-boundary/recommendation-truth-vs-host-actionability/TECHNIQUE.md",
            ):
                with self.subTest(relative_path=relative_path):
                    self.assertTrue((REPO_ROOT / relative_path).is_file())

    def test_landed_capability_boundary_pilot_review_selects_skill_discovery(
            self,
        ) -> None:
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
                / "landed-capability-boundary-pilot-review.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Landed Capability-Boundary Pilot Review", review)
            self.assertIn("pilot-validated", review)
            self.assertIn("fourth successful shelf under the `instruction` trunk", review)
            self.assertIn("What The Ninth Pilot Proved", review)
            self.assertIn("Tenth Shelf Choice", review)
            self.assertIn("Choose `skill-discovery`", review)
            self.assertIn("AOA-T-0041", review)
            self.assertIn("AOA-T-0042", review)
            self.assertIn("techniques/instruction/skill-discovery/", review)
            self.assertIn("Why direct-read first", review)
            self.assertIn("Do not move `skill-discovery` from this review alone", review)
            self.assertIn("Do not add `tree_path`", review)
            self.assertIn("Run a direct-read migration review for `skill-discovery`", review)

            self.assertIn("landed-capability-boundary-pilot-review", reviews_index)
            self.assertIn("landed capability-boundary pilot review: landed", ingress)
            self.assertIn("skill-discovery` chosen", ingress)
            self.assertIn("Landed capability-boundary pilot review", landing_log)
            self.assertIn("fourth successful instruction trunk shelf", landing_log)
            self.assertIn("skill-discovery` for the next direct-read", distillation_roadmap)
            self.assertIn(
                "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
                root_roadmap,
            )
            self.assertIn("Landed Capability-Boundary Pilot Review", tree_contract)
            self.assertIn("Skill-Discovery Direct-Read Migration Review", tree_contract)
            self.assertIn(
                "accepted the landed `capability-boundary` pilot review",
                changelog,
            )
            self.assertFalse(
                (
                    REPO_ROOT
                    / "techniques"
                    / "docs"
                    / "skill-marketplace-curation"
                    / "TECHNIQUE.md"
                ).is_file()
            )
            self.assertFalse(
                (
                    REPO_ROOT
                    / "techniques"
                    / "evaluation"
                    / "upstream-skill-health-checking"
                    / "TECHNIQUE.md"
                ).is_file()
            )
            self.assertTrue(
                (
                    REPO_ROOT
                    / "techniques"
                    / "instruction"
                    / "skill-discovery"
                ).exists()
            )

    def test_skill_discovery_direct_read_review_accepts_tenth_pilot(
            self,
        ) -> None:
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
                / "skill-discovery-direct-read-migration-review.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
            flat_distillation_roadmap = " ".join(distillation_roadmap.split())

            self.assertIn("Skill-Discovery Direct-Read Migration Review", review)
            self.assertIn("accepted-for-tenth-migration-pilot", review)
            self.assertIn("not path migration", review)
            self.assertIn("not\n`tree_path` frontmatter", review)
            self.assertIn("Accept `skill-discovery` as the tenth", review)
            self.assertIn("Direct Bundle Read", review)
            for technique_id in ("AOA-T-0041", "AOA-T-0042"):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)

            self.assertIn("techniques/docs/skill-marketplace-curation/", review)
            self.assertIn(
                "techniques/evaluation/upstream-skill-health-checking/",
                review,
            )
            self.assertIn("Instruction Trunk Fit", review)
            self.assertIn("Boundary Watch Accepted", review)
            self.assertIn("Move exactly these two bundles", review)
            self.assertIn("techniques/instruction/skill-discovery/", review)
            self.assertIn("Do not move files from this review pack alone", review)
            self.assertIn("Do not add `tree_path`", review)
            self.assertIn("Do not collapse curated marketplace discoverability", review)
            self.assertIn("Run the tenth pilot migration", review)

            self.assertIn("skill-discovery-direct-read-migration-review", reviews_index)
            self.assertIn("skill-discovery direct-read review: landed", ingress)
            self.assertIn("accepted-for-tenth-migration-pilot", ingress)
            self.assertIn("Skill-discovery direct-read migration review", landing_log)
            self.assertIn("shared skill-surfacing shelf", landing_log)
            self.assertIn("accepted-for-tenth-migration-pilot", distillation_roadmap)
            self.assertIn("tenth pilot migration is now landed exactly", flat_distillation_roadmap)
            self.assertIn(
                "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
                root_roadmap,
            )
            self.assertIn("Skill-Discovery Direct-Read Migration Review", tree_contract)
            self.assertIn("AOA-T-0041` and `AOA-T-0042", tree_contract)
            self.assertIn("2026-05-05-skill-discovery-tree-pilot.md", tree_contract)
            self.assertIn(
                "accepted the `skill-discovery` direct-read migration review",
                changelog,
            )
            self.assertIn("moved `AOA-T-0041` and `AOA-T-0042`", changelog)
            self.assertFalse(
                (
                    REPO_ROOT
                    / "techniques"
                    / "docs"
                    / "skill-marketplace-curation"
                    / "TECHNIQUE.md"
                ).is_file()
            )
            self.assertFalse(
                (
                    REPO_ROOT
                    / "techniques"
                    / "evaluation"
                    / "upstream-skill-health-checking"
                    / "TECHNIQUE.md"
                ).is_file()
            )
            self.assertTrue(
                (
                    REPO_ROOT
                    / "techniques"
                    / "instruction"
                    / "skill-discovery"
                ).exists()
            )

    def test_landed_skill_discovery_pilot_review_selects_skill_support(
            self,
        ) -> None:
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
                / "landed-skill-discovery-pilot-review.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            flat_distillation_roadmap = " ".join(distillation_roadmap.split())
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Landed Skill-Discovery Pilot Review", review)
            self.assertIn("pilot-validated", review)
            self.assertIn("fifth successful shelf under the `instruction` trunk", review)
            self.assertIn("What The Tenth Pilot Proved", review)
            self.assertIn("Remaining Weaknesses", review)
            self.assertIn("Eleventh Shelf Choice", review)
            self.assertIn("Choose `skill-support`", review)
            for technique_id in ("AOA-T-0016", "AOA-T-0015", "AOA-T-0017"):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)

            self.assertIn("techniques/proof/skill-support/", review)
            self.assertIn("Do not move `skill-support` from this review alone", review)
            self.assertIn("Do not add `tree_path`", review)
            self.assertIn("Run a direct-read migration review for `skill-support`", review)
            self.assertIn("landed-skill-discovery-pilot-review", reviews_index)
            self.assertIn("landed skill-discovery pilot review: landed", ingress)
            self.assertIn("skill-support` chosen", ingress)
            self.assertIn("Landed skill-discovery pilot review", landing_log)
            self.assertIn("fifth successful instruction trunk shelf", landing_log)
            self.assertIn(
                "skill-support` for the next direct-read",
                flat_distillation_roadmap,
            )
            self.assertIn(
                "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
                root_roadmap,
            )
            self.assertIn("Landed Skill-Discovery Pilot Review", tree_contract)
            self.assertIn("chooses `skill-support`", tree_contract)
            self.assertIn(
                "accepted the landed `skill-discovery` pilot review",
                changelog,
            )
            self.assertTrue(
                (
                    REPO_ROOT
                    / "techniques"
                    / "proof"
                    / "skill-support"
                    / "bounded-context-map"
                    / "TECHNIQUE.md"
                ).is_file()
            )
            self.assertTrue(
                (
                    REPO_ROOT
                    / "techniques"
                    / "proof"
                    / "skill-support"
                    / "contract-test-design"
                    / "TECHNIQUE.md"
                ).is_file()
            )
            self.assertTrue(
                (
                    REPO_ROOT
                    / "techniques"
                    / "proof"
                    / "skill-support"
                    / "property-invariants"
                    / "TECHNIQUE.md"
                ).is_file()
            )
            for old_parts in (
                ("docs", "bounded-context-map"),
                ("evaluation", "contract-test-design"),
                ("evaluation", "property-invariants"),
            ):
                with self.subTest(old_parts=old_parts):
                    self.assertFalse(
                        (REPO_ROOT / "techniques" / old_parts[0] / old_parts[1]).exists()
                    )

            self.assertTrue(
                (
                    REPO_ROOT
                    / "techniques"
                    / "proof"
                    / "skill-support"
                ).exists()
            )

    def test_skill_support_direct_read_migration_review_accepts_eleventh_pilot(
            self,
        ) -> None:
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
                / "skill-support-direct-read-migration-review.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Skill-Support Direct-Read Migration Review", review)
            self.assertIn("accepted-for-eleventh-migration-pilot", review)
            self.assertIn("not path migration", review)
            self.assertIn("not\n`tree_path` frontmatter", review)
            self.assertIn("Accept `skill-support` as the eleventh", review)
            self.assertIn("Direct Bundle Read", review)
            self.assertIn("Why The Shelf Holds", review)
            self.assertIn("Proof Trunk Fit", review)
            self.assertIn("Boundary Watch Accepted", review)
            for technique_id in ("AOA-T-0016", "AOA-T-0015", "AOA-T-0017"):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)

            self.assertIn("techniques/docs/bounded-context-map/", review)
            self.assertIn("techniques/evaluation/contract-test-design/", review)
            self.assertIn("techniques/evaluation/property-invariants/", review)
            self.assertIn("techniques/proof/skill-support/", review)
            self.assertIn("Move exactly these three bundles", review)
            self.assertIn("Do not move files from this review pack alone", review)
            self.assertIn("Do not add `tree_path`", review)
            self.assertIn("Do not treat `skill-support` as proof authority", review)
            self.assertIn("Run the eleventh pilot migration", review)

            self.assertIn("skill-support-direct-read-migration-review", reviews_index)
            self.assertIn("skill-support direct-read review: landed", ingress)
            self.assertIn("accepted-for-eleventh-migration-pilot", ingress)
            self.assertIn("Skill-support direct-read migration review", landing_log)
            self.assertIn("Skill-support tree pilot migration", landing_log)
            self.assertIn("proof-side support triangle", landing_log)
            self.assertIn("accepted-for-eleventh-migration-pilot", distillation_roadmap)
            self.assertIn(
                "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
                root_roadmap,
            )
            self.assertIn("Skill-Support Direct-Read Migration Review", tree_contract)
            self.assertIn("AOA-T-0016`, `AOA-T-0015`, and `AOA-T-0017", tree_contract)
            self.assertIn(
                "accepted the `skill-support` direct-read migration review",
                changelog,
            )
            self.assertTrue(
                (
                    REPO_ROOT
                    / "techniques"
                    / "proof"
                    / "skill-support"
                    / "bounded-context-map"
                    / "TECHNIQUE.md"
                ).is_file()
            )
            self.assertTrue(
                (
                    REPO_ROOT
                    / "techniques"
                    / "proof"
                    / "skill-support"
                    / "contract-test-design"
                    / "TECHNIQUE.md"
                ).is_file()
            )
            self.assertTrue(
                (
                    REPO_ROOT
                    / "techniques"
                    / "proof"
                    / "skill-support"
                    / "property-invariants"
                    / "TECHNIQUE.md"
                ).is_file()
            )
            self.assertTrue((REPO_ROOT / "techniques" / "proof" / "skill-support").exists())

    def test_skill_support_tree_pilot_migration_lands_eleventh_shelf(self) -> None:
            ingress = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "README.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
            receipt = (
                REPO_ROOT
                / "legacy"
                / "receipts"
                / "2026-05-05-skill-support-tree-pilot.md"
            ).read_text(encoding="utf-8")
            proof_route = (
                REPO_ROOT / "techniques" / "proof" / "AGENTS.md"
            ).read_text(encoding="utf-8")

            self.assertIn("skill-support migration: landed exactly", ingress)
            self.assertIn("Skill-Support Tree Pilot Receipt", ingress)
            self.assertIn("migration is now landed exactly", distillation_roadmap)
            self.assertIn("Skill-support tree pilot migration", landing_log)
            self.assertIn(
                "Review the landed `evaluation-chain` pilot",
                root_roadmap,
            )
            self.assertIn("eleventh pilot migration moves exactly", tree_contract)
            self.assertIn("2026-05-05-skill-support-tree-pilot.md", tree_contract)
            self.assertIn(
                "moved `AOA-T-0016`, `AOA-T-0015`, and `AOA-T-0017`",
                changelog,
            )
            self.assertIn("techniques/proof/skill-support/", receipt)
            self.assertIn("skill-support/", proof_route)
            self.assertIn("proof verdict authority", proof_route)

            for new_path in (
                "techniques/proof/skill-support/bounded-context-map/TECHNIQUE.md",
                "techniques/proof/skill-support/contract-test-design/TECHNIQUE.md",
                "techniques/proof/skill-support/property-invariants/TECHNIQUE.md",
            ):
                with self.subTest(new_path=new_path):
                    self.assertTrue((REPO_ROOT / new_path).is_file())

            for old_path in (
                "techniques/docs/bounded-context-map",
                "techniques/evaluation/contract-test-design",
                "techniques/evaluation/property-invariants",
            ):
                with self.subTest(old_path=old_path):
                    self.assertFalse((REPO_ROOT / old_path).exists())

    def test_landed_skill_support_pilot_review_selects_evaluation_chain(
            self,
        ) -> None:
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
                / "landed-skill-support-pilot-review.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            flat_distillation_roadmap = " ".join(distillation_roadmap.split())
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Landed Skill-Support Pilot Review", review)
            self.assertIn("pilot-validated", review)
            self.assertIn("first successful shelf under the `proof` trunk", review)
            self.assertIn("What The Eleventh Pilot Proved", review)
            self.assertIn("Remaining Weaknesses", review)
            self.assertIn("Twelfth Shelf Choice", review)
            self.assertIn("Choose `evaluation-chain`", review)
            for technique_id in (
                "AOA-T-0003",
                "AOA-T-0007",
                "AOA-T-0032",
                "AOA-T-0016",
                "AOA-T-0015",
                "AOA-T-0017",
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)

            self.assertIn("techniques/proof/evaluation-chain/", review)
            self.assertIn("Do not move `evaluation-chain` from this review alone", review)
            self.assertIn("Do not add `tree_path`", review)
            self.assertIn("Run a direct-read migration review for `evaluation-chain`", review)
            self.assertIn("landed-skill-support-pilot-review", reviews_index)
            self.assertIn("landed skill-support pilot review: landed", ingress)
            self.assertIn("evaluation-chain` chosen", ingress)
            self.assertIn("Landed skill-support pilot review", landing_log)
            self.assertIn("first successful proof trunk shelf", landing_log)
            self.assertIn("evaluation-chain` for the next direct-read", flat_distillation_roadmap)
            self.assertIn(
                "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
                root_roadmap,
            )
            self.assertIn("Landed Skill-Support Pilot Review", tree_contract)
            self.assertIn("chooses `evaluation-chain`", tree_contract)
            self.assertIn(
                "accepted the landed `skill-support` pilot review",
                changelog,
            )
            self.assertTrue(
                (
                    REPO_ROOT
                    / "techniques"
                    / "proof"
                    / "evaluation-chain"
                    / "contract-first-smoke-summary"
                    / "TECHNIQUE.md"
                ).is_file()
            )
            self.assertTrue(
                (
                    REPO_ROOT
                    / "techniques"
                    / "proof"
                    / "evaluation-chain"
                    / "signal-first-gate-promotion"
                    / "TECHNIQUE.md"
                ).is_file()
            )
            self.assertTrue(
                (
                    REPO_ROOT
                    / "techniques"
                    / "proof"
                    / "evaluation-chain"
                    / "context-report-for-ci"
                    / "TECHNIQUE.md"
                ).is_file()
            )
            for old_slug in (
                "contract-first-smoke-summary",
                "signal-first-gate-promotion",
                "context-report-for-ci",
            ):
                with self.subTest(old_slug=old_slug):
                    self.assertFalse(
                        (REPO_ROOT / "techniques" / "evaluation" / old_slug).exists()
                    )

    def test_evaluation_chain_direct_read_migration_review_accepts_twelfth_pilot(
            self,
        ) -> None:
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
                / "evaluation-chain-direct-read-migration-review.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Evaluation-Chain Direct-Read Migration Review", review)
            self.assertIn("accepted-for-twelfth-migration-pilot", review)
            self.assertIn("not path migration", review)
            self.assertIn("not\n`tree_path` frontmatter", review)
            self.assertIn("Accept `evaluation-chain` as the twelfth", review)
            self.assertIn("Direct Bundle Read", review)
            self.assertIn("Why The Shelf Holds", review)
            self.assertIn("Proof Trunk Fit", review)
            self.assertIn("Boundary Watch Accepted", review)
            for technique_id in ("AOA-T-0003", "AOA-T-0007", "AOA-T-0032"):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)

            self.assertIn("techniques/evaluation/contract-first-smoke-summary/", review)
            self.assertIn("techniques/evaluation/signal-first-gate-promotion/", review)
            self.assertIn("techniques/evaluation/context-report-for-ci/", review)
            self.assertIn("techniques/proof/evaluation-chain/", review)
            self.assertIn("Move exactly these three bundles", review)
            self.assertIn("Do not move files from this review pack alone", review)
            self.assertIn("Do not add `tree_path`", review)
            self.assertIn("Do not treat `evaluation-chain` as CI ownership", review)
            self.assertIn("Do not promote `AOA-T-0032`", review)
            self.assertIn("Run the twelfth pilot migration", review)

            self.assertIn("evaluation-chain-direct-read-migration-review", reviews_index)
            self.assertIn("evaluation-chain direct-read review: landed", ingress)
            self.assertIn("accepted-for-twelfth-migration-pilot", ingress)
            self.assertIn("Evaluation-chain direct-read migration review", landing_log)
            self.assertIn("proof-facing chain", landing_log)
            self.assertIn("accepted-for-twelfth-migration-pilot", distillation_roadmap)
            self.assertIn(
                "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
                root_roadmap,
            )
            self.assertIn("Evaluation-Chain Direct-Read Migration Review", tree_contract)
            self.assertIn("AOA-T-0003`, `AOA-T-0007`, and `AOA-T-0032", tree_contract)
            self.assertIn(
                "accepted the `evaluation-chain` direct-read migration review",
                changelog,
            )
            self.assertTrue(
                (
                    REPO_ROOT
                    / "techniques"
                    / "proof"
                    / "evaluation-chain"
                    / "contract-first-smoke-summary"
                    / "TECHNIQUE.md"
                ).is_file()
            )
            self.assertTrue(
                (
                    REPO_ROOT
                    / "techniques"
                    / "proof"
                    / "evaluation-chain"
                    / "signal-first-gate-promotion"
                    / "TECHNIQUE.md"
                ).is_file()
            )
            self.assertTrue(
                (
                    REPO_ROOT
                    / "techniques"
                    / "proof"
                    / "evaluation-chain"
                    / "context-report-for-ci"
                    / "TECHNIQUE.md"
                ).is_file()
            )
            for old_slug in (
                "contract-first-smoke-summary",
                "signal-first-gate-promotion",
                "context-report-for-ci",
            ):
                with self.subTest(old_slug=old_slug):
                    self.assertFalse(
                        (REPO_ROOT / "techniques" / "evaluation" / old_slug).exists()
                    )

    def test_evaluation_chain_tree_pilot_migration_lands_twelfth_shelf(
            self,
        ) -> None:
            ingress = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "README.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
            receipt = (
                REPO_ROOT
                / "legacy"
                / "receipts"
                / "2026-05-05-evaluation-chain-tree-pilot.md"
            ).read_text(encoding="utf-8")
            proof_route = (
                REPO_ROOT / "techniques" / "proof" / "AGENTS.md"
            ).read_text(encoding="utf-8")

            self.assertIn("evaluation-chain migration: landed exactly", ingress)
            self.assertIn("Evaluation-Chain Tree Pilot Receipt", ingress)
            self.assertIn("twelfth pilot migration is now landed exactly", distillation_roadmap)
            self.assertIn("Evaluation-chain tree pilot migration", landing_log)
            self.assertIn("twelfth landed pilot moved `AOA-T-0003`", root_roadmap)
            self.assertIn("Review the landed `evaluation-chain` pilot", root_roadmap)
            self.assertIn("twelfth pilot migration moves exactly", tree_contract)
            self.assertIn("2026-05-05-evaluation-chain-tree-pilot.md", tree_contract)
            self.assertIn(
                "moved `AOA-T-0003`, `AOA-T-0007`, and `AOA-T-0032`",
                changelog,
            )
            self.assertIn("techniques/proof/evaluation-chain/", receipt)
            self.assertIn("evaluation-chain/", proof_route)
            self.assertIn("CI ownership", proof_route)

            for new_path in (
                "techniques/proof/evaluation-chain/contract-first-smoke-summary/TECHNIQUE.md",
                "techniques/proof/evaluation-chain/signal-first-gate-promotion/TECHNIQUE.md",
                "techniques/proof/evaluation-chain/context-report-for-ci/TECHNIQUE.md",
            ):
                with self.subTest(new_path=new_path):
                    self.assertTrue((REPO_ROOT / new_path).is_file())

            for old_path in (
                "techniques/evaluation/contract-first-smoke-summary",
                "techniques/evaluation/signal-first-gate-promotion",
                "techniques/evaluation/context-report-for-ci",
            ):
                with self.subTest(old_path=old_path):
                    self.assertFalse((REPO_ROOT / old_path).exists())

    def test_landed_evaluation_chain_pilot_review_selects_published_summary(
            self,
        ) -> None:
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
                / "landed-evaluation-chain-pilot-review.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Landed Evaluation-Chain Pilot Review", review)
            self.assertIn("pilot-validated", review)
            self.assertIn("second successful shelf under the `proof` trunk", review)
            self.assertIn("What The Twelfth Pilot Proved", review)
            self.assertIn("Remaining Weaknesses", review)
            self.assertIn("Thirteenth Shelf Choice", review)
            self.assertIn("Choose `published-summary`", review)
            for technique_id in (
                "AOA-T-0003",
                "AOA-T-0007",
                "AOA-T-0032",
                "AOA-T-0006",
                "AOA-T-0008",
                "AOA-T-0010",
                "AOA-T-0011",
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)

            self.assertIn("techniques/proof/published-summary/", review)
            self.assertIn("Do not move `published-summary` from this review alone", review)
            self.assertIn("Do not add `tree_path`", review)
            self.assertIn("Do not treat `published-summary` as proof authority", review)
            self.assertIn("Run a direct-read migration review for `published-summary`", review)
            self.assertIn("landed-evaluation-chain-pilot-review", reviews_index)
            self.assertIn("landed evaluation-chain pilot review: landed", ingress)
            self.assertIn("published-summary` chosen", ingress)
            self.assertIn("Landed evaluation-chain pilot review", landing_log)
            self.assertIn("second successful proof trunk shelf", landing_log)
            self.assertIn("published-summary` direct-read review", distillation_roadmap)
            self.assertIn("published-summary` pilot before choosing", root_roadmap)
            self.assertIn("Landed Evaluation-Chain Pilot Review", tree_contract)
            self.assertIn("chooses `published-summary`", tree_contract)
            self.assertIn(
                "accepted the landed `evaluation-chain` pilot review",
                changelog,
            )

            for old_path, current_path in (
                (
                    "techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md",
                    "techniques/proof/published-summary/latest-alias-plus-history-copy/TECHNIQUE.md",
                ),
                (
                    "techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md",
                    "techniques/proof/published-summary/published-summary-remediation-snapshot/TECHNIQUE.md",
                ),
                (
                    "techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md",
                    "techniques/proof/published-summary/telemetry-integrity-snapshot/TECHNIQUE.md",
                ),
                (
                    "techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md",
                    "techniques/proof/published-summary/required-vs-optional-source-rendering/TECHNIQUE.md",
                ),
            ):
                with self.subTest(old_path=old_path):
                    self.assertFalse((REPO_ROOT / old_path).exists())
                    self.assertTrue((REPO_ROOT / current_path).is_file())

            self.assertTrue((REPO_ROOT / "techniques" / "proof" / "published-summary").is_dir())


if __name__ == "__main__":
    unittest.main()
