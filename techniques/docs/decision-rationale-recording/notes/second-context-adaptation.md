# Second Context Adaptation

## Technique
- id: AOA-T-0033
- name: decision-rationale-recording

## Target project
- name: aoa-techniques
- environment: public documentation repository for reusable engineering techniques
- runtime: human and agent contribution workflow over reviewable repository changes

## What changed
- the origin practice was rewritten as a reusable docs technique instead of a local skill instruction
- the note format was generalized from origin-project phrasing into public-safe decision language
- the support surfaces were reduced to one technique doc, one checklist, one example, and three evidence notes
- the result keeps the bounded rationale pattern while dropping private context and origin-specific detail

## What stayed invariant
- one meaningful decision is still the unit of record
- context, options, rationale, and consequences are still required
- the technique still rejects trivial edits and non-decision tasks
- the technique still avoids source-of-truth governance and architecture taxonomy

## Risks introduced by adaptation
- the note can drift into generic meeting minutes if the explicit decision statement is lost
- the technique can become too broad if every explanation is treated as a decision record
- public vocabulary can invite taxonomy-heavy writing if the boundary is not restated clearly

## Evidence
- The public docs framing keeps the practice in `docs` as a reviewable decision-recording pattern.
- Existing sibling docs techniques in `aoa-techniques` already show how reusable docs guidance can stay bounded without turning into generic architecture theory.
- The technique contract still centers practical reviewability rather than a larger governance model.

## Result
- verdict: works
- note: the adapted bundle stays readable as a docs technique for decision rationale recording
