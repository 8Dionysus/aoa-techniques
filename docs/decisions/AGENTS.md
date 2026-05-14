# AGENTS.md

## Applies to

This card applies to `docs/decisions/` and all descendants unless a nearer
`AGENTS.md` narrows the path.

## Role

`docs/decisions/` holds decision records for meaningful `aoa-techniques`
structure, ownership, workflow, route-law, validator, public-contract, and
topology choices.

Decision records explain why a path was chosen. Current source surfaces define
what the repository now does.

## Read before editing

Read root `AGENTS.md`, `docs/AGENTS.md`, `docs/README.md`,
`docs/ROOT_SURFACE_LAW.md`, this file, and `TEMPLATE.md`.

Also read the source surfaces that the decision affects, such as root docs,
mechanic package cards, generated-source builders, validators, tests, or
technique contracts.

## Boundaries

- Do not treat this district as stronger than its source surfaces.
- Do not use a decision record to duplicate a roadmap, changelog, landing log,
  runbook, generated manifest, or mechanic ledger.
- Keep options, rationale, consequences, source surfaces, and follow-up route
  explicit.
- Route mechanic-local truth to `mechanics/<slug>/`.
- Route technique meaning to `techniques/**/TECHNIQUE.md`.
- Route sibling-owner truth to the owning AoA repository.

## Validation

For decision-lane shape or AGENTS mesh changes, run:

```bash
python scripts/validate_agents_md_shape.py
python scripts/validate_agents_mesh.py
python scripts/build_agents_mesh_index.py --check
python scripts/validate_agents_mesh_index.py
```

For broad route, generated, or public-facing changes, run:

```bash
python scripts/validate_repo.py
python scripts/release_check.py
```

## Closeout

Report the decision records changed, the source surfaces consulted, whether the
record explains why rather than replacing current law, which generated mirrors
were rebuilt or checked, and which validators ran.
