# Canonical Readiness

## Technique
- id: AOA-T-0019
- name: frontmatter-metadata-spine

## Verdict
- stronger ready, still promoted

## Evidence summary
- origin evidence: the current catalog layer already projects bounded frontmatter into derived routing outputs, so the metadata spine is real and not hypothetical
- second context: `aoa-skills/generated/skill_catalog.json` provides live donor evidence for bounded `technique_refs` with `source_ref` and `use_sections`, `aoa-evals/generated/eval_catalog.json` provides bounded `evidence`, `relations`, and dependency metadata, and `aoa-routing` proves those generated min catalogs are actually ingested together
- validation strength: the bundle already has a checklist, a reusable example, and clear separation between metadata, derived catalog outputs, and markdown meaning, and the sibling repos now show the same spine surviving committed downstream consumers

## Default-use rationale
- this is the right default when a repository needs small routing fields for lookup, review posture, and direct adjacency without turning frontmatter into the technique's primary knowledge source
- it remains narrower than section lift or provenance lift because it should help navigate the bundle, not replace the bundle's prose
- it is now the first canonical candidate in the family because the same bounded spine is visible in committed skill, eval, and routing consumers, but the technique still belongs in `promoted` until a future wave chooses to elevate it

## Fresh public-safety check
- review date: 2026-03-20
- result: pass
- sanitization still holds: the bundle keeps the reusable metadata-spine contract and strips project-specific implementation detail
- public reuse check: the current wording remains understandable without hidden repository context or a richer schema contract

## Remaining gaps
- the remaining gap is not donor existence but promotion timing: the technique is ready enough to lead the family, but this wave keeps it `promoted`
- a future canonical review should still confirm that shallow frontmatter remains enough even when a downstream routing problem is slightly different

## Recommendation
- keep `AOA-T-0019` `promoted`
- treat `AOA-T-0019` as the first promotion candidate for canonical review in the next wave, but do not change the status in this wave
