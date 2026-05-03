#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

PART_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[5]
CONFIG_PATH = PART_ROOT / "config" / "agon_candidate_handoff.seed.json"
GENERATED_PATH = PART_ROOT / "generated" / "agon_candidate_handoff.min.json"

MOVE_SOURCE = (
    REPO_ROOT
    / "mechanics"
    / "agon"
    / "parts"
    / "move-technique-bridge"
    / "generated"
    / "agon_technique_binding_candidates.min.json"
)
EPISTEMIC_SOURCE = (
    REPO_ROOT
    / "mechanics"
    / "agon"
    / "parts"
    / "epistemic-technique-candidates"
    / "generated"
    / "agon_epistemic_technique_candidates.min.json"
)

EXPECTED_SCHEMA_VERSION = "distillation-agon-candidate-handoff.seed/0.1"
EXPECTED_INDEX_SCHEMA = "distillation-agon-candidate-handoff-index/0.1"
EXPECTED_REGISTRY_ID = "distillation.agon_candidate_handoff.v1"
EXPECTED_SOURCE_SURFACES = {
    "move_technique_bridge": "mechanics/agon/parts/move-technique-bridge/generated/agon_technique_binding_candidates.min.json",
    "epistemic_technique_candidates": "mechanics/agon/parts/epistemic-technique-candidates/generated/agon_epistemic_technique_candidates.min.json",
}
EXPECTED_LANE_COUNTS = {
    "first_narrowing_watch": 11,
    "owner_route_hold": 1,
    "source_boundary_hold": 10,
}
EXPECTED_SOURCE_COUNTS = {
    "epistemic-technique-candidates": 10,
    "move-technique-bridge": 12,
}
EXPECTED_TOTAL = sum(EXPECTED_SOURCE_COUNTS.values())
LANE_TO_ATOMIC_STATUS = {
    "first_narrowing_watch": "candidate_named",
    "source_boundary_hold": "not_named_cleanly",
    "owner_route_hold": "owner_route_needed",
}
REQUIRED_GATE_FIELDS = (
    "atomic_move_status",
    "atomic_move_note",
    "likely_domain",
    "primary_kind",
    "family_posture",
    "capability_class",
    "substrate",
    "execution_profile",
    "risk_posture",
    "portable_core",
)
REQUIRED_BRIDGE_FIELDS = (
    "higher_law",
    "local_route",
    "nearest_wrong_owner",
    "bridge_stop_line",
)
STOP_LINE_AUTHORITY_TERMS = (
    "agon",
    "skill",
    "proof",
    "scar",
    "arena",
    "rank",
    "trust",
    "memory",
    "kag",
    "tos",
    "doctrine",
    "route",
)
GATE_CARD_PREFIX = "mechanics/distillation/parts/agon-candidate-handoff/gates/"
GATE_EXAMPLE_PREFIX = (
    "mechanics/distillation/parts/agon-candidate-handoff/gates/examples/"
)
GATE_CHECKLIST_PREFIX = (
    "mechanics/distillation/parts/agon-candidate-handoff/gates/checklists/"
)
GATE_EVIDENCE_NOTE_PREFIX = (
    "mechanics/distillation/parts/agon-candidate-handoff/gates/evidence-notes/"
)
BUNDLE_READINESS_REVIEW_PREFIX = (
    "mechanics/distillation/parts/agon-candidate-handoff/gates/bundle-reviews/"
)
GATE_CARD_EXCLUDED_PREFIXES = (
    GATE_EXAMPLE_PREFIX,
    GATE_CHECKLIST_PREFIX,
    GATE_EVIDENCE_NOTE_PREFIX,
    BUNDLE_READINESS_REVIEW_PREFIX,
)


class ValidationError(Exception):
    pass


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValidationError(f"missing required file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValidationError(f"invalid JSON in {path}: {exc}") from exc


def write_json_min(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )


def require_text(value: Any, field: str, candidate_ref: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValidationError(f"{candidate_ref}: {field} must be a non-empty string")
    return value


def require_object(value: Any, field: str, candidate_ref: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValidationError(f"{candidate_ref}: {field} must be an object")
    return value


def source_refs() -> dict[str, dict[str, str]]:
    move = read_json(MOVE_SOURCE)
    epistemic = read_json(EPISTEMIC_SOURCE)

    move_refs = {
        item["candidate_id"]: item["status"]
        for item in move.get("candidates", [])
        if isinstance(item, dict)
    }
    epistemic_refs = {
        item["technique_id"]: item["status"]
        for item in epistemic.get("techniques", [])
        if isinstance(item, dict)
    }

    if len(move_refs) != EXPECTED_SOURCE_COUNTS["move-technique-bridge"]:
        raise ValidationError("unexpected move-technique-bridge source count")
    if len(epistemic_refs) != EXPECTED_SOURCE_COUNTS["epistemic-technique-candidates"]:
        raise ValidationError("unexpected epistemic-technique-candidates source count")

    return {
        "move-technique-bridge": move_refs,
        "epistemic-technique-candidates": epistemic_refs,
    }


def validate_entry(entry: dict[str, Any], source_map: dict[str, dict[str, str]]) -> None:
    ref = require_text(entry.get("candidate_ref"), "candidate_ref", "<unknown>")
    source_part = require_text(entry.get("source_part"), "source_part", ref)
    source_status = require_text(entry.get("source_status"), "source_status", ref)
    require_text(entry.get("source_label"), "source_label", ref)
    lane = require_text(entry.get("distillation_lane"), "distillation_lane", ref)
    require_text(entry.get("next_move"), "next_move", ref)

    if source_part not in source_map:
        raise ValidationError(f"{ref}: unknown source_part {source_part!r}")
    if ref not in source_map[source_part]:
        raise ValidationError(f"{ref}: missing source candidate in {source_part}")
    if source_status != source_map[source_part][ref]:
        raise ValidationError(f"{ref}: source_status does not match Agon source registry")
    if lane not in EXPECTED_LANE_COUNTS:
        raise ValidationError(f"{ref}: unknown distillation_lane {lane!r}")

    gate = require_object(entry.get("distillation_gate"), "distillation_gate", ref)
    for field in REQUIRED_GATE_FIELDS:
        require_text(gate.get(field), f"distillation_gate.{field}", ref)
    expected_atomic_status = LANE_TO_ATOMIC_STATUS[lane]
    if gate["atomic_move_status"] != expected_atomic_status:
        raise ValidationError(
            f"{ref}: {lane} must use atomic_move_status {expected_atomic_status}"
        )
    portable_core = gate["portable_core"].lower()
    if not any(term in portable_core for term in ("portable", "outside os abyss", "outside agon")):
        raise ValidationError(f"{ref}: portable_core must name portability")

    bridge = require_object(entry.get("bridge"), "bridge", ref)
    for field in REQUIRED_BRIDGE_FIELDS:
        require_text(bridge.get(field), f"bridge.{field}", ref)
    stop_line = bridge["bridge_stop_line"].lower()
    if "do not" not in stop_line:
        raise ValidationError(f"{ref}: bridge_stop_line must be an explicit stop-line")
    if not any(term in stop_line for term in STOP_LINE_AUTHORITY_TERMS):
        raise ValidationError(f"{ref}: bridge_stop_line must preserve an authority boundary")

    gate_card = entry.get("gate_card")
    if gate_card is not None:
        if not isinstance(gate_card, str) or not gate_card.startswith(GATE_CARD_PREFIX):
            raise ValidationError(f"{ref}: gate_card must stay under the handoff gates directory")
        if gate_card.startswith(GATE_CARD_EXCLUDED_PREFIXES):
            raise ValidationError(f"{ref}: gate_card must point to a gate card, not a child artifact")
        gate_path = REPO_ROOT / gate_card
        if not gate_path.is_file():
            raise ValidationError(f"{ref}: gate_card path does not exist")
        if lane != "first_narrowing_watch":
            raise ValidationError(f"{ref}: only first_narrowing_watch entries may carry gate_card")

    gate_example = entry.get("gate_example")
    if gate_example is not None:
        if gate_card is None:
            raise ValidationError(f"{ref}: gate_example requires gate_card")
        if not isinstance(gate_example, str) or not gate_example.startswith(
            GATE_EXAMPLE_PREFIX
        ):
            raise ValidationError(
                f"{ref}: gate_example must stay under the handoff gate examples directory"
            )
        example_path = REPO_ROOT / gate_example
        if not example_path.is_file():
            raise ValidationError(f"{ref}: gate_example path does not exist")
        if lane != "first_narrowing_watch":
            raise ValidationError(
                f"{ref}: only first_narrowing_watch entries may carry gate_example"
            )

    gate_checklist = entry.get("gate_checklist")
    if gate_checklist is not None:
        if gate_example is None:
            raise ValidationError(f"{ref}: gate_checklist requires gate_example")
        if not isinstance(gate_checklist, str) or not gate_checklist.startswith(
            GATE_CHECKLIST_PREFIX
        ):
            raise ValidationError(
                f"{ref}: gate_checklist must stay under the handoff gate checklists directory"
            )
        checklist_path = REPO_ROOT / gate_checklist
        if not checklist_path.is_file():
            raise ValidationError(f"{ref}: gate_checklist path does not exist")
        if lane != "first_narrowing_watch":
            raise ValidationError(
                f"{ref}: only first_narrowing_watch entries may carry gate_checklist"
            )

    gate_evidence_note = entry.get("gate_evidence_note")
    if gate_evidence_note is not None:
        if gate_checklist is None:
            raise ValidationError(f"{ref}: gate_evidence_note requires gate_checklist")
        if not isinstance(gate_evidence_note, str) or not gate_evidence_note.startswith(
            GATE_EVIDENCE_NOTE_PREFIX
        ):
            raise ValidationError(
                f"{ref}: gate_evidence_note must stay under the handoff gate evidence-notes directory"
            )
        note_path = REPO_ROOT / gate_evidence_note
        if not note_path.is_file():
            raise ValidationError(f"{ref}: gate_evidence_note path does not exist")
        if lane != "first_narrowing_watch":
            raise ValidationError(
                f"{ref}: only first_narrowing_watch entries may carry gate_evidence_note"
            )

    bundle_readiness_review = entry.get("bundle_readiness_review")
    if bundle_readiness_review is not None:
        if gate_evidence_note is None:
            raise ValidationError(
                f"{ref}: bundle_readiness_review requires gate_evidence_note"
            )
        if not isinstance(
            bundle_readiness_review, str
        ) or not bundle_readiness_review.startswith(BUNDLE_READINESS_REVIEW_PREFIX):
            raise ValidationError(
                f"{ref}: bundle_readiness_review must stay under the handoff bundle-reviews directory"
            )
        review_path = REPO_ROOT / bundle_readiness_review
        if not review_path.is_file():
            raise ValidationError(f"{ref}: bundle_readiness_review path does not exist")
        if lane != "first_narrowing_watch":
            raise ValidationError(
                f"{ref}: only first_narrowing_watch entries may carry bundle_readiness_review"
            )


def validate_config(config: dict[str, Any]) -> None:
    if config.get("schema_version") != EXPECTED_SCHEMA_VERSION:
        raise ValidationError("unexpected schema_version")
    if config.get("registry_id") != EXPECTED_REGISTRY_ID:
        raise ValidationError("unexpected registry_id")
    if config.get("status") != "candidate_lane_map":
        raise ValidationError("unexpected status")
    if config.get("source_surfaces") != EXPECTED_SOURCE_SURFACES:
        raise ValidationError("unexpected source_surfaces")

    entries = config.get("entries")
    if not isinstance(entries, list) or not entries:
        raise ValidationError("entries must be a non-empty list")
    if len(entries) != EXPECTED_TOTAL:
        raise ValidationError(f"expected {EXPECTED_TOTAL} entries, found {len(entries)}")

    refs = [entry.get("candidate_ref") for entry in entries]
    if len(refs) != len(set(refs)):
        raise ValidationError("duplicate candidate_ref")

    source_map = source_refs()
    for entry in entries:
        validate_entry(entry, source_map)

    lane_counts = Counter(entry["distillation_lane"] for entry in entries)
    if dict(sorted(lane_counts.items())) != EXPECTED_LANE_COUNTS:
        raise ValidationError(f"unexpected distillation lane counts: {dict(lane_counts)}")

    source_counts = Counter(entry["source_part"] for entry in entries)
    if dict(sorted(source_counts.items())) != EXPECTED_SOURCE_COUNTS:
        raise ValidationError(f"unexpected source counts: {dict(source_counts)}")

    expected_refs = set().union(*[set(refs_by_part) for refs_by_part in source_map.values()])
    if set(refs) != expected_refs:
        missing = sorted(expected_refs - set(refs))
        extra = sorted(set(refs) - expected_refs)
        raise ValidationError(f"source coverage mismatch missing={missing} extra={extra}")


def build_index(config: dict[str, Any]) -> dict[str, Any]:
    validate_config(config)
    entries = config["entries"]
    lane_counts = Counter(entry["distillation_lane"] for entry in entries)
    source_counts = Counter(entry["source_part"] for entry in entries)
    candidate_rows = []
    for entry in entries:
        row = {
            "candidate_ref": entry["candidate_ref"],
            "source_part": entry["source_part"],
            "source_status": entry["source_status"],
            "source_label": entry["source_label"],
            "distillation_lane": entry["distillation_lane"],
            "atomic_move_status": entry["distillation_gate"]["atomic_move_status"],
            "likely_domain": entry["distillation_gate"]["likely_domain"],
            "primary_kind": entry["distillation_gate"]["primary_kind"],
            "nearest_wrong_owner": entry["bridge"]["nearest_wrong_owner"],
        }
        if "gate_card" in entry:
            row["gate_card"] = entry["gate_card"]
        if "gate_example" in entry:
            row["gate_example"] = entry["gate_example"]
        if "gate_checklist" in entry:
            row["gate_checklist"] = entry["gate_checklist"]
        if "gate_evidence_note" in entry:
            row["gate_evidence_note"] = entry["gate_evidence_note"]
        if "bundle_readiness_review" in entry:
            row["bundle_readiness_review"] = entry["bundle_readiness_review"]
        candidate_rows.append(row)
    return {
        "schema_version": EXPECTED_INDEX_SCHEMA,
        "registry_id": "distillation.agon_candidate_handoff.index.v1",
        "source_surfaces": config["source_surfaces"],
        "status": config["status"],
        "total_candidates": len(entries),
        "source_counts": dict(sorted(source_counts.items())),
        "distillation_lane_counts": dict(sorted(lane_counts.items())),
        "first_narrowing_watch": [
            entry["candidate_ref"]
            for entry in entries
            if entry["distillation_lane"] == "first_narrowing_watch"
        ],
        "owner_route_holds": [
            entry["candidate_ref"]
            for entry in entries
            if entry["distillation_lane"] == "owner_route_hold"
        ],
        "gate_cards": {
            entry["candidate_ref"]: entry["gate_card"]
            for entry in entries
            if "gate_card" in entry
        },
        "gate_examples": {
            entry["candidate_ref"]: entry["gate_example"]
            for entry in entries
            if "gate_example" in entry
        },
        "gate_checklists": {
            entry["candidate_ref"]: entry["gate_checklist"]
            for entry in entries
            if "gate_checklist" in entry
        },
        "gate_evidence_notes": {
            entry["candidate_ref"]: entry["gate_evidence_note"]
            for entry in entries
            if "gate_evidence_note" in entry
        },
        "bundle_readiness_reviews": {
            entry["candidate_ref"]: entry["bundle_readiness_review"]
            for entry in entries
            if "bundle_readiness_review" in entry
        },
        "candidates": candidate_rows,
        "stop_line": (
            "Agon candidate handoff does not define Agon law, create skills, issue proof, "
            "write scars, start arena runtime, promote KAG, write ToS canon, or promote techniques"
        ),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)

    try:
        config = read_json(CONFIG_PATH)
        index = build_index(config)
        if args.check:
            existing = read_json(GENERATED_PATH)
            if existing != index:
                raise ValidationError(f"{GENERATED_PATH} is stale; rerun without --check")
        else:
            write_json_min(GENERATED_PATH, index)
        print(f"ok: {index['total_candidates']} Agon handoff candidates")
        return 0
    except ValidationError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
