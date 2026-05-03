from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

ACTIVE_BOUNDARY_BRIDGE_SURFACES = (
    "mechanics/boundary-bridge/AGENTS.md",
    "mechanics/boundary-bridge/README.md",
    "mechanics/boundary-bridge/DIRECTION.md",
    "mechanics/boundary-bridge/PARTS.md",
    "mechanics/boundary-bridge/PROVENANCE.md",
    "mechanics/boundary-bridge/LANDING_LOG.md",
    "mechanics/boundary-bridge/ROADMAP.md",
    "mechanics/boundary-bridge/parts/AGENTS.md",
    "mechanics/boundary-bridge/parts/README.md",
)

PART_LOCAL_BOUNDARY_BRIDGE_READMES = (
    "mechanics/boundary-bridge/parts/owner-boundary-anchors/README.md",
    "mechanics/boundary-bridge/parts/derived-projection-anchors/README.md",
    "mechanics/boundary-bridge/parts/proof-claim-anchors/README.md",
)


class BoundaryBridgeMechanicsTopologyTestCase(unittest.TestCase):
    def test_boundary_bridge_active_surfaces_are_discoverable(self) -> None:
        for relative_path in (
            ACTIVE_BOUNDARY_BRIDGE_SURFACES + PART_LOCAL_BOUNDARY_BRIDGE_READMES
        ):
            with self.subTest(relative_path=relative_path):
                self.assertTrue((REPO_ROOT / relative_path).is_file())

    def test_boundary_bridge_part_map_names_all_current_parts(self) -> None:
        parts = (
            REPO_ROOT / "mechanics" / "boundary-bridge" / "PARTS.md"
        ).read_text(encoding="utf-8")
        provenance = (
            REPO_ROOT / "mechanics" / "boundary-bridge" / "PROVENANCE.md"
        ).read_text(encoding="utf-8")

        for part_name in (
            "owner-boundary-anchors",
            "derived-projection-anchors",
            "proof-claim-anchors",
        ):
            with self.subTest(part_name=part_name):
                self.assertIn(part_name, parts)
                self.assertIn(part_name, provenance)

    def test_boundary_bridge_stays_outside_direct_orq_lane(self) -> None:
        receipts = (REPO_ROOT / "mechanics" / "REQUEST_RECEIPTS.md").read_text(
            encoding="utf-8"
        )
        direct_section = receipts.split("## Non-ORQ Center Pressure", 1)[0]
        non_orq_section = receipts.split("## Non-ORQ Center Pressure", 1)[1]
        compact_non_orq = " ".join(non_orq_section.split())

        self.assertNotIn("ORQ-BRIDGE-TECHNIQUES", direct_section)
        self.assertIn(
            "### [boundary-bridge](boundary-bridge/README.md)",
            non_orq_section,
        )
        self.assertIn("Current status: `candidate-only`", non_orq_section)
        self.assertIn(
            "direct `ORQ-BRIDGE-TECHNIQUES-*` request",
            compact_non_orq,
        )
        for phrase in (
            "owner acceptance",
            "identity between bridged surfaces",
            "Tree-of-Sophia canon",
            "source interpretation",
            "derived projection as source truth",
            "routing authority",
            "SDK authority",
            "memory authority",
            "runtime authority",
            "public projection authority",
            "proof before `aoa-evals` or the source owner lands evidence",
            "generated companion authority",
            "automatic technique promotion",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, compact_non_orq)

    def test_owner_boundary_anchors_point_to_bundle_local_homes(self) -> None:
        anchors = (
            REPO_ROOT
            / "mechanics"
            / "boundary-bridge"
            / "parts"
            / "owner-boundary-anchors"
            / "README.md"
        ).read_text(encoding="utf-8")

        for technique_id in ("AOA-T-0076", "AOA-T-0090", "AOA-T-0016", "AOA-T-0094"):
            with self.subTest(technique_id=technique_id):
                self.assertIn(technique_id, anchors)

        self.assertIn("does not change technique status", anchors)
        self.assertIn("owner acceptance", anchors)
        self.assertIn("techniques/**/TECHNIQUE.md", anchors)

    def test_derived_projection_anchors_preserve_source_authority(self) -> None:
        anchors = (
            REPO_ROOT
            / "mechanics"
            / "boundary-bridge"
            / "parts"
            / "derived-projection-anchors"
            / "README.md"
        ).read_text(encoding="utf-8")

        for expected in (
            "KAG Source Lift Guide",
            "KAG Export",
            "AOA-T-0043",
            "AOA-T-0021",
            "AOA-T-0046",
            "AOA-T-0018",
            "derived projection as source truth",
            "generated companions as authority",
        ):
            with self.subTest(expected=expected):
                self.assertIn(expected, anchors)

    def test_proof_claim_anchors_do_not_issue_proof(self) -> None:
        anchors = (
            REPO_ROOT
            / "mechanics"
            / "boundary-bridge"
            / "parts"
            / "proof-claim-anchors"
            / "README.md"
        ).read_text(encoding="utf-8")

        for expected in (
            "AOA-T-0015",
            "AOA-T-0068",
            "AOA-T-0092",
            "AOA-T-0093",
            "aoa-evals",
            "Do not issue proof verdicts",
            "generated companions",
        ):
            with self.subTest(expected=expected):
                self.assertIn(expected, anchors)

    def test_boundary_bridge_does_not_create_legacy_raw_without_source_receipts(self) -> None:
        provenance = (
            REPO_ROOT / "mechanics" / "boundary-bridge" / "PROVENANCE.md"
        ).read_text(encoding="utf-8")

        self.assertFalse(
            (REPO_ROOT / "mechanics" / "boundary-bridge" / "legacy").exists()
        )
        self.assertIn("does not create `legacy/raw/`", provenance)
        self.assertIn("no local pre-split", provenance)

    def test_boundary_bridge_stop_lines_remain_explicit(self) -> None:
        direction = (
            REPO_ROOT / "mechanics" / "boundary-bridge" / "DIRECTION.md"
        ).read_text(encoding="utf-8")
        roadmap = (
            REPO_ROOT / "mechanics" / "boundary-bridge" / "ROADMAP.md"
        ).read_text(encoding="utf-8")
        compact_direction = " ".join(direction.split())
        compact_roadmap = " ".join(roadmap.split())

        for phrase in (
            "owner acceptance",
            "identity between bridged surfaces",
            "Tree-of-Sophia canon",
            "source interpretation",
            "derived projection as source truth",
            "routing authority",
            "SDK authority",
            "memory authority",
            "runtime authority",
            "public projection authority",
            "generated companion authority",
            "proof before `aoa-evals` or the source owner lands evidence",
            "automatic technique promotion",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, compact_direction)
                self.assertIn(phrase, compact_roadmap)


if __name__ == "__main__":
    unittest.main()
