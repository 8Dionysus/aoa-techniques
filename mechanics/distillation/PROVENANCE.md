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
| Pre-split flat `EXTERNAL_TECHNIQUE_CANDIDATES.md`, its 2026-05-01 pre-prune receipt, named historical `seed_4.txt` / `seed_6.txt` labels whose raw files are not present in the current checkout, and the part-local [structured registry](parts/external-candidate-ledger/config/external_candidate_registry.source.json) plus [generated index](parts/external-candidate-ledger/generated/external_candidate_registry.min.json) | [parts/external-candidate-ledger](parts/external-candidate-ledger/README.md) | External donor candidates remain accounted for with explicit landed, hold, incubation, substrate, and narrowing-lane states while the missing raw seed files are treated as historical labels rather than active source files; the structured registry preserves the same accounting for validation and does not change candidate authority. |
| [legacy/raw/EXTERNAL_CANDIDATE_LEDGER_2026-05-01_PRE_PRUNE.md](legacy/raw/EXTERNAL_CANDIDATE_LEDGER_2026-05-01_PRE_PRUNE.md) | [parts/external-candidate-ledger](parts/external-candidate-ledger/README.md) | Detailed wave execution notes, public donor-read details, and old import package expectations are preserved out of the compact active route. |
| Pre-split flat `CROSS_LAYER_TECHNIQUE_CANDIDATES.md`, sibling donor notes, incoming wave packets, its 2026-05-01 pre-prune receipt, and the part-local [structured registry](parts/cross-layer-candidate-ledger/config/cross_layer_candidate_registry.source.json) plus [generated index](parts/cross-layer-candidate-ledger/generated/cross_layer_candidate_registry.min.json) | [parts/cross-layer-candidate-ledger](parts/cross-layer-candidate-ledger/README.md) | Cross-layer candidate pressure stays visible without turning `aoa-techniques` into a second donor backlog; the structured registry preserves the same `24`-candidate accounting for validation and does not change candidate authority or recurrence authority. |
| Closed incoming packet archive under [legacy/archive/closed-incoming-packets](legacy/archive/closed-incoming-packets/README.md), including chat wave packets and personal-media-ingest | [parts/candidate-intake](parts/candidate-intake/README.md), archived packet README/docs/support surfaces, landed `techniques/**/TECHNIQUE.md` bundles, and packet-local closeout memos | First-pass landing queues are exhausted; active intake lives in the Candidate Intake part, while the archive preserves donor-wave accounting, explicit exclusions, and closed non-import verdicts without duplicating canonical bundle meaning. |
| [legacy/raw/CROSS_LAYER_CANDIDATE_LEDGER_2026-05-01_PRE_PRUNE.md](legacy/raw/CROSS_LAYER_CANDIDATE_LEDGER_2026-05-01_PRE_PRUNE.md) | [parts/cross-layer-candidate-ledger](parts/cross-layer-candidate-ledger/README.md) | Detailed landed wave execution order, worker-role notes, and seam rationale are preserved out of the compact active route. |
| Agon active candidate registries [move-technique-bridge generated index](../agon/parts/move-technique-bridge/generated/agon_technique_binding_candidates.min.json) and [epistemic-technique-candidates generated index](../agon/parts/epistemic-technique-candidates/generated/agon_epistemic_technique_candidates.min.json), checked against center owner-binding boundaries in `Agents-of-Abyss` | [parts/agon-candidate-handoff](parts/agon-candidate-handoff/README.md), [gate cards](parts/agon-candidate-handoff/gates/README.md), and [first-narrowing frontier review](parts/agon-candidate-handoff/gates/frontier/first-narrowing-frontier-review.md) | Agon requested-only candidates are mapped into Distillation lanes for atom/topology narrowing without changing Agon candidate status or importing Agon law into technique canon; a gate card may narrow one candidate but cannot promote it, and the frontier review only exposes the remaining ungated first-narrowing queue. |
| Technique atom/topology contracts, kind registry, part-local family/topology scout inputs, part-local kind overlay data, kind ambiguity audit, Agon first-narrowing frontier evidence, mechanic-local scout reports, part-local scout scripts, and semantic/shadow review packets | [parts/technique-reform-ingress](parts/technique-reform-ingress/README.md), [technique reform scout config](parts/technique-reform-ingress/config/AGENTS.md), [technique reform overlay data](parts/technique-reform-ingress/data/AGENTS.md), [technique reform scout scripts](parts/technique-reform-ingress/scripts/AGENTS.md), [technique reform reports](parts/technique-reform-ingress/reports/AGENTS.md), [semantic review packets](parts/technique-reform-ingress/reviews/semantic/README.md), and [shadow review packets](parts/technique-reform-ingress/reviews/shadow/README.md) | Future classification reform should start from a bounded ingress packet that keeps `domain` and `kind` authoritative, keeps other axes scout/design-only until promoted intentionally, preserves scout inputs, overlay data, reports, scripts, and review packets as movement evidence, and prevents generated evidence from remapping bundle meaning automatically. |
| Pre-split flat `LONG_GAP_CANON_DESIGN.md` plus bundle-local technique evidence | [parts/long-gap-reentry](parts/long-gap-reentry/README.md) | Long-gap promoted material needs new external contracts before another honest canonical review. |

## Legacy posture

The 2026-05-01 split moved the current flat files into active part homes without
rewriting candidate verdicts. The later external and cross-layer candidate
ledger compaction passes preserved pre-pruned active ledgers in `legacy/raw/`
before shortening the current route surfaces.

When a future pass compacts another ledger, preserve the pre-pruned accounting
in `legacy/raw/`, update [legacy/INDEX.md](legacy/INDEX.md), and record the
distillation in [legacy/DISTILLATION_LOG.md](legacy/DISTILLATION_LOG.md).

## Distillation rule

When source evidence changes current behavior, update the relevant active part
first, then update this bridge, `legacy/INDEX.md`, and `LANDING_LOG.md`. Active
part docs must not become raw source dumps.
