# Second Context Adaptation

## Technique
- id: AOA-T-0022
- name: risk-and-negative-effect-lift

## Target project
- name: aoa-techniques
- environment: public library repository with markdown-first technique bundles, validator-enforced Risks language, and canonical adverse-effects review notes on already-canonical bundles
- runtime: documentation-first repository that can describe the pattern clearly even when it does not automate any caution policy layer directly

## What changed
- paths: the source guide and live corpus were shaped into one bounded markdown-first caution-lift contract for reuse across review surfaces
- services: there is no local scoring engine, caution policy service, or generated caution program in this repository
- dependencies: the adaptation depends on authored `Risks` prose and explicit note-backed review surfaces, not on private safety tooling or metadata expansion
- operating assumptions: a public docs-oriented repository can keep caution lookup bounded while still letting canonical bundles add a supplemental adverse-effects review note

## What stayed invariant
- contract: `Risks` remains the primary caution source for the bundle
- validation logic: caution questions should still route back to authored markdown when meaning matters
- safety rules: bounded caution lookup must not become metadata, scoring, or generated policy

## Risks introduced by adaptation
- a small repository may over-abstract the pattern and start treating caution lookup as a policy layer
- without the underlying markdown contract, contributors could describe the caution split well but fail to keep it reviewable
- the presence of a canonical supplement could blur the boundary unless it stays explicitly downstream from `Risks`

## Evidence
- `AOA-T-0022` already has the fixed five-part `Risks` shape that the caution-lift contract needs
- `AOA-T-0022` already sits beside the canonical-only adverse-effects review note pattern, which keeps caution review bounded without introducing metadata policy
- this adaptation combines those repository-native instincts into a bounded sketch for markdown-first caution lookup without making caution authoritative over the bundle
- this is sufficient as repo-local adaptation evidence for a first promoted draft, but it is not enough to argue for canonical status on its own

## Result
- works as a bounded repo-local adaptation sketch for a first promoted draft, while still needing stronger live reuse evidence before any future canonical review
