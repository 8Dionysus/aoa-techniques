# Canonical Readiness

## Technique
- id: AOA-T-0019
- name: frontmatter-metadata-spine

## Verdict
- approve for canonical promotion

## Evidence summary
- origin evidence: the current catalog layer already projects bounded frontmatter into derived routing outputs, so the metadata spine is real and not hypothetical
- second context: `aoa-skills/generated/skill_catalog.json` provides live donor evidence for bounded `technique_refs` with `source_ref` and `use_sections`, `aoa-evals/generated/eval_catalog.json` provides bounded `evidence`, `relations`, and dependency metadata, and `aoa-routing` proves those generated min catalogs are actually ingested together
- validation strength: the bundle already has a checklist, a reusable example, and clear separation between metadata, derived catalog outputs, and markdown meaning, and the sibling repos now show the same spine surviving committed downstream consumers

## Default-use rationale
- this is the right default when a repository needs small routing fields for lookup, review posture, and direct adjacency without turning frontmatter into the technique's primary knowledge source
- it is the canonical bundle-level metadata entrypoint for the KAG/source-lift family when the next question is routing or lookup rather than section lift, provenance lift, relation lift, or caution review
- it remains narrower than section lift or provenance lift because it should help navigate the bundle, not replace the bundle's prose

## Fresh public-safety check
- review date: 2026-03-20
- result: pass
- sanitization still holds: the bundle keeps the reusable metadata-spine contract and strips project-specific implementation detail
- public reuse check: the current wording remains understandable without hidden repository context or a richer schema contract

## Remaining gaps
- no blocking gap remains for canonical use as long as the technique stays bounded to shallow metadata routing and does not widen into schema growth or markdown replacement
- future review should keep watching for catalog-overread and schema creep, but those are ongoing watch seams rather than promotion blockers

## Recommendation
- promote `AOA-T-0019` to `canonical`
- use `AOA-T-0019` as the default metadata-spine entrypoint for the KAG/source-lift family while keeping its contract bounded to routing and lookup
