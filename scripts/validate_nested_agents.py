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
            "`techniques/<trunk>/<shelf>/<slug>/TECHNIQUE.md`",
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
            "retained frontmatter review lane",
            "no active leaf bundle currently lives directly here",
            "`techniques/governance/practice-adoption-lifecycle/`",
            "`techniques/tool-use/tool-gateway/`",
            "explicit dry-run",
            "small reversible slice",
        ),
    ),
    AgentsDocSpec(
        Path("techniques") / "continuity" / "AGENTS.md",
        (
            "# AGENTS.md",
            "This is a tree trunk, not a frontmatter domain",
            "`review-compaction/`",
            "`handoff-continuation/`",
            "`donor-harvest/`",
            "without granting memory, playbook, or progression authority",
            "Do not turn a continuity technique",
        ),
    ),
    AgentsDocSpec(
        Path("techniques") / "execution" / "AGENTS.md",
        (
            "# AGENTS.md",
            "This is a tree trunk, not a frontmatter domain",
            "`ready-work-graphs/`",
            "`intent-chain/`",
            "`agent-workflows-core/`",
            "`runtime-truth-lifecycle/`",
            "hidden orchestration",
            "benchmark-suite governance",
        ),
    ),
    AgentsDocSpec(
        Path("techniques") / "governance" / "AGENTS.md",
        (
            "# AGENTS.md",
            "This is a tree trunk, not a frontmatter domain",
            "`decision-routing/`",
            "`approval-evidence/`",
            "`automation-readiness/`",
            "`promotion-boundary/`",
            "`practice-adoption-lifecycle/`",
            "AoA constitutional authority",
            "proof verdict authority",
        ),
    ),
    AgentsDocSpec(
        Path("techniques") / "history" / "AGENTS.md",
        (
            "# AGENTS.md",
            "This is a tree trunk, not a frontmatter domain",
            "`session-capture-as-repo-artifact`",
            "`versionable-session-transcripts`",
            "`witness-trace-as-reviewable-artifact`",
            "memory objects and recall surfaces still stay outside",
            "private transcripts",
            "`docs/TECHNIQUE_TREE_CONTRACT.md`",
        ),
    ),
    AgentsDocSpec(
        Path("techniques") / "ingest" / "AGENTS.md",
        (
            "# AGENTS.md",
            "This is a tree trunk, not a frontmatter domain",
            "`media-ingest/`",
            "source material",
            "reviewable intermediate object",
            "live connector",
        ),
    ),
    AgentsDocSpec(
        Path("techniques") / "instruction" / "AGENTS.md",
        (
            "# AGENTS.md",
            "This is a tree trunk, not a frontmatter domain",
            "`instruction-surface/`",
            "`docs-boundary/`",
            "`capability-registry/`",
            "`capability-boundary/`",
            "`skill-discovery/`",
            "source of truth",
            "Do not turn an instruction technique into AoA doctrine",
        ),
    ),
    AgentsDocSpec(
        Path("techniques") / "knowledge-lift" / "AGENTS.md",
        (
            "# AGENTS.md",
            "This is a tree trunk, not a frontmatter domain",
            "`kag-source-lift/`",
            "authored source remains authoritative",
            "`aoa-kag` owner doctrine",
            "generated source-of-truth replacement",
        ),
    ),
    AgentsDocSpec(
        Path("techniques") / "proof" / "AGENTS.md",
        (
            "# AGENTS.md",
            "This is a tree trunk, not a frontmatter domain",
            "`skill-support/`",
            "`evaluation-chain/`",
            "`published-summary/`",
            "`review-evidence/`",
            "`owner-truth-closeout/`",
            "`aoa-evals`",
            "proof verdict authority",
            "CI ownership",
            "dashboard ownership",
            "runtime storage policy",
            "public-share approval policy",
            "Do not widen a proof technique",
        ),
    ),
    AgentsDocSpec(
        Path("techniques") / "recovery" / "AGENTS.md",
        (
            "# AGENTS.md",
            "This is a tree trunk, not a frontmatter domain",
            "`diagnosis-repair/`",
            "`antifragility-recovery/`",
            "validation-shaped leaves",
            "runtime self-healing",
        ),
    ),
    AgentsDocSpec(
        Path("techniques") / "tool-use" / "AGENTS.md",
        (
            "# AGENTS.md",
            "This is a tree trunk, not a frontmatter domain",
            "`tool-gateway/`",
            "caller-facing surface",
            "metadata",
            "security-scanner",
            "`aoa-skills`",
            "`aoa-evals`",
        ),
    ),
    AgentsDocSpec(
        Path("techniques") / "docs" / "AGENTS.md",
        (
            "# AGENTS.md",
            "retained frontmatter review lane",
            "No active leaf bundles currently live directly here",
            "`techniques/proof/`",
            "documentation posture",
        ),
    ),
    AgentsDocSpec(
        Path("techniques") / "evaluation" / "AGENTS.md",
        (
            "# AGENTS.md",
            "retained frontmatter review lane",
            "No active leaf bundles currently live directly here",
            "`techniques/proof/`",
            "`techniques/execution/`",
            "proof posture",
            "`aoa-evals`",
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
