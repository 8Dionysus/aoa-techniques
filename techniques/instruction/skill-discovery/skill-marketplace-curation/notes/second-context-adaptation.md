# Second Context Adaptation

## Technique
- id: AOA-T-0041
- name: skill-marketplace-curation

## Target project
- name: aoa-techniques
- environment: public library repository with technique bundles, generated catalog surfaces, and explicit evidence-note discipline
- runtime: documentation-first repository that records the curation pattern rather than shipping the donor marketplace implementation

## What changed

- paths: the donor uses one live marketplace repository with categories, discovery files, and sync helpers; this adaptation presents a generic local curation layer that can fit other public collections
- services: no installer, registry generator, or sync workflow is required in this repository
- dependencies: the adaptation depends on editorial grouping, short summaries, and visible upstream ownership, not on the donor marketplace tooling
- operating assumptions: contributors should treat the curated layer as discovery-only and keep sync or provenance substrate visibly separate

## What stayed invariant

- contract: one local surface curates discoverability over upstream-owned skills
- validation logic: the curated entries remain legible as upstream-owned while the local layer adds editorial value
- safety rules: the local marketplace stays subordinate to upstream ownership and does not silently become registry, installer, or capability truth

## Risks introduced by adaptation

- the pattern can become vague if a project copies upstream entries but adds no real editorial value
- some repositories may keep category and summary language but let the surface drift into hidden routing or marketplace policy

## Evidence

- the donor README describes the repository as a curated marketplace, names `AGENTS.md` as the universal discovery file, and uses categories plus featured-quality language to shape how skills are surfaced
- the donor also keeps auto-sync and attribution in adjacent surfaces, which makes it possible to import curation separately from sync substrate
- this imported technique narrows those behaviors into one reusable docs pattern for local discoverability over upstream-owned skills

## Result

- works as a documentation-first second context and preserves the bounded core without carrying over donor-specific installer, registry, or sync breadth
