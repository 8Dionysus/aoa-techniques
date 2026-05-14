# AGENTS.md

## Guidance for Technique-Reform Ingress Config

This directory holds scout-only input registries for the
`technique-reform-ingress` Distillation part.

These files support generated review reports. They do not define frontmatter
truth, schema truth, automatic remap authority, or technique meaning. Root
`config/` keeps repo-wide contract inputs such as the current kind registry.

When changing these files, rebuild the affected reports and verify that the
generated output remains weaker than authored technique bundles.

Verify with:

```bash
python scripts/build_kind_manifest.py
python mechanics/distillation/parts/technique-reform-ingress/scripts/build_topology_scout.py
python mechanics/distillation/parts/technique-reform-ingress/scripts/build_tree_projection.py
python scripts/validate_repo.py
```
