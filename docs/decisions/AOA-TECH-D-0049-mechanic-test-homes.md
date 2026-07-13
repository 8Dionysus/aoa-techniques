# Mechanic Test Homes

Date: 2026-05-14

## Index Metadata

- Decision ID: AOA-TECH-D-0049
- Original date: 2026-05-14
- Surface classes: mechanic package, mechanic part
- Technique axes: mechanic bridge
- Mechanic parents: none
- Guard families: mechanic topology, part-local artifact
- Posture: accepted

## Context

Root `tests/` had become a warehouse for repo-wide validation and
mechanic-owned topology or contract suites.

That made the root test district look like it owned mechanic package shape,
Distillation tree-pilot evidence, Recurrence live receipt publishing,
Experience and Release-support contract packets, and cross-mechanics package
posture.

The stronger local pattern is the same one used by the AoA center repository:
root tests stay for root-owned gates, while mechanic-owned tests live beside the
mechanic they constrain.

## Decision

Keep root `tests/` for repo-wide validation:

- current direction and root README routing
- generated downstream feed contracts
- nested AGENTS validation
- roadmap parity
- root legacy topology
- `validate_repo.py` and semantic AGENTS regression coverage

Move mechanic-owned suites to owner homes:

- `mechanics/<slug>/tests/` for one mechanic package
- `mechanics/tests/` for mechanics-wide package standards, shared request
  receipts, shared legacy scaffolds, and cross-mechanic contract tests
- existing `mechanics/<slug>/parts/<part>/tests/` homes remain part-local

Add `scripts/run_tests.py` as the release-facing unittest entrypoint so the
release check can run root-owned and mechanic-owned unittest directories without
pulling the tests back into root.

## Consequences

- Root `tests/` is now a repo-wide validation district, not a mechanic test
  warehouse.
- Mechanic package tests are easier to find from the mechanic route cards and
  can move with their owners.
- Root-only test discovery is no longer the full repository unittest gate. Use
  the repository test runner for the full unittest suite.
- `scripts/release_check.py` calls the new runner, preserving release coverage.

## Verification

Verification was routed through the targeted owner checks and repository validation lanes.
