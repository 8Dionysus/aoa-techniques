# Minimal Context Report For CI

Use one small CI report that describes source coverage and token drift without trying to fix anything.

## Report

```md
# Context Composition Report

- sources expected: 4
- sources covered: 4
- token estimate: 1,280
- token delta from baseline: +3%
- composition checks: pass
- notes:
  - no missing fragments
  - no provider/runtime telemetry included
```

## What this proves

- the report stays read-only
- source coverage is visible
- token drift is visible
- the report does not become the composition engine or a remediation snapshot
