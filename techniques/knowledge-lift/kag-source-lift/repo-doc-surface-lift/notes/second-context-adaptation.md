# Second Context Adaptation

## Technique
- id: AOA-T-0046
- name: repo-doc-surface-lift

## Target project
- first support name: nuxt-llms
- first support repository: `nuxt-content/nuxt-llms`
- first support observed revision: `6faa1c45e082274267eae9295b501ab0053d0365`
- first support public surfaces:
  - `src/runtime/server/routes/llms.txt.get.ts`
  - `src/runtime/types.ts`
- second support name: 8Dionysus public route map
- second support repository: `8Dionysus`
- second support public surfaces:
  - `docs/PUBLIC_ENTRY_POSTURE.md`
  - `scripts/public_route_map_common.py`
  - `generated/public_route_map.min.json`
  - `tests/test_public_route_map.py`

## What changed
- docs reader shape: Nuxt LLMs turns configured documentation sections into a `llms.txt` reader route made of titles, descriptions, links, and notes.
- source boundary: the reader route is downstream from configured documentation metadata rather than the authored docs themselves becoming generated truth.
- route purpose: the generated text surface answers "which docs links should an LLM or reader open?" rather than replacing the source documentation or becoming a product-wide docs taxonomy.
- route-map shape: 8Dionysus turns one authored public-entry posture table into a compact generated route map with route ids, canonical owner repos, capsule refs, authority refs, and verification refs.
- second-context fit: 8Dionysus closes the missing repo-owned route-manifest proof because the generated route map is explicitly `route-map-only`, derived from `docs/PUBLIC_ENTRY_POSTURE.md`, and validated without becoming owner authority for sibling repos.

## What stayed invariant
- authored documentation and configured doc links remain the source layer.
- the derived reader is route-oriented and bounded.
- the reader output is useful because it points back to source docs instead of embedding all meaning.
- the surface does not claim release policy, status policy, scoring, or filesystem-wide doc discovery authority.
- sibling owner truth stays in the owning repositories; the route map only points to canonical homes and verification refs.

## Risks introduced by adaptation
- an `llms.txt` surface can be mistaken for a full docs authority if maintainers stop routing readers back to source docs.
- a framework module can hide which source set was intentionally selected unless the configuration remains explicit.
- broad "LLM-ready docs" tooling can drift into documentation conversion rather than repo-doc routing; this bundle only uses the bounded route-reader portion.
- a public route map can overreach if it starts owning linked repo semantics instead of remaining an orientation surface.
- route manifests can become noisy if low-context implementation refs replace the curated public docs/status layer.

## Evidence
- `src/runtime/server/routes/llms.txt.get.ts` builds a text route from configured sections and link entries.
- `src/runtime/types.ts` defines section entries with `title`, optional `description`, and linked `href` values, keeping the reader surface route-shaped.
- the public module repository provides a real non-origin implementation of docs-to-reader projection without making the generated reader the authored source of meaning.
- `8Dionysus/docs/PUBLIC_ENTRY_POSTURE.md` owns the public onboarding table and states that the repository is a route map, not a hidden center of authority.
- `8Dionysus/scripts/public_route_map_common.py` parses that authored table, enforces exactly three public onboarding routes, validates canonical owner repos, blocks low-context `src/` and `scripts/` repo refs in route targets, and emits `generated/public_route_map.min.json`.
- `8Dionysus/generated/public_route_map.min.json` records `owner_repo`, `surface_kind`, `authority_ref`, `posture: route-map-only`, validation refs, and route entries back to authored owner surfaces.
- `8Dionysus/tests/test_public_route_map.py` checks the route map remains orientation-only, keeps expected canonical homes, preserves workspace/profile route refs, and does not leak implementation refs into the rendered payload.

## Result
- cross-context adaptation accepted
- the Nuxt LLMs reader proves the route-reader shape outside `aoa-techniques`
- the 8Dionysus public route map proves the repo-owned route-manifest shape outside framework-specific `llms.txt` generation
- promote `AOA-T-0046` to canonical while keeping owner authority, policy, release semantics, and broader docs taxonomy outside the bundle
