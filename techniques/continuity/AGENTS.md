# AGENTS.md

Guidance for coding agents and humans working under `techniques/continuity/`.

## Purpose

`continuity/` stores technique bundles whose primary placement question is how
working context, review truth, handoff state, donor material, or capability
availability survives a state boundary.

This is a tree trunk, not a frontmatter domain. Technique bundles here may keep
their existing `domain` and `kind` values when the reviewed move is only path
architecture.

## Current scope

The first accepted pilot shelf is `review-compaction/`.

It contains techniques for preserving or restoring review and capability
context across commit, compaction, or repeated-review boundaries.

## Domain rules

Keep the continuity object explicit:

- what state crosses the boundary
- what evidence or capability must remain inspectable
- what stale, noisy, or missing context is being reduced
- what the technique refuses to reconstruct or govern

Do not turn a continuity technique into a live skill, phase system, memory
policy, or review verdict contract.

## Boundary

Use `docs/TECHNIQUE_TREE_CONTRACT.md` before adding another shelf here.

Do not add `tree_path` frontmatter merely because a bundle lives under this
trunk. Do not rename trunks or shelves without a reviewed projection and a
bounded migration receipt.

## Validation

After changing continuity techniques, run:

- `python scripts/validate_nested_agents.py`
- `python scripts/validate_repo.py`

Run `python scripts/release_check.py` when generated catalogs or reader
surfaces changed.
