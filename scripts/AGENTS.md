# AGENTS.md

## Applies to

This card applies to `scripts/` and all descendants unless a nearer
`AGENTS.md` narrows the path.

## Role

`scripts/` contains deterministic builders, validators, test runners,
promotion helpers, and report tools for repo-wide technique canon surfaces.

Scripts that only serve one mechanic part belong beside that part under
`mechanics/<slug>/parts/<part>/scripts/`.

## Read before editing

Read root `AGENTS.md`, `docs/START_HERE.md`, the source surfaces consumed by
the script, the generated surfaces it writes, and the tests or validators that
cover it.

For agent mesh scripts, also read `DESIGN.AGENTS.md`,
`docs/guardrails/AGENTS_MESH_PROTOCOL.md`, and `config/agents_mesh.json`.

## Boundaries

- Keep scripts repo-relative and reproducible.
- Avoid hidden network calls, private paths, ambient credentials, and
  machine-local assumptions unless the command explicitly documents them.
- Preserve the distinction between authored technique bundles and generated
  summaries. Generated summaries do not become the canon.
- Keep generated summaries subordinate to authored sources.
- When editing validators, prefer precise failures that name the file, field,
  and owner surface.
- Do not weaken validators to make a bad corpus pass.

## Validation

Verify with:

```bash
python scripts/validate_agents_md_shape.py
python scripts/validate_agents_mesh.py
python scripts/build_agents_mesh_index.py --check
python scripts/validate_agents_mesh_index.py
python scripts/validate_repo.py
python scripts/validate_semantic_agents.py
```

## Closeout

Report changed scripts, source inputs, generated outputs, tests or validators
run, skipped checks, and whether a release-check rerun is needed for generated
parity.
