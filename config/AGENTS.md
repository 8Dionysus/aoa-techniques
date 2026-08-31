# AGENTS.md

## Applies to

This card applies to `config/` and all descendants unless a nearer `AGENTS.md`
narrows the path.

## Role

`config/` holds policy, export, and build inputs for the technique canon.

Use config to tune publication and generation behavior, not to author technique
meaning. Technique meaning belongs in `TECHNIQUE.md`, checks, examples, notes,
and source-owned docs.

Root config is for repo-wide contract inputs such as the current kind registry
the AGENTS mesh config, and validation lane command authority in
`config/validation_lanes.json`. Scout-only Distillation inputs for
technique-reform review live under
`mechanics/distillation/parts/technique-reform-ingress/config/`.

## Read before editing

Read root `AGENTS.md`, `DESIGN.md`, `DESIGN.AGENTS.md`, `docs/START_HERE.md`,
and the source doc or generated surface that consumes the changed config.

For `config/agents_mesh.json`, also read
`docs/guardrails/AGENTS_MESH_PROTOCOL.md`.
Read `README.md` only when the selected task needs its human map; do not preload unrelated maps.

## Boundaries

- Do not use config as a hidden doctrine surface.
- Do not add hidden environment assumptions, private paths, local host state, or
  policy that only one machine understands.
- Do not loosen repo-wide config merely to make a broken generated surface pass.
- Do not move mechanic-local config back into root config.

## Validation

Select the narrowest owner route: `source-fast` for authored or route-card work; add `generated` for projections and `release` only for release posture. See [VALIDATION.md](../VALIDATION.md); exact order is `config/validation_lanes.json`; focused procedure stays with the nearest owner. Report checks, skips, and blockers.

## Closeout

Report changed config files, affected generated surfaces, source surfaces
consulted, validation run, validation skipped, and any downstream consumer that
needs review.
