#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

PART_ROOT = Path(__file__).resolve().parents[1]
BUILDER = PART_ROOT / "scripts" / "build_agon_candidate_handoff.py"


def load_builder():
    spec = importlib.util.spec_from_file_location("agon_candidate_handoff_builder", BUILDER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load builder from {BUILDER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    builder = load_builder()
    try:
        config = builder.read_json(builder.CONFIG_PATH)
        builder.build_index(config)
        print("ok: Agon candidate handoff registry validates")
        return 0
    except builder.ValidationError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
