# Root Legacy Archive

`legacy/archive/` preserves retired public-safe repo-wide surfaces whose active
route now lives elsewhere.

Current archive inventory: none preserved.

Use this directory when a root, docs-root, incoming, or other repo-wide tail
surface needs to stay auditable after it stops being the current route.

Prefer narrower homes first:

- `mechanics/<slug>/legacy/` for one mechanic's lineage
- `docs/decisions/` for rationale
- `generated/` or mechanic-local `mechanics/**/reports/` for current
  reproducible outputs
- `incoming/` for unreviewed candidate quarantine

Agent edits, archive stop-lines, route-link updates, validation, and closeout
live in [archive/AGENTS](AGENTS.md).
