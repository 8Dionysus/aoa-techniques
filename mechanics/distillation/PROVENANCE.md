# Distillation Provenance Bridge

This is the active-first bridge from current Distillation parts back to donor,
cross-layer, and legacy evidence. Use it when auditing how source pressure feeds
an active part, not when you need the current operating contract.

## Current route first

Start with the active surfaces:

- [README](README.md)
- [DIRECTION](DIRECTION.md)
- [PARTS](PARTS.md)
- [parts](parts/)
- [LANDING_LOG](LANDING_LOG.md)

If those surfaces answer the task, stop there. Do not pull donor history into
the active route just because it exists.

## Source map

| Evidence source | Active route | Distilled signal |
|---|---|---|
| Pre-split flat `DONOR_REFINERY_RUBRIC.md` | [parts/donor-refinery](parts/donor-refinery/README.md) | Donor extraction must name pattern, contamination risk, and foreign doctrine before importing reusable practice. |
| Pre-split flat `EXTERNAL_IMPORT_RUNBOOK.md` plus repo templates | [parts/external-import-runbook](parts/external-import-runbook/README.md) | A donor can move from triage to merge only through explicit overlap checks, evidence notes, generated-surface expectations, validation, and public-safe review. |
| Pre-split flat `EXTERNAL_TECHNIQUE_CANDIDATES.md` plus named historical seed references retained in that ledger | [parts/external-candidate-ledger](parts/external-candidate-ledger/README.md) | External donor candidates remain accounted for with explicit landed, hold, incubation, substrate, and narrowing-lane states. |
| Pre-split flat `CROSS_LAYER_TECHNIQUE_CANDIDATES.md`, sibling donor notes, and incoming wave packets | [parts/cross-layer-candidate-ledger](parts/cross-layer-candidate-ledger/README.md) | Cross-layer candidate pressure stays visible without turning `aoa-techniques` into a second donor backlog. |
| Pre-split flat `LONG_GAP_CANON_DESIGN.md` plus bundle-local technique evidence | [parts/long-gap-reentry](parts/long-gap-reentry/README.md) | Long-gap promoted material needs new external contracts before another honest canonical review. |

## Legacy posture

The 2026-05-01 split moved the current flat files into active part homes without
rewriting candidate verdicts. Because no ledger was pruned in this slice,
`legacy/raw/` remains reserved for future pre-prune receipts.

When a future pass compacts a ledger, preserve the pre-pruned accounting in
`legacy/raw/`, update [legacy/INDEX.md](legacy/INDEX.md), and record the
distillation in [legacy/DISTILLATION_LOG.md](legacy/DISTILLATION_LOG.md).

## Distillation rule

When source evidence changes current behavior, update the relevant active part
first, then update this bridge, `legacy/INDEX.md`, and `LANDING_LOG.md`. Active
part docs must not become raw source dumps.
