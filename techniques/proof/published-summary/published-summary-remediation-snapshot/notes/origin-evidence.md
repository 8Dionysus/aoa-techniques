# Origin Evidence

## Technique
- id: AOA-T-0008
- name: published-summary-remediation-snapshot

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
  - `tests/test_gateway_sla_readiness_nightly_workflow.py`
  - `tests/test_run_gateway_sla_operating_cycle.py`
  - `tests/test_streamlit_operator_panel.py`
  - `tests/test_streamlit_operator_panel_smoke.py`

## Evidence
- `docs/DECISIONS.md` records a read-only remediation helper that aggregates only latest published summaries such as `readiness`, `governance`, `progress`, and `transition`, and states explicitly that it does not recompute history.
- The same source records a deterministic bucket policy with fixed bucket names and an explicit maximum of 5 candidate items so nightly triage stays reviewable.
- `docs/RUNBOOK.md` defines the helper contract and policy surface as `report_only|fail_if_remediation_required`, including the rule that `fail_if_remediation_required` trips on broken required sources or non-empty remediation backlog.
- `.github/workflows/gateway-sla-readiness-nightly.yml` and `tests/test_gateway_sla_readiness_nightly_workflow.py` show the snapshot as a workflow-published artifact with explicit source-of-truth path `runs/nightly-gateway-sla-remediation/remediation_summary.json`.
- `docs/SESSION_2026-03-12.md` treats that workflow-published remediation summary as the nightly source-of-truth and records Streamlit `Latest Metrics` visibility as a separate downstream consumer surface.
- `docs/SESSION_2026-03-13.md` shows the snapshot as a live triage surface with a bounded candidate set, concrete bucket output, preserved reason-code reporting, and local operating-cycle use.
- `tests/test_streamlit_operator_panel.py` and `tests/test_streamlit_operator_panel_smoke.py` treat the remediation snapshot as a first-class published contract for tolerant UI loading rather than as incidental helper output.
- `tests/test_run_gateway_sla_operating_cycle.py` shows a second non-UI consumer path: the local operating-cycle helper reads the remediation snapshot to drive triage interpretation and next-action hints.
- `README.md` and `MANIFEST.md` describe the remediation snapshot as part of the public-facing monitoring surface, which reinforces that one published backlog serves more than one bounded consumer.

## Interpretation
- The origin proves this technique as an active published-summary rollup, not just as an abstract helper outline: it is documented in policy, published by workflow, and consumed by multiple bounded downstream surfaces such as nightly triage, Streamlit visibility, and local operating-cycle interpretation.
