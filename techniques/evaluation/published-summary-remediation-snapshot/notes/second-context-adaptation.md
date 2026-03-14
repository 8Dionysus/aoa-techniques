# Second Context Adaptation

## Technique
- id: AOA-T-0008
- name: published-summary-remediation-snapshot

## Target project
- name: generic evaluation repository with read-only triage helpers over published object-store summaries
- environment: public-safe summary pipelines that publish latest aliases as stable object keys
- runtime: scheduled or on-demand remediation helpers that consume published summaries without replaying history

## What changed
- paths: the origin used local published summary paths; this adaptation reads stable object keys for latest aliases
- services: snapshot generation may run in any scheduler or helper process; the technique does not depend on one workflow system
- dependencies: the helper needs stable latest-alias discovery, a deterministic bucket policy, and explicit source references, not local directory traversal
- operating assumptions: the helper remains read-only and bounded even when the storage layer is remote

## What stayed invariant
- contract: the helper reads only latest published summaries and never scans historical runs
- validation logic: fixed buckets, explicit caps, and source references remain required for a trustworthy snapshot
- safety rules: snapshot generation stays read-only and does not widen into a second evaluator or executor

## Risks introduced by adaptation
- object alias publication can lag and make stale-input reporting more important
- teams can accidentally reintroduce history replay by scanning object prefixes instead of reading declared latest aliases
- snapshot consumers can lose auditability if emitted candidates do not preserve exact source object keys

## Evidence
- the origin already proves a read-only remediation helper over published latest summaries with deterministic buckets and explicit caps
- `AOA-T-0006` already isolates the stable latest-alias contract that this snapshot depends on
- the adaptation changes only where the latest summaries live, not the bounded remediation role of the helper

## Result
- works as a bounded object-store second context for a promoted technique without widening the snapshot into history replay or storage-specific automation
