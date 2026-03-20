# Canonical Readiness

## Technique
- id: AOA-T-0019
- name: frontmatter-metadata-spine

## Verdict
- defer for now

## Evidence summary
- origin evidence: the current catalog layer already projects bounded frontmatter into derived routing outputs, so the metadata spine is real and not hypothetical
- second context: the repo-local adaptation note shows the same contract surviving in `aoa-techniques` as a public routing layer rather than as schema expansion
- validation strength: the bundle already has a checklist, a reusable example, and clear separation between metadata, derived catalog outputs, and markdown meaning

## Default-use rationale
- this is the right default when a repository needs small routing fields for lookup, review posture, and direct adjacency without turning frontmatter into the technique's primary knowledge source
- it remains narrower than section lift or provenance lift because it should help navigate the bundle, not replace the bundle's prose

## Fresh public-safety check
- review date: 2026-03-20
- result: pass
- sanitization still holds: the bundle keeps the reusable metadata-spine contract and strips project-specific implementation detail
- public reuse check: the current wording remains understandable without hidden repository context or a richer schema contract

## Remaining gaps
- the missing proof is a second live context where the same bounded metadata spine is reused outside this repository narrative
- a future canonical review should show that shallow frontmatter remains enough even when the downstream routing problem is slightly different

## Recommendation
- keep `AOA-T-0019` `promoted`
- defer canonical promotion until the technique proves itself in another live reuse context and the metadata spine still stays shallow
