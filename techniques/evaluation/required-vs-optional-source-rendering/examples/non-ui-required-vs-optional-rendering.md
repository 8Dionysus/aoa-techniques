# non-ui-required-vs-optional-rendering

This example shows the same required-versus-optional policy in a machine-readable CLI or smoke report rather than a UI panel.

## Required sources

- `published/nightly-readiness/latest/summary.json`
- `published/nightly-governance/latest/summary.json`
- `published/nightly-transition/latest/summary.json`

If one of these is missing or invalid, the strict contract fails.

## Optional sources

- `published/nightly-remediation/latest/summary.json`
- `published/nightly-integrity/latest/summary.json`
- `published/nightly-operating-cycle/latest/summary.json`

If one of these is missing, the report still renders and records the absence explicitly.

## Example report

```json
{
  "status": "ok",
  "required_missing_sources": [],
  "optional_missing_sources": [
    "published/nightly-remediation/latest/summary.json"
  ],
  "warnings": [
    "optional source published/nightly-remediation/latest/summary.json not available yet"
  ]
}
```

## Staged promotion rule

If `published/nightly-integrity/latest/summary.json` later becomes required, that change should happen through an explicit contract update, a staged rollout, and an updated required-source list. It should not silently stop being optional because one consumer started to rely on it.
