# AGENTS.md

## Applies to

This card applies to `docs/validation/` and all descendants.

## Role

`docs/validation/` owns the active map of validation lanes, command authority,
validator inventory, script inventory, lane posture, and failure routes for
`aoa-techniques`.

It documents how guards are routed. It does not author technique meaning,
generated projection meaning, runtime policy, eval verdicts, security policy,
or sibling-repo authority.

## Read before editing

Read root `AGENTS.md`, `docs/AGENTS.md`, `docs/ROOT_SURFACE_LAW.md`,
`config/validation_lanes.json`, `scripts/validation_lanes.py`, and
`scripts/ci_gate.py`. For script-surface changes, also read
`SCRIPT_TOPOLOGY.md` and `script_inventory.json`.

For AGENTS mesh changes, also read `docs/guardrails/AGENTS_MESH_PROTOCOL.md`
and `config/agents_mesh.json`.

## Boundaries

- Do not duplicate full lane command sequences in docs.
- Do not promote advisory export, runtime, eval, or security notes into hard
  gates unless `aoa-techniques` actually owns the checked surface.
- Do not let generated validators define source meaning.
- Do not turn historical release evidence into active command authority.
- Do not let `script_inventory.json` become command authority; it describes
  owner, lane, side-effect, and test coverage only.

## Validation

Run:

```bash
python -m unittest tests.test_validation_topology tests.test_validation_command_authority tests.test_script_topology
python scripts/ci_gate.py --mode source-fast
```

For release-visible lane changes, run:

```bash
python scripts/release_check.py
```

## Closeout

Report changed lane ids, command-authority surfaces, validator/script inventory
entries, generated mirrors rebuilt, checks run, checks skipped, and any
advisory boundary that was intentionally not promoted to a hard gate.
