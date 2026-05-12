# Second Context Adaptation

## Technique
- id: AOA-T-0033
- name: decision-rationale-recording

## Target project
- name: aoa-techniques
- environment: public documentation repository for reusable engineering techniques
- runtime: human and agent contribution workflow over reviewable repository changes
- external reinforcement:
  - name: Markdown Architectural Decision Records
  - repository: `adr/madr`
  - observed revision: `8135ed2e01503be852769402ec3eeb585bfe75a2`
  - public surfaces: `README.md`, `template/adr-template.md`, `docs/decisions/0003-provide-own-madr-tools.md`

## What changed
- the origin practice was rewritten as a reusable docs technique instead of a local skill instruction
- the note format was generalized from origin-project phrasing into public-safe decision language
- the support surfaces were reduced to one technique doc, one checklist, one example, and three evidence notes
- the result keeps the bounded rationale pattern while dropping private context and origin-specific detail
- the external MADR reinforcement proves the same one-decision record shape in a mature public docs practice: a decision record names context and problem, considered options, chosen outcome with justification, and accepted consequences

## What stayed invariant
- one meaningful decision is still the unit of record
- context, options, rationale, and consequences are still required
- the technique still rejects trivial edits and non-decision tasks
- the technique still avoids source-of-truth governance and architecture taxonomy
- the public reinforcement remains a decision-record format rather than a governance system, architecture taxonomy, or proof verdict

## Risks introduced by adaptation
- the note can drift into generic meeting minutes if the explicit decision statement is lost
- the technique can become too broad if every explanation is treated as a decision record
- public vocabulary can invite taxonomy-heavy writing if the boundary is not restated clearly
- ADR vocabulary can over-specialize the technique toward architecture decisions unless the invariant remains "one meaningful decision with visible rationale"

## Evidence
- The public docs framing keeps the practice in `docs` as a reviewable decision-recording pattern.
- Existing sibling docs techniques in `aoa-techniques` already show how reusable docs guidance can stay bounded without turning into generic architecture theory.
- The technique contract still centers practical reviewability rather than a larger governance model.
- MADR's `template/adr-template.md` carries the same review shape through `Context and Problem Statement`, `Considered Options`, `Decision Outcome`, and optional `Consequences`.
- MADR's own `docs/decisions/0003-provide-own-madr-tools.md` uses that shape in practice by naming a tooling decision, listing real alternatives, choosing the own-tooling option with justification, and accepting maintenance cost.
- `adr-tools` and the architecture-decision-record catalog were inspected as adjacent reinforcement: they support the ADR practice family, but MADR is the exact-fit public consumer for this bundle because it preserves the visible options and justification seam.

## Result
- verdict: works across origin and external decision-record contexts
- note: the adapted bundle now has exact-fit external reinforcement for one bounded decision rationale record without widening into source-of-truth governance, architecture taxonomy, or decision-log tooling ownership
