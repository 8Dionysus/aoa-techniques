---
id: AOA-T-XXXX
name: template-backed-field-extraction-after-ocr
domain: agent-workflows
status: draft-seed
origin: personal-ingest-wave-2
note: seed bundle staged for operator-guided external import
owners:
  - 8Dionysus
tags:
  - reusable
  - public
  - agent-friendly
  - personal-ingest
summary: Extract stable fields after OCR through explicit templates, heuristics, and fallback review rather than pretending the parser already understands every document.
maturity_score: 1
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: donor_soil
export_ready: false
relations: []
evidence:
  - kind: external_origin
    path: notes/external-origin.seed.md
---
# template-backed-field-extraction-after-ocr

## Intent

Turn OCR text into bounded structured fields such as date, amount, currency, and merchant without importing donor-specific parser doctrine wholesale.

## When to use

- you need receipt or invoice-like fields after OCR
- fields can be named explicitly
- template or heuristic routing is acceptable

## When not to use

- the source data is already structured
- the document family is too open-ended for bounded extraction
- the route really needs a live skill or app integration

## Inputs

- OCR handoff text
- optional donor-family template or merchant heuristics
- review thresholds

## Outputs

- bounded field object
- missing-field markers
- review-required cases

## Core procedure

1. take OCR handoff as the only parsing input
2. match candidate templates or heuristics
3. extract bounded fields such as date, amount, currency, merchant
4. emit missing or conflicting fields explicitly
5. route uncertain cases into review instead of forcing a full parse

## Contracts

- OCR and field extraction remain separate steps
- templates are bounded aids, not universal law
- uncertain or missing fields remain explicit
- the technique stays document-family-shaped, not vendor-app-shaped

## Risks

### Failure modes

- amount and tax lines are confused
- date parsing drifts across locale formats
- merchant heuristics overfit one store family

### Negative effects

- clean tables that hide missing evidence
- template sprawl that quietly becomes doctrine

### Misuse patterns

- treating one donor template family as universal
- backfilling guessed values without evidence

### Detection signals

- high extraction rate but low human trust
- silent default currency or date assumptions

### Mitigations

- missing-field markers
- template-level review notes
- review bucket for conflicts

## Validation

- mixed receipt set with known totals and dates
- conflict cases where amount candidates disagree
- duplicate receipt handling

## Adaptation notes

- locale/date formats
- merchant families
- currency defaults
- review thresholds

## Public sanitization notes

Remove donor-specific parser implementations, locale lock-in, and invoice-only world assumptions. Keep the bounded extraction contract.

## Example

See `examples/minimal_field_object.seed.md`.

## Checks

See `checks/checklist.seed.md`.

## Promotion history

- born in donor parsers and invoice extraction tools
- staged for personal-ingest wave 2

## Future evolution

- screen-receipt variants
- duplicate collapse
- receipt family packs
