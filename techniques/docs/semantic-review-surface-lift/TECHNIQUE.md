---
id: AOA-T-0048
name: semantic-review-surface-lift
domain: docs
status: promoted
origin:
  project: aoa-techniques
  path: docs/SEMANTIC_REVIEW_GUIDE.md
  note: Extracted from the authored semantic-review guide, the current semantic-review manifest, and review-backed selection surfaces to keep cluster lookup derived from human review docs without turning it into scoring or status automation.
owners:
  - 8Dionysus
tags:
  - docs
  - kag
  - review
  - semantic-review
  - manifests
summary: Lift authored semantic-review docs into derived boundary-review knowledge without creating automatic semantic verdicts.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-23
export_ready: true
relations:
  - type: complements
    target: AOA-T-0018
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
---

# semantic-review-surface-lift

## Intent

Lift authored `*_SEMANTIC_REVIEW.md` docs into one derived boundary-review surface so readers and tooling can find the current cluster map, seam review, findings, and next-step summary without turning semantic review into a scoring system, a status driver, or a graph engine.

Within the current KAG/source-lift family, this technique is the cluster-level counterpart to section lift and metadata lift: it keeps the review meaning in authored markdown while making the review surface easier to navigate.

## When to use

- repositories that already have authored semantic-review docs and review-backed working sets
- review flows where the question is whether nearby techniques still read as distinct
- lookup surfaces that need one bounded place to inspect a cluster map, seam review, and next-step summary
- KAG-oriented work that needs review-cluster lookup before any broader automation exists
- cases where the review doc itself should remain the place where semantic meaning is argued

## When not to use

- repos without authored semantic-review docs
- workflows that want semantic scoring, automated verdicts, or status transitions
- cases where the real problem is bundle-local caution, not cluster-level review
- situations where the next need is relation cleanup or graph behavior rather than bounded review lookup
- workflows that would treat the derived manifest as a replacement for the authored review doc

## Inputs

- one or more authored `*_SEMANTIC_REVIEW.md` docs
- a review-backed working set or cluster definition
- a derived manifest that can expose review path, reviewed techniques, cluster title, and next-step summary
- explicit agreement that review meaning still lives in authored markdown

## Outputs

- bounded cluster-level review lookup
- review path and cluster map entries that remain traceable to authored review docs
- preserved human-authored review meaning
- a derived surface that can point readers back to the review doc when they need the full argument
- no automatic semantic verdicts, ranking, or status changes

## Core procedure

1. Keep the authored semantic-review doc as the only source of review meaning.
2. Identify the cluster scope that is actually being reviewed.
3. Lift the cluster map, seam review, findings, and next-step summary into a derived manifest or reader surface.
4. Preserve the review order and the review doc's own wording instead of rewriting it into a new policy language.
5. Rebuild the derived output whenever the authored review doc changes.
6. Route disagreements about meaning, boundaries, or watch seams back to the authored review doc.
7. Stop when the next request is really for scoring, automation, or a new status engine.

## Contracts

- authored semantic-review docs remain the source of review meaning
- the derived surface stays cluster-bounded and review-shaped
- the manifest can help navigation, but it does not become the review authority
- the technique does not require scores, verdict IDs, or automatic status changes
- review meaning stays distinct from bundle-local notes and from shadow-review surfaces
- the technique does not collapse into relation cleanup, semantic adjudication, or graph semantics

## Risks

### Failure modes

- clusters expand until the derived surface stops reflecting one real bounded seam
- maintainers edit the derived manifest instead of the review doc and break source-of-truth boundaries
- the review surface starts acting like a policy engine because the manifest is easier to read than the authored argument

### Negative effects

- review lookup can create false confidence that the cluster has already been fully settled
- a clean derived surface can hide how much judgment still lives in the authored review text
- review aggregation can feel more complete while making it easier to skip the underlying review doc

### Misuse patterns

- treating the semantic-review surface as a scoring engine or ranking layer
- using the manifest to drive status changes instead of to support bounded review lookup
- widening a cluster just because another nearby technique is available
- folding shadow-caution questions into semantic review or using semantic review to replace bundle-local notes

### Detection signals

- people ask for scores, promotion logic, or automated decisions from the review surface
- the manifest has to be edited directly to fix review meaning
- a cluster no longer has a single clear watch seam and starts reading like a catch-all review bucket
- consumers stop opening the authored review doc and rely only on the derived lookup

### Mitigations

- keep clusters narrow and seam-shaped
- route meaning changes back to the authored review doc and regenerate outputs afterward
- reject requests that turn review lookup into automated verdict logic
- open a new cluster only when the current seam is truly ambiguous and still bounded

## Validation

Verify the technique by confirming that:
- the authored semantic-review doc exists and stays readable as the source of review meaning
- the derived surface can be regenerated from authored markdown
- the review lookup preserves the cluster map, seam review, findings, and next-step summary
- consumers can route from the derived surface back to the authored review doc
- the technique remains review-shaped and does not require scoring, status automation, or graph semantics
- semantic-review lookup stays distinct from shadow-review lookup and from bundle-local adverse-effects notes

See `checks/semantic-review-surface-lift-checklist.md` and `examples/minimal-semantic-review-surface-lift.md`.
For repo-grounded origin evidence, see `notes/origin-evidence.md`.

## Adaptation notes

What can vary across projects:
- the cluster size and review doc naming pattern
- the derived manifest filename or reader companion
- how many sections are lifted from the authored review doc
- whether the downstream consumer is a navigation surface or a bounded review aid

What should stay invariant:
- authored review docs remain authoritative
- derived review lookup stays bounded and cluster-shaped
- review meaning stays in markdown
- the technique does not become a policy or scoring system
- consumers can still route back to the review doc

This technique sits beside other KAG/source-lift surfaces, but it does not become a new `kag` domain or a semantic automation layer. It is a bounded review lift, not a machine judge.

## Public sanitization notes

This public version keeps the reusable review-lift contract and removes any implication that semantic review already drives automatic decisions. The point is bounded lookup over authored review docs, not a replacement for review judgment.

## Example

See `examples/minimal-semantic-review-surface-lift.md` for a small semantic-review doc excerpt and the corresponding derived lookup excerpt.

## Checks

See `checks/semantic-review-surface-lift-checklist.md`.

## Promotion history

- shaped inside `aoa-techniques` while authored semantic-review docs and review-backed working sets became useful as a bounded lookup surface
- extracted into first public reusable form on 2026-03-23 as part of the docs review-surface lift wave

## Future evolution

- strengthen second-context evidence once another markdown-first corpus reuses the same review-lift split
- clarify when a review cluster should be split rather than expanded
- keep scoring, status automation, and relation-cleanup semantics deferred unless the current bounded lookup stops being enough
