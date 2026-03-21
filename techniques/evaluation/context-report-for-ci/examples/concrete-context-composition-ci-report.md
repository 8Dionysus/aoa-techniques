# Concrete Context Composition CI Report

This example shows a CI job reporting on a composed context after fragment assembly completed elsewhere.

## Inputs

- expected source list:
  - `docs/agent-guidance.md`
  - `docs/selection-rules.md`
  - `docs/validation-notes.md`
- observed composed artifact:
  - one markdown context bundle emitted by the build step
- token baseline:
  - one previously recorded estimate for the same bundle shape

## Report

```md
# Context Composition CI Report

## Source coverage

- expected sources: 3
- observed sources: 3
- missing sources: none

## Token drift

- baseline tokens: 1,040
- observed tokens: 1,118
- delta: +7.5%

## Composition checks

- fragment ordering: pass
- source traceability: pass
- provider/runtime telemetry: not included

## Follow-up

- review the fragment set if the drift exceeds the current CI threshold
```

## What this proves

- the CI artifact is a report about composition, not the composition engine
- source coverage and token drift stay bounded and reviewable
- follow-up remains a separate decision outside the report surface
