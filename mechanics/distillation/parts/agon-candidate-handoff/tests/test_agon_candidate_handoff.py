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
    path = PART_ROOT / "scripts" / "build_agon_candidate_handoff.py"
    spec = importlib.util.spec_from_file_location("agon_candidate_handoff_builder_test", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_agon_candidate_handoff_current() -> None:
    result = subprocess.run(
        [
            sys.executable,
            str(PART_ROOT / "scripts" / "build_agon_candidate_handoff.py"),
            "--check",
        ],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr + result.stdout

    result = subprocess.run(
        [
            sys.executable,
            str(PART_ROOT / "scripts" / "validate_agon_candidate_handoff.py"),
        ],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr + result.stdout


def test_agon_candidate_handoff_shape() -> None:
    data = json.loads((PART_ROOT / "generated" / "agon_candidate_handoff.min.json").read_text())

    assert data["total_candidates"] == 22
    assert data["source_counts"] == {
        "epistemic-technique-candidates": 10,
        "move-technique-bridge": 12,
    }
    assert data["distillation_lane_counts"] == {
        "first_narrowing_watch": 11,
        "owner_route_hold": 1,
        "source_boundary_hold": 10,
    }
    assert "candidate:aoa-techniques:agon/request-evidence-practice" in data[
        "first_narrowing_watch"
    ]
    assert "agon.tech.epistemic.doctrine_revision_review_practice" in data[
        "owner_route_holds"
    ]
    assert data["gate_cards"] == {
        "candidate:aoa-techniques:agon/request-evidence-practice": "mechanics/distillation/parts/agon-candidate-handoff/gates/request-evidence-practice.md"
    }
    gate_card_rows = [
        candidate for candidate in data["candidates"] if "gate_card" in candidate
    ]
    assert gate_card_rows == [
        {
            "atomic_move_status": "candidate_named",
            "candidate_ref": "candidate:aoa-techniques:agon/request-evidence-practice",
            "distillation_lane": "first_narrowing_watch",
            "gate_card": "mechanics/distillation/parts/agon-candidate-handoff/gates/request-evidence-practice.md",
            "likely_domain": "agent-workflows",
            "nearest_wrong_owner": "aoa-evals",
            "primary_kind": "evidence-request",
            "source_label": "request_evidence",
            "source_part": "move-technique-bridge",
            "source_status": "requested_not_landed",
        }
    ]
    assert "does not define Agon law" in data["stop_line"]


def test_builder_rejects_missing_source_candidate() -> None:
    builder = load_builder()
    config = json.loads(
        (PART_ROOT / "config" / "agon_candidate_handoff.seed.json").read_text(
            encoding="utf-8"
        )
    )
    config["entries"][0]["candidate_ref"] = "candidate:aoa-techniques:agon/missing"
    case = unittest.TestCase()
    with case.assertRaisesRegex(builder.ValidationError, "missing source candidate"):
        builder.validate_config(config)


def test_builder_rejects_lane_atomic_status_drift() -> None:
    builder = load_builder()
    config = json.loads(
        (PART_ROOT / "config" / "agon_candidate_handoff.seed.json").read_text(
            encoding="utf-8"
        )
    )
    first = next(
        entry
        for entry in config["entries"]
        if entry["distillation_lane"] == "first_narrowing_watch"
    )
    first["distillation_gate"]["atomic_move_status"] = "not_named_cleanly"
    case = unittest.TestCase()
    with case.assertRaisesRegex(builder.ValidationError, "must use atomic_move_status"):
        builder.validate_config(config)


def test_builder_rejects_missing_gate_card() -> None:
    builder = load_builder()
    config = json.loads(
        (PART_ROOT / "config" / "agon_candidate_handoff.seed.json").read_text(
            encoding="utf-8"
        )
    )
    with_card = next(entry for entry in config["entries"] if "gate_card" in entry)
    with_card["gate_card"] = "mechanics/distillation/parts/agon-candidate-handoff/gates/missing.md"
    case = unittest.TestCase()
    with case.assertRaisesRegex(builder.ValidationError, "gate_card path does not exist"):
        builder.validate_config(config)


def test_builder_rejects_gate_card_on_hold_lane() -> None:
    builder = load_builder()
    config = json.loads(
        (PART_ROOT / "config" / "agon_candidate_handoff.seed.json").read_text(
            encoding="utf-8"
        )
    )
    with_card = next(entry for entry in config["entries"] if "gate_card" in entry)
    with_card["distillation_lane"] = "source_boundary_hold"
    with_card["distillation_gate"]["atomic_move_status"] = "not_named_cleanly"
    case = unittest.TestCase()
    with case.assertRaisesRegex(
        builder.ValidationError, "only first_narrowing_watch entries may carry gate_card"
    ):
        builder.validate_config(config)
