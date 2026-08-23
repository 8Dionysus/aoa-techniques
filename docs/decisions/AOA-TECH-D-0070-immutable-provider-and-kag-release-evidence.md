# Bind Provider Pins And KAG Evidence To Immutable Release Source

Status: accepted
Date: 2026-08-23

## Index Metadata

- Decision ID: AOA-TECH-D-0070
- Original date: 2026-08-23
- Surface classes: release, artifact evidence, owner boundary
- Technique axes: provenance, validation, consumer boundary
- Mechanic parents: none
- Guard families: release identity, generated/read-model, artifact trust
- Posture: corrective release law

## Context

The `v0.6.0` release workflow and local KAG validator accepted ancestor-only
provider revisions even though the published `aoa-kag@v0.5.0` and
`aoa-stats@v0.2.0` tags had newer exact commits. Its KAG export evidence also
used the bundle-manifest path as `source_ref`, which identifies a file but does
not prove which released source produced the evidence. The artifact owner now
requires an exact Git commit for this KAG artifact class.

## Options considered

1. Keep ancestor-only pins and rely on the provider tag names.
2. Replace every consumer pin with the exact peeled commit of the published
   provider tag and bind artifact evidence to the exact Techniques commit at
   preparation time.
3. Treat a local artifact allow as a public-release trust decision.

## Decision

Choose option 2. Direct `aoa-kag` and `aoa-stats` consumers in this repository
must resolve the current published provider tags to their exact immutable
commits. The KAG artifact validator must resolve the checked-out Techniques
`HEAD`, pass `commit:<40-hex-git-SHA>` through artifact sidecars, durable
registry promotion, subject materialization, and trust-gate expectations, and
reject a caller-supplied ref that differs from that `HEAD`.

The declared local consumer boundary remains `consumer_intent=agent` with
`trust_root_mode=host_managed`. Production `release_consumer` and
`public_release` verdicts are observed separately and remain whatever the
artifact owner returns; missing public-release trust is manual review, not an
allow conversion.

## Rationale

Provider-before-consumer compatibility is a commit identity constraint, not
an ancestor relationship. A path-only artifact ref has the same weakness: it
cannot distinguish evidence produced before and after a source repair. The
runtime source ref belongs in owner-generated evidence and the registry record
because embedding a future release commit in the generated payload would make
the payload self-referential. Keeping local and production consumer intents
separate preserves the artifact owner's fail-closed trust semantics.

## Consequences

- Workflow and local KAG validation gates follow the exact published provider
  commits until a fresh provider release changes them.
- Artifact sidecars and registry records carry an immutable Techniques commit;
  manifest paths remain source-document references only.
- The local agent boundary can be `allow` while production release consumers
  remain `manual_review_required`, `deny`, `warn`, or `unknown` as returned by
  the owner gate.
- The corrective release must retain `v0.6.0` and must not rewrite prior tags,
  releases, or historical changelog claims.

## Source surfaces

- `.github/workflows/repo-validation.yml`
- `scripts/validate_repo_local_kag_index.py`
- `scripts/validate_abyss_machine_kag_export_bundle.py`
- `scripts/validators/common.py`
- `docs/source-lift/KAG_EXPORT.md`
- `docs/source-lift/artifact-bundles/kag_export.bundle.json`
- `CHANGELOG.md`

## Follow-up route

When a published provider tag advances, refresh the exact source pin through
the provider-before-consumer release route. When the artifact owner changes its
trust-root or consumer-intent policy, rerun the artifact loop and preserve the
raw verdicts rather than widening this repository's authority.

## Verification

- `source-fast` checks the direct provider checkout and source contract.
- `generated` checks the KAG export, decision indexes, and derived parity.
- `release` checks the complete release snapshot and KAG artifact validator.
- The artifact-owner registry and trust-gate route remains the authority for
  artifact admission; this decision does not claim runtime health, proof,
  deployment, or human acceptance.
