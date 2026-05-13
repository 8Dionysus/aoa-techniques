# Adverse Effects Review

## Technique
- id: AOA-T-0073
- name: semantic-media-bucketing-with-vision-plus-ocr

## Review focus
- promotion from `promoted` to `canonical` after exact-fit public reinforcement from `end1989/ai-image-classification`
- confirm that the bundle remains one bounded semantic media bucketing and review-threshold contract, not OCR extraction ownership, duplicate grouping, moderation policy, identity inference, face detection, file deletion, archive policy, auto-routing doctrine, UI workflow, database schema, or full media-management product behavior

## Failure modes
- OCR-heavy screenshots or receipts overpower the visual classification signal and make text artifacts look more certain than they are
- vague taxonomy labels cause screenshots, memes, receipts, documents, and social-media captures to drift across buckets
- one confidence threshold tuned for a small media set is reused as a universal review gate
- low-confidence or conflicting items are forced into a final bucket because later storage or routing wants a single label
- text extraction misses small, rotated, low-resolution, or multilingual text and weakens the bucket assignment without making uncertainty visible

## Negative effects
- bounded media bucketing can create review overhead when simple source folders or metadata would have been enough
- confidence scores can look like final truth even though they only support a reviewable classification surface
- OCR side text can leak into downstream policy if consumers treat it as proof rather than a classification aid
- product examples with auto-organization, NSFW detection, or face/person surfaces can tempt contributors to import unrelated behavior into the smaller technique
- broad label sets can become a hidden media ontology instead of one task-specific taxonomy

## Misuse patterns
- using bucket labels as final truth for deletion, archive, migration, moderation, identity inference, or other destructive actions
- treating OCR extraction as the center of the technique instead of a side-channel that may sharpen text-bearing images
- replacing a bounded taxonomy with open-ended visual question answering or multimodal assistant behavior
- using this bundle as a substitute for [perceptual-media-dedupe-with-threshold-review](../../perceptual-media-dedupe-with-threshold-review/TECHNIQUE.md) when the actual need is near-duplicate grouping
- copying donor app thresholds, routes, UI behavior, database schema, NSFW labels, face-detection features, or file-manager actions into the invariant technique

## Detection signals
- examples center cleanup, move actions, moderation, face/person grouping, or storage organization more than bounded bucket labels and review thresholds
- output no longer includes a confidence signal, review bucket, or equivalent uncertainty handle
- OCR text silently changes labels without a visible note that text influenced the assignment
- taxonomy additions happen without a corresponding review of ambiguous or conflicting media examples
- downstream systems consume labels without preserving the review status or threshold context

## Mitigations
- keep the taxonomy small, explicit, and task-shaped
- preserve a confidence signal, review band, or equivalent uncertainty handle with each bucket assignment
- record when OCR influenced a label and keep OCR extraction ownership separate from media bucketing
- route low-confidence, conflicting, or OCR-dominant cases into review rather than forcing a final class
- keep duplicate grouping, moderation, identity inference, deletion, archiving, auto-routing, UI, and media-management product behavior outside the technique contract

## Recommendation
- safe to promote as a canonical agent-workflow ingest technique when bounded taxonomy, visual semantic scoring, OCR side-channel handling, confidence gates, and reviewability remain visible before later policy or action layers begin
- keep future revisions narrow: do not absorb OCR pipeline ownership, duplicate grouping, moderation or NSFW policy, face/person identification, file deletion, archive/move policy, route governance, UI workflows, database schemas, local model-serving detail, or full media-management product behavior into this bundle
