from __future__ import annotations

import sys
import unittest
from pathlib import Path


SUPPORT_DIR = Path(__file__).resolve().parent / "support"
if str(SUPPORT_DIR) not in sys.path:
    sys.path.insert(0, str(SUPPORT_DIR))

from distillation_topology_fixtures import *  # noqa: F403


class DistillationTreePilotIngressWaveTests(unittest.TestCase):
    def test_review_compaction_pilot_migration_is_landed_after_direct_read(self) -> None:
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
                / "review-compaction-direct-read-migration-review.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()

            self.assertIn("Review-Compaction Direct-Read Migration Review", review)
            self.assertIn("accepted-for-first-migration-pilot", review)
            self.assertIn("not path migration", review)
            self.assertIn("not `tree_path` frontmatter", review)
            self.assertIn("AOA-T-0051", review)
            self.assertIn("AOA-T-0052", review)
            self.assertIn("AOA-T-0054", review)
            self.assertIn("commit-triggered-background-review", review)
            self.assertIn("review-findings-compaction", review)
            self.assertIn("compaction-resilient-skill-loading", review)
            self.assertIn("techniques/continuity/review-compaction/", review)
            self.assertIn("The move is clearer than current placement", review)
            self.assertIn("Move exactly these three bundles", review)
            self.assertIn("Do not move files from this review pack alone", review)
            self.assertIn("Do not add `family` or `tree_path` frontmatter", review)
            self.assertIn("Create a minimal `techniques/continuity/AGENTS.md`", review)
            self.assertIn("Run `python scripts/release_check.py`", review)

            self.assertIn("review-compaction-direct-read-migration-review", reviews_index)
            self.assertIn("review-compaction direct-read review: landed", ingress)
            self.assertIn("accepted-for-first-migration-pilot", ingress)
            self.assertIn("The first pilot migration has moved exactly", ingress)
            self.assertIn("techniques/continuity/review-compaction/", ingress)
            self.assertIn("review-compaction direct-read migration review is landed", distillation_roadmap)
            self.assertIn("first pilot migration", distillation_roadmap)
            self.assertIn("first landed pilot moved `AOA-T-0051`", root_roadmap)
            self.assertIn("current landed pilot review", tree_contract)

    def test_landed_review_compaction_pilot_review_selects_next_direct_read_shelf(self) -> None:
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
                / "landed-review-compaction-pilot-review.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()

            self.assertIn("Landed Review-Compaction Pilot Review", review)
            self.assertIn("pilot-validated", review)
            self.assertIn("not path migration", review)
            self.assertIn("not `tree_path` frontmatter", review)
            self.assertIn("The pilot improved browsability", review)
            self.assertIn("Root `legacy/receipts/`", review)
            self.assertIn("Choose `handoff-continuation`", review)
            self.assertIn("AOA-T-0056", review)
            self.assertIn("AOA-T-0062", review)
            self.assertIn("Do not move `handoff-continuation` from this review alone", review)
            self.assertIn("Run a direct-read migration review for `handoff-continuation`", review)

            self.assertIn("landed-review-compaction-pilot-review", reviews_index)
            self.assertIn("landed review-compaction pilot review: landed", ingress)
            self.assertIn("pilot-validated", ingress)
            self.assertIn("handoff-continuation", ingress)
            self.assertIn("direct-read migration review", distillation_roadmap)
            self.assertIn("Landed review-compaction pilot review", landing_log)
            self.assertIn("handoff-continuation", root_roadmap)
            self.assertIn("Landed Review-Compaction Pilot Review", tree_contract)

    def test_handoff_continuation_direct_read_review_accepts_second_pilot_without_migration(self) -> None:
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
                / "handoff-continuation-direct-read-migration-review.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Handoff-Continuation Direct-Read Migration Review", review)
            self.assertIn("accepted-for-second-migration-pilot", review)
            self.assertIn("not path migration", review)
            self.assertIn("not `tree_path` frontmatter", review)
            for technique_id in (
                "AOA-T-0056",
                "AOA-T-0057",
                "AOA-T-0058",
                "AOA-T-0059",
                "AOA-T-0060",
                "AOA-T-0061",
                "AOA-T-0062",
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)
            for slug in (
                "channelized-agent-mailbox",
                "structured-handoff-before-compaction",
                "receipt-confirmed-handoff-packet",
                "git-verified-handoff-claims",
                "session-opening-ritual-before-work",
                "cross-repo-resource-map-bootstrap",
                "episode-bounded-agent-loop",
            ):
                with self.subTest(slug=slug):
                    self.assertIn(slug, review)

            self.assertIn("The move is clearer than current placement", review)
            self.assertIn("Move exactly these seven bundles", review)
            self.assertIn("techniques/continuity/handoff-continuation/", review)
            self.assertIn("Do not move files from this review pack alone", review)
            self.assertIn("Do not add `family` or `tree_path` frontmatter", review)
            self.assertIn("Run the second pilot migration", review)
            self.assertIn("run `python scripts/release_check.py`", review)

            self.assertIn("handoff-continuation-direct-read-migration-review", reviews_index)
            self.assertIn("handoff-continuation direct-read review: landed", ingress)
            self.assertIn("accepted-for-second-migration-pilot", ingress)
            self.assertIn("handoff-continuation migration: landed", ingress)
            self.assertIn("handoff-continuation` direct-read migration review is now landed", distillation_roadmap)
            self.assertIn("Handoff-continuation direct-read migration review", landing_log)
            self.assertIn("second landed pilot moved `AOA-T-0056` through `AOA-T-0062`", root_roadmap)
            self.assertIn("Handoff-Continuation Direct-Read Migration Review", tree_contract)
            self.assertIn("accepted the `handoff-continuation` direct-read migration review", changelog)

    def test_handoff_continuation_tree_pilot_migration_is_landed_after_direct_read(self) -> None:
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

            self.assertIn("handoff-continuation migration: landed", ingress)
            self.assertIn("techniques/continuity/handoff-continuation/", ingress)
            self.assertIn("without frontmatter changes", ingress)
            self.assertIn("media-ingest direct-read review: landed", ingress)
            self.assertIn("accepted-for-third-migration-pilot", ingress)
            self.assertIn("second pilot migration is", distillation_roadmap)
            self.assertIn("Handoff-continuation tree pilot migration", landing_log)
            self.assertIn("legacy/receipts/2026-05-04-handoff-continuation-tree-pilot.md", landing_log)
            self.assertIn("second landed pilot moved `AOA-T-0056` through `AOA-T-0062`", root_roadmap)
            self.assertIn("Handoff-Continuation Direct-Read Migration Review", tree_contract)
            self.assertIn("2026-05-04-handoff-continuation-tree-pilot.md", tree_contract)
            self.assertIn("moved `AOA-T-0056` through `AOA-T-0062`", changelog)

    def test_landed_handoff_continuation_pilot_review_selects_media_ingest(self) -> None:
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
                / "landed-handoff-continuation-pilot-review.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
            archived_wave2 = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "legacy"
                / "archive"
                / "closed-incoming-packets"
                / "chat-graph-review-mailbox"
                / "docs"
                / "EXTERNAL_TECHNIQUE_CANDIDATES_CHAT_GRAPH_REVIEW_MAILBOX.md"
            ).read_text(encoding="utf-8")
            archived_wave3 = (
                REPO_ROOT
                / "mechanics"
                / "distillation"
                / "legacy"
                / "archive"
                / "closed-incoming-packets"
                / "chat-handoff-bounded-continuation"
                / "docs"
                / "EXTERNAL_TECHNIQUE_CANDIDATES_CHAT_HANDOFF_BOUNDED_CONTINUATION.md"
            ).read_text(encoding="utf-8")

            self.assertIn("Landed Handoff-Continuation Pilot Review", review)
            self.assertIn("pilot-validated", review)
            self.assertIn("not path migration", review)
            self.assertIn("not `tree_path` frontmatter", review)
            self.assertIn("Accept the landed `handoff-continuation` pilot", review)
            self.assertIn("staging links", review)
            self.assertIn("Choose `media-ingest`", review)
            for technique_id in (
                "AOA-T-0070",
                "AOA-T-0071",
                "AOA-T-0072",
                "AOA-T-0073",
                "AOA-T-0074",
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)

            self.assertIn("Do not move `media-ingest` from this review alone", review)
            self.assertIn("Run a direct-read migration review for `media-ingest`", review)
            self.assertIn("landed-handoff-continuation-pilot-review", reviews_index)
            self.assertIn("landed handoff-continuation pilot review: landed", ingress)
            self.assertIn("media-ingest", ingress)
            self.assertIn("`media-ingest` direct-read review is now", distillation_roadmap)
            self.assertIn("Landed handoff-continuation pilot review", landing_log)
            self.assertIn("selected\n  `media-ingest`", changelog)
            self.assertIn(
                "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
                root_roadmap,
            )
            self.assertIn("Landed Handoff-Continuation Pilot Review", tree_contract)
            self.assertIn("techniques/continuity/handoff-continuation/channelized-agent-mailbox/TECHNIQUE.md", archived_wave2)
            self.assertIn("techniques/continuity/handoff-continuation/episode-bounded-agent-loop/TECHNIQUE.md", archived_wave3)
            self.assertNotIn(
                "techniques/agent-workflows/channelized-agent-mailbox/TECHNIQUE.md",
                archived_wave2,
            )
            self.assertNotIn(
                "techniques/agent-workflows/episode-bounded-agent-loop/TECHNIQUE.md",
                archived_wave3,
            )

    def test_media_ingest_direct_read_review_accepts_third_pilot(self) -> None:
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
                / "media-ingest-direct-read-migration-review.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Media-Ingest Direct-Read Migration Review", review)
            self.assertIn("accepted-for-third-migration-pilot", review)
            self.assertIn("not path migration", review)
            self.assertIn("not\n`tree_path` frontmatter", review)
            self.assertIn("Accept `media-ingest` as the third migration pilot", review)
            for technique_id in (
                "AOA-T-0070",
                "AOA-T-0071",
                "AOA-T-0072",
                "AOA-T-0073",
                "AOA-T-0074",
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)

            self.assertIn("Telegram Edge", review)
            self.assertIn("telegram-account-auth-and-session-bridge", review)
            self.assertIn("Move exactly these five bundles", review)
            self.assertIn("techniques/ingest/media-ingest/", review)
            self.assertIn("Do not move files from this review pack alone", review)
            self.assertIn("Do not add `family` or `tree_path` frontmatter", review)
            self.assertIn("Run the third pilot migration", review)

            self.assertIn("media-ingest-direct-read-migration-review", reviews_index)
            self.assertIn("media-ingest direct-read review: landed", ingress)
            self.assertIn("accepted-for-third-migration-pilot", ingress)
            self.assertIn("media-ingest migration: landed", ingress)
            self.assertIn("third pilot migration", ingress)
            self.assertIn("media-ingest` direct-read review is now", distillation_roadmap)
            self.assertIn("third pilot\n   migration is landed", distillation_roadmap)
            self.assertIn("Media-ingest direct-read migration review", landing_log)
            self.assertIn("Media-ingest tree pilot migration", landing_log)
            self.assertIn("accepted the `media-ingest` direct-read migration review", changelog)
            self.assertIn("moved `AOA-T-0070` through `AOA-T-0074`", changelog)
            self.assertIn("first non-continuity migrated shelf", root_roadmap)
            self.assertIn("third landed pilot, the first non-continuity", root_roadmap)
            self.assertIn("Media-Ingest Direct-Read Migration Review", tree_contract)
            self.assertIn("2026-05-04-media-ingest-tree-pilot.md", tree_contract)
            self.assertTrue(
                (
                    REPO_ROOT
                    / "techniques"
                    / "ingest"
                    / "media-ingest"
                    / "two-stage-document-ocr-pipeline"
                    / "TECHNIQUE.md"
                ).is_file()
            )

    def test_landed_media_ingest_pilot_review_selects_diagnosis_repair(self) -> None:
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
                / "landed-media-ingest-pilot-review.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Landed Media-Ingest Pilot Review", review)
            self.assertIn("pilot-validated", review)
            self.assertIn("not path migration", review)
            self.assertIn("not `tree_path` frontmatter", review)
            self.assertIn("Accept the landed `media-ingest` pilot", review)
            self.assertIn("first non-continuity trunk test", review)
            self.assertIn("Telegram edge remained bounded", review)
            self.assertIn("Choose `diagnosis-repair`", review)
            for technique_id in (
                "AOA-T-0080",
                "AOA-T-0081",
                "AOA-T-0082",
                "AOA-T-0083",
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)

            self.assertIn("Do not move `diagnosis-repair` from this review alone", review)
            self.assertIn("Run a direct-read migration review for `diagnosis-repair`", review)
            self.assertIn("landed-media-ingest-pilot-review", reviews_index)
            self.assertIn("landed media-ingest pilot review: landed", ingress)
            self.assertIn("diagnosis-repair", ingress)
            self.assertIn("diagnosis-repair` is now", distillation_roadmap)
            self.assertIn("Landed media-ingest pilot review", landing_log)
            self.assertIn("selected\n  `diagnosis-repair`", changelog)
            self.assertIn(
                "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
                root_roadmap,
            )
            self.assertIn("Landed Media-Ingest Pilot Review", tree_contract)
            self.assertIn("techniques/recovery/diagnosis-repair/", tree_contract)

    def test_diagnosis_repair_direct_read_review_accepts_fourth_pilot(self) -> None:
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
                / "diagnosis-repair-direct-read-migration-review.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Diagnosis-Repair Direct-Read Migration Review", review)
            self.assertIn("accepted-for-fourth-migration-pilot", review)
            self.assertIn("not path migration", review)
            self.assertIn("not\n`tree_path` frontmatter", review)
            self.assertIn("Accept `diagnosis-repair` as the fourth migration pilot", review)
            for technique_id in (
                "AOA-T-0080",
                "AOA-T-0081",
                "AOA-T-0082",
                "AOA-T-0083",
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)

            self.assertIn("Mixed Kind Stress", review)
            self.assertIn("Move exactly these four bundles", review)
            self.assertIn("techniques/recovery/diagnosis-repair/", review)
            self.assertIn("Do not move files from this review pack alone", review)
            self.assertIn("Do not add `family` or `tree_path` frontmatter", review)
            self.assertIn("Run the fourth pilot migration", review)

            self.assertIn("diagnosis-repair-direct-read-migration-review", reviews_index)
            self.assertIn("diagnosis-repair direct-read review: landed", ingress)
            self.assertIn("accepted-for-fourth-migration-pilot", ingress)
            self.assertIn("diagnosis-repair migration: landed", ingress)
            self.assertIn("fourth pilot migration", ingress)
            self.assertIn("accepted-for-fourth-migration-pilot", distillation_roadmap)
            self.assertIn("fourth pilot migration is", distillation_roadmap)
            self.assertIn("techniques/recovery/diagnosis-repair/", distillation_roadmap)
            self.assertIn("Diagnosis-repair direct-read migration review", landing_log)
            self.assertIn("Diagnosis-repair tree pilot migration", landing_log)
            self.assertIn("accepted the `diagnosis-repair` direct-read migration review", changelog)
            self.assertIn("moved `AOA-T-0080` through `AOA-T-0083`", changelog)
            self.assertIn("fourth landed pilot", root_roadmap)
            self.assertIn(
                "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
                root_roadmap,
            )
            self.assertIn("Diagnosis-Repair Direct-Read Migration Review", tree_contract)
            self.assertIn("AOA-T-0080` through `AOA-T-0083", tree_contract)
            self.assertIn("2026-05-04-diagnosis-repair-tree-pilot.md", tree_contract)
            self.assertTrue(
                (
                    REPO_ROOT
                    / "techniques"
                    / "recovery"
                    / "diagnosis-repair"
                    / "session-drift-taxonomy"
                    / "TECHNIQUE.md"
                ).is_file()
            )

    def test_landed_diagnosis_repair_pilot_review_selects_instruction_surface(self) -> None:
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
                / "landed-diagnosis-repair-pilot-review.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Landed Diagnosis-Repair Pilot Review", review)
            self.assertIn("pilot-validated", review)
            self.assertIn("not path migration", review)
            self.assertIn("not `tree_path` frontmatter", review)
            self.assertIn("Accept the landed `diagnosis-repair` pilot", review)
            self.assertIn("first recovery trunk test", review)
            self.assertIn("Choose `instruction-surface`", review)
            for technique_id in (
                "AOA-T-0012",
                "AOA-T-0013",
                "AOA-T-0024",
                "AOA-T-0027",
                "AOA-T-0029",
                "AOA-T-0030",
                "AOA-T-0035",
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)

            self.assertIn("Why not `kag-source-lift` first", review)
            self.assertIn("Do not move `instruction-surface` from this review alone", review)
            self.assertIn(
                "Run a direct-read migration review for `instruction-surface`",
                review,
            )
            self.assertIn("landed-diagnosis-repair-pilot-review", reviews_index)
            self.assertIn("landed diagnosis-repair pilot review: landed", ingress)
            self.assertIn("instruction-surface", ingress)
            self.assertIn("instruction-surface direct-read review: landed", ingress)
            self.assertIn("Landed Diagnosis-Repair Pilot Review", ingress)
            self.assertIn("`instruction-surface` is now chosen", distillation_roadmap)
            self.assertIn("accepted-for-fifth-migration-pilot", distillation_roadmap)
            self.assertIn("Landed diagnosis-repair pilot review", landing_log)
            self.assertIn("selected\n  `instruction-surface`", changelog)
            self.assertIn(
                "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
                root_roadmap,
            )
            self.assertIn("Landed Diagnosis-Repair Pilot Review", tree_contract)
            self.assertIn("instruction-surface", tree_contract)

    def test_instruction_surface_direct_read_review_accepts_fifth_pilot(self) -> None:
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
                / "instruction-surface-direct-read-migration-review.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Instruction-Surface Direct-Read Migration Review", review)
            self.assertIn("accepted-for-fifth-migration-pilot", review)
            self.assertIn("not path migration", review)
            self.assertIn("not\n`tree_path` frontmatter", review)
            self.assertIn("Accept `instruction-surface` as the fifth migration pilot", review)
            for technique_id in (
                "AOA-T-0012",
                "AOA-T-0013",
                "AOA-T-0024",
                "AOA-T-0027",
                "AOA-T-0029",
                "AOA-T-0030",
                "AOA-T-0035",
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)

            self.assertIn("Profile Edge", review)
            self.assertIn("Move exactly these seven bundles", review)
            self.assertIn("techniques/instruction/instruction-surface/", review)
            self.assertIn("Do not move files from this review pack alone", review)
            self.assertIn("Do not add `family` or `tree_path` frontmatter", review)
            self.assertIn("Run the fifth pilot migration", review)

            self.assertIn("instruction-surface-direct-read-migration-review", reviews_index)
            self.assertIn("instruction-surface direct-read review: landed", ingress)
            self.assertIn("accepted-for-fifth-migration-pilot", ingress)
            self.assertIn("instruction-surface migration: landed", ingress)
            self.assertIn("fifth pilot migration", ingress)
            self.assertIn("accepted-for-fifth-migration-pilot", distillation_roadmap)
            self.assertIn("fifth pilot migration is", distillation_roadmap)
            self.assertIn("techniques/instruction/instruction-surface/", distillation_roadmap)
            self.assertIn("Instruction-surface direct-read migration review", landing_log)
            self.assertIn("Instruction-surface tree pilot migration", landing_log)
            self.assertIn(
                "accepted the `instruction-surface` direct-read migration review",
                changelog,
            )
            self.assertIn("moved `AOA-T-0012`, `AOA-T-0013", changelog)
            self.assertIn(
                "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
                root_roadmap,
            )
            self.assertIn("Instruction-Surface Direct-Read Migration Review", tree_contract)
            self.assertIn("AOA-T-0012`, `AOA-T-0013", tree_contract)
            self.assertIn("2026-05-04-instruction-surface-tree-pilot.md", tree_contract)
            self.assertTrue(
                (
                    REPO_ROOT
                    / "techniques"
                    / "instruction"
                    / "instruction-surface"
                    / "deterministic-context-composition"
                    / "TECHNIQUE.md"
                ).is_file()
            )
            self.assertFalse(
                (
                    REPO_ROOT
                    / "techniques"
                    / "docs"
                    / "deterministic-context-composition"
                ).exists()
            )

    def test_landed_instruction_surface_pilot_review_selects_kag_source_lift(self) -> None:
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
                / "landed-instruction-surface-pilot-review.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Landed Instruction-Surface Pilot Review", review)
            self.assertIn("pilot-validated", review)
            self.assertIn("not path migration", review)
            self.assertIn("not `tree_path` frontmatter", review)
            self.assertIn("Accept the landed `instruction-surface` pilot", review)
            self.assertIn("first instruction trunk test", review)
            self.assertIn("Choose `kag-source-lift`", review)
            for technique_id in (
                "AOA-T-0018",
                "AOA-T-0019",
                "AOA-T-0020",
                "AOA-T-0021",
                "AOA-T-0022",
                "AOA-T-0046",
                "AOA-T-0047",
                "AOA-T-0048",
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)

            self.assertIn("Why not `docs-boundary` first", review)
            self.assertIn("Do not move `kag-source-lift` from this review alone", review)
            self.assertIn("Do not treat `knowledge-lift` as `aoa-kag`", review)
            self.assertIn("Run a direct-read migration review for `kag-source-lift`", review)

            self.assertIn("landed-instruction-surface-pilot-review", reviews_index)
            self.assertIn("landed instruction-surface pilot review: landed", ingress)
            self.assertIn("kag-source-lift", ingress)
            self.assertIn("next direct-read migration review", ingress)
            self.assertIn("`kag-source-lift` is now chosen", distillation_roadmap)
            self.assertIn("Landed instruction-surface pilot review", landing_log)
            self.assertIn("selected\n  `kag-source-lift`", changelog)
            self.assertIn(
                "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
                root_roadmap,
            )
            self.assertIn("Landed Instruction-Surface Pilot Review", tree_contract)
            self.assertIn("knowledge-lift", tree_contract)
            self.assertIn("kag-source-lift", tree_contract)

    def test_kag_source_lift_direct_read_review_accepts_sixth_pilot(self) -> None:
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
                / "kag-source-lift-direct-read-migration-review.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Kag-Source-Lift Direct-Read Migration Review", review)
            self.assertIn("accepted-for-sixth-migration-pilot", review)
            self.assertIn("not path migration", review)
            self.assertIn("not\n`tree_path` frontmatter", review)
            self.assertIn("Accept `kag-source-lift` as the sixth migration pilot", review)
            for technique_id in (
                "AOA-T-0018",
                "AOA-T-0019",
                "AOA-T-0020",
                "AOA-T-0021",
                "AOA-T-0022",
                "AOA-T-0046",
                "AOA-T-0047",
                "AOA-T-0048",
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)

            self.assertIn("Source-Lift Chain", review)
            self.assertIn("KAG Name Edge", review)
            self.assertIn("Move exactly these eight bundles", review)
            self.assertIn("techniques/knowledge-lift/kag-source-lift/", review)
            self.assertIn("Do not move files from this review pack alone", review)
            self.assertIn("Do not add `family` or `tree_path` frontmatter", review)
            self.assertIn("Do not treat `knowledge-lift` as `aoa-kag`", review)
            self.assertIn("Run the sixth pilot migration", review)

            self.assertIn("kag-source-lift-direct-read-migration-review", reviews_index)
            self.assertIn("kag-source-lift direct-read review: landed", ingress)
            self.assertIn("accepted-for-sixth-migration-pilot", ingress)
            self.assertIn("kag-source-lift migration: landed", ingress)
            self.assertIn("The sixth pilot migration is now landed", ingress)
            self.assertIn("accepted-for-sixth-migration-pilot", distillation_roadmap)
            self.assertIn("The sixth pilot migration is now", distillation_roadmap)
            self.assertIn("Kag-source-lift direct-read migration review", landing_log)
            self.assertIn("Kag-source-lift tree pilot migration", landing_log)
            self.assertIn("accepted the `kag-source-lift` direct-read migration review", changelog)
            self.assertIn("moved `AOA-T-0018`, `AOA-T-0019", changelog)
            self.assertIn(
                "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
                root_roadmap,
            )
            self.assertIn("Kag-Source-Lift Direct-Read Migration Review", tree_contract)
            self.assertIn("AOA-T-0018`, `AOA-T-0019", tree_contract)
            self.assertIn("2026-05-04-kag-source-lift-tree-pilot.md", tree_contract)

    def test_kag_source_lift_tree_pilot_migration_is_landed_after_direct_read(self) -> None:
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

            self.assertIn("kag-source-lift migration: landed", ingress)
            self.assertIn("techniques/knowledge-lift/kag-source-lift/", ingress)
            self.assertIn("without frontmatter changes", ingress)
            self.assertIn("landed `kag-source-lift` pilot review", ingress)
            self.assertIn("sixth pilot migration is now", distillation_roadmap)
            self.assertIn("techniques/knowledge-lift/kag-source-lift/", distillation_roadmap)
            self.assertIn("Kag-source-lift tree pilot migration", landing_log)
            self.assertIn("legacy/receipts/2026-05-04-kag-source-lift-tree-pilot.md", landing_log)
            self.assertIn("sixth landed pilot moved `AOA-T-0018`", root_roadmap)
            self.assertIn(
                "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
                root_roadmap,
            )
            self.assertIn("2026-05-04-kag-source-lift-tree-pilot.md", tree_contract)
            self.assertIn("moved `AOA-T-0018`, `AOA-T-0019", changelog)
            self.assertTrue(
                (
                    REPO_ROOT
                    / "techniques"
                    / "knowledge-lift"
                    / "kag-source-lift"
                    / "frontmatter-metadata-spine"
                    / "TECHNIQUE.md"
                ).is_file()
            )
            self.assertFalse(
                (
                    REPO_ROOT
                    / "techniques"
                    / "docs"
                    / "frontmatter-metadata-spine"
                ).exists()
            )

    def test_landed_kag_source_lift_pilot_review_selects_docs_boundary(self) -> None:
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
                / "landed-kag-source-lift-pilot-review.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Landed Kag-Source-Lift Pilot Review", review)
            self.assertIn("pilot-validated", review)
            self.assertIn("not path migration", review)
            self.assertIn("not `tree_path` frontmatter", review)
            self.assertIn("Accept the landed `kag-source-lift` pilot", review)
            self.assertIn("first `knowledge-lift` trunk test", review)
            self.assertIn("Choose `docs-boundary`", review)
            for technique_id in (
                "AOA-T-0018",
                "AOA-T-0019",
                "AOA-T-0020",
                "AOA-T-0021",
                "AOA-T-0022",
                "AOA-T-0046",
                "AOA-T-0047",
                "AOA-T-0048",
                "AOA-T-0002",
                "AOA-T-0009",
                "AOA-T-0034",
                "AOA-T-0033",
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)

            self.assertIn("KAG Name Edge", review)
            self.assertIn("Do not move `docs-boundary` from this review alone", review)
            self.assertIn("Do not treat `knowledge-lift` as `aoa-kag`", review)
            self.assertIn("Run a direct-read migration review for `docs-boundary`", review)

            self.assertIn("landed-kag-source-lift-pilot-review", reviews_index)
            self.assertIn("landed kag-source-lift pilot review: landed", ingress)
            self.assertIn("docs-boundary", ingress)
            self.assertIn("direct-read migration review", ingress)
            self.assertIn("`docs-boundary` for the next", distillation_roadmap)
            self.assertIn("Landed kag-source-lift pilot review", landing_log)
            self.assertIn("selected\n  `docs-boundary`", changelog)
            self.assertIn(
                "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
                root_roadmap,
            )
            self.assertIn("Landed Kag-Source-Lift Pilot Review", tree_contract)
            self.assertIn("docs-boundary", tree_contract)

    def test_docs_boundary_direct_read_review_accepts_seventh_pilot(self) -> None:
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
                / "docs-boundary-direct-read-migration-review.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Docs-Boundary Direct-Read Migration Review", review)
            self.assertIn("accepted-for-seventh-migration-pilot", review)
            self.assertIn("not path migration", review)
            self.assertIn("not\n`tree_path` frontmatter", review)
            self.assertIn("Accept `docs-boundary` as the seventh migration pilot", review)
            for technique_id in (
                "AOA-T-0002",
                "AOA-T-0009",
                "AOA-T-0034",
                "AOA-T-0033",
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)

            self.assertIn("Boundary Chain", review)
            self.assertIn("Instruction Trunk Fit", review)
            self.assertIn("Mixed Kind Stress", review)
            self.assertIn("Move exactly these four bundles", review)
            self.assertIn("techniques/instruction/docs-boundary/", review)
            self.assertIn("Do not move files from this review pack alone", review)
            self.assertIn("Do not add `family` or `tree_path` frontmatter", review)
            self.assertIn("Do not turn `docs-boundary` into source-of-truth governance", review)
            self.assertIn("Run the seventh pilot migration", review)

            self.assertIn("docs-boundary-direct-read-migration-review", reviews_index)
            self.assertIn("docs-boundary direct-read review: landed", ingress)
            self.assertIn("accepted-for-seventh-migration-pilot", ingress)
            self.assertIn("docs-boundary migration: landed", ingress)
            self.assertIn("accepted-for-seventh-migration-pilot", distillation_roadmap)
            self.assertIn("The seventh pilot migration is now landed", distillation_roadmap)
            self.assertIn("Docs-boundary direct-read migration review", landing_log)
            self.assertIn("accepted the `docs-boundary` direct-read migration review", changelog)
            self.assertIn("moved `AOA-T-0002`, `AOA-T-0009", changelog)
            self.assertIn(
                "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
                root_roadmap,
            )
            self.assertIn("Docs-Boundary Direct-Read Migration Review", tree_contract)
            self.assertIn("AOA-T-0002`, `AOA-T-0009", tree_contract)
            self.assertIn("2026-05-04-docs-boundary-tree-pilot.md", tree_contract)
            self.assertTrue(
                (
                    REPO_ROOT
                    / "techniques"
                    / "instruction"
                    / "docs-boundary"
                    / "source-of-truth-layout"
                    / "TECHNIQUE.md"
                ).is_file()
            )
            self.assertFalse(
                (
                    REPO_ROOT
                    / "techniques"
                    / "docs"
                    / "source-of-truth-layout"
                ).exists()
            )

    def test_docs_boundary_tree_pilot_migration_is_landed_after_direct_read(self) -> None:
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

            self.assertIn("docs-boundary migration: landed", ingress)
            self.assertIn("techniques/instruction/docs-boundary/", ingress)
            self.assertIn("without frontmatter changes", ingress)
            self.assertIn("landed docs-boundary pilot review", ingress)
            self.assertIn("seventh pilot migration is now landed", distillation_roadmap)
            self.assertIn("techniques/instruction/docs-boundary/", distillation_roadmap)
            self.assertIn("Docs-boundary tree pilot migration", landing_log)
            self.assertIn("legacy/receipts/2026-05-04-docs-boundary-tree-pilot.md", landing_log)
            self.assertIn("seventh landed pilot moved `AOA-T-0002`", root_roadmap)
            self.assertIn(
                "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
                root_roadmap,
            )
            self.assertIn("2026-05-04-docs-boundary-tree-pilot.md", tree_contract)
            self.assertIn("moved `AOA-T-0002`, `AOA-T-0009", changelog)
            self.assertTrue(
                (
                    REPO_ROOT
                    / "techniques"
                    / "instruction"
                    / "docs-boundary"
                    / "decision-rationale-recording"
                    / "TECHNIQUE.md"
                ).is_file()
            )
            self.assertFalse(
                (
                    REPO_ROOT
                    / "techniques"
                    / "docs"
                    / "decision-rationale-recording"
                ).exists()
            )

    def test_landed_docs_boundary_pilot_review_selects_capability_registry(
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
                / "landed-docs-boundary-pilot-review.md"
            ).read_text(encoding="utf-8")
            distillation_roadmap = read_distillation_reform_context()
            landing_log = (
                REPO_ROOT / "mechanics" / "distillation" / "LANDING_LOG.md"
            ).read_text(encoding="utf-8")
            root_roadmap = TREE_MIGRATION_BREADCRUMB_ROADMAP.read_text(encoding="utf-8")
            tree_contract = read_tree_migration_context()
            changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

            self.assertIn("Landed Docs-Boundary Pilot Review", review)
            self.assertIn("pilot-validated", review)
            self.assertIn("not path migration", review)
            self.assertIn("not `tree_path` frontmatter", review)
            self.assertIn("Accept the landed `docs-boundary` pilot", review)
            self.assertIn(
                "second successful shelf under the `instruction` trunk",
                review,
            )
            self.assertIn("Choose `capability-registry`", review)
            for technique_id in (
                "AOA-T-0002",
                "AOA-T-0009",
                "AOA-T-0034",
                "AOA-T-0033",
                "AOA-T-0025",
                "AOA-T-0063",
                "AOA-T-0064",
            ):
                with self.subTest(technique_id=technique_id):
                    self.assertIn(technique_id, review)

            self.assertIn(
                "Do not move `capability-registry` from this review alone",
                review,
            )
            self.assertIn("registry product doctrine", review)
            self.assertIn(
                "Run a direct-read migration review for `capability-registry`",
                review,
            )

            self.assertIn("landed-docs-boundary-pilot-review", reviews_index)
            self.assertIn("landed docs-boundary pilot review: landed", ingress)
            self.assertIn("capability-registry", ingress)
            self.assertIn("direct-read migration review", ingress)
            self.assertIn("`capability-registry` for the next", distillation_roadmap)
            self.assertIn(
                "eighth pilot migration is landed",
                distillation_roadmap,
            )
            self.assertIn("Landed docs-boundary pilot review", landing_log)
            self.assertIn("second successful instruction trunk shelf", landing_log)
            self.assertIn("selected\n  `capability-registry`", changelog)
            self.assertIn(
                "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf",
                root_roadmap,
            )
            self.assertIn("Landed Docs-Boundary Pilot Review", tree_contract)
            self.assertIn("capability-registry", tree_contract)


if __name__ == "__main__":
    unittest.main()
