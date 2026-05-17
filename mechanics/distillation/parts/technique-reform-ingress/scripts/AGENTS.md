# AGENTS.md

## Applies to

This card applies to
`mechanics/distillation/parts/technique-reform-ingress/scripts/` and every descendant unless a nearer
`AGENTS.md` narrows the path.

## Role

This directory holds one-owner technique-reform report builders for the
Distillation part.

These scripts may rebuild scout or projection reports under the same
`technique-reform-ingress` part. They do not own repo-wide generated readers,
frontmatter truth, schema truth, or path migration authority.

Keep imports repo-relative and deterministic. If a script needs shared parsing
or validation helpers, import them from root `scripts/validate_repo.py` rather
than copying logic into the part.

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
python mechanics/distillation/parts/technique-reform-ingress/scripts/build_topology_scout.py
python mechanics/distillation/parts/technique-reform-ingress/scripts/build_tree_projection.py
python scripts/validate_repo.py
```

## Closeout

Report the mechanic package, part, legacy surface, or helper changed;
whether source, generated, schema, example, or test surfaces moved; checks run;
checks skipped; and the next owner route.
