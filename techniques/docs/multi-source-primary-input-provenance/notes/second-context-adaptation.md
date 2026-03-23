# Second Context Adaptation

## Technique
- id: AOA-T-0043
- name: multi-source-primary-input-provenance

## Target project
- name: aoa-techniques
- environment: public documentation repository for reusable engineering techniques

## What changed
- bridge-oriented source ordering was reduced to a public docs contract
- the technique stays at the level of primary-versus-supporting input priority
- graph semantics, ranking, and traversal were kept out of scope

## What stayed invariant
- when multiple sources are combined, one source can be named as primary
- the supporting inputs still matter, but they do not replace the primary input
- the ordering remains visible in authored markdown

## Risks introduced by adaptation
- the wording can drift into note provenance or relation semantics if the boundary is not restated
- readers may assume the contract is a ranking system if priority language is left vague
- a bridge surface can accidentally hide which input is primary if the example is too generic

## Evidence
- `aoa-kag` keeps the multi-source bridge contract explicit with exactly one `primary` input and additional `supporting` inputs
- `Tree-of-Sophia` keeps conceptual origin authored while allowing derived bridge projection to stay downstream and explicit
- the adapted bundle preserves the same smaller seam: source-priority ordering remains visible without importing graph traversal, note provenance handles, or ranking doctrine

## Result
- verdict: works
- note: the adapted bundle reads as a bounded docs technique for explicit source-priority ordering
