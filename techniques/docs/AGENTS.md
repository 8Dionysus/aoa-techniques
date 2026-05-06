# AGENTS.md

Guidance for coding agents and humans working under `techniques/docs/`.

## Purpose

`docs/` remains a retained frontmatter review lane for documentation,
provenance, boundary, and source-surface techniques.

No active leaf bundles currently live directly here after reviewed tree
migrations. Docs-frontmatter bundles may live under `techniques/instruction/`,
`techniques/knowledge-lift/`, or `techniques/proof/` when a reviewed tree
migration places them there without changing their frontmatter domain.

This is a retained lane, not a current tree shelf. Use it when old links,
frontmatter `domain`, or migration reviews need docs provenance, then route new
authored leaves into the current tree through `docs/TECHNIQUE_TREE_CONTRACT.md`.

## Lane Rules

Keep the technique about documentation posture, provenance, or source-lift
structure.
Preserve explicit ownership boundaries between authored docs and derived
surfaces.
Keep examples public-safe and sanitized, especially when the technique touches
prompts, review notes, or artifact export.

## Boundary

Do not add a new leaf bundle directly under this lane unless a reviewed tree
projection proves that broad docs placement is again the honest authored home.

Do not smuggle hidden execution policy into a docs technique.
Do not widen a documentation technique into graph semantics, runtime
orchestration, or a repo-specific workflow unless the authored bundle already
states that contract clearly.
If the placement question is derived source-lift into bounded reader knowledge,
check `techniques/knowledge-lift/AGENTS.md` before adding or moving a bundle.
If the change is really about live repo docs or generated manifests, edit those surfaces directly and keep the technique reusable.

## Hard NO

Do not:

- treat derived docs as the primary source of truth
- copy project-private context into a supposedly portable docs technique
- erase provenance language that keeps lifts bounded
- collapse distinct techniques such as `nested-rule-loading` and `single-source-rule-distribution` into one blurred idea

## Validation

Before validator or release-check commands here, run
`python -m pip install -r requirements-dev.txt`.

After changing a docs technique, run:

- `python scripts/validate_nested_agents.py`
- `python scripts/validate_repo.py`

Run `python scripts/release_check.py` when the change affects generated reader surfaces.
