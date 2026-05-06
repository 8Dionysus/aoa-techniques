# AGENTS.md

Guidance for coding agents and humans working under `techniques/history/`.

## Purpose

`history/` stores technique bundles whose primary placement question is how
reviewable history, witness material, session capture, transcript structure, or
lineage artifacts remain inspectable without becoming memory doctrine.

This is a tree trunk, not a frontmatter domain. Technique bundles here may keep
their existing `domain` and `kind` values when the reviewed move is only path
architecture.

## Current Shelves

Current shelves:

- `history-artifacts/`: session capture, transcript packaging, derivative
  local indexing, witness trace review, transcript replay, and code-lineage
  links over already-saved history artifacts.

Leaf bundles stay separate: `session-capture-as-repo-artifact`,
`versionable-session-transcripts`, `local-first-session-index`,
`witness-trace-as-reviewable-artifact`, `transcript-replay-artifact`, and
`transcript-linked-code-lineage`.

## Trunk Rules

Keep the historical object explicit: what gets captured, what stays out, and
how reviewability is preserved.
Preserve the rule that memory objects and recall surfaces still stay outside
`aoa-techniques` unless the task is about the reusable capture technique
itself.
Keep examples sanitized, and keep the line between public witness material and
private transcripts visible.

## Boundary

Use `docs/TECHNIQUE_TREE_CONTRACT.md` before adding another shelf here.

Do not add `tree_path` frontmatter merely because a bundle lives under this
trunk. Do not rename trunks or shelves without a reviewed projection and a
bounded migration receipt.

If the object becomes a live memory model, a repo-local audit log, or a
project-specific retention policy, route it to the owning repository instead of
widening this technique.
If the value is mainly operational recall rather than reusable capture
structure, it does not belong here yet.

## Hard NO

Do not:

- publish private transcripts or hidden internal notes
- treat witness capture as an excuse to dump raw logs without bounded structure
- collapse reusable capture technique into memory doctrine or repo-local retention policy
- blur public-safe history surfaces with sensitive internal chronology

## Validation

After changing a history technique, run:

- `python -m pip install -r requirements-dev.txt`
- `python scripts/validate_nested_agents.py`
- `python scripts/validate_repo.py`

Run `python scripts/release_check.py` if generated reader surfaces changed.
