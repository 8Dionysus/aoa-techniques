# Adverse Effects Review

## Technique
- id: AOA-T-0010
- name: telemetry-integrity-snapshot

## Review focus
- current role: canonical diagnostic trust layer over published summaries and downstream rollups
- current watch seam: preserve the helper's diagnostic-only role and keep it separate from remediation backlog or rendering-policy semantics

## Failure modes
- schema drift between latest alias and history copies goes undetected and corrupts integrity conclusions
- the helper is treated as a replacement for fixing broken producers instead of a diagnostic signal

## Negative effects
- checking too many optional invariants can turn a focused trust layer into noise
- implicit hard-gate promotion can make enforcement brittle while still claiming to be read-only

## Misuse patterns
- using the helper as a default enforcement gate instead of a diagnostic surface
- expanding optional guardrail checks until they overshadow required source health and dual-write invariants

## Detection signals
- integrity findings repeat across runs without upstream producer fixes, but the helper keeps being treated as the main response
- optional-source consistency checks dominate the snapshot more than required health or anti-double-count issues

## Mitigations
- keep the snapshot focused on required source health, telemetry invariants, dual-write coherence, and anti-double-count checks
- make any hard-gate promotion a separate rollout decision instead of an implicit property of the helper

## Recommendation
- keep current `canonical` status and use this note as the watch surface for diagnostic-helper drift toward hard enforcement or overlap with neighboring downstream consumers
