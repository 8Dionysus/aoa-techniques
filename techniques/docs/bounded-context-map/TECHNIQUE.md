---
id: AOA-T-0016
name: bounded-context-map
domain: docs
kind: artifact
status: canonical
origin:
  project: atm10-agent
  path: planning-layer
  note: Extracted from repeated need to keep agent work semantically scoped by clarifying domain and subsystem boundaries.
owners:
  - 8Dionysus
tags:
  - architecture
  - ddd-lite
  - contexts
  - vocabulary
summary: Reduce semantic drift by naming bounded contexts, separating responsibilities, and making handoff interfaces visible for docs and scoping work.
maturity_score: 5
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: cross_context
public_safety_reviewed_at: 2026-03-20
export_ready: true
relations:
  - type: complements
    target: AOA-T-0002
  - type: complements
    target: AOA-T-0001
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

# bounded-context-map

## Intent

Reduce semantic confusion and misplaced changes by naming bounded contexts, clarifying their responsibilities, and making the handoff interfaces between them visible.

## When to use

- repositories with several domains, services, or subsystems that can blur together
- situations where naming is overloaded or ambiguous
- docs or scoping work that needs a compact boundary map before implementation widens the wrong area
- agent-assisted work where semantic confusion would widen the context unnecessarily

## When not to use

- tiny repositories with no meaningful subsystem ambiguity
- changes that are fully local and already clearly bounded
- situations where drawing context labels would only add ceremony without reducing confusion
- broad architecture redesigns where the real need is deeper design work, not a bounded context map

## Inputs

- target area, subsystem, or domain surface
- current vocabulary and responsibilities
- neighboring areas likely to be confused with the target
- known ambiguous or overloaded terms

## Outputs

- named bounded contexts or subsystem groupings
- rough responsibility map
- visible handoff or interface notes
- ambiguity notes and recommended vocabulary

## Core procedure

1. identify the target area and the words currently used to describe it
2. separate responsibilities into bounded contexts or subsystem groupings
3. name what belongs inside each context and what stays outside
4. describe the handoff points, interfaces, or translation surfaces between contexts
5. surface ambiguous terms and propose clearer language
6. report how the map should constrain future changes or reviews

## Contracts

- context boundaries should reduce semantic confusion rather than create taxonomy for its own sake
- neighboring contexts should be named explicitly when they matter
- handoff or translation points should be visible
- the result should help a future reviewer scope docs or implementation work more safely

## Risks

### Failure modes

- too many contexts are invented for a small problem
- the map renames concepts without reducing ambiguity or scoping the next change more safely
- interfaces remain muddy even after the map is drawn, so the artifact looks cleaner than the work actually feels

### Negative effects

- over-structuring can slow small projects if no real confusion exists
- premature context formalization can freeze evolving vocabulary too early
- a polished map can create false architectural confidence even while handoffs, ownership, or translation points remain implicit
- the map can become generic architecture formalism if it stops being tied to one concrete scoping problem

### Misuse patterns

- using context mapping as a substitute for real interface cleanup
- declaring a DDD-style map without changing how reviews or changes are scoped
- treating every folder boundary as a bounded context automatically
- using the technique to justify architecture theater instead of one bounded ambiguity reduction pass
- using context mapping as a durable architecture program when the real need is one immediate scoping decision

### Detection signals

- contributors still confuse neighboring areas after the map is written
- the context names overlap, feel interchangeable, or only repeat folder names
- handoff points are still implicit or undocumented
- reviewers start discussing taxonomy or diagram shape more than the actual scope boundary being protected
- the first question after reading the map is still "what stays out of scope for this change?"

### Mitigations

- collapse weak or ceremonial contexts
- tighten the vocabulary around observable responsibilities
- add or clarify the interface notes between contexts
- re-anchor the map in one concrete scoping decision instead of a broader architecture program
- delete or reduce the map when one sharper scoping note would do more work than a permanent taxonomy surface

## Validation

Verify the technique by confirming that:
- the main ambiguity or vocabulary drift was reduced
- contexts or subsystems were named with clearer responsibility boundaries
- handoff or interface points were made visible
- the result would help a future docs or implementation change stay better scoped
- a future change could use the map to decide what stays out of scope, not just to rename the areas already in scope
- the same bounded contract is already consumable from the committed `aoa-bounded-context-map` skill manifest and example

## Adaptation notes

What can vary across projects:
- whether the units are called bounded contexts, subsystems, domains, or responsibility zones
- how formal the map needs to be
- how vocabulary is recorded
- where the interface notes live

What should stay invariant:
- visible responsibility boundaries
- reduction of semantic confusion
- explicit handoff or interface notes where relevant
- usefulness for future docs or change scoping

## Public sanitization notes

This public version strips project-specific naming and local architecture layout while preserving the bounded-context mapping pattern in a reusable form.

## Example

See `examples/minimal-context-boundary-map.md` for a small example where two neighboring contexts are separated and their handoff is named explicitly.
See `examples/concrete-infra-context-map.md` for a more concrete public-safe infra-repository example where scoping and handoff naming reduce drift without turning into generic architecture taxonomy.

## Checks

See `checks/bounded-context-map-checklist.md` for a minimal review pass covering responsibility clarity, ambiguity reduction, and visible handoff notes.

## Promotion history

- shaped from semantic-boundary needs around `atm10-agent`
- extracted into first public reusable form in `aoa-techniques` on 2026-03-18

## Future evolution

- connect more explicitly to ubiquitous-language guidance
- record stronger examples of handoff notes
