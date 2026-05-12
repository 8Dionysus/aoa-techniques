# Adverse Effects Review

## Technique

- id: AOA-T-0064
- name: capability-discovery

## Review focus

- current role: canonical default for locating already-published capability or agent records through one explicit bounded lookup contract
- current watch seam: preserve discovery as query over published entries without turning it into entry publication, capability-spec ownership, endpoint subscription, runtime invocation, ranking, trust or signature policy, marketplace curation, graph semantics, or registry product governance

## Failure modes

- query fields change without contract review, so discovery semantics drift while callers still believe the same lookup surface is in use
- fuzzy matching or wildcard behavior expands until reviewers can no longer tell which records a query is allowed to return
- result shape changes from identifiers or records into product-specific invocation, routing, trust, or editorial payloads
- discovery starts querying hidden runtime state instead of already-published entries

## Negative effects

- tiny systems can gain unnecessary query-contract ceremony when manual lookup or a static index is enough
- teams can mistake explicit lookup for quality ranking, trustworthiness, or runtime readiness
- discovery fields can become a dumping ground for reputation, policy, endpoint health, graph relations, or marketplace labels
- a registry product can make the reusable contract look platform-specific if lookup, subscription, invocation, and UI browsing are described as one object

## Misuse patterns

- treating query filters as a backdoor for ranking, recommendation, trust, reputation, or governance policy
- using discovery to redefine what the published entry means instead of requiring a separate publication contract
- importing registry console search, SDK subscription, endpoint selection, A2A invocation, or service deployment into the technique
- turning future filters such as skill, tag, or description search into current canonical requirements before the inspected source actually owns them
- collapsing query metadata into graph semantics or marketplace curation

## Detection signals

- reviewers cannot state the query fields, match behavior, and result shape without reading server code
- new fields mainly explain policy, ranking, trust, endpoint availability, or graph relations rather than bounded lookup
- the response payload starts selecting an endpoint, invoking an agent, asserting quality, or producing editorial placement
- adjacent techniques such as versioned registry-entry contract, capability-spec versioning, marketplace curation, or relation lift are being copied into this bundle instead of linked or routed

## Mitigations

- keep query parameters, match behavior, pagination or limit semantics, and result shape visible in the discovery surface
- require review when query fields, fuzzy or wildcard behavior, result shape, or response scope changes
- route entry publication to AOA-T-0063 and capability schema work to AOA-T-0025
- keep trust, signature, endpoint selection, runtime invocation, marketplace curation, graph semantics, registry runtime, and product-console behavior in their owning layers
- mark future search dimensions as future or adjacent until a source makes them current and bounded

## Recommendation

- move `AOA-T-0064` to `canonical` and use this note as the watch surface for query drift, fuzzy-match creep, hidden runtime-state lookup, result-shape creep, discovery/ranking collapse, trust-policy absorption, and registry-product creep
