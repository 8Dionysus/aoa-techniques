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
Read `README.md` only when the selected task needs its human map; do not preload unrelated maps.

## Boundaries

- Do not let this local card override authored source surfaces, schemas,
  builders, validators, or sibling owner truth.
- Do not claim skill execution, proof verdict, runtime, routing, memory,
  playbook, or owner-acceptance authority from this package.

## Validation

Select the narrowest owner route: `mechanics/part-local` for part-local work; add `source-fast` for authored routes or `generated` for projections. See [VALIDATION.md](../../../../../VALIDATION.md); exact order is `config/validation_lanes.json`; focused procedure stays with the nearest owner. Report checks, skips, and blockers.

## Closeout

Report the mechanic package, part, legacy surface, or helper changed;
whether source, generated, schema, example, or test surfaces moved; checks run;
checks skipped; and the next owner route.
