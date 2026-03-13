---
id: AOA-T-0003
name: contract-first-smoke-summary
domain: evaluation
status: promoted
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
---

# contract-first-smoke-summary

## Intent

Make smoke checks reviewable, automatable, and reusable by treating the machine-readable summary as the primary contract instead of relying on console text alone.

## When to use

- repositories with runnable smoke scripts or operational probes
- CI pipelines that need stable pass or fail signals
- local operator tools or dashboards that consume validation results
- agent workflows that need structured outputs instead of log scraping

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

## Risks

- creating overly shallow summaries that say `error` without useful context
- changing summary shape too often and breaking downstream consumers
- treating summary generation as optional and falling back to log parsing under pressure

## Validation

Verify the technique by confirming that:
- the summary file is always written on success and is written on failure whenever possible
- the summary is valid machine-readable JSON
- status in the summary matches the process exit behavior
- a downstream consumer can read the summary without scraping console logs

See `checks/summary-contract-checklist.md`.

## Adaptation notes

What can vary across projects:
- summary filenames
- run directory layout
- domain-specific observed fields
- additional contract-check layers
- downstream consumers such as CI, dashboards, local tools, or agents

What should stay invariant:
- one machine-readable summary per smoke path
- explicit status and outcome semantics
- stable summary discovery
- no dependence on raw logs as the only source of truth

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

## Future evolution

- add an adaptation example from a non-Python repository
- add a companion technique for summary history plus latest-alias patterns
- add optional guidance for backward-compatible summary evolution
