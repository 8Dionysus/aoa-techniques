---
id: AOA-T-0004
name: intent-plan-dry-run-contract-chain
domain: agent-workflows
status: promoted
origin:
  project: atm10-agent
  path: docs/RUNBOOK.md
  note: Derived from a real automation workflow where intent payloads are normalized into traceable plans, validated through dry-run, and enforced by contract checks.
owners:
  - 8Dionysus
tags:
  - agent-workflow
  - automation
  - dry-run
  - traceability
summary: Safe workflow that normalizes intent into a traceable plan, validates it with dry-run, and enforces contract checks before any real execution path exists.
---

# intent-plan-dry-run-contract-chain

## Intent

Turn high-level intent into a traceable, reviewable, non-executing automation path before any real action is allowed.

## When to use

- automation systems that start from intent-like inputs
- agent workflows that need a reviewable planning layer before execution
- teams that want dry-run-first automation with explicit artifacts
- systems where traceability matters across adapter, planner, and validator steps

## When not to use

- simple scripts that do not need an intent abstraction
- systems that already execute real actions directly without a dry-run safety layer
- workflows where no stable artifacts or contract checks are required

## Inputs

- a stable intent payload
- an adapter or normalizer that turns intent into a plan
- a dry-run-only executor
- a contract-check step for produced artifacts

## Outputs

- normalized plan artifact
- dry-run execution artifacts
- chain summary or equivalent linking artifacts together
- contract-check result suitable for CI or operator review

## Core procedure

1. Define a stable intent payload that expresses what should happen at a high level.
2. Normalize the intent into a plan and attach planning metadata such as intent type, schema version, adapter identity, and optional traceability IDs.
3. Run a dry-run-only executor against the normalized plan.
4. Emit explicit chain artifacts such as `run.json`, plan output, and chain summary.
5. Run a contract-check over the produced artifacts.
6. Wire the contract result into CI, dashboards, or operator review surfaces before any real execution path is considered.

## Contracts

- the adapter does not perform real input events or equivalent side effects
- the normalized plan carries workflow metadata such as intent type, schema version, adapter identity, and optional traceability IDs
- the execution step remains dry-run only
- chain artifacts are explicit and linkable
- contract checks validate expected intent type or equivalent routing and minimum structural completeness
- exit behavior is explicit and reviewable

## Risks

- false confidence if dry-run artifacts look complete but do not reflect real execution constraints
- metadata drift between intent, normalized plan, and contract-check layers
- overfitting the chain to one project's payload shape

## Validation

Verify the technique by confirming that:
- the intent payload is accepted or rejected by explicit normalization rules
- the normalized plan is written as an artifact before dry-run validation
- the dry-run step performs no real side effects
- chain artifacts can be traced across adapter, dry-run, and contract-check stages
- contract-check output can fail the workflow on structural or routing violations

See `checks/chain-contract-checklist.md`.
For source-backed origin evidence, see `notes/origin-evidence.md`.

## Adaptation notes

What can vary across projects:
- intent schema names
- plan schema names
- artifact filenames
- whether trace or intent IDs are optional or required
- dry-run engines and downstream validators

Project-shaped details that should not be treated as invariant:
- exact artifact filenames such as `chain_summary.json` or `automation_plan.json`
- whether traceability IDs are optional metadata or strict required fields
- whether the dry-run chain targets UI automation, API orchestration, or another domain
- exact CI summary tables or artifact-upload conventions around the chain

What should stay invariant:
- intent is normalized before execution
- dry-run happens before any real action path
- chain artifacts are explicit
- contract-check validates the produced artifacts rather than relying on logs alone

Relationship to adjacent techniques: this technique is the core intent -> plan -> dry-run -> contract chain that `new-intent-rollout-checklist` extends when one new intent is added safely.

## Public sanitization notes

ATM10-specific intent names, UI coordinates, fixture payload details, and project-specific run naming were removed. The published version preserves only the reusable chain pattern: intent input, normalized plan, dry-run artifacts, and contract validation.

## Example

See `examples/minimal-intent-chain.md`.

## Checks

See `checks/chain-contract-checklist.md`.

## Promotion history

- born in `atm10-agent`
- validated through adapter, dry-run chain, contract-check, and regression-test layers
- promoted to `aoa-techniques` on 2026-03-13

## Future evolution

- add examples from a non-UI automation system
- add guidance for partial rollout where some intents still use legacy validation paths
- add optional guidance for compatibility evolution across intent and plan schemas
