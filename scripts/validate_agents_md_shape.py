#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

from agents_mesh_common import (
    AgentsMeshError,
    canonical_card_paths,
    headings_in_order,
    iter_agents_cards,
    load_mesh_config,
    missing_required_headings,
    posix_rel,
    repo_root_from_script,
    required_headings,
    section_body,
)


def validate(repo_root: Path) -> list[str]:
    issues: list[str] = []
    config = load_mesh_config(repo_root)
    canonical = set(canonical_card_paths(config))
    required = required_headings(config)
    discovered = {posix_rel(path, repo_root): path for path in iter_agents_cards(repo_root, config)}

    for rel_path, path in discovered.items():
        text = path.read_text(encoding="utf-8")
        first_line = text.splitlines()[0] if text.splitlines() else ""
        if first_line != "# AGENTS.md":
            issues.append(f"{rel_path}: first line must be '# AGENTS.md'")

    for rel_path in sorted(canonical):
        path = repo_root / rel_path
        if not path.is_file():
            issues.append(f"{rel_path}: canonical card is missing")
            continue

        text = path.read_text(encoding="utf-8")
        missing = missing_required_headings(text, required)
        if missing:
            issues.append(f"{rel_path}: missing canonical headings {', '.join(missing)}")
        elif not headings_in_order(text, required):
            issues.append(f"{rel_path}: canonical headings must appear in configured order")

        boundary = section_body(text, "## Boundaries")
        if "Do not" not in boundary and "do not" not in boundary:
            issues.append(f"{rel_path}: Boundaries section must contain an explicit do-not rule")

        validation = section_body(text, "## Validation")
        if "python " not in validation and "pytest" not in validation:
            issues.append(f"{rel_path}: Validation section must name an executable check")

        closeout = section_body(text, "## Closeout")
        if len(closeout.split()) < 8:
            issues.append(f"{rel_path}: Closeout section must give a useful report contract")

    return issues


def main() -> int:
    repo_root = repo_root_from_script(Path(__file__))
    try:
        issues = validate(repo_root)
    except AgentsMeshError as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 1

    if issues:
        print("AGENTS.md shape validation failed.", file=sys.stderr)
        for issue in issues:
            print(f"- {issue}", file=sys.stderr)
        return 1

    print("[ok] AGENTS.md canonical and migration cards are shaped")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
