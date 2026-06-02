# Validation Lane Command Authority

Status: accepted
Date: 2026-06-02

## Index Metadata

- Decision ID: AOA-TECH-D-0066
- Original date: 2026-06-02
- Surface classes: validation guard, release/tooling, GitHub workflow, docs route
- Technique axes: validation lane
- Mechanic parents: release-support
- Guard families: CI lane, release/tooling, generated/read-model, docs route
- Posture: accepted

## Context

`aoa-techniques` had accumulated a release-facing validation posture where
GitHub `Repo Validation` called `scripts/release_check.py` directly and
`scripts/release_check.py` stored the full command sequence inline.

That made the release gate the default PR and moving-main gate, and it made a
Python tuple act as hidden command authority. The shape was workable while the
repo was small, but it blurred growth validation, generated projection checks,
release stabilization, and documentation guidance.

## Options considered

1. Keep `scripts/release_check.py` as both the CI gate and the inline command
   sequence owner.
2. Move only GitHub workflow YAML to a smaller command while keeping release
   command authority inside `scripts/release_check.py`.
3. Put blocking lane command sequences in `config/validation_lanes.json`, load
   them through `scripts/validation_lanes.py`, execute CI lanes through
   `scripts/ci_gate.py`, and keep `scripts/release_check.py` as the release
   entrypoint and stabilizer.

## Decision

Use `config/validation_lanes.json` as the canonical command storage surface for
blocking validation lanes:

- `source-fast` protects the current growth gate: route/topology plus fast
  authored technique source contracts.
- `generated` protects generated projection parity on moving `main`.
- `release` protects the full release-prep path.

`scripts/validation_lanes.py` is a loader/API. `scripts/ci_gate.py` executes
lane modes for CI. `scripts/release_check.py` remains the release entrypoint and
worktree stabilizer, but it asks the loader for the `release` lane instead of
owning a duplicate command sequence.

GitHub `Repo Validation` calls the `source-fast` lane for PRs and moving
`main`, with the `generated` parity lane on `main` pushes.

## Rationale

This keeps authored technique and route surfaces separate from generated
projection checks and release-freeze behavior. It also gives future validator
splits a stable place to add or move command ownership without editing workflow
YAML, root route cards, and release helper internals in parallel.

The release entrypoint stays familiar and keeps its stabilization behavior, but
the lane command sequence becomes inspectable config rather than script literal
history.

## Consequences

- PR validation no longer treats the full release-prep gate as the default
  growth gate.
- The growth gate now includes `scripts/validate_source_contracts.py`, which
  checks authored technique contracts without generated freshness.
- Active docs and route cards should name lane IDs, local focused checks, or
  entrypoints rather than copying full command sequences.
- Tests must guard that workflows call lane entrypoints and that
  `release_check.py` reads the lane manifest.
- The current `source_fast` lane is intentionally bounded to source/topology:
  it checks AGENTS route law and authored technique source contracts, but not
  generated projections.

## Source surfaces

- `.github/workflows/repo-validation.yml`
- `.github/workflows/release-audit.yml`
- `.github/workflows/nightly-sentinel.yml`
- `config/validation_lanes.json`
- `scripts/validation_lanes.py`
- `scripts/ci_gate.py`
- `scripts/validate_source_contracts.py`
- `scripts/release_check.py`
- `docs/RELEASING.md`
- `docs/validation/VALIDATOR_TOPOLOGY.md`
- `docs/validation/COMMAND_AUTHORITY.md`
- `docs/validation/validator_inventory.json`
- `AGENTS.md`
- `tests/test_validate_repo_ci_release_authority.py`
- `tests/test_validate_repo_generated_drift.py`
- `tests/test_validation_command_authority.py`

## Follow-up route

Do not widen `source_fast` by adding generated builders. Future source-only
checks may join the lane when they validate authored source, schemas, or route
topology without projection freshness.

## Verification

Current verification route:

- `source-fast` lane for growth-safe source/route-card and authored technique
  source-contract checks.
- `generated` lane for projection parity.
- `release` lane for release-prep stabilization.
- `tests/AGENTS.md` focused checks for test-topology and command-authority
  guardrails.

Exact command storage remains in `config/validation_lanes.json` and
`docs/validation/COMMAND_AUTHORITY.md`.
