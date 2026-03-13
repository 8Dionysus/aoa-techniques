---
id: AOA-T-0006
name: latest-alias-plus-history-copy
domain: evaluation
status: promoted
origin:
  project: atm10-agent
  path: docs/RUNBOOK.md
  note: Derived from a real summary pipeline that writes a stable latest alias plus a nested history copy and uses anti-double-count readers for collectors and review surfaces.
owners:
  - 8Dionysus
tags:
  - evaluation
  - summaries
  - history
  - contracts
summary: Dual-write summary pattern that keeps a stable latest alias, preserves nested history, and prevents double-count accumulation.
---

# latest-alias-plus-history-copy

## Intent

Keep machine-readable summaries easy to discover for consumers while also preserving a trustworthy run-by-run history that scanners can accumulate without double-counting.

## When to use

- summary-producing checks need one stable consumer-facing path
- history collectors or trend scanners need per-run rows
- review surfaces need both latest state and historical accumulation
- the project is introducing history retention without breaking existing consumers

## When not to use

- summaries are purely ephemeral and no latest or history contract is needed
- consumers already address immutable per-run objects directly and do not need an alias
- the project cannot keep reader behavior explicit when both alias and history are present

## Inputs

- one machine-readable summary payload
- one stable latest alias path
- one per-run directory
- reader logic that scans history for accumulation

## Outputs

- stable latest alias for the newest summary
- nested history copy under `run_dir`
- path metadata linking both outputs when producers emit paths
- reader behavior that avoids alias plus history double-counting

## Core procedure

1. Define one stable latest alias path for the current summary.
2. Create a per-run directory for each execution.
3. Write the same summary payload to the latest alias and to a history copy under `run_dir`.
4. Expose both paths in artifact metadata when the producer emits path fields such as `summary_json` and `history_summary_json`.
5. Make collectors scan nested history copies first when building accumulation or trends.
6. Allow fallback to the top-level latest alias only for legacy layouts where no history rows exist yet.
7. If the pattern is introduced as a hotfix, start valid accumulation from the first dual-write run instead of inventing backfill.

## Contracts

- the latest alias path is stable and consumer-facing
- the history copy lives under `run_dir`
- the history copy path differs from the latest alias path
- schema and status match between latest alias and history copy
- readers avoid double-counting by preferring nested history rows
- fallback behavior is explicit and limited to legacy layouts without history rows
- if path metadata is emitted, it matches the actual file layout

## Risks

- latest alias and history copy can drift if only one path is updated
- collectors can silently double-count if they read both alias and nested rows as independent runs
- ad hoc backfill can corrupt accumulation windows if older single-write runs are mixed with dual-write runs without policy

## Validation

Verify the technique by confirming that:
- the latest alias exists at the stable expected path
- the history copy exists under `run_dir`
- the history copy differs from the latest alias
- emitted `summary_json` and `history_summary_json` fields match real files when present
- schema and status match between the alias and history copy
- collectors ignore the alias when nested history rows are available
- fallback to latest alias happens only when no nested rows exist

See `checks/dual-write-history-checklist.md`.

## Adaptation notes

What can vary across projects:
- summary filenames
- run directory naming conventions
- whether `run.json` is emitted alongside the summary
- local filesystem, object-store, or equivalent alias and history layouts
- explicit backfill policies for migrations

What should stay invariant:
- one stable latest alias exists for consumers
- one nested history copy exists for accumulation
- readers prefer nested history rows
- fallback behavior is explicit instead of accidental

## Public sanitization notes

ATM10-specific gateway names, nightly workflow names, UTC guardrail details, and repo-specific run roots were removed. The public version keeps only the reusable dual-write and anti-double-count pattern for machine-readable summaries.

## Example

See `examples/minimal-latest-history-layout.md`.

## Checks

See `checks/dual-write-history-checklist.md`.

## Promotion history

- born in `atm10-agent`
- validated through dual-write summary producers, nested-history-first collectors, and integrity checks over alias and history invariants
- promoted to `aoa-techniques` on 2026-03-13

## Future evolution

- add a companion technique for integrity checks over published summary layouts
- add an adaptation example for object-store backed artifacts
- add guidance for safe migration from single-write to dual-write history
