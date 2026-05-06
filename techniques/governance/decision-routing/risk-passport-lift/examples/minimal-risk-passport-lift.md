# minimal risk-passport-lift

```yaml
route_passport:
  route: extract the diagnosis seam next
  difficulty: medium
  risk: bounded-but-real
  control_mode: explicit-review
  delegate_tier: focused
  stop_condition: "stop if diagnosis starts performing repair work"
```

Why this example stays bounded:

- it summarizes one route instead of replacing the branch card
- it keeps posture descriptive rather than sovereign
- it makes stop-condition posture visible without inflating into a full runbook
