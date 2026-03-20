# Second Context Adaptation

## Technique
- id: AOA-T-0021
- name: bounded-relation-lift-for-kag

## Target project
- name: aoa-techniques
- environment: public technique canon with derived navigation surfaces and reviewable direct relations between bundles
- runtime: documentation-first repository where adjacency hints should stay bounded and easy to inspect

## What changed
- paths: the relation layer is surfaced through `docs/SELECTION_PATTERNS.md` and the generated catalog, not through a graph subsystem
- dependencies: the technique depends on direct typed `relations` plus reviewable markdown bundles, not on inference engines or relation scoring
- operating assumptions: a public repository can use direct typed hints to guide nearby inspection without promoting the hints into explanation or traversal policy

## What stayed invariant
- contract: one typed relation still means one bounded adjacency hint
- validation logic: direct targets should stay explicit and inspectable in the authored bundle
- safety rules: rationale, weighting, and multi-hop interpretation stay out of the relation field

## Risks introduced by adaptation
- direct edges can look more authoritative than they are if readers stop opening the underlying bundles
- generated navigation surfaces can encourage relation drift if maintainers start adding edges to satisfy discoverability instead of semantic clarity
- the pattern can drift into graph-like thinking if future consumers ask the relation layer to answer "why" or "what next next" questions

## Evidence
- `AOA-T-0019 frontmatter-metadata-spine` already proves that this repository can keep routing metadata shallow while meaning stays in markdown
- `AOA-T-0018 markdown-technique-section-lift` already proves that derived lookup surfaces can remain bounded and subordinate to authored bundles
- the current `SELECTION_PATTERNS.md` surface already consumes direct relations as nearby-hint navigation rather than as graph traversal

## Result
- works as a bounded repo-local adaptation sketch for direct typed relation hints, while still needing stronger live reuse evidence before any future canonical review
