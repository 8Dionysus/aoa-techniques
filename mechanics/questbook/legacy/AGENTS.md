# AGENTS.md

Route card for `mechanics/questbook/legacy/`.

## Role

`legacy/` preserves Questbook source receipts and source-to-active accounting.
It is a provenance district, not the normal first route for current mechanics
edits.

## Editing Posture

- Start in `../README.md`, `../DIRECTION.md`, `../PARTS.md`, and `../parts/`
  for current behavior.
- Use `../PROVENANCE.md` as the active bridge into this district.
- Keep `INDEX.md`, `DISTILLATION_LOG.md`, and `raw/README.md` aligned.
- Do not place current Questbook behavior only in raw legacy files.
- Do not invent raw receipts; preserve only actual source packets.

## Verify

Run:

```bash
python -m unittest tests.test_questbook_mechanics_topology
```
