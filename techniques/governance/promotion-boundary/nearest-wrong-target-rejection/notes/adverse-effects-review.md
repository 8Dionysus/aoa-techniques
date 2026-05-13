# Adverse Effects Review

## Technique
- id: AOA-T-0090
- name: nearest-wrong-target-rejection
- current role: bounded canonical default

## Review focus

Review the effects of making one adjacent wrong target explicit beside one
chosen owner or promotion verdict.

## Failure modes

- the rejected target is dramatic rather than nearest and plausible
- rejection language is used to defend a weak chosen verdict
- the reason is rhetorical and does not clarify a boundary
- the rejection widens into broad anti-pattern doctrine

## Negative effects

- forced rejection can create false certainty when `defer` is more honest
- reviewers may over-focus on the wrong target instead of the chosen boundary
- terse rejection can look like policy if the surrounding verdict is missing

## Misuse patterns

- naming a strawman no one would actually choose
- using rejection to avoid revisiting a weak owner choice
- rejecting whole neighboring organs instead of one bounded target for one
  bounded unit
- treating nearest-wrong rejection as the promotion verdict itself

## Detection signals

- the rejected target is not adjacent to the chosen one
- the reason cannot name a concrete boundary difference
- the same confusion remains after the rejection is written
- the note reads like an anti-pattern essay rather than a small verdict aid

## Mitigations

- require adjacency and plausibility
- keep one short boundary-shaped reason
- fall back to `hold`, `quest`, or `defer` when no honest chosen target exists
- pair the rejection with the surrounding verdict rather than isolating it as
  standalone doctrine

## Recommendation

Keep the canonical bundle and use this note as one bounded watch surface. Future
changes should keep nearest-wrong rejection small, paired, and boundary-focused
without replacing owner triage, quest promotion review, proof verdicts, memory
writeback, or playbook design.
