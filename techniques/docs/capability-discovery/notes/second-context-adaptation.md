# Second Context Adaptation

## Technique
- id: AOA-T-0064
- name: capability-discovery

## Target project
- name: aoa-techniques
- environment: public library repository with technique bundles, generated catalog surfaces, and explicit evidence-note discipline
- runtime: documentation-first repository that records the discovery-query contract rather than shipping the donor search service

## What changed

- paths: the donor uses protobuf query and service definitions; this adaptation presents a generic reviewable discovery contract that can fit other public registries or catalogs
- services: no search server, peer network, marketplace UI, or runtime watcher is required in this repository
- dependencies: the adaptation depends on explicit query fields, bounded match rules, and visible result shape, not on donor transport or runtime internals
- operating assumptions: contributors should treat discovery as lookup-only and keep ranking, trust, semantic linkage, and runtime resolution visibly separate

## What stayed invariant

- contract: one bounded query surface discovers already-published capability records
- validation logic: another reader can inspect the query fields and tell what can be looked up and what shape discovery returns
- safety rules: the discovery contract stays subordinate to publication and capability meaning and does not silently become ranking, trust, or graph doctrine

## Risks introduced by adaptation

- the pattern can become vague if a project exposes query fields but never explains which ones remain part of the stable contract
- some repositories may keep discovery explicit at first and then let reputation, verification, or ranking semantics colonize the lookup surface

## Evidence

- the donor README presents capability-based discovery as a directory concern built around structured metadata and discovery by attributes and constraints
- `record_query.proto` defines explicit fielded query types and bounded wildcard matching
- `search_service.proto` separates identifier-only lookup from full-record return, which helps keep result shape reviewable
- adjacent record and signature proto families make it clear that publication contracts and trust services are neighboring layers rather than the same object as bounded discovery

## Result

- works as a documentation-first second context and preserves the bounded core without carrying over donor-specific transport, networking, or directory-product breadth
