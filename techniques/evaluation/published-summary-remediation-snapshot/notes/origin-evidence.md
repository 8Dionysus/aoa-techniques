# Origin Evidence

## Technique
- id: AOA-T-0008
- name: published-summary-remediation-snapshot

## Source project
- name: atm10-agent
- source files:
  - `docs/DECISIONS.md`
  - `docs/RUNBOOK.md`
  - `docs/SESSION_2026-03-12.md`
  - `docs/SESSION_2026-03-13.md`

## Evidence
- `docs/DECISIONS.md` records a read-only remediation helper that aggregates only latest published summaries such as `readiness`, `governance`, `progress`, and `transition`, and states explicitly that it does not recompute history.
- The same source records a deterministic bucket policy with fixed bucket names and an explicit maximum of 5 candidate items so nightly triage stays reviewable.
- `docs/RUNBOOK.md` defines the helper contract and policy surface as `report_only|fail_if_remediation_required`, including the rule that `fail_if_remediation_required` trips on broken required sources or non-empty remediation backlog.
- `docs/RUNBOOK.md` also records the workflow behavior: the nightly workflow runs the helper in `report_only` mode and publishes `runs/nightly-gateway-sla-remediation/remediation_summary.json`.
- `docs/SESSION_2026-03-12.md` treats that workflow-published remediation summary as the nightly source-of-truth and describes direct local helper execution as a fallback path.
- `docs/SESSION_2026-03-13.md` shows the snapshot as a live triage surface with a bounded candidate set, concrete bucket output, and preserved reason-code reporting.

## Interpretation
- The origin proves this technique as an active published-summary rollup, not just as an abstract helper outline: it is documented in policy, executed in workflow, and consumed in live operator triage.
