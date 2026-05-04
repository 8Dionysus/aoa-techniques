# Root Legacy Archive

`legacy/archive/` preserves retired public-safe repo-wide surfaces whose active
route now lives elsewhere.

Current archive inventory: none preserved.

Use this directory when a root, docs-root, incoming, or other repo-wide tail
surface needs to stay auditable after it stops being the current route.

Prefer narrower homes first:

- `mechanics/<slug>/legacy/` for one mechanic's lineage
- `docs/decisions/` for rationale
- `generated/` or `reports/` for current reproducible outputs
- `incoming/` for unreviewed candidate quarantine

Do not archive active source files without updating links, route docs, and
`../INDEX.md`.
