# AGENTS.md

## Applies to

This card applies to preserved Audit lineage and future raw receipts.

## Role

`legacy/` preserves source-to-active accounting. It does not own current Audit
behavior.

## Read before editing

Read:

1. repository root `AGENTS.md`
2. `mechanics/AGENTS.md`
3. `mechanics/audit/AGENTS.md`
4. `mechanics/audit/PROVENANCE.md`
5. `mechanics/audit/legacy/README.md` or the touched raw/receipt surface when present

## Boundaries

- Do not use raw legacy files as the normal first route for current edits.
- Do not make raw legacy files the only place current active behavior lives.
- Do not create placeholder source receipts; preserve only actual source packets.
- Keep current behavior in `../README.md`, `../DIRECTION.md`, `../PARTS.md`, and
  `../parts/`.
- Add raw receipts under `raw/` before shortening an active ledger or runbook.
- Update `INDEX.md` and `DISTILLATION_LOG.md` when a legacy source is moved or
  compacted.

- Do not let this local card override authored source surfaces, schemas,
  builders, validators, or sibling owner truth.
- Do not claim skill execution, proof verdict, runtime, routing, memory,
  playbook, or owner-acceptance authority from this package.

## Validation

```bash
python -m unittest discover -s mechanics/audit/tests
```

## Closeout

Report the mechanic package, part, legacy surface, or helper changed;
whether source, generated, schema, example, or test surfaces moved; checks run;
checks skipped; and the next owner route.
