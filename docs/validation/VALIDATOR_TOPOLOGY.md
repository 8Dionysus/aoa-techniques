# Validator Topology

Validators in `aoa-techniques` are boundary organs for the public technique
canon. They protect source topology, reproducible generated projections,
mechanic-local candidate surfaces, and release stabilization.

They should not become one historical pile where every wave leaves a new
standalone gate.

## Lanes

| Lane | Posture | Owns | Does not own |
|---|---|---|---|
| `source-fast` | blocking growth gate | repo-local KAG parity, owner-local stats protocol, AGENTS mesh, nested route-card shape, semantic route snippets, fast authored technique source contracts | generated freshness, cross-owner statistics, release freeze, runtime/export policy |
| `generated` | blocking projection gate | generated/read-model rebuild parity and drift snapshots | technique meaning, skill export/runtime contracts |
| `mechanics/part-local` | blocking mechanic-owned gate | part-local candidate registries, handoff packets, builder `--check` parity, pytest homes | root release packaging, sibling runtime behavior |
| `release` | blocking release gate | frozen release-prep sequence, Spark lane, mechanics/part-local lane, tests, validators, worktree stabilization | ordinary PR growth gating |
| `nightly` | blocking moving-main sentinel | source, generated, and mechanic part-local drift on the growth surface | release artifact identity or sibling release reproduction |
| `advisory` | non-blocking boundary inventory | route-only export/runtime, trace/eval, and security/adversarial boundaries | hard runtime policy, eval verdicts, security enforcement |

## GitHub CI Route

`Repo Validation` runs `source-fast` for pull requests and pushes to `main`.
That gate checks repo-local KAG parity, the owner-local stats port, route
topology, and source-owned technique contracts. The stats adapter delegates
protocol validation to pinned `aoa-stats`; it does not copy central schemas or
aggregate sibling owners. The gate does not rebuild or compare generated
freshness. Generated checks run only on pushes to `main`, where the moving
growth surface can absorb projection drift checks without turning every PR into
a release freeze.

`Release Audit` and `Nightly Sentinel` are separate workflows. Release uses the
`release` mode; nightly runs the moving-main `nightly` mode and separately
reproduces the latest `v*` release tag through `scripts/release_check.py`. Both
keep pinned GitHub actions and call lane entrypoints rather than copying command
sequences.

The generated lane is grouped in
[`validation_lanes.json`](../../config/validation_lanes.json) so each
projection family has a named owner: catalog, decisions, AGENTS mesh, mechanics
projections, KAG export, Technique Intelligence, questbook, and public hygiene.

## Source/Projection Boundary

Authored technique bundles, docs contracts, mechanic source packets, schemas,
and AGENTS cards own meaning.

The local `stats/` port owns technique-canon questions and measurement meaning.
Central protocol grammar and cross-owner aggregation remain with `aoa-stats`.

Generated catalogs, readers, capsules, KAG export, AGENTS mesh mirrors, and
mechanic generated indexes are projections. Generated validators check rebuild
parity and drift. They do not define what a technique means.

## Validator Modules

`scripts/validate_repo.py` is a compatibility CLI and re-export adapter only.
Rule ownership lives under `scripts/validators/`:

- `common.py` owns shared models, constants, schema parsing, and parser helpers.
- `source_contracts.py` owns authored technique and repo-source contracts.
- `projection_parity.py` stays a compatibility re-export facade.
- `projection_catalog.py` owns catalog and reader projection parity.
- `projection_decisions.py` owns generated decision-index parity.
- `projection_agents_mesh.py` owns generated AGENTS mesh parity.
- `projection_mechanics.py` owns mechanic report projection parity.
- `projection_kag.py` owns KAG export parity.
- `projection_intelligence.py` owns Technique Intelligence registry, DAG, and
  reader parity.
- `questbook.py` owns quest source topology and quest projection parity.
- `public_hygiene.py` owns public surface hygiene checks.
- `orchestrator.py` owns validate-repo call order and status output.

Generated validators must stay in `projection_*.py` as parity checks. They may
rebuild expected payloads from source, but they do not become source meaning
owners for frontmatter truth, technique intent, route doctrine, or runtime
policy.

## Mechanics Boundary

Mechanic package and part homes own candidate movement around the technique
canon. The `mechanics/part-local` lane enters through
`scripts/run_part_local_tests.py`, which discovers current
`mechanics/*/parts/*/tests/test*.py` files and their related part-local
builder `--check` and validator scripts. This keeps part-local coverage
source-derived instead of freezing a historical file list outside
`scripts/run_tests.py`.

## Advisory Boundary

Do not copy `aoa-skills` export/runtime lanes wholesale.

`aoa-techniques` may publish generated technique capsules, KAG export
companions, examples, and public-hygiene checks; it does not own skill portable export,
runtime guardrail policy, runtime policy engine, eval verdict layer, agent
trace grading, or security enforcement.
Those topics stay in the advisory lane unless a future source decision promotes
one concrete `aoa-techniques`-owned check.

## Inventory

Machine-readable lane inventory lives in
[`validator_inventory.json`](validator_inventory.json). It records lane owners,
inputs, outputs, command sequence ids, modes, and failure routes. Update it
with `config/validation_lanes.json` when command routing changes.

The broader script-surface map lives in
[`SCRIPT_TOPOLOGY.md`](SCRIPT_TOPOLOGY.md) and
[`script_inventory.json`](script_inventory.json). That inventory covers every
active file under `*/scripts/*`, including mechanic-local scripts, Spark lane
scripts, exported skill companion helpers, and script-local `AGENTS.md` route
cards. It is descriptive coverage, not command authority.
