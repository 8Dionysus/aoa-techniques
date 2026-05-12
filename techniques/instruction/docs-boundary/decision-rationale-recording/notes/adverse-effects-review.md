# Adverse Effects Review

## Technique
- id: AOA-T-0033
- name: decision-rationale-recording

## Review focus
- current role: canonical default for preserving one meaningful decision as a compact, reviewable rationale note with visible context, alternatives, chosen path, rationale, and consequences
- current watch seam: keep the bundle centered on one decision record rather than widening into source-of-truth governance, architecture taxonomy, ADR tooling ownership, decision-log management, or generic changelog writing

## Failure modes
- decision notes become mandatory ceremony for trivial edits
- the record names the chosen path but hides the rejected option or accepted cost
- the note drifts into architecture classification, repository ownership, or source-of-truth placement instead of preserving rationale
- multiple unrelated decisions get packed into one polished but hard-to-review artifact

## Negative effects
- extra documentation can slow small changes when no meaningful decision exists
- a structured decision note can create false confidence if the real tradeoff was never exposed
- decision records can bury important signals if every routine edit receives the same durable treatment
- ADR vocabulary can pull the technique toward architecture-governance posture when the needed move is only a bounded rationale record

## Misuse patterns
- treating every explanation, changelog entry, or status update as a decision record
- using the note to decide where source truth should live instead of recording a decision already made
- turning the record into a multi-decision policy document, taxonomy map, or tool adoption mandate
- citing the note as proof that the decision was correct rather than evidence of why the decision was made

## Detection signals
- the note has no explicit decision sentence
- reviewers can see what was chosen but cannot see what was rejected
- consequences are generic, missing, or all positive
- the content starts assigning canonical owners, schema classes, or architecture categories rather than explaining a bounded choice
- the record is longer than the underlying decision warrants

## Mitigations
- reserve this technique for meaningful decisions with a real tradeoff
- require at least one rejected option and one accepted consequence
- split unrelated decisions into separate notes
- route source-of-truth layout, boundary mapping, architecture classification, and decision-log tooling to neighboring techniques or owner surfaces
- keep the note public-safe and small enough for a future reviewer to inspect without reopening the whole discussion

## Recommendation
- move `AOA-T-0033` to `canonical` and use this note as the watch surface for ceremony drift, hidden-tradeoff drift, governance drift, architecture-taxonomy drift, and generic changelog drift
