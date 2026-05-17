from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

PART_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[5]


def load_builder():
    path = PART_ROOT / "scripts" / "build_external_candidate_registry.py"
    spec = importlib.util.spec_from_file_location("external_candidate_registry_builder_test", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_external_candidate_registry_current() -> None:
    result = subprocess.run(
        [
            sys.executable,
            str(PART_ROOT / "scripts" / "build_external_candidate_registry.py"),
            "--check",
        ],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr + result.stdout


def test_external_candidate_registry_shape() -> None:
    data = json.loads((PART_ROOT / "generated" / "external_candidate_registry.min.json").read_text())
    assert data["total_candidates"] == 13
    assert data["active_narrowing_lanes"] == ["phase_sync_for_agents"]
    assert data["ledger_status_counts"]["future_import_here"] == 1
    assert data["gate_status_counts"]["overlap_hold"] == 4


def test_builder_rejects_active_lane_without_named_atom() -> None:
    builder = load_builder()
    config = json.loads(
        (PART_ROOT / "config" / "external_candidate_registry.source.json").read_text(encoding="utf-8")
    )
    config["candidates"][0]["atom_topology_gate"]["atomic_move_status"] = "not_named"
    case = unittest.TestCase()
    with case.assertRaisesRegex(builder.ValidationError, "active narrowing lane must name"):
        builder.validate_config(config)


def test_builder_rejects_ledger_gate_pair_drift() -> None:
    builder = load_builder()
    config = json.loads(
        (PART_ROOT / "config" / "external_candidate_registry.source.json").read_text(encoding="utf-8")
    )
    config["candidates"][0]["gate_status"] = "overlap_hold"
    case = unittest.TestCase()
    with case.assertRaisesRegex(builder.ValidationError, "must pair with gate_status"):
        builder.validate_config(config)


def test_builder_rejects_portability_gap() -> None:
    builder = load_builder()
    config = json.loads(
        (PART_ROOT / "config" / "external_candidate_registry.source.json").read_text(encoding="utf-8")
    )
    config["candidates"][0]["atom_topology_gate"]["portability_note"] = "donor-local only"
    case = unittest.TestCase()
    with case.assertRaisesRegex(builder.ValidationError, "portability_note"):
        builder.validate_config(config)
