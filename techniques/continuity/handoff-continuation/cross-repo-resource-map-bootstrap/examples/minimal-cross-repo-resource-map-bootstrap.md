# minimal cross-repo resource-map bootstrap

```markdown
# Cross-Repo Resource Map

- repo: `frontend`
  role: consumes the changed API route
  first_lookup: `src/app/routes.ts`

- repo: `backend`
  role: owns the request contract
  resources:
    - `api/openapi.yaml`
    - `src/routes/widgets.ts`

- repo: `docs`
  role: holds the operator rollout note that the change must match
  resources:
    - `docs/DEPLOYMENT_FLOW.md`
```

Why this example stays bounded:

- it names only the repos and surfaces needed for the current cross-repo step
- it shows where to look first without becoming a full architecture map
- it does not import global workspace inventory, infrastructure catalogs, or a whole boot-sequence protocol
