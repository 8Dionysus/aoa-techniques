from __future__ import annotations

import sys
import unittest
from pathlib import Path


SUPPORT_DIR = Path(__file__).resolve().parent / "support"
if str(SUPPORT_DIR) not in sys.path:
    sys.path.insert(0, str(SUPPORT_DIR))

from distillation_topology_fixtures import *  # noqa: F403


class DistillationTreePilotAutomationCloseoutTests(unittest.TestCase):
    def test_automation_governance_direct_read_split_review_rejects_bulk_shelf(
            self,
        ) -> None:
            review = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "automation-governance-direct-read-split-review.md"
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
            ingress = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "README.md"
            ).read_text(encoding="utf-8")
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Automation-Governance Direct-Read Split Review", review)
            self.assertIn("split-required-before-migration", review)
            self.assertIn(
                "Reject `governance/automation-governance` as one bulk migration shelf",
                review,
            )
            self.assertIn("governance/automation-readiness", review)
            self.assertIn("governance/promotion-boundary", review)
            self.assertIn("governance/practice-adoption-lifecycle", review)
            self.assertIn("Do not move any `automation-governance` bundle", review)
            self.assertIn("Run a split-expansion closeout", review)
            self.assertIn(
                "automation-governance-direct-read-split-review",
                reviews_index,
            )
            self.assertIn(
                "automation-governance direct-read split review: landed",
                ingress,
            )
            self.assertIn("split-required-before-migration", ingress)
            self.assertIn(
                "Automation-governance direct-read split review",
                landing_log,
            )
            self.assertIn(
                "automation-governance\n   direct-read split review is now landed",
                distillation_roadmap,
            )
            self.assertIn(
                "Run the automation-governance split-expansion closeout",
                root_roadmap,
            )
            self.assertIn(
                "Automation-Governance Direct-Read Split Review",
                tree_contract,
            )
            self.assertIn(
                "rejected one bulk `governance/automation-governance` shelf",
                changelog,
            )

            for technique_id, current_path, future_path, current_exists, future_exists in (
                (
                    "AOA-T-0086",
                    "techniques/agent-workflows/automation-fit-matrix/TECHNIQUE.md",
                    "techniques/governance/automation-readiness/automation-fit-matrix/TECHNIQUE.md",
                    False,
                    True,
                ),
                (
                    "AOA-T-0087",
                    "techniques/agent-workflows/human-loop-to-first-landing/TECHNIQUE.md",
                    "techniques/governance/automation-readiness/human-loop-to-first-landing/TECHNIQUE.md",
                    False,
                    True,
                ),
                (
                    "AOA-T-0088",
                    "techniques/agent-workflows/approval-sensitivity-check/TECHNIQUE.md",
                    "techniques/governance/automation-readiness/approval-sensitivity-check/TECHNIQUE.md",
                    False,
                    True,
                ),
                (
                    "AOA-T-0089",
                    "techniques/agent-workflows/quest-unit-promotion-review/TECHNIQUE.md",
                    "techniques/governance/promotion-boundary/quest-unit-promotion-review/TECHNIQUE.md",
                    False,
                    True,
                ),
                (
                    "AOA-T-0090",
                    "techniques/agent-workflows/nearest-wrong-target-rejection/TECHNIQUE.md",
                    "techniques/governance/promotion-boundary/nearest-wrong-target-rejection/TECHNIQUE.md",
                    False,
                    True,
                ),
                (
                    "AOA-T-0102",
                    "techniques/agent-workflows/skill-proposal-handoff-packet/TECHNIQUE.md",
                    "techniques/governance/promotion-boundary/skill-proposal-handoff-packet/TECHNIQUE.md",
                    False,
                    True,
                ),
                (
                    "AOA-T-0101",
                    "techniques/agent-workflows/local-pattern-adoption-gate/TECHNIQUE.md",
                    "techniques/governance/practice-adoption-lifecycle/local-pattern-adoption-gate/TECHNIQUE.md",
                    False,
                    True,
                ),
                (
                    "AOA-T-0103",
                    "techniques/agent-workflows/adopted-practice-retention-review/TECHNIQUE.md",
                    "techniques/governance/practice-adoption-lifecycle/adopted-practice-retention-review/TECHNIQUE.md",
                    False,
                    True,
                ),
                (
                    "AOA-T-0104",
                    "techniques/agent-workflows/superseded-practice-obsolescence-route/TECHNIQUE.md",
                    "techniques/governance/practice-adoption-lifecycle/superseded-practice-obsolescence-route/TECHNIQUE.md",
                    False,
                    True,
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)
                    self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                    self.assertIn(future_path.rsplit("/", 1)[0] + "/", review)
                    self.assertEqual(current_exists, (REPO_ROOT / current_path).is_file())
                    self.assertEqual(future_exists, (REPO_ROOT / future_path).is_file())

    def test_automation_governance_split_expansion_closeout_activates_candidate_a(
            self,
        ) -> None:
            closeout = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "automation-governance-split-expansion-closeout.md"
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
            ingress = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "README.md"
            ).read_text(encoding="utf-8")
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Automation-Governance Split Expansion Closeout", closeout)
            self.assertIn("split-expanded", closeout)
            self.assertIn("no path migration", closeout)
            self.assertIn("Candidate A", closeout)
            self.assertIn("governance/automation-readiness", closeout)
            self.assertIn("governance/promotion-boundary", closeout)
            self.assertIn("governance/practice-adoption-lifecycle", closeout)
            self.assertIn("Do not move files from this closeout", closeout)
            self.assertIn(
                "Run a direct-read review for Candidate A",
                closeout,
            )
            self.assertIn(
                "automation-governance-split-expansion-closeout",
                reviews_index,
            )
            self.assertIn(
                "automation-governance split expansion closeout: landed",
                ingress,
            )
            self.assertIn("split-expanded", ingress)
            self.assertIn(
                "Automation-governance split expansion closeout",
                landing_log,
            )
            self.assertIn(
                "automation-governance split\n   expansion closeout is now landed",
                distillation_roadmap,
            )
            self.assertIn(
                "Run the `governance/automation-readiness` direct-read review",
                root_roadmap,
            )
            self.assertIn(
                "Automation-Governance Split Expansion Closeout",
                tree_contract,
            )
            self.assertIn(
                "landed the automation-governance split expansion closeout",
                changelog,
            )

            for current_path, future_path in (
                (
                    "techniques/agent-workflows/automation-fit-matrix/TECHNIQUE.md",
                    "techniques/governance/automation-readiness/automation-fit-matrix/TECHNIQUE.md",
                ),
                (
                    "techniques/agent-workflows/human-loop-to-first-landing/TECHNIQUE.md",
                    "techniques/governance/automation-readiness/human-loop-to-first-landing/TECHNIQUE.md",
                ),
                (
                    "techniques/agent-workflows/approval-sensitivity-check/TECHNIQUE.md",
                    "techniques/governance/automation-readiness/approval-sensitivity-check/TECHNIQUE.md",
                ),
            ):
                with self.subTest(current_path=current_path):
                    self.assertFalse((REPO_ROOT / current_path).exists())
                    self.assertTrue((REPO_ROOT / future_path).is_file())

    def test_automation_readiness_direct_read_review_accepts_twenty_fifth_pilot(
            self,
        ) -> None:
            review = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "automation-readiness-direct-read-migration-review.md"
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
            ingress = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "README.md"
            ).read_text(encoding="utf-8")
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Automation-Readiness Direct-Read Migration Review", review)
            self.assertIn("accepted-for-twenty-fifth-migration-pilot", review)
            self.assertIn("Accept `governance/automation-readiness`", review)
            self.assertIn("Candidate B and Candidate C stay out", review)
            self.assertIn("Run the twenty-fifth migration pilot", review)
            self.assertIn(
                "automation-readiness-direct-read-migration-review",
                reviews_index,
            )
            self.assertIn(
                "automation-readiness direct-read review: landed",
                ingress,
            )
            self.assertIn(
                "accepted-for-twenty-fifth-migration-pilot",
                ingress,
            )
            self.assertIn(
                "Automation-readiness direct-read migration review",
                landing_log,
            )
            self.assertIn(
                "automation-readiness direct-read review is now landed",
                distillation_roadmap,
            )
            self.assertIn(
                "Migrate exactly `AOA-T-0086`, `AOA-T-0087`, and `AOA-T-0088`",
                root_roadmap,
            )
            self.assertIn(
                "automation-readiness` direct-read\nreview accepts",
                root_roadmap,
            )
            self.assertIn(
                "Automation-Readiness Direct-Read Migration Review",
                tree_contract,
            )
            self.assertIn(
                "migration should move exactly those three bundles",
                tree_contract,
            )
            self.assertIn(
                "accepted the `automation-readiness` direct-read migration review",
                changelog,
            )

            for technique_id, current_path, future_path in (
                (
                    "AOA-T-0086",
                    "techniques/agent-workflows/automation-fit-matrix/TECHNIQUE.md",
                    "techniques/governance/automation-readiness/automation-fit-matrix/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0087",
                    "techniques/agent-workflows/human-loop-to-first-landing/TECHNIQUE.md",
                    "techniques/governance/automation-readiness/human-loop-to-first-landing/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0088",
                    "techniques/agent-workflows/approval-sensitivity-check/TECHNIQUE.md",
                    "techniques/governance/automation-readiness/approval-sensitivity-check/TECHNIQUE.md",
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)
                    self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                    self.assertIn(future_path.rsplit("/", 1)[0] + "/", review)
                    self.assertFalse((REPO_ROOT / current_path).exists())
                    self.assertTrue((REPO_ROOT / future_path).is_file())

    def test_automation_readiness_tree_pilot_migration_landed(self) -> None:
            receipt = (
                REPO_ROOT
                / "legacy"
                / "receipts"
                / "2026-05-05-automation-readiness-tree-pilot.md"
            ).read_text(encoding="utf-8")
            governance_agents = (
                REPO_ROOT / "techniques" / "governance" / "AGENTS.md"
            ).read_text(encoding="utf-8")
            agent_workflows_agents = (
                REPO_ROOT / "techniques" / "agent-workflows" / "AGENTS.md"
            ).read_text(encoding="utf-8")
            ingress = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "README.md"
            ).read_text(encoding="utf-8")
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            legacy_index = (REPO_ROOT / "legacy" / "INDEX.md").read_text(
                encoding="utf-8"
            )
            receipts_index = (
                REPO_ROOT / "legacy" / "receipts" / "README.md"
            ).read_text(encoding="utf-8")
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Automation-Readiness Tree Pilot Receipt", receipt)
            self.assertIn("Twenty-fifth authored path migration", receipt)
            self.assertIn("`domain` stayed unchanged as `agent-workflows`", receipt)
            self.assertIn("`kind` stayed unchanged as `assessment`", receipt)
            self.assertIn("automation-readiness/", governance_agents)
            self.assertIn("automation-fit", governance_agents)
            self.assertNotIn("automation-fit-matrix", agent_workflows_agents)
            self.assertIn("automation-readiness migration: landed", ingress)
            self.assertIn("Automation-readiness tree pilot migration", landing_log)
            self.assertIn(
                "2026-05-05-automation-readiness-tree-pilot",
                landing_log,
            )
            self.assertIn(
                "twenty-fifth pilot\n   migration is now landed",
                distillation_roadmap,
            )
            self.assertIn(
                "Review the landed `governance/automation-readiness` pilot",
                root_roadmap,
            )
            self.assertIn(
                "2026-05-05-automation-readiness-tree-pilot",
                tree_contract,
            )
            self.assertIn("twenty-eight receipts", legacy_index)
            self.assertIn(
                "2026-05-05-automation-readiness-tree-pilot.md",
                legacy_index,
            )
            self.assertIn("twenty-eight technique tree pilot receipts", receipts_index)
            self.assertIn("moved `AOA-T-0086`", changelog)

            for technique_id, old_path, new_path in (
                (
                    "AOA-T-0086",
                    "techniques/agent-workflows/automation-fit-matrix/",
                    "techniques/governance/automation-readiness/automation-fit-matrix/",
                ),
                (
                    "AOA-T-0087",
                    "techniques/agent-workflows/human-loop-to-seed-lift/",
                    "techniques/governance/automation-readiness/human-loop-to-first-landing/",
                ),
                (
                    "AOA-T-0088",
                    "techniques/agent-workflows/approval-sensitivity-check/",
                    "techniques/governance/automation-readiness/approval-sensitivity-check/",
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, receipt)
                    self.assertIn(old_path, receipt)
                    self.assertIn(new_path, receipt)
                    self.assertFalse((REPO_ROOT / old_path).exists())
                    self.assertTrue((REPO_ROOT / new_path / "TECHNIQUE.md").is_file())

    def test_landed_automation_readiness_pilot_review_routes_candidate_b(
            self,
        ) -> None:
            review = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "landed-automation-readiness-pilot-review.md"
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
            ingress = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "README.md"
            ).read_text(encoding="utf-8")
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Landed Automation-Readiness Pilot Review", review)
            self.assertIn("pilot-validated", review)
            self.assertIn(
                "The landed `governance/automation-readiness` shelf holds.",
                review,
            )
            self.assertIn("generated tree projection keeps", review)
            self.assertIn("Run a direct-read review for Candidate B", review)
            self.assertIn("governance/promotion-boundary", review)
            self.assertIn(
                "landed-automation-readiness-pilot-review",
                reviews_index,
            )
            self.assertIn(
                "landed automation-readiness pilot review: landed",
                ingress,
            )
            self.assertIn("Landed automation-readiness pilot review", landing_log)
            self.assertIn(
                "automation-readiness` pilot review is now complete",
                distillation_roadmap,
            )
            self.assertIn(
                "Run the `governance/promotion-boundary` direct-read review",
                root_roadmap,
            )
            self.assertIn("Landed Automation-Readiness Pilot Review", tree_contract)
            self.assertIn(
                "accepted the landed `automation-readiness` pilot review",
                changelog,
            )

            for old_path, new_path in (
                (
                    "techniques/agent-workflows/automation-fit-matrix/TECHNIQUE.md",
                    "techniques/governance/automation-readiness/automation-fit-matrix/TECHNIQUE.md",
                ),
                (
                    "techniques/agent-workflows/human-loop-to-first-landing/TECHNIQUE.md",
                    "techniques/governance/automation-readiness/human-loop-to-first-landing/TECHNIQUE.md",
                ),
                (
                    "techniques/agent-workflows/approval-sensitivity-check/TECHNIQUE.md",
                    "techniques/governance/automation-readiness/approval-sensitivity-check/TECHNIQUE.md",
                ),
            ):
                with self.subTest(new_path=new_path):
                    self.assertFalse((REPO_ROOT / old_path).exists())
                    self.assertTrue((REPO_ROOT / new_path).is_file())

            for current_path, future_path in (
                (
                    "techniques/agent-workflows/quest-unit-promotion-review/TECHNIQUE.md",
                    "techniques/governance/promotion-boundary/quest-unit-promotion-review/TECHNIQUE.md",
                ),
                (
                    "techniques/agent-workflows/nearest-wrong-target-rejection/TECHNIQUE.md",
                    "techniques/governance/promotion-boundary/nearest-wrong-target-rejection/TECHNIQUE.md",
                ),
                (
                    "techniques/agent-workflows/skill-proposal-handoff-packet/TECHNIQUE.md",
                    "techniques/governance/promotion-boundary/skill-proposal-handoff-packet/TECHNIQUE.md",
                ),
            ):
                with self.subTest(current_path=current_path):
                    self.assertFalse((REPO_ROOT / current_path).exists())
                    self.assertTrue((REPO_ROOT / future_path).is_file())

    def test_promotion_boundary_direct_read_review_accepts_twenty_sixth_pilot(
            self,
        ) -> None:
            review = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "promotion-boundary-direct-read-migration-review.md"
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
            ingress = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "README.md"
            ).read_text(encoding="utf-8")
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Promotion-Boundary Direct-Read Migration Review", review)
            self.assertIn("accepted-for-twenty-sixth-migration-pilot", review)
            self.assertIn("Accept `governance/promotion-boundary`", review)
            self.assertIn("Candidate C remains queued", review)
            self.assertIn("Run the twenty-sixth migration pilot", review)
            self.assertIn(
                "promotion-boundary-direct-read-migration-review",
                reviews_index,
            )
            self.assertIn(
                "promotion-boundary direct-read review: landed",
                ingress,
            )
            self.assertIn(
                "accepted-for-twenty-sixth-migration-pilot",
                ingress,
            )
            self.assertIn(
                "Promotion-boundary direct-read migration review",
                landing_log,
            )
            self.assertIn(
                "promotion-boundary direct-read review is now\n   landed",
                distillation_roadmap,
            )
            self.assertIn(
                "Previous Candidate B migration breadcrumb preserved",
                root_roadmap,
            )
            self.assertIn(
                "Promotion-Boundary Direct-Read Migration Review",
                tree_contract,
            )
            self.assertIn(
                "migration should move exactly those\nthree bundles",
                tree_contract,
            )
            self.assertIn(
                "accepted the `promotion-boundary` direct-read migration review",
                changelog,
            )

            for technique_id, current_path, future_path in (
                (
                    "AOA-T-0089",
                    "techniques/agent-workflows/quest-unit-promotion-review/TECHNIQUE.md",
                    "techniques/governance/promotion-boundary/quest-unit-promotion-review/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0090",
                    "techniques/agent-workflows/nearest-wrong-target-rejection/TECHNIQUE.md",
                    "techniques/governance/promotion-boundary/nearest-wrong-target-rejection/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0102",
                    "techniques/agent-workflows/skill-proposal-handoff-packet/TECHNIQUE.md",
                    "techniques/governance/promotion-boundary/skill-proposal-handoff-packet/TECHNIQUE.md",
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)
                    self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                    self.assertIn(future_path.rsplit("/", 1)[0] + "/", review)
                    self.assertFalse((REPO_ROOT / current_path).exists())
                    self.assertTrue((REPO_ROOT / future_path).is_file())

            for current_path, future_path in (
                (
                    "techniques/agent-workflows/local-pattern-adoption-gate/TECHNIQUE.md",
                    "techniques/governance/practice-adoption-lifecycle/local-pattern-adoption-gate/TECHNIQUE.md",
                ),
                (
                    "techniques/agent-workflows/adopted-practice-retention-review/TECHNIQUE.md",
                    "techniques/governance/practice-adoption-lifecycle/adopted-practice-retention-review/TECHNIQUE.md",
                ),
                (
                    "techniques/agent-workflows/superseded-practice-obsolescence-route/TECHNIQUE.md",
                    "techniques/governance/practice-adoption-lifecycle/superseded-practice-obsolescence-route/TECHNIQUE.md",
                ),
            ):
                with self.subTest(current_path=current_path):
                    self.assertFalse((REPO_ROOT / current_path).exists())
                    self.assertTrue((REPO_ROOT / future_path).is_file())

    def test_promotion_boundary_tree_pilot_migration_landed(self) -> None:
            receipt = (
                REPO_ROOT
                / "legacy"
                / "receipts"
                / "2026-05-05-promotion-boundary-tree-pilot.md"
            ).read_text(encoding="utf-8")
            governance_agents = (
                REPO_ROOT / "techniques" / "governance" / "AGENTS.md"
            ).read_text(encoding="utf-8")
            agent_workflows_agents = (
                REPO_ROOT / "techniques" / "agent-workflows" / "AGENTS.md"
            ).read_text(encoding="utf-8")
            ingress = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "README.md"
            ).read_text(encoding="utf-8")
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            legacy_index = (REPO_ROOT / "legacy" / "INDEX.md").read_text(
                encoding="utf-8"
            )
            receipts_index = (
                REPO_ROOT / "legacy" / "receipts" / "README.md"
            ).read_text(encoding="utf-8")
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Promotion-Boundary Tree Pilot Receipt", receipt)
            self.assertIn("Twenty-sixth authored path migration", receipt)
            self.assertIn("`domain` stayed unchanged as `agent-workflows`", receipt)
            self.assertIn("`kind` stayed unchanged as `assessment`", receipt)
            self.assertIn("`kind: guardrail`", landing_log)
            self.assertIn("`kind: handoff`", landing_log)
            self.assertIn("promotion-boundary/", governance_agents)
            self.assertIn("nearest-wrong-target", governance_agents)
            self.assertNotIn("quest-unit-promotion-review", agent_workflows_agents)
            self.assertIn("promotion-boundary migration: landed", ingress)
            self.assertIn("Promotion-boundary tree pilot migration", landing_log)
            self.assertIn(
                "2026-05-05-promotion-boundary-tree-pilot",
                landing_log,
            )
            self.assertIn(
                "twenty-sixth pilot\n   migration is now landed",
                distillation_roadmap,
            )
            self.assertIn(
                "Review the landed `governance/promotion-boundary` pilot",
                root_roadmap,
            )
            self.assertIn(
                "2026-05-05-promotion-boundary-tree-pilot",
                tree_contract,
            )
            self.assertIn("twenty-eight receipts", legacy_index)
            self.assertIn(
                "2026-05-05-promotion-boundary-tree-pilot.md",
                legacy_index,
            )
            self.assertIn("twenty-eight technique tree pilot receipts", receipts_index)
            self.assertIn("moved `AOA-T-0089`", changelog)

            for technique_id, old_path, new_path in (
                (
                    "AOA-T-0089",
                    "techniques/agent-workflows/quest-unit-promotion-review/",
                    "techniques/governance/promotion-boundary/quest-unit-promotion-review/",
                ),
                (
                    "AOA-T-0090",
                    "techniques/agent-workflows/nearest-wrong-target-rejection/",
                    "techniques/governance/promotion-boundary/nearest-wrong-target-rejection/",
                ),
                (
                    "AOA-T-0102",
                    "techniques/agent-workflows/skill-proposal-handoff-packet/",
                    "techniques/governance/promotion-boundary/skill-proposal-handoff-packet/",
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, receipt)
                    self.assertIn(old_path, receipt)
                    self.assertIn(new_path, receipt)
                    self.assertFalse((REPO_ROOT / old_path).exists())
                    self.assertTrue((REPO_ROOT / new_path / "TECHNIQUE.md").is_file())

    def test_landed_promotion_boundary_pilot_review_routes_candidate_c(
            self,
        ) -> None:
            review = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "landed-promotion-boundary-pilot-review.md"
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
            ingress = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "README.md"
            ).read_text(encoding="utf-8")
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Landed Promotion-Boundary Pilot Review", review)
            self.assertIn("pilot-validated", review)
            self.assertIn(
                "The landed `governance/promotion-boundary` shelf holds.",
                review,
            )
            self.assertIn("generated tree projection keeps", review)
            self.assertIn("three unmoved automation-governance leaves", review)
            self.assertIn("Run a direct-read review for Candidate C", review)
            self.assertIn("governance/practice-adoption-lifecycle", review)
            self.assertIn(
                "landed-promotion-boundary-pilot-review",
                reviews_index,
            )
            self.assertIn(
                "landed promotion-boundary pilot review: landed",
                ingress,
            )
            self.assertIn(
                "Landed promotion-boundary pilot review",
                landing_log,
            )
            self.assertIn(
                "promotion-boundary` pilot review is now complete",
                distillation_roadmap,
            )
            self.assertIn(
                "Run the `governance/practice-adoption-lifecycle` direct-read review",
                root_roadmap,
            )
            self.assertIn(
                "Landed Promotion-Boundary Pilot Review",
                tree_contract,
            )
            self.assertIn(
                "accepted the landed `promotion-boundary` pilot review",
                changelog,
            )

            for old_path, new_path in (
                (
                    "techniques/agent-workflows/quest-unit-promotion-review/TECHNIQUE.md",
                    "techniques/governance/promotion-boundary/quest-unit-promotion-review/TECHNIQUE.md",
                ),
                (
                    "techniques/agent-workflows/nearest-wrong-target-rejection/TECHNIQUE.md",
                    "techniques/governance/promotion-boundary/nearest-wrong-target-rejection/TECHNIQUE.md",
                ),
                (
                    "techniques/agent-workflows/skill-proposal-handoff-packet/TECHNIQUE.md",
                    "techniques/governance/promotion-boundary/skill-proposal-handoff-packet/TECHNIQUE.md",
                ),
            ):
                with self.subTest(new_path=new_path):
                    self.assertFalse((REPO_ROOT / old_path).exists())
                    self.assertTrue((REPO_ROOT / new_path).is_file())

            for current_path, future_path in (
                (
                    "techniques/agent-workflows/local-pattern-adoption-gate/TECHNIQUE.md",
                    "techniques/governance/practice-adoption-lifecycle/local-pattern-adoption-gate/TECHNIQUE.md",
                ),
                (
                    "techniques/agent-workflows/adopted-practice-retention-review/TECHNIQUE.md",
                    "techniques/governance/practice-adoption-lifecycle/adopted-practice-retention-review/TECHNIQUE.md",
                ),
                (
                    "techniques/agent-workflows/superseded-practice-obsolescence-route/TECHNIQUE.md",
                    "techniques/governance/practice-adoption-lifecycle/superseded-practice-obsolescence-route/TECHNIQUE.md",
                ),
            ):
                with self.subTest(current_path=current_path):
                    self.assertFalse((REPO_ROOT / current_path).exists())
                    self.assertTrue((REPO_ROOT / future_path).is_file())

    def test_practice_adoption_lifecycle_direct_read_review_accepts_twenty_seventh_pilot(
            self,
        ) -> None:
            review = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "practice-adoption-lifecycle-direct-read-migration-review.md"
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
            ingress = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "README.md"
            ).read_text(encoding="utf-8")
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn(
                "Practice-Adoption-Lifecycle Direct-Read Migration Review",
                review,
            )
            self.assertIn("accepted-for-twenty-seventh-migration-pilot", review)
            self.assertIn(
                "Accept `governance/practice-adoption-lifecycle`",
                review,
            )
            self.assertIn("Run the twenty-seventh migration pilot", review)
            self.assertIn("Do not move `tool-use/tool-gateway`", review)
            self.assertIn(
                "practice-adoption-lifecycle-direct-read-migration-review",
                reviews_index,
            )
            self.assertIn(
                "practice-adoption-lifecycle direct-read review: landed",
                ingress,
            )
            self.assertIn(
                "accepted-for-twenty-seventh-migration-pilot",
                ingress,
            )
            self.assertIn(
                "Practice-adoption-lifecycle direct-read migration review",
                landing_log,
            )
            self.assertIn(
                "practice-adoption-lifecycle direct-read review\n   is now landed",
                distillation_roadmap,
            )
            self.assertIn(
                "Migrate exactly `AOA-T-0101`, `AOA-T-0103`, and `AOA-T-0104`",
                root_roadmap,
            )
            self.assertIn(
                "Practice-Adoption-Lifecycle Direct-Read Migration Review",
                tree_contract,
            )
            self.assertIn(
                "migration should\nmove exactly those three bundles",
                tree_contract,
            )
            self.assertIn(
                "accepted the `practice-adoption-lifecycle` direct-read migration review",
                changelog,
            )

            for technique_id, current_path, future_path in (
                (
                    "AOA-T-0101",
                    "techniques/agent-workflows/local-pattern-adoption-gate/TECHNIQUE.md",
                    "techniques/governance/practice-adoption-lifecycle/local-pattern-adoption-gate/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0103",
                    "techniques/agent-workflows/adopted-practice-retention-review/TECHNIQUE.md",
                    "techniques/governance/practice-adoption-lifecycle/adopted-practice-retention-review/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0104",
                    "techniques/agent-workflows/superseded-practice-obsolescence-route/TECHNIQUE.md",
                    "techniques/governance/practice-adoption-lifecycle/superseded-practice-obsolescence-route/TECHNIQUE.md",
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)
                    self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                    self.assertIn(future_path.rsplit("/", 1)[0] + "/", review)
                    self.assertFalse((REPO_ROOT / current_path).exists())
                    self.assertTrue((REPO_ROOT / future_path).is_file())

    def test_practice_adoption_lifecycle_tree_pilot_migration_landed(self) -> None:
            receipt = (
                REPO_ROOT
                / "legacy"
                / "receipts"
                / "2026-05-05-practice-adoption-lifecycle-tree-pilot.md"
            ).read_text(encoding="utf-8")
            governance_agents = (
                REPO_ROOT / "techniques" / "governance" / "AGENTS.md"
            ).read_text(encoding="utf-8")
            agent_workflows_agents = (
                REPO_ROOT / "techniques" / "agent-workflows" / "AGENTS.md"
            ).read_text(encoding="utf-8")
            ingress = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "README.md"
            ).read_text(encoding="utf-8")
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            legacy_index = (REPO_ROOT / "legacy" / "INDEX.md").read_text(
                encoding="utf-8"
            )
            receipts_index = (
                REPO_ROOT / "legacy" / "receipts" / "README.md"
            ).read_text(encoding="utf-8")
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Practice-Adoption-Lifecycle Tree Pilot Receipt", receipt)
            self.assertIn("Twenty-seventh authored path migration", receipt)
            self.assertIn("`domain` stayed unchanged as `agent-workflows`", receipt)
            self.assertIn("`kind` stayed unchanged as `guardrail`", receipt)
            self.assertIn("`kind: assessment`", landing_log)
            self.assertIn("`kind: handoff`", landing_log)
            self.assertIn("practice-adoption-lifecycle/", governance_agents)
            self.assertIn("local adoption", governance_agents)
            self.assertNotIn("local-pattern-adoption-gate", agent_workflows_agents)
            self.assertIn("practice-adoption-lifecycle migration: landed", ingress)
            self.assertIn(
                "Practice-adoption-lifecycle tree pilot migration",
                landing_log,
            )
            self.assertIn(
                "2026-05-05-practice-adoption-lifecycle-tree-pilot",
                landing_log,
            )
            self.assertIn(
                "twenty-seventh\n   pilot migration is now landed",
                distillation_roadmap,
            )
            self.assertIn(
                "Previous Candidate C migration breadcrumb preserved",
                root_roadmap,
            )
            self.assertIn(
                "2026-05-05-practice-adoption-lifecycle-tree-pilot",
                tree_contract,
            )
            self.assertIn("twenty-eight receipts", legacy_index)
            self.assertIn(
                "2026-05-05-practice-adoption-lifecycle-tree-pilot.md",
                legacy_index,
            )
            self.assertIn("twenty-eight technique tree pilot receipts", receipts_index)
            self.assertIn("moved `AOA-T-0101`", changelog)

            for technique_id, old_path, new_path in (
                (
                    "AOA-T-0101",
                    "techniques/agent-workflows/local-pattern-adoption-gate/",
                    "techniques/governance/practice-adoption-lifecycle/local-pattern-adoption-gate/",
                ),
                (
                    "AOA-T-0103",
                    "techniques/agent-workflows/adopted-practice-retention-review/",
                    "techniques/governance/practice-adoption-lifecycle/adopted-practice-retention-review/",
                ),
                (
                    "AOA-T-0104",
                    "techniques/agent-workflows/superseded-practice-obsolescence-route/",
                    "techniques/governance/practice-adoption-lifecycle/superseded-practice-obsolescence-route/",
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, receipt)
                    self.assertIn(old_path, receipt)
                    self.assertIn(new_path, receipt)
                    self.assertFalse((REPO_ROOT / old_path).exists())
                    self.assertTrue((REPO_ROOT / new_path / "TECHNIQUE.md").is_file())

    def test_landed_practice_adoption_lifecycle_pilot_review_routes_tool_gateway(
            self,
        ) -> None:
            review = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "landed-practice-adoption-lifecycle-pilot-review.md"
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
            ingress = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "README.md"
            ).read_text(encoding="utf-8")
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
            projection = (
                REPO_ROOT / validate_repo.TECHNIQUE_REFORM_REPORTS_DIR / "technique_tree_projection.md"
            ).read_text(encoding="utf-8")
            agent_workflows_agents = (
                REPO_ROOT / "techniques" / "agent-workflows" / "AGENTS.md"
            ).read_text(encoding="utf-8")
            tool_use_agents = (
                REPO_ROOT / "techniques" / "tool-use" / "AGENTS.md"
            ).read_text(encoding="utf-8")

            self.assertIn("Landed Practice-Adoption-Lifecycle Pilot Review", review)
            self.assertIn("pilot-validated", review)
            self.assertIn("split-tail-closed", review)
            self.assertIn(
                "No projected automation-governance ID remains unaccounted",
                review,
            )
            self.assertIn(
                "Run the direct-read singleton review for `tool-use/tool-gateway`",
                review,
            )
            self.assertIn(
                "landed-practice-adoption-lifecycle-pilot-review",
                reviews_index,
            )
            self.assertIn(
                "landed practice-adoption-lifecycle pilot review: landed",
                ingress,
            )
            self.assertIn(
                "Landed practice-adoption-lifecycle pilot review",
                landing_log,
            )
            self.assertIn("all nine split\n  IDs accounted", landing_log)
            self.assertIn(
                "landed `practice-adoption-lifecycle` pilot review is now complete",
                distillation_roadmap,
            )
            self.assertIn(
                "Previous tool-gateway breadcrumb preserved",
                root_roadmap,
            )
            self.assertIn(
                "Landed Practice-Adoption-Lifecycle Pilot Review",
                tree_contract,
            )
            self.assertIn("No projected automation-governance", tree_contract)
            self.assertIn("ID remains unaccounted", tree_contract)
            self.assertIn(
                "accepted the landed `practice-adoption-lifecycle` pilot review",
                changelog,
            )
            self.assertIn("| `split-review-needed` | `0` |", projection)
            self.assertIn("| `singleton-hold` | `0` |", projection)
            self.assertIn("no active leaf bundle currently lives directly here", agent_workflows_agents)
            self.assertIn("`tool-gateway/`", tool_use_agents)

            for technique_id, new_path in (
                (
                    "AOA-T-0086",
                    "techniques/governance/automation-readiness/automation-fit-matrix/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0089",
                    "techniques/governance/promotion-boundary/quest-unit-promotion-review/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0101",
                    "techniques/governance/practice-adoption-lifecycle/local-pattern-adoption-gate/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0104",
                    "techniques/governance/practice-adoption-lifecycle/superseded-practice-obsolescence-route/TECHNIQUE.md",
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)
                    self.assertTrue((REPO_ROOT / new_path).is_file())

            self.assertFalse(
                (
                    REPO_ROOT
                    / "techniques"
                    / "agent-workflows"
                    / "mcp-gateway-proxy"
                    / "TECHNIQUE.md"
                ).exists()
            )
            self.assertTrue(
                (
                    REPO_ROOT
                    / "techniques"
                    / "tool-use"
                    / "tool-gateway"
                    / "mcp-gateway-proxy"
                    / "TECHNIQUE.md"
                ).is_file()
            )

    def test_tool_gateway_direct_read_singleton_review_accepts_twenty_eighth_pilot(
            self,
        ) -> None:
            review = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "tool-gateway-direct-read-singleton-review.md"
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
            ingress = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "README.md"
            ).read_text(encoding="utf-8")
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
            projection = (
                REPO_ROOT / validate_repo.TECHNIQUE_REFORM_REPORTS_DIR / "technique_tree_projection.md"
            ).read_text(encoding="utf-8")

            self.assertIn("Tool-Gateway Direct-Read Singleton Review", review)
            self.assertIn("accepted-for-twenty-eighth-migration-pilot", review)
            self.assertIn("singleton-accepted", review)
            self.assertIn(
                "Accept `tool-use/tool-gateway` as the twenty-eighth",
                review,
            )
            self.assertIn("Move exactly `AOA-T-0065`", review)
            self.assertIn(
                "tool-gateway-direct-read-singleton-review",
                reviews_index,
            )
            self.assertIn(
                "tool-gateway direct-read singleton review: landed",
                ingress,
            )
            self.assertIn(
                "Tool-gateway direct-read singleton review",
                landing_log,
            )
            self.assertIn(
                "accepted `tool-use/tool-gateway` as the twenty-eighth",
                landing_log,
            )
            self.assertIn(
                "tool-gateway` direct-read singleton review is\n   now landed",
                distillation_roadmap,
            )
            self.assertIn(
                "Migrate exactly `AOA-T-0065`",
                root_roadmap,
            )
            self.assertIn(
                "Tool-Gateway Direct-Read Singleton Review",
                tree_contract,
            )
            self.assertIn(
                "accepted the `tool-gateway` direct-read singleton review",
                changelog,
            )
            self.assertIn("| `singleton-hold` | `0` |", projection)

            current_path = (
                REPO_ROOT
                / "techniques"
                / "agent-workflows"
                / "mcp-gateway-proxy"
                / "TECHNIQUE.md"
            )
            future_path = (
                REPO_ROOT
                / "techniques"
                / "tool-use"
                / "tool-gateway"
                / "mcp-gateway-proxy"
                / "TECHNIQUE.md"
            )
            self.assertFalse(current_path.exists())
            self.assertTrue(future_path.is_file())

    def test_tool_gateway_tree_pilot_migration_landed(self) -> None:
            receipt = (
                REPO_ROOT
                / "legacy"
                / "receipts"
                / "2026-05-05-tool-gateway-tree-pilot.md"
            ).read_text(encoding="utf-8")
            ingress = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "README.md"
            ).read_text(encoding="utf-8")
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
            projection = (
                REPO_ROOT / validate_repo.TECHNIQUE_REFORM_REPORTS_DIR / "technique_tree_projection.md"
            ).read_text(encoding="utf-8")
            tool_use_agents = (
                REPO_ROOT / "techniques" / "tool-use" / "AGENTS.md"
            ).read_text(encoding="utf-8")
            agent_workflows_agents = (
                REPO_ROOT / "techniques" / "agent-workflows" / "AGENTS.md"
            ).read_text(encoding="utf-8")

            self.assertIn("Tool-Gateway Tree Pilot Receipt", receipt)
            self.assertIn("Twenty-eighth authored path migration", receipt)
            self.assertIn("techniques/agent-workflows/mcp-gateway-proxy/", receipt)
            self.assertIn(
                "techniques/tool-use/tool-gateway/mcp-gateway-proxy/",
                receipt,
            )
            self.assertIn("No `tree_path`, `family`", receipt)
            self.assertIn("tool-gateway migration: landed", ingress)
            self.assertIn("Tool-gateway tree pilot migration", landing_log)
            self.assertIn("moved `AOA-T-0065`", landing_log)
            self.assertIn("migration is now landed exactly for that one bundle", distillation_roadmap)
            self.assertIn(
                "Review the landed `tool-use/tool-gateway` pilot",
                root_roadmap,
            )
            self.assertIn("twenty-eighth pilot migration moves exactly", tree_contract)
            self.assertIn(
                "moved `AOA-T-0065` into\n  `techniques/tool-use/tool-gateway/`",
                changelog,
            )
            self.assertIn("| `singleton-hold` | `0` |", projection)
            self.assertIn("`tool-gateway/`", tool_use_agents)
            self.assertIn("no active leaf bundle currently lives directly here", agent_workflows_agents)

            old_path = (
                REPO_ROOT
                / "techniques"
                / "agent-workflows"
                / "mcp-gateway-proxy"
                / "TECHNIQUE.md"
            )
            new_path = (
                REPO_ROOT
                / "techniques"
                / "tool-use"
                / "tool-gateway"
                / "mcp-gateway-proxy"
                / "TECHNIQUE.md"
            )
            self.assertFalse(old_path.exists())
            self.assertTrue(new_path.is_file())

    def test_landed_tool_gateway_pilot_review_routes_whole_tree_closeout(self) -> None:
            review = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "landed-tool-gateway-pilot-review.md"
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
            ingress = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "README.md"
            ).read_text(encoding="utf-8")
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
            projection = (
                REPO_ROOT / validate_repo.TECHNIQUE_REFORM_REPORTS_DIR / "technique_tree_projection.md"
            ).read_text(encoding="utf-8")

            self.assertIn("Landed Tool-Gateway Pilot Review", review)
            self.assertIn("pilot-validated", review)
            self.assertIn("singleton-resolved", review)
            self.assertIn("Choose whole-tree closeout review next", review)
            self.assertIn("landed-tool-gateway-pilot-review", reviews_index)
            self.assertIn("landed tool-gateway pilot review: landed", ingress)
            self.assertIn("Run the whole-tree closeout review", ingress)
            self.assertIn("Landed tool-gateway pilot review", landing_log)
            self.assertIn("whole-tree closeout review", distillation_roadmap)
            self.assertIn(
                "Run the whole-tree closeout review",
                root_roadmap,
            )
            self.assertIn("Landed Tool-Gateway Pilot Review", tree_contract)
            self.assertIn(
                "accepted the landed `tool-gateway` pilot review",
                changelog,
            )
            self.assertIn("| `singleton-hold` | `0` |", projection)
            self.assertTrue(
                (
                    REPO_ROOT
                    / "techniques"
                    / "tool-use"
                    / "tool-gateway"
                    / "mcp-gateway-proxy"
                    / "TECHNIQUE.md"
                ).is_file()
            )

    def test_whole_tree_closeout_review_validates_current_tree(self) -> None:
            review = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "whole-tree-closeout-review.md"
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
            ingress = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "README.md"
            ).read_text(encoding="utf-8")
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
            projection = json.loads(
                (REPO_ROOT / validate_repo.TECHNIQUE_REFORM_REPORTS_DIR / "technique_tree_projection.json").read_text(
                    encoding="utf-8"
                )
            )
            projection_markdown = (
                REPO_ROOT / validate_repo.TECHNIQUE_REFORM_REPORTS_DIR / "technique_tree_projection.md"
            ).read_text(encoding="utf-8")

            techniques = projection["techniques"]
            receipts = sorted(
                (REPO_ROOT / "legacy" / "receipts").glob("*tree-pilot.md")
            )
            direct_two_level_leaves = list(
                (REPO_ROOT / "techniques").glob("*/*/TECHNIQUE.md")
            )

            self.assertIn("Whole-Tree Closeout Review", review)
            self.assertIn("tree-closeout-validated", review)
            self.assertIn("current-paths-match-projection", review)
            self.assertIn("all-shelves-receipted", review)
            self.assertIn("Run tree route-card consolidation", review)
            self.assertIn("whole-tree-closeout-review", reviews_index)
            self.assertIn("whole-tree closeout review: landed", ingress)
            self.assertIn("Whole-tree closeout review", landing_log)
            self.assertIn("tree route-card consolidation", distillation_roadmap)
            self.assertIn(
                "Run tree route-card consolidation",
                root_roadmap,
            )
            self.assertIn("Whole-Tree Closeout Review", tree_contract)
            self.assertIn(
                "accepted the whole-tree closeout review",
                changelog,
            )
            self.assertEqual(107, len(techniques))
            self.assertEqual(
                107,
                sum(
                    entry["current_path"] == entry["proposed_future_path"]
                    for entry in techniques
                ),
            )
            self.assertEqual(28, len(receipts))
            self.assertEqual([], direct_two_level_leaves)
            self.assertEqual(
                0,
                projection["review_status_counts"]["split-review-needed"],
            )
            self.assertEqual(
                0,
                projection["review_status_counts"]["singleton-hold"],
            )
            self.assertEqual(
                0,
                projection["review_status_counts"]["unassigned-hold"],
            )
            self.assertIn("not source truth for bundle meaning", projection_markdown)

    def test_tree_route_card_consolidation_covers_current_trunks(self) -> None:
            techniques_agents = (REPO_ROOT / "techniques" / "AGENTS.md").read_text(
                encoding="utf-8"
            )
            validator = (REPO_ROOT / "scripts" / "validate_nested_agents.py").read_text(
                encoding="utf-8"
            )
            ingress = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "README.md"
            ).read_text(encoding="utf-8")
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            current_trunks = (
                "continuity",
                "execution",
                "governance",
                "history",
                "ingest",
                "instruction",
                "knowledge-lift",
                "proof",
                "recovery",
                "tool-use",
            )
            retained_lanes = ("agent-workflows", "docs", "evaluation")

            self.assertIn(
                "`techniques/<trunk>/<shelf>/<slug>/TECHNIQUE.md`",
                techniques_agents,
            )
            self.assertIn("tree route-card consolidation: landed", ingress)
            self.assertIn("Tree route-card consolidation", landing_log)
            self.assertIn("final migration ledger and generated parity pass", ingress)
            self.assertIn("final migration ledger and generated parity pass", distillation_roadmap)
            self.assertIn("Current latest tree route-card consolidation", root_roadmap)
            self.assertIn("Tree route-card consolidation is now complete", tree_contract)
            self.assertIn(
                "consolidated tree route cards",
                changelog,
            )

            for trunk in current_trunks:
                with self.subTest(trunk=trunk):
                    agents = (
                        REPO_ROOT / "techniques" / trunk / "AGENTS.md"
                    ).read_text(encoding="utf-8")
                    self.assertIn(
                        "shared placement applies",
                        agents,
                    )
                    self.assertIn("## Current Shelves", agents)
                    self.assertIn("## Trunk Rules", agents)
                    self.assertIn("path placement follows the parent contract", agents)
                    self.assertIn(
                        f'Path("techniques") / "{trunk}" / "AGENTS.md"',
                        validator,
                    )

            for lane in retained_lanes:
                with self.subTest(lane=lane):
                    agents = (
                        REPO_ROOT / "techniques" / lane / "AGENTS.md"
                    ).read_text(encoding="utf-8")
                    self.assertIn("retained frontmatter review lane", agents)
                    self.assertIn("not a current tree shelf", agents)
                    self.assertIn("Do not add a new leaf bundle directly", agents)
                    self.assertIn(
                        f'Path("techniques") / "{lane}" / "AGENTS.md"',
                        validator,
                    )

    def test_final_tree_migration_ledger_closes_tree_program(self) -> None:
            ledger = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "final-tree-migration-ledger.md"
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
            ingress = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "README.md"
            ).read_text(encoding="utf-8")
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
            projection = json.loads(
                (REPO_ROOT / validate_repo.TECHNIQUE_REFORM_REPORTS_DIR / "technique_tree_projection.json").read_text(
                    encoding="utf-8"
                )
            )

            self.assertIn("Final Tree Migration Ledger", ledger)
            self.assertIn("final-ledger-validated", ledger)
            self.assertIn("generated-parity-clean", ledger)
            self.assertIn("receipts-complete", ledger)
            self.assertIn("temporary-plan-distilled", ledger)
            self.assertIn("ready-for-technique-bundle-reform", ledger)
            self.assertIn("shelves with matching receipt | `28/28`", ledger)
            self.assertIn("current path equals projected path | `107/107`", ledger)
            self.assertIn(
                "direct `techniques/<domain>/<slug>/TECHNIQUE.md` leaves | `0`",
                ledger,
            )
            self.assertIn("Receipt matching is by projected shelf name", ledger)
            self.assertIn("deleted locally. Future agents", ledger)
            self.assertIn("Start technique-bundle reform", ledger)
            self.assertIn("final-tree-migration-ledger", reviews_index)
            self.assertIn("final tree migration ledger: landed", ingress)
            self.assertIn("Final tree migration ledger", landing_log)
            self.assertIn(
                "final migration ledger and generated parity pass is now complete",
                distillation_roadmap,
            )
            self.assertIn("Current latest final tree ledger", root_roadmap)
            self.assertIn("Final Tree Migration Ledger", tree_contract)
            self.assertIn(
                "added the final tree migration ledger",
                changelog,
            )
            self.assertEqual(107, len(projection["techniques"]))
            self.assertEqual(
                107,
                sum(
                    entry["current_path"] == entry["proposed_future_path"]
                    for entry in projection["techniques"]
                ),
            )


if __name__ == "__main__":
    unittest.main()
