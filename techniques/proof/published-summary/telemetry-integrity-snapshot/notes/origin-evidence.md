# Origin Evidence

## Technique
- id: AOA-T-0010
- name: telemetry-integrity-snapshot

## Source project
- name: atm10-agent
- source files:
  - `.github/workflows/gateway-sla-readiness-nightly.yml`
  - `docs/DECISIONS.md`
  - `docs/MANIFEST.md`
  - `docs/README.md`
  - `docs/RUNBOOK.md`
  - `docs/SESSION_2026-03-12.md`
  - `docs/SESSION_2026-03-13.md`
  - `tests/test_check_gateway_sla_fail_nightly_integrity.py`
  - `tests/test_gateway_sla_readiness_nightly_workflow.py`
  - `tests/test_run_gateway_sla_operating_cycle.py`
  - `tests/test_streamlit_operator_panel.py`
  - `tests/test_streamlit_operator_panel_smoke.py`

## Evidence
- `docs/DECISIONS.md` records a dedicated integrity layer that checks required source health, telemetry counters, dual-write consistency, anti-double-count rules, and optional UTC-guardrail consistency.
- The same source states that the integrity layer is strictly diagnostic and does not add a new hard fail surface beyond the already active strict trend gate.
- `.github/workflows/gateway-sla-readiness-nightly.yml` and `tests/test_gateway_sla_readiness_nightly_workflow.py` show the integrity snapshot as a workflow-published artifact with explicit summary path and summary-section wiring.
- `docs/SESSION_2026-03-12.md` records the published artifact layout explicitly: latest alias `runs/nightly-gateway-sla-integrity/integrity_summary.json` plus a nested history copy in the timestamped run directory.
- The same session note lists the exact invariant families checked by the helper: required source health, `invalid_or_mismatched_count == 0`, dual-write and anti-double-count checks, and optional cadence/UTC consistency.
- `docs/RUNBOOK.md` defines the helper contract as `report_only`, records the expected sources, and keeps the integrity snapshot as a workflow-published artifact rather than an implicit side effect.
- `docs/SESSION_2026-03-13.md` shows the integrity snapshot as a live machine-readable source with `integrity_status=clean`, `telemetry_ok=true`, `dual_write_ok=true`, and `anti_double_count_ok=true`, while remaining separate from enforcement decisions and feeding local operating-cycle interpretation.
- `tests/test_check_gateway_sla_fail_nightly_integrity.py` treats the integrity snapshot as a first-class contract with explicit happy-path and attention-path cases over telemetry, dual-write, anti-double-count, and UTC guardrail checks.
- `tests/test_streamlit_operator_panel.py` and `tests/test_streamlit_operator_panel_smoke.py` show a separate downstream consumer path where Streamlit reads the integrity snapshot as an optional published source without embedding the trust logic directly in the UI.
- `tests/test_run_gateway_sla_operating_cycle.py` shows another non-UI consumer path where the operating-cycle helper uses `integrity_status` to decide whether telemetry repair should outrank remediation backlog interpretation.
- `README.md` and `MANIFEST.md` describe the integrity snapshot as part of the public monitoring surface, reinforcing that one published trust verdict serves more than one bounded consumer.

## Interpretation
- The origin shows this technique as a diagnostic trust check over published summaries: it validates whether downstream rollups can be trusted without itself becoming the next enforcement gate, and it already serves multiple bounded consumers instead of forcing each consumer to re-implement trust logic.
