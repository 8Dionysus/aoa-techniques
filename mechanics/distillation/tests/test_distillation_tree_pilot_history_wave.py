from __future__ import annotations

import sys
import unittest
from pathlib import Path


SUPPORT_DIR = Path(__file__).resolve().parent / "support"
if str(SUPPORT_DIR) not in sys.path:
    sys.path.insert(0, str(SUPPORT_DIR))

from distillation_topology_fixtures import *  # noqa: F403


class DistillationTreePilotHistoryWaveTests(unittest.TestCase):
    def test_published_summary_direct_read_review_accepts_thirteenth_pilot(
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
                / "published-summary-direct-read-migration-review.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Published-Summary Direct-Read Migration Review", review)
            self.assertIn("accepted-for-thirteenth-migration-pilot", review)
            self.assertIn("not path migration", review)
            self.assertIn("not\n`tree_path` frontmatter", review)
            self.assertIn("Accept `published-summary` as the thirteenth", review)
            self.assertIn("Direct Bundle Read", review)
            self.assertIn("Why The Shelf Holds", review)
            self.assertIn("Proof Trunk Fit", review)
            self.assertIn("Boundary Watch Accepted", review)
            for technique_id in (
                "AOA-T-0006",
                "AOA-T-0008",
                "AOA-T-0010",
                "AOA-T-0011",
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)

            for old_path in (
                "techniques/evaluation/latest-alias-plus-history-copy/",
                "techniques/evaluation/published-summary-remediation-snapshot/",
                "techniques/evaluation/telemetry-integrity-snapshot/",
                "techniques/evaluation/required-vs-optional-source-rendering/",
            ):
                with self.subTest(old_path=old_path):
                    self.assertIn(old_path, review)

            self.assertIn("techniques/proof/published-summary/", review)
            self.assertIn("Move exactly these four bundles", review)
            self.assertIn("Do not move files from this review pack alone", review)
            self.assertIn("Do not add `tree_path`", review)
            self.assertIn("Do not treat `published-summary` as telemetry owner doctrine", review)
            self.assertIn("Do not let `AOA-T-0011` become only a package appendix", review)
            self.assertIn("Run the thirteenth pilot migration", review)
            self.assertIn("published-summary-direct-read-migration-review", reviews_index)
            self.assertIn("published-summary direct-read review: landed", ingress)
            self.assertIn("accepted-for-thirteenth-migration-pilot", ingress)
            self.assertIn("Published-summary direct-read migration review", landing_log)
            self.assertIn("proof-facing package", landing_log)
            self.assertIn("accepted-for-thirteenth-migration-pilot", distillation_roadmap)
            self.assertIn("published-summary` pilot before choosing", root_roadmap)
            self.assertIn("Published-Summary Direct-Read Migration Review", tree_contract)
            self.assertIn("AOA-T-0006`, `AOA-T-0008`, `AOA-T-0010`, and `AOA-T-0011", tree_contract)
            self.assertIn(
                "accepted the `published-summary` direct-read migration review",
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
                with self.subTest(current_path=current_path):
                    self.assertFalse((REPO_ROOT / old_path).exists())
                    self.assertTrue((REPO_ROOT / current_path).is_file())

            self.assertTrue((REPO_ROOT / "techniques" / "proof" / "published-summary").is_dir())

    def test_landed_published_summary_review_selects_history_artifacts(self) -> None:
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
                / "landed-published-summary-pilot-review.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Landed Published-Summary Pilot Review", review)
            self.assertIn("pilot-validated", review)
            self.assertIn("third successful shelf under the `proof` trunk", review)
            self.assertIn("What The Thirteenth Pilot Proved", review)
            self.assertIn("Remaining Weaknesses", review)
            self.assertIn("Fourteenth Shelf Choice", review)
            self.assertIn("Choose `history-artifacts`", review)
            for technique_id in (
                "AOA-T-0006",
                "AOA-T-0008",
                "AOA-T-0010",
                "AOA-T-0011",
                "AOA-T-0044",
                "AOA-T-0053",
                "AOA-T-0026",
                "AOA-T-0045",
                "AOA-T-0066",
                "AOA-T-0067",
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)

            self.assertIn("techniques/proof/published-summary/", review)
            self.assertIn("Do not move `history-artifacts` from this review alone", review)
            self.assertIn("Do not add `tree_path`", review)
            self.assertIn("Do not treat `history-artifacts` as memory doctrine", review)
            self.assertIn("private transcript publication", review)
            self.assertIn("repo\n  analytics", review)
            self.assertIn("Run a direct-read migration review for `history-artifacts`", review)
            self.assertIn("landed-published-summary-pilot-review", reviews_index)
            self.assertIn("landed published-summary pilot review: landed", ingress)
            self.assertIn("history-artifacts` chosen", ingress)
            self.assertIn("Landed published-summary pilot review", landing_log)
            self.assertIn("third successful proof trunk shelf", landing_log)
            self.assertIn("history-artifacts` direct-read review", distillation_roadmap)
            self.assertIn("published-summary` pilot before choosing", root_roadmap)
            self.assertIn("Run the `history-artifacts` direct-read migration review", root_roadmap)
            self.assertIn("Landed Published-Summary Pilot Review", tree_contract)
            self.assertIn("chooses `history-artifacts`", tree_contract)
            self.assertIn(
                "accepted the landed `published-summary` pilot review",
                changelog,
            )

            for old_path, current_path in (
                (
                    "techniques/history/versionable-session-transcripts/TECHNIQUE.md",
                    "techniques/history/history-artifacts/versionable-session-transcripts/TECHNIQUE.md",
                ),
                (
                    "techniques/history/local-first-session-index/TECHNIQUE.md",
                    "techniques/history/history-artifacts/local-first-session-index/TECHNIQUE.md",
                ),
                (
                    "techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md",
                    "techniques/history/history-artifacts/session-capture-as-repo-artifact/TECHNIQUE.md",
                ),
                (
                    "techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md",
                    "techniques/history/history-artifacts/witness-trace-as-reviewable-artifact/TECHNIQUE.md",
                ),
                (
                    "techniques/history/transcript-replay-artifact/TECHNIQUE.md",
                    "techniques/history/history-artifacts/transcript-replay-artifact/TECHNIQUE.md",
                ),
                (
                    "techniques/history/transcript-linked-code-lineage/TECHNIQUE.md",
                    "techniques/history/history-artifacts/transcript-linked-code-lineage/TECHNIQUE.md",
                ),
            ):
                with self.subTest(current_path=current_path):
                    self.assertFalse((REPO_ROOT / old_path).exists())
                    self.assertTrue((REPO_ROOT / current_path).is_file())

            self.assertTrue((REPO_ROOT / "techniques" / "history" / "history-artifacts").is_dir())

    def test_history_artifacts_direct_read_review_accepts_fourteenth_pilot(
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
                / "history-artifacts-direct-read-migration-review.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("History-Artifacts Direct-Read Migration Review", review)
            self.assertIn("accepted-for-fourteenth-migration-pilot", review)
            self.assertIn("not path migration", review)
            self.assertIn("not\n`tree_path` frontmatter", review)
            self.assertIn("Accept `history-artifacts` as the fourteenth", review)
            self.assertIn("Direct Bundle Read", review)
            self.assertIn("Why The Shelf Holds", review)
            self.assertIn("Split Decision", review)
            self.assertIn("History Trunk Fit", review)
            self.assertIn("Boundary Watch Accepted", review)
            self.assertIn("Proposed Move", review)
            for technique_id in (
                "AOA-T-0044",
                "AOA-T-0053",
                "AOA-T-0026",
                "AOA-T-0045",
                "AOA-T-0066",
                "AOA-T-0067",
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)

            for current_path in (
                "techniques/history/versionable-session-transcripts/",
                "techniques/history/local-first-session-index/",
                "techniques/history/session-capture-as-repo-artifact/",
                "techniques/history/witness-trace-as-reviewable-artifact/",
                "techniques/history/transcript-replay-artifact/",
                "techniques/history/transcript-linked-code-lineage/",
            ):
                with self.subTest(current_path=current_path):
                    self.assertIn(current_path, review)

            self.assertIn("techniques/history/history-artifacts/", review)
            self.assertIn("Move exactly these six bundles", review)
            self.assertIn("Do not move files from this review pack alone", review)
            self.assertIn("Do not add `tree_path`", review)
            self.assertIn("Do not treat `history-artifacts` as memory doctrine", review)
            self.assertIn("hidden capture policy", review)
            self.assertIn("repo analytics", review)
            self.assertIn("Run the fourteenth pilot migration", review)
            self.assertIn("history-artifacts-direct-read-migration-review", reviews_index)
            self.assertIn("history-artifacts direct-read review: landed", ingress)
            self.assertIn("accepted-for-fourteenth-migration-pilot", ingress)
            self.assertIn("History-artifacts direct-read migration review", landing_log)
            self.assertIn("fourteenth bounded migration pilot", landing_log)
            self.assertIn("accepted-for-fourteenth-migration-pilot", distillation_roadmap)
            self.assertIn(
                "Run the `history-artifacts` direct-read migration review",
                root_roadmap,
            )
            self.assertIn("Review the landed `history-artifacts` pilot", root_roadmap)
            self.assertIn("History-Artifacts Direct-Read Migration Review", tree_contract)
            self.assertIn(
                "fourteenth pilot migration moves exactly those six bundles",
                tree_contract,
            )
            self.assertIn(
                "accepted the `history-artifacts` direct-read migration review",
                changelog,
            )

            for current_path, future_path in (
                (
                    "techniques/history/versionable-session-transcripts/TECHNIQUE.md",
                    "techniques/history/history-artifacts/versionable-session-transcripts/TECHNIQUE.md",
                ),
                (
                    "techniques/history/local-first-session-index/TECHNIQUE.md",
                    "techniques/history/history-artifacts/local-first-session-index/TECHNIQUE.md",
                ),
                (
                    "techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md",
                    "techniques/history/history-artifacts/session-capture-as-repo-artifact/TECHNIQUE.md",
                ),
                (
                    "techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md",
                    "techniques/history/history-artifacts/witness-trace-as-reviewable-artifact/TECHNIQUE.md",
                ),
                (
                    "techniques/history/transcript-replay-artifact/TECHNIQUE.md",
                    "techniques/history/history-artifacts/transcript-replay-artifact/TECHNIQUE.md",
                ),
                (
                    "techniques/history/transcript-linked-code-lineage/TECHNIQUE.md",
                    "techniques/history/history-artifacts/transcript-linked-code-lineage/TECHNIQUE.md",
                ),
            ):
                with self.subTest(current_path=current_path):
                    self.assertFalse((REPO_ROOT / current_path).exists())
                    self.assertTrue((REPO_ROOT / future_path).is_file())

            self.assertTrue((REPO_ROOT / "techniques" / "history" / "history-artifacts").is_dir())

    def test_history_artifacts_tree_pilot_migration_is_recorded(self) -> None:
            history_agents = (
                REPO_ROOT / "techniques" / "history" / "AGENTS.md"
            ).read_text(encoding="utf-8")
            ingress = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "README.md"
            ).read_text(encoding="utf-8")
            receipt = (
                REPO_ROOT
                / "legacy"
                / "receipts"
                / "2026-05-05-history-artifacts-tree-pilot.md"
            ).read_text(encoding="utf-8")
            legacy_index = (REPO_ROOT / "legacy" / "INDEX.md").read_text(
                encoding="utf-8"
            )
            receipts_index = (
                REPO_ROOT / "legacy" / "receipts" / "README.md"
            ).read_text(encoding="utf-8")
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            flat_history_distillation_roadmap = " ".join(distillation_roadmap.split())
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("history-artifacts/", history_agents)
            self.assertIn("memory objects and recall surfaces still stay outside", history_agents)
            self.assertIn("private transcripts", history_agents)
            self.assertIn("transcript-linked-code-lineage", history_agents)
            self.assertIn("history-artifacts migration: landed", ingress)
            self.assertIn("History-Artifacts Tree Pilot Receipt", receipt)
            self.assertIn("They did not pass through root `legacy/`.", receipt)
            self.assertIn("Do not add `tree_path` frontmatter.", receipt)
            self.assertIn("six separate leaf", receipt)
            self.assertIn("generic history platform", receipt)
            self.assertIn("twenty-eight receipts", legacy_index)
            self.assertIn("2026-05-05-history-artifacts-tree-pilot.md", legacy_index)
            self.assertIn("twenty-eight technique tree pilot receipts", receipts_index)
            self.assertIn("History-artifacts tree pilot migration", landing_log)
            self.assertIn("kept capture, transcript packaging", landing_log)
            self.assertIn(
                "fourteenth pilot migration is now landed",
                flat_history_distillation_roadmap,
            )
            self.assertIn("fourteenth landed pilot moved", root_roadmap)
            self.assertIn("Review the landed `history-artifacts` pilot", root_roadmap)
            self.assertIn("2026-05-05-history-artifacts-tree-pilot", tree_contract)
            self.assertIn("moved `AOA-T-0044`", changelog)

            for technique_id, old_path, new_path in (
                (
                    "AOA-T-0044",
                    "techniques/history/versionable-session-transcripts/",
                    "techniques/history/history-artifacts/versionable-session-transcripts/",
                ),
                (
                    "AOA-T-0053",
                    "techniques/history/local-first-session-index/",
                    "techniques/history/history-artifacts/local-first-session-index/",
                ),
                (
                    "AOA-T-0026",
                    "techniques/history/session-capture-as-repo-artifact/",
                    "techniques/history/history-artifacts/session-capture-as-repo-artifact/",
                ),
                (
                    "AOA-T-0045",
                    "techniques/history/witness-trace-as-reviewable-artifact/",
                    "techniques/history/history-artifacts/witness-trace-as-reviewable-artifact/",
                ),
                (
                    "AOA-T-0066",
                    "techniques/history/transcript-replay-artifact/",
                    "techniques/history/history-artifacts/transcript-replay-artifact/",
                ),
                (
                    "AOA-T-0067",
                    "techniques/history/transcript-linked-code-lineage/",
                    "techniques/history/history-artifacts/transcript-linked-code-lineage/",
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, receipt)
                    self.assertIn(old_path, receipt)
                    self.assertIn(new_path, receipt)
                    self.assertFalse((REPO_ROOT / old_path).exists())
                    self.assertTrue(
                        (REPO_ROOT / new_path / "TECHNIQUE.md").is_file()
                    )

    def test_landed_history_artifacts_review_selects_antifragility_recovery(
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
                / "landed-history-artifacts-pilot-review.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Landed History-Artifacts Pilot Review", review)
            self.assertIn("pilot-validated", review)
            self.assertIn("first successful shelf under the `history` trunk", review)
            self.assertIn("What The Fourteenth Pilot Proved", review)
            self.assertIn("Remaining Weaknesses", review)
            self.assertIn("Fifteenth Shelf Choice", review)
            self.assertIn("Choose `recovery/antifragility-recovery`", review)

            for technique_id in (
                "AOA-T-0044",
                "AOA-T-0053",
                "AOA-T-0026",
                "AOA-T-0045",
                "AOA-T-0066",
                "AOA-T-0067",
                "AOA-T-0097",
                "AOA-T-0099",
                "AOA-T-0100",
                "AOA-T-0098",
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)

            self.assertIn("techniques/history/history-artifacts/", review)
            self.assertIn(
                "Do not move `recovery/antifragility-recovery` from this review alone",
                review,
            )
            self.assertIn("Do not add `tree_path`", review)
            self.assertIn("Do not treat `history-artifacts` as memory doctrine", review)
            self.assertIn(
                "Do not treat `recovery/antifragility-recovery` as incident response",
                review,
            )
            self.assertIn("validation-patterns erasure", review)
            self.assertIn(
                "Run a direct-read migration review for `recovery/antifragility-recovery`",
                review,
            )
            self.assertIn("landed-history-artifacts-pilot-review", reviews_index)
            self.assertIn("landed history-artifacts pilot review: landed", ingress)
            self.assertIn("recovery/antifragility-recovery` chosen", ingress)
            self.assertIn("Landed history-artifacts pilot review", landing_log)
            self.assertIn("first successful history trunk shelf", landing_log)
            self.assertIn("validation-patterns\n  erasure", landing_log)
            self.assertIn(
                "recovery/antifragility-recovery` for the next direct-read",
                distillation_roadmap,
            )
            self.assertIn(
                "history-artifacts` pilot before choosing any fifteenth shelf",
                root_roadmap,
            )
            self.assertIn(
                "Run the `recovery/antifragility-recovery` direct-read migration review",
                root_roadmap,
            )
            self.assertIn("Landed History-Artifacts Pilot Review", tree_contract)
            self.assertIn("chooses\n`recovery/antifragility-recovery`", tree_contract)
            self.assertIn(
                "accepted the landed `history-artifacts` pilot review",
                changelog,
            )

            for current_path, future_path in (
                (
                    "techniques/system-recovery/degrade-reground-recover/TECHNIQUE.md",
                    "techniques/recovery/antifragility-recovery/degrade-reground-recover/TECHNIQUE.md",
                ),
                (
                    "techniques/system-recovery/isolated-service-stop-on-shared-substrate/TECHNIQUE.md",
                    "techniques/recovery/antifragility-recovery/isolated-service-stop-on-shared-substrate/TECHNIQUE.md",
                ),
                (
                    "techniques/system-recovery/stress-receipt-reground-closeout/TECHNIQUE.md",
                    "techniques/recovery/antifragility-recovery/stress-receipt-reground-closeout/TECHNIQUE.md",
                ),
                (
                    "techniques/validation-patterns/receipt-first-failure-analysis/TECHNIQUE.md",
                    "techniques/recovery/antifragility-recovery/receipt-first-failure-analysis/TECHNIQUE.md",
                ),
            ):
                with self.subTest(current_path=current_path):
                    self.assertFalse((REPO_ROOT / current_path).exists())
                    self.assertTrue((REPO_ROOT / future_path).is_file())

            self.assertTrue((REPO_ROOT / "techniques" / "history" / "history-artifacts").is_dir())

    def test_antifragility_recovery_direct_read_review_accepts_fifteenth_pilot(
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
                / "antifragility-recovery-direct-read-migration-review.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Antifragility-Recovery Direct-Read Migration Review", review)
            self.assertIn("accepted-for-fifteenth-migration-pilot", review)
            self.assertIn("not path migration", review)
            self.assertIn("not\n`tree_path` frontmatter", review)
            self.assertIn("Accept `recovery/antifragility-recovery`", review)
            self.assertIn("Direct Bundle Read", review)
            self.assertIn("Why The Shelf Holds", review)
            self.assertIn("Cross-Domain Decision", review)
            self.assertIn("Recovery Trunk Fit", review)
            self.assertIn("Boundary Watch Accepted", review)
            self.assertIn("Proposed Move", review)

            for technique_id in (
                "AOA-T-0097",
                "AOA-T-0099",
                "AOA-T-0100",
                "AOA-T-0098",
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)

            for current_path in (
                "techniques/system-recovery/degrade-reground-recover/",
                "techniques/system-recovery/isolated-service-stop-on-shared-substrate/",
                "techniques/system-recovery/stress-receipt-reground-closeout/",
                "techniques/validation-patterns/receipt-first-failure-analysis/",
            ):
                with self.subTest(current_path=current_path):
                    self.assertIn(current_path, review)

            self.assertIn("techniques/recovery/antifragility-recovery/", review)
            self.assertIn("Move exactly these four bundles", review)
            self.assertIn("Do not move files from this review pack alone", review)
            self.assertIn("Do not add `tree_path`", review)
            self.assertIn("Do not change `domain` or `kind`", review)
            self.assertIn("Do not erase `AOA-T-0098` as a validation pattern", review)
            self.assertIn("Run the fifteenth pilot migration", review)
            self.assertIn(
                "antifragility-recovery-direct-read-migration-review",
                reviews_index,
            )
            self.assertIn("antifragility-recovery direct-read review: landed", ingress)
            self.assertIn("accepted-for-fifteenth-migration-pilot", ingress)
            self.assertIn(
                "Antifragility-recovery direct-read migration review",
                landing_log,
            )
            self.assertIn("validation-shaped leaf", landing_log)
            self.assertIn("accepted-for-fifteenth-migration-pilot", distillation_roadmap)
            self.assertIn("AOA-T-0098` as `domain: validation-patterns`", distillation_roadmap)
            self.assertIn(
                "Run the `recovery/antifragility-recovery` direct-read migration review",
                root_roadmap,
            )
            self.assertIn("accepted exactly `AOA-T-0097`", root_roadmap)
            self.assertIn(
                "Antifragility-Recovery Direct-Read Migration Review",
                tree_contract,
            )
            self.assertIn("preserving `AOA-T-0098`", tree_contract)
            self.assertIn(
                "accepted the `antifragility-recovery` direct-read migration review",
                changelog,
            )

            for current_path, future_path in (
                (
                    "techniques/system-recovery/degrade-reground-recover/TECHNIQUE.md",
                    "techniques/recovery/antifragility-recovery/degrade-reground-recover/TECHNIQUE.md",
                ),
                (
                    "techniques/system-recovery/isolated-service-stop-on-shared-substrate/TECHNIQUE.md",
                    "techniques/recovery/antifragility-recovery/isolated-service-stop-on-shared-substrate/TECHNIQUE.md",
                ),
                (
                    "techniques/system-recovery/stress-receipt-reground-closeout/TECHNIQUE.md",
                    "techniques/recovery/antifragility-recovery/stress-receipt-reground-closeout/TECHNIQUE.md",
                ),
                (
                    "techniques/validation-patterns/receipt-first-failure-analysis/TECHNIQUE.md",
                    "techniques/recovery/antifragility-recovery/receipt-first-failure-analysis/TECHNIQUE.md",
                ),
            ):
                with self.subTest(current_path=current_path):
                    self.assertFalse((REPO_ROOT / current_path).exists())
                    self.assertTrue((REPO_ROOT / future_path).is_file())

    def test_antifragility_recovery_tree_pilot_migration_is_recorded(self) -> None:
            recovery_agents = (
                REPO_ROOT / "techniques" / "recovery" / "AGENTS.md"
            ).read_text(encoding="utf-8")
            ingress = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "README.md"
            ).read_text(encoding="utf-8")
            receipt = (
                REPO_ROOT
                / "legacy"
                / "receipts"
                / "2026-05-05-antifragility-recovery-tree-pilot.md"
            ).read_text(encoding="utf-8")
            legacy_index = (REPO_ROOT / "legacy" / "INDEX.md").read_text(
                encoding="utf-8"
            )
            receipts_index = (
                REPO_ROOT / "legacy" / "receipts" / "README.md"
            ).read_text(encoding="utf-8")
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("antifragility-recovery/", recovery_agents)
            self.assertIn("validation-shaped leaves", recovery_agents)
            self.assertIn("runtime self-healing", recovery_agents)
            self.assertIn("antifragility-recovery migration: landed", ingress)
            self.assertIn("Antifragility-Recovery Tree Pilot Receipt", receipt)
            self.assertIn("They did not pass through root `legacy/`.", receipt)
            self.assertIn("Preserve `AOA-T-0098` as `domain: validation-patterns`", receipt)
            self.assertIn("Do not add `tree_path` frontmatter.", receipt)
            self.assertIn("four separate leaf bundles", receipt)
            self.assertIn("generic resilience platform", receipt)
            self.assertIn("twenty-eight receipts", legacy_index)
            self.assertIn("2026-05-05-antifragility-recovery-tree-pilot.md", legacy_index)
            self.assertIn("twenty-eight technique tree pilot receipts", receipts_index)
            self.assertIn("Antifragility-recovery tree pilot migration", landing_log)
            self.assertIn("preserved `AOA-T-0098`", landing_log)
            self.assertIn("fifteenth pilot migration is now landed", distillation_roadmap)
            self.assertIn("fifteenth landed pilot moved", root_roadmap)
            self.assertIn("Review the landed `antifragility-recovery` pilot", root_roadmap)
            self.assertIn("2026-05-05-antifragility-recovery-tree-pilot", tree_contract)
            self.assertIn("review the landed", tree_contract)
            self.assertIn("`antifragility-recovery` pilot", tree_contract)
            self.assertIn("moved `AOA-T-0097`", changelog)

            for technique_id, old_path, new_path in (
                (
                    "AOA-T-0097",
                    "techniques/system-recovery/degrade-reground-recover/",
                    "techniques/recovery/antifragility-recovery/degrade-reground-recover/",
                ),
                (
                    "AOA-T-0099",
                    "techniques/system-recovery/isolated-service-stop-on-shared-substrate/",
                    "techniques/recovery/antifragility-recovery/isolated-service-stop-on-shared-substrate/",
                ),
                (
                    "AOA-T-0100",
                    "techniques/system-recovery/stress-receipt-reground-closeout/",
                    "techniques/recovery/antifragility-recovery/stress-receipt-reground-closeout/",
                ),
                (
                    "AOA-T-0098",
                    "techniques/validation-patterns/receipt-first-failure-analysis/",
                    "techniques/recovery/antifragility-recovery/receipt-first-failure-analysis/",
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, receipt)
                    self.assertIn(old_path, receipt)
                    self.assertIn(new_path, receipt)
                    self.assertFalse((REPO_ROOT / old_path).exists())
                    self.assertTrue(
                        (REPO_ROOT / new_path / "TECHNIQUE.md").is_file()
                    )

    def test_landed_antifragility_recovery_review_selects_ready_work_graphs(
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
                / "landed-antifragility-recovery-pilot-review.md"
            ).read_text(encoding="utf-8")
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Landed Antifragility-Recovery Pilot Review", review)
            self.assertIn("pilot-validated", review)
            self.assertIn("choose `execution/ready-work-graphs`", review)
            self.assertIn("second successful shelf under the `recovery` trunk", review)
            self.assertIn("AOA-T-0098` remains `domain: validation-patterns`", review)
            self.assertIn("What The Fifteenth Pilot Proved", review)
            self.assertIn("Remaining Weaknesses", review)
            self.assertIn("Sixteenth Shelf Choice", review)
            self.assertIn("Why direct-read first", review)
            self.assertIn("Do not move `execution/ready-work-graphs`", review)
            self.assertIn("do not move any files until that", review)
            self.assertIn("review lands", review)
            self.assertIn("landed-antifragility-recovery-pilot-review", reviews_index)
            self.assertIn("landed antifragility-recovery pilot review: landed", ingress)
            self.assertIn("execution/ready-work-graphs", ingress)
            self.assertIn("Landed antifragility-recovery pilot review", landing_log)
            self.assertIn("second successful recovery trunk", landing_log)
            self.assertIn("shelf after `diagnosis-repair`", landing_log)
            self.assertIn("The landed `antifragility-recovery` pilot review is now complete", distillation_roadmap)
            self.assertIn("Run the `execution/ready-work-graphs` direct-read", root_roadmap)
            self.assertIn("Landed Antifragility-Recovery Pilot Review", tree_contract)
            self.assertIn("chooses `execution/ready-work-graphs`", tree_contract)
            self.assertIn(
                "accepted the landed `antifragility-recovery` pilot review",
                changelog,
            )

            for technique_id, path in (
                (
                    "AOA-T-0097",
                    "techniques/recovery/antifragility-recovery/degrade-reground-recover/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0099",
                    "techniques/recovery/antifragility-recovery/isolated-service-stop-on-shared-substrate/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0100",
                    "techniques/recovery/antifragility-recovery/stress-receipt-reground-closeout/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0098",
                    "techniques/recovery/antifragility-recovery/receipt-first-failure-analysis/TECHNIQUE.md",
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)
                    self.assertTrue((REPO_ROOT / path).is_file())

            for old_path, current_dir, current_path in (
                (
                    "techniques/agent-workflows/dependency-aware-task-graph/",
                    "techniques/execution/ready-work-graphs/dependency-aware-task-graph/",
                    "techniques/execution/ready-work-graphs/dependency-aware-task-graph/TECHNIQUE.md",
                ),
                (
                    "techniques/agent-workflows/ready-work-from-blocker-graph/",
                    "techniques/execution/ready-work-graphs/ready-work-from-blocker-graph/",
                    "techniques/execution/ready-work-graphs/ready-work-from-blocker-graph/TECHNIQUE.md",
                ),
                (
                    "techniques/agent-workflows/requirements-design-tasks-ladder/",
                    "techniques/execution/ready-work-graphs/requirements-design-tasks-ladder/",
                    "techniques/execution/ready-work-graphs/requirements-design-tasks-ladder/TECHNIQUE.md",
                ),
            ):
                with self.subTest(old_path=old_path):
                    self.assertIn(old_path, review)
                    self.assertIn(current_dir, review)
                    self.assertFalse((REPO_ROOT / old_path).exists())
                    self.assertTrue((REPO_ROOT / current_path).is_file())

    def test_ready_work_graphs_direct_read_review_accepts_sixteenth_pilot(
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
                / "ready-work-graphs-direct-read-migration-review.md"
            ).read_text(encoding="utf-8")
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Ready-Work-Graphs Direct-Read Migration Review", review)
            self.assertIn("accepted-for-sixteenth-migration-pilot", review)
            self.assertIn("not path migration", review)
            self.assertIn("Accept `execution/ready-work-graphs`", review)
            self.assertIn("Direct Bundle Read", review)
            self.assertIn("Watch Line For `AOA-T-0055`", review)
            self.assertIn("Execution Trunk Fit", review)
            self.assertIn("Boundary Watch Accepted", review)
            self.assertIn("Proposed Move", review)
            self.assertIn("Move exactly these three bundles", review)
            self.assertIn("Do not move files from this review pack alone", review)
            self.assertIn("Do not change `domain` or `kind`", review)
            self.assertIn("Run the sixteenth pilot migration", review)
            self.assertIn(
                "ready-work-graphs-direct-read-migration-review",
                reviews_index,
            )
            self.assertIn("ready-work-graphs direct-read review: landed", ingress)
            self.assertIn("accepted-for-sixteenth-migration-pilot", ingress)
            self.assertIn(
                "Ready-work-graphs direct-read migration review",
                landing_log,
            )
            self.assertIn("AOA-T-0055` as a watch-line readiness ladder", landing_log)
            self.assertIn("accepted-for-sixteenth-migration-pilot", distillation_roadmap)
            self.assertIn("Review the landed `intent-chain` pilot", root_roadmap)
            self.assertIn("Ready-Work-Graphs Direct-Read Migration Review", tree_contract)
            self.assertIn("preserving\n`AOA-T-0055` as a readiness ladder", tree_contract)
            self.assertIn(
                "accepted the `ready-work-graphs` direct-read migration review",
                changelog,
            )

            for technique_id, old_path, current_path in (
                (
                    "AOA-T-0049",
                    "techniques/agent-workflows/dependency-aware-task-graph/TECHNIQUE.md",
                    "techniques/execution/ready-work-graphs/dependency-aware-task-graph/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0050",
                    "techniques/agent-workflows/ready-work-from-blocker-graph/TECHNIQUE.md",
                    "techniques/execution/ready-work-graphs/ready-work-from-blocker-graph/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0055",
                    "techniques/agent-workflows/requirements-design-tasks-ladder/TECHNIQUE.md",
                    "techniques/execution/ready-work-graphs/requirements-design-tasks-ladder/TECHNIQUE.md",
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)
                    self.assertIn(old_path.rsplit("/", 1)[0] + "/", review)
                    self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                    self.assertFalse((REPO_ROOT / old_path).exists())
                    self.assertTrue((REPO_ROOT / current_path).is_file())

    def test_ready_work_graphs_tree_pilot_migration_landed(self) -> None:
            receipt = (
                REPO_ROOT
                / "legacy"
                / "receipts"
                / "2026-05-05-ready-work-graphs-tree-pilot.md"
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

            self.assertIn("Ready-Work-Graphs Tree Pilot Receipt", receipt)
            self.assertIn("sixteenth authored path migration", receipt)
            self.assertIn("Preserve `AOA-T-0055` as a readiness ladder", receipt)
            self.assertIn("shared placement applies", execution_agents)
            self.assertIn("ready-work-graphs/", execution_agents)
            self.assertIn("ready-work-graphs migration: landed", ingress)
            self.assertIn("Ready-work-graphs tree pilot migration", landing_log)
            self.assertIn("sixteenth pilot migration is\n   now landed", distillation_roadmap)
            self.assertIn("sixteenth landed pilot moved", root_roadmap)
            self.assertIn("2026-05-05-ready-work-graphs-tree-pilot", tree_contract)
            self.assertIn("moved `AOA-T-0049`", changelog)

            for technique_id, old_path, current_path in (
                (
                    "AOA-T-0049",
                    "techniques/agent-workflows/dependency-aware-task-graph/",
                    "techniques/execution/ready-work-graphs/dependency-aware-task-graph/",
                ),
                (
                    "AOA-T-0050",
                    "techniques/agent-workflows/ready-work-from-blocker-graph/",
                    "techniques/execution/ready-work-graphs/ready-work-from-blocker-graph/",
                ),
                (
                    "AOA-T-0055",
                    "techniques/agent-workflows/requirements-design-tasks-ladder/",
                    "techniques/execution/ready-work-graphs/requirements-design-tasks-ladder/",
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, receipt)
                    self.assertIn(old_path, receipt)
                    self.assertIn(current_path, receipt)
                    self.assertFalse((REPO_ROOT / old_path).exists())
                    self.assertTrue((REPO_ROOT / current_path / "TECHNIQUE.md").is_file())

    def test_landed_ready_work_graphs_review_selects_intent_chain(self) -> None:
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
                / "landed-ready-work-graphs-pilot-review.md"
            ).read_text(encoding="utf-8")
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Landed Ready-Work-Graphs Pilot Review", review)
            self.assertIn("pilot-validated", review)
            self.assertIn("choose `execution/intent-chain`", review)
            self.assertIn("first successful shelf under the `execution` trunk", review)
            self.assertIn("AOA-T-0055` remains the shelf watch line", review)
            self.assertIn("What The Sixteenth Pilot Proved", review)
            self.assertIn("Remaining Weaknesses", review)
            self.assertIn("Seventeenth Shelf Choice", review)
            self.assertIn("Why direct-read first", review)
            self.assertIn("Do not move `execution/intent-chain`", review)
            self.assertIn("do not move any\nfiles until that", review)
            self.assertIn("review lands", review)
            self.assertIn("landed-ready-work-graphs-pilot-review", reviews_index)
            self.assertIn("landed ready-work-graphs pilot review: landed", ingress)
            self.assertIn("execution/intent-chain", ingress)
            self.assertIn("Landed ready-work-graphs pilot review", landing_log)
            self.assertIn("first successful execution trunk shelf", landing_log)
            self.assertIn("execution/intent-chain` for the next", landing_log)
            self.assertIn("The landed `ready-work-graphs` pilot review is now complete", distillation_roadmap)
            self.assertIn("Review the landed `intent-chain` pilot", root_roadmap)
            self.assertIn("Landed Ready-Work-Graphs Pilot Review", tree_contract)
            self.assertIn("chooses `execution/intent-chain`", tree_contract)
            self.assertIn(
                "accepted the landed `ready-work-graphs` pilot review",
                changelog,
            )

            for technique_id, path in (
                (
                    "AOA-T-0049",
                    "techniques/execution/ready-work-graphs/dependency-aware-task-graph/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0050",
                    "techniques/execution/ready-work-graphs/ready-work-from-blocker-graph/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0055",
                    "techniques/execution/ready-work-graphs/requirements-design-tasks-ladder/TECHNIQUE.md",
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)
                    self.assertTrue((REPO_ROOT / path).is_file())

            for old_dir, current_dir, current_path in (
                (
                    "techniques/agent-workflows/intent-plan-dry-run-contract-chain/",
                    "techniques/execution/intent-chain/intent-plan-dry-run-contract-chain/",
                    "techniques/execution/intent-chain/intent-plan-dry-run-contract-chain/TECHNIQUE.md",
                ),
                (
                    "techniques/agent-workflows/new-intent-rollout-checklist/",
                    "techniques/execution/intent-chain/new-intent-rollout-checklist/",
                    "techniques/execution/intent-chain/new-intent-rollout-checklist/TECHNIQUE.md",
                ),
            ):
                with self.subTest(old_dir=old_dir):
                    self.assertIn(old_dir, review)
                    self.assertIn(current_dir, review)
                    self.assertIn(current_path, review)
                    self.assertFalse((REPO_ROOT / old_dir).exists())
                    self.assertTrue((REPO_ROOT / current_path).is_file())

    def test_intent_chain_direct_read_review_accepts_seventeenth_pilot(self) -> None:
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
                / "intent-chain-direct-read-migration-review.md"
            ).read_text(encoding="utf-8")
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Intent-Chain Direct-Read Migration Review", review)
            self.assertIn("accepted-for-seventeenth-migration-pilot", review)
            self.assertIn("Accept `execution/intent-chain`", review)
            self.assertIn("Move exactly `AOA-T-0004` and `AOA-T-0005`", review)
            self.assertIn("not path migration", review)
            self.assertIn("Direct Bundle Read", review)
            self.assertIn("Why The Earlier Small-Shelf Hold No Longer Blocks", review)
            self.assertIn("Execution Trunk Fit", review)
            self.assertIn("Proposed Move", review)
            self.assertIn("Do not move files from this review pack alone", review)
            self.assertIn("Do not promote `AOA-T-0005` to canonical", review)
            self.assertIn(
                "router ownership, API contract authority,\n  runtime dispatch",
                review,
            )
            self.assertIn("Run the seventeenth migration pilot", review)
            self.assertIn("intent-chain-direct-read-migration-review", reviews_index)
            self.assertIn("intent-chain direct-read review: landed", ingress)
            self.assertIn("accepted-for-seventeenth-migration-pilot", ingress)
            self.assertIn("Intent-chain direct-read migration review", landing_log)
            self.assertIn("AOA-T-0004` as the base artifact-first intent chain", landing_log)
            self.assertIn("AOA-T-0005` as `status: promoted`", landing_log)
            self.assertIn("accepted-for-seventeenth-migration-pilot", distillation_roadmap)
            self.assertIn("Review the landed `intent-chain` pilot", root_roadmap)
            self.assertIn("Intent-Chain Direct-Read Migration Review", tree_contract)
            self.assertIn("preserves `AOA-T-0005` as promoted", tree_contract)
            self.assertIn(
                "accepted the `intent-chain` direct-read migration review",
                changelog,
            )

            for technique_id, old_path, current_path in (
                (
                    "AOA-T-0004",
                    "techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md",
                    "techniques/execution/intent-chain/intent-plan-dry-run-contract-chain/TECHNIQUE.md",
                ),
                (
                    "AOA-T-0005",
                    "techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md",
                    "techniques/execution/intent-chain/new-intent-rollout-checklist/TECHNIQUE.md",
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)
                    self.assertIn(old_path.rsplit("/", 1)[0] + "/", review)
                    self.assertIn(current_path.rsplit("/", 1)[0] + "/", review)
                    self.assertFalse((REPO_ROOT / old_path).exists())
                    self.assertTrue((REPO_ROOT / current_path).is_file())

    def test_intent_chain_tree_pilot_migration_landed(self) -> None:
            receipt = (
                REPO_ROOT
                / "legacy"
                / "receipts"
                / "2026-05-05-intent-chain-tree-pilot.md"
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

            self.assertIn("Intent-Chain Tree Pilot Receipt", receipt)
            self.assertIn("Seventeenth authored path migration", receipt)
            self.assertIn("AOA-T-0005` stayed `promoted`", receipt)
            self.assertIn("intent-chain/", execution_agents)
            self.assertIn("router ownership", execution_agents)
            self.assertIn("API contract\nauthority", execution_agents)
            self.assertIn("intent-chain migration: landed", ingress)
            self.assertIn("Intent-chain tree pilot migration", landing_log)
            self.assertIn("seventeenth pilot migration is now\n   landed", distillation_roadmap)
            self.assertIn("seventeenth pilot without moving files", root_roadmap)
            self.assertIn("Review the landed `intent-chain` pilot", root_roadmap)
            self.assertIn("2026-05-05-intent-chain-tree-pilot", tree_contract)
            self.assertIn("moved `AOA-T-0004`", changelog)

            for technique_id, old_path, current_path in (
                (
                    "AOA-T-0004",
                    "techniques/agent-workflows/intent-plan-dry-run-contract-chain/",
                    "techniques/execution/intent-chain/intent-plan-dry-run-contract-chain/",
                ),
                (
                    "AOA-T-0005",
                    "techniques/agent-workflows/new-intent-rollout-checklist/",
                    "techniques/execution/intent-chain/new-intent-rollout-checklist/",
                ),
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, receipt)
                    self.assertIn(old_path, receipt)
                    self.assertIn(current_path, receipt)
                    self.assertFalse((REPO_ROOT / old_path).exists())
                    self.assertTrue((REPO_ROOT / current_path / "TECHNIQUE.md").is_file())

    def test_landed_intent_chain_review_selects_agent_workflows_core(self) -> None:
            review = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "parts"
                / "technique-reform-ingress"
                / "reviews"
                / "landed-intent-chain-pilot-review.md"
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

            self.assertIn("Landed Intent-Chain Pilot Review", review)
            self.assertIn("second successful shelf under the `execution` trunk", review)
            self.assertIn("`AOA-T-0005` can stay promoted after path migration", review)
            self.assertIn("Choose `execution/agent-workflows-core`", review)
            self.assertIn("current projected five-leaf shelf", review)
            self.assertIn("whether the shell-facing cluster should\nsplit", review)
            self.assertIn("Do not move `execution/agent-workflows-core`", review)
            self.assertIn("landed-intent-chain-pilot-review", reviews_index)
            self.assertIn("landed intent-chain pilot review: landed", ingress)
            self.assertIn("execution/agent-workflows-core", ingress)
            self.assertIn("Landed intent-chain pilot review", landing_log)
            self.assertIn("second successful execution trunk shelf", landing_log)
            self.assertIn("The landed `intent-chain` pilot review is now complete", distillation_roadmap)
            self.assertIn(
                "Run the `execution/agent-workflows-core` direct-read",
                root_roadmap,
            )
            self.assertIn("Landed Intent-Chain Pilot Review", tree_contract)
            self.assertIn("execution/agent-workflows-core", tree_contract)
            self.assertIn(
                "accepted the landed `intent-chain` pilot review",
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


if __name__ == "__main__":
    unittest.main()
