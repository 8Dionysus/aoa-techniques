#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from agents_mesh_common import (
    AgentsMeshError,
    build_agents_mesh_index,
    compact_json,
    load_mesh_config,
    repo_root_from_script,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build the generated AGENTS mesh index for aoa-techniques."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="check that generated/agents_mesh.min.json is current",
    )
    args = parser.parse_args()

    repo_root = repo_root_from_script(Path(__file__))
    try:
        config = load_mesh_config(repo_root)
        payload = build_agents_mesh_index(repo_root)
    except AgentsMeshError as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 1

    generated_path = repo_root / config["generated_ref"]
    expected = compact_json(payload)

    if args.check:
        if not generated_path.is_file():
            print(f"[error] {config['generated_ref']}: file is missing", file=sys.stderr)
            return 1
        actual = generated_path.read_text(encoding="utf-8")
        if actual != expected:
            print(
                f"[error] {config['generated_ref']} is stale; run "
                "'python scripts/build_agents_mesh_index.py'",
                file=sys.stderr,
            )
            return 1
        print(f"[ok] {config['generated_ref']} is current")
        return 0

    generated_path.parent.mkdir(parents=True, exist_ok=True)
    generated_path.write_text(expected, encoding="utf-8")
    print(f"[ok] wrote {config['generated_ref']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
