# Adverse Effects Review

## Technique
- id: AOA-T-0028
- name: confirmation-gated-mutating-action

## Review focus
- current role: canonical default for one explicit confirmation seam before a bounded mutating action
- current watch seam: keep the bundle centered on a fresh named mutation gate rather than generic caution prose, session-wide approval defaults, or broader workflow governance

## Failure modes
- teams treat any warning or trust prompt as if it were already a real confirmation gate
- one vague approval gets reused to cover several writes or commands that should have been split
- canonical pressure widens the bundle into full approval-policy doctrine or broader multi-step workflow control

## Negative effects
- a strong confirmation default can add friction to small safe actions that would otherwise stay simple
- teams may overuse the bundle instead of escalating honestly to `AOA-T-0001` once the task becomes multi-step
- session-wide approval conveniences can make the pattern feel safe while silently eroding the review seam that keeps it bounded

## Misuse patterns
- using `AOA-T-0028` as shorthand for generic CLI permissions or trust policy rather than the bounded mutation gate itself
- bundling several writes behind one approval that does not name the actual mutation clearly enough to review
- collapsing `AOA-T-0028`, `AOA-T-0023`, and longer approval-bearing workflows into one generic shell-agent pattern

## Detection signals
- approval arrives after the mutation is already underway
- the confirmation text does not match the concrete command or write that actually runs
- the same approval is treated as reusable for unrelated mutations
- new guidance focuses more on session-wide allowlists or product permissions than on one explicit bounded action

## Mitigations
- keep the proposed mutation specific, visible, and narrow before asking for approval
- require a fresh confirmation whenever the action changes scope
- route broader work into `AOA-T-0001` or a more explicit governed workflow instead of stretching this bundle
- revisit canonical status if the technique starts being used mainly for generic approval policy rather than explicit confirmation-before-mutation

## Recommendation
- keep current `canonical` status and use this note as the watch surface for weak-gate drift, approval-breadth creep, and misuse of one confirmation across broader multi-step work
