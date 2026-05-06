# external-origin seed - two-stage-document-ocr-pipeline

## Donor spine

- PaddleOCR
- docTR

## Bounded pattern extracted

- Stage OCR as detect/layout -> recognize -> structured handoff so downstream extraction stays interchangeable and reviewable.

## What stays out

- model-serving doctrine
- benchmark theater
- framework-specific runtime packaging
- LLM wrapper posture

## Why narrower than the donors

- this seed extracts one reusable operational form
- it leaves implementation, runtime packaging, and donor worldview behind
- it does not claim the donor repo should be imported wholesale

## Expected evidence package if landed later

- `TECHNIQUE.md`
- `notes/external-origin.md`
- one minimal example or checklist
- release-path generated surfaces only after source markdown is accepted
