# Origin Evidence

## Technique
- id: AOA-T-0003
- name: contract-first-smoke-summary

## Source project
- name: atm10-agent
- source files:
  - `atm10-agent/docs/DECISIONS.md`
  - `atm10-agent/docs/RUNBOOK.md`
  - `atm10-agent/docs/SESSION_2026-03-12.md`
  - `atm10-agent/docs/SESSION_2026-03-13.md`

## Evidence
- `atm10-agent/docs/DECISIONS.md` records that the repository standardized a machine-readable summary layer for non-automation smoke with `scripts/collect_smoke_run_summary.py` and one `smoke_summary.json` contract instead of relying on console output.
- The same source records reuse of the same contract-first pattern across multiple smoke families: gateway smoke publishes `gateway_smoke_summary.json`, gateway HTTP smoke publishes `gateway_http_smoke_summary.json`, and Streamlit smoke publishes `streamlit_smoke_summary_v1`.
- `atm10-agent/docs/RUNBOOK.md` lists concrete smoke commands with stable `--summary-json` surfaces and expected artifact paths for phase, retrieval, automation contract, gateway, gateway HTTP, SLA, and Streamlit smoke flows.
- `atm10-agent/docs/SESSION_2026-03-12.md` records a live Streamlit smoke run on the normal summary path with the schema left unchanged, showing that the published summary contract stayed stable while the surrounding implementation evolved.
- `atm10-agent/docs/SESSION_2026-03-13.md` states explicitly that the green verdict is determined by `streamlit_smoke_summary_v1` rather than by debug process-exit details, confirming summary-first acceptance behavior.
- the same origin surfaces show multiple downstream consumers of the same summary contract: CI verdicts, operator-facing review paths, and agent-readable structured outputs all depend on the emitted summaries rather than on log scraping
- together these sources show the pattern as the default producer layer once a smoke family needs one reusable acceptance surface for more than one consumer

## Interpretation
- The origin proves this technique as a reusable producer-layer contract over multiple smoke families and consumers: summaries are standardized, discoverable, and treated as the default acceptance surface for downstream CI, operators, and agents before storage, rollout, or remediation helpers are added.
