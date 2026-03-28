# two-stage-document-ocr-pipeline checklist

- [ ] the workflow keeps OCR staging separate from downstream field extraction
- [ ] region, line, or layout references remain visible in the handoff
- [ ] low-confidence spans remain explicit
- [ ] the handoff can be consumed without donor-specific runtime code
- [ ] engine choice can vary without changing the bounded contract
- [ ] receipt-specific schema, serving posture, and benchmark doctrine stay out of scope
