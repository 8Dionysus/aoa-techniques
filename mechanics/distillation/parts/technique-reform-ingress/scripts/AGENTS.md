# AGENTS.md

## Guidance for `technique-reform-ingress/scripts/`

This directory holds one-owner technique-reform report builders for the
Distillation part.

These scripts may rebuild scout or projection reports under the same
`technique-reform-ingress` part. They do not own repo-wide generated readers,
frontmatter truth, schema truth, or path migration authority.

Keep imports repo-relative and deterministic. If a script needs shared parsing
or validation helpers, import them from root `scripts/validate_repo.py` rather
than copying logic into the part.

Verify with:

```bash
python mechanics/distillation/parts/technique-reform-ingress/scripts/build_topology_scout.py
python mechanics/distillation/parts/technique-reform-ingress/scripts/build_tree_projection.py
python scripts/validate_repo.py
```
