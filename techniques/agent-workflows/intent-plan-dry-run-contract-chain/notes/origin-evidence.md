# Origin Evidence

## Technique
- id: AOA-T-0004
- name: intent-plan-dry-run-contract-chain

## Source project
- name: atm10-agent
- source files:
  - `atm10-agent/docs/DECISIONS.md`
  - `atm10-agent/docs/RUNBOOK.md`
  - `atm10-agent/docs/SESSION_2026-02-23.md`
  - `atm10-agent/docs/SESSION_2026-02-24.md`

## Evidence
- `atm10-agent/docs/SESSION_2026-02-23.md` records the unified dry-run chain entrypoint `scripts/automation_intent_chain_smoke.py` and lists the artifact contract explicitly: `run.json`, `chain_summary.json`, `automation_plan.json`, and `child_runs/*`.
- The same session note records the contract-check layer `scripts/check_automation_smoke_contract.py` for `dry_run|intent_chain`, together with local validation that both modes produce `status=ok`.
- `atm10-agent/docs/SESSION_2026-02-24.md` records the planning metadata envelope in `automation_plan_v1`: `intent_type`, `intent_schema_version`, `adapter_name`, `adapter_version`, and propagated `intent_id/trace_id`.
- The same source also records that `check_automation_smoke_contract.py` writes `trace_id` and `intent_id` into `summary_json.observed`, with fallback recovery for `trace_id` in the intent-chain path.
- `atm10-agent/docs/DECISIONS.md` formalizes the planning metadata policy and the strict contract behavior: missing required `trace_id` or `intent_id` is treated as a contract violation with non-zero exit.
- `atm10-agent/docs/RUNBOOK.md` defines concrete smoke and contract-check commands for both `automation_dry_run` and `automation_intent_chain_smoke`, including machine-readable `contract_summary.json` output and explicit non-zero exit on contract violations such as missing artifacts, threshold failures, or expected-intent mismatch.

## Interpretation
- The origin proves this technique as a real safe-chain workflow: intent is normalized into a traceable plan, validated through dry-run, and enforced by explicit contract summaries before any real execution path is considered.
