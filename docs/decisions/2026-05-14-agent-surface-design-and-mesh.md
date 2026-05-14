# Agent Surface Design And Mesh

Date: 2026-05-14

## Context

`Agents-of-Abyss` already uses root `DESIGN.md`, `DESIGN.AGENTS.md`, and many
local `AGENTS.md` cards as a layered agent-surface mesh.

`aoa-techniques` had many useful local cards, but they were not yet tied to a
repo-local design surface, generated coverage mirror, or validator-backed
migration posture. Copying the center repo wording directly would blur the
practice-canon owner boundary; leaving the cards as prose-only route hints
would make future growth hard to audit.

## Decision

Add repo-local design and mesh surfaces:

- `DESIGN.md` for the practice-canon system form
- `DESIGN.AGENTS.md` for the desired agent-facing surface form
- `docs/guardrails/AGENTS_MESH_PROTOCOL.md` for the checkable mesh contract
- `docs/guardrails/AGENTS_MESH_INDEX.md` for the human route to the mesh
- `config/agents_mesh.json` for canonical cards, migration posture, and
  validation commands
- `generated/agents_mesh.min.json` as the reproducible compact mirror
- validators and tests for card shape, top-level coverage, and generated
  freshness

The first canonical wave covers root and durable top-level districts. Existing
deep cards remain registered as `migration` in the generated mirror until a
later normalization pass lifts them into the full shape.

## Consequences

- New durable districts should add a local `AGENTS.md`, a deliberate migration
  or exemption entry, or proof that the directory is temporary.
- Agent guidance now has an explicit source/design/validation route instead of
  only local prose.
- Generated mesh output is a companion mirror only. It does not author
  technique meaning or override source docs.
- The remaining deep-card normalization debt is visible rather than hidden.

## Validation

The mesh route is validated by:

```bash
python scripts/validate_agents_md_shape.py
python scripts/validate_agents_mesh.py
python scripts/build_agents_mesh_index.py --check
python scripts/validate_agents_mesh_index.py
```

`scripts/release_check.py` includes the same mesh checks.
