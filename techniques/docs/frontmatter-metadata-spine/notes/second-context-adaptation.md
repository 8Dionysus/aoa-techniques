# Second Context Adaptation

## Technique
- id: AOA-T-0019
- name: frontmatter-metadata-spine

## Target project
- name: aoa-techniques
- environment: public library repository with technique bundles, a generated catalog, and reader-facing navigation surfaces
- runtime: markdown-first repository where frontmatter must stay shallow and derived outputs stay subordinate to authored bundle meaning

## What changed
- paths: the origin contract is now grounded in committed sibling surfaces, with `aoa-skills/generated/skill_catalog.json` carrying bounded `technique_refs` that pair `repo`, `path`, `source_ref`, and `use_sections`, `aoa-evals/generated/eval_catalog.json` carrying bounded `evidence`, `relations`, and dependency metadata, and `aoa-routing` ingesting the generated min catalogs from all three sibling repos
- services: there is no need for additional schema layers, graph behavior, or hand-authored metadata mirrors in this repository because the live donor surfaces already prove the routing spine can stay bounded
- dependencies: the adaptation depends on a small stable set of frontmatter fields plus regenerated catalogs, not on richer metadata modeling or repo-local sketch logic
- operating assumptions: public docs can use frontmatter for identity and routing while markdown keeps the actual technique meaning, and the sibling repos already show that the downstream consumers can stay committed and reviewable

## What stayed invariant
- contract: shallow frontmatter can still act as a bounded spine for bundle lookup and review posture
- validation logic: routing should still come from derived catalog outputs, not from manually edited metadata copies
- safety rules: markdown meaning stays authoritative and frontmatter does not become the primary knowledge source

## Risks introduced by adaptation
- the repository could start treating the catalog as a substitute for reading the bundle itself
- frontmatter could widen into a schema-first surface if future KAG work keeps asking for more fields instead of narrower routing
- small metadata changes could drift into the illusion that the technique owns more meaning than it actually does

## Evidence
- `aoa-skills/generated/skill_catalog.json` shows bounded technique reuse in practice: each `technique_refs` entry can pin a donor commit through `source_ref` and constrain lift through `use_sections`, which keeps the consumer tied to specific markdown sections instead of generic provenance prose
- `aoa-evals/generated/eval_catalog.json` shows the same bounded pattern on the proof side: `evidence` stays typed, `relations` stay explicit, and technique and skill dependency metadata remain separate from the eval text itself
- `aoa-routing/README.md` and `aoa-routing/scripts/build_router.py` show the routing consumer is built from generated min catalogs in `aoa-techniques`, `aoa-skills`, and `aoa-evals`, so the spine is already live in the family rather than hypothetical
- `AOA-T-0002 source-of-truth-layout` still proves this repository values one canonical home per information class rather than many drifting copies
- `AOA-T-0018 markdown-technique-section-lift` still proves that the repo supports derived lift surfaces while keeping authored markdown authoritative

## Result
- works as the strongest live family example for the metadata-spine contract and the first canonical promotion candidate, while still staying `promoted` in this wave because the contract remains bounded to routing and lookup rather than replacing markdown meaning
