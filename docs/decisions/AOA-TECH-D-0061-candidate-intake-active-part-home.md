# Candidate Intake Active Part Home

Status: accepted
Date: 2026-05-18

## Index Metadata

- Decision ID: AOA-TECH-D-0061
- Original date: 2026-05-18
- Surface classes: mechanic part
- Technique axes: mechanic bridge
- Mechanic parents: cross-mechanic
- Guard families: part-local artifact
- Posture: accepted

## Context

After closed root `incoming/` packets moved to Distillation legacy, the next
question was where future active intake should live.

Root `incoming/` was too broad: active donor intake is mechanic-local
Distillation behavior, not a repo-wide public root district. A sibling
`mechanics/distillation/incoming/` directory was also too weak because
Distillation active behavior is mapped through `parts/`.

## Options considered

1. Keep root `incoming/` as the active quarantine.
2. Keep `mechanics/distillation/incoming/` beside `parts/`.
3. Move active intake to `mechanics/distillation/parts/candidate-intake/`.

## Decision

Active public-safe candidate intake lives in
`mechanics/distillation/parts/candidate-intake/`.

Closed packet roots live in
`mechanics/distillation/legacy/archive/closed-incoming-packets/`.
Root `incoming/` is retired unless a future decision creates a genuinely
repo-wide intake contract.

## Rationale

Candidate intake is current Distillation operation. It decides whether source
pressure remains a packet, becomes a ledger row, moves through an import
runbook, narrows into a gate packet, closes as a hold or exclusion, or becomes
legacy evidence.

That is active part behavior, so it belongs under `parts/` and must appear in
`PARTS.md`. Keeping it outside `parts/` would create an unindexed side door for
the same mechanic.

## Consequences

- Root no longer has a generic `incoming/` district.
- `candidate-intake/` has a bounded packet shape for future public-safe intake.
- Closed packet evidence remains archived under Distillation legacy.
- Distillation route docs, AGENTS mesh config, semantic AGENTS validation, and
  topology tests must name the part-local route.

## Source surfaces

- `docs/ROOT_SURFACE_LAW.md`
- `mechanics/distillation/AGENTS.md`
- `mechanics/distillation/README.md`
- `mechanics/distillation/PARTS.md`
- `mechanics/distillation/parts/candidate-intake/README.md`
- `mechanics/distillation/legacy/archive/closed-incoming-packets/README.md`

## Follow-up route

Create new candidate packet roots only under
`mechanics/distillation/parts/candidate-intake/`. Once a packet closes, move it
to the owning legacy route and update Distillation provenance, legacy index/log,
changelog, and tests.

## Verification

Validate the resulting route with:

```bash
python -m unittest mechanics.distillation.tests.test_distillation_incoming_topology
python scripts/validate_agents_md_shape.py
python scripts/validate_agents_mesh.py
python scripts/build_agents_mesh_index.py --check
python scripts/validate_agents_mesh_index.py
python scripts/validate_repo.py
python scripts/validate_semantic_agents.py
git diff --check
```
