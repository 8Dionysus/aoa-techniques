import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
MECHANICS_ROOT = REPO_ROOT / "mechanics"

PACKAGE_CARD_HEADINGS = [
    "## Mechanic card",
    "### Trigger",
    "### Local owns",
    "### Stronger owner split",
    "### Inputs",
    "### Outputs",
    "### Must not claim",
    "### Next route",
]

CARD_STATUS_MARKERS = {
    "agon": "candidate-only",
    "antifragility": "candidate-only",
    "boundary-bridge": "candidate-only",
    "checkpoint": "candidate-only",
    "distillation": "mapped-with-local-evidence",
    "experience": "mapped-with-local-evidence",
    "growth-cycle": "candidate-only",
    "method-growth": "mapped-with-local-evidence",
    "questbook": "candidate-only",
    "recurrence": "candidate-only",
    "release-support": "candidate-only",
    "rpg": "candidate-only",
}

ACTIVE_ROUTE_FILES = [
    "DIRECTION.md",
    "PARTS.md",
    "PROVENANCE.md",
    "LANDING_LOG.md",
    "ROADMAP.md",
]


class MechanicsPackageCardTests(unittest.TestCase):
    def test_mechanics_readme_defines_owner_local_card_standard(self) -> None:
        readme = (MECHANICS_ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("## Package Card Standard", readme)
        self.assertIn("`### Local owns`", readme)
        self.assertIn("This mirrors the AoA center mechanic-card shape", readme)
        self.assertIn("`REQUEST_RECEIPTS.md`", readme)
        self.assertIn("package `PROVENANCE.md`", readme)
        self.assertIn("Validation commands belong in the nearest `AGENTS.md`", readme)

    def test_mechanics_agents_routes_through_local_cards(self) -> None:
        agents = (MECHANICS_ROOT / "AGENTS.md").read_text(encoding="utf-8")

        self.assertIn("local `Mechanic card`", agents)
        self.assertIn("Package README cards use `Local owns`, not `Center owns`", agents)
        self.assertIn("Package README cards do not carry validation command lanes", agents)
        self.assertIn("`REQUEST_RECEIPTS.md`", agents)
        self.assertIn("`PROVENANCE.md`", agents)

    def test_package_card_decision_is_discoverable(self) -> None:
        decision = (
            REPO_ROOT
            / "docs"
            / "decisions"
            / "AOA-TECH-D-0026-mechanics-package-card-standard.md"
        ).read_text(encoding="utf-8")

        self.assertIn("Status: accepted", decision)
        self.assertIn("### Local owns", decision)
        self.assertIn("should mirror the local receipt posture", decision)
        self.assertIn("does not add package-local `OWNER_MAP.md`", decision)
        self.assertIn("mechanics/tests/test_mechanics_package_cards.py", decision)

    def test_every_mechanic_package_has_local_card_headings(self) -> None:
        package_dirs = sorted(
            path
            for path in MECHANICS_ROOT.iterdir()
            if path.is_dir() and path.name != "tests"
        )
        self.assertGreater(len(package_dirs), 0)

        for package_dir in package_dirs:
            readme = (package_dir / "README.md").read_text(encoding="utf-8")
            with self.subTest(package=package_dir.name):
                for heading in PACKAGE_CARD_HEADINGS:
                    self.assertIn(heading, readme)
                self.assertNotIn("### Center owns", readme)

                positions = [readme.index(heading) for heading in PACKAGE_CARD_HEADINGS]
                self.assertEqual(sorted(positions), positions)

    def test_package_card_status_matches_request_receipt_posture(self) -> None:
        receipts = (MECHANICS_ROOT / "REQUEST_RECEIPTS.md").read_text(
            encoding="utf-8"
        )

        for package_name, status_marker in CARD_STATUS_MARKERS.items():
            readme = (
                MECHANICS_ROOT / package_name / "README.md"
            ).read_text(encoding="utf-8")

            with self.subTest(package=package_name):
                self.assertIn(f"Status: {status_marker}", readme)
                self.assertIn(f"[{package_name}]", receipts)

        audit_readme = (MECHANICS_ROOT / "audit" / "README.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("Status: active", audit_readme)

    def test_package_cards_route_to_active_parts_and_route_files(self) -> None:
        package_dirs = sorted(
            path
            for path in MECHANICS_ROOT.iterdir()
            if path.is_dir() and path.name != "tests"
        )

        for package_dir in package_dirs:
            readme = (package_dir / "README.md").read_text(encoding="utf-8")
            parts_map = (package_dir / "PARTS.md").read_text(encoding="utf-8")
            part_dirs = sorted(
                path
                for path in (package_dir / "parts").iterdir()
                if path.is_dir()
            )

            with self.subTest(package=package_dir.name):
                for route_file in ACTIVE_ROUTE_FILES:
                    self.assertIn(route_file, readme)
                    self.assertTrue((package_dir / route_file).is_file())

                for part_dir in part_dirs:
                    part_route = f"parts/{part_dir.name}/README.md"
                    self.assertIn(part_route, readme)
                    self.assertIn(f"`{part_dir.name}`", parts_map)
                    self.assertTrue((part_dir / "README.md").is_file())


if __name__ == "__main__":
    unittest.main()
