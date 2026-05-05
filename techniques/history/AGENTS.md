# AGENTS.md

Guidance for coding agents and humans working under `techniques/history/`.

## Purpose

This domain stores reusable techniques for preserving reviewable history, witness material, and bounded session capture.

Current compact shelf:

- `history-artifacts/`: session capture, transcript packaging, derivative
  local indexing, witness trace review, transcript replay, and code-lineage
  links over already-saved history artifacts.

Leaf bundles stay separate: `session-capture-as-repo-artifact`,
`versionable-session-transcripts`, `local-first-session-index`,
`witness-trace-as-reviewable-artifact`, `transcript-replay-artifact`, and
`transcript-linked-code-lineage`.

## Domain rules

Keep the historical object explicit: what gets captured, what stays out, and how reviewability is preserved.
Preserve the rule that memory objects and recall surfaces still stay outside `aoa-techniques` unless the task is about the reusable capture technique itself.
Keep examples sanitized, and keep the line between public witness material and private transcripts visible.

## Boundary

If the object becomes a live memory model, a repo-local audit log, or a project-specific retention policy, route it to the owning repository instead of widening this technique.
If the value is mainly operational recall rather than reusable capture structure, it does not belong here yet.

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
