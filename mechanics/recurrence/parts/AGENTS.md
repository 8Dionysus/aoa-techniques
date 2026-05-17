# AGENTS.md

## Applies to

This card applies to `mechanics/recurrence/parts/` and every descendant unless a nearer
`AGENTS.md` narrows the path.

## Role

Each part owns one bounded local recurrence route for `aoa-techniques`.
Parts describe observation and closure movement around technique canon; they do
not become canonical technique bundles.

## Read before editing

Read:

1. repository root `AGENTS.md`
2. `mechanics/AGENTS.md`
3. `mechanics/recurrence/AGENTS.md`
4. `mechanics/recurrence/PARTS.md`
5. the touched part README, schema, example, script, report, or test

## Boundaries

- Keep part docs concise and owner-bounded.
- Preserve links to `PROVENANCE.md` when moving or compacting source material.
- Keep generated surfaces, manifests, live receipts, and readiness payloads as
  evidence only.
- Route execution, proof, memory, runtime, role, route, SDK carry, KAG, stats,
  and playbook meaning to the owning repository.
- Promote into `techniques/` only when the reusable practice can stand as an
  atomic technique with validation.

- Do not let this local card override authored source surfaces, schemas,
  builders, validators, or sibling owner truth.
- Do not claim skill execution, proof verdict, runtime, routing, memory,
  playbook, or owner-acceptance authority from this package.

## Validation

Use the package and root tests after part changes:

```bash
python -m unittest discover -s mechanics/recurrence/tests
python scripts/validate_repo.py
```

## Closeout

Report the mechanic package, part, legacy surface, or helper changed;
whether source, generated, schema, example, or test surfaces moved; checks run;
checks skipped; and the next owner route.
