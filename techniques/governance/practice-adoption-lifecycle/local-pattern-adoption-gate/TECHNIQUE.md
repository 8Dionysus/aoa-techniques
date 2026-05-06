---
id: AOA-T-0101
name: local-pattern-adoption-gate
domain: agent-workflows
kind: guardrail
status: promoted
origin:
  project: aoa-techniques
  path: mechanics/method-growth/parts/pattern-adoption/README.md + mechanics/method-growth/PROVENANCE.md
  note: Extracted from the Method-growth adoption surface where a shared pattern must pass a second local adoption act before it becomes durable behavior.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - method-growth
  - adoption
  - owner-consent
  - rollback
summary: Gate one shared pattern before local adoption by requiring owner consent, compatibility evidence, rollback, and retention watch so precedent does not silently become durable behavior.
maturity_score: 3
rigor_level: bounded
reversibility: moderate
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-05-03
export_ready: true
relations:
  - type: complements
    target: AOA-T-0076
  - type: complements
    target: AOA-T-0090
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# local-pattern-adoption-gate

## Intent

Gate one shared practice pattern before it becomes durable local behavior, so
approval, precedent, or repeated usefulness does not silently turn into local
adoption without owner consent, compatibility evidence, rollback, and retention
watch.

## When to use

- a shared practice pattern has already been noticed, approved upstream, or
  proven useful elsewhere
- a local repository, team, or owner surface is considering making that pattern
  part of normal behavior
- the pattern might change contributor instructions, review expectations,
  generated surfaces, operating habits, or default workflow posture
- the reviewer needs one adoption gate before drafting implementation or
  activation changes
- shadow use, quarantine, defer, or reject outcomes should remain honest
  possibilities

## When not to use

- the source material is still several mixed patterns that have not been split
- the real task is choosing the owner layer for an isolated reusable unit
- the work only needs a nearest-wrong-target rejection beside an already chosen
  verdict
- the pattern already has explicit local adoption, rollback, and retention
  evidence and only needs implementation
- the request is to activate a skill, runtime, route, proof verdict, or memory
  object that belongs to another owner

## Inputs

- one shared pattern proposed for local adoption
- the local owner or surface that would change behavior
- source or precedent evidence for the pattern
- compatibility notes for the local context
- owner consent state
- rollback or quarantine option
- retention watch or review interval

## Outputs

- one local adoption gate result such as `adopt`, `shadow`, `quarantine`,
  `defer`, or `reject`
- one owner-consent statement or missing-consent blocker
- one compatibility and evidence note
- one rollback or quarantine path
- one retention watch note for later review

## Core procedure

1. Start from one named shared pattern. Split or hold if several patterns are
   still fused together.
2. Name the local owner and the exact behavior surface that would change if the
   pattern were adopted.
3. Check whether local owner consent is explicit. If it is not, stop at
   `defer` or `shadow` instead of adopting.
4. Compare the pattern's source evidence with the local compatibility
   conditions that matter for this surface.
5. Require a rollback, quarantine, or removal path before any durable behavior
   change is accepted.
6. Require a retention watch so adoption can be revisited after real use.
7. Emit one bounded adoption gate result. Keep the result smaller than the
   implementation, skill proposal, proof verdict, route change, or runtime
   activation that may follow.

## Contracts

- one gate result covers one shared pattern and one local behavior surface
- upstream approval or useful precedent is not local adoption
- owner consent, compatibility evidence, rollback, and retention watch must all
  stay visible
- `shadow`, `quarantine`, `defer`, and `reject` are valid outcomes, not failed
  adoption
- the gate does not grant skill activation, proof authority, route behavior,
  runtime mutation, memory truth, or sibling owner acceptance

Relationship to adjacent techniques: unlike
[AOA-T-0076](../../decision-routing/owner-layer-triage/TECHNIQUE.md), this technique does not choose
the primary owner layer for any reusable unit; it assumes a local adoption
surface is already in view and gates whether that surface may change behavior.
Unlike [AOA-T-0090](../../promotion-boundary/nearest-wrong-target-rejection/TECHNIQUE.md), it does
not only sharpen a chosen verdict by rejecting an adjacent target; it emits the
local adopt, shadow, quarantine, defer, or reject posture itself.

## Risks

### Failure modes

- a broad method-growth lifecycle is squeezed into one gate result
- owner consent is implied from usefulness or upstream approval
- rollback and retention are named symbolically but cannot actually be used

### Negative effects

- too much adoption ceremony can slow clearly low-risk local conventions
- a gate result can make tentative shadow practice look more settled than it is
- local owners may overfit the pattern to one repo and weaken portability

### Misuse patterns

- treating the gate as permission to implement or activate the pattern
- using upstream approval as a substitute for local owner consent
- calling a pattern adopted because it appeared in one successful session
- hiding missing rollback behind vague "can revert later" language

### Detection signals

- the adoption note cannot name the local behavior surface that changes
- consent, rollback, or retention fields are blank or generic
- the result jumps from precedent directly to implementation
- reviewers cannot tell whether the posture is `adopt`, `shadow`, `quarantine`,
  `defer`, or `reject`

### Mitigations

- keep the gate to one pattern and one local behavior surface
- require explicit owner consent before `adopt`
- prefer `shadow`, `quarantine`, or `defer` when compatibility or rollback is
  weak
- record a retention watch so adoption can be rechecked after real use

## Validation

Verify the technique by confirming that:
- one shared pattern is named explicitly
- one local owner and behavior surface are named explicitly
- owner consent is explicit or the result stops short of `adopt`
- compatibility evidence is visible
- rollback or quarantine is concrete enough to use
- a retention watch exists
- the result does not imply skill, route, proof, runtime, memory, or sibling
  owner activation

See `checks/local-pattern-adoption-gate-checklist.md`.

## Adaptation notes

What can vary across projects:
- the names of local owners and behavior surfaces
- the allowed gate result labels
- whether shadow practice is recorded in prose, YAML, or a review packet
- how retention watches are scheduled or reviewed

What should stay invariant:
- upstream approval does not equal local adoption
- one pattern gates against one local behavior surface
- owner consent, compatibility, rollback, and retention remain visible
- the gate stays smaller than implementation or activation

Project-shaped details that should not be treated as invariant:
- one AoA repository map
- one Method-growth vocabulary
- one PR template or review checklist
- one command, bot, or runtime activation path

AoA adaptation example:
- a pattern may originate from `Agents-of-Abyss`, `aoa-skills`, or another
  sibling surface
- `aoa-techniques` can adopt only the technique-layer practice posture it owns
- skill execution, proof verdicts, route behavior, memory objects, and runtime
  changes still require their own owners after the gate

## Public sanitization notes

This public bundle keeps only the reusable adoption guardrail: one shared
pattern, one local owner surface, explicit consent, compatibility evidence,
rollback or quarantine, and retention watch. AoA center law, private session
detail, local command wrappers, and sibling-owner acceptance mechanics were
reduced to provenance and adaptation context rather than made part of the core
technique.

## Example

See `examples/minimal-local-pattern-adoption-gate.md`.

## Checks

See `checks/local-pattern-adoption-gate-checklist.md`.

## Promotion history

- born in `aoa-techniques` Method-growth mechanics as part of the v0.7
  downstream adoption wave
- extracted into `aoa-techniques` on 2026-05-03 as one bounded local adoption
  gate rather than the full Method-growth lifecycle

## Future evolution

- keep broader adoption lifecycle hooks in Method-growth instead of widening
  this bundle into adoption governance
- add one second live context where a non-Method-growth surface uses the same
  consent, rollback, and retention gate before local adoption
- consider a separate retention or obsolescence technique only after those
  parts prove one atomic reusable move of their own
