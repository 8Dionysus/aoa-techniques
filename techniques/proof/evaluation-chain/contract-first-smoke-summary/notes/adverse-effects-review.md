# Adverse Effects Review

## Technique
- id: AOA-T-0003
- name: contract-first-smoke-summary

## Review focus
- current role: default summary-contract producer for runnable smoke and probe paths
- current watch seam: keep storage and rollout semantics downstream so the producer contract does not collapse into the broader evaluation chain

## Failure modes
- failure paths emit bare `error` signals with too little observed context to diagnose quickly
- summary shape drifts often enough to break downstream consumers that expect one stable contract
- the producer still emits a summary artifact, but the artifact is too thin to explain failure and only gives the illusion of a healthy contract surface

## Negative effects
- over-minimal summaries can push humans back toward log scraping
- pressure-driven fallback to raw logs can become sticky and weaken the producer contract over time
- the smoke path can look automation-friendly while the real operator experience is still "summary first, logs immediately after"

## Misuse patterns
- treating summary generation as optional when execution is under pressure
- changing filenames, fields, or status semantics without a bounded compatibility plan
- preserving the summary only as a pass/fail token while richer explanation quietly migrates back to console text

## Detection signals
- downstream consumers start scraping console logs again instead of reading the summary artifact
- repeated failures show `error` with too little observed data to explain the problem quickly
- the summary is still published on every run, but operators no longer trust it as the first place to diagnose a failure

## Mitigations
- keep one stable machine-readable summary path across success and failure paths whenever the process can still emit output
- evolve summary shape deliberately and keep rollout or storage detail outside the producer contract
- treat log-scraping relapse as a stop signal and widen observed summary context before layering on more downstream consumers

## Recommendation
- keep current `canonical` status and use this note as the watch surface for green-looking producer contracts that still degrade into log-scraping diagnosis
