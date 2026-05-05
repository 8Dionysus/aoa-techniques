---
id: AOA-T-0106
name: single-scoped-evidence-reference
domain: docs
kind: artifact
status: promoted
origin:
  project: aoa-techniques
  path: mechanics/distillation/parts/agon-candidate-handoff/gates/bundle-reviews/offer-evidence-reference-bundle-readiness-review.md
  note: Extracted from the Distillation Agon handoff where offer_evidence_reference was narrowed into one portable reference artifact without importing Agon move law, proof authority, or eval adequacy checks.
owners:
  - 8Dionysus
tags:
  - docs
  - evidence
  - reference
  - citation
  - review
  - small-agent
summary: Offer exactly one scoped evidence reference with relevance, support limit, and reliance condition so review can use a source without treating it as proof, verdict, or source-truth transfer.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-05-03
export_ready: true
relations:
  - type: complements
    target: AOA-T-0105
  - type: complements
    target: AOA-T-0043
  - type: complements
    target: AOA-T-0034
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# single-scoped-evidence-reference

## Intent

Offer exactly one scoped evidence reference with relevance, support limit, and
reliance condition so review can use a source without treating it as proof,
verdict, or source-truth transfer.

## When to use

- one claim, decision, review state, or documentation statement is already in
  view
- one available source, line, artifact, excerpt, command receipt, or citation
  can help a reviewer inspect the current claim
- the useful move is to provide a reference and its limits, not to prove the
  claim
- the reviewer needs to know how the reference may be used before relying on it
- a small agent needs a compact citation artifact instead of multi-source
  provenance or an evaluation check

## When not to use

- the real task is to prove correctness, score adequacy, or issue an evaluation
  verdict
- the review needs several sources ordered by priority
- the source is not inspectable, quotable, rerunnable, or rejectable
- the reference would expose private logs, credentials, user data, or sensitive
  operational detail
- offering the reference would mutate routing, runtime, memory, skill
  activation, KAG state, ToS canon, Agon law, or proof authority

## Inputs

- one reviewed claim, decision point, artifact statement, or route state
- one available evidence reference
- the exact form of the reference, such as path, line, receipt, quoted excerpt,
  artifact pointer, or stable citation
- one reason the reference is relevant to the reviewed claim
- the support scope the reference can honestly carry
- the support limit the reference cannot carry
- the reliance condition before the reference is used in review

## Outputs

- one scoped evidence reference
- one relevance statement
- one support-scope statement
- one support-limit statement
- one reliance condition for review
- no proof verdict, no source-truth transfer, no multi-source provenance pack,
  and no owner-law mutation

## Core procedure

1. Name the single claim, decision, artifact statement, or route state under
   review.
2. Choose one inspectable evidence reference already available to the review.
3. State why the reference is relevant to that one claim or decision.
4. State the narrow support scope the reference can honestly carry.
5. State the support limit the reference cannot carry.
6. State the reliance condition before the reference is cited, accepted, or used
   downstream.
7. Stop after the one reference. Do not widen into a citation bundle, proof
   verdict, eval adequacy check, route change, memory write, or Agon move.

## Contracts

- one use of the technique offers one evidence reference
- the reference is tied to one bounded review state
- the reference must be inspectable enough for another reviewer to accept,
  reject, quote, rerun, or ask for a different source
- the support scope and support limit are both explicit
- reliance is conditional until the reviewer inspects the reference
- the output is read-only and smaller than evaluation, routing, runtime,
  memory, skill, KAG, ToS, or Agon authority
- the technique does not define Agon evidence law; it only distills a portable
  evidence-reference atom for ordinary technique use

Relationship to adjacent techniques: unlike
[AOA-T-0105](../../agent-workflows/single-missing-evidence-request/TECHNIQUE.md),
this technique offers one available reference instead of asking for one missing
evidence object. Unlike
[AOA-T-0043](../multi-source-primary-input-provenance/TECHNIQUE.md), it does not
order multiple primary and supporting inputs. Unlike
[AOA-T-0034](../../instruction/docs-boundary/public-safe-artifact-sanitization/TECHNIQUE.md), it does not
transform or sanitize the referenced artifact.

## Risks

### Failure modes

- the reference is vague and cannot be inspected
- the agent offers several references and hides a provenance bundle inside the
  output
- the reference is treated as proof instead of one bounded support object
- the support limit is missing, so reviewers overread what the reference proves
- the reliance condition is missing, so downstream work treats the citation as
  already accepted

### Negative effects

- overuse can clutter reviews with narrow citations when the issue is already
  settled
- a poorly scoped reference can make weak support look stronger than it is
- the technique can slow review if it becomes a citation ritual rather than a
  focused support artifact

### Misuse patterns

- linking to a broad page and calling it evidence without a relevance statement
- using one source to smuggle a proof verdict
- laundering source-truth authority from an owning repo into a derived note
- treating the reference as evaluation adequacy, route permission, memory
  intake, KAG promotion, ToS canon, or Agon law
- citing private or sensitive material without public-safety review

### Detection signals

- the output contains more than one reference
- reviewers cannot tell what the reference can and cannot support
- the reference is not inspectable by the intended reviewer
- wording says or implies that the reference settles the full claim
- the output starts mutating owner state instead of supporting review

### Mitigations

- force the output to one claim, one reference, one relevance statement, one
  support scope, one support limit, and one reliance condition
- prefer the smallest stable pointer or excerpt that can be reviewed
- say explicitly that the reference is not proof, verdict, or source-truth
  transfer
- route proof, evaluation, memory, KAG, ToS, runtime, skill, and Agon questions
  to their own owner surfaces
- sanitize or withhold references that expose private or sensitive detail

## Validation

Verify the technique by confirming that:
- exactly one claim or decision point is named
- exactly one evidence reference is offered
- the reference is concrete enough to inspect, quote, rerun, or reject
- the relevance statement explains why the reference matters to the review
- the support scope and support limit are both explicit
- the reliance condition is explicit
- the output does not issue proof, evaluation, route, memory, runtime, skill,
  KAG, ToS, or Agon effects

See `checks/single-scoped-evidence-reference-checklist.md`.

## Adaptation notes

What can vary across projects:
- the reference form
- whether the reference appears as prose, YAML, checklist item, review comment,
  citation note, or compact artifact card
- who inspects the reference
- whether reliance means cite, defer, rerun, quote, or request a stronger source

What should stay invariant:
- one bounded review state
- one evidence reference
- one relevance statement
- one support scope
- one support limit
- one reliance condition
- no proof, route, memory, skill, KAG, ToS, runtime, eval, or Agon authority

Project-shaped details that should not be treated as invariant:
- AoA repository names
- Agon move labels
- local generated-output paths
- local command receipts
- one handoff packet format

AoA adaptation example:
- a Distillation candidate may offer one generated index path to support that a
  handoff pointer landed, while saying it does not prove canonical readiness
- a technique review may offer one source line to support an origin claim,
  while routing proof adequacy to a separate check
- a docs review may offer one sanitized excerpt for public sharing, while
  keeping private logs outside the public artifact

## Public sanitization notes

This public bundle keeps only the reusable evidence-reference atom. Agon move
law, arena effects, rank/scar language, private session details, and local proof
authority stay outside the technique. Source project names are retained only as
provenance and adaptation context.

## Example

See `examples/minimal-single-scoped-evidence-reference.md`.

## Checks

See `checks/single-scoped-evidence-reference-checklist.md`.

## Promotion history

- born in the Distillation Agon candidate handoff as an
  `offer_evidence_reference` first-narrowing candidate
- shaped through a gate card, public-safe example, checklist, evidence note,
  and bundle-readiness review
- promoted in `aoa-techniques` on 2026-05-03 as a source-backed artifact bundle
  without changing the source Agon status

## Future evolution

- collect a second-context adaptation from ordinary code review, documentation
  review, or generated-output review
- revisit canonical readiness only after second-context evidence shows the same
  atom outside the Agon handoff
- use the bundle as evidence for future topology reform across family,
  capability, substrate, execution, and risk axes
