# Origin Evidence

## Technique
- id: AOA-T-0022
- name: risk-and-negative-effect-lift

## Source project
- name: aoa-techniques
- source files:
  - `docs/TECHNIQUE_SHADOW_GUIDE.md`
  - `docs/RISK_AND_NEGATIVE_EFFECT_LIFT_GUIDE.md`
  - `scripts/validate_repo.py`
  - published `TECHNIQUE.md` bundles across the live corpus

## Evidence
- `docs/TECHNIQUE_SHADOW_GUIDE.md` already defines the five-part shadow-language split as the current markdown-first caution contract
- `docs/RISK_AND_NEGATIVE_EFFECT_LIFT_GUIDE.md` already describes bounded caution lift as a later reusable source-lift surface without metadata or scoring
- `scripts/validate_repo.py` already enforces the fixed `Risks` subsection structure across published techniques
- the live corpus already uses the richer `Risks` shape, so caution lookup is grounded in an existing repo-wide authoring contract rather than a speculative future program

## Interpretation
- the reusable pattern already exists in a live public repository as markdown-first caution lift over authored `Risks`
- this technique does not invent a new caution layer; it generalizes the caution discipline that `aoa-techniques` already uses and keeps bounded
