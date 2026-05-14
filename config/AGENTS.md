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
and the AGENTS mesh config. Scout-only Distillation inputs for
technique-reform review live under
`mechanics/distillation/parts/technique-reform-ingress/config/`.

## Read before editing

Read root `AGENTS.md`, `DESIGN.md`, `DESIGN.AGENTS.md`, `docs/START_HERE.md`,
and the source doc or generated surface that consumes the changed config.

For `config/agents_mesh.json`, also read
`docs/guardrails/AGENTS_MESH_PROTOCOL.md`.

## Boundaries

- Do not use config as a hidden doctrine surface.
- Do not add hidden environment assumptions, private paths, local host state, or
  policy that only one machine understands.
- Do not loosen repo-wide config merely to make a broken generated surface pass.
- Do not move mechanic-local config back into root config.

## Validation

When config changes generated surfaces, rebuild the affected catalogs and
inspect the diff for meaning drift.

Common checks:

```bash
python scripts/validate_agents_mesh.py
python scripts/build_agents_mesh_index.py --check
python scripts/validate_repo.py
python scripts/validate_semantic_agents.py
```

## Closeout

Report changed config files, affected generated surfaces, source surfaces
consulted, validation run, validation skipped, and any downstream consumer that
needs review.
