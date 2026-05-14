# AGENTS.md

## Applies to

This card applies to `techniques/` and all descendants unless a nearer
`AGENTS.md` narrows the path.

## Role

`techniques/` stores the published technique bundles of `aoa-techniques`.

The authored bundle is the canonical meaning surface for a technique. The
primary object is `techniques/<trunk>/<shelf>/<slug>/TECHNIQUE.md`, with
optional support directories such as `checks/`, `examples/`, and `notes/`.

## Read before editing

Before editing anything here, read in this order:

1. `../AGENTS.md`
2. `../README.md`
3. `../TECHNIQUE_INDEX.md`
4. `../docs/START_HERE.md`
5. the relevant trunk or retained frontmatter-lane `AGENTS.md`
6. the target `TECHNIQUE.md`
7. any touched `checks/`, `examples/`, and `notes/`
8. any generated surfaces affected by the change

## Boundaries

`TECHNIQUE.md` owns the bounded contract, section posture, and frontmatter
semantics. `checks/`, `examples/`, and `notes/` may clarify, verify, or record
evidence, but they must not silently replace the main technique meaning.

Preserve technique IDs, maturity labels, and domain placement unless the task
explicitly requires a reviewed change.

Do not add bundle-local `AGENTS.md` by default. Use a deeper file only when one
domain or sub-surface has a genuine local rule that cannot live cleanly in
`TECHNIQUE.md`.

Do not publish secrets, private hostnames, internal-only procedures, vague
philosophy, project-local folklore, or live runtime contracts that belong in
`aoa-skills`, `aoa-evals`, or a project repo.

## Validation

After changes, run the smallest checks that cover the touched surface. Common
paths include:

```bash
python scripts/validate_nested_agents.py
python scripts/validate_repo.py
```

Snippet contract: keep `python scripts/validate_repo.py` visible for nested
AGENTS validation.

Run `python scripts/release_check.py` when generated outputs changed.

## Closeout

Report technique IDs, trunk/shelf/slug paths, frontmatter changes, generated
surfaces rebuilt or left untouched, checks run, checks skipped, and remaining
owner-boundary risk.
