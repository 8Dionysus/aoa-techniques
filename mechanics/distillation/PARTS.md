# Distillation Parts

This file maps current Distillation behavior to active parts. It is not a raw
source inventory.

| Part | Current role | Active source | Provenance |
|---|---|---|---|
| `donor-refinery` | Defines the compact extraction law for external donors: pattern, contamination, and foreign doctrine. | [parts/donor-refinery](parts/donor-refinery/README.md) | [PROVENANCE](PROVENANCE.md) |
| `external-import-runbook` | Gives maintainers the path from bounded donor triage to draft, review, validation, and merge. | [parts/external-import-runbook](parts/external-import-runbook/README.md) | [PROVENANCE](PROVENANCE.md) |
| `external-candidate-ledger` | Preserves public-safe external donor candidate accounting and the current active narrowing lane, with a structured part-local registry for machine checks. | [README](parts/external-candidate-ledger/README.md), [seed registry](parts/external-candidate-ledger/config/external_candidate_registry.seed.json), [generated index](parts/external-candidate-ledger/generated/external_candidate_registry.min.json) | [PROVENANCE](PROVENANCE.md) |
| `cross-layer-candidate-ledger` | Preserves sibling-repo donor-note accounting without widening the external-only intake surface, with a structured part-local registry for wave and verdict checks. | [README](parts/cross-layer-candidate-ledger/README.md), [seed registry](parts/cross-layer-candidate-ledger/config/cross_layer_candidate_registry.seed.json), [generated index](parts/cross-layer-candidate-ledger/generated/cross_layer_candidate_registry.min.json) | [PROVENANCE](PROVENANCE.md) |
| `agon-candidate-handoff` | Maps Agon requested-only practice candidates into Distillation lanes while preserving Agon source authority and technique-side stop-lines. | [README](parts/agon-candidate-handoff/README.md), [seed registry](parts/agon-candidate-handoff/config/agon_candidate_handoff.seed.json), [gate cards](parts/agon-candidate-handoff/gates/README.md), [frontier review](parts/agon-candidate-handoff/gates/frontier/first-narrowing-frontier-review.md), [generated index](parts/agon-candidate-handoff/generated/agon_candidate_handoff.min.json) | [PROVENANCE](PROVENANCE.md) |
| `technique-reform-ingress` | Collects current topology evidence into a bounded entry packet before future classification reform. | [README](parts/technique-reform-ingress/README.md), [topology scout review](parts/technique-reform-ingress/reviews/first-topology-scout-review-pack.md), [decision](../../docs/decisions/2026-05-03-technique-reform-ingress-packet.md) | [PROVENANCE](PROVENANCE.md) |
| `long-gap-reentry` | Holds the long-gap backlog posture for promoted material that needs another external contract before canonical review. | [parts/long-gap-reentry](parts/long-gap-reentry/README.md) | [PROVENANCE](PROVENANCE.md) |

## Part rule

If a part starts carrying stable reusable practice with inputs, outputs, risks,
and validation, route the practice bundle into `techniques/`. Leave this package
as the mechanics layer that explains how donor pressure moved.
