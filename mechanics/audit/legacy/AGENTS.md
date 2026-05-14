# AGENTS.md

Route card for `aoa-techniques/mechanics/audit/legacy/`.

## Applies to

This card applies to preserved Audit lineage and future raw receipts.

## Role

`legacy/` preserves source-to-active accounting. It does not own current Audit
behavior.

## Editing posture

- Keep current behavior in `../README.md`, `../DIRECTION.md`, `../PARTS.md`, and
  `../parts/`.
- Add raw receipts under `raw/` before shortening an active ledger or runbook.
- Update `INDEX.md` and `DISTILLATION_LOG.md` when a legacy source is moved or
  compacted.

## Verify

```bash
python -m unittest discover -s mechanics/audit/tests
```
