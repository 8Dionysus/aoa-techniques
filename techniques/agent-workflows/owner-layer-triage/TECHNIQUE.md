---
id: AOA-T-0076
name: owner-layer-triage
domain: agent-workflows
kind: assessment
status: promoted
origin:
  project: aoa-skills
  path: skills/aoa-session-donor-harvest/SKILL.md + skills/aoa-session-donor-harvest/references/owner-layer-map.md
  note: Extracted from the aoa-session-donor-harvest skill where one bounded candidate unit is mapped to one primary owner shape, one next artifact, and one rejected nearest-wrong target.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - owner-layer
  - triage
  - classification
  - boundaries
summary: Route one bounded reusable unit to one primary owner layer and one rejected nearest-wrong target so practice, workflow, scenario, proof, recall, and role surfaces stay distinct instead of collapsing into generic reuse.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-04-05
export_ready: true
relations:
  - type: complements
    target: AOA-T-0075
  - type: complements
    target: AOA-T-0016
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# owner-layer-triage

## Intent

Take one bounded reusable unit and assign it to one primary owner layer, one smallest honest next artifact, and one rejected nearest-wrong target so adjacent surfaces stay distinct and later promotion work starts from an explicit placement verdict.

## When to use

- one reusable unit has already been isolated from its source artifact
- several nearby owner layers look plausible and a primary placement verdict is needed
- the workflow must separate reusable practice, bounded workflow, recurring scenario, proof, recall, role, and hold posture
- the reviewer needs one reason for the chosen owner and one reason against the nearest wrong owner
- derivative routing or graph layers must not become first-authoring targets for source-owned meaning

## When not to use

- the source still contains several mixed units that have not been split yet
- the real need is still raw capture, transcript packaging, replay, or indexing
- the work already has one repeated quest unit and only needs final promotion triage
- the reusable object is a whole context map or ecosystem charter rather than one bounded candidate-unit placement
- the task is purely to derive a derivative bridge after the source-owned artifact already exists elsewhere

## Inputs

- one bounded candidate unit
- evidence anchors that justify the candidate
- a reuse-kind hint such as pattern, mechanic, utility, law, proof, recall, or route
- nearby owner-layer options in scope
- optional local repo or artifact map for the current ecosystem

## Outputs

- one primary owner-layer verdict
- one smallest honest next artifact
- one rejected nearest-wrong target
- one short reason for the chosen owner and one short reason against the rejected owner
- one `hold` outcome when evidence is too weak to place honestly

## Core procedure

1. Start with one bounded candidate unit. Split again first if several units are still fused together.
2. Re-state the unit in reusable form rather than as a session anecdote or topic label.
3. Ask which owner shape the unit primarily belongs to: reusable practice canon, bounded executable workflow, recurring multi-step scenario, proof or verdict surface, recall or writeback surface, role or actor-boundary surface, or hold.
4. Choose one primary owner layer instead of spreading one unit across several surfaces at once.
5. Name the nearest wrong target and explain why it is wrong for this unit.
6. Reject derivative routing, graph, or search layers as first-authoring targets unless the source-owned object already exists elsewhere and only the derivative bridge changed.
7. Name the smallest honest next artifact such as `TECHNIQUE.md`, `SKILL.md`, `PLAYBOOK.md`, `EVAL.md`, memory seed, role note, or `hold`.
8. Preserve `hold` when the evidence is weak, mixed, or still too early.

## Contracts

- one candidate unit maps to one primary owner layer
- usefulness is a reuse signal, not an owner layer by itself
- the nearest wrong target is named explicitly rather than left implicit
- derivative routing or graph layers do not become first-authoring targets for source-owned meaning
- the technique owns one placement verdict, not the whole donor-extraction workflow
- the technique stays smaller than final promotion review for an already repeated quest unit

Relationship to adjacent techniques: unlike [AOA-T-0075](../session-donor-harvest/TECHNIQUE.md), this technique does not extract candidate units from a reviewed session artifact; it only places one already-isolated unit. Unlike [AOA-T-0016](../../docs/bounded-context-map/TECHNIQUE.md), it does not define the full context map or interface structure of a system; it makes one bounded owner verdict over one candidate unit. It should also stay narrower than final quest promotion triage because it can return `hold` or a first owner layer without deciding whether the unit is already ready for canon promotion.

## Risks

### Failure modes

- one mixed unit is forced into one owner layer before it is actually split
- the chosen owner is really just the most convenient repo rather than the honest primary shape
- the nearest wrong target is not named and boundary drift stays hidden

### Negative effects

- a hard owner verdict can create false certainty when evidence is still weak
- reviewers may over-fit placement to the current ecosystem's repo map
- too much placement ceremony can slow down obvious cases

### Misuse patterns

- treating every useful unit as a skill because it feels executable
- pushing source-owned meaning into derivative routing or graph surfaces first
- using the technique as a substitute for donor extraction, proof review, or full context-map design
- collapsing role law, workflow, and scenario composition into one generic reuse bucket

### Detection signals

- reviewers cannot explain why one nearby owner is right and another is wrong
- several owner layers still look equally primary after the verdict is written
- the proposed next artifact is larger than the chosen owner verdict needs
- the same kind of unit is repeatedly misrouted into derivative or convenience surfaces

### Mitigations

- split mixed units before placement
- require one chosen owner and one rejected nearest-wrong target
- keep derivative surfaces as downstream bridges rather than first-authoring targets
- preserve `hold` when evidence is not strong enough for an honest placement verdict

## Validation

Verify the technique by confirming that:
- the candidate unit is bounded and singular
- one primary owner layer is named explicitly
- the nearest wrong target is rejected explicitly
- the chosen next artifact fits the owner verdict
- derivative routing or graph surfaces were not selected as first-authoring targets
- `hold` remains available when evidence is weak or mixed

See `checks/owner-layer-triage-checklist.md`.

## Adaptation notes

What can vary across projects:
- the owner-layer names
- the artifact names used after triage
- how evidence anchors are recorded
- whether local policy requires an extra review step before drafting
- how `hold` or defer states are represented

What should stay invariant:
- one candidate unit gets one primary owner verdict
- the nearest wrong target stays explicit
- the next artifact stays proportional to the verdict
- derivative layers stay downstream of source-owned authoring

Project-shaped details that should not be treated as invariant:
- one specific repo layout
- one promotion board or routing table
- one command or orchestrator syntax
- one local naming convention for notes and bundles

AoA adaptation example:
- reusable practice canon usually maps to `aoa-techniques`
- bounded executable workflow usually maps to `aoa-skills`
- recurring multi-step scenario usually maps to `aoa-playbooks`
- proof or verdict posture usually maps to `aoa-evals`
- recall or writeback posture usually maps to `aoa-memo`
- role or actor-boundary posture usually maps to `aoa-agents`
- derivative routing and KAG surfaces stay downstream unless the source-owned object already exists elsewhere

## Public sanitization notes

This public bundle keeps only the reusable placement contract: take one bounded candidate unit, choose one primary owner shape, reject the nearest wrong target, and name the smallest next artifact. AoA repo names, local routing tables, and skill-specific invocation wrappers were reduced to adaptation examples or kept out of the invariant core.

## Example

See `examples/minimal-owner-layer-triage.md`.

## Checks

See `checks/owner-layer-triage-checklist.md`.

## Promotion history

- born in `aoa-skills` as the owner-placement half of `aoa-session-donor-harvest`
- extracted into `aoa-techniques` on 2026-04-05 as a bounded owner-layer placement workflow

## Future evolution

- keep donor extraction separate through `AOA-T-0075` instead of widening this bundle into a whole post-session harvest stack
- add a second live context that uses the same one-unit placement verdict outside the current AoA session-harvest lineage
- keep final quest promotion review, derivative bridge updates, and broader context-map design in sibling techniques
