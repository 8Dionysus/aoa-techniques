# Agon Parts

This file maps current Agon technique-side behavior to active parts. It is not a
raw source inventory.

| Part | Current role | Active source | Provenance |
|---|---|---|---|
| `move-technique-bridge` | Receives Wave IV owner-binding pressure as requested-only practice candidates. | [parts/move-technique-bridge](parts/move-technique-bridge/README.md), `parts/move-technique-bridge/config/agon_technique_binding_candidates.source.json`, `parts/move-technique-bridge/generated/agon_technique_binding_candidates.min.json` | [Wave IV immutable source](https://github.com/8Dionysus/aoa-techniques/blob/feffba63dc22fd921512ba5a3ff1b5d78606f93b/mechanics/agon/legacy/raw/AGON_WAVE4_TECHNIQUE_LANDING.md) |
| `epistemic-practice-boundary` | Keeps epistemic practice capture distinct from workflow, proof, memory, runtime, KAG, and ToS authority. | [parts/epistemic-practice-boundary](parts/epistemic-practice-boundary/README.md) | [Wave XV immutable source](https://github.com/8Dionysus/aoa-techniques/blob/feffba63dc22fd921512ba5a3ff1b5d78606f93b/mechanics/agon/legacy/raw/AGON_WAVE15_TECHNIQUES_LANDING.md) |
| `epistemic-technique-candidates` | Holds requested-only practice candidates behind epistemic move extensions. | [parts/epistemic-technique-candidates](parts/epistemic-technique-candidates/README.md), `parts/epistemic-technique-candidates/config/agon_epistemic_technique_candidates.source.json`, `parts/epistemic-technique-candidates/generated/agon_epistemic_technique_candidates.min.json` | [Wave XV immutable source](https://github.com/8Dionysus/aoa-techniques/blob/feffba63dc22fd921512ba5a3ff1b5d78606f93b/mechanics/agon/legacy/raw/AGON_WAVE15_TECHNIQUES_LANDING.md) |
| `recurrence-adapter` | Exposes Agon technique-side surfaces to recurrence observation without runtime or authority effects. | [parts/recurrence-adapter](parts/recurrence-adapter/README.md), `parts/recurrence-adapter/manifests/recurrence/component.agon.*.json` | Wave IV and Wave XV routes through [PROVENANCE](PROVENANCE.md) |

## Downstream Distillation Route

[Distillation Agon Candidate Handoff](../distillation/parts/agon-candidate-handoff/README.md)
maps the current Agon candidate registries into technique-side narrowing lanes.
It reads Agon requested-only candidates as source evidence; it does not change
candidate status, define lawful moves, or promote technique bundles.

## Part rule

If a part starts carrying stable reusable practice with inputs, outputs, risks,
and validation, route the practice bundle into `techniques/`. Leave this package
as the mechanics layer that explains how the request moved.
