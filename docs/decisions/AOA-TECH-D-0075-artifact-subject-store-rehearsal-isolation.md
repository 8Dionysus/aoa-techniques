# Isolate Techniques Artifact Subject-Store Rehearsals

Status: accepted
Date: 2026-08-24

## Index Metadata

- Decision ID: AOA-TECH-D-0075
- Original date: 2026-08-24
- Surface classes: artifact validation, release, CI, source contract
- Technique axes: isolation, provenance, validation
- Mechanic parents: none
- Guard families: artifact trust, negative precondition, release identity
- Posture: corrective owner law

## Context

The Techniques KAG artifact validator promoted a rehearsal record through the
abyss-machine artifact owner while the owner resolver still considered its
canonical host subject store. A preserved matching host store could therefore
make an explicit empty rehearsal appear subject-store verified before the
validator materialized its supplied store. The resulting source run could show
an apparently successful final rehearsal while failing to prove the required
deny-before-materialization precondition.

## Options considered

1. Set only the subject-store environment variables and rely on the
   abyss-machine resolver to prefer them.
2. Bind the imported owner module default and both subject-store environment
   variables to the explicit rehearsal root, and run every negative
   precondition through a fresh registry and empty temporary store.
3. Change the shared abyss-machine resolver or mutate the canonical host store
   from the Techniques repository.

## Decision

Choose option 2. The Techniques validator owns the rehearsal boundary: its
explicit subject-store root is authoritative for the process, while the
abyss-machine artifact policy and trust-gate semantics remain unchanged. Each
invocation proves the negative precondition in a fresh registry before
materialization, including `--no-clean` reruns. Empty and repository-root CLI
values are rejected before any artifact output is created.

The artifact owner's verdicts remain independent claims. The local materialized
agent rehearsal may be `allow`, while `release_consumer` or `public_release`
may remain `manual_review_required`, `deny`, `warn`, or `unknown` according to
their exact owner gates.

## Rationale

Environment-only binding is insufficient because the owner resolver appends a
host default after reading environment roots. A process-local module-plus-
environment binding is the smallest repair in the true Techniques validator
owner and avoids changing shared host policy or touching preserved host state.
A fresh negative registry prevents retained records from satisfying the
precondition on a `--no-clean` rerun.

## Consequences

- Ambient canonical subject-store state cannot satisfy the Techniques negative
  rehearsal by accident.
- Materialized final admission remains testable in the caller-selected local
  store, with release and public consumer boundaries reported separately.
- The repair changes current-main `[Unreleased]` behavior only; it creates no
  tag or GitHub Release and does not rewrite `v0.6.0`.
- The shared abyss-machine artifact owner remains the authority for registry,
  trust-root, lifecycle, and consumer verdict semantics.

## Source surfaces

- `scripts/validate_abyss_machine_kag_export_bundle.py`
- `tests/test_downstream_feed_contracts.py`
- `docs/source-lift/KAG_EXPORT.md`
- `docs/source-lift/artifact-bundles/kag_export.bundle.json`
- `CHANGELOG.md`

## Follow-up route

If the abyss-machine artifact subject-store resolver gains an explicit scoped
API, re-evaluate this local binding against that owner contract. Until then,
keep the Techniques process-local isolation and rerun the exact artifact-owner
consumer gates for each landed source commit.

## Verification

- `source-fast`, `generated`, and `mechanics/part-local` cover the validator,
  generated contract, and mechanic release-support surfaces.
- `release` covers the full source snapshot and artifact manifest contract.
- The exact artifact-owner negative, final, and adversarial checks preserve
  separate `allow`, `warn`, `deny`, `manual_review_required`, and `unknown`
  results.
- The nearest root, `scripts/`, `tests/`, `docs/decisions/`, and artifact
  owner AGENTS cards remain in force.
