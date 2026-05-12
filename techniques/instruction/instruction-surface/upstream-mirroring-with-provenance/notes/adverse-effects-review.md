# Adverse Effects Review

## Technique
- id: AOA-T-0024
- name: upstream-mirroring-with-provenance

## Review focus
- current role: canonical default for mirroring upstream-owned content into a local curated collection while preserving explicit source ownership and adjacent provenance
- current watch seam: keep the bundle centered on mirror provenance and subordinate local copies rather than marketplace curation, installer behavior, registry generation, sync policy, or local canonical-source fan-out

## Failure modes
- mirrored content is edited locally until the upstream source no longer owns the meaning in practice
- provenance metadata exists but no longer matches the mirrored payload or source manifest
- fetch pins and import scripts look trustworthy while reviewers can no longer tell which content is upstream-owned and which content is local wrapper material
- local metadata is injected into upstream markdown and blurs the boundary between mirrored payload and local curation

## Negative effects
- canonical status can encourage projects to mirror more upstream content than they can review or refresh
- provenance overhead can become ceremonial if the mirror is rarely resynced or checked
- a convenient local copy can reduce attention to upstream license, maintenance, and authorship changes
- tightly pinned mirrors can lag behind important upstream fixes if stale pins are never reviewed

## Misuse patterns
- using the technique as a generic marketplace, registry, or installer contract
- treating mirrored local files as new canonical sources because they live in the current repository
- adding local policy, categories, or compatibility metadata directly to the mirrored upstream payload
- claiming provenance from a source manifest while dropping adjacent attribution or local wrapper separation

## Detection signals
- pull requests edit mirrored payloads directly without touching the source manifest, provenance record, or upstream reference
- reviewers cannot name the upstream repository, source path, and local destination from the local files alone
- local wrapper notes and upstream payloads are mixed in the same file
- sync or import changes are discussed mainly as convenience tooling rather than ownership preservation

## Mitigations
- keep upstream source, local destination, and provenance carrier visible together
- keep local metadata in sibling files or wrapper surfaces instead of mutating upstream markdown
- review source manifests and adjacent provenance whenever mirrored payloads change
- route editorial curation, health checking, installer behavior, and registry policy to sibling techniques
- revisit canonical status if the bundle is used mainly to justify bulk copying rather than reviewable upstream-owned mirrors

## Recommendation
- keep current `canonical` status and use this note as the watch surface for local-copy authority drift, stale provenance, wrapper/payload mixing, and sync-substrate overreach
