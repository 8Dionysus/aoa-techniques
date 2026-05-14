#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

from agents_mesh_common import (
    AgentsMeshError,
    INDEX_SCHEMA_VERSION,
    build_agents_mesh_index,
    compact_json,
    load_mesh_config,
    repo_root_from_script,
)


def validate(repo_root: Path) -> list[str]:
    issues: list[str] = []
    config = load_mesh_config(repo_root)
    generated_path = repo_root / config["generated_ref"]
    if not generated_path.is_file():
        return [f"{config['generated_ref']}: file is missing"]

    try:
        actual = json.loads(generated_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{config['generated_ref']}: invalid JSON: {exc}"]

    if actual.get("schema_version") != INDEX_SCHEMA_VERSION:
        issues.append(
            f"{config['generated_ref']}: schema_version must be {INDEX_SCHEMA_VERSION!r}"
        )

    cards = actual.get("cards")
    if not isinstance(cards, list) or not cards:
        issues.append(f"{config['generated_ref']}: cards must be a non-empty list")
    else:
        seen_paths: set[str] = set()
        for card in cards:
            path = card.get("path")
            if not isinstance(path, str) or not path:
                issues.append(f"{config['generated_ref']}: card path must be non-empty")
                continue
            if path in seen_paths:
                issues.append(f"{config['generated_ref']}: duplicate card path {path}")
            seen_paths.add(path)
            if card.get("shape_status") not in {"canonical", "migration"}:
                issues.append(f"{path}: unsupported shape_status {card.get('shape_status')!r}")
            if card.get("first_line_ok") is not True:
                issues.append(f"{path}: first_line_ok must be true")

    expected_text = compact_json(build_agents_mesh_index(repo_root))
    actual_text = generated_path.read_text(encoding="utf-8")
    if actual_text != expected_text:
        issues.append(
            f"{config['generated_ref']} is stale; run "
            "'python scripts/build_agents_mesh_index.py'"
        )

    return issues


def main() -> int:
    repo_root = repo_root_from_script(Path(__file__))
    try:
        issues = validate(repo_root)
    except AgentsMeshError as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 1

    if issues:
        print("AGENTS mesh index validation failed.", file=sys.stderr)
        for issue in issues:
            print(f"- {issue}", file=sys.stderr)
        return 1

    print("[ok] generated AGENTS mesh index is valid and current")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
