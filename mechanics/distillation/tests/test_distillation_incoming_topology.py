from __future__ import annotations

import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
ROOT_INCOMING = REPO_ROOT / "incoming"
INCOMING_ROOT = (
    REPO_ROOT / "mechanics" / "distillation" / "parts" / "candidate-intake"
)
LEGACY_PACKET_ROOT = (
    REPO_ROOT
    / "mechanics"
    / "distillation"
    / "legacy"
    / "archive"
    / "closed-incoming-packets"
)

EXPECTED_PACKETS = {
    "chat-graph-review-mailbox",
    "chat-handoff-bounded-continuation",
    "chat-history-lineage-governed-actions",
    "chat-registry-discovery",
    "chat-tool-proxy-runtime",
    "personal-media-ingest",
}

EXPECTED_NON_LANDED = {
    "markdown-definition-of-done-defaults": "closed-no-import",
    "shadow-epic-federation": "explicit-exclusion",
    "typed-governance-obligation-ledger": "explicit-exclusion",
    "governed-action-surfaces": "explicit-exclusion",
    "cross-agent-session-browser": "explicit-exclusion",
    "why-retrieval-from-code": "explicit-exclusion",
    "agent-readiness-telemetry": "closed-no-import",
    "signed-trace-artifacts": "closed-no-import",
    "semantic-linkage-records": "closed-no-import",
    "well-known-skill-discovery": "explicit-exclusion",
    "versioned-skill-package-manifest": "explicit-exclusion",
    "source-manifest-sync": "explicit-exclusion",
    "universal-skill-loader": "explicit-exclusion",
    "progressive-skill-loading": "explicit-exclusion",
    "lifecycle-managed-tool-proxy": "explicit-exclusion",
    "preflight-reputation-check": "closed-no-import",
    "isolated-stateful-agent-runtime": "explicit-exclusion",
    "bounded-single-step-agent": "explicit-exclusion",
    "confirm-before-tool-execution": "explicit-exclusion",
    "review-gated-multi-agent-orchestration": "explicit-exclusion",
    "recursive-orchestrator-pattern": "explicit-exclusion",
    "telegram-account-auth-and-session-bridge": "closed-no-import",
}

FORBIDDEN_LIVE_DEBT_MARKERS = (
    "narrowing-only",
    "narrow-first",
    "incubation-hold",
    "incubation hold",
    "reopen",
    "reopening",
    "reopen gate",
    "reopen gates",
)


class IncomingTopologyTestCase(unittest.TestCase):
    def test_root_incoming_directory_is_retired(self) -> None:
        self.assertFalse(ROOT_INCOMING.exists())

    def test_incoming_root_is_active_intake_only(self) -> None:
        active_packet_dirs = {
            path.name
            for path in INCOMING_ROOT.iterdir()
            if path.is_dir() and not path.name.startswith(".")
        }
        self.assertEqual(set(), active_packet_dirs)

    def test_closed_packet_roots_are_distillation_legacy_evidence(self) -> None:
        packet_dirs = {
            path.name
            for path in LEGACY_PACKET_ROOT.iterdir()
            if path.is_dir() and not path.name.startswith(".")
        }
        self.assertEqual(EXPECTED_PACKETS, packet_dirs)

        for packet in sorted(EXPECTED_PACKETS):
            manifest_path = LEGACY_PACKET_ROOT / packet / "support" / "manifest.json"
            with self.subTest(packet=packet):
                manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                self.assertEqual("evidence-only", manifest["activation_state"])

    def test_no_packet_local_candidate_bundles_remain(self) -> None:
        candidate_bundle_paths = [
            *INCOMING_ROOT.glob("**/candidate_bundles/**"),
            *LEGACY_PACKET_ROOT.glob("**/candidate_bundles/**"),
        ]
        self.assertEqual([], candidate_bundle_paths)

    def test_registries_do_not_claim_live_seed_bundles(self) -> None:
        non_landed: dict[str, str] = {}

        for registry_path in sorted(LEGACY_PACKET_ROOT.glob("*/support/registry.json")):
            registry = json.loads(registry_path.read_text(encoding="utf-8"))

            for row in registry:
                with self.subTest(
                    packet=registry_path.parents[1].name,
                    candidate=row["candidate_slug"],
                ):
                    self.assertFalse(row["candidate_bundle_present"])

                if row["status_lane"] != "landed":
                    non_landed[row["candidate_slug"]] = row["activation_state"]

        self.assertEqual(EXPECTED_NON_LANDED, non_landed)

    def test_incoming_root_names_closed_packet_stop_line(self) -> None:
        text = (INCOMING_ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("There are no active packet roots in this part.", text)
        self.assertIn("closed incoming packets", text)
        self.assertIn("new Distillation intake", text)
        self.assertIn("Do not use this part as a long-term archive", text)
        self.assertIn("## Packet Shape", text)

    def test_closed_archive_names_former_roots_without_claiming_active_intake(self) -> None:
        text = (LEGACY_PACKET_ROOT / "README.md").read_text(encoding="utf-8")

        for packet in EXPECTED_PACKETS:
            with self.subTest(packet=packet):
                self.assertIn(f"[{packet}]({packet}/README.md)", text)
                self.assertIn(f"`incoming/{packet}/`", text)

        self.assertIn("evidence, not active intake", text)

    def test_no_live_debt_markers_remain_in_current_intake_or_closed_archive(self) -> None:
        current_files = [
            path
            for root in (INCOMING_ROOT, LEGACY_PACKET_ROOT)
            for path in root.rglob("*")
            if path.is_file() and path.suffix in {".md", ".json"}
        ]

        for path in current_files:
            text = path.read_text(encoding="utf-8")
            for marker in FORBIDDEN_LIVE_DEBT_MARKERS:
                with self.subTest(path=path.relative_to(REPO_ROOT), marker=marker):
                    self.assertNotIn(marker, text)


if __name__ == "__main__":
    unittest.main()
