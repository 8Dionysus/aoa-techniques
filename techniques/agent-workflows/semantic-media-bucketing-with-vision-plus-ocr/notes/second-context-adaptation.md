# Second Context Adaptation

## Technique
- id: AOA-T-0073
- name: semantic-media-bucketing-with-vision-plus-ocr

## Target project
- name: aoa-techniques
- environment: public technique repository with authored bundle contracts, generated routing surfaces, and validator-backed markdown discipline
- runtime: documentation-first corpus that records the bounded media-bucketing pattern rather than shipping donor models, prompts, or OCR services

## What changed

- donor multimodal systems were reduced to one portable bucketing-and-review contract rather than one broad image-understanding or assistant workflow
- moderation policy, identity inference, and serving detail were removed from the reusable public bundle
- OCR-stage ownership was kept out so the adaptation only uses OCR as one optional side-channel during classification
- the bundle was reduced to one technique doc, one checklist, one example, and four bounded evidence notes

## What stayed invariant

- visual semantics remain the main classification signal
- OCR can sharpen text-heavy items without becoming hidden truth
- taxonomy remains explicit and bounded
- low-confidence or conflicting items remain visible for review

## Risks introduced by adaptation

- the technique can collapse into taxonomy sprawl if later users widen the bucket set without preserving reviewability
- teams may over-associate the technique with one donor model or one OCR stack if the bounded contract is not kept generic
- OCR-heavy items can look more certain than they are if the side-channel is not clearly labeled

## Evidence

- CLIP's README presents zero-shot prediction over explicit image-label text pairings, which supports bounded bucket scoring without requiring fixed task-specific training
- PaddleOCR's README presents OCR as a reusable text-extraction surface for text-bearing images
- together they show why coarse media bucketing can remain explicit and reviewable before later action policy is decided

## Result

- works as a documentation-first second context and preserves the bounded core without carrying over donor model-serving detail, moderation claims, or OCR-runtime packaging
