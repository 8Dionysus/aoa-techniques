# Concrete Non-UI Intent Chain

This example shows a public-safe non-UI dry-run chain for a repository-maintenance action: refreshing a generated skill index without letting the refresh step perform real writes before the contract is satisfied.

## Input intent

```json
{
  "schema_version": "skill_ops_intent_v1",
  "intent_type": "refresh_skill_index",
  "intent_id": "intent-refresh-skill-index-001",
  "trace_id": "trace-refresh-skill-index-001",
  "goal": "rebuild the generated skill index from skill metadata and preview the resulting changes"
}
```

## Normalized plan artifact

The adapter writes one plan artifact before dry-run execution:

```json
{
  "plan_version": "automation_plan_v1",
  "intent_type": "refresh_skill_index",
  "adapter_name": "skill_ops_adapter",
  "adapter_version": "2026-03-19",
  "trace_id": "trace-refresh-skill-index-001",
  "intent_id": "intent-refresh-skill-index-001",
  "steps": [
    {
      "kind": "inspect",
      "target": "skills/",
      "purpose": "collect skill metadata and current index state"
    },
    {
      "kind": "dry_run_generate",
      "target": "SKILL_INDEX.md",
      "purpose": "render the next index body without writing it"
    },
    {
      "kind": "contract_check",
      "target": "runs/refresh-skill-index/contract_summary.json",
      "purpose": "verify artifacts, routing, and traceability"
    }
  ]
}
```

## Dry-run artifacts

The dry-run path writes explicit artifacts instead of relying on logs:

- `automation_plan.json`
- `run.json`
- `chain_summary.json`
- `contract_summary.json`
- `render_preview.md`
- `predicted_diff.json`

That artifact family lets a reviewer confirm what the refresh would change without letting the refresh step update `SKILL_INDEX.md` yet.

## Contract summary

```json
{
  "status": "ok",
  "observed": {
    "intent_type": "refresh_skill_index",
    "trace_id": "trace-refresh-skill-index-001",
    "intent_id": "intent-refresh-skill-index-001",
    "predicted_targets": [
      "SKILL_INDEX.md"
    ]
  },
  "violations": []
}
```

## What this proves

- the repository-maintenance action is expressed as intent first rather than as an ad hoc script invocation
- the plan artifact exists before any dry-run execution begins
- the dry-run result is reviewable through artifacts such as `render_preview.md` and `predicted_diff.json`
- the contract-check can fail on routing or traceability problems before any real write path is considered

## Failure signals to preserve

- If `automation_plan.json` is missing, the contract should fail rather than infer success from a printed command line.
- If the dry-run path writes `SKILL_INDEX.md` directly, the preview step has violated the technique and should fail.
- If `trace_id` or `intent_id` disappear between intent and contract summary, the contract should record that explicitly.
- If the predicted target set expands beyond the bounded maintenance surface, the contract should fail rather than silently widen the action.
