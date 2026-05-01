# Distillation Active Parts Split

Date: 2026-05-01

## Status

Accepted

## Context

`mechanics/distillation/` had five flat active files carrying different jobs:
donor extraction law, import operation, external candidate accounting,
cross-layer candidate accounting, and long-gap reentry design. That shape kept
the material visible, but it did not match the mechanics topology now used for
larger practice-motion packages.

The project also needs to preserve the difference between active behavior and
source lineage. Distillation has candidate ledgers with historical seed and
sibling-repo evidence, but those sources should not be the only place current
behavior lives.

## Decision

Move the five flat Distillation docs into part-local active homes under
`mechanics/distillation/parts/`, and add route-local `AGENTS.md`,
`DIRECTION.md`, `PARTS.md`, `PROVENANCE.md`, `LANDING_LOG.md`, `ROADMAP.md`,
and `legacy/` accounting.

No candidate verdicts, ledger counts, or technique statuses are changed by this
split.

## Consequences

Distillation now has an active route that can grow one part at a time. Future
ledger compaction has a clear preservation path through `legacy/raw/`, and
entrypoint docs can route directly to the part that owns the current question.

The cost is path churn across repo docs, tests, quest routing, and recurrence
surfaces. The benefit is that distillation can now be refined like the Agon
mechanic without copying AoA center authority or treating historical donor
material as current law.
