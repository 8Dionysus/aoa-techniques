#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import sys
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / "config" / "agon_epistemic_technique_candidates.seed.json"
OUT = ROOT / "generated" / "agon_epistemic_technique_candidates.min.json"
ITEM_KEY = "techniques"
REGISTRY_ID = "agon.epistemic_technique_candidates.registry.v1"
WAVE = "XV"
RUNTIME_POSTURE = "candidate_only"
REQUIRED_SOURCE_FIELDS = ("registry_id", "wave", "runtime_posture", ITEM_KEY)


class BuildError(ValueError):
    pass


def digest_obj(obj: Any) -> str:
    payload = json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def compact(obj: Any) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"


def load_source() -> dict[str, Any]:
    if not SRC.exists():
        raise BuildError(f"missing source {SRC}")
    data = json.loads(SRC.read_text(encoding="utf-8"))
    for field in REQUIRED_SOURCE_FIELDS:
        if field not in data:
            raise BuildError(f"missing source field {field}")
    if data["registry_id"] != REGISTRY_ID:
        raise BuildError(f"registry_id must be {REGISTRY_ID}")
    if data["wave"] != WAVE:
        raise BuildError(f"wave must be {WAVE}")
    if data["runtime_posture"] != RUNTIME_POSTURE:
        raise BuildError(f"runtime_posture must be {RUNTIME_POSTURE}")
    if not isinstance(data[ITEM_KEY], list):
        raise BuildError(f"{ITEM_KEY} must be an array")
    return data


def build() -> dict[str, Any]:
    data = load_source()
    items = data[ITEM_KEY]
    return {
        "registry_id": REGISTRY_ID,
        "wave": WAVE,
        "runtime_posture": RUNTIME_POSTURE,
        "count": len(items),
        ITEM_KEY: items,
        "digest": digest_obj(items),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        rendered = compact(build())
    except BuildError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    if args.check:
        if not OUT.exists():
            print(f"missing generated registry {OUT}", file=sys.stderr)
            return 1
        if OUT.read_text(encoding="utf-8") != rendered:
            print("generated registry drift: run this builder without --check", file=sys.stderr)
            return 1
        return 0
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(rendered, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
