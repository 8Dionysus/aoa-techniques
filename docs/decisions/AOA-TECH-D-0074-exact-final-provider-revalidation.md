# Revalidate Techniques Against the Final Published KAG and Stats Providers

Status: accepted
Date: 2026-08-23

## Index Metadata

- Decision ID: AOA-TECH-D-0074
- Original date: 2026-08-23
- Surface classes: release, CI, provider validation, generated evidence
- Technique axes: provenance, validation, lifecycle
- Mechanic parents: none
- Guard families: release identity, provider currentness, workflow topology
- Posture: corrective release law

## Context

The published campaign settled the provider spine at `aoa-kag@v0.5.0` and
`aoa-stats@v0.2.0`, but the current Techniques source still required the
superseded KAG `8136d3eb…` and stats `f119805c…` commits. A green validation
against either stale or merely ancestral source does not establish exact
provider-before-consumer compatibility.

## Options considered

1. Keep the current pins and rely on the historical `v0.6.0` release evidence.
2. Move current-main consumer lanes and local adapters to the exact peeled
   commits of the final published provider tags, regenerate owner companions,
   and preserve the immutable release history.
3. Rewrite or retag `v0.6.0` after changing the provider declarations.

## Decision

Choose option 2. Current-main Techniques consumers must resolve:

- `aoa-kag@v0.5.0` tag object
  `8f63e3ae558ea96d21ee06becfa6ef61d63d698a`, peeled commit
  `f46f146cc79a26fa81ad0f400b9c5774df293e57`;
- `aoa-stats@v0.2.0` tag object
  `a63dd6f95c6f0c87a371720885c2d90a1baa3436`, peeled commit
  `88ff38b1b38eef939f2c5b4541cbe8363a05fc8d`.

The exact peeled commits are the checkout constraints in the local adapters
and the current `Repo Validation` and `Nightly Sentinel` moving-main lanes.
The tag-scoped Release Audit and latest-release reproducer continue to derive
their stats checkout from the selected immutable Techniques source so that
historical release evidence remains historical.

Generated KAG-family and document/decision projections remain builder-owned.
The artifact owner retains independent `allow`, `warn`, `deny`,
`manual_review_required`, and `unknown` outcomes for each consumer intent;
this source repair does not rewrite or promote any artifact verdict.

## Rationale

Provider-before-consumer compatibility is an exact commit identity constraint,
not an ancestor relationship. The tag object and peeled commit are recorded
separately so a workflow action identity, tag ref, or generated family cannot
stand in for the provider source commit. Keeping current-main pins separate
from tag-scoped historical reproduction preserves both reproducibility and
immutable release history.

## Consequences

- Current source-fast and moving-main checks fail closed on stale or moving
  KAG/stat checkouts.
- The generated KAG family changes only through the exact `aoa-kag` owner
  builder after the authored source repair; generated output remains weaker
  than authored source.
- The `[Unreleased]` changelog records the correction without creating a new
  release, and `v0.6.0` remains unchanged.
- Artifact admission, deployment, runtime health, proof, delivery, closure,
  master acceptance, and human acceptance remain separate claims.

## Source surfaces

- `.github/workflows/repo-validation.yml`
- `.github/workflows/nightly-sentinel.yml`
- `.github/workflows/release-audit.yml`
- `scripts/validate_repo_local_kag_index.py`
- `scripts/validate_local_stats_port.py`
- `CHANGELOG.md`
- `kag/indexes/index_family.manifest.json`

## Follow-up route

When either published provider tag advances, repeat this exact
provider-before-consumer route and re-resolve its tag object and peeled commit.
Rerun the artifact-owner trust loop for the landed Techniques source and keep
each raw consumer-intent verdict unchanged in meaning. Do not retag or rewrite
an existing Techniques release.

## Verification

- `source-fast` checks exact provider identity and authored contracts.
- `generated` checks decision indexes and derived parity.
- `mechanics/part-local` checks mechanic-owned source movement.
- `release` checks the frozen source snapshot and KAG artifact contract.
- The nearest `.github/`, `scripts/`, `generated/`, `kag/`, and
  `docs/decisions/` owner cards remain in force.
