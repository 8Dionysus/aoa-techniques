# External Origin Note

Use this note when a technique is adapted from an external open-source or public documentation source.
It complements `TECHNIQUE.md` and records provenance, adaptation boundaries, and public-safety review.

## Source

- source_repo: `https://github.com/PaddlePaddle/PaddleOCR` plus `https://github.com/mindee/doctr`
- source_license: `Apache-2.0` donor family
- inspired_by: not used in this import
- adapted_from: upstream `README.md` guidance from PaddleOCR and docTR showing OCR as an explicit detect or layout plus recognize flow before downstream parsing

## What changed

- what_changed: narrowed the donor family to one bounded OCR seam: detect or layout -> recognize -> structured handoff before later extraction starts
- reusable object extracted: one confidence-aware OCR handoff that preserves region or layout references and low-confidence spans for later review or extraction
- invariant core kept: OCR stays explicitly staged, ambiguity remains visible, and downstream consumers receive one structured handoff instead of engine-specific runtime internals
- project-shaped details removed or generalized: serving posture, benchmark claims, framework packaging, engine-comparison rhetoric, and receipt-specific or invoice-specific field semantics
- nearest existing technique or overlap watch: `template-backed-field-extraction-after-ocr`
- what stays out of the donor: downstream field extraction, document taxonomy, model-serving doctrine, benchmark theater, and app-specific automation logic

## Public-safety review

- secrets or tokens removed: none from the donor surfaces used for this import
- private paths, URLs, or IDs removed: none; the donor inputs are public upstream repositories and public README documentation
- environment-specific assumptions generalized: the public technique does not depend on one OCR engine package, one serving topology, or one donor-specific runtime layout
- remaining public-safety concerns: the main risks are drift into field-extraction doctrine on one side and drift into OCR platform, benchmarking, or packaging doctrine on the other

## Review notes

- why this adaptation is reusable here: many document and screenshot workflows need OCR to remain a visible intermediate seam before later extraction, review, or normalization logic begins
- downstream repo impact: likely follow-on imports stay in `aoa-techniques` first as bounded siblings, while later execution packaging belongs in `aoa-skills`
- limits or follow-up review concerns: this import still needs one second live adopter beyond the donor OCR family and documentation-first adaptation before any canonical discussion is honest
