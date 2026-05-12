# Canonical Readiness

## Technique
- id: AOA-T-0064
- name: capability-discovery

## Verdict
- approve for canonical promotion

## Evidence summary
- external origin: the imported technique has a bounded donor contract and explicit exclusions around ranking, semantic linkage, trust filters, and registry runtime breadth
- second context: `aoa-techniques` now records the same contract as a documentation-first adaptation with one example and one checklist
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- `nacos-group/nacos-group.github.io` provides exact-fit public reinforcement beyond the donor family: its A2A Registry guide separates query from publication, retrieves the default published AgentCard by name, exposes HTTP exact-name detail lookup with `namespaceId` and `agentName`, exposes list search with `pageNo`, `pageSize`, `agentName`, `namespaceId`, and `search=blur`, and keeps skills/tags/description filtering as a future search dimension rather than an imported current contract
- validation strength: the bundle now carries one checklist, one example, a clean external-origin note, a documentation-first second context, and public cross-context reinforcement for the same bounded discovery-query contract

## Default-use rationale
- this is the right canonical default when the main problem is making capability lookup explicit and reviewable over already-published entries instead of hiding discovery semantics in server code or registry product behavior
- it remains narrower than [AOA-T-0063](../../versioned-agent-registry-contract/TECHNIQUE.md) because it does not publish the entry contract, and it remains narrower than [AOA-T-0041](../../../skill-discovery/skill-marketplace-curation/TECHNIQUE.md) because it does not curate or rank discovery
- it is now strong enough as a canonical default because the Nacos source repeats the same lookup-over-published-AgentCards shape in a separate live agent-registry family without requiring this bundle to absorb Nacos product semantics, endpoint subscription, A2A runtime invocation, console workflow, future filter roadmap, trust policy, or marketplace curation

## Fresh public-safety check
- review date: 2026-05-12
- result: pass
- sanitization still holds: the bundle keeps only the reusable discovery-query contract and excludes donor-specific network, ranking, trust, and runtime details
- public reuse check: the example, checklist, and adaptation notes remain understandable without hidden donor-repo context; the inspected `nacos-group/nacos-group.github.io` source is Apache-2.0 licensed and no source code, credentials, private deployment state, local endpoints, or Nacos-specific runtime setup was copied into the technique

## Remaining gaps
- no blocker remains for canonical status
- future discovery sources can reinforce the default, but they must preserve the narrow boundary: one lookup surface over already-published entries, explicit query fields or parameters, bounded match behavior, explicit result shape, and clear separation from ranking, trust, runtime invocation, subscription, marketplace curation, and registry governance

## Recommendation
- move `AOA-T-0064` to `canonical`
- add an adverse-effects review to preserve the boundary between capability discovery, versioned registry-entry publication, capability-spec ownership, endpoint subscription, runtime invocation, trust or signature policy, marketplace curation, graph semantics, and registry product governance
