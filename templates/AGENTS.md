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

After changing templates, run:

```bash
python scripts/validate_nested_agents.py
python scripts/validate_repo.py
```

Snippet contract: keep `python scripts/validate_nested_agents.py` visible for
nested AGENTS validation.

## Closeout

Report changed templates, contract surfaces consulted, placeholder or heading
changes, checks run, and checks skipped.
