# Origin Evidence

## Technique
- id: AOA-T-0033
- name: decision-rationale-recording

## Source project
- name: aoa-skills
- source files:
  - `skills/aoa-adr-write/SKILL.md`
  - `skills/aoa-adr-write/examples/meaningful-decision.md`
  - `docs/reviews/status-promotions/aoa-adr-write.md`

## Evidence
- the source skill already defines the practice as recording one meaningful decision rather than documenting every small edit
- the source skill already keeps the boundary narrow by excluding trivial obvious edits, source-of-truth clarification, and document-role classification work
- the source skill already requires context, alternatives, rationale, and consequences to remain visible in one reviewable note
- the source example and promotion review show that the reusable object is the bounded decision record itself, not a broader governance or taxonomy layer

## Interpretation
- the reusable pattern already exists as a live bounded skill and can be lifted into a public docs technique without changing its core contract
- the public bundle keeps the decision-rationale pattern while stripping origin-project identifiers and private discussion detail
