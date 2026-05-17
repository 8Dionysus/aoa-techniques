# AGENTS.md

## Applies to

This card applies to `mechanics/release-support/parts/` and every descendant unless a nearer
`AGENTS.md` narrows the path.

## Role

Each part owns one bounded local release-support route for `aoa-techniques`.
Parts describe movement around technique canon; they do not become canonical
technique bundles or release authority.

## Read before editing

Read:

1. repository root `AGENTS.md`
2. `mechanics/AGENTS.md`
3. `mechanics/release-support/AGENTS.md`
4. `mechanics/release-support/PARTS.md`
5. the touched part README, schema, example, script, report, or test

## Boundaries

- Keep part docs concise and owner-bounded.
- Preserve links to `PROVENANCE.md` when moving or compacting source material.
- Keep release claims, public claims, proof, runtime, routing, SDK, stats,
  profile projection, and owner acceptance with their owning repositories.
- Promote into `techniques/` only when the reusable practice can stand as an
  atomic technique with validation.

- Do not let this local card override authored source surfaces, schemas,
  builders, validators, or sibling owner truth.
- Do not claim skill execution, proof verdict, runtime, routing, memory,
  playbook, or owner-acceptance authority from this package.

## Validation

Use the package and root tests after part changes:

```bash
python -m unittest discover -s mechanics/release-support/tests
python scripts/validate_repo.py
```

## Closeout

Report the mechanic package, part, legacy surface, or helper changed;
whether source, generated, schema, example, or test surfaces moved; checks run;
checks skipped; and the next owner route.
