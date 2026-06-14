from __future__ import annotations

import sys
from pathlib import Path

SUPPORT_DIR = Path(__file__).resolve().parent / "support"
if str(SUPPORT_DIR) not in sys.path:
    sys.path.insert(0, str(SUPPORT_DIR))

from validate_repo_fixtures import *


class ValidateRepoAgentsMeshTests(unittest.TestCase):
    def test_spark_lane_lives_under_agents_district(self) -> None:
        self.assertTrue((REPO_ROOT / ".agents" / "spark" / "AGENTS.md").is_file())
        self.assertTrue((REPO_ROOT / ".agents" / "spark" / "SWARM.md").is_file())
        self.assertTrue((REPO_ROOT / ".agents" / "spark" / "README.md").is_file())
        self.assertTrue((REPO_ROOT / ".agents" / "spark" / "registry.json").is_file())
        self.assertTrue(
            (REPO_ROOT / ".agents" / "spark" / "scripts" / "validate_spark_lane.py").is_file()
        )
        self.assertTrue(
            (REPO_ROOT / ".agents" / "spark" / "tests" / "test_spark_lane.py").is_file()
        )
        notebook = REPO_ROOT / ".agents" / "spark" / "SPARK_EXTRAPOLATION_NOTEBOOK.md"
        self.assertTrue(notebook.is_file())
        self.assertFalse((REPO_ROOT / "Spark").exists())

        root_law = (REPO_ROOT / "docs" / "ROOT_SURFACE_LAW.md").read_text(
            encoding="utf-8"
        )
        spark_agents = (
            REPO_ROOT / ".agents" / "spark" / "AGENTS.md"
        ).read_text(encoding="utf-8")
        notebook_text = notebook.read_text(encoding="utf-8")
        registry = (
            REPO_ROOT / ".agents" / "spark" / "registry.json"
        ).read_text(encoding="utf-8")
        decision = (
            REPO_ROOT / "docs" / "decisions" / "AOA-TECH-D-0054-spark-agent-lane-home.md"
        ).read_text(encoding="utf-8")

        self.assertIn(".agents/spark/", root_law)
        self.assertIn("agent-lane packet", root_law)
        self.assertIn(".agents/spark/", decision)
        self.assertIn("SPARK_EXTRAPOLATION_NOTEBOOK.md", spark_agents)
        self.assertIn("done-or-handoff", notebook_text)
        self.assertIn("registry-backed", notebook_text)
        self.assertIn("technique-refinement", notebook_text)

        source_section = notebook_text.split(
            "Local `aoa-techniques` surfaces that constrain the adaptation:",
            maxsplit=1,
        )[0]
        local_section = notebook_text.split(
            "Local `aoa-techniques` surfaces that constrain the adaptation:",
            maxsplit=1,
        )[1].split("## Center Pattern To Preserve", maxsplit=1)[0]
        self.assertIn(
            "docs/decisions/AOA-CENTER-D-0024-spark-session-lane-contract.md",
            source_section,
        )
        self.assertIn(
            "docs/decisions/AOA-CENTER-D-0027-codex-spark-agent-lane-home.md",
            source_section,
        )
        self.assertNotIn("AOA-TECH-D-0054", source_section)
        self.assertNotIn("AOA-TECH-D-0057", source_section)
        self.assertIn(
            "docs/decisions/AOA-TECH-D-0054-spark-agent-lane-home.md",
            local_section,
        )
        self.assertIn(
            "docs/decisions/AOA-TECH-D-0057-spark-registry-backed-technique-lane.md",
            local_section,
        )
        self.assertIn("aoa_techniques_spark_lane_registry_v1", registry)
        self.assertIn("technique-audit", registry)
        self.assertIn("release-prep", registry)
        self.assertIn(".agents/spark/scripts/validate_spark_lane.py", registry)


if __name__ == "__main__":
    unittest.main()
