#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "agon_technique_binding_candidates.seed.json"
GENERATED_PATH = ROOT / "generated" / "agon_technique_binding_candidates.min.json"
EXPECTED_SCHEMA_VERSION = "agon-technique-binding-candidates.seed/0.1"
EXPECTED_INDEX_SCHEMA = "agon-technique-binding-candidates-index/0.1"
EXPECTED_BRIDGE_KIND = "practice_candidate"
EXPECTED_TOTAL = 12
EXPECTED_REPO = "aoa-techniques"
REQUIRED_MUST_NOT_BOUNDARIES = (
    "lawful move vocabulary",
    "create skill workflow",
    "proof verdict",
    "scars",
    "arena",
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


def validate_config(config: dict[str, Any]) -> None:
    if config.get("schema_version") != EXPECTED_SCHEMA_VERSION:
        raise ValidationError("unexpected schema_version")
    if config.get("wave") != "IV":
        raise ValidationError("wave must be IV")
    if config.get("status") != "owner_repo_candidate_requests":
        raise ValidationError("unexpected status")

    candidates = config.get("candidates")
    if not isinstance(candidates, list) or not candidates:
        raise ValidationError("candidates must be a non-empty list")
    if len(candidates) != EXPECTED_TOTAL:
        raise ValidationError(f"expected {EXPECTED_TOTAL} candidates, found {len(candidates)}")

    ids = [c.get("candidate_id") for c in candidates]
    if len(ids) != len(set(ids)):
        raise ValidationError("duplicate candidate_id")

    expected_prefix = f"candidate:{EXPECTED_REPO}:agon/"
    for candidate in candidates:
        cid = candidate.get("candidate_id", "")
        if not cid.startswith(expected_prefix):
            raise ValidationError(f"{cid}: wrong candidate namespace")
        if candidate.get("status") != "requested_not_landed":
            raise ValidationError(f"{cid}: status must be requested_not_landed")
        if candidate.get("bridge_kind") != EXPECTED_BRIDGE_KIND:
            raise ValidationError(f"{cid}: bridge_kind must be {EXPECTED_BRIDGE_KIND}")
        if not candidate.get("move_id", "").startswith("agon.move."):
            raise ValidationError(f"{cid}: invalid move_id")
        must_not = " ".join(candidate.get("must_not", [])).lower()
        for forbidden in REQUIRED_MUST_NOT_BOUNDARIES:
            if forbidden not in must_not:
                raise ValidationError(f"{cid}: must_not must preserve {forbidden!r} boundary")


def build_index(config: dict[str, Any]) -> dict[str, Any]:
    validate_config(config)
    counts = Counter(c["move_class"] for c in config["candidates"])
    return {
        "schema_version": EXPECTED_INDEX_SCHEMA,
        "wave": "IV",
        "title": "Agon technique binding candidate index",
        "status": config["status"],
        "total_candidates": len(config["candidates"]),
        "source_owner_binding_registry": config["source_owner_binding_registry"],
        "move_classes": dict(sorted(counts.items())),
        "candidates": [
            {
                "candidate_id": c["candidate_id"],
                "move_id": c["move_id"],
                "move_name": c["move_name"],
                "move_class": c["move_class"],
                "status": c["status"],
                "bridge_kind": c["bridge_kind"],
            }
            for c in config["candidates"]
        ],
        "stop_line": (
            "candidate requests do not create promoted techniques, promoted skills, live arena protocol, "
            "verdicts, scars, retention, or ToS promotion"
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
        print(f"ok: {index['total_candidates']} {EXPECTED_BRIDGE_KIND} candidates")
        return 0
    except ValidationError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
