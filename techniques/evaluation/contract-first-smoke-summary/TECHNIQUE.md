---
id: AOA-T-0003
name: contract-first-smoke-summary
domain: evaluation
status: canonical
origin:
  project: atm10-agent
  path: docs/RUNBOOK.md
  note: Derived from a real repository pattern where runnable smoke entrypoints emit machine-readable summaries consumed by CI, UI, and agents.
owners:
  - 8Dionysus
tags:
  - evaluation
  - smoke
  - contracts
  - ci
summary: Runnable smoke pattern where each smoke path emits a machine-readable summary that becomes the primary validation contract.
maturity_score: 5
rigor_level: strict
reversibility: moderate
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-15
export_ready: true
relations:
  - type: used_together_for
    target: AOA-T-0006
  - type: used_together_for
    target: AOA-T-0007
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# contract-first-smoke-summary

## Intent

Make smoke checks reviewable, automatable, and reusable by treating the machine-readable summary as the default producer-layer contract instead of relying on console text alone.

## When to use

- repositories with runnable smoke scripts or operational probes
- CI pipelines that need stable pass or fail signals
- local operator tools or dashboards that consume validation results
- agent workflows that need structured outputs instead of log scraping
- cases where one bounded smoke or probe path should publish the same acceptance surface for CI, operators, and agents before any storage/history or gate-promotion layer is added

## When not to use

- one-off manual checks with no need for repeatability
- cases where a full test suite already provides the only required contract surface
- checks that cannot produce any stable artifact or status signal

## Inputs

- a runnable smoke entrypoint
- expected output artifacts
- explicit success and failure conditions
- one stable summary output path or `--summary-json` surface

## Outputs

- smoke run artifacts
- one machine-readable summary file
- explicit `ok` or `error` status
- enough observed fields to support basic diagnosis

## Core procedure

1. Define the smoke entrypoint and the scenario it is meant to validate.
2. Define the expected artifacts the smoke run should create.
3. Emit a stable machine-readable summary file such as `summary.json`, `smoke_summary.json`, or `contract_summary.json`.
4. Make exit behavior explicit:
   - return `0` when the summary contract is satisfied
   - return non-zero when the contract fails
5. Wire the same summary into CI reports, artifact uploads, local dashboards, or agent surfaces.
6. Preserve summary writing on failure whenever possible so diagnosis does not depend on raw logs alone.

## Contracts

- each smoke path produces one machine-readable summary
- the summary contains an explicit success or error status
- the summary contains enough observed data to diagnose basic failures
- the summary path is stable, either by convention or via a stable `--summary-json` flag
- exit code aligns with summary status
- console output may help humans, but it is not the primary contract surface
- this technique owns the producer contract only; storage/history, staged enforcement, and downstream rollups remain separate adjacent techniques

## Risks

### Failure modes

- summaries collapse to a bare `error` signal without enough observed context to diagnose what failed
- summary shape changes too often and breaks downstream consumers that expect a stable contract

### Negative effects

- over-minimal summaries push humans back toward manual debugging even when the machine-readable path exists
- pressure-driven fallback to raw logs can become sticky and weaken the producer contract over time

### Misuse patterns

- treating summary generation as optional and falling back to log parsing under pressure
- changing filenames, fields, or status semantics without a bounded compatibility plan

### Detection signals

- downstream consumers start scraping console logs again instead of reading the summary artifact
- repeated failures show `error` with too little observed data to explain the problem quickly

### Mitigations

- keep one stable machine-readable summary path and evolve schema deliberately rather than casually
- require summary generation on every run path possible, including failure paths whenever the process can still write output

## Validation

Verify the technique by confirming that:
- the summary file is always written on success and is written on failure whenever possible
- the summary is valid machine-readable JSON
- status in the summary matches the process exit behavior
- a downstream consumer can read the summary without scraping console logs

See `checks/summary-contract-checklist.md`.
For source-backed origin evidence and bounded second-context reinforcement, see `notes/origin-evidence.md` and `notes/second-context-adaptation.md`.

## Adaptation notes

What can vary across projects:
- summary filenames
- run directory layout
- domain-specific observed fields
- additional contract-check layers
- downstream consumers such as CI, dashboards, local tools, or agents

Project-shaped details that should not be treated as invariant:
- exact smoke family names such as phase, retrieval, gateway, or Streamlit
- whether some smoke paths publish `smoke_summary.json` while others publish `contract_summary.json`
- exact artifact upload grouping or step-summary presentation in CI
- exact schema names or observed fields used by one repository

What should stay invariant:
- one machine-readable summary per smoke path
- explicit status and outcome semantics
- stable summary discovery
- no dependence on raw logs as the only source of truth

Relationship to adjacent techniques: this technique produces the machine-readable summaries that `latest-alias-plus-history-copy` later stabilizes for history consumers and that `signal-first-gate-promotion` later uses for staged enforcement.

## Public sanitization notes

Project-specific workflow names, run directory conventions, threshold values, and ATM10-specific scenarios were removed. The published version keeps the reusable pattern: runnable smoke entrypoints, structured summaries, and explicit contract-based pass or fail behavior.

## Example

See `examples/minimal-smoke-summary-flow.md`.

## Checks

See `checks/summary-contract-checklist.md`.

## Promotion history

- born in `atm10-agent`
- validated across multiple smoke paths that publish structured summary artifacts for CI and operator use
- promoted to `aoa-techniques` on 2026-03-13
- approved for `canonical` in `aoa-techniques` on 2026-03-16 after stronger multi-family producer evidence, bounded second-context reinforcement, and a fresh public-safety recheck

## Future evolution

- add an adaptation example from a non-Python repository
- add optional guidance for backward-compatible summary evolution
- add a variant for long-running smoke families that publish richer diagnostic envelopes
