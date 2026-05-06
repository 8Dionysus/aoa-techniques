# minimal example seed

Input:
- one screenshot or scan

Output handoff object:
- `source_path`
- `regions[]`
  - `bbox`
  - `text`
  - `confidence`
- `low_confidence_spans[]`

The point of the example is not engine choice.
The point is that OCR output stays reviewable and separate from later field extraction.
