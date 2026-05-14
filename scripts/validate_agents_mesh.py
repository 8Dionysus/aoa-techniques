#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

from agents_mesh_common import (
    AgentsMeshError,
    canonical_card_paths,
    iter_agents_cards,
    load_mesh_config,
    posix_rel,
    repo_root_from_script,
    top_level_exemptions,
)


REQUIRED_CONFIG_REFS = (
    "authority_ref",
    "design_ref",
    "system_design_ref",
    "root_agents_ref",
    "route_contract_ref",
    "generated_ref",
)


def validate(repo_root: Path) -> list[str]:
    issues: list[str] = []
    config = load_mesh_config(repo_root)

    for key in REQUIRED_CONFIG_REFS:
        value = config.get(key)
        if not isinstance(value, str) or not value:
            issues.append(f"config/agents_mesh.json: {key} must be a non-empty path string")
            continue
        if key != "generated_ref" and not (repo_root / value).is_file():
            issues.append(f"config/agents_mesh.json: {key} target is missing: {value}")

    cards = canonical_card_paths(config)
    if len(cards) != len(set(cards)):
        issues.append("config/agents_mesh.json: canonical_cards contains duplicates")

    discovered = {posix_rel(path, repo_root) for path in iter_agents_cards(repo_root, config)}
    for rel_path in cards:
        if rel_path not in discovered:
            issues.append(f"{rel_path}: canonical AGENTS.md card is not discovered")

    migration_cards = sorted(discovered - set(cards))
    if migration_cards and not config.get("migration_allowed", False):
        issues.append(
            "config/agents_mesh.json: migration cards exist but migration_allowed is false"
        )

    exemptions = top_level_exemptions(config)
    for child in sorted(repo_root.iterdir(), key=lambda path: path.name):
        if not child.is_dir() or child.name in exemptions:
            continue
        if child.is_symlink():
            continue
        local_card = child / "AGENTS.md"
        if not local_card.is_file():
            issues.append(f"{child.name}/: durable top-level directory lacks AGENTS.md")

    return issues


def main() -> int:
    repo_root = repo_root_from_script(Path(__file__))
    try:
        issues = validate(repo_root)
    except AgentsMeshError as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 1

    if issues:
        print("AGENTS mesh validation failed.", file=sys.stderr)
        for issue in issues:
            print(f"- {issue}", file=sys.stderr)
        return 1

    print("[ok] AGENTS mesh config and top-level coverage are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
