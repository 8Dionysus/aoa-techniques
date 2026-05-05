# Adverse Effects Review

## Technique
- id: AOA-T-0031
- name: shell-composable-agent-invocation

## Review focus
- current role: canonical default for shell-visible one-shot agent invocation through stdin, stdout, files, and pipes
- current watch seam: keep explicit shell I/O as the center of gravity instead of letting interactive session behavior, approval policy, or broader automation doctrine swallow the bundle

## Failure modes
- the invocation depends on hidden prior session state even while the docs still describe it as shell-composable
- output stops being usable in pipes or file handoffs because wrappers or product-shaped behavior become the real execution surface
- canonical pressure widens the technique into generic CLI ergonomics, interactive continuation, or workflow automation rather than preserving the one-shot shell contract

## Negative effects
- a strong shell-composable default can tempt teams to force every task into a pipe-friendly form even when a broader workflow would be clearer
- file or JSONL output can create a false sense of safety if operators assume shell composability already covers mutation review and workflow discipline
- one polished CLI surface can make the technique feel more vendor-shaped than it really is if the invariant I/O boundary is not kept explicit

## Misuse patterns
- using `AOA-T-0031` as a grab bag for generic shell best practices or CLI product features
- collapsing `AOA-T-0031`, `AOA-T-0023`, and `AOA-T-0028` into one generic shell-agent doctrine
- treating resume, session history, or approval presets as if they were part of the core shell-composability contract

## Detection signals
- reviewers can no longer explain how stdin, stdout, files, or pipes delimit the invocation
- the command only works through hidden state, interactive side channels, or product-specific UI features
- docs and PRs focus more on session continuation, approval presets, or wrappers than on one visible I/O boundary
- downstream consumers cannot trivially pipe, capture, or hand off the result without bespoke glue

## Mitigations
- keep the invocation one-shot and centered on explicit shell I/O boundaries
- route mutation review into `AOA-T-0028` and broader multi-step work into `AOA-T-0001`
- narrow wrappers until the underlying command boundary is easy to inspect and explain
- revisit canonical status if the technique starts being used mainly for interactive session behavior rather than shell composition

## Recommendation
- keep current `canonical` status and use this note as the watch surface for hidden-session creep, wrapper overgrowth, and loss of explicit shell I/O boundaries
