# Adverse Effects Review

## Technique
- id: AOA-T-0072
- name: perceptual-media-dedupe-with-threshold-review

## Review focus
- promotion from `promoted` to `canonical` after exact-fit public reinforcement from `qarmin/czkawka`
- confirm that the bundle remains one thresholded perceptual grouping and review-output contract, not cleanup automation, archive policy, semantic media taxonomy, quality ranking, GUI selection workflow, cache design, hardlink strategy, or full media-management product

## Failure modes
- perceptual thresholds group visually similar but meaningfully different screenshots, memes, documents, or edited photos
- one threshold tuned for one media family is reused across unrelated media without recalibration
- borderline candidates are flattened into high-confidence groups and later treated as cleanup-safe
- representative images hide why a group was formed or which member carries the actual evidence
- group output drops similarity evidence, making reviewers unable to inspect why two files were paired

## Negative effects
- reviewable grouping adds friction when exact hashes would have been enough
- preserving candidate groups and uncertainty can increase storage and review workload for large media sets
- users may over-trust a grouped result as a delete verdict even when the technique only produces candidates
- threshold language can become local doctrine if teams stop recording why a value fits one media family
- strong public dedupe tools can tempt contributors to import delete methods, hardlinks, cache behavior, GUI workflows, or media-management product assumptions into the smaller technique

## Misuse patterns
- auto-deleting all grouped images because they appear in one duplicate group
- using this bundle as a substitute for [semantic-media-bucketing-with-vision-plus-ocr](../../semantic-media-bucketing-with-vision-plus-ocr/TECHNIQUE.md) when the actual need is media classification
- treating perceptual duplicates as evidence of semantic equivalence, authorship, provenance, or file quality
- widening the bundle into archive policy, representative selection, quality scoring, ranking, hardlinking, or cleanup governance
- copying donor CLI flags, GUI flows, cache formats, or delete method names into the invariant technique

## Detection signals
- review output cannot show the threshold, band, difference, score, or equivalent evidence behind a pair or group
- candidate groups immediately trigger delete, archive, hardlink, or merge actions without a separate policy layer
- examples center cleanup wins, storage savings, UI affordances, or product workflows more than thresholded grouping and visible uncertainty
- false positives cluster around crops, memes, screenshots with shared layouts, watermarked images, or minor text edits
- reviewers cannot tell which matches are high-confidence and which are borderline

## Mitigations
- keep deletion, archiving, hardlinking, ranking, and representative selection outside the technique contract
- preserve a threshold, band, difference, similarity label, or equivalent review signal with each group or candidate pair
- calibrate thresholds per media family and record when a stricter or looser value is being used
- keep borderline matches visible as review candidates rather than collapsing them into high-confidence groups
- test the smallest handoff by confirming that a downstream reviewer can inspect why files were grouped without running donor-specific product code

## Recommendation
- safe to promote as a canonical agent-workflow ingest technique when perceptual duplicate grouping remains bounded, thresholds stay explicit, group evidence remains reviewable, and later file actions are owned by a separate policy or workflow
- keep future revisions narrow: do not absorb semantic media bucketing, deletion or archive policy, quality ranking, representative-selection doctrine, hardlink strategy, cache layout, GUI review workflows, storage cleanup, or full media-management product behavior into this bundle
