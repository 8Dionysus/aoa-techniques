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
2. Attach planning metadata such as `intent_type`, adapter identity, and traceability IDs.
3. Run a dry-run executor against the plan.
4. Emit `run.json`, `automation_plan.json`, and `chain_summary.json`.
5. Run a contract-check that validates expected routing and structural completeness.

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

## Traceability note

If the workflow requires `trace_id` or `intent_id`, the contract-check should fail when those fields are missing rather than silently downgrading traceability.
