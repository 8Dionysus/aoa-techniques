#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

PART_ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = PART_ROOT / "config" / "cross_layer_candidate_registry.seed.json"
GENERATED_PATH = PART_ROOT / "generated" / "cross_layer_candidate_registry.min.json"

EXPECTED_SCHEMA_VERSION = "distillation-cross-layer-candidate-registry.seed/0.1"
EXPECTED_INDEX_SCHEMA = "distillation-cross-layer-candidate-registry-index/0.1"
EXPECTED_TOTAL = 24
EXPECTED_SOURCE_LEDGER = "mechanics/distillation/parts/cross-layer-candidate-ledger/README.md"
EXPECTED_LEDGER_STATUS_COUNTS = {
    "already_staged_elsewhere": 6,
    "hold_because_overlap": 2,
    "landed_from_wave_map": 10,
    "needs_layer_incubation_before_distillation_here": 3,
    "substrate_or_architecture_pattern_not_yet_technique": 3,
}
EXPECTED_SUMMARY_COUNTS = {
    "already_staged_elsewhere": 6,
    "future_import_here": 0,
    "hold_because_overlap": 2,
    "landed_from_wave_map": 10,
    "needs_layer_incubation_before_distillation_here": 3,
    "ready_to_distill_here": 0,
    "substrate_or_architecture_pattern_not_yet_technique": 3,
}
EXPECTED_GATE_STATUS_COUNTS = {
    "inherited_external": 6,
    "landed": 10,
    "layer_incubation": 3,
    "not_technique_shaped": 3,
    "overlap_hold": 2,
}
EXPECTED_WAVE_COUNTS = {
    "A": 5,
    "B": 3,
    "C": 2,
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
    "portability_note",
)
REQUIRED_BRIDGE_FIELDS = ("higher_law", "local_route", "bridge_stop_line")


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


def require_text(value: Any, field: str, candidate_id: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValidationError(f"{candidate_id}: {field} must be a non-empty string")
    return value


def require_object(value: Any, field: str, candidate_id: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValidationError(f"{candidate_id}: {field} must be an object")
    return value


def validate_landed_technique(candidate: dict[str, Any], candidate_id: str) -> None:
    landed = require_object(candidate.get("landed_technique"), "landed_technique", candidate_id)
    for field in ("id", "path", "domain"):
        require_text(landed.get(field), f"landed_technique.{field}", candidate_id)
    if not landed["id"].startswith("AOA-T-"):
        raise ValidationError(f"{candidate_id}: landed technique id must use AOA-T-*")
    if not landed["path"].startswith("techniques/"):
        raise ValidationError(f"{candidate_id}: landed technique path must stay under techniques/")


def validate_candidate(candidate: dict[str, Any]) -> None:
    candidate_id = require_text(candidate.get("candidate"), "candidate", "<unknown>")
    for field in (
        "source_layer",
        "tentative_domain",
        "ledger_status",
        "gate_status",
        "current_gate",
        "next_move",
    ):
        require_text(candidate.get(field), field, candidate_id)

    if candidate["ledger_status"] not in EXPECTED_SUMMARY_COUNTS:
        raise ValidationError(f"{candidate_id}: unknown ledger_status {candidate['ledger_status']!r}")
    if candidate["ledger_status"] in {"ready_to_distill_here", "future_import_here"}:
        raise ValidationError(f"{candidate_id}: cross-layer registry has no ready/future import lanes")
    if candidate["gate_status"] not in EXPECTED_GATE_STATUS_COUNTS:
        raise ValidationError(f"{candidate_id}: unknown gate_status {candidate['gate_status']!r}")
    if not isinstance(candidate.get("nearest_overlap"), list):
        raise ValidationError(f"{candidate_id}: nearest_overlap must be a list")

    gate = require_object(candidate.get("atom_topology_gate"), "atom_topology_gate", candidate_id)
    for field in REQUIRED_GATE_FIELDS:
        require_text(gate.get(field), f"atom_topology_gate.{field}", candidate_id)
    if gate["atomic_move_status"] not in {"inherited", "landed", "not_named"}:
        raise ValidationError(f"{candidate_id}: unsupported atomic_move_status")

    bridge = require_object(candidate.get("law_local_bridge"), "law_local_bridge", candidate_id)
    for field in REQUIRED_BRIDGE_FIELDS:
        require_text(bridge.get(field), f"law_local_bridge.{field}", candidate_id)

    portability_note = gate["portability_note"].lower()
    if not any(
        term in portability_note
        for term in ("portable", "standalone", "outside os abyss", "external reuse")
    ):
        raise ValidationError(f"{candidate_id}: portability_note must name portability pressure")

    ledger_status = candidate["ledger_status"]
    atomic_status = gate["atomic_move_status"]
    gate_status = candidate["gate_status"]

    if ledger_status == "already_staged_elsewhere":
        require_text(
            candidate.get("inherited_external_status"),
            "inherited_external_status",
            candidate_id,
        )
        if gate_status != "inherited_external" or atomic_status != "inherited":
            raise ValidationError(f"{candidate_id}: inherited rows must use inherited gate status")
    elif ledger_status == "landed_from_wave_map":
        validate_landed_technique(candidate, candidate_id)
        if gate_status != "landed" or atomic_status != "landed":
            raise ValidationError(f"{candidate_id}: landed rows must use landed gate status")
        if candidate.get("wave") not in EXPECTED_WAVE_COUNTS:
            raise ValidationError(f"{candidate_id}: landed rows must name wave A, B, or C")
    elif ledger_status == "hold_because_overlap":
        if gate_status != "overlap_hold" or atomic_status != "not_named":
            raise ValidationError(f"{candidate_id}: overlap rows must stay not_named")
    elif ledger_status == "needs_layer_incubation_before_distillation_here":
        if gate_status != "layer_incubation" or atomic_status != "not_named":
            raise ValidationError(f"{candidate_id}: incubation rows must stay not_named")
    elif ledger_status == "substrate_or_architecture_pattern_not_yet_technique":
        if gate_status != "not_technique_shaped" or atomic_status != "not_named":
            raise ValidationError(f"{candidate_id}: architecture rows must stay not_named")


def validate_config(config: dict[str, Any]) -> None:
    if config.get("schema_version") != EXPECTED_SCHEMA_VERSION:
        raise ValidationError("unexpected schema_version")
    if config.get("registry_id") != "distillation.cross_layer_candidate_registry.v1":
        raise ValidationError("unexpected registry_id")
    if config.get("source_ledger") != EXPECTED_SOURCE_LEDGER:
        raise ValidationError("unexpected source_ledger")
    if config.get("status") != "active_accounting_registry":
        raise ValidationError("unexpected status")
    if config.get("summary_counts") != EXPECTED_SUMMARY_COUNTS:
        raise ValidationError("unexpected summary_counts")

    candidates = config.get("candidates")
    if not isinstance(candidates, list) or not candidates:
        raise ValidationError("candidates must be a non-empty list")
    if len(candidates) != EXPECTED_TOTAL:
        raise ValidationError(f"expected {EXPECTED_TOTAL} candidates, found {len(candidates)}")

    names = [c.get("candidate") for c in candidates]
    if len(names) != len(set(names)):
        raise ValidationError("duplicate candidate")

    for candidate in candidates:
        validate_candidate(candidate)

    ledger_counts = Counter(c["ledger_status"] for c in candidates)
    gate_counts = Counter(c["gate_status"] for c in candidates)
    if dict(sorted(ledger_counts.items())) != EXPECTED_LEDGER_STATUS_COUNTS:
        raise ValidationError(f"unexpected ledger status counts: {dict(ledger_counts)}")
    if dict(sorted(gate_counts.items())) != EXPECTED_GATE_STATUS_COUNTS:
        raise ValidationError(f"unexpected gate status counts: {dict(gate_counts)}")

    wave_counts = Counter(c.get("wave") for c in candidates if c["ledger_status"] == "landed_from_wave_map")
    if dict(sorted(wave_counts.items())) != EXPECTED_WAVE_COUNTS:
        raise ValidationError(f"unexpected wave counts: {dict(wave_counts)}")


def build_index(config: dict[str, Any]) -> dict[str, Any]:
    validate_config(config)
    candidates = config["candidates"]
    ledger_counts = Counter(c["ledger_status"] for c in candidates)
    gate_counts = Counter(c["gate_status"] for c in candidates)
    source_counts = Counter(c["source_layer"] for c in candidates)
    wave_counts = Counter(c.get("wave") for c in candidates if c["ledger_status"] == "landed_from_wave_map")
    return {
        "schema_version": EXPECTED_INDEX_SCHEMA,
        "registry_id": "distillation.cross_layer_candidate_registry.index.v1",
        "source_ledger": config["source_ledger"],
        "status": config["status"],
        "total_candidates": len(candidates),
        "summary_counts": config["summary_counts"],
        "ledger_status_counts": {
            key: ledger_counts.get(key, 0) for key in sorted(EXPECTED_SUMMARY_COUNTS)
        },
        "gate_status_counts": {
            key: gate_counts.get(key, 0) for key in sorted(EXPECTED_GATE_STATUS_COUNTS)
        },
        "source_layer_counts": dict(sorted(source_counts.items())),
        "wave_counts": dict(sorted(wave_counts.items())),
        "future_import_lanes": [
            c["candidate"] for c in candidates if c["ledger_status"] == "future_import_here"
        ],
        "wave_landed_technique_ids": [
            c["landed_technique"]["id"]
            for c in candidates
            if c["ledger_status"] == "landed_from_wave_map"
        ],
        "inherited_external_candidates": [
            c["candidate"] for c in candidates if c["ledger_status"] == "already_staged_elsewhere"
        ],
        "candidates": [
            {
                "candidate": c["candidate"],
                "source_layer": c["source_layer"],
                "ledger_status": c["ledger_status"],
                "gate_status": c["gate_status"],
                "tentative_domain": c["tentative_domain"],
                "atomic_move_status": c["atom_topology_gate"]["atomic_move_status"],
                "primary_kind": c["atom_topology_gate"]["primary_kind"],
                "landed_technique_id": c.get("landed_technique", {}).get("id"),
                "wave": c.get("wave"),
            }
            for c in candidates
        ],
        "stop_line": (
            "registry accounting does not create bundles, change candidate status, "
            "authorize import, or give recurrence promotion authority"
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
        print(f"ok: {index['total_candidates']} cross-layer candidates")
        return 0
    except ValidationError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
