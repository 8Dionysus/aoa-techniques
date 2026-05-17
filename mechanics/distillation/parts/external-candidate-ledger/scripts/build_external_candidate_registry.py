#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

PART_ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = PART_ROOT / "config" / "external_candidate_registry.source.json"
GENERATED_PATH = PART_ROOT / "generated" / "external_candidate_registry.min.json"

EXPECTED_SCHEMA_VERSION = "distillation-external-candidate-registry.seed/0.1"
EXPECTED_INDEX_SCHEMA = "distillation-external-candidate-registry-index/0.1"
EXPECTED_TOTAL = 13
EXPECTED_LEDGER_STATUS_COUNTS = {
    "future_import_here": 1,
    "hold_because_overlap": 4,
    "needs_layer_incubation_before_distillation_here": 5,
    "substrate_or_architecture_pattern_not_yet_technique": 3,
}
EXPECTED_GATE_STATUS_COUNTS = {
    "active_narrowing": 1,
    "layer_incubation": 5,
    "not_technique_shaped": 3,
    "overlap_hold": 4,
}
LEDGER_STATUS_TO_GATE_STATUS = {
    "future_import_here": "active_narrowing",
    "hold_because_overlap": "overlap_hold",
    "needs_layer_incubation_before_distillation_here": "layer_incubation",
    "substrate_or_architecture_pattern_not_yet_technique": "not_technique_shaped",
}
EXPECTED_ACTIVE_LANE = "phase_sync_for_agents"
EXPECTED_SOURCE_LEDGER = "mechanics/distillation/parts/external-candidate-ledger/README.md"
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


def validate_candidate(candidate: dict[str, Any]) -> None:
    seed = require_text(candidate.get("seed_candidate"), "seed_candidate", "<unknown>")
    for field in (
        "donor",
        "suggested_technique_name",
        "tentative_domain",
        "ledger_status",
        "gate_status",
        "current_gate",
        "next_move",
    ):
        require_text(candidate.get(field), field, seed)

    if candidate["ledger_status"] not in EXPECTED_LEDGER_STATUS_COUNTS:
        raise ValidationError(f"{seed}: unknown ledger_status {candidate['ledger_status']!r}")
    if candidate["gate_status"] not in EXPECTED_GATE_STATUS_COUNTS:
        raise ValidationError(f"{seed}: unknown gate_status {candidate['gate_status']!r}")
    expected_gate_status = LEDGER_STATUS_TO_GATE_STATUS[candidate["ledger_status"]]
    if candidate["gate_status"] != expected_gate_status:
        raise ValidationError(
            f"{seed}: ledger_status {candidate['ledger_status']!r} must pair with gate_status {expected_gate_status!r}"
        )
    if not isinstance(candidate.get("nearest_overlap"), list):
        raise ValidationError(f"{seed}: nearest_overlap must be a list")

    gate = candidate.get("atom_topology_gate")
    if not isinstance(gate, dict):
        raise ValidationError(f"{seed}: atom_topology_gate must be an object")
    for field in REQUIRED_GATE_FIELDS:
        require_text(gate.get(field), f"atom_topology_gate.{field}", seed)
    if gate["atomic_move_status"] not in {"named", "not_named"}:
        raise ValidationError(f"{seed}: unsupported atomic_move_status")
    if candidate["gate_status"] == "active_narrowing" and gate["atomic_move_status"] != "named":
        raise ValidationError(f"{seed}: active narrowing lane must name the candidate atom")
    if candidate["gate_status"] != "active_narrowing" and gate["atomic_move_status"] != "not_named":
        raise ValidationError(f"{seed}: non-active lanes should stay honest as not_named")

    bridge = candidate.get("law_local_bridge")
    if not isinstance(bridge, dict):
        raise ValidationError(f"{seed}: law_local_bridge must be an object")
    for field in REQUIRED_BRIDGE_FIELDS:
        require_text(bridge.get(field), f"law_local_bridge.{field}", seed)
    portability_note = gate["portability_note"].lower()
    if not any(
        term in portability_note
        for term in ("portable", "standalone", "outside os abyss", "external reuse")
    ):
        raise ValidationError(f"{seed}: portability_note must name portability pressure")


def validate_config(config: dict[str, Any]) -> None:
    if config.get("schema_version") != EXPECTED_SCHEMA_VERSION:
        raise ValidationError("unexpected schema_version")
    if config.get("registry_id") != "distillation.external_candidate_registry.v1":
        raise ValidationError("unexpected registry_id")
    if config.get("source_ledger") != EXPECTED_SOURCE_LEDGER:
        raise ValidationError("unexpected source_ledger")
    if config.get("status") != "active_accounting_registry":
        raise ValidationError("unexpected status")

    candidates = config.get("candidates")
    if not isinstance(candidates, list) or not candidates:
        raise ValidationError("candidates must be a non-empty list")
    if len(candidates) != EXPECTED_TOTAL:
        raise ValidationError(f"expected {EXPECTED_TOTAL} candidates, found {len(candidates)}")

    seeds = [c.get("seed_candidate") for c in candidates]
    if len(seeds) != len(set(seeds)):
        raise ValidationError("duplicate seed_candidate")

    for candidate in candidates:
        validate_candidate(candidate)

    ledger_counts = Counter(c["ledger_status"] for c in candidates)
    gate_counts = Counter(c["gate_status"] for c in candidates)
    if dict(sorted(ledger_counts.items())) != EXPECTED_LEDGER_STATUS_COUNTS:
        raise ValidationError(f"unexpected ledger status counts: {dict(ledger_counts)}")
    if dict(sorted(gate_counts.items())) != EXPECTED_GATE_STATUS_COUNTS:
        raise ValidationError(f"unexpected gate status counts: {dict(gate_counts)}")

    active = [c for c in candidates if c["gate_status"] == "active_narrowing"]
    if [c["seed_candidate"] for c in active] != [EXPECTED_ACTIVE_LANE]:
        raise ValidationError("active narrowing lane must stay phase_sync_for_agents")


def build_index(config: dict[str, Any]) -> dict[str, Any]:
    validate_config(config)
    candidates = config["candidates"]
    ledger_counts = Counter(c["ledger_status"] for c in candidates)
    gate_counts = Counter(c["gate_status"] for c in candidates)
    donors = Counter(c["donor"] for c in candidates)
    return {
        "schema_version": EXPECTED_INDEX_SCHEMA,
        "registry_id": "distillation.external_candidate_registry.index.v1",
        "source_ledger": config["source_ledger"],
        "status": config["status"],
        "total_candidates": len(candidates),
        "ledger_status_counts": dict(sorted(ledger_counts.items())),
        "gate_status_counts": dict(sorted(gate_counts.items())),
        "donor_counts": dict(sorted(donors.items())),
        "active_narrowing_lanes": [
            c["seed_candidate"] for c in candidates if c["gate_status"] == "active_narrowing"
        ],
        "candidates": [
            {
                "seed_candidate": c["seed_candidate"],
                "donor": c["donor"],
                "suggested_technique_name": c["suggested_technique_name"],
                "ledger_status": c["ledger_status"],
                "gate_status": c["gate_status"],
                "tentative_domain": c["tentative_domain"],
                "atomic_move_status": c["atom_topology_gate"]["atomic_move_status"],
                "primary_kind": c["atom_topology_gate"]["primary_kind"],
            }
            for c in candidates
        ],
        "stop_line": (
            "registry accounting does not create bundles, change candidate status, "
            "or authorize import without bundle-local review"
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
        print(f"ok: {index['total_candidates']} external candidates")
        return 0
    except ValidationError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
