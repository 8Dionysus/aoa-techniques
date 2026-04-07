---
id: AOA-T-0097
name: degrade-reground-recover
domain: system-recovery
status: promoted
origin:
  project: ATM10-Agent
  path: docs/ANTIFRAGILITY_FIRST_WAVE.md
  note: Generalized from bounded hybrid-query degradation work where degraded continuation had to stay truthful, source-owned, and weaker than the normal path.
owners:
  - 8Dionysus
tags:
  - antifragility
  - degraded-mode
  - recovery
  - receipts
summary: Continue safely in a bounded degraded mode, reground against stronger sources, and recover later through explicit source-owned evidence instead of hidden repair theater.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-04-07
export_ready: true
relations:
  - type: complements
    target: AOA-T-0098
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
---

# degrade-reground-recover

## Intent

Keep partial failure honest and useful by moving through one bounded sequence:
degrade safely, reground on stronger authority, and recover later through explicit reviewed adaptation rather than hidden widening or repair theater.

## When to use

- an optional or derived stage fails but earlier grounded evidence is still usable
- retrieval, routing, memory, runtime helper, or another adjunct surface is degraded
- continuing with a smaller truthful answer is safer than inventing a fuller one
- operator trust depends on visible degraded posture instead of silent best-effort completion

## When not to use

- the degraded mode would become broader than the normal path
- the surface cannot say what remains trustworthy after the stress event
- the fallback would hide uncertainty, citations, or blocked actions
- the real need is a proof bundle, not an operational recovery posture

## Inputs

- owner-local run artifacts
- current surface status or error state
- bounded source evidence that still remains trustworthy
- fallback policy for the current surface

## Outputs

- one bounded degraded result or explicit safe stop
- one source-owned stressor receipt
- one clearer reground path to stronger sources
- optional later adaptation delta after a reviewed change

## Core procedure

1. detect the stressor in owner-local language
2. contain the impact to the current run, turn, surface, or action lane
3. degrade honestly into the weakest valid mode that preserves truthfulness
4. reground against stronger authority such as source-owned artifacts, canonical policy, or operator confirmation
5. emit a source-owned receipt that records what failed, what stayed bounded, and what fallback was taken
6. recover later only through an explicit reviewed change that cites the originating receipt

## Contracts

- degraded mode must stay weaker than the normal mode
- blocked actions stay blocked during degradation
- source-owned evidence comes before cross-repo summaries
- regrounding leans on stronger authority rather than speculative completion
- recovery work cites the original receipt instead of rewriting history from memory

## Risks

### Failure modes

- degraded continuation quietly broadens authority or claims equivalent quality to the normal path
- regrounding collapses into speculation instead of leaning on stronger owner-local sources
- source-owned evidence is skipped because the degraded result already worked

### Negative effects

- overusing degraded mode can normalize permanently weaker operation
- extra receipt and fallback ceremony can slow fast local iteration when the stress event is trivial
- a clean degraded surface can create false confidence that recovery pressure no longer matters

### Misuse patterns

- using degraded mode as an excuse for hidden repair automation
- treating any warning string as sufficient evidence instead of publishing a receipt
- claiming regrounding happened when the system only guessed from nearby context

### Detection signals

- degraded outputs look broader or more certain than healthy outputs
- reviewers cannot point to a source-owned receipt for the event
- later remediation work mentions stressors without citing owner-local evidence

### Mitigations

- keep degraded behavior explicitly weaker and machine-readable
- bind each stress event to one owner-local receipt path
- prefer explicit safe stop when no trustworthy reground source remains

## Validation

Verify the technique by confirming that:
- the degraded result or stop condition stayed bounded
- the reground source stayed stronger than speculative completion
- one source-owned receipt was emitted for the stress event
- blocked mutations remained blocked
- later recovery work can cite the original receipt cleanly

## Adaptation notes

What can vary across projects:
- which surfaces degrade
- the names of stressor classes
- whether regrounding uses retrieval, canonical docs, runtime artifacts, or operator confirmation
- where receipts are stored and surfaced

What should stay invariant:
- degraded mode stays weaker than the normal mode
- regrounding uses stronger authority, not broader guessing
- source-owned receipt emission remains explicit
- later recovery cites the originating receipt

## Public sanitization notes

The public bundle removes project-local runtime topology and host details while keeping the reusable degraded-continuation sequence and receipt-first posture intact.

## Example

See `examples/minimal-degraded-handoff.md`.

## Checks

See `checks/degrade-reground-recover-checklist.md`.

## Promotion history

- born from `ATM10-Agent` first-wave hybrid-query degradation review
- promoted into `aoa-techniques` as a public reusable recovery pattern on 2026-04-07

## Future evolution

- add a second public context beyond hybrid-query degradation
- connect more explicitly to bounded eval and stats consumer surfaces
- clarify when explicit safe stop is healthier than degraded continuation
