# Canonical Readiness

## Technique
- id: AOA-T-0022
- name: risk-and-negative-effect-lift

## Verdict
- defer for now

## Evidence summary
- origin evidence: the bundle already has the fixed `Risks` contract plus the public caution-lift guide that keeps the markdown-first split explicit
- second context: committed sibling repos add live donor surfaces for the caution vocabulary, including `aoa-skills/skills/aoa-safe-infra-change/SKILL.md` `Risks and anti-patterns` language and `aoa-evals/bundles/aoa-bounded-change-quality/EVAL.md` plus `aoa-evals/bundles/aoa-eval-integrity-check/EVAL.md` failure/blind-spot surfaces, but they do not reproduce the same five-part `Risks` contract, so this is contrast evidence rather than a positive analogy
- validation strength: the bundle already has a checklist, an example, and explicit markdown-first caution routing, but it still lacks another committed corpus proving the exact five-part `Failure modes`, `Negative effects`, `Misuse patterns`, `Detection signals`, `Mitigations` split in practice

## Default-use rationale
- this remains the right default when one bundle needs bounded caution lookup over `Risks` without turning that lookup into scoring or policy
- it is narrower than a threat model, incident taxonomy, or policy-scoring framework because the core contract is still review-oriented markdown lookup
- the bundle should stay promoted with a bounded defer reason until another committed corpus proves that the same caution split remains useful outside this public canon

## Fresh public-safety check
- review date: 2026-03-20
- result: pass
- sanitization still holds: the bundle keeps the reusable markdown-first caution pattern and strips repo-local implementation trivia
- public reuse check: the pattern remains understandable without hidden automation or private source files

## Remaining gaps
- the main missing proof is live reuse of the exact five-part `Risks` contract in another committed repository
- a future canonical review should show that caution lookup survives repeated use without turning into generated policy, scoring, or metadata replacement for `Risks`

## Recommendation
- keep `AOA-T-0022` `promoted`
- defer canonical promotion until the technique proves itself in a live reuse context that reuses the same five-part `Risks` contract, not just adjacent caution or blind-spot language
