# Spark Agent Lane Home

Status: accepted
Date: 2026-05-14

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

```bash
find . -maxdepth 1 -type d -name Spark -print
rg -n 'Spark/|\\.agents/spark' AGENTS.md README.md ROADMAP.md CHANGELOG.md docs .agents scripts tests
python scripts/validate_repo.py
python -m unittest discover -s tests
git diff --check
```
