# External Origin Note

Use this note when a technique is adapted from an external open-source source.
It complements `TECHNIQUE.md` and records provenance, adaptation boundaries, and public-safety review.

## Source

- source_repo: `https://github.com/agntcy/dir`
- source_license: Apache-2.0
- inspired_by: not used in this import
- adapted_from: `README.md`, `proto/agntcy/dir/search/v1/record_query.proto`, `proto/agntcy/dir/search/v1/search_service.proto`, and the adjacent record and signature proto families that help bound what stays outside the imported contract

## What changed

- what_changed: narrowed the donor repository to one bounded pattern: discovery is an explicit query contract over already-published capability records
- invariant core kept: discovery fields, bounded match rules, and explicit result shape stay readable instead of hiding lookup semantics in server internals
- project-shaped details removed or generalized: distributed routing, DHT synchronization, runtime watchers, signature services, semantic linkage, ranking policy, CLI and GUI tooling, and broader directory product semantics

## Public-safety review

- secrets or tokens removed: none from the donor surfaces used for this import
- private paths, URLs, or IDs removed: donor service endpoints, deployment paths, and node/runtime layout were omitted
- environment-specific assumptions generalized: peer-to-peer networking, service transport, and deployment specifics were removed from the invariant core
- remaining public-safety concerns: future sibling techniques should handle trust, semantic linkage, curation, or runtime resolution separately rather than widening this discovery contract

## Review notes

- why this adaptation is reusable here: many public systems need a reviewable lookup contract for published capability records without importing a whole registry platform
- primary evidence used: the donor README names capability-based discovery as a first-class directory feature, while `record_query.proto` and `search_service.proto` define explicit query types, bounded wildcard matching, and reviewable lookup/response shapes
- limits or follow-up review concerns: publication contracts, graph relations, trust filters, and directory runtime semantics remain intentionally outside this import
