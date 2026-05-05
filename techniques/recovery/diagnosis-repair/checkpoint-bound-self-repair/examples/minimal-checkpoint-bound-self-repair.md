# minimal checkpoint-bound-self-repair

```yaml
checkpoint_bound_repair:
  repair_shape_ref: bounded-repair-shape-2026-04-05.md
  policy_check: constitution-fit-confirmed
  approval_gate: explicit-review-required
  rollback_marker: pre-repair-session-harvest-family
  health_check: release-check
  iteration_limit: 1
  improvement_log_stub: docs/improvement-log/session-harvest-family.md
```

Why this example stays bounded:

- it wraps an existing repair shape instead of inventing one
- it makes rollback and health-check posture explicit
- it prevents silent retries from masquerading as safe self-repair
