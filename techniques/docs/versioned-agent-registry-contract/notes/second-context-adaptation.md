# Second Context Adaptation

## Technique
- id: AOA-T-0063
- name: versioned-agent-registry-contract

## Target project
- name: aoa-techniques
- environment: public library repository with technique bundles, generated catalog surfaces, and explicit evidence-note discipline
- runtime: documentation-first repository that records the registry-entry contract rather than shipping the donor directory implementation

## What changed

- paths: the donor uses protobuf models and service families; this adaptation presents a generic reviewable entry contract that can fit other public registries or directories
- services: no distributed routing, query API, signature service, or registry node is required in this repository
- dependencies: the adaptation depends on explicit entry identity plus bounded metadata, not on the donor runtime or peer network
- operating assumptions: contributors should treat the contract as publication-only and keep discovery, trust, semantic linkage, and product semantics visibly separate

## What stayed invariant

- contract: one registry-facing entry publishes a named versioned record with explicit reference and metadata
- validation logic: another reader can inspect the entry and tell what object is published and which version it claims to be
- safety rules: the entry contract stays subordinate to capability meaning and does not silently become search policy, curation, or trust doctrine

## Risks introduced by adaptation

- the pattern can become vague if a project publishes records but never explains which metadata remains contract-relevant
- some repositories may keep name and version fields but let search, ranking, or trust semantics quietly colonize the entry surface

## Evidence

- the donor README describes publication, exchange, and discovery of records and frames capability-based discovery as a directory concern built around structured metadata
- `record.proto` defines `NamedRecordRef` with name, version, and CID plus `RecordMeta` with schema version, annotations, and creation time
- adjacent `record_query.proto` and signature proto files make it clear that discovery queries and trust referrers are neighboring layers rather than the same contract as the entry itself

## Result

- works as a documentation-first second context and preserves the bounded core without carrying over donor-specific routing, trust, or runtime breadth
