# Script Surface Inventory

Status: accepted
Date: 2026-06-03

## Index Metadata

- Decision ID: AOA-TECH-D-0068
- Original date: 2026-06-03
- Surface classes: validation guard, release/tooling, docs route
- Technique axes: validation lane
- Mechanic parents: release-support
- Guard families: script topology, command authority, generated/read-model, source contract
- Posture: accepted

## Context

After the validator and test topology split, `aoa-techniques` still had a
broader script problem: root scripts, validator modules, Spark lane scripts,
exported skill companion helpers, and mechanic part-local scripts were not
covered by one explicit owner/lane/side-effect map.

That left a path for future historical scripts to accumulate outside lane
authority. A script could remain useful locally while becoming unclear about
whether it was a hard gate, generated builder, runtime-policy helper,
mechanic-owned command, or advisory tool.

## Options considered

1. Keep only `validator_inventory.json` and rely on local `AGENTS.md` cards for
   every non-validator script.
2. Add a script-wide inventory and topology guard while keeping command
   sequences in `config/validation_lanes.json`.

## Decision

Add `docs/validation/SCRIPT_TOPOLOGY.md` and
`docs/validation/script_inventory.json`.

The script inventory covers every tracked non-pyc file under `*/scripts/*`.
Each entry names path, family, organ lane, owner surface, source truth, reads,
writes, side effects, validation lane, CI inclusion, focused test target, and
disposition.

Keep `config/validation_lanes.json` as the only active lane command authority.
The script inventory describes script ownership and coverage; it does not store
or execute lane command sequences.

`tests/test_script_topology.py` guards the inventory against orphan scripts,
missing owner or test targets, stale script references in active route docs,
hidden hard gates for advisory helpers, untracked side-effect claims, and
tracked Python cache residue.

## Rationale

Agentic-OS scripts should be boundary organs. The important question is not
only whether a script passes, but what it protects and whether it is allowed to
write, execute subprocesses, append local observation state, or remain
advisory.

A script-wide inventory makes that route explicit without widening PR
validation into release-sized work. It also keeps exported skill helper scripts
and runtime-shaped local tools from quietly becoming CI hard gates in the
technique-canon repo.

## Consequences

- New scripts must receive an inventory entry before they are treated as
  active.
- Moving or changing a script's side-effect posture requires updating the
  inventory and the nearest owner route.
- Advisory skill-local or observation helpers can stay in the repo when their
  non-blocking posture and test route are explicit.
- The inventory adds maintenance overhead, but the topology test turns that
  overhead into a clear failure route instead of hidden command drift.

## Source surfaces

- `docs/validation/SCRIPT_TOPOLOGY.md`
- `docs/validation/script_inventory.json`
- `docs/validation/COMMAND_AUTHORITY.md`
- `docs/validation/VALIDATOR_TOPOLOGY.md`
- `scripts/AGENTS.md`
- `config/validation_lanes.json`
- `tests/test_script_topology.py`
- `docs/testing/test_inventory.json`

## Follow-up route

Revisit this decision when a future script class becomes a true owned hard
gate rather than advisory/local-only. Promotion should update
`config/validation_lanes.json`, the script inventory, the nearest `AGENTS.md`,
and the relevant validator or test topology.

## Verification

Current verification route:

- `tests/AGENTS.md` focused checks for script topology and validation topology.
- `source-fast` for active route-card and source-contract posture.
- `generated` when script inventory or docs changes affect generated decision
  or AGENTS mesh read-models.
- `mechanics/part-local` for mechanic-owned part-local script discovery.
- `release` when command execution, runner, or release-facing scripts move.

Exact command storage remains in `config/validation_lanes.json` and
`docs/validation/COMMAND_AUTHORITY.md`.
