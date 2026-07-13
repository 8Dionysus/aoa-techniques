# Script Topology

Scripts in `aoa-techniques` are command-plane organs for a public technique
canon. They should name the boundary they protect, the source truth they read,
the projections they may write, and the validation lane that covers them.

They are not a second command authority. Blocking command sequences live in
[`validation_lanes.json`](../../config/validation_lanes.json). The script
inventory is descriptive and testable: it proves every active script has an
owner route, side-effect boundary, lane posture, and test target.

## Inventory

Machine-readable script coverage lives in
[`script_inventory.json`](script_inventory.json). It includes every tracked
non-pyc file under `*/scripts/*`, including local `AGENTS.md` route cards.

Each entry records:

- `path`
- `family`
- `organ_lane`
- `owner_surface`
- `source_truth`
- `reads`
- `writes`
- `side_effects`
- `validation_lane`
- `ci_inclusion`
- `test_target`
- `disposition`

`tests/test_script_topology.py` keeps the inventory synchronized with the
filesystem and rejects orphan scripts, missing owner/test targets, stale script
references in active route docs, hidden hard gates for advisory helpers, and
tracked Python cache residue.

## Script Families

| Family | Owns | Boundary |
|---|---|---|
| `source_validator` | authored route, AGENTS, and technique source checks | may read source meaning; must not check generated freshness |
| `source_validator_adapter` | owner-local contracts checked by a stronger sibling protocol owner | delegate without copying sibling schemas or rules into this repo |
| `projection_builder` | generated/read-model writes from source | may write tracked projections; must not define source meaning |
| `projection_validator_module` | generated/read-model parity checks | compares projections; does not own technique truth |
| `part_local_builder` / `part_local_validator` | mechanic-owned candidate artifacts | discovered by `scripts/run_part_local_tests.py` from part homes |
| `skill_local_contract_tool` | exported skill companion contract helpers | advisory/local-only; not CI hard gates for this repo |
| `agent_lane_validator` | Spark lane registry and scenario shape | release-owned, not PR source-fast |
| `lane_executor`, `lane_loader`, `release_entrypoint`, `test_runner` | command execution and release/test orchestration | load command authority from `config/validation_lanes.json` |
| `compatibility_adapter` | old import/CLI surfaces | keep thin; rule ownership stays elsewhere |
| `script_route_card` | local route and stop-line guidance | source-fast AGENTS validators cover shape and mesh inclusion |
| `mechanic_local_observation_tool` | bounded local observation receipt append | advisory; tested, but not a hard runtime-policy lane |

## Root Scripts

Root `scripts/*.py` own repo-wide builders, validators, lane execution, release
stabilization, and test runners. Root builders may write tracked generated
companions only through generated/read-model lanes. Root validators and
validator modules must keep source checks separate from projection parity.

`scripts/validate_repo.py` stays a compatibility CLI and import adapter.
Implementation ownership lives under `scripts/validators/`, and
[`validator_inventory.json`](validator_inventory.json) remains the narrower
inventory for validator modules.

The repo-local KAG and stats adapters remain thin source-lane delegates. Local
KAG indexes and stats measurement meaning stay here; shared KAG generation and
stats protocol grammar stay with their sibling owners.

## Non-Root Scripts

Mechanic part-local builders and validators live beside the part that owns the
candidate surface. The `mechanics/part-local` lane enters through
`scripts/run_part_local_tests.py`, which discovers current part-local tests and
the related `build_*.py --check` / `validate_*.py` scripts from source homes.

The Distillation `technique-reform-ingress` report builders are projection
builders because they write generated report companions and are covered by the
generated mechanics projection group.

The Recurrence `publish_live_receipts.py` helper appends local JSONL
observation receipts. It is tested as a mechanic-local helper, but it is not
runtime policy, proof verdict, memory authority, or a release command.

The Spark lane validator is release-owned and validates agent-lane registry,
scenario, result, and handoff shape. It does not belong in PR `source-fast`.

The `.agents/skills/*/scripts` helpers are deterministic contract tools inside
exported skill companion material. They can model approval, dry-run,
readiness, and risk contracts, but they do not become `aoa-techniques` runtime
policy enforcement and are not hidden hard gates.

## Promotion Rule

A script may move from advisory/local-only into a blocking lane only when a
current owner surface and decision record prove that `aoa-techniques` owns the
checked behavior. Until then, runtime policy, trace/eval verdicts, memory/RAG
authority, security enforcement, and skill export execution remain route-only
or sibling-owned.
