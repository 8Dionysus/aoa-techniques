# AGENTS.md

Guidance for coding agents and humans working under `techniques/docs/`.

## Purpose

This domain stores documentation and source-lift techniques: how rules are distributed, how provenance is preserved, and how bounded reader surfaces are formed from authored sources.

Representative bundles here include `nested-rule-loading`, `single-source-rule-distribution`, `source-of-truth-layout`, `markdown-technique-section-lift`, `repo-doc-surface-lift`, and `semantic-review-surface-lift`.

## Domain rules

Keep the technique about documentation posture, provenance, or source-lift structure.
Preserve explicit ownership boundaries between authored docs and derived surfaces.
Keep examples public-safe and sanitized, especially when the technique touches prompts, review notes, or artifact export.

## Boundary

Do not smuggle hidden execution policy into a docs technique.
Do not widen a documentation technique into graph semantics, runtime orchestration, or a repo-specific workflow unless the authored bundle already states that contract clearly.
If the change is really about live repo docs or generated manifests, edit those surfaces directly and keep the technique reusable.

## Hard NO

Do not:

- treat derived docs as the primary source of truth
- copy project-private context into a supposedly portable docs technique
- erase provenance language that keeps lifts bounded
- collapse distinct techniques such as `nested-rule-loading` and `single-source-rule-distribution` into one blurred idea

## Validation

After changing a docs technique, run:

- `python scripts/validate_nested_agents.py`
- `python scripts/validate_repo.py`

Run `python scripts/release_check.py` when the change affects generated reader surfaces.
