#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from build_cross_layer_candidate_registry import (  # noqa: E402
    CONFIG_PATH,
    GENERATED_PATH,
    ValidationError,
    build_index,
    read_json,
    validate_config,
)


def main() -> int:
    try:
        config = read_json(CONFIG_PATH)
        validate_config(config)
        expected = build_index(config)
        actual = read_json(GENERATED_PATH)
        if actual != expected:
            raise ValidationError(f"{GENERATED_PATH} is stale; rerun builder")
        print(f"ok: {expected['total_candidates']} cross-layer candidates validated")
        return 0
    except ValidationError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
