# Adverse Effects Review

## Technique
- id: AOA-T-0010
- name: telemetry-integrity-snapshot

## Review focus
- current role: canonical diagnostic trust layer over published summaries and downstream rollups
- current watch seam: preserve the helper's diagnostic-only role, keep optional checks subordinate to required-source health, and keep stricter enforcement as a separate rollout decision

## Failure modes
- optional consistency noise starts crowding out required-source health and dual-write coherence
- the helper is treated as a replacement for fixing broken producers or as a de facto gate instead of a diagnostic signal
- schema drift between latest alias and history copies goes undetected and corrupts integrity conclusions

## Negative effects
- checking too many optional invariants can turn a focused trust layer into noise
- the helper can start reading like a pre-gate even while it still claims to be read-only

## Misuse patterns
- using the helper as a default enforcement gate or merge-block proxy instead of a diagnostic surface
- expanding optional guardrail checks until they overshadow required source health and dual-write invariants

## Detection signals
- integrity findings repeat across runs without upstream producer fixes, but the helper keeps being treated as the main response or block signal
- optional-source consistency checks dominate the snapshot more than required health or anti-double-count issues
- operators or CI language start talking about `attention` as if it already means "block by default"

## Mitigations
- keep the snapshot focused on required source health, telemetry invariants, dual-write coherence, and anti-double-count checks
- make any hard-gate or block-semantics promotion a separate rollout decision instead of an implicit property of the helper

## Recommendation
- keep current `canonical` status and use this note as the watch surface for diagnostic-helper drift toward implicit enforcement or optional-check noise
