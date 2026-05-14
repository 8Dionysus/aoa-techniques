# AGENTS.md

## Applies to

This card applies to `schemas/` and all descendants unless a nearer
`AGENTS.md` narrows the path.

## Role

`schemas/` holds machine-readable contracts for technique surfaces, reports,
manifests, examples, or downstream exports.

Schema edits are contract edits. Preserve `$schema`, stable identifier posture,
required fields, enums, and descriptions that keep techniques reproducible.

Root schemas are for repo-wide contracts and shared export shapes. A schema
that describes one mechanic part belongs under
`mechanics/<slug>/parts/<part>/schemas/`, with its paired examples under the
same part's `examples/` directory.

## Read before editing

Read root `AGENTS.md`, `docs/START_HERE.md`, the consuming builder or
validator, the paired examples, and any downstream consumer route.

## Boundaries

- Do not loosen a schema only to pass a broken generated file.
- Fix the source, update paired examples, or document the contract change.
- Do not move mechanic-local contracts into root schemas.
- Do not add a schema without naming the downstream consumer and validation
  path.

## Validation

When a schema affects routing, KAG lift, or skill composition, re-check the
downstream consumer surface and name the owner repo in the report.

Verify with:

```bash
python scripts/validate_repo.py
python scripts/validate_semantic_agents.py
```

## Closeout

Report changed schemas, paired examples, downstream consumer, generated
surfaces rebuilt or left untouched, validation run, and validation skipped.
