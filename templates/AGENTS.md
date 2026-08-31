# AGENTS.md

## Applies to

This card applies to `templates/` and all descendants unless a nearer
`AGENTS.md` narrows the path.

## Role

`templates/` stores reusable authoring scaffolds for technique bundles and
related notes.

## Read before editing

Read root `AGENTS.md`, `docs/TECHNIQUE_ATOM_CONTRACT.md`,
`docs/TECHNIQUE_TOPOLOGY_CONTRACT.md`, `docs/TECHNIQUE_TREE_CONTRACT.md`, and
the validator that enforces the edited template.
Read `README.md` only when the selected task needs its human map; do not preload unrelated maps.

## Boundaries

- Keep templates aligned with the current repository contract and section
  posture.
- Preserve placeholders, frontmatter keys, and required headings unless the
  repository-wide bundle contract has intentionally changed.
- Do not turn a template into a finished example that hides what is supposed to
  be filled in by the author.
- Keep `TECHNIQUE.template.md`, `ADAPTATION_NOTE.template.md`, and
  `PROMOTION_NOTE.template.md` public-safe and source-neutral.

## Validation

Select the narrowest owner route: `source-fast` for authored or route-card work; add `generated` for projections and `release` only for release posture. See [VALIDATION.md](../VALIDATION.md); exact order is `config/validation_lanes.json`; focused procedure stays with the nearest owner. Report checks, skips, and blockers.

## Closeout

Report changed templates, contract surfaces consulted, placeholder or heading
changes, checks run, and checks skipped.
