# AGENTS Mesh Index

## Current Mesh

The AGENTS mesh gives durable work districts local route cards while keeping
root law at the root and source truth in its owner surface.

## Core Surfaces

| Surface | Role |
|---|---|
| `DESIGN.AGENTS.md` | root design form for agent-facing guidance |
| `AGENTS.md` | root route and boundary card |
| `docs/guardrails/AGENTS_MESH_PROTOCOL.md` | mesh law and growth contract |
| `config/agents_mesh.json` | source configuration for canonical cards, migration posture, and validation commands |
| `generated/agents_mesh.min.json` | compact machine-facing mirror |
| `scripts/validate_agents_md_shape.py` | card shape validator |
| `scripts/validate_agents_mesh.py` | coverage and mesh config validator |
| `scripts/build_agents_mesh_index.py` | generated mesh builder |
| `scripts/validate_agents_mesh_index.py` | generated mesh validator |

## Growth Posture

A new durable district should never be a silent room. Give it a card, route it
to a stronger owner, or mark it as temporary. The mesh should make agent work
safer by making local authority and local limits visible.

## Migration Posture

The generated mirror currently reports zero migration cards. All discovered
cards are canonical, and `config/agents_mesh.json` keeps migration disabled.

If a future change needs temporary migration status, make the exception
explicit, name the cleanup route, and restore the zero-migration posture before
it becomes background debt.

## Release Posture

The mesh checks are part of `scripts/release_check.py`.

If a durable directory is added, removed, or re-scoped, update
`config/agents_mesh.json`, the nearest local `AGENTS.md`, and
`generated/agents_mesh.min.json` together.
