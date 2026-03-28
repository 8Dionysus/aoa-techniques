---
id: AOA-T-0071
name: template-backed-field-extraction-after-ocr
domain: agent-workflows
status: promoted
origin:
  project: invoice2data + receiptparser + receipt-parser-legacy
  path: README.md
  note: Adapted from open-source invoice and receipt parsers that keep field extraction explicit through templates, heuristics, and bounded output objects after OCR rather than collapsing every document family into one opaque parser.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - ocr
  - field-extraction
  - templates
  - receipts
summary: Extract bounded fields after OCR through explicit templates, heuristics, and missing-or-conflict signaling so structured receipt-like data stays reviewable instead of being guessed by one opaque parser.
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

# template-backed-field-extraction-after-ocr

## Intent

Turn OCR handoff text into a bounded field object such as merchant, date, amount, and currency through explicit templates, heuristics, and fallback review instead of pretending one parser already understands every document family.

## When to use

- a prior OCR stage already exists and the next reusable seam is post-OCR field extraction
- the target field set can be named explicitly ahead of time
- receipt-like, invoice-like, or similarly bounded document families are in scope
- template or heuristic matching is acceptable as long as uncertainty stays visible
- downstream consumers need structured fields without inheriting donor parser code or app-specific accounting flows

## When not to use

- the source is already structured and no OCR-derived extraction is needed
- the real reusable object is still OCR staging rather than field extraction
- the document family is too open-ended for one bounded field contract
- the workflow only makes sense as a full bookkeeping, ingestion, or app-automation product stack

## Inputs

- one structured OCR handoff from an earlier OCR stage
- one explicit field set such as merchant, transaction date, total amount, and currency
- optional template family, merchant heuristics, or locale hints
- one review threshold for missing or conflicting fields

## Outputs

- one bounded field object
- missing-field markers for absent required values
- conflict markers when more than one candidate survives
- optional source snippets or field-evidence references back to the OCR handoff

## Core procedure

1. Take the OCR handoff as the only parsing input for the bounded contract.
2. Match one template or heuristic family using explicit cues from the OCR output.
3. Extract only the named bounded field set instead of widening into every possible document attribute.
4. Preserve field-to-source evidence references when the downstream review path needs to inspect where a value came from.
5. Emit missing or conflicting fields explicitly instead of silently guessing a best-looking parse.
6. Route unresolved cases into review rather than backfilling defaults as if they were certain truth.
7. Keep locale policy, duplicate handling, bookkeeping automation, and donor parser implementation outside the invariant contract.

## Contracts

- OCR staging and field extraction remain separate steps
- the target field set stays explicit and bounded
- templates and heuristics act as reviewable aids, not as universal document law
- missing or conflicting values remain explicit
- field extraction stays smaller than end-to-end receipt, invoice, or accounting automation
- downstream consumers receive a structured field object plus review signals rather than donor parser internals

Relationship to adjacent techniques: unlike [AOA-T-0070](../two-stage-document-ocr-pipeline/TECHNIQUE.md), this technique starts after OCR handoff already exists and does not own text-region detection or recognition. It also stays smaller than any later semantic media bucketing or ingestion automation technique because it only extracts a bounded field object from OCR-derived text.

## Risks

### Failure modes

- amount, subtotal, tax, or tip lines are confused
- locale-specific date formats are parsed incorrectly
- merchant heuristics overfit one store or invoice family
- source references disappear and reviewers cannot tell why a field was chosen

### Negative effects

- clean-looking structured output can hide missing evidence
- template sprawl can quietly become doctrine
- downstream systems may overtrust a bounded field object as final truth

### Misuse patterns

- treating one donor template family as universal
- backfilling guessed values without evidence
- widening the technique into end-to-end accounting or ingestion automation

### Detection signals

- extraction coverage looks high while human trust stays low
- currency, date, or merchant values default silently too often
- reviewers cannot trace a parsed value back to the OCR handoff

### Mitigations

- keep missing-field and conflict markers explicit
- preserve field-evidence references when review matters
- keep template assumptions visible and local to the bounded field set
- route unresolved cases into review instead of forcing a parse

## Validation

Verify the technique by confirming that:
- OCR handoff is the only bounded parsing input
- the extracted field set is explicit and small enough to review
- missing or conflicting fields remain visible
- source evidence can be traced back into the OCR handoff when needed
- locale defaults, donor parser code, and automation doctrine stay outside the contract

See `checks/template-backed-field-extraction-after-ocr-checklist.md`.

## Adaptation notes

What can vary across projects:
- the exact field set
- template files or heuristic packs
- locale and currency hints
- field-evidence reference format
- review thresholds for conflicts or missing values

What should stay invariant:
- OCR handoff remains upstream and separate
- extraction targets a bounded field object
- uncertainty stays explicit through missing or conflicting markers
- templates and heuristics stay reviewable rather than hidden inside parser code

Project-shaped details that should not be treated as invariant:
- invoice-only schema assumptions
- merchant-specific logic as universal law
- donor parser internals
- bookkeeping or ingestion automation

## Public sanitization notes

This public bundle keeps only the reusable post-OCR extraction seam: bounded fields are extracted from OCR text through visible templates or heuristics, uncertainty stays explicit, and downstream systems receive one reviewable field object. Donor parser implementation, locale lock-in, bookkeeping flows, and app-specific automation were intentionally removed or generalized.

## Example

See `examples/minimal-template-backed-field-extraction-after-ocr.md`.

## Checks

See `checks/template-backed-field-extraction-after-ocr-checklist.md`.

## Promotion history

- adapted from open-source `invoice2data`, `receiptparser`, and `receipt-parser-legacy`
- landed from `personal-ingest-wave-2`
- promoted into `aoa-techniques` on 2026-03-28 as a bounded external-import technique for post-OCR template-backed field extraction

## Future evolution

- keep OCR staging separate unless a narrower bridge seam proves necessary
- split duplicate handling or receipt-family packs only if those contracts survive independently
- add a stronger second live context if another public workflow keeps post-OCR field extraction explicit and reviewable
