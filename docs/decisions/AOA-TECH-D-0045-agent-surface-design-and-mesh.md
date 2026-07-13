# Decision Note: Agent Surface Design And Mesh

Status: accepted
Date: 2026-05-14

## Index Metadata

- Decision ID: AOA-TECH-D-0045
- Original date: 2026-05-14
- Surface classes: agent route
- Technique axes: agent mesh
- Mechanic parents: none
- Guard families: AGENTS/mesh
- Posture: accepted

## Context

`Agents-of-Abyss` already uses root `DESIGN.md`, `DESIGN.AGENTS.md`, and many
local `AGENTS.md` cards as a layered agent-surface mesh.

`aoa-techniques` had many useful local cards, but they were not yet tied to a
repo-local design surface, generated coverage mirror, or validator-backed
migration posture. Copying the center repo wording directly would blur the
practice-canon owner boundary; leaving the cards as prose-only route hints
would make future growth hard to audit.

## Options considered

1. Keep the existing local cards as prose-only route hints.
2. Copy the `Agents-of-Abyss` agent-surface wording directly.
3. Adapt the AoA pattern into a repo-local design surface, mesh protocol,
   config, generated mirror, validators, and tests.

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

## Rationale

The agent-surface mesh is useful only if it is local to the practice-canon
boundary. Directly copying center law would make `aoa-techniques` sound like it
owned AoA center doctrine. Leaving the cards unregistered would hide the
migration debt and make future directory growth hard to review.

The chosen path keeps the design, route law, guardrail protocol, config,
generated mirror, and validators distinct. That mirrors the AoA pattern while
preserving the stronger local truth: techniques define practice meaning,
mechanics move candidates and evidence, and generated mirrors stay subordinate.

## Consequences

- New durable districts should add a local `AGENTS.md`, a deliberate migration
  or exemption entry, or proof that the directory is temporary.
- Agent guidance now has an explicit source/design/validation route instead of
  only local prose.
- Generated mesh output is a companion mirror only. It does not author
  technique meaning or override source docs.
- The remaining deep-card normalization debt is visible rather than hidden.

## Source surfaces

- `DESIGN.md`
- `DESIGN.AGENTS.md`
- `AGENTS.md`
- `docs/ROOT_SURFACE_LAW.md`
- `docs/guardrails/AGENTS_MESH_PROTOCOL.md`
- `docs/guardrails/AGENTS_MESH_INDEX.md`
- `config/agents_mesh.json`
- `generated/agents_mesh.min.json`
- `scripts/validate_agents_md_shape.py`
- `scripts/validate_agents_mesh.py`
- `scripts/build_agents_mesh_index.py`
- `scripts/validate_agents_mesh_index.py`

## Follow-up route

Revisit this decision if `DESIGN.AGENTS.md` starts duplicating root
`AGENTS.md`, if migration cards stop being visible in the generated mirror, or
if agent guidance begins absorbing technique, skill, eval, memory, runtime,
role, playbook, routing, KAG, stats, or ToS owner truth.

## Verification

The mesh route is validated by:

Verification was routed through the targeted owner checks and repository validation lanes.

`scripts/release_check.py` includes the same mesh checks.
