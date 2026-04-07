# Origin Evidence

## Technique
- id: AOA-T-0098
- name: receipt-first-failure-analysis

## Source project
- name: ATM10-Agent
- source files:
  - `docs/ANTIFRAGILITY_FIRST_WAVE.md`
  - `schemas/stressor_receipt_v1.json`
  - `examples/stressor_receipt.retrieval_only_fallback.example.json`

## Evidence
- the first-wave antifragility landing showed that the main risk was not a lack of ideas but jumping from a degraded run straight to explanation, remediation, or summary language without a stable owner-local evidence anchor
- the owner-local receipt surface gave a compact starting point for bounded review without collapsing the larger run artifacts into one prestige narrative
- the portable review shape is small and repeatable: start from the receipt, separate fact from guess, propose the smallest plausible change, and define how the next receipt or eval would show improvement

## Interpretation
- the pattern is evidence-led rather than dashboard-led or memory-led
- it stays downstream from owner-local receipts instead of replacing them
- it can travel to other repos as long as they already expose one trustworthy receipt family
