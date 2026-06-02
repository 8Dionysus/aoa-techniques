# Test Topology

This map keeps `aoa-techniques` tests readable as a topology authority for the
technique organ. Tests should answer what boundary is protected, which owner
surface is authoritative, where the test lives, which execution authority covers
it, and where a failure routes next.

The machine inventory is [`test_inventory.json`](test_inventory.json). Update
it when adding, deleting, renaming, splitting, folding, or changing the home of
a test file.

## Route Shape

Use the compact route shape:

```text
family -> protects -> owner surface -> home scope -> coverage authority -> focused target -> failure route
```

Test files are not command authority. Blocking command sequences live in
`config/validation_lanes.json`; release execution enters through the lane
system. `scripts/run_tests.py` owns unittest discovery homes for root and
mechanic-level tests. Part-local and agent-lane tests are covered by lane
commands because they are not ordinary unittest discovery homes.
`scripts/run_part_local_tests.py` owns source-derived pytest and
builder/validator coverage for mechanic part-local homes.

## Home Scopes

| Home Scope | Homes | Protects | Coverage Authority | Failure Route |
|---|---|---|---|---|
| `root` | `tests/` | Repo-wide route, docs, generated projection, validator, CI, and release contracts. | `scripts/run_tests.py` | Fix the root-owned source or validator before changing mechanic-local tests. |
| `mechanic-level` | `mechanics/tests/`, `mechanics/<slug>/tests/` | Mechanics-wide package law or one mechanic package's active topology. | `scripts/run_tests.py` | Fix the owning mechanic package, part map, route card, schema, or local contract. |
| `part-local` | `mechanics/<slug>/parts/<part>/tests/` | One active mechanic part, its generated companion, source registry, or handoff packet. | `validation_lanes.mechanics_part_local` | Fix the part-local source, builder, and validator before widening to release. |
| `agent-lane` | `.agents/spark/tests/` | Agent-lane operating guidance and local Spark scenario registry. | `validation_lanes.release_check` | Fix `.agents/spark/` route, registry, scenarios, or validator before treating release as clean. |

## Families

| Family | Protects | Owner Surface |
|---|---|---|
| `AGENTS/mesh` | Nested route-card shape, mesh config, and generated AGENTS index. | `AGENTS.md`, `config/agents_mesh.json`, AGENTS cards. |
| `docs/root-surface` | Root/docs markdown routing, public hygiene, and docs district boundaries. | `docs/guardrails/*`, `docs/ROOT_SURFACE_LAW.md`. |
| `source/contract` | Authored technique/parser/source bundle contracts and source-owned docs routes. | `scripts/validators/source_contracts.py`. |
| `generated/read-model` | Generated reader/export/projection surfaces derived from technique source. | Builder scripts and `scripts/validators/projection_*.py`. |
| `release/ci-lane` | CI lane composition, release stabilization, and workflow posture. | `config/validation_lanes.json`, `.github/workflows/*`, `scripts/release_check.py`. |
| `compatibility/imports` | Thin compatibility imports and optional dependency behavior. | `scripts/validate_repo.py`. |
| `public-hygiene` | Public-safe URL/path checks and public route-surface behavior. | `scripts/validators/public_hygiene.py`. |
| `questbook/intelligence` | Questbook source/projection contracts and related schema examples. | `scripts/validators/questbook.py`. |
| `test-topology/authority` | Test inventory, home classification, and runner/lane coverage. | `docs/testing/*`, `tests/support/topology_inventory.py`. |
| `mechanics/package-topology` | One mechanic package's active homes, local cards, part map, and legacy stop-lines. | `mechanics/<slug>/`. |
| `mechanics/shared` | Mechanics-wide package standards, request receipts, and cross-mechanic contracts. | `mechanics/`. |
| `mechanics/tree-pilot` | Distillation tree-pilot migration evidence and current-path receipts. | `mechanics/distillation/` and moved technique bundles. |
| `mechanics/part-local` | One mechanic part's registry, generated packet, and validation pair. | `mechanics/<slug>/parts/<part>/`. |
| `agent-lane/spark` | Spark agent-lane scenarios, registry, templates, and validator wiring. | `.agents/spark/`. |

## Lane Rules

- Inventory entries must name `focused_target`, not commands.
- Root and mechanic-level unittest homes must be discoverable from
  `scripts/run_tests.py`.
- Large mechanic-level topology suites should split by the owning phase, part,
  or surface; each split file needs its own inventory entry, owner surface, and
  failure route.
- Part-local pytest homes must be covered by the `mechanics_part_local` lane
  through `scripts/run_part_local_tests.py`, including each discovered home
  with a related builder `--check` and validator script.
- Spark agent-lane tests must stay outside root unittest discovery and remain
  release-covered through the lane manifest.
- Release command order belongs in `config/validation_lanes.json`; tests may
  assert lane coverage but must not replay the release sequence as a local
  command store.
