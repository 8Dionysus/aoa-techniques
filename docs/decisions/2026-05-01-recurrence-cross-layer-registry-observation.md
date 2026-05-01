# Recurrence Cross-Layer Registry Observation

Status: accepted
Date: 2026-05-01

## Context

The Distillation cross-layer candidate ledger now has two paired active
surfaces: the human README route and a generated registry index that preserves
the `24`-candidate accounting, wave counts, inherited external rows, and current
gates.

Recurrence already observed the cross-layer README as a source of candidate and
overlap pressure. After the registry landed, leaving recurrence pointed only at
the README would hide the new machine-checkable accounting. Pointing recurrence
at the generated index as a decision surface would be worse: it would turn
derived evidence into candidate or promotion authority.

## Decision

Repoint technique recurrence observation so the `cross-layer-technique-candidates`
input reads both:

- `mechanics/distillation/parts/cross-layer-candidate-ledger/README.md`
- `mechanics/distillation/parts/cross-layer-candidate-ledger/generated/cross_layer_candidate_registry.min.json`

Keep the README as the decision surface. Treat the generated registry as
observation evidence only.

## Consequences

Recurrence can now notice count, gate, wave, and hold drift from the generated
registry while still routing any follow-up through the active README and normal
technique review surfaces.

The generated registry cannot create candidates, release overlap holds, release
layer-incubation lanes, authorize import, or promote techniques. If the README
and generated index disagree, the correct action is to repair the paired
Distillation surfaces, not to let recurrence choose one as authority.
