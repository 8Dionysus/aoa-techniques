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
- `AOA-T-0002 source-of-truth-layout` already proves that this repository prefers canonical homes for meaning instead of duplicate role copies
- `AOA-T-0012 deterministic-context-composition` already proves that this repository can publish bounded derived doc surfaces while preserving authored source authority
- the current section-lift bundle fits those instincts by keeping lookup derived and section meaning rooted in markdown

## Result
- works as a bounded repo-local adaptation sketch for a promoted source-lift technique, while still needing stronger live reuse evidence before any future canonical review
