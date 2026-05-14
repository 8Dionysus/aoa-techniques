# AGENTS.md

Route card for `mechanics/method-growth/legacy/`.

## Role

`legacy/` preserves Method-growth source receipts and source-to-active
accounting. It is a provenance district, not the normal first route for current
mechanics edits.

## Editing Posture

- Start in `../README.md`, `../DIRECTION.md`, `../PARTS.md`, and `../parts/`
  for current behavior.
- Use `../PROVENANCE.md` as the active bridge into this district.
- Keep `INDEX.md`, `DISTILLATION_LOG.md`, and `raw/README.md` aligned.
- Do not place current Method-growth behavior only in raw legacy files.
- Do not invent raw receipts; preserve only actual source packets.

## Verify

Run:

```bash
python -m unittest discover -s mechanics/method-growth/tests
```
