# AGENTS.md

## Guidance for Technique-Reform Ingress Data

This directory holds source-supporting overlay data for the
`technique-reform-ingress` Distillation part.

The overlay data feeds scout reports and projection review. It is not current
frontmatter truth, not a generated report, and not a root-level data contract.
Treat generated reports as consumers of this data, not as authority over it.

When changing these files, rebuild the affected reports and verify exact corpus
coverage.

Verify with:

```bash
python scripts/build_kind_manifest.py
python mechanics/distillation/parts/technique-reform-ingress/scripts/build_topology_scout.py
python mechanics/distillation/parts/technique-reform-ingress/scripts/build_tree_projection.py
python scripts/validate_repo.py
```
