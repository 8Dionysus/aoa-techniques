# Second Context Adaptation

## Technique
- id: AOA-T-0019
- name: frontmatter-metadata-spine

## Target project
- name: aoa-techniques
- environment: public library repository with technique bundles, a generated catalog, and reader-facing navigation surfaces
- runtime: markdown-first repository where frontmatter must stay shallow and derived outputs stay subordinate to authored bundle meaning

## What changed
- paths: the origin uses a richer internal catalog spine; this adaptation keeps the same bounded routing idea but maps it onto public technique bundles and generated catalog surfaces
- services: there is no need for additional schema layers, graph behavior, or hand-authored metadata mirrors in this repository
- dependencies: the adaptation depends on a small stable set of frontmatter fields plus a regenerated catalog, not on richer metadata modeling
- operating assumptions: public docs can use frontmatter for identity and routing while markdown keeps the actual technique meaning

## What stayed invariant
- contract: shallow frontmatter can still act as a bounded spine for bundle lookup and review posture
- validation logic: routing should still come from derived catalog outputs, not from manually edited metadata copies
- safety rules: markdown meaning stays authoritative and frontmatter does not become the primary knowledge source

## Risks introduced by adaptation
- the repository could start treating the catalog as a substitute for reading the bundle itself
- frontmatter could widen into a schema-first surface if future KAG work keeps asking for more fields instead of narrower routing
- small metadata changes could drift into the illusion that the technique owns more meaning than it actually does

## Evidence
- `AOA-T-0002 source-of-truth-layout` already proves this repository values one canonical home per information class rather than many drifting copies
- `AOA-T-0018 markdown-technique-section-lift` proves that the repo already supports derived lift surfaces while keeping authored markdown authoritative
- the current catalog and selection surfaces already consume `AOA-T-0019`-style metadata in a bounded, derived way rather than as a replacement for the bundle text

## Result
- works as a bounded repo-local adaptation sketch for a first promoted draft, while still needing stronger reuse evidence before any future canonical review
