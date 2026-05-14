# Adverse Effects Review

## Technique
- id: AOA-T-0048
- name: semantic-review-surface-lift
- current role: canonical default for lifting authored review markdown into a subordinate derived review-reader surface

## Review focus
- current watch seam: keep review meaning in authored markdown while the derived surface exposes lookup posture, scope, evidence refs, signal summary, and next trigger without becoming a scoring or status engine

## Failure modes
- the generated review reader starts replacing the authored review doc as the place where meaning is argued
- review-status fields become generic quality scores, promotion gates, or automated verdicts
- maintainers widen the reader until it mixes semantic review, policy enforcement, relation cleanup, graph behavior, and local bundle readiness in one surface
- sibling-layer verdicts or gate tokens are imported as technique authority instead of remaining evidence posture in their owning repository

## Negative effects
- a compact generated reader can hide how much judgment still lives in the source review notes
- downstream readers may stop opening the authored review documents when the generated surface looks complete enough
- review lookup can create false closure when the underlying cluster or boundary is still contested
- sibling evidence can blur owner boundaries if playbook, eval, routing, or promotion semantics leak into the technique

## Misuse patterns
- using the reader to decide status transitions or promotion outcomes
- treating AI review summaries, code-review dashboards, quality scores, or issue triage reports as equivalent to authored review-note lift
- editing generated JSON to fix review meaning instead of editing authored markdown and rebuilding
- folding every nearby review or relation question into one semantic-review reader because it is convenient

## Detection signals
- reviewers ask the generated surface for scores, approvals, or final decisions
- the reader no longer links back to the authored review doc or reviewed evidence notes
- generated fields expand toward policy checks, dashboards, graph ranking, or release gates
- source review notes go stale while generated outputs continue to look current

## Mitigations
- keep the reviewed corpus explicit and bounded before generating a reader
- regenerate review-status surfaces from authored markdown and fail validation when required sections or evidence refs drift
- route meaning changes, contested boundaries, and cluster splits back to authored review notes
- split a new technique or sibling owner route when the real need becomes scoring, composition governance, graph semantics, or policy automation

## Recommendation
- keep current `canonical` status and use this note as the watch surface for review-reader authority drift, status-automation overreach, source-doc bypass, and sibling-owner import
