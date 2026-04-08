---
id: AOA-T-0072
name: perceptual-media-dedupe-with-threshold-review
domain: agent-workflows
kind: ingest
status: promoted
origin:
  project: imagededup + imgdupes
  path: README.md
  note: Adapted from open-source image deduplication tools that expose perceptual similarity, candidate duplicate groups, and threshold tuning, while this bundle keeps only the bounded reviewable grouping contract.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - media
  - dedupe
  - perceptual-similarity
  - review
summary: Group near-duplicate media through perceptual similarity and thresholded review buckets so cleanup stays reviewable instead of collapsing into silent deletion or one-threshold dogma.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-28
export_ready: true
relations: []
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

# perceptual-media-dedupe-with-threshold-review

## Intent

Make screenshot, meme, or photo deduplication reviewable by grouping near-duplicate media through perceptual similarity while keeping uncertain matches visible and file-action policy outside the technique.

## When to use

- an image set contains exact duplicates, crops, edits, or recompressions that still need duplicate review
- the reusable seam is duplicate grouping and uncertainty routing rather than semantic classification
- thresholds may vary by media family and should stay explicit
- a human or later policy layer will decide preserve, delete, archive, or merge actions
- the workflow needs duplicate groups, not one opaque cleanup command

## When not to use

- exact hashes alone are enough and near-duplicate handling is unnecessary
- the real reusable object is semantic bucketing rather than duplicate grouping
- the workflow assumes auto-delete with no review seam
- ranking, quality scoring, or representative selection doctrine is the real center of gravity

## Inputs

- one bounded media set
- one perceptual similarity method or equivalent near-duplicate handle
- explicit thresholds or threshold bands
- optional grouping strategy or representative-selection rule for review display

## Outputs

- one set of high-confidence duplicate groups
- one set of uncertain groups or candidate pairs
- one review bucket for borderline matches
- optional representative references for group display, without making that representative the policy winner

## Core procedure

1. Compute perceptual similarity handles for the bounded media set.
2. Form candidate duplicate pairs or groups from those handles.
3. Separate clearly similar groups from borderline matches through explicit thresholds or bands.
4. Emit uncertain groups into a review bucket instead of flattening them into the same action path as high-confidence duplicates.
5. Preserve enough group-level evidence that reviewers can see why images were paired or grouped.
6. Keep deletion, archival, ranking, and semantic labeling outside the invariant contract.
7. Split out a sibling technique if the real reusable object becomes semantic taxonomy, automatic cleanup policy, or cross-media quality scoring.

## Contracts

- the technique groups and flags near-duplicates; it does not own file deletion policy
- thresholds stay explicit and tunable
- uncertain matches remain visible instead of being silently resolved
- grouping remains reviewable and explainable
- the technique stays smaller than semantic media taxonomy, cleanup automation, or quality-ranking doctrine
- downstream systems receive duplicate groups and review signals rather than donor CLI behavior or storage policy

Relationship to adjacent techniques: unlike `semantic-media-bucketing-with-vision-plus-ocr`, this bundle does not classify media into receipt, meme, screenshot, or other semantic buckets; it only groups likely duplicates. Unlike [AOA-T-0052](../review-findings-compaction/TECHNIQUE.md), it deduplicates media artifacts rather than review findings. It also stays smaller than any delete-or-archive policy because it stops at grouping plus review.

## Risks

### Failure modes

- edited memes collapse into the wrong groups
- cropped screenshots become false duplicates
- threshold settings drift across media families and over-group meaningful variants
- representative images hide why a group was formed

### Negative effects

- aggressive cleanup can remove variants users expected to keep
- one threshold can become false doctrine across unrelated media families
- duplicate groups can look authoritative even when similarity is borderline

### Misuse patterns

- auto-deleting all grouped images
- treating duplicate groups as semantic labels
- widening the technique into ranking, quality scoring, or cleanup governance

### Detection signals

- high duplicate counts with obvious false matches
- users report loss of meaningful variants after cleanup
- reviewers cannot tell why a borderline match was grouped

### Mitigations

- keep a review bucket for uncertain matches
- separate action policy from grouping
- calibrate thresholds by media family
- preserve enough evidence to explain group membership

## Validation

Verify the technique by confirming that:
- the corpus includes exact duplicates, crops, and edited variants
- high-confidence groups and uncertain groups are visibly separated
- thresholds can be adjusted without rewriting the contract
- grouping output stays reviewable without forcing deletion or archive actions
- semantic labeling and cleanup policy remain outside the technique

See `checks/perceptual-media-dedupe-with-threshold-review-checklist.md`.

## Adaptation notes

What can vary across projects:
- the perceptual hash or similarity method
- threshold bands by media family
- group or pair presentation
- representative-selection hints for review UIs
- storage layout and later action policy

What should stay invariant:
- duplicate grouping remains separate from file actions
- thresholds remain explicit
- uncertain matches remain visible
- the output is a reviewable grouping surface rather than a cleanup verdict

Project-shaped details that should not be treated as invariant:
- donor CLI flags
- delete or preserve defaults
- one-threshold-fits-all claims
- ranking or quality-scoring doctrine

## Public sanitization notes

This public bundle keeps only the reusable duplicate-grouping seam: perceptual similarity forms candidate groups, uncertainty stays visible, and later file actions remain outside the technique. Donor CLI workflow, delete defaults, approximate-nearest-neighbor implementation detail, and quality-ranking posture were intentionally removed or generalized.

## Example

See `examples/minimal-perceptual-media-dedupe-with-threshold-review.md`.

## Checks

See `checks/perceptual-media-dedupe-with-threshold-review-checklist.md`.

## Promotion history

- adapted from open-source `imagededup` and `imgdupes`
- landed from `personal-ingest-wave-2`
- promoted into `aoa-techniques` on 2026-03-28 as a bounded external-import technique for reviewable near-duplicate media grouping

## Future evolution

- keep semantic bucketing separate unless a narrower bridge seam proves reusable
- split out duplicate manifests or deletion policy only if those contracts survive independently
- add a stronger second live context if another public workflow keeps perceptual dedupe explicit before later cleanup actions
