# External Origin Note

Use this note when a technique is adapted from an external open-source source.
It complements `TECHNIQUE.md` and records provenance, adaptation boundaries, and public-safety review.

## Source

- source_repo: `https://github.com/agntcy/dir`
- source_license: Apache-2.0
- inspired_by: not used in this import
- adapted_from: `README.md`, `proto/agntcy/dir/core/v1/record.proto`, and the adjacent `search` and `sign` proto families that help bound what stays outside the imported contract

## What changed

- what_changed: narrowed the donor repository to one bounded pattern: a registry-facing capability entry is a named, versioned record with explicit reference and metadata
- invariant core kept: published entries expose explicit entry identity, stable reference, and bounded metadata instead of hiding those meanings in registry internals
- project-shaped details removed or generalized: distributed peer routing, DHT synchronization, search service APIs, signature services, runtime deployment, GUI and CLI tooling, and broader directory product semantics

## Public-safety review

- secrets or tokens removed: none from the donor surfaces used for this import
- private paths, URLs, or IDs removed: donor service endpoints, deployment paths, and registry runtime layout were omitted
- environment-specific assumptions generalized: peer-to-peer routing, distributed synchronization, and service deployment details were removed from the invariant core
- remaining public-safety concerns: future sibling techniques should handle discovery, semantic linkage, trust, or registry runtime breadth separately rather than widening this entry contract

## Review notes

- why this adaptation is reusable here: many public systems need a reviewable publication contract for capability records without importing the full registry product or distributed runtime
- primary evidence used: the donor README describes publication and discovery of records over a distributed network, while `record.proto` defines `NamedRecordRef`, `RecordMeta`, and a generic `Record` object that together expose an explicit registry-facing entry shape
- limits or follow-up review concerns: discovery queries, semantic linkage, signatures, and registry implementation concerns remain intentionally outside this first import
