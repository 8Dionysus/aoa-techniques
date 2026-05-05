# Adverse Effects Review

## Technique

- id: AOA-T-0023
- name: stateless-single-shot-agent

## Review focus

- current role: canonical default for quick shell-side agent work that should stay mostly stateless, one-prompt, and approval-gated before any mutating or command-executing step
- current watch seam: keep the bundle centered on one bounded fast-path invocation without widening into interactive session doctrine, broad approval policy, or hidden multi-step autonomy

## Failure modes

- teams keep calling the workflow stateless after hidden continuity, resume behavior, or multi-step planning has become necessary
- a convenient fast path encourages operators to skip escalation into `AOA-T-0001` even after the task clearly needs planning, verification, or diff review
- canonical pressure widens the technique into general CLI approval policy, tool governance, or interactive chat posture instead of preserving the one-prompt shell contract

## Negative effects

- a strong fast path can normalize under-scoped repository work where a richer workflow would have caught risk earlier
- session-wide or global auto-approval can make the one-shot path feel safe while silently removing the review seam that keeps it bounded
- keeping the contract low-ceremony can tempt teams to hide stateful conventions in wrappers, profiles, or resume mechanics while still using the same label

## Misuse patterns

- using `AOA-T-0023` for multi-step repository edits, iterative debugging loops, or broader planning sessions that belong under `AOA-T-0001`
- treating approval flags or tool allowlists as operational convenience defaults rather than as deliberate boundary changes
- collapsing `AOA-T-0023`, `AOA-T-0028`, and `AOA-T-0031` into one generic shell-agent pattern and losing the specific center of gravity of each bundle

## Detection signals

- one invocation starts chaining several tool actions or depends on hidden prior state before reporting back
- operators stop distinguishing between quick read-only questions, one confirmed action, and wider multi-step workflows
- new guidance starts focusing more on permission presets, interactive continuation, or wrapper features than on one bounded shell-side invocation
- pull requests keep using this bundle as justification for work that really needed plan/diff/verify discipline

## Mitigations

- re-narrow the contract to one prompt, one invocation, and one confirmed step before mutation, then escalate wider work to `AOA-T-0001`
- keep approval widening explicit and local instead of treating session-wide or global auto-approval as part of the default contract
- preserve the sibling boundaries with `AOA-T-0028` and `AOA-T-0031` so confirmation-gating and shell composability do not swallow this bundle
- revisit canonical status if the technique starts being used mainly for interactive session guidance, general approval policy, or hidden stateful automation rather than bounded fast-path work

## Recommendation

- keep current `canonical` status and use this note as the watch surface for hidden continuity, approval-breadth drift, and fast-path overuse after a task has outgrown single-shot execution
