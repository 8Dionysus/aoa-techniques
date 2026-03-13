# Origin Evidence

## Technique
- id: AOA-T-0010
- name: telemetry-integrity-snapshot

## Source project
- name: atm10-agent
- source files:
  - `docs/DECISIONS.md`
  - `docs/RUNBOOK.md`
  - `docs/SESSION_2026-03-12.md`
  - `docs/SESSION_2026-03-13.md`

## Evidence
- `docs/DECISIONS.md` records a dedicated integrity layer that checks required source health, telemetry counters, dual-write consistency, anti-double-count rules, and optional UTC-guardrail consistency.
- The same source states that the integrity layer is strictly diagnostic and does not add a new hard fail surface beyond the already active strict trend gate.
- `docs/SESSION_2026-03-12.md` records the published artifact layout explicitly: latest alias `runs/nightly-gateway-sla-integrity/integrity_summary.json` plus a nested history copy in the timestamped run directory.
- The same session note lists the exact invariant families checked by the helper: required source health, `invalid_or_mismatched_count == 0`, dual-write and anti-double-count checks, and optional cadence/UTC consistency.
- `docs/RUNBOOK.md` defines the helper contract as `report_only`, records the expected sources, and keeps the integrity snapshot as a workflow-published artifact rather than an implicit side effect.
- `docs/SESSION_2026-03-13.md` shows the integrity snapshot as a live machine-readable source with `integrity_status=clean`, `telemetry_ok=true`, `dual_write_ok=true`, and `anti_double_count_ok=true`, while remaining separate from enforcement decisions.

## Interpretation
- The origin shows this technique as a diagnostic trust check over published summaries: it validates whether downstream rollups can be trusted without itself becoming the next enforcement gate.
