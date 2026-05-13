# Canonical Readiness

## Technique
- id: AOA-T-0046
- name: repo-doc-surface-lift

## Verdict
- approve for canonical promotion

## Evidence summary
- origin evidence: `aoa-techniques` already projects a bounded repo-doc source set into generated repo-doc reader surfaces.
- second context: `nuxt-content/nuxt-llms` provides a public docs-to-`llms.txt` reader route, using configured sections and links as the bounded downstream reader object.
- second repo-owned route-manifest context: 8Dionysus derives `generated/public_route_map.min.json` from `docs/PUBLIC_ENTRY_POSTURE.md`, keeps `posture: route-map-only`, names canonical owner repos and authority refs, and validates the generated surface through builder and test coverage.
- validation strength: the bundle now has origin evidence, one public docs reader implementation, and one repo-owned public route manifest that preserves the same source-owned docs/status boundary without turning the generated reader into policy, release authority, or filesystem-wide docs taxonomy.

## Default-use rationale
- the technique is the right default when the exact question is "which authored repo doc should this reader open next?"
- it remains narrower than docs search, documentation conversion, policy routing, or full docs taxonomy.
- it is now the canonical default for a bounded public docs/status source set that needs a subordinate route reader or manifest, provided the authored docs remain the authority and the generated surface only routes to them.
- it still must not absorb owner-route doctrine, release semantics, public support policy, deeper guide selection, local planning docs, or semantic-review surfaces.

## Fresh public-safety check
- review date: 2026-05-13
- result: pass
- sanitization still holds: the note names only public repository paths, public source behavior, and reusable source-lift boundaries.
- public reuse check: an external reader can understand the pattern without OS Abyss, private docs, or hidden generator state.

## Remaining gaps
- no blocking gap remains for canonical use as long as the generated reader stays subordinate to the authored docs/status set.
- future review should watch for generated route maps becoming source truth, linked owner repositories losing authority to the route surface, or the source set widening into planning docs, deeper guides, semantic reviews, status policy, release policy, or general docs discovery.

## Recommendation
- promote `AOA-T-0046` to `canonical`
- use it as the default repo-doc route-surface lift when a bounded public docs/status layer needs a generated reader or manifest that points back to authored docs
