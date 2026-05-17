# AGENTS.md

## Applies to

This card applies to `docs/readers/` and all descendant generated-reader
districts unless a nearer `AGENTS.md` narrows the path.

## Role

`docs/readers/` holds Markdown reader companions that are generated or
builder-backed from stronger authored sources.

It does not own technique meaning, guide doctrine, source-lift contracts,
generated JSON authority, or release status.

## Read before editing

Read root `AGENTS.md`, `docs/AGENTS.md`, `docs/ROOT_SURFACE_LAW.md`, and the
guide that owns the reader family before changing paths or builder output.

For source-lift readers, also read `docs/source-lift/KAG_SOURCE_LIFT_GUIDE.md` and the
matching lift guide for the reader being moved or regenerated.

## Boundaries

- Keep reader Markdown subordinate to authored source docs and technique
  bundles.
- Keep generated JSON under `generated/`; this district is only for human
  Markdown companions.
- Do not hand-edit generated reader files except as part of a builder change
  that is immediately regenerated.
- Keep relative links valid from the reader district, not from `docs/` root.

## Validation

Run the builder for the moved reader family, then:

```bash
python scripts/validate_repo.py
python scripts/run_tests.py
```

For docs-root topology changes, also run:

```bash
python -m unittest tests.test_docs_surface_guardrails
```

## Closeout

Report which reader family moved, which builder paths changed, which generated
Markdown files were rebuilt, and which flat `docs/*.md` pressure remains.
