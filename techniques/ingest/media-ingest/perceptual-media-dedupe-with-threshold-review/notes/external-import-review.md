# External Import Review

## Technique
- id: AOA-T-0072
- name: perceptual-media-dedupe-with-threshold-review

## Verdict
- pass
- review date: 2026-03-28

## Evidence summary

- the bundle includes the expected bounded external-import package: `TECHNIQUE.md`, `notes/external-origin.md`, `notes/second-context-adaptation.md`, one public-safe checklist, and one public-safe example
- the technique document states one narrow contract: near-duplicate media are grouped through perceptual similarity and borderline matches are routed into review instead of silent deletion
- the provenance note records the donor family plus explicit exclusions around semantic taxonomy, delete policy, ranking, and donor-specific runtime detail
- the second-context note keeps the same duplicate-grouping seam readable as a documentation-first adaptation inside `aoa-techniques`

## Boundedness check

- result: pass
- the invariant core stays narrow: perceptual similarity, explicit thresholds, duplicate groups, and visible uncertain matches
- excluded donor features remain explicit and out of scope: delete prompts, preserve defaults, ANN backend detail, semantic taxonomy, and quality ranking
- the example and checklist reinforce reviewable grouping without widening the bundle into cleanup governance or media-classification doctrine

## Provenance readability

- result: pass
- a reviewer can trace the path from donor dedupe READMEs to the public technique through the external-origin note, bounded exclusions, and documentation-first adaptation without hidden internal context
- the bundle reads as one duplicate-grouping contract rather than a disguised cleanup CLI or media-management product guide
- the import path is public-safe and reviewable at the current repo scale

## Import-path assessment

- result: pass
- this was a successful bounded external import, and the later Pack 29 review confirmed the same seam in a second public source outside the donor dedupe family
- `qarmin/czkawka` reinforces the import path by exposing thresholded perceptual image grouping, visible grouped results, similarity labels, JSON or text output, and deletion as a separate default-off option

## Remaining gaps

- no import-path blocker remains for canonical status
- future stronger contexts should still show near-duplicate media grouped through explicit thresholds or bands and reviewable output before later cleanup, archive, semantic classification, or ranking actions

## Recommendation

- keep this note as the original import review
- use `notes/canonical-readiness.md` and `notes/adverse-effects-review.md` as the current canonical promotion and boundary review surfaces
