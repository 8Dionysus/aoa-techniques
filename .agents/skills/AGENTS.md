# AGENTS.md

## Guidance for `.agents/skills/`

`.agents/skills/` is a generated or exported agent-facing companion surface for technique use.

It may help a coding agent find reusable practice quickly, but the source-authored technique canon remains in `techniques/*/*/TECHNIQUE.md` and related bundle files.

Do not turn a technique export into a new skill bundle. Skills belong in `aoa-skills`; this layer should describe practice primitives, validation patterns, docs layouts, and transfer methods.

Do not hand-edit exported files as the first move. Change the source technique, export configuration, or builder, then regenerate and review the diff.

Keep descriptions short, public-safe, and bounded. Avoid hidden project assumptions, private paths, or capability claims stronger than the source technique.

Verify with:

```bash
python scripts/validate_repo.py
python scripts/validate_semantic_agents.py
```
