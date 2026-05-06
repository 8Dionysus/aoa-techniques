---
id: AOA-T-0037
name: contextual-host-doctor
domain: evaluation
kind: validation
status: promoted
origin:
  project: abyss-stack
  path: docs/DOCTOR.md
  note: Extracted from a selector-aware preflight check that changes its verdicts based on the chosen runtime shape instead of treating every host warning as universally relevant.
owners:
  - 8Dionysus
tags:
  - evaluation
  - preflight
  - readiness
  - diagnostic
  - profile-aware
summary: Run selector-aware host-readiness checks before startup so environment drift becomes visible for the chosen runtime without widening into generic monitoring or lifecycle control.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-22
export_ready: true
relations:
  - type: complements
    target: AOA-T-0036
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# contextual-host-doctor

## Intent

Expose whether the current host is shaped enough for the selected runtime before startup by running selector-aware readiness checks that distinguish relevant warnings from real preflight blockers.

## When to use

- startup success depends on host-side conditions that vary by the selected profile, preset, or runtime path
- different runtime selections make different readiness signals relevant
- operators need one bounded pre-start readiness verdict before launch
- environment drift should become visible before time is spent on startup failure triage
- the reusable object is a contextual preflight diagnostic, not startup control or post-start health verification

## When not to use

- the main need is layered runtime composition or rendered startup truth
- the main need is smoke, health, or internal probe verification after services are running
- the check surface is really fleet monitoring, incident response, or continuous observability
- every warning should always be a hard failure regardless of context
- the tool would become a bootstrap installer, secret manager, or lifecycle wrapper instead of a readiness verdict

## Inputs

- one selected profile, preset, or equivalent runtime choice
- one known set of host-side prerequisites and optional signals
- one context rule that says which checks matter for the selected runtime
- one pre-start execution point for the diagnostic
- one optional strict mode that can promote warnings into failure

## Outputs

- one selector-aware readiness verdict before startup
- explicit `ok`, `warn`, or `fail` signals for checked items
- earlier visibility into environment drift that matters for the chosen runtime
- one clear handoff into render, launch, or post-start checks after preflight review

## Core procedure

1. Resolve the selected profile, preset, or equivalent runtime choice through the same selector logic used by adjacent runtime tools.
2. Print the selected runtime summary so the verdict is visibly tied to one concrete runtime choice.
3. Check the small set of host prerequisites that always matter, such as core commands, basic runtime backend availability, or baseline platform expectations.
4. Add contextual checks only when the selected runtime makes them relevant.
5. Emit explicit `ok`, `warn`, or `fail` results for each checked item rather than one opaque pass or fail outcome.
6. Keep optional or context-specific issues visible as warnings unless the chosen strictness policy promotes them.
7. Stop at the readiness verdict and hand off to render, launch, smoke, or internal probes as separate steps.

## Contracts

- the doctor verdict is selector-aware rather than one global readiness score
- the same selection inputs used by nearby runtime tools must determine which checks are relevant here
- the technique stays pre-start and diagnostic
- explicit `ok`, `warn`, and `fail` signals remain visible item by item
- strict mode may harden warning handling, but the default contract keeps contextual warnings distinct from hard blockers
- the technique does not own composition, rendered truth, startup, smoke, internal probes, or monitoring programs
- the doctor result should help an operator decide whether to proceed, but it is not proof that startup or post-start health will succeed

Relationship to adjacent techniques: unlike `AOA-T-0036`, this technique answers whether the host is ready enough for the selected runtime, not what the final composed runtime resolves to. Unlike `AOA-T-0003`, it is a pre-start diagnostic verdict rather than a post-start smoke summary contract.

## Risks

### Failure modes

- a warning becomes ambient and stops influencing real preflight decisions
- the check list grows until the doctor behaves like a generic monitoring suite
- the selected runtime changes but the relevant checks do not change with it
- operators treat a passing doctor result as proof that startup and post-start health are guaranteed

### Negative effects

- preflight checks can add friction to small local runs
- warning-heavy output can create alert fatigue if severity is not kept honest
- strict mode can make optional drift feel like a hard blocker in contexts where it should remain advisory
- a concise preflight verdict can create false confidence when it is mistaken for broader runtime validation

### Misuse patterns

- turning selector-aware preflight into a generic host inventory or monitoring program
- adding post-start health or internal probe checks to make the doctor feel more complete
- using the doctor as a substitute for render review, smoke, or lifecycle control
- hard-coding donor-specific paths or device assumptions as universal requirements

### Detection signals

- the doctor output is mostly the same no matter which runtime selection is used
- contributors start discussing dashboards, incidents, or continuous polling instead of pre-start readiness
- the doctor begins naming running-service health rather than host-side preconditions
- operators still hit the same startup blockers even though the doctor supposedly covered them

### Mitigations

- keep the check set small and tied to concrete pre-start blockers or warnings
- require selection-aware branching whenever a check matters only for some runtime paths
- keep item-level severity explicit and review whether warnings are still genuinely advisory
- route render, smoke, and lifecycle concerns into sibling techniques instead of widening the doctor
- treat repeated uncaught startup blockers as evidence that the preflight contract needs sharpening

## Validation

Verify the technique by confirming that:
- the readiness verdict changes when a different runtime selection changes what should matter
- item-level `ok`, `warn`, and `fail` signals are visible
- context-specific checks appear only when the selected runtime makes them relevant
- strict mode behavior is explicit rather than implicit
- the bundle stays pre-start and diagnostic rather than drifting into startup, smoke, or monitoring

See `checks/contextual-host-doctor-checklist.md`.

## Adaptation notes

What can vary across projects:
- the exact host prerequisites
- the selector names and runtime-path vocabulary
- the strictness policy for warnings
- the command or UI surface that presents the readiness verdict

What should stay invariant:
- readiness checks are contextual to the selected runtime
- item-level severity remains explicit
- the diagnostic runs before startup
- the result stays diagnostic rather than mutating or continuously monitoring

Project-shaped details that should not be treated as invariant:
- exact device paths such as `/dev/dri`
- exact runtime roots such as `/srv/...`
- exact command names such as `podman` or `systemctl`
- donor-specific internal-only layer names or vault mount points

## Public sanitization notes

This public bundle keeps only the reusable selector-aware preflight contract. Donor-specific device paths, runtime roots, command names, and internal service names were generalized so the technique stays portable and public-safe.

## Example

See `examples/minimal-contextual-host-doctor.md`.

## Checks

See `checks/contextual-host-doctor-checklist.md`.

## Promotion history

- extracted from `abyss-stack`
- promoted to `aoa-techniques` on 2026-03-22 as a bounded evaluation technique for selector-aware host readiness

## Future evolution

- keep `one-command-service-lifecycle` as the lifecycle sibling rather than widening this bundle into launch control
- keep `baseline-first-additive-profile-benchmarks` as the comparison sibling rather than turning readiness into performance judgment
- add a second live context if another runtime stack adopts the same selector-aware preflight verdict
