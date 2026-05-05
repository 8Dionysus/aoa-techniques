# AGENTS.md

Guidance for coding agents and humans working under `techniques/proof/`.

## Purpose

This trunk stores technique bundles that support validation, review evidence,
summary integrity, owner-truth checks, and related proof-facing practice.

The trunk is a placement aid for browseable technique canon. It is not
`aoa-evals`, not proof verdict authority, and not a replacement for an owning
repository's validation policy.

## Domain rules

Keep proof-facing techniques narrow, portable, and explicit about what their
evidence does and does not prove.

Current landed shelves:

- `skill-support/`: bounded-context vocabulary, consumer-visible contract
  validation, and invariant-oriented coverage around capability or subsystem
  boundaries.

## Boundary

Do not widen a proof technique into an eval suite, release gate, runtime
doctor, owner-truth law, security policy, or generic testing doctrine.

If the object becomes a concrete reusable eval bundle, route it to `aoa-evals`.
If it becomes an execution workflow or operational runbook, route it to the
owning repo or `aoa-skills`. If it becomes AoA constitutional direction, route
it to `Agents-of-Abyss`.

## Hard NO

Do not:

- claim that a technique path proves quality by itself
- change `domain` or `kind` frontmatter merely because the bundle now lives
  under `proof/`
- collapse context mapping, contract testing, and invariant coverage into one
  combined proof technique
- import sibling-owner authority into a portable technique bundle

## Validation

After changing proof-trunk technique bundles, run:

- `python scripts/validate_nested_agents.py`
- `python scripts/validate_repo.py`

Run `python scripts/release_check.py` when paths, generated reader surfaces, or
catalog outputs change.
