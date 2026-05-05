# Adverse Effects Review

## Technique
- id: AOA-T-0007
- name: signal-first-gate-promotion

## Review focus
- current role: default staged-promotion pattern for moving one observed signal toward one narrow strict enforcement surface
- current watch seam: keep storage-layout dependency detail subordinate to rollout semantics and keep one strict surface explicit

## Failure modes
- promotion happens from a shallow or noisy history window and strict mode arrives too early
- strict behavior leaks from the chosen enforcement surface into unrelated paths that were supposed to remain observational

## Negative effects
- long staged rollouts can slow response to real regressions when immediate blocking would be healthier
- telemetry-rich rollout language can make control look stronger than the actual enforcement decision
- a rollout can look highly instrumented and disciplined while nobody can still state one narrow enforcement boundary in plain language

## Misuse patterns
- keeping the technique in endless `signal_only` observation instead of deciding whether the signal deserves a strict surface
- spreading rollout telemetry across many surfaces until the pattern becomes a generic governance stack

## Detection signals
- operators cannot state which single surface is strict, which surfaces are observational, and why that boundary exists
- strict failures appear without the diagnostic artifacts that were supposed to remain visible after rollout
- rollout dashboards look richer over time, but the answer to "what exactly is strict right now?" keeps getting harder rather than easier

## Mitigations
- re-narrow strict enforcement to one explicit surface and keep all other paths observational until the boundary is clear again
- collapse decision layers that no longer help explain the rollout instead of treating more telemetry as automatic progress

## Recommendation
- keep current `canonical` status and use this note as the watch surface for rollout-boundary drift or storage-detail crowding in the `AOA-T-0003` / `AOA-T-0006` dependency chain
