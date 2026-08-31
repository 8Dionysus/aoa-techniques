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

Use this shared order: root `AGENTS.md` -> `TECHNIQUE_INDEX.md` ->
`docs/START_HERE.md` -> the relevant trunk or retained lane -> target
`TECHNIQUE.md` -> touched support/generated surfaces. Read `README.md` only
when the selected task needs its human map; do not preload unrelated maps.
Trunk cards add their local role and shelves; retained lanes add migration and
provenance context.

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

Select the narrowest owner route: `source-fast` for authored or route-card work; add `generated` for projections and `release` only for release posture. See [VALIDATION.md](../VALIDATION.md); exact order is `config/validation_lanes.json`; focused procedure stays with the nearest owner. Report checks, skips, and blockers.

## Closeout

Report technique IDs; trunk, shelf, and slug paths; frontmatter changes;
generated surfaces rebuilt or left untouched; checks run; checks skipped; and
remaining owner-boundary risk. Trunk cards also report the trunk, shelf, and
bundle paths changed; whether path, frontmatter, generated catalogs, or reader
surfaces changed; checks run; checks skipped; and any remaining owner-route
risk.

Tree trunks inherit this placement contract: the tree is a route spine, not
frontmatter truth; meaning stays in `TECHNIQUE.md`; `tree_path` is not added by
path alone; and renames require a reviewed projection and bounded receipt.
