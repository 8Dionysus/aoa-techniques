# AGENTS.md

## Applies to

This card applies to `mechanics/tests/` and all descendants unless a nearer
`AGENTS.md` narrows the path.

## Role

`mechanics/tests/` owns mechanics-wide regression tests that span more than one
mechanic package.

Use this home for package-card standards, shared request-receipt posture,
shared active-route and historical-recovery contracts, and cross-mechanic
contract checks. Tests
that only serve one mechanic belong in `mechanics/<slug>/tests/`; tests that
only serve one part belong in `mechanics/<slug>/parts/<part>/tests/`.

## Read before editing

package card or mechanics route contract under test.
Read `README.md` only when the selected task needs its human map; do not preload unrelated maps.

## Boundaries

These tests guard mechanics route contracts. They do not authorize technique
promotion, owner acceptance, runtime behavior, or sibling-repo status changes.

Do not move one-mechanic tests here just to make the root `tests/` directory
look smaller.

## Validation

Inherit [../AGENTS.md](../AGENTS.md#validation): `mechanics/part-local`; see [VALIDATION.md](../../VALIDATION.md) and `config/validation_lanes.json`. Local `mechanics/tests/AGENTS.md`: package practice/owner stop-line.
## Closeout

Report changed mechanics-wide tests, mechanic packages affected, validation
run, validation skipped, and whether any test should be moved closer to a
single mechanic owner.
