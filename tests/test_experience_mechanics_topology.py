from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

ACTIVE_EXPERIENCE_SURFACES = (
    "mechanics/experience/AGENTS.md",
    "mechanics/experience/README.md",
    "mechanics/experience/DIRECTION.md",
    "mechanics/experience/PARTS.md",
    "mechanics/experience/PROVENANCE.md",
    "mechanics/experience/LANDING_LOG.md",
    "mechanics/experience/ROADMAP.md",
    "mechanics/experience/parts/AGENTS.md",
    "mechanics/experience/parts/README.md",
)

PART_LOCAL_EXPERIENCE_READMES = (
    "mechanics/experience/parts/governance-precedent/README.md",
    "mechanics/experience/parts/authority-resolution/README.md",
    "mechanics/experience/parts/appeal-reasoning/README.md",
    "mechanics/experience/parts/sealed-decision/README.md",
    "mechanics/experience/parts/scope-boundary/README.md",
    "mechanics/experience/parts/handoff-compression/README.md",
    "mechanics/experience/parts/service-clarity/README.md",
    "mechanics/experience/parts/technique-candidate-bridge/README.md",
)

OLD_FLAT_EXPERIENCE_FILES = (
    "mechanics/experience/GOVERNANCE_TECHNIQUE_PRECEDENT.md",
    "mechanics/experience/AUTHORITY_RESOLUTION_TECHNIQUES.md",
    "mechanics/experience/APPEAL_REASONING_TECHNIQUES.md",
    "mechanics/experience/SEALED_DECISION_TECHNIQUES.md",
    "mechanics/experience/SCOPE_BOUNDARY_TECHNIQUE.md",
    "mechanics/experience/HANDOFF_COMPRESSION_TECHNIQUE.md",
    "mechanics/experience/SERVICE_CLARITY_TECHNIQUE.md",
)

EXPERIENCE_CONTRACT_PACKETS = (
    (
        "mechanics/experience/parts/appeal-reasoning/schemas/appeal_reasoning_step_v1.json",
        "mechanics/experience/parts/appeal-reasoning/examples/appeal_reasoning_step.example.json",
        "schemas/appeal_reasoning_step_v1.json",
        "examples/appeal_reasoning_step.example.json",
    ),
    (
        "mechanics/experience/parts/governance-precedent/schemas/technique_governance_precedent_v1.json",
        "mechanics/experience/parts/governance-precedent/examples/technique_governance_precedent.example.json",
        "schemas/technique_governance_precedent_v1.json",
        "examples/technique_governance_precedent.example.json",
    ),
    (
        "mechanics/experience/parts/sealed-decision/schemas/sealed_decision_technique_note_v1.json",
        "mechanics/experience/parts/sealed-decision/examples/sealed_decision_technique_note_v1.example.json",
        "schemas/sealed_decision_technique_note_v1.json",
        "examples/sealed_decision_technique_note_v1.example.json",
    ),
    (
        "mechanics/experience/parts/scope-boundary/schemas/scope_boundary_technique_note_v1.json",
        "mechanics/experience/parts/scope-boundary/examples/scope_boundary_technique_note_v1.example.json",
        "schemas/scope_boundary_technique_note_v1.json",
        "examples/scope_boundary_technique_note_v1.example.json",
    ),
    (
        "mechanics/experience/parts/handoff-compression/schemas/handoff_compression_technique_note_v1.json",
        "mechanics/experience/parts/handoff-compression/examples/handoff_compression_technique_note_v1.example.json",
        "schemas/handoff_compression_technique_note_v1.json",
        "examples/handoff_compression_technique_note_v1.example.json",
    ),
    (
        "mechanics/experience/parts/service-clarity/schemas/service_clarity_technique_note_v1.json",
        "mechanics/experience/parts/service-clarity/examples/service_clarity_technique_note_v1.example.json",
        "schemas/service_clarity_technique_note_v1.json",
        "examples/service_clarity_technique_note_v1.example.json",
    ),
)


class ExperienceMechanicsTopologyTestCase(unittest.TestCase):
    def test_experience_active_surfaces_are_discoverable(self) -> None:
        for relative_path in ACTIVE_EXPERIENCE_SURFACES + PART_LOCAL_EXPERIENCE_READMES:
            with self.subTest(relative_path=relative_path):
                self.assertTrue((REPO_ROOT / relative_path).is_file())

    def test_experience_flat_files_moved_into_owning_parts(self) -> None:
        for relative_path in OLD_FLAT_EXPERIENCE_FILES:
            with self.subTest(relative_path=relative_path):
                self.assertFalse((REPO_ROOT / relative_path).exists())

    def test_experience_contract_packets_live_under_parts(self) -> None:
        for schema_path, example_path, old_schema_path, old_example_path in (
            EXPERIENCE_CONTRACT_PACKETS
        ):
            with self.subTest(schema_path=schema_path):
                self.assertTrue((REPO_ROOT / schema_path).is_file())
                self.assertTrue((REPO_ROOT / example_path).is_file())
                self.assertFalse((REPO_ROOT / old_schema_path).exists())
                self.assertFalse((REPO_ROOT / old_example_path).exists())

    def test_experience_contract_packet_routes_are_documented(self) -> None:
        parts = (REPO_ROOT / "mechanics" / "experience" / "PARTS.md").read_text(
            encoding="utf-8"
        )
        provenance = (
            REPO_ROOT / "mechanics" / "experience" / "PROVENANCE.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "experience" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")

        self.assertIn("Part-Local Contract Packets", parts)
        self.assertIn("Contract Packet Bridge", provenance)

        for required in (
            "appeal_reasoning_step_v1.json",
            "technique_governance_precedent_v1.json",
            "sealed_decision_technique_note_v1.json",
            "scope_boundary_technique_note_v1.json",
            "handoff_compression_technique_note_v1.json",
            "service_clarity_technique_note_v1.json",
        ):
            with self.subTest(required=required):
                self.assertIn(required, parts)
                self.assertIn(required, provenance)

        self.assertIn("Contract Packet Part Homes", landing_log)
        self.assertIn("public part-local\n  schema URLs", landing_log)

    def test_experience_part_map_names_all_current_parts(self) -> None:
        parts = (REPO_ROOT / "mechanics" / "experience" / "PARTS.md").read_text(
            encoding="utf-8"
        )
        provenance = (
            REPO_ROOT / "mechanics" / "experience" / "PROVENANCE.md"
        ).read_text(encoding="utf-8")

        for part_name in (
            "governance-precedent",
            "authority-resolution",
            "appeal-reasoning",
            "sealed-decision",
            "scope-boundary",
            "handoff-compression",
            "service-clarity",
            "technique-candidate-bridge",
        ):
            with self.subTest(part_name=part_name):
                self.assertIn(part_name, parts)
                self.assertIn(part_name, provenance)

    def test_experience_candidate_bridge_preserves_extraction_gate(self) -> None:
        bridge = (
            REPO_ROOT
            / "mechanics"
            / "experience"
            / "parts"
            / "technique-candidate-bridge"
            / "README.md"
        ).read_text(encoding="utf-8")

        for required in (
            "extract_watch",
            "narrow_more",
            "hold_overlap",
            "authority-resolution",
            "sealed-decision",
            "governance-precedent",
            "handoff-compression",
            "no automatic technique promotion",
            "capability-authority-separation-check",
        ):
            with self.subTest(required=required):
                self.assertIn(required, bridge)

    def test_request_receipt_points_to_experience_parts_without_runtime_authority(self) -> None:
        receipts = (REPO_ROOT / "mechanics" / "REQUEST_RECEIPTS.md").read_text(
            encoding="utf-8"
        )
        experience_section = receipts.split("### `ORQ-EXPERIENCE-TECHNIQUES-001`", 1)[
            1
        ].split("## Non-ORQ Center Pressure", 1)[0]

        self.assertIn("Governance Precedent", experience_section)
        self.assertIn("Handoff Compression", experience_section)
        self.assertIn("Technique Candidate Bridge", experience_section)
        self.assertIn("candidate extraction now routes through", experience_section)
        self.assertIn("portable practice stops before live office activation", experience_section)
        self.assertIn("runtime truth", experience_section)
        self.assertIn("ToS write authority", experience_section)
        self.assertIn("technique canon lands only", experience_section)


if __name__ == "__main__":
    unittest.main()
