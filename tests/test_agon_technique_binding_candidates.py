from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_builder():
    path = ROOT / "scripts" / "build_agon_technique_binding_candidates.py"
    spec = importlib.util.spec_from_file_location("agon_technique_binding_builder_test", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_agon_technique_binding_candidates_current() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/build_agon_technique_binding_candidates.py", "--check"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr + result.stdout


def test_agon_technique_binding_candidate_shape() -> None:
    data = json.loads((ROOT / "generated" / "agon_technique_binding_candidates.min.json").read_text())
    assert data["wave"] == "IV"
    assert data["total_candidates"] == 12
    assert all(c["bridge_kind"] == "practice_candidate" for c in data["candidates"])


def test_builder_rejects_candidates_without_skill_workflow_stop_line() -> None:
    builder = load_builder()
    config = json.loads((ROOT / "config" / "agon_technique_binding_candidates.seed.json").read_text(encoding="utf-8"))
    config["candidates"][0]["must_not"] = [
        item for item in config["candidates"][0]["must_not"] if "skill workflow" not in item
    ]
    case = unittest.TestCase()
    with case.assertRaisesRegex(builder.ValidationError, "create skill workflow"):
        builder.validate_config(config)
