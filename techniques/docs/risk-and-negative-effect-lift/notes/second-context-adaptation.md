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
- `aoa-skills/skills/aoa-safe-infra-change/SKILL.md` shows live caution language as `Risks and anti-patterns`, including explicit risk naming and rollback thinking, but its contract stays skill-local rather than reproducing the same five-part technique `Risks` split
- `aoa-evals/bundles/aoa-bounded-change-quality/EVAL.md` and `aoa-evals/bundles/aoa-eval-integrity-check/EVAL.md` show live failure-mode and blind-spot surfaces for bounded review, but they remain eval surfaces rather than authored technique `Risks`
- taken together, those committed sibling repos prove that the caution vocabulary is live in adjacent donor surfaces, but they do not provide an equally strong second corpus for the exact five-part `Risks` contract
- this is therefore a contrast-based live evidence read, not a forced positive analogy, and it still leaves the same bounded defer reason in place for canonical review

## Result
- works as a bounded contrast-based adaptation read for a first promoted draft, while still needing stronger live reuse of the exact five-part `Risks` contract before any future canonical review
