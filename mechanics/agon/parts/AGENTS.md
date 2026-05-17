# AGENTS.md

## Applies to

This card applies to `mechanics/agon/parts/` and every descendant unless a nearer
`AGENTS.md` narrows the path.

## Role

Part directories own active Agon technique-side behavior. They do not preserve
raw wave receipts and they do not author Agon center doctrine.

## Read before editing

Read:

1. repository root `AGENTS.md`
2. `mechanics/AGENTS.md`
3. `mechanics/agon/AGENTS.md`
4. `mechanics/agon/PARTS.md`
5. the touched part README, schema, example, script, report, or test

## Boundaries

- Keep each part focused on one current behavior.
- Route historical wave detail through `../PROVENANCE.md` and `../legacy/`.
- Keep generated candidate indexes subordinate to their source seeds and stop
  lines.
- Do not promote candidates into techniques from a part README.

## Validation

Run the owning Agon checks:

```bash
python -m unittest discover -s mechanics/agon/tests
python scripts/validate_repo.py
```

## Closeout

Report the mechanic package, part, legacy surface, or helper changed;
whether source, generated, schema, example, or test surfaces moved; checks run;
checks skipped; and the next owner route.
