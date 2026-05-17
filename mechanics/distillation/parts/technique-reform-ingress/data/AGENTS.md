# AGENTS.md

## Applies to

This card applies to
`mechanics/distillation/parts/technique-reform-ingress/data/` and every descendant unless a nearer
`AGENTS.md` narrows the path.

## Role

This directory holds source-supporting overlay data for the
`technique-reform-ingress` Distillation part.

The overlay data feeds scout reports and projection review. It is not current
frontmatter truth, not a generated report, and not a root-level data contract.
Treat generated reports as consumers of this data, not as authority over it.

When changing these files, rebuild the affected reports and verify exact corpus
coverage.

## Read before editing

Read:

1. repository root `AGENTS.md`
2. `mechanics/AGENTS.md`
3. `mechanics/distillation/AGENTS.md`
4. `mechanics/distillation/PARTS.md`
5. the touched part README, schema, example, script, report, or test

## Boundaries

- Do not let this local card override authored source surfaces, schemas,
  builders, validators, or sibling owner truth.
- Do not claim skill execution, proof verdict, runtime, routing, memory,
  playbook, or owner-acceptance authority from this package.

## Validation

Verify with:

```bash
python scripts/build_kind_manifest.py
python mechanics/distillation/parts/technique-reform-ingress/scripts/build_topology_scout.py
python mechanics/distillation/parts/technique-reform-ingress/scripts/build_tree_projection.py
python scripts/validate_repo.py
```

## Closeout

Report the mechanic package, part, legacy surface, or helper changed;
whether source, generated, schema, example, or test surfaces moved; checks run;
checks skipped; and the next owner route.
