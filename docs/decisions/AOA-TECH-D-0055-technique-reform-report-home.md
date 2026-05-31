# Technique Reform Report Home

Status: accepted
Date: 2026-05-14

## Index Metadata

- Decision ID: AOA-TECH-D-0055
- Original date: 2026-05-14
- Surface classes: mechanic part
- Technique axes: source-lift
- Mechanic parents: none
- Guard families: part-local artifact
- Posture: accepted

## Context

The repository root had a flat `reports/` directory containing generated
technique kind, family, topology, and tree scout readouts.

Those files were useful diagnostic evidence, but they were not a root public
entry surface, root doctrine, or repo-wide reporting authority. Their content
was generated from and for the Distillation
`technique-reform-ingress` part.

`mechanics/distillation/parts/technique-reform-ingress/` already owns the
classification-reform ingress packet, its review lane, and the bounded
scout/projection movement evidence.

## Options

- Keep generated scout reports in root `reports/`.
- Move them to `generated/` as generic build outputs.
- Move them under the owning Distillation part as mechanic-local reports, while
  keeping reader links from root and `docs/`.

## Decision

Move the former root `reports/` package to:

```text
mechanics/distillation/parts/technique-reform-ingress/reports/
```

Update the report builders, validators, tests, and reader links so generated
kind, family, topology, and tree scout readouts are written and checked in that
mechanic-local report home.

Keep those reports as evidence only. Technique bundles and their frontmatter
remain the authority for technique meaning.

## Consequences

- The repository root no longer presents this mechanic-specific report package
  as a root district.
- Technique reform scout evidence now lives beside the mechanic that owns its
  interpretation.
- Generated reports remain derived diagnostic surfaces, not source truth.
- Future repo-wide or public report surfaces must justify their own owner route
  instead of reusing this old root `reports/` precedent.

## Verification

Expected checks:

```bash
python scripts/build_kind_manifest.py
python mechanics/distillation/parts/technique-reform-ingress/scripts/build_topology_scout.py
python mechanics/distillation/parts/technique-reform-ingress/scripts/build_tree_projection.py
python scripts/validate_semantic_agents.py
python -m unittest tests.test_validate_repo
python -m unittest tests.test_distillation_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
python scripts/release_check.py
git diff --check
```
