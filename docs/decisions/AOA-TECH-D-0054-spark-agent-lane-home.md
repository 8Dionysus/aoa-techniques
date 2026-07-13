# Spark Agent Lane Home

Status: accepted
Date: 2026-05-14

## Index Metadata

- Decision ID: AOA-TECH-D-0054
- Original date: 2026-05-14
- Surface classes: agent route
- Technique axes: agent mesh
- Mechanic parents: none
- Guard families: AGENTS/mesh
- Posture: accepted

## Context

The repository root still had a `Spark/` directory with a local Spark lane
route card and swarm recipe.

That material is agent-facing operating guidance, not a public root entry
surface, technique doctrine, mechanic part, or generated reader surface. The
root already has `.agents/` as the agent district, and keeping a separate
capitalized `Spark/` directory at root weakens the same root-topology cleanup
used elsewhere in the AoA workspace.

## Options

- Keep `Spark/` at root as a special-case lane.
- Move the files under a mechanic package.
- Move the lane under `.agents/spark/`, keeping its local `AGENTS.md` and
  `SWARM.md` guidance.

## Decision

Move the Spark lane to:

```text
.agents/spark/
```

Keep the lane subordinate to root `AGENTS.md`. The lane may guide fast-loop
Spark work, but it does not own repository identity, public technique canon,
mechanic routes, validation law, or sibling-owner meaning.

## Consequences

- The repository root no longer has a standalone `Spark/` lane directory.
- Agent-lane materials are grouped under `.agents/`, matching the repository's
  agent district shape.
- Spark guidance remains available for bounded technique-editing loops without
  becoming a root public surface.

## Verification

Expected checks:

Verification was routed through the targeted owner checks and repository validation lanes.
