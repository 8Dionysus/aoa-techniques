# Origin Evidence

## Technique
- id: AOA-T-0034
- name: public-safe-artifact-sanitization

## Source project
- name: aoa-skills
- source files:
  - `skills/aoa-sanitized-share/SKILL.md`
  - `skills/aoa-sanitized-share/examples/runtime.md`
  - `skills/aoa-sanitized-share/checks/review.md`
  - `docs/reviews/status-promotions/aoa-sanitized-share.md`

## Evidence
- the source skill already separates share-prep work from approval gating and execution preview
- the source skill already requires removal, redaction, or generalization of sensitive detail before sharing
- the source review checklist already asks reviewers to confirm sensitive surfaces, retained usefulness, and remaining uncertainty
- the promotion review already treats the practice as a bounded public-safe share-prep contract rather than an incident or permissioning workflow

## Interpretation
- the reusable pattern already exists as a live bounded skill and can be lifted into a public docs technique without widening into approval, execution, or incident handling
- the public bundle keeps the share-prep contract while removing source-specific operational detail and private topology
