# Canonical Readiness

## Technique
- id: AOA-T-0037
- name: contextual-host-doctor

## Verdict
- approve for canonical promotion

## Evidence summary
- origin evidence is strong enough to justify a promoted public bundle
- Get Physics Done now provides an exact-fit public second context: it exposes `gpd doctor --runtime <runtime> --local/--global`, resolves the selected runtime target, emits item-level readiness checks, distinguishes warnings/advisories from blockers, and keeps permission, plan, and build verdicts in sibling commands
- the second context adaptation keeps the contract bounded around selected-target preflight readiness rather than install orchestration, unattended permission policy, plan validation, manuscript build, smoke, lifecycle, or monitoring breadth
- the bundle now has a checklist, a public-safe example, origin evidence, exact-fit second-context evidence, and an adverse-effects review, so the pattern is no longer proven mainly through one donor lineage

## Default-use rationale
- this is the right canonical default when the missing object is a selected-target pre-start readiness verdict, not a renderer, launcher, smoke check, monitor, or permission-policy engine
- it is strongest when one selected runtime, profile, preset, install target, or equivalent path changes which checks matter and which warnings remain advisory
- it remains narrower than `AOA-T-0035` because it assumes a selected runtime path and diagnoses readiness rather than owning profile/preset composition
- it remains narrower than `AOA-T-0036` and `AOA-T-0038` because it does not render the final runtime truth and does not own startup, shutdown, or lifecycle control
- Get Physics Done confirms that the default move can survive outside `abyss-stack`: inspect selected-runtime readiness, surface item-level failures and advisories, then hand off to the next bounded runtime or workflow step

## Fresh public-safety check
- review date: 2026-05-12
- result: pass
- sanitization still holds: the published technique keeps the selector-aware readiness contract while stripping donor-specific commands, paths, and hardware assumptions
- Get Physics Done evidence strengthens the public-safety boundary because runtime/provider specifics remain target-scoped diagnostics while warnings, blockers, permission alignment, plan preflight, and build truth stay separated

## Remaining gaps
- no blocking promotion gap remains as long as the bundle stays centered on selected-target pre-start diagnostics with item-level severity
- future review should keep rejecting surfaces that are only generic environment checks, install wrappers, permission gates, plan validators, build validators, smoke tests, lifecycle controllers, or monitoring dashboards without the same selector-aware doctor verdict

## Recommendation
- promote `AOA-T-0037` to `canonical`
- use `AOA-T-0037` as the default runtime-readiness technique when selected runtime context changes which pre-start warnings or blockers matter, while routing composition, render truth, lifecycle, permission alignment, plan validation, smoke, build, and monitoring concerns to sibling owners
