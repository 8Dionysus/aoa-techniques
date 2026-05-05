# Second Context Adaptation

## Technique
- id: AOA-T-0024
- name: upstream-mirroring-with-provenance

## Target project
- name: aoa-techniques
- environment: public library repository with technique bundles, generated catalog surfaces, and explicit provenance-note discipline
- runtime: documentation-first repository that records the mirroring pattern rather than shipping the donor sync engine itself

## What changed
- paths: the donor uses `sources.yaml` plus mirrored skill folders; this adaptation presents a generic source-manifest pattern that can fit other curated local collections
- services: no GitHub Actions cron, installer integration, or registry generator is required in this repository
- dependencies: the adaptation depends on declared source ownership, repeatable mirroring, and adjacent provenance, not on the donor sync scripts
- operating assumptions: contributors should treat mirrored copies as subordinate to upstream ownership and keep local wrapper notes visibly separate

## What stayed invariant
- contract: one explicit source manifest declares what is mirrored and from where
- validation logic: mirrored content remains traceable to upstream through adjacent provenance metadata
- safety rules: local copies stay subordinate to upstream ownership and do not silently become new canonical sources

## Risks introduced by adaptation
- the pattern can become vague if a project copies mirrored content but drops the adjacent provenance signal
- some repositories may keep provenance files but stop using the manifest as the actual sync authority

## Evidence
- the donor `README.md` describes `sources.yaml` as the upstream external skill manifest and `.source.json` as the preserved attribution marker for synced skills
- the donor auto-sync section keeps upstream ownership explicit by naming the source repo, mirrored copy, and repeated refresh path
- this imported technique narrows those behaviors into one reusable docs pattern for manifest-driven mirroring with provenance

## Result
- works as a documentation-first second context and preserves the bounded core without carrying over donor-specific marketplace or registry breadth
