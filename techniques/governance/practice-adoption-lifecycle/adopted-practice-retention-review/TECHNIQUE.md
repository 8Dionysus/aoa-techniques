---
id: AOA-T-0103
name: adopted-practice-retention-review
domain: agent-workflows
kind: assessment
status: canonical
origin:
  project: aoa-techniques
  path: mechanics/method-growth/parts/retention-checks/README.md + mechanics/method-growth/PROVENANCE.md
  note: Extracted from the Method-growth retention surface where adopted practice must remain active only while evidence, rollback, and retention posture stay reviewable.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - method-growth
  - retention
  - adoption
  - review
summary: Review one adopted practice against current evidence, usefulness, drift, and rollback posture so it stays active only while retention remains explicit.
maturity_score: 5
rigor_level: bounded
reversibility: moderate
review_required: true
validation_strength: cross_context
public_safety_reviewed_at: 2026-05-13
export_ready: true
relations:
  - type: complements
    target: AOA-T-0101
  - type: complements
    target: AOA-T-0090
  - type: used_together_for
    target: AOA-T-0104
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
  - kind: adverse_effects_review
    path: notes/adverse-effects-review.md
---

# adopted-practice-retention-review

## Intent

Review one already-adopted practice to decide whether it should remain active,
be revised, be quarantined, be deferred for another review, or route toward
obsolescence without silently treating past adoption as permanent approval.

## When to use

- a practice was previously adopted, shadowed, or made part of normal behavior
- the adoption record included a retention watch, review interval, or rollback
  expectation
- evidence, usefulness, owner fit, or negative effects may have changed after
  real use
- reviewers need one explicit retention verdict before keeping the practice
  active
- the next route might be `retain`, `revise`, `quarantine`, `defer`, or
  `route_to_obsolescence`

## When not to use

- the practice has not passed a local adoption gate yet
- the real question is whether to adopt a new shared pattern
- the current task is to deprecate, remove, or supersede the practice directly
- the practice lacks enough real use to evaluate retention
- the work is really a proof verdict, skill activation, route behavior, memory
  writeback, or runtime rollback owned by another layer

## Inputs

- one adopted or shadowed practice under review
- the original adoption note or equivalent owner record
- current evidence of usefulness, fit, or harm
- known drift, negative effects, or support cost
- the active rollback, quarantine, or removal path
- the owner who can confirm whether the practice should remain active
- the next review interval or defer condition

## Outputs

- one retention verdict such as `retain`, `revise`, `quarantine`, `defer`, or
  `route_to_obsolescence`
- a current evidence note
- a drift or negative-effects note
- an owner-confirmation or missing-confirmation note
- a rollback, quarantine, or obsolescence route reminder
- a next review interval or explicit reason no further retention watch is
  needed

## Core procedure

1. Start from one adopted or shadowed practice. Stop if the object is still only
   a proposal, donor candidate, or unreviewed habit.
2. Reopen the original adoption record and name the owner, behavior surface,
   rollback or quarantine path, and retention watch that were promised.
3. Compare current evidence against the reason the practice was adopted:
   usefulness, compatibility, repeated need, reduced risk, or clearer workflow.
4. Look for drift, negative effects, support cost, stale assumptions, or owner
   discomfort that could make retention dishonest.
5. Check whether rollback, quarantine, or removal is still concrete enough to
   use if the practice should stop being active.
6. Emit one retention verdict. Use `retain` only when evidence, owner fit, and
   rollback posture remain visible.
7. Route `quarantine` or `route_to_obsolescence` without performing deletion,
   deprecation, skill activation, proof claims, or memory writeback inside this
   technique.

## Contracts

- one review covers one adopted or shadowed practice and one owner surface
- past adoption does not guarantee current retention
- `retain` requires current evidence, owner fit, and usable rollback or
  quarantine posture
- `revise`, `quarantine`, `defer`, and `route_to_obsolescence` are honest
  results, not failed retention
- the review does not adopt a new practice, delete an old practice, activate a
  skill, issue a proof verdict, write memory truth, or mutate runtime behavior
- missing evidence, missing owner confirmation, or unusable rollback must stop
  the result short of `retain`

Relationship to adjacent techniques: unlike
[AOA-T-0101](../local-pattern-adoption-gate/TECHNIQUE.md), this technique does
not decide whether a shared pattern may become local behavior; it reviews a
practice after adoption or shadow use. Unlike
[AOA-T-0090](../../promotion-boundary/nearest-wrong-target-rejection/TECHNIQUE.md), it does not only
reject an adjacent promotion target; it emits the retention verdict itself.

## Risks

### Failure modes

- retention review becomes a ceremonial renewal with no current evidence
- `retain` is chosen because removing the practice feels inconvenient
- drift, support cost, or owner discomfort is hidden behind old adoption notes

### Negative effects

- frequent retention reviews can burden simple low-risk conventions
- a quarantine verdict can interrupt useful local practice if evidence is
  under-collected
- retention language can make a practice seem more permanent than the evidence
  supports

### Misuse patterns

- using retention review to adopt a new practice without an adoption gate
- using retention review to deprecate or delete without an obsolescence route
- treating a retained practice as proof of quality or public default status
- hiding missing rollback behind "we have used it for a while" language

### Detection signals

- reviewers cannot find the original adoption or shadow-use record
- the write-up has old rationale but no current evidence
- rollback, quarantine, or obsolescence route is vague or unusable
- no owner can confirm that the practice still belongs on the active surface
- the verdict jumps from stale use directly to permanent retention

### Mitigations

- require one current evidence note before `retain`
- keep owner confirmation visible
- prefer `defer`, `revise`, or `quarantine` when rollback or evidence is weak
- route actual deprecation, removal, proof, memory, and runtime changes to their
  owners
- schedule the next review when active retention still needs a watch

## Validation

Verify the technique by confirming that:
- one adopted or shadowed practice is named
- the original owner surface and adoption record are visible
- current evidence is compared against the adoption reason
- drift, negative effects, and support cost were checked
- rollback, quarantine, or obsolescence route is concrete enough to use
- the verdict does not imply new adoption, deletion, proof, memory, skill, or
  runtime activation

See `checks/adopted-practice-retention-review-checklist.md`.

## Adaptation notes

What can vary across projects:
- retention verdict labels
- adoption-record format
- retention interval
- what counts as owner confirmation
- whether the review is recorded in Markdown, YAML, issue comments, or a local
  review packet

What should stay invariant:
- past adoption does not equal current retention
- current evidence and owner fit are required before `retain`
- rollback, quarantine, or obsolescence route remains visible
- the review stops before deletion, proof, memory, runtime, or skill activation

Project-shaped details that should not be treated as invariant:
- one repository map
- one retention schedule
- one changelog or decision-note format
- one runtime rollback mechanism
- one proof or evaluation pipeline

AoA adaptation example:
- a Method-growth retention watch can ask whether an adopted technique-layer
  practice should remain active in `aoa-techniques`
- obsolescence or supersession routes stay in the Method-growth obsolescence
  part until a separate atom is extracted
- memory retention reasons route to `aoa-memo`, proof claims to `aoa-evals`,
  and skill execution changes to `aoa-skills`

## Public sanitization notes

This public bundle keeps only the portable retention review: one adopted
practice, current evidence, owner fit, drift check, rollback or quarantine path,
and one bounded retention verdict. AoA center wording, session-specific
decisions, local command wrappers, and sibling-owner acceptance mechanics were
reduced to provenance and adaptation context.

## Example

See `examples/minimal-adopted-practice-retention-review.md`.

## Checks

See `checks/adopted-practice-retention-review-checklist.md`.

## Promotion history

- born in `aoa-techniques` Method-growth mechanics as part of the v0.7
  downstream adoption wave
- extracted into `aoa-techniques` on 2026-05-03 as one bounded retention review
  rather than adoption, obsolescence, proof, memory, skill, or runtime authority

## Future evolution

- keep obsolescence and supersession in Method-growth until a separate atomic
  practice is proven
- add one second live context where an adopted practice is retained or
  quarantined by the same review shape outside the Method-growth extraction
  wave
- consider typed retention verdict examples only after several projects reuse
  the same output fields
