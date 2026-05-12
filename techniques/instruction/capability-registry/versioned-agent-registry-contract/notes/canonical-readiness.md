# Canonical Readiness

## Technique
- id: AOA-T-0063
- name: versioned-agent-registry-contract

## Verdict
- approve for canonical promotion

## Evidence summary
- external origin: the imported technique has a bounded donor contract and explicit exclusions around discovery queries, semantic linkage, trust services, and registry runtime breadth
- second context: `aoa-techniques` now records the same contract as a documentation-first adaptation with one example and one checklist
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- `nacos-group/nacos-group.github.io` provides exact-fit public reinforcement beyond the donor family: its A2A Registry guide treats AgentCards as registered agent entries with namespace/name identity, unique versions, a current default published version, SDK and HTTP publication paths, and explicit AgentCard fields such as name, description, URL, version, and protocol version
- validation strength: the bundle now carries one checklist, one example, a clean external-origin note, a documentation-first second context, and public cross-context reinforcement for the same bounded named/versioned registry-entry contract

## Default-use rationale
- this is the right canonical default when the main problem is making a registry-facing capability entry explicit and versioned instead of hiding publication meaning in runtime or directory internals
- it remains narrower than [AOA-T-0025](../../capability-spec-versioning/TECHNIQUE.md) because it owns the publication contract for a registry entry rather than the full capability spec, and it remains narrower than [AOA-T-0041](../../../skill-discovery/skill-marketplace-curation/TECHNIQUE.md) because it does not curate discovery or selection
- it is now strong enough as a canonical default because the Nacos source repeats the same entry-contract shape in a separate live agent-registry family without requiring this bundle to absorb Nacos product semantics, A2A runtime invocation, discovery ranking, fuzzy search, endpoint subscription, or trust policy

## Fresh public-safety check
- review date: 2026-05-12
- result: pass
- sanitization still holds: the bundle keeps only the reusable entry contract and excludes donor-specific network, query, signature, and runtime details
- public reuse check: the example, checklist, and adaptation notes remain understandable without hidden donor-repo context; the inspected `nacos-group/nacos-group.github.io` source is Apache-2.0 licensed and no source code, credentials, private deployment state, local endpoints, or Nacos-specific runtime setup was copied into the technique

## Remaining gaps
- no blocker remains for canonical status
- future registry-entry sources can reinforce the default, but they must preserve the narrow boundary: one explicit registry-facing entry identity, one version, one bounded publication payload or reference, and reviewable metadata without collapsing into discovery, ranking, trust, runtime invocation, or marketplace curation

## Recommendation
- move `AOA-T-0063` to `canonical`
- add an adverse-effects review to preserve the boundary between versioned registry-entry publication, capability-spec ownership, discovery/query behavior, endpoint subscription, trust or signature policy, marketplace curation, graph semantics, and registry product governance
