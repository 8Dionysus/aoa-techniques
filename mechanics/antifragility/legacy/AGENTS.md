# AGENTS.md

Route card for `mechanics/antifragility/legacy/`.

## Purpose

This lane preserves pre-split antifragility source material. It is source
lineage, not the active operating route.

## Local law

- Keep raw donor or wave material in `raw/`.
- Use `INDEX.md` and `DISTILLATION_LOG.md` to explain how source material moved
  into active parts.
- Do not make legacy files the only home for current behavior.
- Do not edit raw files to make them read like current law; add active distills
  or provenance notes instead.

## Verify

After legacy changes, run:

```bash
python -m unittest discover -s mechanics/antifragility/tests
python scripts/validate_repo.py
```
