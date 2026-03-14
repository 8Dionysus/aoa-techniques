# Minimal Intent Chain

This example shows a generic automation chain that turns high-level intent into a dry-run-only validation path.

## Input intent

```json
{
  "schema_version": "example_intent_v1",
  "intent_type": "open_status_panel",
  "goal": "open the status panel and inspect current state",
  "intent_id": "intent-001",
  "trace_id": "trace-001"
}
```

## Flow

1. Normalize the intent into a plan artifact.
2. Attach planning metadata such as `intent_type`, adapter identity, schema version, and traceability IDs.
3. Persist the plan artifact before running any dry-run executor.
4. Run a dry-run executor against the plan.
5. Emit `run.json`, `automation_plan.json`, and `chain_summary.json`.
6. Run a contract-check that validates expected routing, structural completeness, and any required traceability fields.

## Expected artifacts

The minimum artifact set should make the chain reviewable without log scraping:

- `automation_plan.json` or equivalent normalized plan artifact
- `run.json` or equivalent dry-run record
- `chain_summary.json` or equivalent linking artifact
- `contract_summary.json` or equivalent machine-readable contract verdict

## Contract-check summary

```json
{
  "ok": true,
  "status": "ok",
  "observed": {
    "intent_type": "open_status_panel",
    "trace_id": "trace-001",
    "intent_id": "intent-001"
  },
  "violations": []
}
```

## Failure signals to preserve

- If `automation_plan.json` is missing, the contract-check should fail rather than infer success from logs.
- If `intent_type` does not match the expected route, the contract summary should record that mismatch explicitly.
- If the workflow requires `trace_id` or `intent_id`, the contract-check should fail when those fields are missing rather than silently downgrading traceability.
- A passing dry-run is not enough by itself; the chain should still require an explicit contract verdict before any real execution path is enabled.

## Traceability note

If the workflow requires `trace_id` or `intent_id`, the contract-check should surface them in the machine-readable summary so CI or operator review can correlate the run without opening raw logs.
