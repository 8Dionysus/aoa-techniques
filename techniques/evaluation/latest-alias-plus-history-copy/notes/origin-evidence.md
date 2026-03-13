# Origin Evidence

## Technique
- id: AOA-T-0006
- name: latest-alias-plus-history-copy

## Source project
- name: atm10-agent
- source files:
  - `atm10-agent/docs/DECISIONS.md`
  - `atm10-agent/docs/RUNBOOK.md`
  - `atm10-agent/docs/SESSION_2026-03-12.md`
  - `atm10-agent/docs/SESSION_2026-03-13.md`

## Evidence
- `atm10-agent/docs/DECISIONS.md` records the first history-friendly upgrade as `scripts/check_gateway_sla.py --runs-dir`, where the checker writes a timestamped run plus a nested history copy without changing the existing latest summary contract.
- The same source later fixes the dual-write pattern for nightly `readiness`, `governance`, `progress`, and `transition`: each run writes one top-level latest alias and one history copy under `run_dir/<summary>.json`.
- `atm10-agent/docs/DECISIONS.md` also records the collector rule directly: when history copies exist, readers must exclude the top-level latest alias from history scans, with fallback to the alias only for legacy layouts that do not have history rows yet.
- `atm10-agent/docs/RUNBOOK.md` defines the consumer-facing layout explicitly, including named latest aliases, timestamped history rows, and path metadata such as `paths.summary_json` and `paths.history_summary_json`.
- `atm10-agent/docs/SESSION_2026-03-12.md` records a live integrity snapshot with explicit latest alias and history copy paths and checks dual-write and anti-double-count invariants over `run_json` and `history_summary_json`.
- `atm10-agent/docs/SESSION_2026-03-13.md` shows that higher-level operator helpers read latest `readiness`, `governance`, `progress`, `transition`, `remediation`, `integrity`, and `cadence` summaries first and reuse those aliases when they are still fresh, proving the alias is a real consumer surface rather than a write-only convenience.

## Interpretation
- The origin shows this technique as a real storage and reader contract for published summaries: it keeps latest discovery simple, preserves run history, and makes collector behavior explicit enough to avoid silent double-count inflation.
