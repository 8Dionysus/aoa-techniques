# External Origin Note

Use this note when a technique is adapted from an external open-source or public documentation source.
It complements `TECHNIQUE.md` and records provenance, adaptation boundaries, and public-safety review.

## Source

- source_repo: `https://github.com/openai/CLIP` plus `https://github.com/PaddlePaddle/PaddleOCR`
- source_license: `MIT + Apache-2.0` donor family
- inspired_by: not used in this import
- adapted_from: upstream README guidance from CLIP and PaddleOCR showing zero-shot image-text semantic scoring plus OCR-derived text extraction that can sharpen classification over text-bearing images

## What changed

- what_changed: narrowed the donor family to one bounded classification seam: visual semantics plus optional OCR side text produce coarse bucket labels under explicit confidence gates
- reusable object extracted: one reviewable media-bucketing surface with bounded labels, confidence signals, and explicit review handling for low-confidence or conflicting items
- invariant core kept: taxonomy remains explicit, OCR stays side-channel, and classification remains separate from later policy actions
- project-shaped details removed or generalized: open-ended multimodal assistant claims, moderation policy, identity inference, model-serving detail, prompt engineering doctrine, and donor runtime packaging
- nearest existing technique or overlap watch: `AOA-T-0072 perceptual-media-dedupe-with-threshold-review`
- what stays out of the donor: duplicate grouping, OCR extraction ownership, moderation, deletion or archive policy, and identity inference

## Public-safety review

- secrets or tokens removed: none from the donor surfaces used for this import
- private paths, URLs, or IDs removed: none; the donor inputs are public upstream repositories and public README documentation
- environment-specific assumptions generalized: the public technique does not depend on one model checkpoint, one OCR service layout, one prompt template, or one serving topology
- remaining public-safety concerns: the main risks are drift into open-ended multimodal policy on one side and drift into OCR-first truth or duplicate-grouping policy on the other

## Review notes

- why this adaptation is reusable here: many mixed-media workflows need one bounded taxonomy seam before later review, storage, or cleanup actions happen, especially when OCR can sharpen ambiguous text-heavy images
- downstream repo impact: later routing or cleanup workflows belong in `aoa-skills`, while this repository keeps only the reusable classification contract
- limits or follow-up review concerns: this import still needs one second live adopter beyond the donor classification family and documentation-first adaptation before any canonical discussion is honest
