#!/usr/bin/env python3
"""Validate required nested AGENTS.md documents for aoa-techniques."""

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
        Path("techniques") / "AGENTS.md",
        (
            "# AGENTS.md",
            "`TECHNIQUE.md`",
            "`checks/`, `examples/`, and `notes/`",
            "Do not add bundle-local `AGENTS.md` by default",
            "`python scripts/validate_repo.py`",
        ),
    ),
    AgentsDocSpec(
        Path("techniques") / "agent-workflows" / "AGENTS.md",
        (
            "# AGENTS.md",
            "`plan-diff-apply-verify-report`",
            "`render-truth-before-startup`",
            "explicit dry-run",
            "small reversible slice",
        ),
    ),
    AgentsDocSpec(
        Path("techniques") / "docs" / "AGENTS.md",
        (
            "# AGENTS.md",
            "`nested-rule-loading`",
            "`single-source-rule-distribution`",
            "`source-of-truth-layout`",
            "documentation posture",
        ),
    ),
    AgentsDocSpec(
        Path("techniques") / "evaluation" / "AGENTS.md",
        (
            "# AGENTS.md",
            "`contract-test-design`",
            "`property-invariants`",
            "`signal-first-gate-promotion`",
            "proof posture",
            "`aoa-evals`",
        ),
    ),
    AgentsDocSpec(
        Path("techniques") / "history" / "AGENTS.md",
        (
            "# AGENTS.md",
            "`session-capture-as-repo-artifact`",
            "`versionable-session-transcripts`",
            "`witness-trace-as-reviewable-artifact`",
            "memory objects and recall surfaces still stay outside",
            "private transcripts",
        ),
    ),
    AgentsDocSpec(
        Path("generated") / "AGENTS.md",
        (
            "# AGENTS.md",
            "`generated/technique_catalog.json`",
            "`generated/technique_capsules.json`",
            "`generated/repo_doc_surface_manifest.json`",
            "`generated/kag_export.json`",
            "Do not hand-edit",
            "`python scripts/build_catalog.py`",
        ),
    ),
    AgentsDocSpec(
        Path("templates") / "AGENTS.md",
        (
            "# AGENTS.md",
            "`TECHNIQUE.template.md`",
            "`ADAPTATION_NOTE.template.md`",
            "`PROMOTION_NOTE.template.md`",
            "Preserve placeholders",
            "`python scripts/validate_nested_agents.py`",
        ),
    ),
)


def validate(repo_root: Path) -> list[str]:
    issues: list[str] = []
    for spec in REQUIRED_DOCS:
        path = repo_root / spec.path
        if not path.is_file():
            issues.append(f"{spec.path.as_posix()}: file is missing")
            continue

        text = path.read_text(encoding="utf-8")
        for snippet in spec.required_snippets:
            if snippet not in text:
                issues.append(f"{spec.path.as_posix()}: missing snippet {snippet!r}")

    return issues


def main() -> int:
    issues = validate(REPO_ROOT)
    if issues:
        print("Nested AGENTS validation failed:", file=sys.stderr)
        for issue in issues:
            print(f"- {issue}", file=sys.stderr)
        return 1

    print("[ok] nested AGENTS docs are present and shaped")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
