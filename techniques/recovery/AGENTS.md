# AGENTS.md

Guidance for coding agents and humans working under `techniques/recovery/`.

## Purpose

`recovery/` stores technique bundles whose primary placement question is how
reviewed failure, drift, degradation, or repair pressure becomes bounded,
reviewable recovery work without turning into vague self-improvement or hidden
mutation.

This is a tree trunk, not a frontmatter domain. Technique bundles here may keep
their existing `domain` and `kind` values when the reviewed move is only path
architecture.

## Current scope

Accepted pilot shelves:

- `diagnosis-repair/`: turns reviewed friction into drift taxonomy, diagnosis,
  repair-shape, and checkpoint-bound repair posture while keeping each leaf
  technique separate
- `antifragility-recovery/`: degraded continuation, isolated service stop,
  stress receipt closeout, and receipt-first failure analysis under bounded
  recovery pressure while preserving validation-shaped leaves

## Domain rules

Keep the recovery object explicit:

- what reviewed evidence or diagnosis starts the recovery move
- what remains read-only assessment versus bounded repair planning
- what mutation, approval, rollback, or health-check posture remains visible
- what owner-law, proof-law, role-law, scenario rollout, or runtime doctrine is
  refused

Do not turn a recovery technique into a live self-modifying loop, generic
governance framework, incident-response playbook, role contract, proof verdict,
runtime self-healing, service catalog owner, generic resilience platform, or
broad improvement doctrine.

## Boundary

Use `docs/TECHNIQUE_TREE_CONTRACT.md` before adding another shelf here.

Do not add `tree_path` frontmatter merely because a bundle lives under this
trunk. Do not rename trunks or shelves without a reviewed projection and a
bounded migration receipt.

## Validation

After changing recovery techniques, run:

- `python scripts/validate_nested_agents.py`
- `python scripts/validate_repo.py`

Run `python scripts/release_check.py` when generated catalogs or reader
surfaces changed.
