---
id: AOA-T-0032
name: context-report-for-ci
domain: evaluation
kind: validation
status: promoted
origin:
  project: agents-md
  path: README.md
  note: Adapted from the open-source agents-md project, which uses composable markdown fragments and CI-facing reports to observe context coverage and drift.
owners:
  - 8Dionysus
tags:
  - evaluation
  - ci
  - context-composition
  - reporting
  - source-coverage
summary: Emit CI-facing reports for context composition, source coverage, token-estimate drift, and related composition checks without turning the report surface into the composition technique itself.
maturity_score: 3
rigor_level: bounded
reversibility: moderate
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-21
export_ready: true
relations:
  - type: complements
    target: AOA-T-0012
evidence:
  - kind: external_origin
    path: notes/external-origin.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: external_review
    path: notes/external-import-review.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# context-report-for-ci

## Intent

Produce a bounded CI-facing report that tells reviewers how well a composed context covered its expected sources, how much token-estimate drift appeared, and whether any composition-related check needs follow-up.

## When to use

- CI jobs that need one readable report about context composition health
- repositories that want source coverage and token drift visible without opening the composition engine itself
- checks that should observe context assembly quality while leaving remediation decisions to another surface
- workflows where the main need is reporting on composition, not performing composition

## When not to use

- when the main task is deterministic context composition itself
- when the task is to create a remediation snapshot over published summaries
- when the task needs provider/runtime telemetry, product-wide monitoring, or generalized observability
- when the report would become a hidden policy engine instead of a bounded CI artifact

## Inputs

- one composed or assembled context artifact
- source coverage signals or fragment inventory
- token estimates for the composed artifact
- one CI-facing execution point that can emit the report

## Outputs

- one CI-readable report describing source coverage and drift
- one bounded view of token-estimate changes or mismatches
- one place to see composition-related warnings without opening the composition engine
- a clear handoff to the next review or remediation step when the report finds a problem

## Core procedure

1. Read the composed context artifact and the source list that was supposed to feed it.
2. Compare the expected source coverage with the actual coverage.
3. Compare expected token estimates with the observed estimate or delta.
4. Report composition-related gaps in a read-only CI-facing format.
5. Keep the report focused on observation and comparison rather than repair instructions.
6. Hand off any fix decision to the appropriate follow-up technique or review surface.

## Contracts

- the report stays read-only and CI-facing
- source coverage is visible without exposing the composition engine as the technique
- token-estimate drift is reported as a bounded comparison, not as a runtime optimization policy
- the technique complements `AOA-T-0012` rather than replacing it
- the report does not become a generic remediation snapshot doctrine
- provider or runtime telemetry remains outside the contract

Relationship to adjacent techniques: unlike `AOA-T-0012`, this technique does not compose the context itself; it reports on how well composition covered its sources and whether drift appeared. Unlike `AOA-T-0008`, it does not aggregate published summaries into a remediation snapshot; it stays tied to CI-facing context-composition reporting.

## Risks

### Failure modes

- the report starts acting like a hidden remediation engine instead of a read-only CI view
- source coverage becomes too abstract to confirm whether the composed context actually matched its inputs
- token drift is reported without enough context to decide whether the gap matters

### Negative effects

- a strong report can tempt teams to treat the report itself as proof that composition was correct
- over-reporting can make CI noisy enough that the signal gets ignored
- a context report can drift into general observability if it starts collecting runtime telemetry or provider details

### Misuse patterns

- turning the report into the composition step itself
- widening the report into remediation snapshot doctrine or generalized monitoring
- adding provider/runtime telemetry to make the report feel more complete

### Detection signals

- reviewers have to read the composition engine to understand the report
- the report begins prescribing fixes instead of describing coverage and drift
- the CI output starts collecting broad runtime telemetry unrelated to context composition

### Mitigations

- keep the report read-only and limit it to source coverage, token drift, and composition-related checks
- split any remediation guidance into a separate review or fix technique
- keep provider/runtime telemetry outside this contract

## Validation

Verify the technique by confirming that:
- the CI output is readable without inspecting the composition engine
- source coverage is visible and bounded
- token-estimate drift is visible and bounded
- the report stays read-only and does not prescribe remediation
- the report does not become provider/runtime telemetry or a remediation snapshot

See `checks/context-report-for-ci-checklist.md`.

## Adaptation notes

What can vary across projects:
- the CI runner or report-emission command
- the exact source inventory format
- the token-estimate source
- the surface that consumes the report

What should stay invariant:
- the technique stays read-only and CI-facing
- the report describes composition quality rather than performing composition
- source coverage and token drift remain explicit
- the report stays subordinate to the composition technique it observes

Project-shaped details that should not be treated as invariant:
- remediation snapshot doctrine
- provider-specific telemetry
- runtime-wide observability
- build-system internals

## Public sanitization notes

This import narrows the donor repository to one bounded pattern: a CI-facing report about context composition, source coverage, and token-estimate drift. Fragment assembly mechanics, remediation-snapshot doctrine, provider/runtime telemetry, and broader observability breadth were intentionally left out of the public technique contract.

## Example

See `examples/minimal-context-report-for-ci.md` and `examples/concrete-context-composition-ci-report.md`.

## Checks

See `checks/context-report-for-ci-checklist.md`.

## Promotion history

- adapted from open-source `agents-md`
- promoted into `aoa-techniques` on 2026-03-21 as a bounded evaluation import for CI-facing context-composition reporting

## Future evolution

- split out a dedicated source-coverage sibling if that signal becomes reusable without the rest of the context report
- split out a dedicated token-drift sibling if token comparison proves reusable across multiple CI surfaces
- add a stronger second live context if another public repository emits the same kind of CI-facing context report
