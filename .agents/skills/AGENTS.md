# AGENTS.md

## Applies to

This card applies to `.agents/skills/` and all descendants unless a nearer
`AGENTS.md` narrows the path.

## Role

`.agents/skills/` is a generated or exported agent-facing companion surface for
technique use.

It may help a coding agent find reusable practice quickly, but the
source-authored technique canon remains in `techniques/**/TECHNIQUE.md` and
related bundle files.

## Read before editing

Read root `AGENTS.md`, `.agents/AGENTS.md`, `DESIGN.AGENTS.md`,
`docs/guardrails/AGENTS_MESH_PROTOCOL.md`, `techniques/AGENTS.md`, and the
source technique bundle before changing this lane.

## Boundaries

- Do not turn a technique export into a new skill bundle. Skills belong in
  `aoa-skills`; this layer should describe practice primitives, validation
  patterns, docs layouts, and transfer methods.
- Do not hand-edit exported files as the first move. Change the source
  technique, export configuration, or builder, then regenerate and review the
  diff.
- Keep descriptions short, public-safe, and bounded.
- Avoid hidden project assumptions, private paths, or capability claims
  stronger than the source technique.

## Validation

Verify with:

```bash
python scripts/validate_agents_md_shape.py
python scripts/validate_repo.py
python scripts/validate_semantic_agents.py
```

## Closeout

Report the source technique, export or builder route, regenerated companion
files, validation run, skipped checks, and whether anything should be routed to
`aoa-skills` instead of staying in this companion lane.
