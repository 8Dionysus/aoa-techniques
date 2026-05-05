# Second Context Adaptation

## Technique
- id: AOA-T-0022
- name: risk-and-negative-effect-lift

## Target project
- name: aoa-skills
- environment: public skill repository with authored `SKILL.md` bundles, generated reader surfaces, and stable markdown caution sections
- runtime: markdown-first skill corpus where caution language must stay reviewable without becoming generated policy or scoring

## What changed
- paths: the exact five-part caution contract is now reused inside one skill-local `Risks and anti-patterns` section instead of only inside technique bundles
- services: there is still no scoring engine, caution policy service, or generated caution program in the donor repo
- dependencies: the adaptation depends on authored markdown sections in `SKILL.md`, not on metadata widening or generated caution outputs
- operating assumptions: a public skill repository can keep richer caution lookup bounded and review-oriented while still treating the authored skill markdown as the source of meaning

## What stayed invariant
- contract: `Risks` remains the primary caution source for the bundle
- validation logic: caution questions should still route back to authored markdown when meaning matters
- safety rules: bounded caution lookup must not become metadata, scoring, or generated policy

## Risks introduced by adaptation
- one skill-local caution surface can look broader than it really is if readers mistake the first donor for repeated cross-repo reuse
- future generated reader surfaces could tempt maintainers to flatten the five-part caution split into metadata
- the exact five-part split could drift back into generic risk prose if later skill updates stop keeping the headings explicit

## Evidence
- merged `aoa-skills@b1b3fc7b330f2fecc5412c0444bc108b4aecc67c` now gives `skills/aoa-sanitized-share/SKILL.md` the exact five headings `Failure modes`, `Negative effects`, `Misuse patterns`, `Detection signals`, and `Mitigations`
- the same donor keeps the caution split inside authored skill markdown, so the contract stays reviewable and markdown-first rather than becoming generated policy
- adjacent sibling-repo caution surfaces in `aoa-evals` still matter as contrast evidence, but they are no longer the only live context because `aoa-skills` now reproduces the exact five-part split directly
- this closes the first exact-contract donor gap, while still leaving one more independent-corpus reinforcement gap in place for canonical review

## Result
- works as a first live second-context adaptation for the exact five-part `Risks` contract, while still needing one more independent corpus before any future canonical review
