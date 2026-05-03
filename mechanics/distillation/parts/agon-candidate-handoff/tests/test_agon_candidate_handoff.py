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
    assert data["gate_examples"] == {
        "candidate:aoa-techniques:agon/request-evidence-practice": "mechanics/distillation/parts/agon-candidate-handoff/gates/examples/request-evidence-minimal-public-safe.md"
    }
    assert data["gate_checklists"] == {
        "candidate:aoa-techniques:agon/request-evidence-practice": "mechanics/distillation/parts/agon-candidate-handoff/gates/checklists/request-evidence-gate-checklist.md"
    }
    assert data["gate_evidence_notes"] == {
        "candidate:aoa-techniques:agon/request-evidence-practice": "mechanics/distillation/parts/agon-candidate-handoff/gates/evidence-notes/request-evidence-gate-evidence-note.md"
    }
    assert data["bundle_readiness_reviews"] == {
        "candidate:aoa-techniques:agon/request-evidence-practice": "mechanics/distillation/parts/agon-candidate-handoff/gates/bundle-reviews/request-evidence-bundle-readiness-review.md"
    }
    gate_card_rows = [
        candidate
        for candidate in data["candidates"]
        if (
            "gate_card" in candidate
            or "gate_example" in candidate
            or "gate_checklist" in candidate
            or "gate_evidence_note" in candidate
            or "bundle_readiness_review" in candidate
        )
    ]
    assert gate_card_rows == [
        {
            "atomic_move_status": "candidate_named",
            "bundle_readiness_review": "mechanics/distillation/parts/agon-candidate-handoff/gates/bundle-reviews/request-evidence-bundle-readiness-review.md",
            "candidate_ref": "candidate:aoa-techniques:agon/request-evidence-practice",
            "distillation_lane": "first_narrowing_watch",
            "gate_card": "mechanics/distillation/parts/agon-candidate-handoff/gates/request-evidence-practice.md",
            "gate_checklist": "mechanics/distillation/parts/agon-candidate-handoff/gates/checklists/request-evidence-gate-checklist.md",
            "gate_evidence_note": "mechanics/distillation/parts/agon-candidate-handoff/gates/evidence-notes/request-evidence-gate-evidence-note.md",
            "gate_example": "mechanics/distillation/parts/agon-candidate-handoff/gates/examples/request-evidence-minimal-public-safe.md",
            "likely_domain": "agent-workflows",
            "nearest_wrong_owner": "aoa-evals",
            "primary_kind": "guardrail",
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


def test_builder_rejects_gate_card_pointing_to_child_artifact() -> None:
    builder = load_builder()
    config = json.loads(
        (PART_ROOT / "config" / "agon_candidate_handoff.seed.json").read_text(
            encoding="utf-8"
        )
    )
    with_card = next(entry for entry in config["entries"] if "gate_card" in entry)
    with_card["gate_card"] = with_card["gate_checklist"]
    del with_card["gate_example"]
    del with_card["gate_checklist"]
    del with_card["gate_evidence_note"]
    del with_card["bundle_readiness_review"]
    case = unittest.TestCase()
    with case.assertRaisesRegex(builder.ValidationError, "gate_card must point"):
        builder.validate_config(config)


def test_builder_rejects_gate_example_without_gate_card() -> None:
    builder = load_builder()
    config = json.loads(
        (PART_ROOT / "config" / "agon_candidate_handoff.seed.json").read_text(
            encoding="utf-8"
        )
    )
    with_example = next(entry for entry in config["entries"] if "gate_example" in entry)
    del with_example["gate_card"]
    case = unittest.TestCase()
    with case.assertRaisesRegex(builder.ValidationError, "gate_example requires gate_card"):
        builder.validate_config(config)


def test_builder_rejects_missing_gate_example() -> None:
    builder = load_builder()
    config = json.loads(
        (PART_ROOT / "config" / "agon_candidate_handoff.seed.json").read_text(
            encoding="utf-8"
        )
    )
    with_example = next(entry for entry in config["entries"] if "gate_example" in entry)
    with_example["gate_example"] = (
        "mechanics/distillation/parts/agon-candidate-handoff/gates/examples/missing.md"
    )
    case = unittest.TestCase()
    with case.assertRaisesRegex(builder.ValidationError, "gate_example path does not exist"):
        builder.validate_config(config)


def test_builder_rejects_gate_checklist_without_gate_example() -> None:
    builder = load_builder()
    config = json.loads(
        (PART_ROOT / "config" / "agon_candidate_handoff.seed.json").read_text(
            encoding="utf-8"
        )
    )
    with_checklist = next(entry for entry in config["entries"] if "gate_checklist" in entry)
    del with_checklist["gate_example"]
    case = unittest.TestCase()
    with case.assertRaisesRegex(builder.ValidationError, "gate_checklist requires gate_example"):
        builder.validate_config(config)


def test_builder_rejects_missing_gate_checklist() -> None:
    builder = load_builder()
    config = json.loads(
        (PART_ROOT / "config" / "agon_candidate_handoff.seed.json").read_text(
            encoding="utf-8"
        )
    )
    with_checklist = next(entry for entry in config["entries"] if "gate_checklist" in entry)
    with_checklist["gate_checklist"] = (
        "mechanics/distillation/parts/agon-candidate-handoff/gates/checklists/missing.md"
    )
    case = unittest.TestCase()
    with case.assertRaisesRegex(builder.ValidationError, "gate_checklist path does not exist"):
        builder.validate_config(config)


def test_builder_rejects_gate_evidence_note_without_gate_checklist() -> None:
    builder = load_builder()
    config = json.loads(
        (PART_ROOT / "config" / "agon_candidate_handoff.seed.json").read_text(
            encoding="utf-8"
        )
    )
    with_note = next(entry for entry in config["entries"] if "gate_evidence_note" in entry)
    del with_note["gate_checklist"]
    case = unittest.TestCase()
    with case.assertRaisesRegex(
        builder.ValidationError, "gate_evidence_note requires gate_checklist"
    ):
        builder.validate_config(config)


def test_builder_rejects_missing_gate_evidence_note() -> None:
    builder = load_builder()
    config = json.loads(
        (PART_ROOT / "config" / "agon_candidate_handoff.seed.json").read_text(
            encoding="utf-8"
        )
    )
    with_note = next(entry for entry in config["entries"] if "gate_evidence_note" in entry)
    with_note["gate_evidence_note"] = (
        "mechanics/distillation/parts/agon-candidate-handoff/gates/evidence-notes/missing.md"
    )
    case = unittest.TestCase()
    with case.assertRaisesRegex(
        builder.ValidationError, "gate_evidence_note path does not exist"
    ):
        builder.validate_config(config)


def test_builder_rejects_bundle_readiness_review_without_gate_evidence_note() -> None:
    builder = load_builder()
    config = json.loads(
        (PART_ROOT / "config" / "agon_candidate_handoff.seed.json").read_text(
            encoding="utf-8"
        )
    )
    with_review = next(
        entry for entry in config["entries"] if "bundle_readiness_review" in entry
    )
    del with_review["gate_evidence_note"]
    case = unittest.TestCase()
    with case.assertRaisesRegex(
        builder.ValidationError, "bundle_readiness_review requires gate_evidence_note"
    ):
        builder.validate_config(config)


def test_builder_rejects_missing_bundle_readiness_review() -> None:
    builder = load_builder()
    config = json.loads(
        (PART_ROOT / "config" / "agon_candidate_handoff.seed.json").read_text(
            encoding="utf-8"
        )
    )
    with_review = next(
        entry for entry in config["entries"] if "bundle_readiness_review" in entry
    )
    with_review["bundle_readiness_review"] = (
        "mechanics/distillation/parts/agon-candidate-handoff/gates/bundle-reviews/missing.md"
    )
    case = unittest.TestCase()
    with case.assertRaisesRegex(
        builder.ValidationError, "bundle_readiness_review path does not exist"
    ):
        builder.validate_config(config)
