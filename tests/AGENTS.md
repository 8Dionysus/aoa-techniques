# AGENTS.md

## Applies to

This card applies to `tests/` and all descendants unless a nearer `AGENTS.md`
narrows the path.

## Role

`tests/` protects root-owned technique contracts, validators, builders,
generated parity, root legacy, AGENTS mesh behavior, and downstream-consumer
assumptions.

Mechanic-owned tests belong beside the owning mechanic under
`mechanics/<slug>/tests/`, shared mechanics-wide tests belong under
`mechanics/tests/`, and part-local tests belong under
`mechanics/<slug>/parts/<part>/tests/`.

## Read before editing

Read root `AGENTS.md`, `scripts/AGENTS.md`, the source surface under test, and
the builder or validator being exercised.
For adding, deleting, moving, or changing a test home, also read
`docs/testing/TEST_TOPOLOGY.md` and update
`docs/testing/test_inventory.json`.

## Boundaries

- Tests should keep reusable practice reproducible.
- Prefer cases that expose invariants, boundary conditions, drift, and transfer
  behavior rather than incidental formatting.
- Do not update snapshots or expected generated surfaces without rebuilding and
  checking the source-authored technique or manifest that owns meaning.
- Keep fixtures public-safe. No secrets, private transcripts, hidden benchmark
  data, or machine-local paths.

## Validation

Full lane command sequences live in `config/validation_lanes.json`; tests may
guard lane authority, but they should not become a second command store. Verify
with the focused test first, then the relevant lane:

```bash
python -m unittest tests.test_test_topology
python -m unittest tests.test_validator_module_topology
python scripts/ci_gate.py --mode source-fast
python scripts/run_tests.py
python scripts/validate_semantic_agents.py
```

When tests cover AGENTS mesh behavior, also run:

```bash
python scripts/validate_agents_md_shape.py
python scripts/validate_agents_mesh.py
python scripts/validate_agents_mesh_index.py
```

## Closeout

Report changed tests, behavior or invariant covered, generated fixtures rebuilt
or left untouched, public-safe review, checks run, and checks skipped.
