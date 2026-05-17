# AGENTS.md

## Applies to

This card applies to
`mechanics/recurrence/parts/live-observation-producers/scripts/` and every descendant unless a nearer
`AGENTS.md` narrows the path.

## Role

This directory holds one-owner Recurrence helper scripts for live observation
producer inputs.

`publish_live_receipts.py` appends bounded technique-layer receipts to the
owner-local live JSONL log. The log remains observation evidence only; it does
not create candidates, close quests, change technique status, issue proof
verdicts, or claim runtime recurrence authority.

Keep the helper public-safe and repo-relative. Do not add hidden network calls,
ambient credentials, or private session dumps.

## Read before editing

Read:

1. repository root `AGENTS.md`
2. `mechanics/AGENTS.md`
3. `mechanics/recurrence/AGENTS.md`
4. `mechanics/recurrence/PARTS.md`
5. the touched part README, schema, example, script, report, or test

## Boundaries

- Do not let this local card override authored source surfaces, schemas,
  builders, validators, or sibling owner truth.
- Do not claim skill execution, proof verdict, runtime, routing, memory,
  playbook, or owner-acceptance authority from this package.

## Validation

Verify with:

```bash
python -m unittest discover -s mechanics/recurrence/tests -p 'test_publish_live_receipts.py'
python -m unittest discover -s mechanics/recurrence/tests
python scripts/validate_repo.py
```

## Closeout

Report the mechanic package, part, legacy surface, or helper changed;
whether source, generated, schema, example, or test surfaces moved; checks run;
checks skipped; and the next owner route.
