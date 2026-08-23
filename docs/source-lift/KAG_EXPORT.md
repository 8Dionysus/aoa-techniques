# KAG Export

This document records the current source-owned tiny KAG export posture for
`aoa-techniques`.

The export is a bounded capsule for one technique object.
It exists so downstream repositories can consume a source-owned entry surface
without replacing authored technique meaning.

## Current pilot

The current pilot stays intentionally narrow:

- one exported object: `AOA-T-0043`
- one entry surface: `generated/technique_capsules.json`
- one compact consumer surface: `generated/kag_export.min.json`
- one `artifact_identity` block that names the export ABI, producer,
  verification route, public boundary, and consumer expectation
- one source-owned boundary note that keeps markdown authoritative

## Core rule

The export is a guide to the source, not a replacement for the source.

It may expose a bounded question, summaries, section handles, and direct
relation refs for one technique, but authored technique meaning remains in the
corresponding `TECHNIQUE.md` bundle.

The `artifact_identity` block describes the generated export capsule itself. It
does not promote the capsule above the source-authored technique bundle, and it
does not replace KAG owner review.

## Current files

- `generated/kag_export.json`
- `generated/kag_export.min.json`
- `scripts/build_kag_export.py`
- `docs/source-lift/artifact-bundles/kag_export.bundle.json`

## OS Abyss artifact envelope

`docs/source-lift/artifact-bundles/kag_export.bundle.json` wraps the compact
export as `source_owned_kag_export_capsule` for OS Abyss consumers. It requires
ABI verification, SLSA/in-toto generation provenance, durable evidence
promotion, materialized subject-store verification, and fail-closed
trust-gate/latest selection before a consumer treats the capsule as a
release/export handoff.

The envelope is still subordinate to the authored technique bundle and does not
define KAG substrate behavior.

## Release source binding

The generated capsule is content-addressed, so the source commit is bound in
the OS Abyss artifact evidence at preparation time rather than embedded as a
self-referential field in the generated JSON. The release validator resolves
the checked-out `HEAD` and passes it as the exact
`commit:<40-hex-git-SHA>` `source_ref` to artifact sidecars, the durable
registry record, subject materialization, and the trust gate. A path such as
`docs/source-lift/artifact-bundles/kag_export.bundle.json` is a manifest
reference only and is not a currentness proof.

The intended local consumer boundary is `consumer_intent=agent` with
`trust_root_mode=host_managed`. The validator records that boundary's raw
verdict without rewriting it. `release_consumer` and `public_release` are
separate production boundaries: when they lack a public-release trust root,
their `manual_review_required` result remains manual review, not an allow
claim. Unknown, deny, warn, and allow remain distinct outcomes.

## Regeneration

Use [AGENTS](AGENTS.md#validation) for the current regeneration and validation
lane.
