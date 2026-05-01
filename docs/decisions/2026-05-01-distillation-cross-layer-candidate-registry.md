# Distillation Cross-Layer Candidate Registry

Status: accepted
Date: 2026-05-01

## Context

The cross-layer candidate ledger accounts for the Dionysus donor-note universe:
`24` proposed technique-shaped names, including inherited external placements,
landed Wave A/B/C imports, overlap holds, layer-incubation lanes, and
architecture/substrate holds.

Unlike the external candidate ledger, this surface also carries wave-memory and
landed bundle references. Compacting the README too early would make the route
less legible, but leaving the whole surface only as prose and tables would make
counts, inherited rows, and closed wave status too easy to drift.

## Decision

Add a structured part-local registry beside the active cross-layer README,
without compacting the README in this pass.

The registry records each candidate with:

- the existing ledger status and gate status
- landed technique bundle references when a wave import is already landed
- inherited external placement status when the candidate belongs to the
  external candidate ledger
- atom/topology fields for possible future technique shape
- law/local/bridge fields for source law, local route, and stop line
- nearest overlap, wave, and next move

The generated compact index is validation evidence only. The active part README
continues to carry the human route and wave-memory, while landed technique
bundles own their reusable practice contracts.

## Consequences

Future agents can verify the `24`-candidate universe, landed wave counts,
inherited external rows, and zero future-import lane without re-reading every
table. The registry also makes portable technique pressure explicit for rows
that are not yet technique-shaped.

The tradeoff is artifact pairing: the README, seed registry, generated index,
and topology tests must move together when this ledger changes. This is
intentional because recurrence and later compaction work need evidence without
gaining promotion authority.
