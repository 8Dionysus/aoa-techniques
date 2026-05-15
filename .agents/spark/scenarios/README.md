# Spark Scenarios

Scenarios are session-contained operating recipes for Codex Spark.

Each scenario must let a Spark session finish inside its scope or leave a
portable handoff. Scenarios do not create new technique doctrine; they route
fast work through existing owner surfaces.

## Required Shape

Each scenario directory contains:

- `README.md`
- `PROMPT.md`
- `templates/result.md`
- `templates/handoff.md`
- `examples/result.example.md`

The canonical list of scenarios lives in [registry](../registry.json).

## Work Rule

Choose one scenario. Read its prompt. Finish as `done` or `handoff`.
