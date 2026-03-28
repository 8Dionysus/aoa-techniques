---
id: AOA-T-0064
name: capability-discovery
domain: docs
status: promoted
origin:
  project: agntcy/dir
  path: README.md + proto/agntcy/dir/search/v1/record_query.proto + proto/agntcy/dir/search/v1/search_service.proto
  note: Adapted from Directory's explicit discovery-query and search-service surfaces so capability lookup stays reviewable without importing ranking policy, trust pipelines, or registry product semantics.
owners:
  - 8Dionysus
tags:
  - docs
  - discovery
  - registry
  - capability
  - query
summary: Keep capability lookup reviewable as explicit bounded queries over published registry entries so discovery stays separate from ranking, marketplace curation, trust policy, and registry product doctrine.
maturity_score: 3
rigor_level: bounded
reversibility: moderate
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-28
export_ready: true
relations:
  - type: complements
    target: AOA-T-0063
evidence:
  - kind: external_origin
    path: notes/external-origin.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: external_review
    path: notes/external-import-review.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# capability-discovery

## Intent

Keep capability discovery reviewable by expressing lookup as one explicit bounded query contract over already-published registry entries instead of hiding discovery meaning inside registry product semantics, marketplace curation, or runtime resolution logic.

## When to use

- a directory, registry, or catalog needs one reviewable lookup surface for published capability records
- the reusable object is the discovery query contract rather than the capability spec or entry-publication contract
- reviewers need visible search fields, bounded pattern rules, and explicit result shape
- a workflow must separate lookup from ranking, editorial curation, or trust-verdict policy

## When not to use

- the main need is the versioned capability contract itself rather than how records are discovered
- the main need is the registry-entry publication contract for named versioned records
- the main need is editorial grouping, featured placement, or marketplace curation
- discovery only works when bundled with graph semantics, runtime routing, or signature-verification policy

## Inputs

- one set of already-published registry entries or records
- one bounded query surface with explicit field types
- one small matching rule set such as exact or wildcard matching
- one explicit result shape such as record identifiers or full records
- one review path for changes to query fields, limits, or response scope

## Outputs

- one reviewable discovery contract for locating published capability records
- lower ambiguity between record publication, lookup behavior, and downstream selection layers
- a bounded lookup surface that can evolve without redefining capability meaning or registry runtime doctrine
- clearer separation between discovery, ranking, trust, and marketplace presentation

## Core procedure

1. Start from already-published registry entries and make discovery subordinate to that publication surface rather than letting lookup redefine the entry contract.
2. Name one bounded set of queryable fields that map to visible record attributes such as name, version, capability facets, or locator hints.
3. Keep matching behavior explicit and small enough to review, such as exact, wildcard, or similarly bounded field patterns.
4. Keep limits, offsets, and the difference between identifier-only lookup versus full-record return visible at the contract layer.
5. Review discovery changes when query fields, match rules, or result shape change, instead of hiding the changes inside server internals.
6. Keep ranking, marketplace editorial policy, semantic linkage, and trust-verdict semantics outside the bounded lookup contract.
7. Split out separate sibling techniques if discovery grows into registry governance, graph semantics, or runtime capability resolution.

## Contracts

- discovery works over already-published entries or records rather than hidden runtime state
- query fields and match rules remain explicit and reviewable
- result shape stays bounded to record identifiers and/or records, not execution or routing behavior
- lookup semantics stay distinct from ranking, editorial curation, trust policy, and registry product doctrine
- the technique does not own capability meaning, record publication, marketplace curation, graph semantics, or runtime resolution
- discovery does not become a disguised policy engine for selection, reputation, or governance

Relationship to adjacent techniques: unlike [AOA-T-0063](../versioned-agent-registry-contract/TECHNIQUE.md), this technique does not publish the registry-facing entry contract; it owns lookup over entries that are already published. Unlike [AOA-T-0025](../capability-spec-versioning/TECHNIQUE.md), it does not define the capability contract itself; it only defines how published records are queried. Unlike [AOA-T-0041](../skill-marketplace-curation/TECHNIQUE.md), it does not add editorial grouping or featured discovery; it keeps lookup smaller than marketplace curation. Unlike [AOA-T-0021](../bounded-relation-lift-for-kag/TECHNIQUE.md), it does not turn discovery metadata into graph semantics.

## Risks

### Failure modes

- query behavior changes without contract review, so discovery semantics drift silently
- lookup fields multiply until the discovery surface quietly becomes ranking, governance, or trust policy
- result shape becomes ambiguous, so callers cannot tell whether discovery returns identifiers, hydrated records, or product-specific payloads

### Negative effects

- an explicit discovery contract adds ceremony for very small local systems that only need manual lookup
- teams may overfit query fields to one donor platform and reduce portability
- a strong lookup surface can create false confidence that selection quality or trustworthiness is already solved

### Misuse patterns

- widening the bundle into marketplace ranking, featured placement, or recommendation logic
- treating discovery filters as a backdoor for trust, reputation, or governance policy
- collapsing query behavior into graph semantics or runtime routing doctrine

### Detection signals

- reviewers can no longer explain what discovery does without reading server code
- new query fields mainly exist to smuggle in policy, ranking, or graph meaning
- the response payload starts including editorial, routing, or execution-planning semantics that do not belong to bounded lookup

### Mitigations

- keep query fields, match rules, and response shape explicit and small
- route curation, trust, and graph concerns into sibling techniques
- require review when lookup fields or response semantics change
- trim fields that exist mainly to patch downstream policy rather than bounded discovery

## Validation

Verify the technique by confirming that:
- discovery uses one explicit bounded query surface over published entries
- query fields and match behavior are readable without opening runtime code first
- the result shape is explicit and reviewable
- lookup stays separate from ranking, curation, trust, and graph semantics
- discovery remains smaller than registry product doctrine and does not redefine capability meaning

See `checks/capability-discovery-checklist.md`.

## Adaptation notes

What can vary across projects:
- the exact query schema or file format
- which record fields are queryable
- whether results return only identifiers, full records, or both
- the wildcard or pattern syntax
- how pagination or limits are represented

What should stay invariant:
- discovery stays explicit as a bounded lookup contract
- lookup operates over already-published entries or records
- query fields and result shape remain reviewable
- discovery stays separate from ranking, curation, trust, and runtime resolution

Project-shaped details that should not be treated as invariant:
- one search API transport such as gRPC or HTTP
- one peer-to-peer network or DHT
- one signature or verification subsystem
- one marketplace UI or recommendation layer
- one runtime watcher or capability resolver

## Public sanitization notes

This import narrows the donor repository to one bounded pattern: published capability records are discoverable through explicit fielded queries with bounded result shapes. Distributed routing, DHT synchronization, signature-verification filters, semantic linkage, ranking policy, runtime resolution, and directory product semantics were intentionally left out of the public contract.

## Example

See `examples/minimal-capability-discovery.md`.

## Checks

See `checks/capability-discovery-checklist.md`.

## Promotion history

- adapted from open-source `agntcy/dir`
- staged through the chat wave 1A registry-discovery lane inside `aoa-techniques`
- promoted into `aoa-techniques` on 2026-03-28 as a bounded external-import technique for explicit capability-discovery query contracts

## Future evolution

- keep [AOA-T-0063](../versioned-agent-registry-contract/TECHNIQUE.md) as the publication-contract sibling instead of folding publication back into discovery
- keep marketplace and selection doctrine separate instead of widening this bundle into curation or ranking policy
- keep semantic linkage and graph semantics separate instead of turning query fields into relation doctrine
