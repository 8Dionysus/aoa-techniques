---
id: AOA-T-0043
name: multi-source-primary-input-provenance
domain: docs
kind: guardrail
status: promoted
origin:
  project: aoa-kag + Tree-of-Sophia bridge contracts
  path: docs/README.md
  note: Distilled from bridge-style source surfaces that need to mark which inputs are primary versus supporting before downstream readers or synthesis depend on them.
owners:
  - 8Dionysus
tags:
  - docs
  - provenance
  - input-ordering
  - bridge-contracts
  - source-priority
summary: Mark primary versus supporting source inputs explicitly when bridging multiple source surfaces so downstream readers and synthesis keep provenance priority visible without turning the bridge into graph semantics or ranking doctrine.
maturity_score: 3
rigor_level: bounded
reversibility: moderate
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-23
export_ready: true
relations:
  - type: complements
    target: AOA-T-0020
  - type: complements
    target: AOA-T-0021
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# multi-source-primary-input-provenance

## Intent

Keep the order of source inputs explicit when one bridge or docs surface combines multiple source materials so reviewers can tell which input is primary and which inputs are supporting before the downstream surface depends on them.

## When to use

- a docs surface combines more than one upstream source and the reader needs to know which one is primary
- multiple source inputs feed one bridge-style artifact, summary, or synthesis step
- provenance priority matters more than equal treatment of all inputs
- the useful contract is source ordering, not graph traversal or ranking
- the reusable object is the primary-versus-supporting input split rather than the bridge architecture itself

## When not to use

- the only problem is note-level provenance handles such as `evidence.kind` and `evidence.path`
- the real need is direct relation hints between bundles
- the surface wants multi-hop graph semantics, ranking, or retrieval policy
- the bridge would become a general architecture program instead of one bounded ordering contract
- the inputs are already obvious enough that no priority label adds review value

## Inputs

- one docs surface or bridge artifact that consumes multiple source inputs
- one explicit rule that names the primary input
- one bounded set of supporting inputs
- one reviewer-visible place where priority can be stated
- one downstream consumer that should preserve that priority

## Outputs

- one primary input named explicitly
- one or more supporting inputs named explicitly
- a readable priority order for downstream readers or synthesis
- lower chance that a multi-source surface quietly flattens all inputs into equal status

## Core procedure

1. Name the source inputs that are feeding the bridge or combined docs surface.
2. Mark exactly one input as primary for the current contract.
3. Mark the remaining inputs as supporting, not equal owners of the combined meaning.
4. Keep the priority order visible in the authored surface, not only in generated metadata.
5. Preserve the ordering when the bridge feeds a reader, summary, or synthesis step.
6. If the next request is for traversal, inference, or ranking, stop and split that into a different technique.

## Contracts

- one source input is primary and the rest are supporting when the bridge needs a priority order
- the priority order stays visible in authored markdown
- the technique stays about input provenance ordering, not note provenance handles
- the technique does not become graph semantics, traversal policy, retrieval ranking, or bridge architecture doctrine
- downstream readers can preserve the priority order without inventing a new graph layer

Relationship to adjacent techniques: unlike `AOA-T-0020`, this technique does not type note kinds or note paths; it marks which source input should be treated as primary when multiple source surfaces are combined. Unlike `AOA-T-0021`, it does not define direct relation hints or one-step edges. Unlike broader bridge contracts, it stops at priority visibility and does not own traversal, synthesis policy, or graph behavior.

## Risks

### Failure modes

- all source inputs get flattened into equal status and the primary signal disappears
- supporting inputs start acting like hidden primary inputs without review
- the technique drifts into graph or ranking language because multiple sources are involved
- readers cannot tell which source should be treated as the primary anchor

### Negative effects

- explicit priority labels can make a combined surface feel less neutral than a plain list
- writers may over-label inputs when only one priority distinction is actually useful
- a clear ordering rule can be misread as ranking doctrine if the boundary is not restated

### Misuse patterns

- using the technique to encode retrieval ranking or trust scoring
- treating note provenance handles as if they already solve multi-source input ordering
- widening the bridge into graph semantics or multi-hop inference
- labeling every input as primary/supporting even when the combined surface does not need that distinction

### Detection signals

- reviewers cannot answer which source is primary after reading the bridge surface
- downstream consumers silently reorder or flatten inputs
- discussions shift toward ranking, traversal, or graph exports instead of source ordering
- the bridge starts depending on relation semantics to explain priority

### Mitigations

- keep one explicit primary input and name supporting inputs clearly
- restate that the contract is ordering, not graph semantics
- route ranking, traversal, and graph exports into separate sibling techniques
- use the technique only when provenance priority is actually meaningful to the combined surface

## Validation

Verify the technique by confirming that:
- the bridge surface names one primary input and at least one supporting input when multiple sources are combined
- the priority order is visible in authored markdown
- downstream readers can preserve the order without inventing graph semantics
- the bundle does not depend on note provenance handles to explain source priority
- the bundle stays distinct from relation lift, retrieval ranking, and broad bridge architecture

See `checks/multi-source-primary-input-provenance-checklist.md`.

## Adaptation notes

What can vary across projects:
- how the bridge surface is written
- how many supporting inputs are present
- where the priority order is shown
- whether synthesis happens manually or through a downstream reader

What should stay invariant:
- one input is primary when the bridge needs a priority order
- supporting inputs remain explicitly secondary to that primary input
- the ordering stays readable in markdown
- the technique does not expand into graph semantics or ranking policy

Project-shaped details that should not be treated as invariant:
- graph traversal layers
- retrieval scoring systems
- note-ID graphs
- provenance manifests for note bodies
- bridge export pipelines

## Public sanitization notes

This public version keeps only the reusable ordering contract: when multiple source surfaces feed one bridge-style docs artifact, the primary input and supporting inputs stay visibly distinct. Graph semantics, retrieval ranking, export pipelines, and note-ID graphs were intentionally left out.

## Example

See `examples/minimal-multi-source-primary-input-provenance.md`.

## Checks

See `checks/multi-source-primary-input-provenance-checklist.md`.

## Promotion history

- distilled from bridge-style docs work in `aoa-kag` and Tree-of-Sophia-adjacent source surfaces
- promoted into `aoa-techniques` on 2026-03-23 as a bounded docs technique for explicit primary-versus-supporting source ordering

## Future evolution

- add a second live context if another public bridge surface uses the same primary-versus-supporting ordering rule
- keep `AOA-T-0020` as the note-provenance sibling rather than widening this bundle into note metadata
- keep `AOA-T-0021` as the direct-edge sibling rather than widening this bundle into relation or graph semantics
