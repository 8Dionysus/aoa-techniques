from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

ACTIVE_METHOD_GROWTH_SURFACES = (
    "mechanics/method-growth/AGENTS.md",
    "mechanics/method-growth/README.md",
    "mechanics/method-growth/DIRECTION.md",
    "mechanics/method-growth/PARTS.md",
    "mechanics/method-growth/PROVENANCE.md",
    "mechanics/method-growth/LANDING_LOG.md",
    "mechanics/method-growth/ROADMAP.md",
    "mechanics/method-growth/parts/AGENTS.md",
    "mechanics/method-growth/parts/README.md",
)

PART_LOCAL_METHOD_GROWTH_READMES = (
    "mechanics/method-growth/parts/pattern-adoption/README.md",
    "mechanics/method-growth/parts/adoption-boundaries/README.md",
    "mechanics/method-growth/parts/technique-to-skill-handoff/README.md",
    "mechanics/method-growth/parts/retention-checks/README.md",
    "mechanics/method-growth/parts/obsolescence/README.md",
)

OLD_FLAT_METHOD_GROWTH_FILES = (
    "mechanics/method-growth/TECHNIQUE_PATTERN_ADOPTION.md",
    "mechanics/method-growth/TECHNIQUE_ADOPTION_BOUNDARIES.md",
    "mechanics/method-growth/TECHNIQUE_TO_SKILL_HANDOFF.md",
    "mechanics/method-growth/TECHNIQUE_RETENTION_CHECKS.md",
    "mechanics/method-growth/TECHNIQUE_OBSOLESCENCE.md",
)

METHOD_GROWTH_CONTRACT_PACKETS = (
    (
        "mechanics/method-growth/parts/pattern-adoption/schemas/technique_pattern_adoption_note_v1.json",
        "mechanics/method-growth/parts/pattern-adoption/examples/technique_pattern_adoption_note.example.json",
        "schemas/technique_pattern_adoption_note_v1.json",
        "examples/technique_pattern_adoption_note.example.json",
    ),
    (
        "mechanics/method-growth/parts/adoption-boundaries/schemas/technique_adoption_boundary_check_v1.json",
        "mechanics/method-growth/parts/adoption-boundaries/examples/technique_adoption_boundary_check.example.json",
        "schemas/technique_adoption_boundary_check_v1.json",
        "examples/technique_adoption_boundary_check.example.json",
    ),
    (
        "mechanics/method-growth/parts/technique-to-skill-handoff/schemas/technique_to_skill_handoff_v1.json",
        "mechanics/method-growth/parts/technique-to-skill-handoff/examples/technique_to_skill_handoff.example.json",
        "schemas/technique_to_skill_handoff_v1.json",
        "examples/technique_to_skill_handoff.example.json",
    ),
    (
        "mechanics/method-growth/parts/retention-checks/schemas/technique_retention_probe_v1.json",
        "mechanics/method-growth/parts/retention-checks/examples/technique_retention_probe.example.json",
        "schemas/technique_retention_probe_v1.json",
        "examples/technique_retention_probe.example.json",
    ),
    (
        "mechanics/method-growth/parts/obsolescence/schemas/technique_obsolescence_notice_v1.json",
        "mechanics/method-growth/parts/obsolescence/examples/technique_obsolescence_notice.example.json",
        "schemas/technique_obsolescence_notice_v1.json",
        "examples/technique_obsolescence_notice.example.json",
    ),
)


class MethodGrowthMechanicsTopologyTestCase(unittest.TestCase):
    def test_method_growth_active_surfaces_are_discoverable(self) -> None:
        for relative_path in ACTIVE_METHOD_GROWTH_SURFACES + PART_LOCAL_METHOD_GROWTH_READMES:
            with self.subTest(relative_path=relative_path):
                self.assertTrue((REPO_ROOT / relative_path).is_file())

    def test_method_growth_flat_files_moved_into_owning_parts(self) -> None:
        for relative_path in OLD_FLAT_METHOD_GROWTH_FILES:
            with self.subTest(relative_path=relative_path):
                self.assertFalse((REPO_ROOT / relative_path).exists())

    def test_method_growth_contract_packets_live_under_parts(self) -> None:
        for schema_path, example_path, old_schema_path, old_example_path in (
            METHOD_GROWTH_CONTRACT_PACKETS
        ):
            with self.subTest(schema_path=schema_path):
                self.assertTrue((REPO_ROOT / schema_path).is_file())
                self.assertTrue((REPO_ROOT / example_path).is_file())
                self.assertFalse((REPO_ROOT / old_schema_path).exists())
                self.assertFalse((REPO_ROOT / old_example_path).exists())

    def test_method_growth_contract_packet_routes_are_documented(self) -> None:
        parts = (
            REPO_ROOT / "mechanics" / "method-growth" / "PARTS.md"
        ).read_text(encoding="utf-8")
        provenance = (
            REPO_ROOT / "mechanics" / "method-growth" / "PROVENANCE.md"
        ).read_text(encoding="utf-8")
        landing_log = (
            REPO_ROOT / "mechanics" / "method-growth" / "LANDING_LOG.md"
        ).read_text(encoding="utf-8")

        self.assertIn("Part-Local Contract Packets", parts)
        self.assertIn("Contract Packet Bridge", provenance)

        for required in (
            "technique_pattern_adoption_note_v1.json",
            "technique_adoption_boundary_check_v1.json",
            "technique_to_skill_handoff_v1.json",
            "technique_retention_probe_v1.json",
            "technique_obsolescence_notice_v1.json",
        ):
            with self.subTest(required=required):
                self.assertIn(required, parts)
                self.assertIn(required, provenance)

        self.assertIn("Contract Packet Part Homes", landing_log)
        self.assertIn("public part-local\n  schema URLs", landing_log)

    def test_method_growth_part_map_names_all_current_parts(self) -> None:
        parts = (REPO_ROOT / "mechanics" / "method-growth" / "PARTS.md").read_text(
            encoding="utf-8"
        )
        provenance = (
            REPO_ROOT / "mechanics" / "method-growth" / "PROVENANCE.md"
        ).read_text(encoding="utf-8")

        for part_name in (
            "pattern-adoption",
            "adoption-boundaries",
            "technique-to-skill-handoff",
            "retention-checks",
            "obsolescence",
        ):
            with self.subTest(part_name=part_name):
                self.assertIn(part_name, parts)
                self.assertIn(part_name, provenance)

    def test_request_receipt_points_to_method_growth_parts(self) -> None:
        receipts = (REPO_ROOT / "mechanics" / "REQUEST_RECEIPTS.md").read_text(
            encoding="utf-8"
        )
        method_section = receipts.split("### `ORQ-METHOD-TECHNIQUES-001`", 1)[1].split(
            "### `ORQ-DISTILLATION-TECHNIQUES-001`",
            1,
        )[0]

        self.assertIn("Local status: `mapped-with-local-evidence`", method_section)
        self.assertIn("Pattern Adoption", method_section)
        self.assertIn("Technique To Skill Handoff", method_section)
        self.assertIn("skill acceptance", method_section)
        self.assertIn("technique canon lands only", method_section)

    def test_pattern_adoption_routes_to_extracted_atom_without_lifecycle_collapse(self) -> None:
        pattern = (
            REPO_ROOT
            / "mechanics"
            / "method-growth"
            / "parts"
            / "pattern-adoption"
            / "README.md"
        ).read_text(encoding="utf-8")
        provenance = (
            REPO_ROOT / "mechanics" / "method-growth" / "PROVENANCE.md"
        ).read_text(encoding="utf-8")
        technique = (
            REPO_ROOT
            / "techniques"
            / "governance"
            / "practice-adoption-lifecycle"
            / "local-pattern-adoption-gate"
            / "TECHNIQUE.md"
        ).read_text(encoding="utf-8")

        self.assertIn("AOA-T-0101 local-pattern-adoption-gate", pattern)
        self.assertIn("request, readiness,\nshadow, decision, activation, and retention", pattern)
        self.assertIn("The wider Method-growth lifecycle", provenance)
        self.assertIn("upstream approval or useful precedent is not local adoption", technique)
        self.assertIn("does not grant skill activation", technique)

    def test_technique_to_skill_handoff_routes_to_packet_without_skill_acceptance(self) -> None:
        handoff = (
            REPO_ROOT
            / "mechanics"
            / "method-growth"
            / "parts"
            / "technique-to-skill-handoff"
            / "README.md"
        ).read_text(encoding="utf-8")
        provenance = (
            REPO_ROOT / "mechanics" / "method-growth" / "PROVENANCE.md"
        ).read_text(encoding="utf-8")
        technique = (
            REPO_ROOT
            / "techniques"
            / "governance"
            / "promotion-boundary"
            / "skill-proposal-handoff-packet"
            / "TECHNIQUE.md"
        ).read_text(encoding="utf-8")

        self.assertIn("AOA-T-0102 skill-proposal-handoff-packet", handoff)
        self.assertIn("does not create, accept, install, or activate a skill", handoff)
        self.assertIn("proposal packet sent from technique-side review", provenance)
        self.assertIn("Skill acceptance, skill workflow meaning, and activation", provenance)
        self.assertIn("a packet may reference technique dependencies", technique)
        self.assertIn("not skill acceptance, skill creation, skill activation", technique)

    def test_retention_checks_route_to_review_without_obsolescence_collapse(self) -> None:
        retention = (
            REPO_ROOT
            / "mechanics"
            / "method-growth"
            / "parts"
            / "retention-checks"
            / "README.md"
        ).read_text(encoding="utf-8")
        provenance = (
            REPO_ROOT / "mechanics" / "method-growth" / "PROVENANCE.md"
        ).read_text(encoding="utf-8")
        technique = (
            REPO_ROOT
            / "techniques"
            / "governance"
            / "practice-adoption-lifecycle"
            / "adopted-practice-retention-review"
            / "TECHNIQUE.md"
        ).read_text(encoding="utf-8")

        self.assertIn("AOA-T-0103 adopted-practice-retention-review", retention)
        self.assertIn("does not adopt, delete, deprecate", retention)
        self.assertIn("decides whether one adopted or shadowed practice should remain active", provenance)
        self.assertIn("Obsolescence, proof, memory writeback", provenance)
        self.assertIn("past adoption does not guarantee current retention", technique)
        self.assertIn("does not adopt a new practice, delete an old practice", technique)

    def test_obsolescence_routes_to_packet_without_erasure_or_deletion(self) -> None:
        obsolescence = (
            REPO_ROOT
            / "mechanics"
            / "method-growth"
            / "parts"
            / "obsolescence"
            / "README.md"
        ).read_text(encoding="utf-8")
        provenance = (
            REPO_ROOT / "mechanics" / "method-growth" / "PROVENANCE.md"
        ).read_text(encoding="utf-8")
        technique = (
            REPO_ROOT
            / "techniques"
            / "governance"
            / "practice-adoption-lifecycle"
            / "superseded-practice-obsolescence-route"
            / "TECHNIQUE.md"
        ).read_text(encoding="utf-8")

        self.assertIn("AOA-T-0104 superseded-practice-obsolescence-route", obsolescence)
        self.assertIn("does not delete, deprecate, erase evidence", obsolescence)
        self.assertIn("owner-aware\n  route packet", provenance)
        self.assertIn("Actual\n  deletion, deprecation execution", provenance)
        self.assertIn("obsolescence is not erasure", technique)
        self.assertIn("a dropped route is not owner-local deletion", technique)


if __name__ == "__main__":
    unittest.main()
