# minimal-semantic-media-bucketing-with-vision-plus-ocr

Input media item:
- `source_path: inbox/2026-03-28-001.png`
- `visual_candidates: screenshot 0.58, receipt 0.55, meme 0.14`
- `ocr_side_text: TOTAL 14.20 USD`

Output classification:
- `bucket: receipt`
- `confidence: medium`
- `ocr_signal_present: true`
- `review_required: true`
- `notes: OCR side text lifted receipt over screenshot, but confidence stayed below the auto-accept band`

The point of the example is that the technique keeps taxonomy bounded and uncertainty visible.
It does not decide deletion, archive, or downstream routing by itself.
