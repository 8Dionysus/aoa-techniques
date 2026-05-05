---
id: AOA-T-0021
name: bounded-relation-lift-for-kag
domain: docs
kind: lift
status: canonical
origin:
  project: aoa-techniques
  path: docs/SELECTION_PATTERNS.md
  note: Extracted from the current direct-relation consumers and relation-lift guidance to keep typed edges useful for navigation without widening them into graph semantics.
owners:
  - 8Dionysus
tags:
  - docs
  - kag
  - relations
  - edges
  - navigation
summary: Lift small typed direct relations into bounded edge hints for derived consumers without turning them into graph semantics.
maturity_score: 5
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: cross_context
public_safety_reviewed_at: 2026-03-20
export_ready: true
relations:
  - type: requires
    target: AOA-T-0019
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

# bounded-relation-lift-for-kag

## Intent

Use a small typed set of direct bundle relations as bounded edge hints for generated consumers without pretending that those edges already carry rationale, weighting, or multi-hop graph truth.

## When to use

- corpora that already have explicit direct relations between bundles
- navigation or retrieval surfaces that need one-step adjacency hints
- KAG-oriented work that wants future edge inputs without jumping straight to graph behavior
- review paths where relation vocabulary should stay small and human-readable
- generated readers that only need direct typed hints, not explanation layers or inferred traversal

## When not to use

- systems that need relation rationale, weighted edges, or multi-hop traversal policy right now
- repositories where direct relations are still too noisy or unstable to trust as bounded adjacency hints
- cases where the real problem is semantic ambiguity between techniques, which should be handled by review rather than by more edges
- workflows that would use current relations as transitive truth or graph-engine inputs by default
- consumers that want a rationale layer, graph semantics, or multi-hop inference from the relation field itself

## Inputs

- bounded typed `relations` in frontmatter
- direct target technique IDs
- one or more current relation consumers such as catalog or selection surfaces
- explicit agreement that relation explanation, if needed, still lives in markdown and review docs rather than in the relation field

## Outputs

- bounded direct-edge hints
- derived consumers that can show nearby techniques
- reusable small relation vocabulary
- future-ready edge surface that remains human-reviewable
- no implied rationale, weighting, or transitive graph behavior

## Core procedure

1. Keep the relation vocabulary intentionally small and direct.
2. Record only immediate adjacency that helps navigation or bounded review.
3. Project those edges into derived consumers such as catalogs or selection surfaces.
4. Use relations for one-step inspection hints rather than multi-hop inference or graph traversal.
5. Keep the explanation for why an edge exists in markdown bundles or review docs, not inside the relation field.
6. Refuse to widen the edge layer unless current direct-edge use has clearly stopped being enough.

## Contracts

- relations stay direct and typed
- edge meaning is bounded to one-step adjacency hints
- relation rationale remains outside frontmatter and outside the relation field
- derived consumers remain navigation aids rather than graph engines
- the technique does not require new relation types, weighting, or a new `kag` domain

## Risks

### Failure modes

- relations multiply until the signal-to-noise ratio drops and adjacency hints stop helping
- consumers infer transitive truth or ranking from edges that were only meant as direct hints
- teams widen relation vocabulary to patch unclear technique boundaries instead of fixing the underlying docs

### Negative effects

- even a bounded edge layer can make the repository feel more graph-ready than it really is
- relation consumers can pull attention away from reading the bundle itself
- small relation vocabularies can over-simplify why two techniques are near each other

### Misuse patterns

- treating `relations` as a substitute for semantic review
- adding rationale, scoring, or traversal rules because one navigation surface is already helpful
- using direct edges as a reason to open graph/export programs before current use is proven

### Detection signals

- contributors debate relation semantics more than they improve the underlying bundle boundaries
- one-step edges are no longer enough and consumers keep asking for inferred hops or ranking
- relation explanations are missing from markdown, but people still trust the edge layer to answer "why"
- new relation types appear mainly to patch wording drift or bundle overlap

### Mitigations

- keep the relation set small and review-shaped
- move "why does this edge exist?" questions back to markdown bundles and semantic review docs
- remove weak or noisy edges before adding new types
- stop at bounded adjacency when the next request is really for a separate graph or review layer

## Validation

Verify the technique by confirming that:
- each relation points to a real direct target
- current consumers use the edges for one-step navigation rather than inference
- the relation vocabulary remains small and bounded
- reviewers can still find edge rationale in markdown or review surfaces
- no new graph behavior was needed to make the relation layer useful

See `checks/relation-lift-checklist.md` and `examples/direct-relation-to-selection-hint.md`.
For repo-grounded origin evidence, see `notes/origin-evidence.md`.

## Adaptation notes

What can vary across projects:
- the exact set of direct relation consumers
- how adjacency is displayed in generated surfaces
- which small relation vocabulary best fits the corpus
- how often relations are reviewed for noise or drift

What should stay invariant:
- edges remain direct
- relation types remain bounded
- rationale stays in markdown or review docs
- the edge layer does not become graph semantics by accident
- no multi-hop inference is introduced by the derived consumer
- the relation field never becomes a rationale store

This technique sits downstream from a bounded metadata spine. If the next need is graph traversal, relation weighting, exports, or a rationale layer, that is a later platform wave, not this technique.

## Public sanitization notes

This public version keeps the direct-edge contract and removes any implication that the repository already has a graph platform. The useful pattern is bounded adjacency, not graph theater.

## Example

See `examples/direct-relation-to-selection-hint.md` for a small relation block and the derived adjacency shown in a selection surface.

## Checks

See `checks/relation-lift-checklist.md`.

## Promotion history

- shaped inside `aoa-techniques` while direct relation consumers became useful through catalog and selection surfaces
- extracted into first public reusable form on 2026-03-19 as part of the initial KAG/source-lift family wave

## Future evolution

- strengthen second-context evidence once another markdown-first corpus uses the same bounded relation layer
- add clearer relation-review guidance before widening the vocabulary
- keep relation rationale, weighting, graph semantics, and multi-hop behavior deferred
