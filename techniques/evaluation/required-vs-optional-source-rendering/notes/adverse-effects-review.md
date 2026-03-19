# Adverse Effects Review

## Technique
- id: AOA-T-0011
- name: required-vs-optional-source-rendering

## Review focus
- current role: canonical rendering policy for required versus optional summary sources
- current watch seam: keep the policy general enough that it does not collapse back into the published-summary package that currently supplies its clearest examples

## Failure modes
- an actually critical source is misclassified as optional
- optional-source absence is hidden instead of being surfaced explicitly and read-only

## Negative effects
- optional-source warnings can accumulate until the surface becomes noisy
- the renderer can drift away from its bounded summary role and become harder to trust

## Misuse patterns
- treating `optional` as meaning never operationally important rather than visible but non-fatal for this contract
- expanding the rendering surface so it performs repair or retry actions instead of staying read-only

## Detection signals
- operators stop noticing missing-source signals because the warning stream is constant or unsorted
- future wording starts reading like a bundle-specific appendix to remediation or integrity instead of a general consumer policy

## Mitigations
- review required-versus-optional classification explicitly and promote sources when the contract changes
- keep warnings bounded, visible, and read-only so missing optional data stays observable without turning the surface into an action layer

## Recommendation
- keep current `canonical` status and use this note as the watch surface for the documented `AOA-T-0011` rendering-policy seam inside the published-summary cluster
