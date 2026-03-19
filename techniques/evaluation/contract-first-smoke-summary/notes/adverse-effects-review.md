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

## Negative effects
- over-minimal summaries can push humans back toward log scraping
- pressure-driven fallback to raw logs can become sticky and weaken the producer contract over time

## Misuse patterns
- treating summary generation as optional when execution is under pressure
- changing filenames, fields, or status semantics without a bounded compatibility plan

## Detection signals
- downstream consumers start scraping console logs again instead of reading the summary artifact
- repeated failures show `error` with too little observed data to explain the problem quickly

## Mitigations
- keep one stable machine-readable summary path across success and failure paths whenever the process can still emit output
- evolve summary shape deliberately and keep rollout or storage detail outside the producer contract

## Recommendation
- keep current `canonical` status and use this note as the watch surface for producer drift into storage-layout or staged-enforcement language
