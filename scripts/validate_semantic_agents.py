#!/usr/bin/env python3
"""Validate Pack 4 semantic-layer AGENTS.md guidance for aoa-techniques."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class AgentsDocSpec:
    path: Path
    required_snippets: tuple[str, ...]


REQUIRED_DOCS: tuple[AgentsDocSpec, ...] = (
    AgentsDocSpec(
        Path('config/AGENTS.md'),
        (
            'policy',
            'export',
            'TECHNIQUE.md',
            'generated surfaces',
            'validation_lanes.json',
        ),
    ),
    AgentsDocSpec(
        Path('examples/AGENTS.md'),
        (
            'technique canon',
            'public-safe',
            'adaptation boundary',
            'No secrets',
            'validate_repo.py',
        ),
    ),
    AgentsDocSpec(
        Path('mechanics/distillation/parts/candidate-intake/AGENTS.md'),
        (
            'quarantine',
            'candidate',
            'provenance',
            'public-safe',
            'Promotion',
        ),
    ),
    AgentsDocSpec(
        Path('mechanics/distillation/parts/technique-reform-ingress/reports/AGENTS.md'),
        (
            'diagnostic surfaces',
            'source-authored bundles',
            'bounded',
            'aoa-evals',
            'validate_repo.py',
        ),
    ),
    AgentsDocSpec(
        Path('schemas/AGENTS.md'),
        (
            'Schema edits are contract edits',
            '$schema',
            'paired examples',
            'downstream consumer',
            'validate_repo.py',
        ),
    ),
    AgentsDocSpec(
        Path('scripts/AGENTS.md'),
        (
            'deterministic builders',
            'repo-relative',
            'generated summaries',
            'validators',
            'ci_gate.py',
        ),
    ),
    AgentsDocSpec(
        Path('tests/AGENTS.md'),
        (
            'technique contracts',
            'generated parity',
            'public-safe',
            'python scripts/run_tests.py',
            'validate_semantic_agents.py',
        ),
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
        for snippet in spec.required_snippets:
            if snippet not in text:
                issues.append(
                    f"{spec.path.as_posix()}: missing required snippet {snippet!r}"
                )
    return issues


def main() -> int:
    issues = validate(REPO_ROOT)
    if issues:
        print("Pack 4 semantic AGENTS validation failed.", file=sys.stderr)
        for issue in issues:
            print(f"- {issue}", file=sys.stderr)
        return 1
    print(f"[ok] Pack 4 semantic AGENTS docs are present and shaped: {len(REQUIRED_DOCS)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
