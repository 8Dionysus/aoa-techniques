---
id: AOA-T-0030
name: fragmented-agent-context
domain: docs
kind: composition
status: promoted
origin:
  project: agents-md
  path: README.md
  note: Adapted from the open-source agents-md project, which keeps agent context in smaller markdown fragments before deterministic assembly into one generated artifact.
owners:
  - 8Dionysus
tags:
  - docs
  - agent-context
  - fragments
  - modular-authoring
  - source-partitioning
summary: Keep agent context in bounded fragments before deterministic assembly so modular authoring stays reviewable without collapsing into the final generated artifact.
maturity_score: 3
rigor_level: bounded
reversibility: moderate
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-21
export_ready: true
relations:
  - type: complements
    target: AOA-T-0012
evidence:
  - kind: external_origin
    path: notes/external-origin.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: external_review
    path: notes/external-import-review.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# fragmented-agent-context

## Intent

Keep agent context authored in smaller bounded fragments so source partitioning, local ownership, and modular review stay clear before any later deterministic assembly step exists.

## When to use

- repositories where one large hand-maintained agent context file has become hard to review or extend
- projects that want context ownership to stay close to local subtrees, topics, or responsibilities
- workflows where modular authoring matters even before a generated aggregate artifact is introduced
- cases where the main question is source partitioning rather than final output assembly

## When not to use

- repositories that only need one short context file and do not benefit from fragment boundaries
- workflows where the real reusable object is deterministic assembly into one generated artifact
- systems that mainly need CI reporting, token-drift visibility, or validation outputs rather than fragment-first authoring
- cases where context injection behavior or runtime loading is the real center of gravity

## Inputs

- one set of context fragments with bounded local scope
- one naming or placement rule that keeps fragment ownership legible
- one review path that treats fragments as the editable source of truth
- one optional downstream assembly step that remains separate from this technique

## Outputs

- modular context sources that are easier to review and evolve
- clearer local ownership over context content
- lower pressure to keep one large context document hand-maintained
- one cleaner source layer for any later deterministic assembly or CI reporting technique

## Core procedure

1. Break the agent context into smaller fragments with bounded topical or local scope.
2. Place each fragment near the part of the repository or responsibility it describes.
3. Keep one explicit rule for how fragment names or locations signal their intended scope.
4. Review and edit the fragments directly instead of treating a later aggregate artifact as the canonical source.
5. Keep fragment boundaries stable enough that a reviewer can explain why each fragment exists and where it belongs.
6. Add deterministic assembly or CI reporting only as separate downstream techniques when the repository actually needs them.

## Contracts

- fragments remain the editable source of truth for the partitioned context layer
- each fragment carries bounded scope rather than becoming a generic dump of nearby guidance
- fragment placement and naming make ownership legible to reviewers
- the technique stays about modular source partitioning before assembly
- deterministic composition into one artifact remains outside this contract
- CI reporting, token-drift reporting, and runtime injection behavior remain outside this contract

Relationship to adjacent techniques: unlike `AOA-T-0012`, this technique stops at fragment-first authoring and does not own deterministic composition into one generated artifact. It complements `AOA-T-0012` by making the fragment layer itself reviewable and bounded before assembly begins.

## Risks

### Failure modes

- fragment boundaries become arbitrary, so the context is split across files without clearer ownership
- contributors start editing a generated aggregate instead of the fragments that are supposed to stay canonical
- local fragments drift into duplicate or conflicting guidance because their scope is no longer legible

### Negative effects

- fragment-first authoring can add route friction if contributors must open too many files to understand one context area
- local placement can make context feel tidy while actually hiding duplicate guidance across neighboring fragments
- a repository can over-fragment the context layer and create editorial overhead without gaining clearer ownership

### Misuse patterns

- widening the technique into deterministic composition instead of keeping it at the source-partitioning layer
- treating fragment discovery rules or file globs as the main reusable object
- using fragment-first authoring as a cover for runtime injection, hidden loading, or validation behavior

### Detection signals

- reviewers cannot explain why a fragment belongs where it does or what scope it owns
- a generated aggregate becomes the de facto file contributors edit first
- several fragments repeat the same guidance with only minor wording changes
- the repository debates assembly behavior more than the fragment boundaries themselves

### Mitigations

- narrow each fragment to one clear local scope and reject generic catch-all fragments
- route edits back to canonical fragments rather than patching a generated aggregate
- merge or remove fragments when boundaries no longer help reviewers understand ownership
- split deterministic assembly, CI reporting, or runtime behavior into separate sibling techniques when they become the real reusable object

## Validation

Verify the technique by confirming that:
- the fragment set is the editable source of truth
- each fragment has bounded scope that a reviewer can explain
- fragment placement or naming makes local ownership legible
- the repository can add or remove one fragment without making the rest of the layer unreadable
- deterministic assembly, CI reporting, and runtime injection remain outside this bounded contract

See `checks/fragmented-agent-context-checklist.md`.

## Adaptation notes

What can vary across projects:
- the folder layout used for fragments
- the naming convention for fragment files
- how narrowly each fragment is scoped
- whether a later assembly step exists at all

What should stay invariant:
- context is authored in bounded fragments before any aggregate output
- fragments stay canonical and reviewable
- fragment scope and placement remain legible
- this technique remains about source partitioning rather than final generated output

Project-shaped details that should not be treated as invariant:
- exact file suffixes or fragment-glob patterns
- deterministic assembly behavior
- CI reporting details
- runtime injection rules or hidden loading mechanics

## Public sanitization notes

This import narrows the donor repository to one bounded pattern: fragment-first authoring for agent context. Deterministic composition, JSON reporting, token-estimate reporting, migration helpers, and runtime injection behavior were intentionally left out of the public technique contract.

## Example

See `examples/minimal-fragmented-agent-context.md` and `examples/concrete-subtree-fragmented-context.md`.

## Checks

See `checks/fragmented-agent-context-checklist.md`.

## Promotion history

- adapted from open-source `agents-md`
- promoted into `aoa-techniques` on 2026-03-21 as a bounded external-import technique for fragment-first agent-context authoring

## Future evolution

- keep `AOA-T-0012` as the deterministic-assembly sibling rather than widening this bundle into the generated-artifact layer
- split out a dedicated context-injection sibling only if a reusable injection contract becomes cleanly separable from authoring
- add a stronger second live context if another public repository adopts the same fragment-first context-authoring contract
