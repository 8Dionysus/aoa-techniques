# minimal repair-shape-from-diagnosis

```yaml
repair_shape:
  diagnosis_ref: reviewed-diagnosis-2026-04-05.md
  primary_owner_target: aoa-skills
  target_artifact: SKILL.md delta
  validation_plan:
    - rerun release check
    - verify the route no longer collapses diagnosis into repair
  escalation_cue: "escalate to a playbook note if the fix needs several coordinated repo changes"
```

Why this example stays bounded:

- it starts from diagnosis instead of aspiration
- it chooses one owner-facing artifact
- it keeps escalation explicit if the repair would widen
