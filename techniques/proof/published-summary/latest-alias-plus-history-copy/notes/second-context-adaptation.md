# Second Context Adaptation

## Technique
- id: AOA-T-0006
- name: latest-alias-plus-history-copy

## Target project
- name: generic evaluation repository with published artifacts in object storage
- environment: public-safe summary pipelines that publish stable object keys for latest state and immutable per-run evidence
- runtime: storage-backed helpers that read and write object keys rather than local filesystem paths

## What changed
- paths: the origin used local run directories; this adaptation uses stable object keys for the latest alias and immutable per-run history objects
- services: object publication may be handled by any storage client or workflow step; the technique does not depend on a specific vendor or SDK
- dependencies: readers need stable alias discovery and explicit history-object scanning rather than a local directory walk
- operating assumptions: history objects stay immutable, and the latest alias remains a consumer convenience rather than the canonical accumulation source

## What stayed invariant
- contract: one stable latest alias exists for simple discovery, and one distinct history copy exists for each run
- validation logic: schema, status, and path metadata stay coherent between the alias and the history copy
- safety rules: collectors prefer history objects for accumulation and use the latest alias only for explicit legacy fallback

## Risks introduced by adaptation
- object lifecycle rules can delete history rows too aggressively and weaken accumulation
- readers can accidentally scan both latest aliases and history keys unless prefix rules stay explicit
- mutable object-version policies can blur the boundary unless the history key remains distinct from the latest alias

## Evidence
- the origin already treats alias plus history as separate published summary surfaces with explicit `summary_json`, `history_summary_json`, and `run_dir` metadata
- this repository already documents published-summary consumers that depend on stable latest aliases rather than ad hoc log discovery
- the adaptation changes only the storage medium, not the dual-write or anti-double-count contract

## Result
- works as a bounded second context for published object storage without widening the technique into vendor-specific storage automation
