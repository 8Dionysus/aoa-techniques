# Second Context Adaptation

## Technique
- id: AOA-T-0010
- name: telemetry-integrity-snapshot

## Target project
- name: generic evaluation repository with published summaries in object storage
- environment: public-safe summary pipelines that need a diagnostic trust layer before downstream rollups are interpreted
- runtime: scheduled or on-demand helpers that read published latest aliases and emit one integrity verdict

## What changed
- paths: the origin used local published summary paths; this adaptation reads stable latest-alias object keys
- services: the integrity helper may run in any scheduler or operator tool; it does not depend on one CI or workflow platform
- dependencies: the helper needs required-source classification, invariant checks, and explicit source references rather than direct filesystem assumptions
- operating assumptions: the helper remains diagnostic even when the published summaries live in remote storage

## What stayed invariant
- contract: the helper reads latest published summaries only and emits one concise trust verdict
- validation logic: required source health, telemetry checks, dual-write checks, anti-double-count checks, and optional consistency checks remain first-class
- safety rules: the integrity layer stays read-only and diagnostic rather than silently becoming the next enforcement surface
- default-use trigger: once several published summaries or downstream rollups feed several consumers, one shared trust verdict becomes the default companion layer instead of duplicating integrity logic inside each consumer

## Risks introduced by adaptation
- remote publication latency can make missing or stale source reporting more important
- teams can weaken integrity checks if they treat object publication as a reason to skip dual-write or anti-double-count validation
- optional consistency inputs can become noisy unless their absence or disagreement stays explicit

## Evidence
- the origin already proves a published diagnostic integrity helper over latest summaries with explicit invariant families
- `AOA-T-0006` already provides the storage contract that keeps latest aliases and history copies coherent
- `AOA-T-0008` already shows a downstream remediation consumer that benefits from a separate trust verdict before its output is interpreted
- object-store publication preserves the same default pattern when several downstream consumers need one shared read-only trust layer instead of embedding integrity checks separately in reports, dashboards, or agent handoff surfaces

## Result
- works as a bounded object-store second context for a diagnostic published-summary trust layer without merging integrity policy into gate policy, and keeps the layer readable as the default trust companion for multi-summary, multi-consumer systems
