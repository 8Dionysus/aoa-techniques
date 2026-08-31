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
Read `README.md` only when the selected task needs its human map; do not preload unrelated maps.

## Boundaries

- Tests should keep reusable practice reproducible.
- Prefer cases that expose invariants, boundary conditions, drift, and transfer
  behavior rather than incidental formatting.
- Do not update snapshots or expected generated surfaces without rebuilding and
  checking the source-authored technique or manifest that owns meaning.
- Keep fixtures public-safe. No secrets, private transcripts, hidden benchmark
  data, or machine-local paths.

## Validation

Select the narrowest owner route: `source-fast` for focused source/validator work; add `generated` for projections. See [VALIDATION.md](../VALIDATION.md); exact order is `config/validation_lanes.json`; focused procedure stays with the nearest owner. Report checks, skips, and blockers.

## Closeout

Report changed tests, behavior or invariant covered, generated fixtures rebuilt
or left untouched, public-safe review, checks run, and checks skipped.
