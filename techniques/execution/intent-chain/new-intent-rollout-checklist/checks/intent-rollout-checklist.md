# intent-rollout-checklist

- canonical fixture exists for the new intent path
- fixture includes required traceability fields when policy requires them
- dedicated smoke path exists for the new intent
- smoke path uses the shared intent-chain flow rather than a one-off shortcut
- contract-check asserts the expected intent type
- strict traceability flags are enabled when policy requires them
- machine-readable summary is produced and published
- the new intent appears in the same review surface as existing intent paths
- artifact paths match between smoke and contract-check steps
- regression test exists for the new intent rollout
- rollout remains dry-run only
