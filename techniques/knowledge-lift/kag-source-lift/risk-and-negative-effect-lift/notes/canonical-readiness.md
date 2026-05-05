# Canonical Readiness

## Technique
- id: AOA-T-0022
- name: risk-and-negative-effect-lift

## Verdict
- bounded defer for now

## Evidence summary
- origin evidence: the bundle already has the fixed `Risks` contract plus the public caution-lift guide that keeps the markdown-first split explicit
- second context: merged `aoa-skills@b1b3fc7b330f2fecc5412c0444bc108b4aecc67c` now adds the exact five-part caution split to `skills/aoa-sanitized-share/SKILL.md`, so the contract is no longer only contrast-based inside sibling repos
- validation strength: the bundle already has a checklist, an example, explicit markdown-first caution routing, and one real sibling-repo donor for the exact split, but it still lacks a second independent corpus beyond the first skill-local caution surface

## Default-use rationale
- this remains the right default when one bundle needs bounded caution lookup over `Risks` without turning that lookup into scoring or policy
- it is narrower than a threat model, incident taxonomy, or policy-scoring framework because the core contract is still review-oriented markdown lookup
- the bundle should stay promoted with a bounded defer reason until another committed corpus proves that the same caution split remains useful beyond the first `aoa-skills` donor

## Fresh public-safety check
- review date: 2026-03-21
- result: pass
- sanitization still holds: the bundle keeps the reusable markdown-first caution pattern and strips repo-local implementation trivia
- public reuse check: the pattern remains understandable without hidden automation or private source files

## Remaining gaps
- the main missing proof is one more committed reuse of the exact five-part `Risks` contract beyond the first `aoa-skills` donor
- a future canonical review should show that caution lookup survives repeated use in more than one non-techniques corpus without turning into generated policy, scoring, or metadata replacement for `Risks`

## Recommendation
- keep `AOA-T-0022` `promoted`
- defer canonical promotion until the technique proves itself in one more live reuse context that reuses the same five-part `Risks` contract, not just the first committed `aoa-skills` donor
