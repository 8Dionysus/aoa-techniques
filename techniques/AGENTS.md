# AGENTS.md

Guidance for coding agents and humans working under `techniques/`.

## Purpose

`techniques/` stores the published technique bundles of `aoa-techniques`.

The authored bundle is the canonical meaning surface for a technique. The primary object is `techniques/*/*/TECHNIQUE.md`, with optional support directories such as `checks/`, `examples/`, and `notes/`.

## Read this first

Before editing anything here, read in this order:

1. `../AGENTS.md`
2. `../README.md`
3. `../TECHNIQUE_INDEX.md`
4. `../docs/START_HERE.md`
5. the relevant domain-level `AGENTS.md`
6. the target `TECHNIQUE.md`
7. any touched `checks/`, `examples/`, and `notes/`
8. any generated surfaces affected by the change

## Bundle contract

`TECHNIQUE.md` owns the bounded contract, section posture, and frontmatter semantics.
`checks/`, `examples/`, and `notes/` may clarify, verify, or record evidence, but they must not silently replace the main technique meaning.
Preserve technique IDs, maturity labels, and domain placement unless the task explicitly requires a reviewed change.

Do not add bundle-local `AGENTS.md` by default. Use a deeper file only when one domain or sub-surface has a genuine local rule that cannot live cleanly in `TECHNIQUE.md`.

## Allowed changes

Safe, normal contributions here include:

- clarifying bounded intent, inputs, outputs, contracts, risks, or validation
- strengthening examples or notes without widening the technique
- repairing metadata drift between the bundle and generated reader surfaces
- adding a new technique when it is reusable, public-safe, and clearly belongs in this repository

## Changes requiring extra care

Use extra caution when:

- changing a technique ID or directory name
- changing domain placement under `techniques/`
- changing maturity posture such as `promoted`, `canonical`, or `deprecated`
- changing wording that downstream skills, evals, or routing surfaces may rely on
- removing evidence notes or support artifacts that explain current boundedness

## Hard NO

Do not:

- publish secrets, private hostnames, or internal-only procedures
- turn a technique into vague philosophy or project-local folklore
- widen a reusable technique into a live runtime contract that belongs in `aoa-skills`, `aoa-evals`, or a project repo
- add support files that contradict the authored bundle

## Validation

Before validator or release-check commands here, run `python -m pip install -r requirements-dev.txt`.

After changes, run the smallest checks that cover the touched surface. In most cases that means:

- `python scripts/validate_nested_agents.py`
- `python scripts/validate_repo.py`
- `python scripts/release_check.py` when generated outputs changed
