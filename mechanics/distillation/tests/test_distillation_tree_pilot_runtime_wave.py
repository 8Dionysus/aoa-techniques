from __future__ import annotations

import sys
import unittest
from pathlib import Path


SUPPORT_DIR = Path(__file__).resolve().parent / "support"
if str(SUPPORT_DIR) not in sys.path:
    sys.path.insert(0, str(SUPPORT_DIR))

from distillation_topology_fixtures import *  # noqa: F403


class DistillationTreePilotRuntimeWaveTests(unittest.TestCase):
    def test_agent_workflows_core_direct_read_review_accepts_eighteenth_pilot(
            self,
        ) -> None:
            review = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "agent-workflows-core-direct-read-migration-review.md"
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

            self.assertIn("Agent-Workflows-Core Direct-Read Migration Review", review)
            self.assertIn("accepted-for-eighteenth-migration-pilot", review)
            self.assertIn("Accept `execution/agent-workflows-core`", review)
            self.assertIn("visible, bounded, reviewable agent work", review)
            self.assertIn("Do not remap `AOA-T-0028` from `guardrail`", review)
            self.assertIn("Run the eighteenth migration pilot", review)
            self.assertIn("agent-workflows-core-direct-read-migration-review", reviews_index)
            self.assertIn("agent-workflows-core direct-read review: landed", ingress)
            self.assertIn("accepted-for-eighteenth-migration-pilot", ingress)
            self.assertIn("Agent-workflows-core direct-read migration review", landing_log)
            self.assertIn("preserved `AOA-T-0028` as `kind: guardrail`", landing_log)
            self.assertIn("accepted-for-eighteenth-migration-pilot", distillation_roadmap)
            self.assertIn("eighteenth pilot migration moved", root_roadmap)
            self.assertIn("Agent-Workflows-Core Direct-Read Migration Review", tree_contract)
            self.assertIn("preserves\n`AOA-T-0028` as `guardrail`", tree_contract)
            self.assertIn(
                "accepted the `agent-workflows-core` direct-read migration review",
                changelog,
            )

            for technique_id, old_path, current_path in (
                (
                    "AOA-T-0001",
                    "techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md",
                    "techniques/execution/agent-workflows-core/plan-diff-apply-verify-report/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0014",
                    "techniques/agent-workflows/tdd-slice/TECHNIQUE.md",
                    "techniques/execution/agent-workflows-core/tdd-slice/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0023",
                    "techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md",
                    "techniques/execution/agent-workflows-core/stateless-single-shot-agent/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0028",
                    "techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md",
                    "techniques/execution/agent-workflows-core/confirmation-gated-mutating-action/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0031",
                    "techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md",
                    "techniques/execution/agent-workflows-core/shell-composable-agent-invocation/TECHNIQUE.md",
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)
                    self.assertIn(old_path.rsplit("/", 1)[0] + "/", review)
                    self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                    self.assertFalse((REPO_ROOT / old_path).exists())
                    self.assertTrue((REPO_ROOT / current_path).is_file())

    def test_agent_workflows_core_tree_pilot_migration_landed(self) -> None:
            receipt = (
                REPO_ROOT
                / "legacy"
                / "receipts"
                / "2026-05-05-agent-workflows-core-tree-pilot.md"
            ).read_text(encoding="utf-8")
            execution_agents = (
                REPO_ROOT / "techniques" / "execution" / "AGENTS.md"
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

            self.assertIn("Agent-Workflows-Core Tree Pilot Receipt", receipt)
            self.assertIn("Eighteenth authored path migration", receipt)
            self.assertIn("AOA-T-0028` stayed `kind: guardrail`", receipt)
            self.assertIn("AOA-T-0031` stayed `kind: composition`", receipt)
            self.assertIn("agent-workflows-core/", execution_agents)
            self.assertIn("generic agent doctrine, shell policy", execution_agents)
            self.assertIn("agent-workflows-core migration: landed", ingress)
            self.assertIn("Agent-workflows-core tree pilot migration", landing_log)
            self.assertIn("eighteenth pilot migration is now\n   landed", distillation_roadmap)
            self.assertIn("eighteenth pilot without moving files", root_roadmap)
            self.assertIn("Review the landed `agent-workflows-core` pilot", root_roadmap)
            self.assertIn("2026-05-05-agent-workflows-core-tree-pilot", tree_contract)
            self.assertIn("moved `AOA-T-0001`", changelog)

            for technique_id, old_path, current_path in (
                (
                    "AOA-T-0001",
                    "techniques/agent-workflows/plan-diff-apply-verify-report/",
                    "techniques/execution/agent-workflows-core/plan-diff-apply-verify-report/",
                ),
                (
                    "AOA-T-0014",
                    "techniques/agent-workflows/tdd-slice/",
                    "techniques/execution/agent-workflows-core/tdd-slice/",
                ),
                (
                    "AOA-T-0023",
                    "techniques/agent-workflows/stateless-single-shot-agent/",
                    "techniques/execution/agent-workflows-core/stateless-single-shot-agent/",
                ),
                (
                    "AOA-T-0028",
                    "techniques/agent-workflows/confirmation-gated-mutating-action/",
                    "techniques/execution/agent-workflows-core/confirmation-gated-mutating-action/",
                ),
                (
                    "AOA-T-0031",
                    "techniques/agent-workflows/shell-composable-agent-invocation/",
                    "techniques/execution/agent-workflows-core/shell-composable-agent-invocation/",
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, receipt)
                    self.assertIn(old_path, receipt)
                    self.assertIn(current_path, receipt)
                    self.assertFalse((REPO_ROOT / old_path).exists())
                    self.assertTrue((REPO_ROOT / current_path / "TECHNIQUE.md").is_file())

    def test_landed_agent_workflows_core_review_selects_donor_harvest(
            self,
        ) -> None:
            review = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "landed-agent-workflows-core-pilot-review.md"
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

            self.assertIn("Landed Agent-Workflows-Core Pilot Review", review)
            self.assertIn("third successful shelf under the `execution` trunk", review)
            self.assertIn("mixed `workflow` / `guardrail` / `composition`", review)
            self.assertIn("Choose `continuity/donor-harvest`", review)
            self.assertIn("Do not move `continuity/donor-harvest`", review)
            self.assertIn("memory authority, playbook quest authority", review)
            self.assertIn(
                "Run a direct-read migration review for `continuity/donor-harvest`",
                review,
            )
            self.assertIn("landed-agent-workflows-core-pilot-review", reviews_index)
            self.assertIn("landed agent-workflows-core pilot review: landed", ingress)
            self.assertIn("continuity/donor-harvest", ingress)
            self.assertIn("Landed agent-workflows-core pilot review", landing_log)
            self.assertIn("third successful execution trunk", landing_log)
            self.assertIn("continuity/donor-harvest` for the next", landing_log)
            self.assertIn("The landed `agent-workflows-core` pilot\n   review", distillation_roadmap)
            self.assertIn(
                "Run the `continuity/donor-harvest` direct-read",
                root_roadmap,
            )
            self.assertIn("Landed Agent-Workflows-Core Pilot Review", tree_contract)
            self.assertIn("chooses `continuity/donor-harvest`", tree_contract)
            self.assertIn(
                "accepted the landed `agent-workflows-core` pilot review",
                changelog,
            )

            for technique_id, current_path, future_path in (
                (
                    "AOA-T-0075",
                    "techniques/agent-workflows/session-donor-harvest/TECHNIQUE.md",
                    "techniques/continuity/donor-harvest/session-donor-harvest/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0077",
                    "techniques/agent-workflows/harvest-packet-contract/TECHNIQUE.md",
                    "techniques/continuity/donor-harvest/harvest-packet-contract/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0084",
                    "techniques/agent-workflows/progression-evidence-lift/TECHNIQUE.md",
                    "techniques/continuity/donor-harvest/progression-evidence-lift/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0085",
                    "techniques/agent-workflows/multi-axis-quest-overlay/TECHNIQUE.md",
                    "techniques/continuity/donor-harvest/multi-axis-quest-overlay/TECHNIQUE.md",
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)
                    self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                    self.assertIn(future_path.rsplit("/", 1)[0] + "/", review)
                    self.assertFalse((REPO_ROOT / current_path).exists())
                    self.assertTrue((REPO_ROOT / future_path).is_file())

    def test_donor_harvest_direct_read_review_accepts_nineteenth_pilot(
            self,
        ) -> None:
            review = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "donor-harvest-direct-read-migration-review.md"
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

            self.assertIn("Donor-Harvest Direct-Read Migration Review", review)
            self.assertIn("accepted-for-nineteenth-migration-pilot", review)
            self.assertIn("Accept `continuity/donor-harvest`", review)
            self.assertIn("Do not move files from this review pack alone", review)
            self.assertIn("memory authority, playbook quest authority", review)
            self.assertIn("Run the nineteenth migration pilot", review)
            self.assertIn("donor-harvest-direct-read-migration-review", reviews_index)
            self.assertIn("donor-harvest direct-read review: landed", ingress)
            self.assertIn("accepted-for-nineteenth-migration-pilot", ingress)
            self.assertIn("Donor-harvest direct-read migration review", landing_log)
            self.assertIn("accepted-for-nineteenth-migration-pilot", distillation_roadmap)
            self.assertIn("nineteenth pilot migration moved", root_roadmap)
            self.assertIn("Donor-Harvest Direct-Read Migration Review", tree_contract)
            self.assertIn(
                "accepted the `donor-harvest` direct-read migration review",
                changelog,
            )

            for technique_id, current_path, future_path in (
                (
                    "AOA-T-0075",
                    "techniques/agent-workflows/session-donor-harvest/TECHNIQUE.md",
                    "techniques/continuity/donor-harvest/session-donor-harvest/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0077",
                    "techniques/agent-workflows/harvest-packet-contract/TECHNIQUE.md",
                    "techniques/continuity/donor-harvest/harvest-packet-contract/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0084",
                    "techniques/agent-workflows/progression-evidence-lift/TECHNIQUE.md",
                    "techniques/continuity/donor-harvest/progression-evidence-lift/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0085",
                    "techniques/agent-workflows/multi-axis-quest-overlay/TECHNIQUE.md",
                    "techniques/continuity/donor-harvest/multi-axis-quest-overlay/TECHNIQUE.md",
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)
                    self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                    self.assertIn(future_path.rsplit("/", 1)[0] + "/", review)
                    self.assertFalse((REPO_ROOT / current_path).exists())
                    self.assertTrue((REPO_ROOT / future_path).is_file())

    def test_donor_harvest_tree_pilot_migration_landed(self) -> None:
            receipt = (
                REPO_ROOT
                / "legacy"
                / "receipts"
                / "2026-05-05-donor-harvest-tree-pilot.md"
            ).read_text(encoding="utf-8")
            continuity_agents = (
                REPO_ROOT / "techniques" / "continuity" / "AGENTS.md"
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

            self.assertIn("Donor-Harvest Tree Pilot Receipt", receipt)
            self.assertIn("Nineteenth authored path migration", receipt)
            self.assertIn("AOA-T-0077` stayed `kind: handoff`", receipt)
            self.assertIn("AOA-T-0075`, `AOA-T-0084`, and `AOA-T-0085` stayed", receipt)
            self.assertIn("donor-harvest/", continuity_agents)
            self.assertIn("without granting memory, playbook, or progression authority", continuity_agents)
            self.assertIn("donor-harvest migration: landed", ingress)
            self.assertIn("Donor-harvest tree pilot migration", landing_log)
            self.assertIn("legacy/receipts/2026-05-05-donor-harvest-tree-pilot.md", landing_log)
            self.assertIn("nineteenth pilot migration is now landed", distillation_roadmap)
            self.assertIn("Review the landed `donor-harvest` pilot", root_roadmap)
            self.assertIn("2026-05-05-donor-harvest-tree-pilot", tree_contract)
            self.assertIn("twenty-eight receipts", legacy_index)
            self.assertIn("2026-05-05-donor-harvest-tree-pilot.md", legacy_index)
            self.assertIn("twenty-eight technique tree pilot receipts", receipts_index)
            self.assertIn("moved `AOA-T-0075`", changelog)

            for technique_id, old_path, new_path in (
                (
                    "AOA-T-0075",
                    "techniques/agent-workflows/session-donor-harvest/",
                    "techniques/continuity/donor-harvest/session-donor-harvest/",
                ),
                (
                    "AOA-T-0077",
                    "techniques/agent-workflows/harvest-packet-contract/",
                    "techniques/continuity/donor-harvest/harvest-packet-contract/",
                ),
                (
                    "AOA-T-0084",
                    "techniques/agent-workflows/progression-evidence-lift/",
                    "techniques/continuity/donor-harvest/progression-evidence-lift/",
                ),
                (
                    "AOA-T-0085",
                    "techniques/agent-workflows/multi-axis-quest-overlay/",
                    "techniques/continuity/donor-harvest/multi-axis-quest-overlay/",
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, receipt)
                    self.assertIn(old_path, receipt)
                    self.assertIn(new_path, receipt)
                    self.assertFalse((REPO_ROOT / old_path).exists())
                    self.assertTrue((REPO_ROOT / new_path / "TECHNIQUE.md").is_file())

    def test_landed_donor_harvest_review_selects_decision_routing(self) -> None:
            review = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "landed-donor-harvest-pilot-review.md"
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

            self.assertIn("Landed Donor-Harvest Pilot Review", review)
            self.assertIn("third successful shelf under the `continuity` trunk", review)
            self.assertIn("Choose `governance/decision-routing`", review)
            self.assertIn("Do not move `governance/decision-routing`", review)
            self.assertIn("no governance route card was created", landing_log)
            self.assertIn(
                "Run a direct-read migration review for `governance/decision-routing`",
                review,
            )
            self.assertIn("landed-donor-harvest-pilot-review", reviews_index)
            self.assertIn("landed donor-harvest pilot review: landed", ingress)
            self.assertIn("governance/decision-routing", ingress)
            self.assertIn("Landed donor-harvest pilot review", landing_log)
            self.assertIn("third successful continuity trunk", landing_log)
            self.assertIn("The landed\n   `donor-harvest` pilot review", distillation_roadmap)
            self.assertIn("chooses `governance/decision-routing`", root_roadmap)
            self.assertIn("Landed Donor-Harvest Pilot Review", tree_contract)
            self.assertIn("chooses `governance/decision-routing`", tree_contract)
            self.assertIn(
                "accepted the landed `donor-harvest` pilot review",
                changelog,
            )
            self.assertTrue(
                (REPO_ROOT / "techniques" / "governance" / "AGENTS.md").is_file()
            )

            for technique_id, current_path, future_path in (
                (
                    "AOA-T-0076",
                    "techniques/agent-workflows/owner-layer-triage/TECHNIQUE.md",
                    "techniques/governance/decision-routing/owner-layer-triage/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0078",
                    "techniques/agent-workflows/decision-fork-cards/TECHNIQUE.md",
                    "techniques/governance/decision-routing/decision-fork-cards/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0079",
                    "techniques/agent-workflows/risk-passport-lift/TECHNIQUE.md",
                    "techniques/governance/decision-routing/risk-passport-lift/TECHNIQUE.md",
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)
                    self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                    self.assertIn(future_path.rsplit("/", 1)[0] + "/", review)
                    self.assertFalse((REPO_ROOT / current_path).exists())
                    self.assertTrue((REPO_ROOT / future_path).is_file())

    def test_decision_routing_direct_read_review_accepts_twentieth_pilot(
            self,
        ) -> None:
            review = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "decision-routing-direct-read-migration-review.md"
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

            self.assertIn("Decision-Routing Direct-Read Migration Review", review)
            self.assertIn("accepted-for-twentieth-migration-pilot", review)
            self.assertIn("Accept `governance/decision-routing`", review)
            self.assertIn("Do not move files from this review pack alone", review)
            self.assertIn("AoA constitutional authority", review)
            self.assertIn("Run the twentieth migration pilot", review)
            self.assertIn("decision-routing-direct-read-migration-review", reviews_index)
            self.assertIn("decision-routing direct-read review: landed", ingress)
            self.assertIn("accepted-for-twentieth-migration-pilot", ingress)
            self.assertIn("Decision-routing direct-read migration review", landing_log)
            self.assertIn("accepted-for-twentieth-migration-pilot", distillation_roadmap)
            self.assertIn("twentieth pilot without moving files", root_roadmap)
            self.assertIn("Decision-Routing Direct-Read Migration Review", tree_contract)
            self.assertIn(
                "accepted the `decision-routing` direct-read migration review",
                changelog,
            )
            self.assertTrue(
                (REPO_ROOT / "techniques" / "governance" / "AGENTS.md").is_file()
            )

            for technique_id, current_path, future_path in (
                (
                    "AOA-T-0076",
                    "techniques/agent-workflows/owner-layer-triage/TECHNIQUE.md",
                    "techniques/governance/decision-routing/owner-layer-triage/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0078",
                    "techniques/agent-workflows/decision-fork-cards/TECHNIQUE.md",
                    "techniques/governance/decision-routing/decision-fork-cards/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0079",
                    "techniques/agent-workflows/risk-passport-lift/TECHNIQUE.md",
                    "techniques/governance/decision-routing/risk-passport-lift/TECHNIQUE.md",
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)
                    self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                    self.assertIn(future_path.rsplit("/", 1)[0] + "/", review)
                    self.assertFalse((REPO_ROOT / current_path).exists())
                    self.assertTrue((REPO_ROOT / future_path).is_file())

    def test_decision_routing_tree_pilot_migration_landed(self) -> None:
            receipt = (
                REPO_ROOT
                / "legacy"
                / "receipts"
                / "2026-05-05-decision-routing-tree-pilot.md"
            ).read_text(encoding="utf-8")
            governance_agents = (
                REPO_ROOT / "techniques" / "governance" / "AGENTS.md"
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

            self.assertIn("Decision-Routing Tree Pilot Receipt", receipt)
            self.assertIn("Twentieth authored path migration", receipt)
            self.assertIn("`kind` stayed unchanged as `assessment`", receipt)
            self.assertIn("stayed `promoted`", receipt)
            self.assertIn("decision-routing/", governance_agents)
            self.assertIn(
                "Do not turn a governance technique into AoA constitutional authority",
                governance_agents,
            )
            self.assertIn("decision-routing migration: landed", ingress)
            self.assertIn("Decision-routing tree pilot migration", landing_log)
            self.assertIn(
                "legacy/receipts/2026-05-05-decision-routing-tree-pilot.md",
                landing_log,
            )
            self.assertIn(
                "twentieth pilot migration is now landed",
                distillation_roadmap,
            )
            self.assertIn("Review the landed `decision-routing` pilot", root_roadmap)
            self.assertIn("2026-05-05-decision-routing-tree-pilot", tree_contract)
            self.assertIn("twenty-eight receipts", legacy_index)
            self.assertIn(
                "2026-05-05-decision-routing-tree-pilot.md",
                legacy_index,
            )
            self.assertIn("twenty-eight technique tree pilot receipts", receipts_index)
            self.assertIn("moved `AOA-T-0076`", changelog)

            for technique_id, old_path, new_path in (
                (
                    "AOA-T-0076",
                    "techniques/agent-workflows/owner-layer-triage/",
                    "techniques/governance/decision-routing/owner-layer-triage/",
                ),
                (
                    "AOA-T-0078",
                    "techniques/agent-workflows/decision-fork-cards/",
                    "techniques/governance/decision-routing/decision-fork-cards/",
                ),
                (
                    "AOA-T-0079",
                    "techniques/agent-workflows/risk-passport-lift/",
                    "techniques/governance/decision-routing/risk-passport-lift/",
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, receipt)
                    self.assertIn(old_path, receipt)
                    self.assertIn(new_path, receipt)
                    self.assertFalse((REPO_ROOT / old_path).exists())
                    self.assertTrue((REPO_ROOT / new_path / "TECHNIQUE.md").is_file())

    def test_landed_decision_routing_review_selects_approval_evidence(
            self,
        ) -> None:
            review = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "landed-decision-routing-pilot-review.md"
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

            self.assertIn("Landed Decision-Routing Pilot Review", review)
            self.assertIn(
                "first successful shelf under the `governance` trunk",
                review,
            )
            self.assertIn("Choose `governance/approval-evidence`", review)
            self.assertIn("Do not move `governance/approval-evidence`", review)
            self.assertIn(
                "Run a direct-read migration review for `governance/approval-evidence`",
                review,
            )
            self.assertIn("landed-decision-routing-pilot-review", reviews_index)
            self.assertIn("landed decision-routing pilot review: landed", ingress)
            self.assertIn("governance/approval-evidence", ingress)
            self.assertIn("Landed decision-routing pilot review", landing_log)
            self.assertIn("first successful\n  governance trunk shelf", landing_log)
            self.assertIn("no `governance/approval-evidence` route card", landing_log)
            self.assertIn(
                "landed `decision-routing` review is\n   now complete",
                distillation_roadmap,
            )
            self.assertIn("chooses `governance/approval-evidence`", root_roadmap)
            self.assertIn(
                "Run the `governance/approval-evidence` direct-read",
                root_roadmap,
            )
            self.assertIn("Landed Decision-Routing Pilot Review", tree_contract)
            self.assertIn(
                "directly read `AOA-T-0068` and `AOA-T-0069`",
                tree_contract,
            )
            self.assertIn(
                "accepted the landed `decision-routing` pilot review",
                changelog,
            )
            self.assertTrue(
                (
                    REPO_ROOT / "techniques" / "governance" / "approval-evidence"
                ).is_dir()
            )

            for technique_id, current_path, future_path in (
                (
                    "AOA-T-0068",
                    "techniques/agent-workflows/fail-closed-evidence-gate/TECHNIQUE.md",
                    "techniques/governance/approval-evidence/fail-closed-evidence-gate/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0069",
                    "techniques/agent-workflows/approval-bound-durable-jobs/TECHNIQUE.md",
                    "techniques/governance/approval-evidence/approval-bound-durable-jobs/TECHNIQUE.md",
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)
                    self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                    self.assertIn(future_path.rsplit("/", 1)[0] + "/", review)
                    self.assertFalse((REPO_ROOT / current_path).exists())
                    self.assertTrue((REPO_ROOT / future_path).is_file())

    def test_approval_evidence_direct_read_review_accepts_twenty_first_pilot(
            self,
        ) -> None:
            review = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "approval-evidence-direct-read-migration-review.md"
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

            self.assertIn("Approval-Evidence Direct-Read Migration Review", review)
            self.assertIn("accepted-for-twenty-first-migration-pilot", review)
            self.assertIn("Accept `governance/approval-evidence`", review)
            self.assertIn("Do not move files from this review pack alone", review)
            self.assertIn("approval policy", review)
            self.assertIn("Run the twenty-first migration pilot", review)
            self.assertIn("approval-evidence-direct-read-migration-review", reviews_index)
            self.assertIn("approval-evidence direct-read review: landed", ingress)
            self.assertIn("accepted-for-twenty-first-migration-pilot", ingress)
            self.assertIn("Approval-evidence direct-read migration review", landing_log)
            self.assertIn("accepted-for-twenty-first-migration-pilot", distillation_roadmap)
            self.assertIn("twenty-first pilot without moving files", root_roadmap)
            self.assertIn("twenty-first pilot migration moved those two bundles", root_roadmap)
            self.assertIn("Approval-Evidence Direct-Read Migration Review", tree_contract)
            self.assertIn("2026-05-05-approval-evidence-tree-pilot", tree_contract)
            self.assertIn(
                "accepted the `approval-evidence` direct-read migration review",
                changelog,
            )
            self.assertTrue(
                (
                    REPO_ROOT / "techniques" / "governance" / "approval-evidence"
                ).is_dir()
            )

            for technique_id, current_path, future_path in (
                (
                    "AOA-T-0068",
                    "techniques/agent-workflows/fail-closed-evidence-gate/TECHNIQUE.md",
                    "techniques/governance/approval-evidence/fail-closed-evidence-gate/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0069",
                    "techniques/agent-workflows/approval-bound-durable-jobs/TECHNIQUE.md",
                    "techniques/governance/approval-evidence/approval-bound-durable-jobs/TECHNIQUE.md",
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)
                    self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                    self.assertIn(future_path.rsplit("/", 1)[0] + "/", review)
                    self.assertFalse((REPO_ROOT / current_path).exists())
                    self.assertTrue((REPO_ROOT / future_path).is_file())

    def test_approval_evidence_tree_pilot_migration_landed(self) -> None:
            receipt = (
                REPO_ROOT
                / "legacy"
                / "receipts"
                / "2026-05-05-approval-evidence-tree-pilot.md"
            ).read_text(encoding="utf-8")
            governance_agents = (
                REPO_ROOT / "techniques" / "governance" / "AGENTS.md"
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

            self.assertIn("Approval-Evidence Tree Pilot Receipt", receipt)
            self.assertIn("Twenty-first authored path migration", receipt)
            self.assertIn("`kind` stayed unchanged as `guardrail`", receipt)
            self.assertIn("`kind` stayed unchanged as `handoff`", receipt)
            self.assertIn("stayed `promoted`", receipt)
            self.assertIn("approval-evidence/", governance_agents)
            self.assertIn("scheduler doctrine", governance_agents)
            self.assertIn("approval-evidence migration: landed", ingress)
            self.assertIn("Approval-evidence tree pilot migration", landing_log)
            self.assertIn(
                "legacy/receipts/2026-05-05-approval-evidence-tree-pilot.md",
                landing_log,
            )
            self.assertIn(
                "twenty-first pilot migration is now landed",
                distillation_roadmap,
            )
            self.assertIn(
                "Review the landed `governance/approval-evidence` pilot",
                root_roadmap,
            )
            self.assertIn("2026-05-05-approval-evidence-tree-pilot", tree_contract)
            self.assertIn("twenty-eight receipts", legacy_index)
            self.assertIn(
                "2026-05-05-approval-evidence-tree-pilot.md",
                legacy_index,
            )
            self.assertIn("twenty-eight technique tree pilot receipts", receipts_index)
            self.assertIn("moved `AOA-T-0068`", changelog)

            for technique_id, old_path, new_path in (
                (
                    "AOA-T-0068",
                    "techniques/agent-workflows/fail-closed-evidence-gate/",
                    "techniques/governance/approval-evidence/fail-closed-evidence-gate/",
                ),
                (
                    "AOA-T-0069",
                    "techniques/agent-workflows/approval-bound-durable-jobs/",
                    "techniques/governance/approval-evidence/approval-bound-durable-jobs/",
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, receipt)
                    self.assertIn(old_path, receipt)
                    self.assertIn(new_path, receipt)
                    self.assertFalse((REPO_ROOT / old_path).exists())
                    self.assertTrue((REPO_ROOT / new_path / "TECHNIQUE.md").is_file())

    def test_landed_approval_evidence_review_selects_review_evidence(
            self,
        ) -> None:
            review = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "landed-approval-evidence-pilot-review.md"
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

            self.assertIn("Landed Approval-Evidence Pilot Review", review)
            self.assertIn("second successful shelf under the `governance` trunk", review)
            self.assertIn("Choose `proof/review-evidence`", review)
            self.assertIn("Do not move `proof/review-evidence`", review)
            self.assertIn("proof verdict authority", review)
            self.assertIn(
                "Run a direct-read migration review for `proof/review-evidence`",
                review,
            )
            self.assertIn("landed-approval-evidence-pilot-review", reviews_index)
            self.assertIn("landed approval-evidence pilot review: landed", ingress)
            self.assertIn("proof/review-evidence", ingress)
            self.assertIn("Landed approval-evidence pilot review", landing_log)
            self.assertIn("Review-evidence tree pilot migration", landing_log)
            self.assertIn(
                "landed `approval-evidence` review is now complete",
                distillation_roadmap,
            )
            self.assertIn(
                "Review the landed `execution/runtime-truth-lifecycle` pilot",
                root_roadmap,
            )
            self.assertIn("Landed Approval-Evidence Pilot Review", tree_contract)
            self.assertIn(
                "Review-Evidence Direct-Read Migration Review",
                tree_contract,
            )
            self.assertIn(
                "accepted the landed `approval-evidence` pilot review",
                changelog,
            )
            self.assertTrue(
                (
                    REPO_ROOT / "techniques" / "proof" / "review-evidence"
                ).is_dir()
            )

            for technique_id, current_path, future_path in (
                (
                    "AOA-T-0105",
                    "techniques/agent-workflows/single-missing-evidence-request/TECHNIQUE.md",
                    "techniques/proof/review-evidence/single-missing-evidence-request/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0107",
                    "techniques/agent-workflows/single-locus-claim-challenge/TECHNIQUE.md",
                    "techniques/proof/review-evidence/single-locus-claim-challenge/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0106",
                    "techniques/docs/single-scoped-evidence-reference/TECHNIQUE.md",
                    "techniques/proof/review-evidence/single-scoped-evidence-reference/TECHNIQUE.md",
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)
                    self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                    self.assertIn(future_path.rsplit("/", 1)[0] + "/", review)
                    self.assertFalse((REPO_ROOT / current_path).exists())
                    self.assertTrue((REPO_ROOT / future_path).is_file())

    def test_review_evidence_direct_read_review_accepts_twenty_second_pilot(
            self,
        ) -> None:
            review = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "review-evidence-direct-read-migration-review.md"
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

            self.assertIn("Review-Evidence Direct-Read Migration Review", review)
            self.assertIn("accepted-for-twenty-second-migration-pilot", review)
            self.assertIn("Accept `proof/review-evidence`", review)
            self.assertIn("Do not move files from this review pack alone", review)
            self.assertIn("proof verdict authority", review)
            self.assertIn("source-truth transfer", review)
            self.assertIn("Run the twenty-second migration pilot", review)
            self.assertIn("review-evidence-direct-read-migration-review", reviews_index)
            self.assertIn("review-evidence direct-read review: landed", ingress)
            self.assertIn("accepted-for-twenty-second-migration-pilot", ingress)
            self.assertIn("Review-evidence direct-read migration review", landing_log)
            self.assertIn("Review-evidence tree pilot migration", landing_log)
            self.assertIn(
                "The `review-evidence` direct-read review is now landed",
                distillation_roadmap,
            )
            self.assertIn(
                "Review the landed `execution/runtime-truth-lifecycle` pilot",
                root_roadmap,
            )
            self.assertIn("Review-Evidence Direct-Read Migration Review", tree_contract)
            self.assertIn("2026-05-05-review-evidence-tree-pilot", tree_contract)
            self.assertIn(
                "twenty-second pilot migration moves exactly those three bundles",
                tree_contract,
            )
            self.assertIn(
                "accepted the `review-evidence` direct-read migration review",
                changelog,
            )
            self.assertTrue(
                (
                    REPO_ROOT / "techniques" / "proof" / "review-evidence"
                ).is_dir()
            )

            for technique_id, current_path, future_path in (
                (
                    "AOA-T-0107",
                    "techniques/agent-workflows/single-locus-claim-challenge/TECHNIQUE.md",
                    "techniques/proof/review-evidence/single-locus-claim-challenge/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0105",
                    "techniques/agent-workflows/single-missing-evidence-request/TECHNIQUE.md",
                    "techniques/proof/review-evidence/single-missing-evidence-request/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0106",
                    "techniques/docs/single-scoped-evidence-reference/TECHNIQUE.md",
                    "techniques/proof/review-evidence/single-scoped-evidence-reference/TECHNIQUE.md",
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)
                    self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                    self.assertIn(future_path.rsplit("/", 1)[0] + "/", review)
                    self.assertFalse((REPO_ROOT / current_path).exists())
                    self.assertTrue((REPO_ROOT / future_path).is_file())

    def test_review_evidence_tree_pilot_migration_landed(self) -> None:
            receipt = (
                REPO_ROOT
                / "legacy"
                / "receipts"
                / "2026-05-05-review-evidence-tree-pilot.md"
            ).read_text(encoding="utf-8")
            proof_agents = (REPO_ROOT / "techniques" / "proof" / "AGENTS.md").read_text(
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
            legacy_index = (REPO_ROOT / "legacy" / "INDEX.md").read_text(
                encoding="utf-8"
            )
            receipts_index = (
                REPO_ROOT / "legacy" / "receipts" / "README.md"
            ).read_text(encoding="utf-8")
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Review-Evidence Tree Pilot Receipt", receipt)
            self.assertIn("Twenty-second authored path migration", receipt)
            self.assertIn("`kind` stayed unchanged as `guardrail`", receipt)
            self.assertIn("`kind` stayed unchanged as `artifact`", receipt)
            self.assertIn("stayed `promoted`", receipt)
            self.assertIn("review-evidence/", proof_agents)
            self.assertIn("evidence adequacy scoring", proof_agents)
            self.assertIn("review-evidence migration: landed", ingress)
            self.assertIn("Review-evidence tree pilot migration", landing_log)
            self.assertIn(
                "legacy/receipts/2026-05-05-review-evidence-tree-pilot.md",
                landing_log,
            )
            self.assertIn(
                "twenty-second pilot migration is now landed",
                distillation_roadmap,
            )
            self.assertIn(
                "Review the landed `execution/runtime-truth-lifecycle` pilot",
                root_roadmap,
            )
            self.assertIn("2026-05-05-review-evidence-tree-pilot", tree_contract)
            self.assertIn("twenty-eight receipts", legacy_index)
            self.assertIn(
                "2026-05-05-review-evidence-tree-pilot.md",
                legacy_index,
            )
            self.assertIn("twenty-eight technique tree pilot receipts", receipts_index)
            self.assertIn("moved `AOA-T-0107`", changelog)

            for technique_id, old_path, new_path in (
                (
                    "AOA-T-0107",
                    "techniques/agent-workflows/single-locus-claim-challenge/",
                    "techniques/proof/review-evidence/single-locus-claim-challenge/",
                ),
                (
                    "AOA-T-0105",
                    "techniques/agent-workflows/single-missing-evidence-request/",
                    "techniques/proof/review-evidence/single-missing-evidence-request/",
                ),
                (
                    "AOA-T-0106",
                    "techniques/docs/single-scoped-evidence-reference/",
                    "techniques/proof/review-evidence/single-scoped-evidence-reference/",
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, receipt)
                    self.assertIn(old_path, receipt)
                    self.assertIn(new_path, receipt)
                    self.assertFalse((REPO_ROOT / old_path).exists())
                    self.assertTrue((REPO_ROOT / new_path / "TECHNIQUE.md").is_file())

    def test_landed_review_evidence_pilot_review_selects_runtime_truth_lifecycle(
            self,
        ) -> None:
            review = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "landed-review-evidence-pilot-review.md"
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

            self.assertIn("Landed Review-Evidence Pilot Review", review)
            self.assertIn("fourth successful shelf under the `proof` trunk", review)
            self.assertIn("Choose `execution/runtime-truth-lifecycle`", review)
            self.assertIn("Do not move `execution/runtime-truth-lifecycle`", review)
            self.assertIn("abyss-stack` runtime law", review)
            self.assertIn(
                "Run a direct-read migration review for `execution/runtime-truth-lifecycle`",
                review,
            )
            self.assertIn("landed-review-evidence-pilot-review", reviews_index)
            self.assertIn("landed review-evidence pilot review: landed", ingress)
            self.assertIn("execution/runtime-truth-lifecycle", ingress)
            self.assertIn("Landed review-evidence pilot review", landing_log)
            self.assertIn(
                "landed `review-evidence` review is now complete",
                distillation_roadmap,
            )
            self.assertIn(
                "Review the landed `execution/runtime-truth-lifecycle` pilot",
                root_roadmap,
            )
            self.assertIn("Landed Review-Evidence Pilot Review", tree_contract)
            self.assertIn(
                "execution/runtime-truth-lifecycle",
                tree_contract,
            )
            self.assertIn(
                "accepted the landed `review-evidence` pilot review",
                changelog,
            )

            for technique_id, current_path, future_path in (
                (
                    "AOA-T-0036",
                    "techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md",
                    "techniques/execution/runtime-truth-lifecycle/render-truth-before-startup/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0038",
                    "techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md",
                    "techniques/execution/runtime-truth-lifecycle/one-command-service-lifecycle/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0037",
                    "techniques/evaluation/contextual-host-doctor/TECHNIQUE.md",
                    "techniques/execution/runtime-truth-lifecycle/contextual-host-doctor/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0039",
                    "techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md",
                    "techniques/execution/runtime-truth-lifecycle/baseline-first-additive-profile-benchmarks/TECHNIQUE.md",
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)
                    self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                    self.assertIn(future_path.rsplit("/", 1)[0] + "/", review)
                    self.assertFalse((REPO_ROOT / current_path).exists())
                    self.assertTrue((REPO_ROOT / future_path).is_file())

    def test_runtime_truth_lifecycle_direct_read_review_accepts_twenty_third_pilot(
            self,
        ) -> None:
            review = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "runtime-truth-lifecycle-direct-read-migration-review.md"
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

            self.assertIn("Runtime-Truth-Lifecycle Direct-Read Migration Review", review)
            self.assertIn("accepted-for-twenty-third-migration-pilot", review)
            self.assertIn("Accept `execution/runtime-truth-lifecycle`", review)
            self.assertIn("Do not move files from this review pack alone", review)
            self.assertIn("abyss-stack` runtime law", review)
            self.assertIn("benchmark-suite governance", review)
            self.assertIn("Run the twenty-third migration pilot", review)
            self.assertIn(
                "runtime-truth-lifecycle-direct-read-migration-review",
                reviews_index,
            )
            self.assertIn(
                "runtime-truth-lifecycle direct-read review: landed",
                ingress,
            )
            self.assertIn(
                "accepted-for-twenty-third-migration-pilot",
                ingress,
            )
            self.assertIn(
                "Runtime-truth-lifecycle direct-read migration review",
                landing_log,
            )
            self.assertIn(
                "`runtime-truth-lifecycle`\n   direct-read review is now landed",
                distillation_roadmap,
            )
            self.assertIn(
                "Review the landed `execution/runtime-truth-lifecycle` pilot",
                root_roadmap,
            )
            self.assertIn(
                "Runtime-Truth-Lifecycle Direct-Read Migration Review",
                tree_contract,
            )
            self.assertIn(
                "twenty-third pilot migration moves exactly those four bundles",
                tree_contract,
            )
            self.assertIn(
                "accepted the `runtime-truth-lifecycle` direct-read migration review",
                changelog,
            )

            for technique_id, current_path, future_path in (
                (
                    "AOA-T-0036",
                    "techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md",
                    "techniques/execution/runtime-truth-lifecycle/render-truth-before-startup/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0038",
                    "techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md",
                    "techniques/execution/runtime-truth-lifecycle/one-command-service-lifecycle/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0037",
                    "techniques/evaluation/contextual-host-doctor/TECHNIQUE.md",
                    "techniques/execution/runtime-truth-lifecycle/contextual-host-doctor/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0039",
                    "techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md",
                    "techniques/execution/runtime-truth-lifecycle/baseline-first-additive-profile-benchmarks/TECHNIQUE.md",
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)
                    self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                    self.assertIn(future_path.rsplit("/", 1)[0] + "/", review)
                    self.assertFalse((REPO_ROOT / current_path).exists())
                    self.assertTrue((REPO_ROOT / future_path).is_file())

    def test_runtime_truth_lifecycle_tree_pilot_migration_landed(self) -> None:
            receipt = (
                REPO_ROOT
                / "legacy"
                / "receipts"
                / "2026-05-05-runtime-truth-lifecycle-tree-pilot.md"
            ).read_text(encoding="utf-8")
            execution_agents = (
                REPO_ROOT / "techniques" / "execution" / "AGENTS.md"
            ).read_text(encoding="utf-8")
            agent_workflows_agents = (
                REPO_ROOT / "techniques" / "agent-workflows" / "AGENTS.md"
            ).read_text(encoding="utf-8")
            tool_use_agents = (
                REPO_ROOT / "techniques" / "tool-use" / "AGENTS.md"
            ).read_text(encoding="utf-8")
            evaluation_agents = (
                REPO_ROOT / "techniques" / "evaluation" / "AGENTS.md"
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

            self.assertIn("Runtime-Truth-Lifecycle Tree Pilot Receipt", receipt)
            self.assertIn("Twenty-third authored path migration", receipt)
            self.assertIn("`kind` stayed unchanged as `composition`", receipt)
            self.assertIn("`kind` stayed unchanged as `workflow`", receipt)
            self.assertIn("`kind` stayed unchanged as `validation`", receipt)
            self.assertIn("runtime-truth-lifecycle/", execution_agents)
            self.assertIn("benchmark-suite governance", execution_agents)
            self.assertNotIn("render-truth-before-startup", agent_workflows_agents)
            self.assertNotIn("one-command-service-lifecycle", agent_workflows_agents)
            self.assertIn("No active leaf bundles currently live directly here", evaluation_agents)
            self.assertIn("runtime-truth-lifecycle migration: landed", ingress)
            self.assertIn("Runtime-truth-lifecycle tree pilot migration", landing_log)
            self.assertIn(
                "2026-05-05-runtime-truth-lifecycle-tree-pilot",
                landing_log,
            )
            self.assertIn(
                "twenty-third pilot\n   migration is now landed",
                distillation_roadmap,
            )
            self.assertIn(
                "Review the landed `execution/runtime-truth-lifecycle` pilot",
                root_roadmap,
            )
            self.assertIn(
                "2026-05-05-runtime-truth-lifecycle-tree-pilot",
                tree_contract,
            )
            self.assertIn("twenty-eight receipts", legacy_index)
            self.assertIn(
                "2026-05-05-runtime-truth-lifecycle-tree-pilot.md",
                legacy_index,
            )
            self.assertIn("twenty-eight technique tree pilot receipts", receipts_index)
            self.assertIn("moved `AOA-T-0036`", changelog)

            for technique_id, old_path, new_path in (
                (
                    "AOA-T-0036",
                    "techniques/agent-workflows/render-truth-before-startup/",
                    "techniques/execution/runtime-truth-lifecycle/render-truth-before-startup/",
                ),
                (
                    "AOA-T-0038",
                    "techniques/agent-workflows/one-command-service-lifecycle/",
                    "techniques/execution/runtime-truth-lifecycle/one-command-service-lifecycle/",
                ),
                (
                    "AOA-T-0037",
                    "techniques/evaluation/contextual-host-doctor/",
                    "techniques/execution/runtime-truth-lifecycle/contextual-host-doctor/",
                ),
                (
                    "AOA-T-0039",
                    "techniques/evaluation/baseline-first-additive-profile-benchmarks/",
                    "techniques/execution/runtime-truth-lifecycle/baseline-first-additive-profile-benchmarks/",
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, receipt)
                    self.assertIn(old_path, receipt)
                    self.assertIn(new_path, receipt)
                    self.assertFalse((REPO_ROOT / old_path).exists())
                    self.assertTrue((REPO_ROOT / new_path / "TECHNIQUE.md").is_file())

    def test_landed_runtime_truth_lifecycle_pilot_review_selects_owner_truth_closeout(
            self,
        ) -> None:
            review = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "landed-runtime-truth-lifecycle-pilot-review.md"
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

            self.assertIn("Landed Runtime-Truth-Lifecycle Pilot Review", review)
            self.assertIn("fourth successful shelf under the `execution` trunk", review)
            self.assertIn("Choose `proof/owner-truth-closeout`", review)
            self.assertIn("Do not move `proof/owner-truth-closeout`", review)
            self.assertIn("root `AGENTS.md` law", review)
            self.assertIn(
                "Run a direct-read migration review for `proof/owner-truth-closeout`",
                review,
            )
            self.assertIn("landed-runtime-truth-lifecycle-pilot-review", reviews_index)
            self.assertIn(
                "landed runtime-truth-lifecycle pilot review: landed",
                ingress,
            )
            self.assertIn("proof/owner-truth-closeout", ingress)
            self.assertIn("Landed runtime-truth-lifecycle pilot review", landing_log)
            self.assertIn(
                "landed `runtime-truth-lifecycle`\n   pilot review is now complete",
                distillation_roadmap,
            )
            self.assertIn(
                "Run the `proof/owner-truth-closeout` direct-read migration review",
                root_roadmap,
            )
            self.assertIn(
                "Landed Runtime-Truth-Lifecycle Pilot Review",
                tree_contract,
            )
            self.assertIn("proof/owner-truth-closeout", tree_contract)
            self.assertIn(
                "accepted the landed `runtime-truth-lifecycle` pilot review",
                changelog,
            )

            for technique_id, current_path, future_path in (
                (
                    "AOA-T-0091",
                    "techniques/agent-workflows/workspace-root-ingress-and-mutation-gate/TECHNIQUE.md",
                    "techniques/proof/owner-truth-closeout/workspace-root-ingress-and-mutation-gate/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0092",
                    "techniques/agent-workflows/audit-to-closeout-proof-loop/TECHNIQUE.md",
                    "techniques/proof/owner-truth-closeout/audit-to-closeout-proof-loop/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0095",
                    "techniques/agent-workflows/github-only-owner-endcap-with-reality-sync/TECHNIQUE.md",
                    "techniques/proof/owner-truth-closeout/github-only-owner-endcap-with-reality-sync/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0096",
                    "techniques/agent-workflows/pinned-validation-matrix-before-generated-publish/TECHNIQUE.md",
                    "techniques/proof/owner-truth-closeout/pinned-validation-matrix-before-generated-publish/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0094",
                    "techniques/docs/canonical-owner-with-validated-mirror/TECHNIQUE.md",
                    "techniques/proof/owner-truth-closeout/canonical-owner-with-validated-mirror/TECHNIQUE.md",
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)
                    self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                    self.assertIn(future_path.rsplit("/", 1)[0] + "/", review)
                    self.assertFalse((REPO_ROOT / current_path).exists())
                    self.assertTrue((REPO_ROOT / future_path).is_file())

    def test_owner_truth_closeout_direct_read_review_accepts_twenty_fourth_pilot(
            self,
        ) -> None:
            review = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "owner-truth-closeout-direct-read-migration-review.md"
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

            self.assertIn("Owner-Truth-Closeout Direct-Read Migration Review", review)
            self.assertIn("accepted-for-twenty-fourth-migration-pilot", review)
            self.assertIn("Accept `proof/owner-truth-closeout`", review)
            self.assertIn("Do not move files from this review pack alone", review)
            self.assertIn("root `AGENTS.md` law", review)
            self.assertIn("public-share approval policy", review)
            self.assertIn("Run the twenty-fourth migration pilot", review)
            self.assertIn(
                "owner-truth-closeout-direct-read-migration-review",
                reviews_index,
            )
            self.assertIn("owner-truth-closeout direct-read review: landed", ingress)
            self.assertIn("accepted-for-twenty-fourth-migration-pilot", ingress)
            self.assertIn(
                "Owner-truth-closeout direct-read migration review",
                landing_log,
            )
            self.assertIn(
                "The owner-truth-closeout direct-read review is now\n   landed",
                distillation_roadmap,
            )
            self.assertIn(
                "Migrate exactly `AOA-T-0091`, `AOA-T-0092`, `AOA-T-0095`, "
                "`AOA-T-0096`, and `AOA-T-0094` into "
                "`techniques/proof/owner-truth-closeout/`",
                root_roadmap,
            )
            self.assertIn(
                "Owner-Truth-Closeout Direct-Read Migration Review",
                tree_contract,
            )
            self.assertIn(
                "twenty-fourth pilot migration moves exactly those five bundles",
                tree_contract,
            )
            self.assertIn(
                "accepted the `owner-truth-closeout` direct-read migration review",
                changelog,
            )

            for technique_id, current_path, future_path in (
                (
                    "AOA-T-0091",
                    "techniques/agent-workflows/workspace-root-ingress-and-mutation-gate/TECHNIQUE.md",
                    "techniques/proof/owner-truth-closeout/workspace-root-ingress-and-mutation-gate/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0092",
                    "techniques/agent-workflows/audit-to-closeout-proof-loop/TECHNIQUE.md",
                    "techniques/proof/owner-truth-closeout/audit-to-closeout-proof-loop/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0095",
                    "techniques/agent-workflows/github-only-owner-endcap-with-reality-sync/TECHNIQUE.md",
                    "techniques/proof/owner-truth-closeout/github-only-owner-endcap-with-reality-sync/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0096",
                    "techniques/agent-workflows/pinned-validation-matrix-before-generated-publish/TECHNIQUE.md",
                    "techniques/proof/owner-truth-closeout/pinned-validation-matrix-before-generated-publish/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0094",
                    "techniques/docs/canonical-owner-with-validated-mirror/TECHNIQUE.md",
                    "techniques/proof/owner-truth-closeout/canonical-owner-with-validated-mirror/TECHNIQUE.md",
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)
                    self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                    self.assertIn(future_path.rsplit("/", 1)[0] + "/", review)
                    self.assertFalse((REPO_ROOT / current_path).exists())
                    self.assertTrue((REPO_ROOT / future_path).is_file())

    def test_owner_truth_closeout_tree_pilot_migration_landed(self) -> None:
            receipt = (
                REPO_ROOT
                / "legacy"
                / "receipts"
                / "2026-05-05-owner-truth-closeout-tree-pilot.md"
            ).read_text(encoding="utf-8")
            proof_agents = (REPO_ROOT / "techniques" / "proof" / "AGENTS.md").read_text(
                encoding="utf-8"
            )
            agent_workflows_agents = (
                REPO_ROOT / "techniques" / "agent-workflows" / "AGENTS.md"
            ).read_text(encoding="utf-8")
            docs_agents = (REPO_ROOT / "techniques" / "docs" / "AGENTS.md").read_text(
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
            legacy_index = (REPO_ROOT / "legacy" / "INDEX.md").read_text(
                encoding="utf-8"
            )
            receipts_index = (
                REPO_ROOT / "legacy" / "receipts" / "README.md"
            ).read_text(encoding="utf-8")
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Owner-Truth-Closeout Tree Pilot Receipt", receipt)
            self.assertIn("Twenty-fourth authored path migration", receipt)
            self.assertIn("`domain` stayed unchanged as `agent-workflows`", receipt)
            self.assertIn("`domain` stayed unchanged as `docs`", receipt)
            self.assertIn("`kind` stayed unchanged as `guardrail`", receipt)
            self.assertIn("`kind` stayed unchanged as `workflow`", receipt)
            self.assertIn("`kind` stayed unchanged as `validation`", receipt)
            self.assertIn("`kind` stayed unchanged as `distribution`", receipt)
            self.assertIn("owner-truth-closeout/", proof_agents)
            self.assertIn("public-share approval policy", proof_agents)
            self.assertNotIn("workspace-root-ingress-and-mutation-gate", agent_workflows_agents)
            self.assertIn("No active leaf bundles currently live directly here", docs_agents)
            self.assertIn("owner-truth-closeout migration: landed", ingress)
            self.assertIn("Owner-truth-closeout tree pilot migration", landing_log)
            self.assertIn(
                "2026-05-05-owner-truth-closeout-tree-pilot",
                landing_log,
            )
            self.assertIn(
                "twenty-fourth\n   pilot migration is now landed",
                distillation_roadmap,
            )
            self.assertIn(
                "Review the landed `proof/owner-truth-closeout` pilot",
                root_roadmap,
            )
            self.assertIn(
                "2026-05-05-owner-truth-closeout-tree-pilot",
                tree_contract,
            )
            self.assertIn("twenty-eight receipts", legacy_index)
            self.assertIn(
                "2026-05-05-owner-truth-closeout-tree-pilot.md",
                legacy_index,
            )
            self.assertIn("twenty-eight technique tree pilot receipts", receipts_index)
            self.assertIn("moved `AOA-T-0091`", changelog)

            for technique_id, old_path, new_path in (
                (
                    "AOA-T-0091",
                    "techniques/agent-workflows/workspace-root-ingress-and-mutation-gate/",
                    "techniques/proof/owner-truth-closeout/workspace-root-ingress-and-mutation-gate/",
                ),
                (
                    "AOA-T-0092",
                    "techniques/agent-workflows/audit-to-closeout-proof-loop/",
                    "techniques/proof/owner-truth-closeout/audit-to-closeout-proof-loop/",
                ),
                (
                    "AOA-T-0095",
                    "techniques/agent-workflows/github-only-owner-endcap-with-reality-sync/",
                    "techniques/proof/owner-truth-closeout/github-only-owner-endcap-with-reality-sync/",
                ),
                (
                    "AOA-T-0096",
                    "techniques/agent-workflows/pinned-validation-matrix-before-generated-publish/",
                    "techniques/proof/owner-truth-closeout/pinned-validation-matrix-before-generated-publish/",
                ),
                (
                    "AOA-T-0094",
                    "techniques/docs/canonical-owner-with-validated-mirror/",
                    "techniques/proof/owner-truth-closeout/canonical-owner-with-validated-mirror/",
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, receipt)
                    self.assertIn(old_path, receipt)
                    self.assertIn(new_path, receipt)
                    self.assertFalse((REPO_ROOT / old_path).exists())
                    self.assertTrue((REPO_ROOT / new_path / "TECHNIQUE.md").is_file())

    def test_landed_owner_truth_closeout_pilot_review_selects_automation_governance(
            self,
        ) -> None:
            review = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "landed-owner-truth-closeout-pilot-review.md"
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

            self.assertIn("Landed Owner-Truth-Closeout Pilot Review", review)
            self.assertIn("fifth successful shelf under the `proof` trunk", review)
            self.assertIn("Choose `governance/automation-governance`", review)
            self.assertIn("direct-read split review", review)
            self.assertIn("Do not move `governance/automation-governance`", review)
            self.assertIn("split-review-needed", review)
            self.assertIn("skill acceptance", review)
            self.assertIn(
                "Run a direct-read split review for `governance/automation-governance`",
                review,
            )
            self.assertIn(
                "landed-owner-truth-closeout-pilot-review",
                reviews_index,
            )
            self.assertIn(
                "landed owner-truth-closeout pilot review: landed",
                ingress,
            )
            self.assertIn("governance/automation-governance", ingress)
            self.assertIn("Landed owner-truth-closeout pilot review", landing_log)
            self.assertIn(
                "landed `owner-truth-closeout` pilot\n   review is now complete",
                distillation_roadmap,
            )
            self.assertIn(
                "Run the `governance/automation-governance` direct-read split review",
                root_roadmap,
            )
            self.assertIn(
                "Owner-Truth-Closeout Pilot Review",
                tree_contract,
            )
            self.assertIn(
                "nine\nprojected automation-governance leaves",
                tree_contract,
            )
            self.assertIn(
                "accepted the landed `owner-truth-closeout` pilot review",
                changelog,
            )

            for technique_id, current_path, future_path, current_exists, future_exists in (
                (
                    "AOA-T-0086",
                    "techniques/agent-workflows/automation-fit-matrix/TECHNIQUE.md",
                    "techniques/governance/automation-governance/automation-fit-matrix/TECHNIQUE.md",
                    False,
                    False,
                ),
                (
                    "AOA-T-0087",
                    "techniques/agent-workflows/human-loop-to-first-landing/TECHNIQUE.md",
                    "techniques/governance/automation-governance/human-loop-to-first-landing/TECHNIQUE.md",
                    False,
                    False,
                ),
                (
                    "AOA-T-0088",
                    "techniques/agent-workflows/approval-sensitivity-check/TECHNIQUE.md",
                    "techniques/governance/automation-governance/approval-sensitivity-check/TECHNIQUE.md",
                    False,
                    False,
                ),
                (
                    "AOA-T-0089",
                    "techniques/agent-workflows/quest-unit-promotion-review/TECHNIQUE.md",
                    "techniques/governance/automation-governance/quest-unit-promotion-review/TECHNIQUE.md",
                    False,
                    False,
                ),
                (
                    "AOA-T-0090",
                    "techniques/agent-workflows/nearest-wrong-target-rejection/TECHNIQUE.md",
                    "techniques/governance/automation-governance/nearest-wrong-target-rejection/TECHNIQUE.md",
                    False,
                    False,
                ),
                (
                    "AOA-T-0101",
                    "techniques/agent-workflows/local-pattern-adoption-gate/TECHNIQUE.md",
                    "techniques/governance/automation-governance/local-pattern-adoption-gate/TECHNIQUE.md",
                    False,
                    False,
                ),
                (
                    "AOA-T-0102",
                    "techniques/agent-workflows/skill-proposal-handoff-packet/TECHNIQUE.md",
                    "techniques/governance/automation-governance/skill-proposal-handoff-packet/TECHNIQUE.md",
                    False,
                    False,
                ),
                (
                    "AOA-T-0103",
                    "techniques/agent-workflows/adopted-practice-retention-review/TECHNIQUE.md",
                    "techniques/governance/automation-governance/adopted-practice-retention-review/TECHNIQUE.md",
                    False,
                    False,
                ),
                (
                    "AOA-T-0104",
                    "techniques/agent-workflows/superseded-practice-obsolescence-route/TECHNIQUE.md",
                    "techniques/governance/automation-governance/superseded-practice-obsolescence-route/TECHNIQUE.md",
                    False,
                    False,
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)
                    self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                    self.assertIn(future_path.rsplit("/", 1)[0] + "/", review)
                    self.assertEqual(current_exists, (REPO_ROOT / current_path).is_file())
                    self.assertEqual(future_exists, (REPO_ROOT / future_path).is_file())


if __name__ == "__main__":
    unittest.main()
