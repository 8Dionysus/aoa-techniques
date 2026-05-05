# Minimal Capability Spec Versioning

Use one small spec as the contract for one named capability.

```yaml
capability:
  name: summarize_history
  version: 1.1.0
  purpose: Produce a short project-history summary from versioned session artifacts.
  inputs:
    - history_path
    - max_entries
  outputs:
    - summary_markdown
  invariants:
    - input artifacts remain read-only
    - summary does not rewrite source history
  compatibility:
    changed_from: 1.0.0
    note: version 1.1.0 adds max_entries but keeps existing summary shape
```

Provider code can change later, but the spec remains the first review surface for what the capability means now.
