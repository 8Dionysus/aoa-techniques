# External Origin Note

Use this note when a technique is adapted from an external open-source or public documentation source.
It complements `TECHNIQUE.md` and records provenance, adaptation boundaries, and public-safety review.

## Source

- source_repo: `https://github.com/invoice-x/invoice2data` plus `https://github.com/knipknap/receiptparser` plus `https://github.com/ReceiptManager/receipt-parser-legacy`
- source_license: `MIT + MIT + Apache-2.0` donor family
- inspired_by: not used in this import
- adapted_from: upstream README guidance from invoice2data, receiptparser, and receipt-parser-legacy showing OCR-derived text routed into explicit field extraction through templates, heuristics, and structured output objects

## What changed

- what_changed: narrowed the donor family to one bounded post-OCR seam: extract a small explicit field object through templates or heuristics and visible review fallbacks
- reusable object extracted: one structured field object with missing or conflicting markers plus optional field-evidence references back to OCR output
- invariant core kept: OCR handoff stays upstream, field targets stay explicit, templates or heuristics remain reviewable aids, and uncertainty remains visible
- project-shaped details removed or generalized: invoice-only schema law, locale-locked merchant logic, donor parser implementation details, bookkeeping integration, and ingestion automation
- nearest existing technique or overlap watch: `AOA-T-0070 two-stage-document-ocr-pipeline`
- what stays out of the donor: OCR staging, document taxonomy, duplicate-handling policy, bookkeeping automation, and donor parser runtime packaging

## Public-safety review

- secrets or tokens removed: none from the donor surfaces used for this import
- private paths, URLs, or IDs removed: none; the donor inputs are public upstream repositories and public README documentation
- environment-specific assumptions generalized: the public technique does not depend on one template pack, one locale bundle, or one donor parser runtime layout
- remaining public-safety concerns: the main risks are drift into OCR-stage ownership on one side and drift into full accounting or ingestion automation on the other

## Review notes

- why this adaptation is reusable here: many receipt-like or invoice-like workflows need a visible post-OCR extraction seam that keeps target fields, template assumptions, and review fallbacks explicit
- downstream repo impact: later execution packaging or ingestion workflows belong in `aoa-skills`, while this repository keeps only the reusable extraction contract
- limits or follow-up review concerns: this import still needs one second live adopter beyond the donor parser family and documentation-first adaptation before any canonical discussion is honest
