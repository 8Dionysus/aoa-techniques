# Topology Scout Axis Registry

Date: 2026-05-04

## Status

Accepted.

## Context

`aoa-techniques` already treats `domain` and `kind` as current frontmatter
truth, while `family`, `capability_class`, `substrate`,
`execution_profile`, `risk_posture`, and richer relation topology remain
weaker design axes.

The family axis already has a source registry and scout report. The other four
axes had doctrine in the topology contract and mechanics gates, but no
repo-owned value registry. Without a registry, the next generated projection
would either invent values inside a builder or jump too quickly into schema and
frontmatter migration.

## Decision

Add `mechanics/distillation/parts/technique-reform-ingress/config/technique_topology_axes.yaml` as the scout value registry for
`capability_class`, `substrate`, `execution_profile`, and `risk_posture`.

The registry is a config-owned source for allowed scout values. It stays below bundle frontmatter, below schema, and below the authored topology contract.
It exists so generated and review surfaces can use one value vocabulary before
any later decision promotes an axis into optional or required bundle metadata.

## Alternatives

- Keep the values only in `docs/TECHNIQUE_TOPOLOGY_CONTRACT.md`.
  Rejected because the contract explains topology law, while builders and tests
  need a structured source.
- Add the fields directly to `schemas/technique.schema.json`.
  Rejected because the first reform pass should prove selection value before
  asking every bundle to carry new metadata.
- Put values only in the future generated report.
  Rejected because generated reports should derive from source, not become the
  first source of vocabulary.

## Consequences

- The next topology scout projection can be generated from a stable value
  source instead of hard-coded ad hoc labels.
- The registry gives reviewers a shared vocabulary for capability, substrate,
  execution profile, and risk posture while preserving `domain + kind` as
  current frontmatter truth.
- Validators can ensure the registry remains public-safe, bounded, and below
  automatic remap authority.
- Future schema or template promotion still needs a separate decision, tests,
  docs, and migration path.

## Verification

Expected checks:

```bash
python -m unittest tests.test_validate_repo
python scripts/validate_repo.py
python -m unittest discover -s tests
python scripts/release_check.py
```
