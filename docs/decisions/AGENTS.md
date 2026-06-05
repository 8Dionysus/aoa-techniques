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

For canonical IDs or index metadata, read `README.md`, `TEMPLATE.md`, and
`indexes/index_contract.yaml`.

## Boundaries

- Do not treat this district as stronger than its source surfaces.
- Do not use a decision record to duplicate a roadmap, changelog, landing log,
  runbook, generated manifest, or mechanic ledger.
- Keep options, rationale, consequences, source surfaces, and follow-up route
  explicit.
- Route mechanic-local truth to `mechanics/<slug>/`.
- Route technique meaning to `techniques/**/TECHNIQUE.md`.
- Route sibling-owner truth to the owning AoA repository.
- Keep `modeled_surfaces` in `indexes/index_contract.yaml` as a top-level list
  of normalized repo-relative paths under `docs/decisions/`; do not use it for
  root non-record Markdown.

## Validation

Full lane command sequences live in `config/validation_lanes.json`; decision
records may preserve command evidence, but active command authority stays in
the lane manifest and entrypoints.
New or revised decision records should name lane ids and the nearest owner
`AGENTS.md` checks in active verification guidance. If an old command transcript
must be preserved, label it as historical verification evidence rather than
current command law.

For decision ID, metadata, and generated lookup-index parity, run:

```bash
python scripts/generate_decision_indexes.py --check
```

For decision-lane shape or AGENTS mesh changes, run:

```bash
python scripts/validate_agents_md_shape.py
python scripts/validate_agents_mesh.py
python scripts/build_agents_mesh_index.py --check
python scripts/validate_agents_mesh_index.py
```

For broad route, generated, release-facing, or public-facing changes, route
through the `generated` or `release` lane named in
[`COMMAND_AUTHORITY.md`](../validation/COMMAND_AUTHORITY.md), plus the nearest
owner `AGENTS.md` focused checks for the changed surface.

## Closeout

Report the decision records changed, the source surfaces consulted, whether the
record explains why rather than replacing current law, which generated mirrors
were rebuilt or checked, and which validators ran.
