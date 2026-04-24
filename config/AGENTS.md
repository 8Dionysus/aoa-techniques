# AGENTS.md

## Guidance for `config/`

`config/` holds policy, export, and build inputs for the technique canon.

Use config to tune publication and generation behavior, not to author technique meaning. Technique meaning belongs in `TECHNIQUE.md`, checks, examples, notes, and source-owned docs.

Keep config explicit and reviewable. Avoid hidden environment assumptions, private paths, and policy that only one local machine understands.

When config changes generated surfaces, rebuild the affected catalogs and inspect the diff for meaning drift.

Verify with:

```bash
python scripts/validate_repo.py
python scripts/validate_semantic_agents.py
```
