---
id: AOA-T-0005
name: new-intent-rollout-checklist
domain: agent-workflows
kind: guardrail
status: promoted
origin:
  project: atm10-agent
  path: docs/RUNBOOK.md
  note: Derived from a real CI rollout policy for safely adding a new intent_type to a dry-run automation chain without contract drift.
owners:
  - 8Dionysus
tags:
  - agent-workflow
  - automation
  - rollout
  - dry-run
summary: Checklist for safely adding a new intent type to an intent-plan-dry-run chain without contract drift.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-20
export_ready: true
relations:
  - type: requires
    target: AOA-T-0004
  - type: complements
    target: AOA-T-0001
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: support_note
    path: notes/rollout-failure-triage.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# new-intent-rollout-checklist

## Intent

Extend an existing `intent -> plan -> dry-run -> contract-check` pipeline with one new `intent_type` without losing traceability, artifact consistency, or dry-run safety.

## When to use

- an automation chain already exists and the rollout is extending that shared chain, not redesigning it
- one new intent type needs a repeatable onboarding path
- CI or operator review depends on machine-readable summaries
- the team wants extension work to stay bounded and reviewable

## When not to use

- there is no stable intent-chain contract yet
- the rollout path performs real side effects before dry-run validation
- the system does not use fixtures, artifacts, or regression checks
- the team is trying to redesign the whole chain instead of extending an existing one safely
- the work is really about a new chain, a new execution mode, or broader workflow redesign rather than one bounded new intent

## Inputs

- an existing intent-chain workflow with normalization, dry-run, and contract-check steps already in place
- a canonical fixture location for new intent payloads
- a contract-check step that can assert expected routing
- CI or another review surface that publishes artifacts
- at least one regression surface that can prove the new intent uses the shared chain rather than a shortcut path

## Outputs

- one canonical fixture for the new intent
- one dedicated smoke path for the new intent rollout
- one machine-readable contract summary for the new intent path
- one published review surface that exposes the new intent path alongside existing intent paths
- at least one regression test covering the dry-run chain

## Core procedure

1. Add one canonical fixture for the new intent rollout.
2. Ensure the fixture includes traceability fields such as `intent_id` and `trace_id` when policy requires them.
3. Add a dedicated chain smoke step that runs the new fixture through the existing shared intent-to-plan-to-dry-run path.
4. Add a strict contract-check step with explicit `expected_intent_type`.
5. Publish the resulting contract summary and review row in the same surface humans and agents already use for the existing chain.
6. Add at least one regression test that exercises the dry-run chain for the new intent.

## Contracts

- one canonical fixture exists for each new intent rollout
- the rollout path stays dry-run only
- the rollout reuses the existing intent-chain path rather than introducing a parallel shortcut or a new chain
- contract-check validates expected intent routing
- machine-readable summary output is published
- artifact paths match between smoke and check steps
- traceability metadata is preserved when required by policy
- regression coverage proves the new intent works through the same chain contracts
- exit behavior is explicit on contract failure

## Risks

### Failure modes

- fixture drift makes the rollout look green while real inputs have already diverged
- intent routing regresses silently when contract checks stop asserting the expected type
- traceability fields disappear during normalization when the checklist is applied only partially
- artifact wiring drifts so the new intent runs correctly but disappears from the main review surface

### Negative effects

- a rollout can look complete on paper while operators still cannot see the new intent path in the published review surface
- one-off intent logic can fragment the shared chain and raise maintenance cost even before obvious failures appear

### Misuse patterns

- applying only the happy-path parts of the checklist and skipping fixture, traceability, or surface checks
- adding special-case intent logic that bypasses the shared chain while still labeling the rollout complete

### Detection signals

- canonical fixtures stop resembling the current intent contract or are not updated when intent shape changes
- the smoke path is green, but the main published review surface no longer shows the new intent artifacts

### Mitigations

- keep the canonical fixture current and preserve explicit type and traceability assertions in the contract checks
- require the new intent to stay on the shared chain and to appear on the same review surfaces and regression paths as existing intents

## Validation

Verify the technique by confirming that:
- the canonical fixture exists and matches the new intent contract
- the smoke path runs the new intent through the full dry-run chain
- contract-check produces a machine-readable summary and fails on routing drift
- artifact paths used by the smoke step and check step stay aligned
- the published review surface exposes the new intent path without log scraping
- at least one regression test covers the new intent rollout

See `checks/intent-rollout-checklist.md`.
For source-backed origin evidence and generalized triage guidance, see `notes/origin-evidence.md` and `notes/rollout-failure-triage.md`.

## Adaptation notes

What can vary across projects:
- fixture locations and naming conventions
- minimum action or step thresholds
- summary filenames
- whether `trace_id` and `intent_id` are optional or required
- CI systems and artifact publishing surfaces
- whether the review surface is fully automated CI, operator review, or a mixed approval loop
- whether the same published review surface is CI-only or also includes a compact operator handoff

Project-shaped details that should not be treated as invariant:
- exact fixture naming patterns such as `intent_<new_intent_type>.json`
- exact script names or workflow job names
- exact thresholds such as minimum action count or minimum step count
- exact CI summary-table names or artifact-upload labels
- whether one rollout example uses keyboard-only, pointer, API, or other dry-run actions

What should stay invariant:
- each new intent rollout has one canonical fixture
- rollout uses the existing shared dry-run chain rather than a parallel shortcut path or replacement chain
- contract-check asserts the expected routing explicitly
- rollout produces machine-readable output suitable for review
- rollout updates the same review surface and regression layer that existing intents already use

Relationship to adjacent techniques:
- `AOA-T-0004 intent-plan-dry-run-contract-chain` defines the underlying chain this checklist extends.
- `AOA-T-0001 plan-diff-apply-verify-report` governs how the rollout change itself should be planned, verified, and reported.

## Public sanitization notes

ATM10-specific intent names, fixture payload details, UI-specific behavior, workflow job names, and project run directory naming were removed. The public version keeps only the reusable rollout checklist and placeholder pattern such as `<new_intent_type>`.

## Example

See `examples/minimal-intent-rollout.md` for a small checklist-shaped rollout where one new intent path is added to an existing dry-run chain.
See `examples/concrete-non-ui-intent-rollout.md` for a more concrete public-safe rollout of `refresh_skill_index`, including one canonical fixture, one dedicated smoke path, one strict contract-check, one published review surface, and one regression proof.

## Checks

See `checks/intent-rollout-checklist.md`.

## Promotion history

- born in `atm10-agent`
- validated through canonical fixtures, dry-run smoke, contract-checks, and regression tests
- promoted to `aoa-techniques` on 2026-03-13

## Future evolution

- add a variant for non-CI operator approval workflows
- add cross-version guidance for evolving intent schemas safely
- add a second source project note once this rollout checklist is observed outside ATM10-shaped automation
