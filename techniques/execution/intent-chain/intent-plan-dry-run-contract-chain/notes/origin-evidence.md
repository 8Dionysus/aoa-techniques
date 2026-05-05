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
- `atm10-agent/docs/SESSION_2026-02-23.md` records the incremental build-up of the chain in `M6.3`, `M6.4`, `M6.6`, and `M6.7`: first the intent-to-plan adapter, then the unified dry-run chain entrypoint, then the contract checker, then machine-readable `summary_json` output.
- The same session log lists the artifact contract explicitly for the unified chain: `run.json`, `chain_summary.json`, `automation_plan.json`, and `child_runs/*`, plus local validation that both `dry_run` and `intent_chain` contract modes return `status=ok`.
- `atm10-agent/docs/RUNBOOK.md` makes the chain public and repeatable: `M6.3` keeps the adapter dry-run only, `M6.4` documents the unified chain, and `M6.6` defines concrete contract-check commands and machine-readable `contract_summary.json` output.
- `atm10-agent/docs/DECISIONS.md` formalizes the same layers as explicit policy rather than ad hoc commands: adapter output is an `automation_plan_v1` artifact, the chain writes linkable artifacts, and the checker is the CI contract surface.
- `atm10-agent/docs/SESSION_2026-02-24.md` records the stronger planning metadata envelope in `automation_plan_v1`: `intent_type`, `intent_schema_version`, `adapter_name`, `adapter_version`, and propagated `intent_id/trace_id`.
- The same 2026-02-24 sources record the strict traceability hardening: `check_automation_smoke_contract.py` writes `trace_id` and `intent_id` into `summary_json.observed`, and missing required IDs are treated as contract violations with non-zero exit.

## Interpretation
- The origin proves this technique as a real artifact-first safety chain, not just a naming convention: intent is normalized into a plan artifact, executed only in dry-run, summarized through explicit chain artifacts, and gated by a machine-readable contract result before any real execution path is considered.
