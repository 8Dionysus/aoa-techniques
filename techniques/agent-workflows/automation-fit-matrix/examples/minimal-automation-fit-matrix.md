# minimal automation-fit-matrix

```yaml
automation_fit:
  route: reviewed remediation closeout report
  frequency: recurring
  friction: checklist-fatigue
  determinism: mostly-stable
  input_clarity: explicit
  output_clarity: explicit
  proof_surface: reviewable
  dry_run: available
  reversibility: easy
  secret_coupling: low
  approval_sensitivity: low
  verdict: seed_ready
```

Why this example stays bounded:

- it classifies one reviewed route instead of authoring the later automation artifact
- it keeps approval sensitivity visible without turning into a checkpoint system
- it keeps the verdict descriptive rather than sovereign
