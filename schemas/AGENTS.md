# AGENTS.md

## Guidance for `schemas/`

`schemas/` holds machine-readable contracts for technique surfaces, reports, manifests, examples, or downstream exports.

Schema edits are contract edits. Preserve `$schema`, stable identifier posture, required fields, enums, and descriptions that keep techniques reproducible.

Do not loosen a schema only to pass a broken generated file. Fix the source, update paired examples, or document the contract change.

When a schema affects routing, KAG lift, or skill composition, re-check the downstream consumer surface and name the owner repo in the report.

Verify with:

```bash
python scripts/validate_repo.py
python scripts/validate_semantic_agents.py
```
