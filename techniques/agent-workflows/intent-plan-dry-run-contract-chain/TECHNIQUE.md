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
maturity_score: 4
rigor_level: strict
reversibility: moderate
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-15
export_ready: true
relations:
  - type: complements
    target: AOA-T-0001
  - type: used_together_for
    target: AOA-T-0005
evidence:
  - kind: support_note
    path: notes/bounded-transfer.md
  - kind: origin_evidence
    path: notes/origin-evidence.md
---

# intent-plan-dry-run-contract-chain

## Intent

Turn high-level intent into a traceable, reviewable, dry-run-only chain that emits explicit artifacts and a contract verdict before any real execution path is allowed.

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
- an adapter or normalizer that turns intent into a plan artifact
- a dry-run-only executor
- a contract-check step that reads produced artifacts and emits a machine-readable verdict

## Outputs

- normalized plan artifact with routing metadata
- dry-run execution artifacts
- chain summary or equivalent linking intent, plan, and dry-run artifacts
- machine-readable contract summary suitable for CI or operator review

## Core procedure

1. Define a stable intent payload that expresses what should happen at a high level.
2. Normalize the intent into a plan and attach planning metadata such as intent type, schema version, adapter identity, and optional traceability IDs.
3. Persist the normalized plan as an artifact before any dry-run execution happens.
4. Run a dry-run-only executor against the normalized plan and preserve the resulting artifacts.
5. Emit explicit chain artifacts such as `run.json`, plan output, and chain summary so the path can be reviewed without log scraping.
6. Run a contract-check over those artifacts and publish a machine-readable summary before any real execution path is considered.

## Contracts

- the adapter does not perform real input events or equivalent side effects
- the planning step emits a plan artifact before dry-run execution begins
- the normalized plan carries workflow metadata such as intent type, schema version, adapter identity, and optional traceability IDs
- the execution step remains dry-run only
- chain artifacts are explicit enough for downstream checks to read them directly
- contract-check validates expected intent type or equivalent routing plus minimum structural completeness
- contract summary exposes an explicit pass or fail verdict and observed routing or traceability data when available
- failure behavior is explicit and stops progression to any real execution path

## Risks

- false confidence if dry-run artifacts look complete but do not reflect real execution constraints
- metadata drift between intent, normalized plan, and contract-check layers
- overfitting the chain to one project's payload shape or artifact naming
- treating CI table layout or exact thresholds as the technique instead of the chain contract

## Validation

Verify the technique by confirming that:
- the intent payload is accepted or rejected by explicit normalization rules
- the normalized plan is written as an artifact before dry-run validation
- the dry-run step performs no real side effects
- chain artifacts can be traced across adapter, dry-run, and contract-check stages
- contract-check output is machine-readable and can fail the workflow on structural or routing violations
- required traceability fields are surfaced or rejected explicitly according to policy

See `checks/chain-contract-checklist.md`.
For source-backed origin evidence and transfer boundaries, see `notes/origin-evidence.md` and `notes/bounded-transfer.md`.

## Adaptation notes

What can vary across projects:
- intent schema names
- plan schema names
- artifact filenames
- whether trace or intent IDs are optional or required
- dry-run engines and downstream validators
- whether the review surface is CI, an operator dashboard, or a local approval loop

Project-shaped details that should not be treated as invariant:
- exact ATM10 commands, scripts, and workflow filenames
- exact artifact filenames such as `chain_summary.json` or `automation_plan.json`
- exact thresholds such as minimum action count or minimum step count
- whether traceability IDs are optional metadata or strict required fields
- whether the dry-run chain targets UI automation, API orchestration, or another domain
- exact CI summary tables or artifact-upload conventions around the chain

What should stay invariant:
- intent is normalized before execution
- the plan artifact exists before dry-run execution
- dry-run happens before any real action path
- chain artifacts are explicit
- contract-check validates the produced artifacts rather than relying on logs alone
- a failing contract result blocks progression to real execution

Relationship to adjacent techniques:
- `AOA-T-0001 plan-diff-apply-verify-report` governs how changes to this chain should be planned, verified, and reported safely.
- `AOA-T-0005 new-intent-rollout-checklist` extends this technique when one new intent is added to an existing chain without bypassing its contracts.

## Public sanitization notes

ATM10-specific intent names, UI coordinates, fixture payload details, exact workflow wiring, and project run naming were removed. The published version preserves only the reusable chain pattern: intent input, normalized plan artifact, dry-run artifacts, and contract validation.

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
- add a second-context note from a non-automation repository that still uses the same artifact-first contract
