# AGENTS.md

Route card for `mechanics/agon/legacy/`.

## Role

`legacy/` preserves Agon wave source receipts that are too historical or heavy
for the active route. It is not a trash archive and not the normal first route
for current edits.

## Editing posture

- Do not delete raw wave receipts after distillation.
- Do not make `legacy/raw/` the only place current active behavior lives.
- When a raw source affects current behavior, update the active part first.
- Keep `INDEX.md` and `DISTILLATION_LOG.md` aligned with any new preserved
  source.

## Verify

Use [../AGENTS.md](../AGENTS.md#verify) when legacy changes affect active
candidate routes or validation posture.
