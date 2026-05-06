# minimal approval-sensitivity-check

```yaml
approval_sensitivity:
  route: repo-wide remediation auto-apply sweep
  mutation_surface: important
  authority_posture: operator-approved-only
  rollback_marker: required
  health_check: required
  checkpoint_required: true
  next_artifact: reviewed skill proposal with checkpoint posture
```

Why this example stays bounded:

- it classifies one candidate instead of approving execution
- it makes rollback and health-check posture visible
- it keeps the next step smaller than a full automation implementation
