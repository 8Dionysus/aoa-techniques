# minimal-template-backed-field-extraction-after-ocr

Input OCR handoff:
- `merchant_line`: `Corner Market`
- `date_line`: `2026-03-24`
- `amount_candidates`: `TOTAL 14.20`, `VAT 1.20`
- `currency_hint`: `USD`

Output field object:
- `merchant`: `Corner Market`
- `transaction_date`: `2026-03-24`
- `total_amount`: `14.20`
- `currency`: `USD`
- `missing_fields[]`: none
- `conflicts[]`: none
- `field_evidence[]`
  - `merchant <- merchant_line`
  - `transaction_date <- date_line`
  - `total_amount <- amount_candidates[0]`

Review case:
- if two amount candidates survive with similar confidence, emit both as a conflict instead of guessing one winner
