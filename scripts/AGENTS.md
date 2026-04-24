# AGENTS.md

## Guidance for `scripts/`

`scripts/` contains deterministic builders, validators, promotion helpers, and report tools for the technique canon.

Keep scripts repo-relative and reproducible. Avoid hidden network calls, private paths, and ambient credentials unless the command explicitly documents them.

When editing builders, preserve the distinction between authored technique bundles and generated summaries. Generated files summarize; they do not become the canon.

When editing validators, prefer precise failures that name the file, field, and owner surface. Do not weaken validation to make a bad corpus pass.

Verify with:

```bash
python scripts/validate_repo.py
python scripts/validate_semantic_agents.py
```
