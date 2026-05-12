# Adverse Effects Review

## Technique
- id: AOA-T-0037
- name: contextual-host-doctor

## Review focus
- current role: canonical default for selected-target pre-start readiness diagnostics
- current watch seam: keep the bundle centered on contextual doctor verdicts with item-level severity rather than install orchestration, rendered runtime truth, lifecycle control, smoke, monitoring, permission policy, plan validation, or build truth

## Failure modes
- a doctor result is treated as proof that startup, runtime health, unattended execution, plan execution, or build output will succeed
- warning-heavy output becomes ambient and no longer affects operator decisions
- the selected runtime, profile, preset, target, or install scope changes but the readiness check set stays static
- a generic environment checker is mistaken for contextual preflight because it uses a `doctor` command name

## Negative effects
- canonical status can make small projects add a doctor step when one static preflight note would be enough
- contextual warnings can create alert fatigue if every optional issue is printed on every selected path
- target-scoped readiness can create false confidence when users forget that permission, render, smoke, build, and monitoring checks are separate
- strict handling of warnings can block useful degraded paths when the warning should remain advisory

## Misuse patterns
- folding install repair, permission synchronization, launch, smoke, paper build, or plan validation into the doctor
- using the doctor as a broad host inventory, fleet monitor, or incident dashboard
- hard-coding one donor's runtime paths, devices, providers, or command names as universal requirements
- counting a context-free `doctor` utility as evidence for this technique without checking selector-aware relevance

## Detection signals
- output is nearly identical across selected runtime paths even when their prerequisites differ
- contributors describe dashboards, polling, running-service health, or automatic repair more than pre-start readiness
- operators still hit the same selected-runtime blockers immediately after a passing doctor result
- warnings and blockers are collapsed into one opaque pass/fail line

## Mitigations
- keep the check set small and tied to selected-path pre-start blockers or advisories
- require one visible selected runtime, profile, preset, target, or equivalent context before interpreting the verdict
- keep warning/advisory output separate from hard blockers and review whether each warning still belongs
- route render, lifecycle, smoke, permission, plan, build, monitoring, and repair concerns to sibling techniques or owner repos
- record context-free doctor tools as adjacent searched lanes unless they prove selected-target branching and item-level severity

## Recommendation
- keep current `canonical` status and use this note as the watch surface for false readiness, alert fatigue, context-free doctor drift, and expansion into runtime owner authority
