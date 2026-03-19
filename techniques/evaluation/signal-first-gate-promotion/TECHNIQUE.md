---
id: AOA-T-0007
name: signal-first-gate-promotion
domain: evaluation
status: canonical
origin:
  project: atm10-agent
  path: docs/RUNBOOK.md
  note: Derived from a real gate rollout where critical regressions were first observed in signal-only mode, then promoted through readiness, governance, progress, and transition telemetry before strict enforcement was enabled on a narrow surface.
owners:
  - 8Dionysus
tags:
  - evaluation
  - gates
  - rollout
  - diagnostics
summary: Staged pattern for promoting an observed validation signal into strict enforcement without losing diagnostics or widening the fail surface too early.
maturity_score: 5
rigor_level: strict
reversibility: hard
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-15
export_ready: true
relations:
  - type: requires
    target: AOA-T-0003
  - type: requires
    target: AOA-T-0006
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
  - kind: adverse_effects_review
    path: notes/adverse-effects-review.md
---

# signal-first-gate-promotion

## Intent

Turn an observed validation signal into the default staged path toward a hard gate, so the team can collect evidence, preserve diagnostics, and choose a narrow enforcement surface before fail-fast behavior becomes operational.

## When to use

- a machine-readable check already exists and can emit stable summaries
- the team wants to observe regressions before converting them into hard failures
- different execution surfaces need different risk levels
- promotion to strict mode should be justified by history rather than one bad or good run
- an already-summary-producing signal should become enforceable gradually instead of jumping straight from observation to broad hard gating

## When not to use

- the check is too immature to produce stable summary output
- the project needs immediate hard blocking and does not need a staged rollout
- there is no place to retain history or publish diagnostics across runs

## Inputs

- one summary-producing validation check
- an observational mode such as `signal_only`
- a stricter enforcement mode such as `fail_nightly`
- history over repeated runs
- decision telemetry layers that evaluate promotion readiness

## Outputs

- stable summaries from both observational and strict runs
- evidence-based readiness and governance decisions
- progress telemetry that shows remaining gap to promotion
- one explicitly chosen strict enforcement surface
- preserved diagnostics even when the strict surface fails

## Core procedure

1. Start with one stable summary-producing check in `signal_only` mode.
2. Keep artifacts and summaries published even when the signal is bad.
3. Add a readiness layer that measures whether the signal is stable enough for stricter enforcement.
4. Add a governance layer that turns readiness history into explicit `go` or `hold`.
5. Add a progress layer that reports the remaining gap to promotion.
6. Add a transition layer that records promotion telemetry while strict enforcement is activated only on the chosen narrow surface.
7. Keep other surfaces in signal mode until an explicit promotion decision exists.
8. Preserve diagnostics with always-published summaries even after strict failures.

## Contracts

- the same underlying summary contract is used in both `signal_only` and strict modes
- `signal_only` returns success for valid snapshots even when the signal is bad
- strict mode returns non-zero only on the explicitly chosen enforcement surface
- promotion is evidence-based through history, not implicit drift
- readiness, governance, progress, and transition remain decision telemetry rather than hidden runtime logic
- diagnostics remain published even when the strict surface goes red
- non-promoted surfaces do not silently inherit strict behavior
- this technique owns the staged enforcement rollout only; summary production and latest/history storage remain separate prerequisite contracts

## Risks

### Failure modes

- promotion happens from a shallow or noisy history window, so strict mode is enabled before the signal is actually stable
- strict behavior leaks from the chosen enforcement surface into unrelated paths that were supposed to stay observational
- diagnostic summaries stop publishing exactly when strict mode starts failing, removing the evidence needed to understand regressions
- decision telemetry and runtime gating get mixed together until nobody can explain which layer is reporting, holding, or enforcing

### Negative effects

- long staged rollouts can slow response to real regressions when immediate hard blocking would have been the healthier contract
- extra readiness, governance, progress, and transition layers can make the rollout feel controlled while actual gate state becomes harder to explain
- a telemetry-rich rollout can create false-success by looking well-instrumented even when the team still has no clear narrow enforcement decision

### Misuse patterns

- keeping the technique in endless `signal_only` observation instead of choosing whether the signal deserves one strict surface at all
- spreading staged-promotion telemetry across many surfaces until the technique becomes a generic governance stack
- using the technique when the real need is an immediate hard gate, not a cautious rollout over existing summary contracts

### Detection signals

- operators cannot state which single surface is strict, which ones remain observational, and why that boundary exists
- summaries publish readiness or progress signals, but promotion decisions keep stalling without a clear `go` or `hold` interpretation
- a formerly narrow strict rule starts appearing in additional workflows, schedules, or review paths without an explicit promotion decision
- strict failures appear without the diagnostic artifacts that were supposed to remain visible after rollout

### Mitigations

- re-narrow strict enforcement to one explicitly chosen surface and move all other paths back to observational mode until the boundary is clear again
- keep summary publication mandatory across both observational and strict runs before adding more telemetry layers
- collapse or remove decision layers that no longer help explain the rollout, instead of treating more telemetry as automatic progress
- stop using the technique for a bounded context when the right answer is immediate hard blocking rather than staged promotion

## Validation

Verify the technique by confirming that:
- the observational mode always publishes machine-readable output
- the same summary contract is still readable after strict mode is introduced
- readiness uses history rather than a single run
- governance makes `go` or `hold` explicit
- progress reports the remaining gap to promotion
- diagnostics still publish when the strict surface fails
- non-promoted surfaces remain observational

See `checks/gate-promotion-checklist.md`.
For source-backed origin evidence and bounded second-context reinforcement, see `notes/origin-evidence.md` and `notes/second-context-adaptation.md`.

## Adaptation notes

What can vary across projects:
- signal names and severity models
- readiness windows and thresholds
- history limits and streak rules
- enforcement surfaces such as nightly jobs, scheduled workflows, release trains, or dedicated ops runs
- manual override policy when it is explicit and auditable

Project-shaped details that should not be treated as invariant:
- exact policy names such as `signal_only`, `fail_nightly`, or `report_only`
- the specific telemetry-layer names used by one repository
- exact readiness windows, streak thresholds, or reason-code vocabularies
- whether the narrow strict surface is a nightly workflow, a release train, or another scheduled path

What should stay invariant:
- promotion is staged rather than immediate
- one narrow surface is chosen for strict enforcement
- observational surfaces continue publishing diagnostics
- evidence and decision layers stay explicit

Relationship to adjacent techniques: this technique assumes a stable summary producer from `contract-first-smoke-summary` and a trustworthy latest/history layout from `latest-alias-plus-history-copy` before promotion from observation to strict enforcement.

## Public sanitization notes

ATM10-specific gateway names, exact thresholds, workflow names, and project-specific nightly paths were removed. The public version preserves only the reusable staged-promotion pattern and the distinction between observation surfaces and strict surfaces.

## Example

See `examples/minimal-signal-first-rollout.md` for the generic pattern and `examples/concrete-repo-validation-rollout.md` for one more concrete public-safe rollout scenario.

## Checks

See `checks/gate-promotion-checklist.md`.

## Promotion history

- born in `atm10-agent`
- validated through summary contracts, history-based readiness, explicit `go|hold` governance, progress telemetry, and a narrow strict enforcement surface
- promoted to `aoa-techniques` on 2026-03-13
- approved for `canonical` in `aoa-techniques` on 2026-03-17 after stronger bounded second-context reinforcement, a concrete beyond-origin rollout example, and a fresh public-safety recheck

## Future evolution

- add a variant for multi-surface promotion across release trains
- add guidance for demotion back to signal mode after unstable strict rollout
- add an example where promotion intentionally stays report-only for a long-lived warning signal
