# Second Context Adaptation

## Technique
- id: AOA-T-0021
- name: bounded-relation-lift-for-kag

## Target project
- name: aoa-techniques
- environment: public technique canon with derived navigation surfaces and reviewable direct relations between bundles
- runtime: documentation-first repository where adjacency hints should stay bounded and easy to inspect

## What changed
- paths: the relation layer is surfaced through committed sibling repos, not through a graph subsystem
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
- `aoa-evals/bundles/aoa-eval-integrity-check/eval.yaml` carries direct typed `relations` alongside explicit `technique_dependencies` and `skill_dependencies`, keeping the edge layer small and inspectable
- `aoa-evals/generated/eval_catalog.json` lifts those relations into generated catalog entries as bounded direct-edge metadata, not as a traversal graph
- `aoa-routing/scripts/router_core.py` builds `recommended_paths` from `technique_dependencies` and `skill_dependencies`, and the hop construction is dependency-driven rather than relation-hint-driven
- `AOA-T-0019 frontmatter-metadata-spine` still proves that this repository can keep routing metadata shallow while meaning stays in markdown
- `AOA-T-0018 markdown-technique-section-lift` still proves that derived lookup surfaces can remain bounded and subordinate to authored bundles

## Result
- works as a bounded cross-repo adaptation with live donor evidence from `aoa-evals` and `aoa-routing`, while still needing one more direct-relation consumer outside eval bundles before canonical readiness
