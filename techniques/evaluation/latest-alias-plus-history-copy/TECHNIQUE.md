---
id: AOA-T-0006
name: latest-alias-plus-history-copy
domain: evaluation
status: canonical
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
maturity_score: 5
rigor_level: strict
reversibility: moderate
review_required: true
validation_strength: cross_context
public_safety_reviewed_at: 2026-03-15
export_ready: true
relations:
  - type: requires
    target: AOA-T-0003
  - type: used_together_for
    target: AOA-T-0007
  - type: shares_contract_with
    target: AOA-T-0008
  - type: shares_contract_with
    target: AOA-T-0010
evidence:
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: adverse_effects_review
    path: notes/adverse-effects-review.md
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

### Failure modes

- the latest alias and nested history copy drift because only one path is updated or one write quietly fails
- collectors silently double-count runs when they treat the latest alias and nested history rows as separate accumulation inputs
- ad hoc migration or backfill corrupts accumulation windows by mixing older single-write runs with dual-write history without an explicit cutoff

### Negative effects

- the dual-write layout adds storage and reader-policy complexity even when the summary payload itself stays simple
- teams can spend more time preserving path shape than checking whether accumulated history is still trustworthy
- a clean latest alias can create false-success by making the newest run look healthy while historical accumulation is already broken

### Misuse patterns

- treating the technique as a generic archival strategy instead of a bounded latest-plus-history contract for machine-readable summaries
- adding more alias layers, mirrors, or backfill passes instead of keeping one stable consumer path and one nested history copy
- assuming every reader may choose its own scan path instead of enforcing nested-history-first behavior explicitly

### Detection signals

- the latest alias and history copy disagree on schema, status, or reported paths
- trend or accumulation outputs jump unexpectedly after a migration even though recent run summaries look normal
- readers or review surfaces start reading both top-level alias data and nested history rows in the same accumulation path
- incident review keeps finding the newest summary quickly, but cannot reconcile it with recent historical totals or streaks

### Mitigations

- narrow the contract back to one stable alias path and one nested history copy, removing extra mirrors or unofficial scan targets
- make reader precedence explicit so nested history rows win whenever they exist and alias fallback stays limited to legacy layouts
- gate migrations with a clear first dual-write boundary instead of inventing retrospective backfill across incompatible eras
- stop expanding storage complexity when accumulation trust is unclear; re-establish alias/history parity before adding retention or archive variants

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
For source-backed origin evidence, see `notes/origin-evidence.md`.
For bounded second-context adaptation guidance, see `notes/second-context-adaptation.md`.
For canonical-prep readiness, see `notes/canonical-readiness.md`.

## Adaptation notes

What can vary across projects:
- summary filenames
- run directory naming conventions
- whether `run.json` is emitted alongside the summary
- local filesystem, object-store, or equivalent alias and history layouts
- explicit backfill policies for migrations

Project-shaped details that should not be treated as invariant:
- exact run-directory naming patterns and timestamp formats
- whether producers emit both `summary_json` and `history_summary_json` path fields
- whether the first adopter is a nightly checker, a smoke helper, or another summary producer
- the exact retention window or cache wiring around the latest and history layout

What should stay invariant:
- one stable latest alias exists for consumers
- one nested history copy exists for accumulation
- readers prefer nested history rows
- fallback behavior is explicit instead of accidental

Relationship to adjacent techniques: this technique stores the summaries produced by `contract-first-smoke-summary` in a latest-plus-history layout that `signal-first-gate-promotion` can accumulate without double-counting.
Within the published-summary package, it is also the storage contract that `AOA-T-0008` and `AOA-T-0010` assume when they read stable latest aliases without turning the alias itself into history.

## Public sanitization notes

ATM10-specific gateway names, nightly workflow names, UTC guardrail details, and repo-specific run roots were removed. The public version keeps only the reusable dual-write and anti-double-count pattern for machine-readable summaries.

## Example

See `examples/minimal-latest-history-layout.md` and `examples/object-store-latest-history-layout.md`.

## Checks

See `checks/dual-write-history-checklist.md`.

## Promotion history

- born in `atm10-agent`
- validated through dual-write summary producers, nested-history-first collectors, and integrity checks over alias and history invariants
- promoted to `aoa-techniques` on 2026-03-13
- approved as `canonical` in `aoa-techniques` on 2026-03-15 after fresh public-safety review and default-use confirmation

## Future evolution

- add guidance for safe migration from single-write to dual-write history
- add retention-policy examples for teams that expire history rows aggressively
