# AGENTS.md

## Applies to

This card applies to
`mechanics/distillation/parts/technique-reform-ingress/config/` and every descendant unless a nearer
`AGENTS.md` narrows the path.

## Role

This directory holds scout-only input registries for the
`technique-reform-ingress` Distillation part.

These files support generated review reports. They do not define frontmatter
truth, schema truth, automatic remap authority, or technique meaning. Root
`config/` keeps repo-wide contract inputs such as the current kind registry.

When changing these files, rebuild the affected reports and verify that the
generated output remains weaker than authored technique bundles.

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
