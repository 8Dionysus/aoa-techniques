---
id: AOA-T-0016
name: bounded-context-map
domain: docs
status: promoted
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
summary: Reduce semantic drift by naming bounded contexts, separating responsibilities, and making handoff interfaces visible.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-18
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
---

# bounded-context-map

## Intent

Reduce semantic confusion and misplaced changes by naming bounded contexts, clarifying their responsibilities, and making the interfaces between them visible.

## When to use

- repositories with several domains, services, or subsystems that can blur together
- situations where naming is overloaded or ambiguous
- architecture discussions that need a compact context boundary map before coding safely
- agent-assisted work where semantic confusion would widen the context unnecessarily

## When not to use

- tiny repositories with no meaningful subsystem ambiguity
- changes that are fully local and already clearly bounded
- situations where drawing context labels would only add ceremony without reducing confusion

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
- the result should help a future reviewer scope work more safely

## Risks

### Failure modes

- too many contexts are invented for a small problem
- the map renames concepts without reducing ambiguity
- interfaces remain muddy even after the map is drawn

### Negative effects

- over-structuring can slow small projects if no real confusion exists
- premature context formalization can freeze evolving vocabulary too early

### Misuse patterns

- using context mapping as a substitute for real interface cleanup
- declaring a DDD-style map without changing how reviews or changes are scoped
- treating every folder boundary as a bounded context automatically

### Detection signals

- contributors still confuse neighboring areas after the map is written
- the context names overlap or feel interchangeable
- handoff points are still implicit or undocumented

### Mitigations

- collapse weak or ceremonial contexts
- tighten the vocabulary around observable responsibilities
- add or clarify the interface notes between contexts

## Validation

Verify the technique by confirming that:
- the main ambiguity or vocabulary drift was reduced
- contexts or subsystems were named with clearer responsibility boundaries
- handoff or interface points were made visible
- the result would help a future change stay better scoped

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
- usefulness for future change scoping

## Public sanitization notes

This public version strips project-specific naming and local architecture layout while preserving the bounded-context mapping pattern in a reusable form.

## Example

See `examples/minimal-context-boundary-map.md` for a small example where two neighboring contexts are separated and their handoff is named explicitly.

## Checks

See `checks/bounded-context-map-checklist.md` for a minimal review pass covering responsibility clarity, ambiguity reduction, and visible handoff notes.

## Promotion history

- shaped from semantic-boundary needs around `atm10-agent`
- extracted into first public reusable form in `aoa-techniques` on 2026-03-18

## Future evolution

- add a second-context example from an infra-oriented repository
- connect more explicitly to ubiquitous-language guidance
- record stronger examples of handoff notes
