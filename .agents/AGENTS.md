# AGENTS.md

## Applies to

This card applies to `.agents/` and all descendants unless a nearer
`AGENTS.md` narrows the path.

## Role

`.agents/` holds agent-facing companion lanes for `aoa-techniques`.

It can expose practice-canon help to local agents, but it does not author
technique meaning, skill workflow meaning, proof authority, route dispatch, or
runtime state.

## Read before editing

Read root `AGENTS.md`, `DESIGN.AGENTS.md`,
`docs/guardrails/AGENTS_MESH_PROTOCOL.md`, and the nearest lane card before
changing files here.

For a registered Spark scenario, also read its `PROMPT.md` and
`registry.json` entry when that scenario is relevant to the task.

For technique-facing help, also read `techniques/AGENTS.md`,
`TECHNIQUE_INDEX.md`, and the selected source `TECHNIQUE.md` bundle.
Read `README.md` only when the selected task needs its human map; do not preload unrelated maps.

## Boundaries

- Do not create `.agents/skills/` as a local cache of shared AoA bundles.
- Do not create an empty top-level `skills/` home. A future repository-owned
  bundle must first pass the admission boundary in root `AGENTS.md`.
- Use host or user-profile projections for shared skills; use authored
  technique routes and source-returning derived readers for technique help.
- Do not hand-edit generated companion content as the first move.
- Do not make agent lanes stronger than the source technique, docs, schemas,
  builders, or owning AoA repository.
- Do not add private project assumptions, secrets, local host paths, or hidden
  capability claims.

## Validation

Inherit parent validation: source-fast/generated; see [VALIDATION.md](../VALIDATION.md) and config/validation_lanes.json.

## Closeout

Report changed agent lanes, source technique or builder surfaces consulted,
generated or exported companions rebuilt or left untouched, validation run,
validation skipped, and any remaining migration-card risk.
