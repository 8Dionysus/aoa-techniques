# AGENTS.md

## Applies to

This card applies to `.agents/` and all descendants unless a nearer
`AGENTS.md` narrows the path.

## Role

`.agents/` holds agent-facing companion lanes for `aoa-techniques`.

It can expose practice-canon help to local agents, but it does not author
technique meaning, skill workflow meaning, proof authority, route dispatch, or
runtime state.

## Read before editing

Read root `AGENTS.md`, `DESIGN.AGENTS.md`,
`docs/guardrails/AGENTS_MESH_PROTOCOL.md`, and the nearest lane card before
changing files here.

For Codex Spark work, also read `.agents/spark/README.md`,
`.agents/spark/registry.json`, and the chosen scenario `README.md` plus
`PROMPT.md`.

For exported skill-like material, also read `techniques/AGENTS.md`,
`TECHNIQUE_INDEX.md`, and the source `TECHNIQUE.md` bundle that produced the
agent-facing companion.

## Boundaries

- Do not turn exported technique guidance into an `aoa-skills` skill bundle.
- Do not hand-edit generated or exported companion content as the first move.
- Do not make agent lanes stronger than the source technique, docs, schemas,
  builders, or owning AoA repository.
- Do not add private project assumptions, secrets, local host paths, or hidden
  capability claims.

## Validation

Run the smallest covering checks:

```bash
python scripts/validate_agents_md_shape.py
python scripts/validate_agents_mesh.py
python .agents/spark/scripts/validate_spark_lane.py
python -m unittest discover -s .agents/spark/tests -p 'test*.py'
python scripts/validate_semantic_agents.py
python scripts/validate_repo.py
```

For broad agent-lane or generated-surface changes, run:

```bash
python scripts/release_check.py
```

## Closeout

Report changed agent lanes, source technique or builder surfaces consulted,
generated or exported companions rebuilt or left untouched, validation run,
validation skipped, and any remaining migration-card risk.
