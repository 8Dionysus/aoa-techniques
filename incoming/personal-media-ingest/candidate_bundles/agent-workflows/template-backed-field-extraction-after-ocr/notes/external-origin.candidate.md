# external-origin seed - template-backed-field-extraction-after-ocr

## Donor spine

- invoice2data
- receiptparser
- receipt-parser-legacy

## Bounded pattern extracted

- Extract stable fields after OCR through explicit templates, heuristics, and fallback review rather than pretending the parser already understands every document.

## What stays out

- invoice-only schema assumptions as universal law
- locale-locked merchant logic
- donor-specific parser code as canon

## Why narrower than the donors

- this seed extracts one reusable operational form
- it leaves implementation, runtime packaging, and donor worldview behind
- it does not claim the donor repo should be imported wholesale

## Expected evidence package if landed later

- `TECHNIQUE.md`
- `notes/external-origin.md`
- one minimal example or checklist
- release-path generated surfaces only after source markdown is accepted
