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
    path = PART_ROOT / "scripts" / "build_cross_layer_candidate_registry.py"
    spec = importlib.util.spec_from_file_location("cross_layer_candidate_registry_builder_test", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_cross_layer_candidate_registry_current() -> None:
    result = subprocess.run(
        [
            sys.executable,
            str(PART_ROOT / "scripts" / "build_cross_layer_candidate_registry.py"),
            "--check",
        ],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr + result.stdout


def test_cross_layer_candidate_registry_shape() -> None:
    data = json.loads((PART_ROOT / "generated" / "cross_layer_candidate_registry.min.json").read_text())
    assert data["total_candidates"] == 24
    assert data["future_import_lanes"] == []
    assert data["summary_counts"]["already_staged_elsewhere"] == 6
    assert data["summary_counts"]["landed_from_wave_map"] == 10
    assert data["ledger_status_counts"]["hold_because_overlap"] == 2
    assert data["ledger_status_counts"]["needs_layer_incubation_before_distillation_here"] == 3
    assert data["gate_status_counts"]["not_technique_shaped"] == 3
    assert data["wave_counts"] == {"A": 5, "B": 3, "C": 2}
    assert "AOA-T-0041" not in data["wave_landed_technique_ids"]


def test_builder_rejects_landed_row_without_landed_technique() -> None:
    builder = load_builder()
    config = json.loads(
        (PART_ROOT / "config" / "cross_layer_candidate_registry.source.json").read_text(
            encoding="utf-8"
        )
    )
    landed = next(c for c in config["candidates"] if c["candidate"] == "profile-preset-composition")
    landed.pop("landed_technique")
    case = unittest.TestCase()
    with case.assertRaisesRegex(builder.ValidationError, "landed_technique"):
        builder.validate_config(config)


def test_builder_rejects_inherited_row_without_inherited_status() -> None:
    builder = load_builder()
    config = json.loads(
        (PART_ROOT / "config" / "cross_layer_candidate_registry.source.json").read_text(
            encoding="utf-8"
        )
    )
    inherited = next(c for c in config["candidates"] if c["candidate"] == "phase-synchronized-agent-handoff")
    inherited.pop("inherited_external_status")
    case = unittest.TestCase()
    with case.assertRaisesRegex(builder.ValidationError, "inherited_external_status"):
        builder.validate_config(config)


def test_builder_rejects_portability_gap() -> None:
    builder = load_builder()
    config = json.loads(
        (PART_ROOT / "config" / "cross_layer_candidate_registry.source.json").read_text(
            encoding="utf-8"
        )
    )
    config["candidates"][0]["atom_topology_gate"]["portability_note"] = "donor-local only"
    case = unittest.TestCase()
    with case.assertRaisesRegex(builder.ValidationError, "portability_note"):
        builder.validate_config(config)
