# AGENTS.md

Guidance for coding agents and humans working under `templates/`.

## Purpose

`templates/` stores reusable authoring scaffolds for technique bundles and related notes.

## Rules

Keep templates aligned with the current repository contract and section posture.
Preserve placeholders, frontmatter keys, and required headings unless the repository-wide bundle contract has intentionally changed.
Do not turn a template into a finished example that hides what is supposed to be filled in by the author.

## Current surfaces

- `TECHNIQUE.template.md`
- `ADAPTATION_NOTE.template.md`
- `PROMOTION_NOTE.template.md`

## Validation

Before validator or release-check commands here, run `python -m pip install -r requirements-dev.txt`.

After changing templates, run:

- `python scripts/validate_nested_agents.py`
- `python scripts/validate_repo.py`
