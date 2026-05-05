# AGENTS.md

Guidance for coding agents and humans working under `techniques/execution/`.

## Purpose

`execution/` stores technique bundles whose primary placement question is how
bounded work becomes ready, sequenced, attempted, checked, or closed without
turning into hidden orchestration or project-local runtime law.

This is a tree trunk, not a frontmatter domain. Technique bundles here may keep
their existing `domain` and `kind` values when the reviewed move is only path
architecture.

## Current scope

Accepted pilot shelves:

- `ready-work-graphs/`: dependency graph authoring, blocker-free ready frontier
  derivation, and requirement-to-design-to-task layering that make the next
  bounded work slice visible before execution.

## Domain rules

Keep execution-facing techniques narrow and explicit:

- what input state makes work ready
- what the technique prepares, chooses, performs, or closes
- what later validation, proof, dispatch, scheduling, runtime, or owner-policy
  surface remains outside the bundle

Do not turn an execution technique into project-management doctrine, staffing
policy, backlog governance, hidden agent scheduling, runtime lifecycle law,
proof authority, or a broad methodology stack.

## Boundary

Use `docs/TECHNIQUE_TREE_CONTRACT.md` before adding another shelf here.

Do not add `tree_path` frontmatter merely because a bundle lives under this
trunk. Do not rename trunks or shelves without a reviewed projection and a
bounded migration receipt.

## Validation

After changing execution techniques, run:

- `python scripts/validate_nested_agents.py`
- `python scripts/validate_repo.py`

Run `python scripts/release_check.py` when generated catalogs or reader
surfaces changed.
