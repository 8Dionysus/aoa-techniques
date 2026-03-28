# minimal-two-stage-document-ocr-pipeline

Input:
- one screenshot, scan, or document page

Output handoff object:
- `source_path`
- `regions[]`
  - `bbox`
  - `text`
  - `confidence`
- `low_confidence_spans[]`

The point of the example is not one specific OCR engine.
The point is that OCR output stays reviewable, confidence-aware, and separate from later field extraction.
