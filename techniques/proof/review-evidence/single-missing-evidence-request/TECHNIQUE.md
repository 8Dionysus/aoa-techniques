---
id: AOA-T-0105
name: single-missing-evidence-request
domain: agent-workflows
kind: guardrail
status: promoted
origin:
  project: aoa-techniques
  path: mechanics/distillation/parts/agon-candidate-handoff/gates/bundle-reviews/request-evidence-bundle-readiness-review.md
  note: Extracted from the Distillation Agon handoff where request_evidence was narrowed into one portable review-state guardrail without importing Agon move law or proof authority.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - evidence
  - review
  - guardrail
  - small-agent
summary: Ask for exactly one missing evidence object that could change a bounded review state so review can narrow without broad research, verdict overclaim, or proof theater.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-05-03
export_ready: true
relations:
  - type: complements
    target: AOA-T-0081
  - type: complements
    target: AOA-T-0032
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# single-missing-evidence-request

## Intent

Ask for exactly one missing evidence object that could change a bounded review
state, so review can narrow without broad research, verdict overclaim, or proof
theater.

## When to use

- one claim, decision, generated artifact, route, or review state is already in
  view
- the current blocker is a missing evidence object, not a missing full
  investigation
- the object can be supplied, linked, quoted, rerun, or honestly declared absent
- the reviewer needs to keep work moving without pretending the absent object is
  a verdict
- a small agent needs a compact request pattern instead of a broad research plan

## When not to use

- the real task is to prove correctness, score quality, or issue an evaluation
  verdict
- the review surface is not bounded to one claim or decision
- several different evidence objects are equally necessary
- the missing item is not concrete enough for another agent or human to provide
- asking for evidence would mutate routing, runtime, memory, skill activation,
  KAG state, ToS canon, Agon law, or proof authority

## Inputs

- one reviewed claim, decision, artifact, or route state
- the current review state or evidence gap
- one missing evidence object that might change, narrow, or reopen the review
- the acceptable form of that object, such as a command receipt, source line,
  linked artifact, saved note, or explicit absence statement
- the reason that this object matters now
- the return condition for both present and absent evidence

## Outputs

- one evidence request naming the reviewed claim or decision
- one concrete missing evidence object
- one short reason the object matters to the review state
- one return condition if the object appears
- one return condition if the object remains unavailable
- no proof verdict, no broad research assignment, and no owner-law mutation

## Core procedure

1. Name the single claim, decision, artifact, or route state under review.
2. State the current evidence gap in one sentence.
3. Choose the smallest missing evidence object that could change or narrow the
   review.
4. Name the acceptable form of the object so it can be supplied or declared
   absent.
5. Explain how the object would change, narrow, or reopen the review state.
6. State what happens if the object appears and what remains blocked if it is
   absent.
7. Stop after the one request. Do not widen into a full research plan, proof
   verdict, route change, memory write, or Agon move.

## Contracts

- one use of the technique asks for one missing evidence object
- the request is tied to one bounded review state
- the object must be concrete enough to supply, rerun, cite, or declare absent
- missing evidence may block or narrow review, but it is not proof of failure
- the output is read-only and smaller than evaluation, routing, runtime,
  memory, skill, KAG, ToS, or Agon authority
- the technique does not define Agon evidence law; it only distills a portable
  evidence-request atom for ordinary technique use

Relationship to adjacent techniques: unlike
[AOA-T-0081](../../../recovery/diagnosis-repair/diagnosis-from-reviewed-evidence/TECHNIQUE.md),
this technique does not turn reviewed evidence into a diagnosis packet; it asks
for one missing object before diagnosis or closure. Unlike
[AOA-T-0032](../../evaluation-chain/context-report-for-ci/TECHNIQUE.md), it
does not emit a broad CI-facing context report; it names the one object whose
presence or absence matters now.

## Risks

### Failure modes

- the request names a vague category instead of one concrete object
- the agent asks for several items and hides a research plan inside the request
- the absent object is treated as proof rather than as a review-state blocker
- the request does not explain how the object would affect the review

### Negative effects

- overuse can slow work by asking for receipts when current evidence is already
  enough
- a poorly scoped request can push burden onto another agent without improving
  the review
- the technique can make missing-evidence language feel more authoritative than
  it is

### Misuse patterns

- asking for "all evidence" or "more context" instead of one object
- demanding a source that cannot reasonably exist for the current surface
- using the request as a disguised verdict against the current claim
- importing Agon, proof, rank, scar, route, memory, or evaluation authority into
  a small read-only evidence request

### Detection signals

- the output contains more than one requested object
- reviewers cannot tell what would change if the object appears
- the request has no explicit absent-evidence return condition
- the wording says or implies that the missing object proves the claim false
- the request starts mutating owner state instead of narrowing review

### Mitigations

- force the request to one claim, one object, one reason, and two return
  conditions
- prefer the smallest rerunnable or inspectable object over broad context
- say explicitly that absence blocks or narrows review but does not prove
  failure
- route proof, evaluation, memory, KAG, ToS, runtime, skill, and Agon questions
  to their own owner surfaces

## Validation

Verify the technique by confirming that:
- exactly one claim or decision point is named
- exactly one missing evidence object is requested
- the object is concrete enough to provide or declare absent
- the request explains why the object matters to the current review state
- both present and absent return conditions are explicit
- the output does not issue a proof verdict, broad research plan, route change,
  memory write, skill activation, KAG promotion, ToS canon change, or Agon law

See `checks/single-missing-evidence-request-checklist.md`.

## Adaptation notes

What can vary across projects:
- the accepted evidence form
- whether the request is written as prose, YAML, checklist item, or review
  comment
- who supplies the object
- whether absence means defer, hold, rerun, or narrow the claim

What should stay invariant:
- one bounded review state
- one missing evidence object
- one reason the object matters
- one present-evidence return condition
- one absent-evidence return condition
- no proof, route, memory, skill, KAG, ToS, runtime, or Agon authority

Project-shaped details that should not be treated as invariant:
- AoA repository names
- Agon move labels
- local CI commands
- local generated-output receipts
- one handoff packet format

AoA adaptation example:
- a Distillation candidate may request one builder receipt before trusting a
  generated handoff index
- a technique review may request one source line before accepting an origin
  claim
- an agent handoff may request one git-visible artifact before continuing a
  resumed thread

## Public sanitization notes

This public bundle keeps only the reusable evidence-request atom. Agon move law,
arena effects, rank/scar language, private session details, and local proof
authority stay outside the technique. The source project names are retained only
as provenance and adaptation context.

## Example

See `examples/minimal-single-missing-evidence-request.md`.

## Checks

See `checks/single-missing-evidence-request-checklist.md`.

## Promotion history

- born in the Distillation Agon candidate handoff as a `request_evidence`
  first-narrowing candidate
- shaped through a gate card, public-safe example, checklist, evidence note,
  and bundle-readiness review
- promoted in `aoa-techniques` on 2026-05-03 as a source-backed guardrail bundle
  without changing the source Agon status

## Future evolution

- collect a second-context adaptation from ordinary code review, documentation
  review, or generated-output review
- revisit canonical readiness only after second-context evidence shows the same
  atom outside the Agon handoff
- watch the boundary with evaluation so missing evidence does not become a
  proof verdict by habit
