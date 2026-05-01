# AGENTS.md

Route card for `aoa-techniques/mechanics/distillation/legacy/`.

## Applies to

This card applies to preserved Distillation lineage and future raw receipts.

## Role

`legacy/` preserves accounting for raw-to-active Distillation movement. It is
not the active operating contract.

## Editing posture

- Do not change a legacy receipt to alter current behavior.
- If a legacy source changes current behavior, update the active part first.
- Record any new raw preservation in `INDEX.md` and `DISTILLATION_LOG.md`.
- Keep raw receipts public-safe before adding them here.

## Verify

```bash
python -m unittest tests.test_distillation_mechanics_topology
```
