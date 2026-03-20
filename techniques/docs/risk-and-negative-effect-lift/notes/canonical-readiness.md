# Canonical Readiness

## Technique
- id: AOA-T-0022
- name: risk-and-negative-effect-lift

## Verdict
- defer for now

## Evidence summary
- origin evidence: the bundle already has the fixed `Risks` contract plus the public caution-lift guide that keeps the markdown-first split explicit
- second context: the adaptation note shows the contract clearly enough to stay reusable, but it still reads as a repo-local caution sketch rather than a live cross-repo proof
- validation strength: the bundle already has a checklist, an example, and explicit markdown-first caution routing, but it still lacks another markdown-first corpus proving the same caution-lift split in practice

## Default-use rationale
- this remains the right default when one bundle needs bounded caution lookup over `Risks` without turning that lookup into scoring or policy
- it is narrower than a threat model, incident taxonomy, or policy-scoring framework because the core contract is still review-oriented markdown lookup
- the bundle should stay promoted until another corpus proves that the same caution split remains useful outside this public canon

## Fresh public-safety check
- review date: 2026-03-20
- result: pass
- sanitization still holds: the bundle keeps the reusable markdown-first caution pattern and strips repo-local implementation trivia
- public reuse check: the pattern remains understandable without hidden automation or private source files

## Remaining gaps
- the main missing proof is live reuse in another markdown-first repository
- a future canonical review should show that caution lookup survives repeated use without turning into generated policy, scoring, or metadata replacement for `Risks`

## Recommendation
- keep `AOA-T-0022` `promoted`
- defer canonical promotion until the technique proves itself in a live reuse context beyond the current repo-local sketch
