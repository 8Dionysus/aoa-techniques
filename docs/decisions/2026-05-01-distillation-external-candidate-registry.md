# Distillation External Candidate Registry

Status: accepted
Date: 2026-05-01

## Context

After the Distillation active/parts/legacy split, the external candidate ledger
had a compact active README and a preserved pre-prune receipt. That made the
route readable, but the current `13` candidate states still lived mostly as
tables and prose.

The project direction now requires each mechanics surface to preserve the
difference between source ownership, local handling, and stop lines where that
distinction affects candidate movement. `aoa-techniques` also needs technique
candidates to stay portable outside OS Abyss while still participating in AoA
provenance and review.

## Decision

Add a structured part-local registry for
`mechanics/distillation/parts/external-candidate-ledger/`.

The registry records each remaining external candidate with:

- the existing ledger status and gate status
- atom/topology fields for the possible future technique shape
- boundary fields for source owner, local route, and stop line
- nearest overlap and next move

The generated compact index is validation evidence only. The active part README
continues to explain the current route, and the normal bundle review path still
owns any future promotion into `techniques/`.

## Consequences

Future agents can verify candidate counts, gates, donors, and the active
narrowing lane without re-reading the whole pre-prune receipt. The registry also
makes the portable technique pressure explicit before any candidate is drafted.

The tradeoff is another maintained artifact: when the ledger changes, the README
and seed registry must move together, then the generated index must be rebuilt
and validated. This is acceptable because it keeps the candidate ledger compact
while avoiding silent reclassification.
