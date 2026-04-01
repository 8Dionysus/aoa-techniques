# AGENTS.md

Guidance for coding agents and humans working under `techniques/evaluation/`.

## Purpose

This domain stores reusable evaluation and validation techniques.

Representative bundles here include `contract-test-design`, `property-invariants`, `signal-first-gate-promotion`, `telemetry-integrity-snapshot`, `contract-first-smoke-summary`, and `upstream-skill-health-checking`.

## Domain rules

Keep the proof posture explicit. These techniques should help a reader bound what is being checked, how evidence is gathered, and how a gate is interpreted.
Preserve clear distinction between a reusable evaluation technique here and a repository-owned proof surface in `aoa-evals`.
When a technique references gates or promotion, keep the signal weaker than the final repository policy it may later inform.

## Boundary

If the object becomes a concrete repository verdict contract or a specific eval bundle, route it to `aoa-evals` instead of widening this domain.
If it becomes a runtime workflow or operational runbook, route it to `aoa-skills` or the owning repository instead.

## Hard NO

Do not:

- overclaim that a technique itself proves quality
- hide required fixtures, baselines, or evidence dependencies
- collapse evaluation technique meaning into one repo-specific scoreboard
- imply `aoa-evals` is optional when the real object under change is a bounded proof surface

## Validation

After changing an evaluation technique, run:

- `python -m pip install -r requirements-dev.txt`
- `python scripts/validate_nested_agents.py`
- `python scripts/validate_repo.py`

Cross-check downstream implications in `aoa-evals` when the technique changes proof posture materially.
