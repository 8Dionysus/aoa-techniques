# Validator Owner Modules

Status: accepted
Date: 2026-06-02

## Index Metadata

- Decision ID: AOA-TECH-D-0067
- Original date: 2026-06-02
- Surface classes: validation guard, release/tooling, docs route
- Technique axes: validation lane
- Mechanic parents: release-support
- Guard families: validator topology, generated/read-model, source contract
- Posture: accepted

## Context

`scripts/validate_repo.py` had become a single large validator that mixed
authored technique source contracts, generated/read-model parity, questbook
source/projection checks, shared parser helpers, and release-facing orchestration.

That made it hard to tell which rule owned source meaning and which rule only
checked projection freshness. It also made future validator work prone to
duplicating rules inside one broad historical script.

## Decision

Keep `scripts/validate_repo.py` as a compatibility CLI and re-export adapter.
Move implementation ownership under `scripts/validators/`:

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

Record these modules in `docs/validation/validator_inventory.json` and test
the topology with `tests/test_validator_module_topology.py`.

## Rationale

Validators should be boundary organs, not accumulated script history. The split
keeps generated validators subordinate to authored source: generated checks may
rebuild expected payloads from source and compare projections, but they do not
define technique meaning, frontmatter truth, route doctrine, or runtime policy.

The compatibility adapter preserves existing imports from `scripts.validate_repo`
while making the owner module visible through each function's implementation
module and the validator inventory.

## Consequences

- Future source-rule changes should land in `source_contracts.py` unless a
  narrower owner module is added.
- Future generated/read-model parity checks should land in the narrow
  `projection_*.py` module for that projection family, with
  `projection_parity.py` kept as a compatibility facade only.
- `scripts/validate_repo.py` must remain thin and must not regain rule logic.
- Topology tests must fail when a validator module appears without inventory
  coverage, when rule ownership is duplicated, or when projection validators
  start owning source meaning.

## Source surfaces

- `scripts/validate_repo.py`
- `scripts/validators/`
- `scripts/validators/AGENTS.md`
- `docs/validation/VALIDATOR_TOPOLOGY.md`
- `docs/validation/COMMAND_AUTHORITY.md`
- `docs/validation/validator_inventory.json`
- `config/validation_lanes.json`
- `tests/test_validator_module_topology.py`
- `tests/test_validate_repo_*.py`

## Verification

Current verification route:

- `tests/AGENTS.md` focused checks for validator topology and split
  `test_validate_repo_*` homes.
- `scripts/AGENTS.md` focused validate-repo compatibility check.
- `generated` lane when projection validator ownership or generated parity
  surfaces move.
- `release` lane when the validator split becomes release-facing.

Exact command storage remains in `config/validation_lanes.json` and
`docs/validation/COMMAND_AUTHORITY.md`.
