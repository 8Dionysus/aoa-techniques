# Second Context Adaptation

## Technique
- id: AOA-T-0020
- name: evidence-note-provenance-lift

## Target project
- name: aoa-techniques
- environment: public technique canon with typed supporting notes and derived manifests
- runtime: markdown-first repository where provenance lookup must stay readable to humans and agents

## What changed
- note kinds: the public form keeps typed note kinds such as origin, second-context adaptation, and canonical readiness instead of flattening all notes into one generic support bucket
- paths: the public form keeps note paths explicit so each supporting note remains independently reachable
- dependencies: the adaptation depends on authored markdown notes plus a derived manifest, not on note IDs or cross-note graph behavior
- operating assumptions: a public repository can expose provenance handles for note lookup while still leaving the note body as the place where interpretation lives

## What stayed invariant
- contract: provenance remains note-kind plus note-path lookup
- validation logic: readers can find the supporting note without losing the authored note text
- safety rules: the manifest stays derived and does not become the source of truth for note meaning

## Risks introduced by adaptation
- note kinds can multiply if future bundles start splitting provenance roles too finely
- a derived manifest can look complete even when the supporting note text still carries the real judgment
- if the note kind layer becomes too clever, maintainers may start expecting graph semantics that the technique does not claim

## Evidence
- `AOA-T-0018 markdown-technique-section-lift` already proves this repository is comfortable with bounded derived lookup over authored markdown
- `AOA-T-0019 frontmatter-metadata-spine` already proves the repo can keep shallow metadata derived while leaving real meaning in markdown
- this technique fits the same public pattern by keeping provenance handles small, explicit, and markdown-first

## Result
- works as a bounded repo-local adaptation sketch for a first promoted draft, while still needing stronger live reuse evidence before any future canonical review
