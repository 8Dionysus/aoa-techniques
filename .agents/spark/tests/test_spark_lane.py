from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
SPARK_ROOT = REPO_ROOT / ".agents" / "spark"
REGISTRY = SPARK_ROOT / "registry.json"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


class SparkLaneTestCase(unittest.TestCase):
    def run_validator(self, repo_root: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                ".agents/spark/scripts/validate_spark_lane.py",
                "--repo-root",
                str(repo_root),
            ],
            cwd=repo_root,
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )

    def test_spark_lane_validator_passes(self) -> None:
        result = subprocess.run(
            [sys.executable, ".agents/spark/scripts/validate_spark_lane.py"],
            cwd=REPO_ROOT,
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_every_scenario_is_registered(self) -> None:
        registry = load_json(REGISTRY)
        registered = {scenario["path"] for scenario in registry["scenarios"]}
        discovered = {
            path.relative_to(REPO_ROOT).as_posix()
            for path in (SPARK_ROOT / "scenarios").iterdir()
            if path.is_dir()
        }
        self.assertEqual(registered, discovered)

    def test_unregistered_scenario_directory_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            temp_root = Path(temp)
            temp_spark_root = temp_root / ".agents" / "spark"
            temp_spark_root.parent.mkdir()
            shutil.copytree(
                SPARK_ROOT,
                temp_spark_root,
                ignore=shutil.ignore_patterns("__pycache__"),
            )
            (temp_root / "scripts").mkdir()
            (temp_root / "scripts/release_check.py").write_text(
                ".agents/spark/scripts/validate_spark_lane.py\n",
                encoding="utf-8",
            )
            extra = temp_root / ".agents/spark/scenarios/unregistered"
            (extra / "templates").mkdir(parents=True)
            (extra / "examples").mkdir(parents=True)
            (extra / "README.md").write_text("# Extra\n", encoding="utf-8")
            result = self.run_validator(temp_root)

        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn("Spark scenarios missing from registry", result.stdout)
        self.assertIn(".agents/spark/scenarios/unregistered", result.stdout)

    def test_prompt_without_done_or_handoff_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            temp_root = Path(temp)
            temp_spark_root = temp_root / ".agents" / "spark"
            temp_spark_root.parent.mkdir()
            shutil.copytree(
                SPARK_ROOT,
                temp_spark_root,
                ignore=shutil.ignore_patterns("__pycache__"),
            )
            (temp_root / "scripts").mkdir()
            (temp_root / "scripts/release_check.py").write_text(
                ".agents/spark/scripts/validate_spark_lane.py\n",
                encoding="utf-8",
            )
            prompt = temp_root / ".agents/spark/scenarios/technique-audit/PROMPT.md"
            prompt.write_text(
                prompt.read_text(encoding="utf-8").replace("done-or-handoff", "done or handoff"),
                encoding="utf-8",
            )
            result = self.run_validator(temp_root)

        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn("must mention done-or-handoff", result.stdout)

    def test_templates_have_done_or_handoff_shape(self) -> None:
        registry = load_json(REGISTRY)
        for scenario in registry["scenarios"]:
            result_template = REPO_ROOT / scenario["result_template_ref"]
            handoff_template = REPO_ROOT / scenario["handoff_template_ref"]
            self.assertIn("Status: done", result_template.read_text(encoding="utf-8"))
            self.assertIn("Status: handoff", handoff_template.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
