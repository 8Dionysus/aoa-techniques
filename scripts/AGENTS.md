# AGENTS.md

## Applies to

This card applies to `scripts/` and all descendants unless a nearer
`AGENTS.md` narrows the path.

## Role

`scripts/` contains deterministic builders, validators, test runners,
promotion helpers, and report tools for repo-wide technique canon surfaces.

Scripts that only serve one mechanic part belong beside that part under
`mechanics/<slug>/parts/<part>/scripts/`.

Repo-wide `validate_repo` rule implementation belongs under
`scripts/validators/`. Keep `scripts/validate_repo.py` as a compatibility
CLI/re-export adapter.

## Read before editing

Read root `AGENTS.md`, `docs/START_HERE.md`, the source surfaces consumed by
the script, the generated surfaces it writes, and the tests or validators that
cover it. Also read `docs/validation/SCRIPT_TOPOLOGY.md` and
`docs/validation/script_inventory.json` before adding, moving, deleting, or
changing the owner/lane/side-effect posture of a script.

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
- Do not leave a script without an inventory entry naming owner source, lane,
  side effects, CI inclusion, and focused test target.

## Validation

Full lane command sequences live in `config/validation_lanes.json`;
`scripts/validation_lanes.py` is the loader/API, and `scripts/ci_gate.py` is the
CI lane executor. Keep root entrypoints thin and verify with:

```bash
python -m unittest tests.test_validator_module_topology tests.test_script_topology
python scripts/ci_gate.py --mode source-fast
python scripts/validate_source_contracts.py
python scripts/validate_agents_md_shape.py
python scripts/validate_agents_mesh.py
python scripts/build_agents_mesh_index.py --check
python scripts/validate_agents_mesh_index.py
python scripts/validate_repo.py
```

## Closeout

Report changed scripts, source inputs, generated outputs, tests or validators
run, skipped checks, and whether a release-check rerun is needed for generated
parity.
