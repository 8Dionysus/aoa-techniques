# minimal workspace-root-ingress-and-mutation-gate

```yaml
workspace_posture:
  workspace_root: /workspace
  repo_root: /workspace/aoa-sdk
  ingress:
    command: aoa skills enter /workspace/aoa-sdk --root /workspace --intent-text "inspect closeout seam"
    must_confirm: []
  guard:
    command: aoa skills guard /workspace/aoa-sdk --root /workspace --intent-text "update closeout routing" --mutation-surface code
    must_confirm:
      - approval_gate
      - dry_run_first
```

Why this example stays bounded:

- it names one workspace root and one repo root instead of a whole install route
- it makes ingress and guard visible without claiming they auto-resolve every decision
- it shows mutation gating without widening into closeout or bootstrap doctrine
