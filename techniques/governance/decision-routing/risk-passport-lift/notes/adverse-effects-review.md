# Adverse Effects Review

## Technique
- id: AOA-T-0079
- name: risk-passport-lift
- current role: bounded canonical default

## Review focus

Review the effects of making a small per-route passport the default posture
surface for difficulty, risk, control mode, delegate tier, and stop conditions.

## Failure modes

- passport fields become hidden routing scores
- stop conditions disappear and risk becomes decorative
- passports grow larger than the route they summarize
- control mode or delegate tier is treated as sovereign approval policy

## Negative effects

- fake precision can create false confidence
- repeated passports can over-formalize obvious low-risk routes
- downstream SDK or playbook consumers may inherit stale posture if the route
  changes but the passport does not

## Misuse patterns

- attaching a passport before any explicit route exists
- using passport fields as command dispatch policy
- flattening uncertainty into one synthetic risk score
- replacing repair checkpoints or approval gates with posture labels

## Detection signals

- reviewers cannot explain what changed when the passport changed
- difficulty, risk, control mode, or delegate tier labels are used as final
  authority
- meaningful risk has no stop condition
- passport metadata outweighs route meaning

## Mitigations

- keep the field set small
- require stop-condition cues when risk or cost is meaningful
- reject synthetic total scores
- keep passports adjacent to branch cards and subordinate to actual execution
  gates

## Recommendation

Keep the canonical bundle and use this note as one bounded watch surface. Future
changes should keep route-passport posture descriptive and reviewable without
widening it into risk scoring, approval governance, dispatch metadata, repair
execution, or SDK authority.
