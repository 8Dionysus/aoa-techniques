# Second Context Adaptation

## Technique
- id: AOA-T-0018
- name: markdown-technique-section-lift

## Target project
- name: aoa-techniques
- environment: public technique canon with authored markdown bundles, generated lookup surfaces, and no separate section-ID authoring system
- runtime: repository documentation and generated readers that need bounded section lookup without moving meaning out of markdown

## What changed
- paths: the source bundle is `techniques/docs/markdown-technique-section-lift/TECHNIQUE.md`; the derived surface is the section manifest and reader companion, not a new authored section store
- dependencies: the pattern depends on stable top-level headings and rebuildable derived outputs, not on graph behavior or section IDs
- operating assumptions: a public docs repository can lift stable headings into a bounded lookup surface while keeping authored prose as the only semantic home

## What stayed invariant
- contract: one markdown bundle remains the authoritative source of section meaning
- validation logic: the derived surface should rebuild from markdown and preserve heading order
- safety rules: metadata can help route readers, but it must not become the place where section meaning lives

## Risks introduced by adaptation
- a repository may start treating the lifted view as a substitute for the bundle instead of a routing aid
- metadata richness can make the lift feel more complete than it is, especially when the surrounding prose still carries the real contract
- a small stable heading set can drift into a shadow schema if consumers keep asking for more fields instead of reading the bundle

## Evidence
- `aoa-skills/docs/BRIDGE_SPEC.md` defines the donor contract for live reuse: stable technique section names are selected from `aoa-techniques`, `use_sections` controls what is lifted, `source_ref` pins the upstream donor commit, and the refresh/drift flow keeps that bridge reviewable
- `aoa-skills/generated/skill_catalog.json` shows the committed runtime projection of that contract, with `technique_refs` entries carrying `repo`, `path`, `source_ref`, and `use_sections` alongside the linked `technique_dependencies`
- `AOA-T-0002 source-of-truth-layout` still supports the same direction: meaning stays in the canonical bundle while the consumer gets a bounded derived surface
- `AOA-T-0012 deterministic-context-composition` still supports the same direction: a derived doc surface can remain subordinate to authored source authority instead of becoming the semantic home

## Result
- works as a bounded cross-repo adaptation grounded in a committed `aoa-skills` consumer, not just a repo-local sketch, while still leaving one gap: another live markdown-first consumer beyond the current bridge pattern
