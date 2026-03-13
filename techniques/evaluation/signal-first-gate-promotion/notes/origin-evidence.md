# Origin Evidence

## Technique
- id: AOA-T-0007
- name: signal-first-gate-promotion

## Source project
- name: atm10-agent
- source files:
  - `atm10-agent/docs/DECISIONS.md`
  - `atm10-agent/docs/RUNBOOK.md`
  - `atm10-agent/docs/SESSION_2026-03-02.md`
  - `atm10-agent/docs/SESSION_2026-03-03.md`
  - `atm10-agent/docs/SESSION_2026-03-12.md`
  - `atm10-agent/docs/SESSION_2026-03-13.md`

## Evidence
- `atm10-agent/docs/DECISIONS.md` records the baseline gate policy as `signal_only`, with an explicit opt-in `fail_nightly` mode for stricter enforcement rather than an implicit widening of the fail surface.
- The same source records the staged decision path in order: readiness stays `report_only`, governance turns history into explicit `go|hold`, progress reports the remaining gap, and transition tracks strict-switch telemetry.
- `atm10-agent/docs/DECISIONS.md` also fixes the narrow enforcement surface as `nightly_only`, keeps `pytest.yml` in `signal_only`, and later records the manual nightly strict override without converting the telemetry layers into hidden runtime gating.
- `atm10-agent/docs/RUNBOOK.md` defines the exit behavior for `signal_only`, `fail_nightly`, `report_only`, and `fail_if_not_go`, and documents the published artifact and summary surfaces for readiness, governance, and progress.
- `atm10-agent/docs/SESSION_2026-03-02.md` records governance rollout as staged instrumentation with no hard-gate switch yet, while still publishing workflow artifacts and keeping `pytest.yml` observational.
- `atm10-agent/docs/SESSION_2026-03-03.md` records the post-switch policy explicitly: enforcement remains only in the nightly workflow, while `readiness`, `governance`, `progress`, and `transition` continue as telemetry and reason-code layers for triage.
- `atm10-agent/docs/SESSION_2026-03-12.md` and `atm10-agent/docs/SESSION_2026-03-13.md` show that diagnostics continue to publish after strict nightly operation through missing-safe summary sections, remediation and integrity layers, and live `hold` snapshots with preserved reason codes.

## Interpretation
- The origin proves this technique as a real staged-promotion pattern: one signal starts observational, gains explicit decision telemetry, and only then moves into a narrowly scoped strict surface while published diagnostics stay intact.
