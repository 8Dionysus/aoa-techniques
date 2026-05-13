# Second Context Adaptation

## Technique
- id: AOA-T-0073
- name: semantic-media-bucketing-with-vision-plus-ocr

## Target project
- name: aoa-techniques
- environment: public technique repository with authored bundle contracts, generated routing surfaces, and validator-backed markdown discipline
- runtime: documentation-first corpus that records the bounded media-bucketing pattern rather than shipping donor models, prompts, or OCR services
- live reinforcement: `end1989/ai-image-classification` at commit `e3f3500bf274e802d669ed38403b7637b0897366` repeats the same media-bucketing seam in a public MIT-licensed offline media sorter, while NSFW detection, face detection, UI workflow, auto-organization, local database schema, and file actions stay evidence-only and out of the technique

## What changed

- donor multimodal systems were reduced to one portable bucketing-and-review contract rather than one broad image-understanding or assistant workflow
- moderation policy, identity inference, and serving detail were removed from the reusable public bundle
- OCR-stage ownership was kept out so the adaptation only uses OCR as one optional side-channel during classification
- the bundle was reduced to one technique doc, one checklist, one example, and four bounded evidence notes
- Pack 30 promoted the adaptation to a cross-context canonical default after `end1989/ai-image-classification` confirmed bounded labels, CLIP scoring, OCR confidence side data, review thresholds, user corrections, and separated action/undo behavior outside the original donor README family

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
- `end1989/ai-image-classification` shows the pattern as a live public workflow: configured labels include screenshot, meme, receipt, document, work, food, people, nature, and other-style buckets; CLIP embeddings score those labels; OCR results are stored with text, confidence, and regions; OCR text boosts relevant labels such as receipt, chat, and work without replacing the visual classifier; review and auto-move thresholds are separate; review items are selected from the confidence band below auto-move; and user corrections are recorded as a separate training signal
- inspected `end1989/ai-image-classification` files: `README.md`, `LICENSE`, `docs/ARCHITECTURE.md`, `docs/03_phase2_ocr_nsfw_routing.md`, `config/config.yaml`, `config/config_loader.py`, `pipeline/classify.py`, `pipeline/ocr.py`, `backend/database.py`, and `pipeline/actions.py`

## Result

- works as a documentation-first adaptation with live public reinforcement and preserves the bounded core without carrying over donor model-serving detail, EasyOCR or PaddleOCR runtime packaging, NSFW/moderation features, face detection, file-manager behavior, auto-organization policy, UI workflow, database schema, or open-ended multimodal assistant behavior
