# Adverse Effects Review

## Technique
- id: AOA-T-0045
- name: witness-trace-as-reviewable-artifact

## Review focus
- current role: canonical default for preserving one substantial agent or automation run as a structured reviewable trace artifact before downstream memory, compost, canon, or promotion decisions
- current watch seam: keep the bundle centered on trace export, ordered events, state-delta visibility, redaction, and summary posture rather than letting transcript packaging, hosted observability, memory writeback, or eval scoring become the real contract

## Failure modes
- trace capture becomes a noisy default for trivial runs where a short note or transcript reference would be enough
- reviewers treat the trace summary or timeline as proof of correctness instead of a guide to inspect the actual event stream
- state-delta payloads leak sensitive operational detail because redaction is weak or applied too late
- the trace artifact quietly becomes a new memory object or promotion verdict because downstream ownership is not explicit

## Negative effects
- structured traces add review and storage overhead compared with smaller summaries
- local trace artifacts can feel more authoritative than authored decisions, status surfaces, or memory objects
- rich event streams can expose tool arguments, state changes, or failure paths that need careful public-safety review
- a useful trace viewer can tempt teams to widen the technique into a tracing platform or hosted observability workflow

## Misuse patterns
- applying witness traces to every run instead of substantial, review-worthy runs
- using the witness trace as repository policy, canonical memory, or automated promotion evidence
- folding transcript export, search, indexing, monitoring dashboards, alerting, or scoring into the trace artifact contract
- preserving raw secret-bearing payloads or hidden reasoning because the trace is "for review"

## Detection signals
- the trace has no clear bounded run identity, goal, or review scope
- state-delta and tool-visibility fields are missing even though the run changed external state
- the human-readable summary tells reviewers what to believe rather than what to inspect next
- later memory, compost, canon, or eval surfaces cite the trace as a verdict instead of as source evidence

## Mitigations
- reserve this technique for substantial runs where reviewability matters
- keep transcript capture, transcript packaging, local indexing, memory writeback, promotion routes, and eval policy as sibling or downstream concerns
- apply redaction-first handling before sharing or publication
- keep the summary as a review guide and route correctness claims to proof/eval surfaces
- split richer trace schemas or hosted observability needs into separate tooling or techniques instead of widening this artifact contract

## Recommendation
- move `AOA-T-0045` to `canonical` and use this note as the watch surface for trace-as-memory drift, trace-as-verdict drift, over-capture noise, and expansion into transcript, indexing, observability, or scoring authority
