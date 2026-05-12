# Canonical Readiness

## Technique
- id: AOA-T-0046
- name: repo-doc-surface-lift

## Verdict
- defer for now

## Evidence summary
- origin evidence: `aoa-techniques` already projects a bounded repo-doc source set into generated repo-doc reader surfaces.
- second context: `nuxt-content/nuxt-llms` provides a public docs-to-`llms.txt` reader route, using configured sections and links as the bounded downstream reader object.
- validation strength: the bundle now has origin evidence plus first non-origin reader evidence, but the second context is a framework module example rather than another repository's durable maintainer-facing route manifest.

## Default-use rationale
- the technique is the right default when the exact question is "which authored repo doc should this reader open next?"
- it remains narrower than docs search, documentation conversion, policy routing, or full docs taxonomy.
- the fresh second-context evidence makes the pattern real beyond `aoa-techniques`, but canonical promotion should wait until one more public corpus or repo-owned route surface shows the same bounded source-owned docs set feeding a subordinate reader without framework-specific assumptions.

## Fresh public-safety check
- review date: 2026-05-12
- result: pass
- sanitization still holds: the note names only public repository paths, public source behavior, and reusable source-lift boundaries.
- public reuse check: an external reader can understand the pattern without OS Abyss, private docs, or hidden generator state.

## Remaining gaps
- one more non-origin repo-owned source set or route manifest would show that the pattern is not only an `llms.txt` framework feature.
- a future canonical review should prove that local planning docs, deeper guides, and review surfaces still stay outside the bounded repo-doc source class.

## Recommendation
- keep `AOA-T-0046` `promoted`
- carry the Nuxt LLMs evidence as first second-context support, not as a status flip
