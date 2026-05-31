# Decision Note: AGENTS Mesh Canonical Closure

Status: accepted
Date: 2026-05-17

## Index Metadata

- Decision ID: AOA-TECH-D-0060
- Original date: 2026-05-17
- Surface classes: agent route
- Technique axes: agent mesh
- Mechanic parents: none
- Guard families: AGENTS/mesh
- Posture: accepted

## Context

The `aoa-techniques` AGENTS mesh was introduced with a deliberate migration
posture: durable top-level route cards were canonical, while many older local
mechanic, technique-trunk, docs-district, and deep part cards remained visible
as migration cards in `generated/agents_mesh.min.json`.

That posture made the migration debt reviewable, but keeping it indefinitely
would let old card shapes stay normal and would make future directory growth
harder to distinguish from unfinished normalization.

## Options considered

1. Keep `migration_allowed` true and continue normalizing cards opportunistically.
2. Normalize every discovered card now and close the mesh to migration drift.
3. Remove deep local cards instead of canonicalizing them.

## Decision

Normalize every discovered `AGENTS.md` card into the canonical shape and set
`config/agents_mesh.json` `migration_allowed` to `false`.

The generated mesh should report all cards as canonical and zero migration
cards. Future migration status is allowed only as an explicit, temporary
exception with a named cleanup route.

## Rationale

The mesh is most useful when every local card has the same minimum handoff
shape: scope, role, read order, boundaries, validation, and closeout.

Keeping migration open after the known cards are normalized would blur future
reviews: a newly noncanonical card could look like old tolerated debt. Closing
the migration lane makes drift fail loudly while preserving the ability to
record a deliberate temporary exception if a future route genuinely needs one.

Removing deep cards would reduce count but also erase useful local risk at
mechanic parts, generated-support helpers, and technique trunks.

## Consequences

- Low-context agents can expect the same minimum route shape everywhere in the
  mesh.
- `generated/agents_mesh.min.json` is now a zero-migration companion mirror.
- New durable districts should land with canonical `AGENTS.md` cards or an
  explicit exemption; migration is no longer the default escape hatch.
- The tradeoff is stricter review: temporary noncanonical cards now require a
  deliberate decision or review note before landing.

## Source surfaces

- `DESIGN.AGENTS.md`
- `docs/guardrails/AGENTS_MESH_PROTOCOL.md`
- `docs/guardrails/AGENTS_MESH_INDEX.md`
- `config/agents_mesh.json`
- `generated/agents_mesh.min.json`
- `scripts/validate_agents_md_shape.py`
- `scripts/validate_agents_mesh.py`
- `scripts/build_agents_mesh_index.py`
- `scripts/validate_agents_mesh_index.py`
- `tests/test_agents_mesh.py`

## Follow-up route

Revisit this decision if future repo growth needs a staged noncanonical card
again. That future change should name the temporary path, cleanup owner, and
validation route before re-enabling migration.

## Verification

The closure is validated by:

```bash
python scripts/validate_agents_md_shape.py
python scripts/validate_agents_mesh.py
python scripts/build_agents_mesh_index.py --check
python scripts/validate_agents_mesh_index.py
python scripts/validate_nested_agents.py
python scripts/release_check.py
```
