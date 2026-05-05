# minimal-required-vs-optional-rendering

This example shows a summary-driven operator surface with strict base data and tolerant enrichments.

## Required sources

- `runs/ci-smoke-phase-a/smoke_summary.json`
- `runs/ci-smoke-retrieve/smoke_summary.json`
- `runs/ci-smoke-eval/smoke_summary.json`

If one of these is missing, the smoke contract fails.

## Optional sources

- `runs/nightly-progress/progress_summary.json`
- `runs/nightly-remediation/remediation_summary.json`
- `runs/nightly-integrity/integrity_summary.json`
- `runs/nightly-operating-cycle/operating_cycle_summary.json`

If one of these is missing, the panel still renders and shows `not available yet`.

## Soft-info artifact

- `runs/nightly-operating-cycle/triage_brief.md`

If this file is absent while the main summary JSON exists, the surface shows the JSON-backed block normally and treats the missing brief as soft-info rather than warning or error.

## Example smoke summary fields

```json
{
  "status": "ok",
  "missing_sources": [],
  "required_missing_sources": [],
  "optional_missing_sources": [
    "runs/nightly-remediation/remediation_summary.json"
  ],
  "errors": []
}
```

## Rendering rule

Optional-source tolerance is allowed only when the base required surface is still trustworthy. It is not a license to downgrade real hard failures into warnings.
