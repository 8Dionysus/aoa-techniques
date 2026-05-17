# AGENTS.md

## Applies to

This card applies to
`mechanics/distillation/parts/technique-reform-ingress/reports/` and every descendant unless a nearer
`AGENTS.md` narrows the path.

## Role

This directory contains generated scout readouts for the Technique Reform
Ingress part: kind counts, family scout output, kind ambiguity audit, topology
scout output, and tree projection output.

Reports are diagnostic surfaces. They may point to evidence and gaps, but they
do not own technique meaning and must not outrank source-authored bundles,
frontmatter, or active Distillation review packets.

Keep report language bounded: say what was measured, what was not measured, and
what command or source produced the readout.

Do not convert a report into a proof claim that belongs in `aoa-evals` or a workflow claim that belongs in `aoa-skills`.

Verify with the report generator when present, then:

```bash
python scripts/validate_repo.py
python scripts/validate_semantic_agents.py
```

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

Run `python scripts/validate_repo.py` and the nearest package or part test.

## Closeout

Report the mechanic package, part, legacy surface, or helper changed;
whether source, generated, schema, example, or test surfaces moved; checks run;
checks skipped; and the next owner route.
