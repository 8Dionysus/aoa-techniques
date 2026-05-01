from __future__ import annotations

import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class MechanicsRequestReceiptsTestCase(unittest.TestCase):
    def test_request_receipts_names_direct_aoa_requests(self) -> None:
        receipts = (REPO_ROOT / "mechanics" / "REQUEST_RECEIPTS.md").read_text(
            encoding="utf-8"
        )
        compact_receipts = re.sub(r"\s+", " ", receipts)

        direct_section = receipts.split("## Non-ORQ Center Pressure", 1)[0]
        headings = re.findall(r"^### `([^`]+)`$", direct_section, flags=re.MULTILINE)

        self.assertEqual(
            [
                "ORQ-METHOD-TECHNIQUES-001",
                "ORQ-DISTILLATION-TECHNIQUES-001",
                "ORQ-EXPERIENCE-TECHNIQUES-001",
            ],
            headings,
        )
        self.assertIn("These statuses are local to this file", receipts)
        self.assertIn("They do not change AoA queue status", receipts)
        self.assertIn(
            "not proof that a center request is accepted or landed",
            compact_receipts,
        )

    def test_request_receipts_keeps_agon_outside_direct_orq_lane(self) -> None:
        receipts = (REPO_ROOT / "mechanics" / "REQUEST_RECEIPTS.md").read_text(
            encoding="utf-8"
        )

        non_orq_section = receipts.split("## Non-ORQ Center Pressure", 1)[1]
        self.assertIn("### [agon](agon/README.md)", non_orq_section)
        self.assertIn("Current status: `candidate-only`", non_orq_section)
        self.assertIn("no direct\n  `ORQ-AGON-TECHNIQUES-*` request", non_orq_section)
        self.assertNotIn("ORQ-AGON-TECHNIQUES", receipts.split("## Non-ORQ Center Pressure", 1)[0])

    def test_distillation_receipt_maps_owner_landing_readout(self) -> None:
        receipts = (REPO_ROOT / "mechanics" / "REQUEST_RECEIPTS.md").read_text(
            encoding="utf-8"
        )
        distillation_section = receipts.split("### `ORQ-DISTILLATION-TECHNIQUES-001`", 1)[
            1
        ].split("### `ORQ-EXPERIENCE-TECHNIQUES-001`", 1)[0]

        for expected in (
            "source intake lives in Donor Refinery",
            "active extraction lives in the external and cross-layer candidate ledgers",
            "noise pruning lives in donor exclusions",
            "provenance-preserving condensation lives in [Provenance]",
            "technique canon lands only when a real `techniques/**/TECHNIQUE.md` bundle",
        ):
            with self.subTest(expected=expected):
                self.assertIn(expected, distillation_section)

    def test_mechanics_routes_to_request_receipts_only_when_needed(self) -> None:
        agents = (REPO_ROOT / "mechanics" / "AGENTS.md").read_text(encoding="utf-8")
        readme = (REPO_ROOT / "mechanics" / "README.md").read_text(encoding="utf-8")

        self.assertIn("read `mechanics/REQUEST_RECEIPTS.md`", agents)
        self.assertIn("do not treat the request\n  packet as local acceptance or landing", agents)
        self.assertIn("[Owner Request Receipts](REQUEST_RECEIPTS.md)", readme)
        self.assertIn("not a copy of the AoA request queue", readme)


if __name__ == "__main__":
    unittest.main()
