---
id: AOA-T-0107
name: single-locus-claim-challenge
domain: agent-workflows
kind: guardrail
status: canonical
origin:
  project: aoa-techniques
  path: mechanics/distillation/parts/agon-candidate-handoff/gates/bundle-reviews/challenge-claim-bundle-readiness-review.md
  note: Extracted from the Distillation Agon handoff where challenge_claim was narrowed into one portable claim-pressure guardrail without importing Agon move law, proof authority, actor eligibility, or eval relevance checks.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - challenge
  - claim
  - review
  - evidence
  - small-agent
summary: Challenge exactly one claim at one vulnerable locus, naming pressure reason and next support question so review can apply pressure without turning challenge into proof, tone, or adjudication.
maturity_score: 5
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: cross_context
public_safety_reviewed_at: 2026-05-13
export_ready: true
relations:
  - type: complements
    target: AOA-T-0105
  - type: complements
    target: AOA-T-0106
  - type: complements
    target: AOA-T-0081
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

# single-locus-claim-challenge

## Intent

Challenge exactly one claim at one vulnerable locus, naming pressure reason and
next support question so review can apply pressure without turning challenge
into proof, tone, or adjudication.

## When to use

- one claim, assertion, generated summary, route statement, or review sentence
  is already in view
- the claim may be too broad, unsupported, overconfident, underspecified, or
  resting on the wrong support surface
- the reviewer needs to apply pressure before asking for evidence, diagnosing
  contradiction, or accepting closure
- one vulnerable locus can be named inside the claim
- a small agent needs a compact challenge pattern instead of a debate plan

## When not to use

- the real task is to prove or disprove the claim
- several claims need to be compared, ranked, or synthesized
- the vulnerable locus cannot be named
- the issue is already a localized contradiction needing contradiction
  handling
- challenging the claim would mutate routing, runtime, memory, skill
  activation, KAG state, ToS canon, Agon law, actor eligibility, or proof
  authority

## Inputs

- one target claim
- the current review state
- one vulnerable locus inside the claim
- one pressure reason showing why that locus is vulnerable
- one next evidence, scope, or revision question
- one non-verdict stop condition

## Outputs

- one challenged claim statement
- one vulnerable-locus statement
- one pressure-reason statement
- one next-support question
- one non-verdict stop condition
- no proof verdict, no personal attack, no debate plan, and no owner-law
  mutation

## Core procedure

1. Quote or name the single target claim.
2. Identify the smallest vulnerable locus inside the claim.
3. State why that locus is under pressure.
4. Ask the next evidence, scope, or revision question that would answer the
   pressure.
5. State the stop condition that keeps the challenge below proof, diagnosis,
   adjudication, route change, memory write, or Agon move.
6. Stop after the one challenge. Do not widen into broad debate, proof verdict,
   tone critique, contradiction resolution, or workflow assignment.

## Contracts

- one use of the technique challenges one target claim
- the challenged locus is smaller than the whole topic, actor, repo, or route
- the pressure reason addresses support, scope, or wording rather than tone
- the next support question is concrete enough to answer, narrow, or defer
- the stop condition makes clear that the challenge does not prove the claim
  false
- the output is read-only and smaller than evaluation, routing, runtime,
  memory, skill, KAG, ToS, actor, or Agon authority
- the technique does not define Agon challenge law; it only distills a portable
  claim-pressure guardrail for ordinary technique use

Relationship to adjacent techniques: unlike
[AOA-T-0105](../single-missing-evidence-request/TECHNIQUE.md), this technique
names the vulnerable claim locus before asking for a specific missing evidence
object. Unlike
[AOA-T-0106](../single-scoped-evidence-reference/TECHNIQUE.md), it does not
offer an available reference; it applies pressure to the claim that may need
support. Unlike
[AOA-T-0081](../../../recovery/diagnosis-repair/diagnosis-from-reviewed-evidence/TECHNIQUE.md),
it does not diagnose from reviewed evidence or name probable causes.

## Risks

### Failure modes

- the challenge targets a broad topic instead of one claim
- the vulnerable locus is vague or missing
- the pressure reason becomes tone critique rather than support pressure
- the next support question is too broad to answer
- the challenge implies a verdict without proof

### Negative effects

- overuse can make ordinary review feel adversarial
- vague challenges can slow work without improving evidence quality
- a challenge can be mistaken for rejection if the non-verdict stop condition
  is missing

### Misuse patterns

- challenging a person, team, repo, or worldview instead of a claim
- using "challenge" language to smuggle adjudication authority
- demanding all evidence instead of naming one next support question
- escalating into debate choreography, role pressure, or arena language
- importing proof, eval, rank, scar, route, memory, KAG, ToS, runtime, skill, or
  actor authority into a small read-only challenge

### Detection signals

- the output contains multiple target claims
- reviewers cannot point to the challenged locus
- the challenge says or implies that the claim is false
- the next question is "prove everything" or "give more context"
- the output starts assigning routes, verdicts, actors, or workflow tasks

### Mitigations

- force the output to one claim, one locus, one pressure reason, one next
  support question, and one stop condition
- quote or name the exact claim before applying pressure
- prefer support, scope, or wording pressure over tone critique
- say explicitly that the challenge is not proof or adjudication
- route proof, evaluation, memory, KAG, ToS, runtime, skill, actor, and Agon
  questions to their own owner surfaces

## Validation

Verify the technique by confirming that:
- exactly one target claim is named
- exactly one vulnerable locus is named inside that claim
- the pressure reason explains why the locus is vulnerable
- the next support question is concrete enough to answer, narrow, or defer
- the stop condition says the challenge is not proof, verdict, or adjudication
- the output does not issue proof, evaluation, route, memory, runtime, skill,
  KAG, ToS, actor, or Agon effects

See `checks/single-locus-claim-challenge-checklist.md`.

## Adaptation notes

What can vary across projects:
- the form of the target claim
- whether the challenge is written as prose, YAML, checklist item, review
  comment, or compact artifact card
- who answers the next support question
- whether the next support question asks for evidence, scope narrowing, wording
  revision, or explicit deferment

What should stay invariant:
- one target claim
- one vulnerable locus
- one pressure reason
- one next support question
- one non-verdict stop condition
- no proof, route, memory, skill, KAG, ToS, runtime, eval, actor, or Agon
  authority

Project-shaped details that should not be treated as invariant:
- AoA repository names
- Agon move labels
- local generated-output paths
- local release-check receipts
- one handoff packet format

AoA adaptation example:
- a Distillation candidate may challenge the claim that a generated index is
  "complete" by asking which reader or manifest entry exposes the new unit
- a technique review may challenge a summary that says "validated" when the
  support only proves schema validity
- an agent handoff may challenge a continuation claim that lacks a visible git
  or artifact anchor

## Public sanitization notes

This public bundle keeps only the reusable claim-pressure guardrail. Agon move
law, actor eligibility, arena effects, rank/scar language, private session
details, and local proof authority stay outside the technique. Source project
names are retained only as provenance and adaptation context.

## Example

See `examples/minimal-single-locus-claim-challenge.md`.

## Checks

See `checks/single-locus-claim-challenge-checklist.md`.

## Promotion history

- born in the Distillation Agon candidate handoff as a `challenge_claim`
  first-narrowing candidate
- shaped through a gate card, public-safe example, checklist, evidence note,
  and bundle-readiness review
- promoted in `aoa-techniques` on 2026-05-03 as a source-backed guardrail
  bundle without changing the source Agon status

## Future evolution

- collect additional ordinary code-review, documentation-review, or
  generated-output examples when they keep the atom to one challenged locus
- watch the boundary with evaluation so challenge pressure does not become a
  proof verdict by habit
