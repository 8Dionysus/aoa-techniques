#!/usr/bin/env python3
"""Validate selected AGENTS.md route-card completeness.

This guard checks selected card paths and delegates route semantics to the
canonical AGENTS mesh helper. It does not treat prose keywords as proof of
meaning, public safety, or owner acceptance.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]

if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.agents_mesh_common import active_card_route_issues


ROUTE_HANDLES = ("VALIDATION.md", "config/validation_lanes.json")


@dataclass(frozen=True)
class AgentsDocSpec:
    path: Path
    # Kept as compatibility metadata for callers that inspect the old field.
    # Route semantics are owned by active_card_route_issues(), not by literal
    # prose matching in this module.
    required_snippets: tuple[str, ...]


REQUIRED_DOCS: tuple[AgentsDocSpec, ...] = (
    AgentsDocSpec(
        Path('config/AGENTS.md'),
        ROUTE_HANDLES,
    ),
    AgentsDocSpec(
        Path('examples/AGENTS.md'),
        ROUTE_HANDLES,
    ),
    AgentsDocSpec(
        Path('mechanics/distillation/parts/candidate-intake/AGENTS.md'),
        ROUTE_HANDLES,
    ),
    AgentsDocSpec(
        Path('mechanics/distillation/parts/technique-reform-ingress/reports/AGENTS.md'),
        ROUTE_HANDLES,
    ),
    AgentsDocSpec(
        Path('schemas/AGENTS.md'),
        ROUTE_HANDLES,
    ),
    AgentsDocSpec(
        Path('scripts/AGENTS.md'),
        ROUTE_HANDLES,
    ),
    AgentsDocSpec(
        Path('tests/AGENTS.md'),
        ROUTE_HANDLES,
    ),
)


def _display(path: Path, repo_root: Path) -> str:
    try:
        return path.relative_to(repo_root).as_posix()
    except ValueError:
        return path.as_posix()


def validate(repo_root: Path = REPO_ROOT) -> list[str]:
    issues: list[str] = []
    for spec in REQUIRED_DOCS:
        path = repo_root / spec.path
        if not path.is_file():
            issues.append(f"{spec.path.as_posix()}: file is missing")
            continue
        text = path.read_text(encoding="utf-8")
        if not text.strip().startswith("# AGENTS.md"):
            issues.append(f"{spec.path.as_posix()}: must start with '# AGENTS.md'")
        issues.extend(
            f"{spec.path.as_posix()}: {issue}"
            for issue in active_card_route_issues(text)
        )
    return issues


def main() -> int:
    issues = validate(REPO_ROOT)
    if issues:
        print("Selected AGENTS route-card validation failed.", file=sys.stderr)
        for issue in issues:
            print(f"- {issue}", file=sys.stderr)
        return 1
    print(
        "[ok] selected AGENTS route-card docs are present and structurally shaped: "
        f"{len(REQUIRED_DOCS)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
