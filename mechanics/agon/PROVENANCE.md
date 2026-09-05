# Agon Provenance Bridge

This is the only active Agon technique-side surface that routes back to
preserved Wave IV and Wave XV source notes. Use it when you are auditing how a
wave receipt feeds an active part, not when you need the current operating
contract.

## Current route first

Start with the active surfaces:

- [README](README.md)
- [DIRECTION](DIRECTION.md)
- [PARTS](PARTS.md)
- [parts](parts/)
- [LANDING_LOG](LANDING_LOG.md)

If those surfaces answer the task, stop there. Do not pull raw wave history into
the active route.

## Source map

| Preserved source | Active route | Distilled signal |
|---|---|---|
| [Wave IV immutable source](https://github.com/8Dionysus/aoa-techniques/blob/feffba63dc22fd921512ba5a3ff1b5d78606f93b/mechanics/agon/legacy/raw/AGON_WAVE4_TECHNIQUE_LANDING.md) | [parts/move-technique-bridge](parts/move-technique-bridge/README.md) | Wave IV gave `aoa-techniques` requested-only practice candidates behind center-owned Agon owner binding. |
| [Wave IV immutable source](https://github.com/8Dionysus/aoa-techniques/blob/feffba63dc22fd921512ba5a3ff1b5d78606f93b/mechanics/agon/legacy/raw/AGON_WAVE4_TECHNIQUE_LANDING.md) | [parts/recurrence-adapter](parts/recurrence-adapter/README.md) | Wave IV candidate surfaces can be observed by recurrence, but recurrence cannot create arena, verdict, scar, rank, or rewrite effects. |
| [Wave XV immutable source](https://github.com/8Dionysus/aoa-techniques/blob/feffba63dc22fd921512ba5a3ff1b5d78606f93b/mechanics/agon/legacy/raw/AGON_WAVE15_TECHNIQUES_LANDING.md) | [parts/epistemic-practice-boundary](parts/epistemic-practice-boundary/README.md) | Epistemic technique candidates stay reusable-practice only and do not execute workflows, issue eval verdicts, or mutate memory. |
| [Wave XV immutable source](https://github.com/8Dionysus/aoa-techniques/blob/feffba63dc22fd921512ba5a3ff1b5d78606f93b/mechanics/agon/legacy/raw/AGON_WAVE15_TECHNIQUES_LANDING.md) | [parts/epistemic-technique-candidates](parts/epistemic-technique-candidates/README.md) | Epistemic move-extension support remains requested-only until owner review promotes a real technique bundle. |

## Detailed districts

- The [immutable Wave IV source](https://github.com/8Dionysus/aoa-techniques/blob/feffba63dc22fd921512ba5a3ff1b5d78606f93b/mechanics/agon/legacy/raw/AGON_WAVE4_TECHNIQUE_LANDING.md)
  and [immutable Wave XV source](https://github.com/8Dionysus/aoa-techniques/blob/feffba63dc22fd921512ba5a3ff1b5d78606f93b/mechanics/agon/legacy/raw/AGON_WAVE15_TECHNIQUES_LANDING.md)
  are the historical recovery paths.
- Current route accounting remains in this bridge and `LANDING_LOG.md`.

## Downstream Distillation Bridge

When current Agon candidate registries need technique-side narrowing, use
[Distillation Agon Candidate Handoff](../distillation/parts/agon-candidate-handoff/README.md).
That bridge reads active Agon generated indexes as source evidence and keeps the
full `12 + 10` candidate map in Distillation lanes. It does not pull raw Wave IV
or Wave XV receipts into the active Distillation route.

## Distillation rule

When a historical source changes current behavior, update the relevant active
part first, then update this bridge and `LANDING_LOG.md`, retaining the exact
immutable Git commit and original path here.
Active part docs must not become raw wave inventories.
