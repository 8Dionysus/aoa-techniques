# AGENTS.md

## Guidance for `incoming/`

`incoming/` is a quarantine and staging area for candidate technique material.

Nothing here is canonical merely because it exists. A candidate must be reviewed, normalized, linked to source evidence, and promoted through the documented technique shape before it can speak as canon.

Preserve provenance, uncertainty, and review status. Do not erase rough edges by turning partial notes into polished doctrine too early.

Do not put secrets, private transcripts, or unreduced project dumps here. If material is not public-safe, keep it out of this repository.

Promotion should end in a source-authored technique bundle, not a generated or staging-only artifact.

Verify with:

```bash
python scripts/validate_repo.py
python scripts/validate_semantic_agents.py
```
