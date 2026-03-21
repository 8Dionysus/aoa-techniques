# Minimal Session Capture As Repo Artifact

Use one project-scoped history directory for saved AI coding sessions.

```text
.specstory/
  history/
    2026-03-21-architecture-review.md
    2026-03-21-bugfix-session.md
```

Contract:
- each session is saved locally as a project artifact
- the history remains usable without cloud sync
- later tools may summarize or organize the files, but the artifact layer stays primary
- the captured sessions do not become the canonical instruction source for the repository
