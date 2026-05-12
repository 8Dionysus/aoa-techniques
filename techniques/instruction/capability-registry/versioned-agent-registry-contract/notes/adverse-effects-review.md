# Adverse Effects Review

## Technique

- id: AOA-T-0063
- name: versioned-agent-registry-contract

## Review focus

- current role: canonical default for publishing one registry-facing capability or agent entry as an explicit named and versioned record with bounded metadata or a stable reference
- current watch seam: preserve the entry contract without turning it into capability-spec ownership, discovery policy, fuzzy search, ranking, trust or signature policy, endpoint subscription, marketplace curation, graph semantics, or registry product governance

## Failure modes

- a registry entry changes content while keeping the same version, so consumers cannot tell which publication contract they are reading
- name, namespace, version, reference, and metadata are split across implementation internals instead of being visible at the entry layer
- annotations expand until the registry entry quietly owns capability meaning, trust state, discovery ranking, or graph relations
- a default or current version pointer changes without review, creating silent drift between the published entry and what consumers receive

## Negative effects

- small local capability specs can gain unnecessary publication ceremony when no registry-facing entry exists
- teams can mistake versioned publication for validated trust, quality, or runtime compatibility
- entry metadata can become a dumping ground for search filters, policy flags, endpoint health, and marketplace labels
- a registry product can make the reusable contract look platform-specific if publication, query, subscription, and runtime invocation are described as one object

## Misuse patterns

- using this technique as a general capability-spec schema instead of a registry-entry publication contract
- treating a named versioned entry as if it proves discovery ranking, trust, signature validity, or endpoint availability
- importing registry console workflows, SDK lifecycle, service endpoints, authentication, or subscription behavior into the technique
- using entry annotations as a backdoor for marketplace curation, graph semantics, or owner-routing policy
- updating a default version pointer as a hidden rollout instead of an explicit publication change

## Detection signals

- reviewers cannot state the entry name, version, reference or payload boundary, and metadata purpose without reading registry runtime code
- the contract starts listing query filters, ranking rules, fuzzy search, trust gates, or endpoint-selection behavior as core entry fields
- the current default version changes but no publication review names why the new version is the default
- adjacent techniques such as capability-spec versioning, capability discovery, marketplace curation, or relation lift are being copied into this bundle instead of linked or routed

## Mitigations

- keep entry identity, version, reference or payload boundary, and bounded metadata visible in the publication surface
- require review when entry identity, version semantics, default-version pointer, reference meaning, or metadata interpretation changes
- route capability schema work to AOA-T-0025 and discovery/query behavior to AOA-T-0064
- keep trust, signature, endpoint selection, marketplace curation, graph semantics, registry runtime, and product-console behavior in their owning layers
- trim metadata that does not help another reader understand the bounded published entry

## Recommendation

- move `AOA-T-0063` to `canonical` and use this note as the watch surface for version drift, metadata creep, hidden default-version rollout, discovery/ranking absorption, trust-policy absorption, and registry-product creep
