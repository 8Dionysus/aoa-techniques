# Pin Release Audit To The Current Artifact Owner And Immutable Target

Status: accepted
Date: 2026-08-23

## Index Metadata

- Decision ID: AOA-TECH-D-0071
- Original date: 2026-08-23
- Surface classes: release, CI, artifact evidence
- Technique axes: provenance, validation, lifecycle
- Mechanic parents: none
- Guard families: release identity, artifact trust, workflow topology
- Posture: postpublish audit repair

## Context

The immutable `v0.6.1` source release changed the KAG artifact validator to
pass an explicit subject root, but the tag-triggered Release Audit workflow
still checked out an older `abyss-machine` commit whose `build_sidecars()` API
did not accept that argument. The source and local owner route were correct;
the tag audit failed at the workflow/provider compatibility boundary.

## Decision

Pin release-audit and nightly artifact-tool checkouts to the exact current
published `abyss-machine` main commit
`a9f52d8bfe23e28167c01dd2a059af231fff77a0` and allow `workflow_dispatch` to
accept an explicit immutable `release_ref`. A rerun may therefore check the
exact `v0.6.1` source without moving its tag or Release. The source tag and
Release remain immutable; this is a postpublish audit-tool repair on main,
not a retagging route.

## Rationale

The artifact owner API is part of the release validator's provider contract.
An old provider checkout can fail before artifact admission and must not be
silently treated as a source or trust verdict. An explicit release target keeps
the audit's source identity exact when the audit workflow itself is repaired
after an immutable publication.

## Consequences

- Future tag-triggered Release Audits use the exact artifact-owner API required
  by the current KAG evidence contract.
- The immutable `v0.6.1` tag and GitHub Release are preserved unchanged; a
  manual audit can target `v0.6.1` explicitly and report its result separately.
- Artifact allow, manual review, deny, warn, and unknown remain owner-returned
  raw verdicts; this decision changes workflow compatibility only.
- This follow-up is unreleased main work and is not retroactively included in
  the `v0.6.1` source range.

## Source surfaces

- `.github/workflows/release-audit.yml`
- `.github/workflows/nightly-sentinel.yml`
- `CHANGELOG.md`

## Verification

- verify the exact live `abyss-machine` commit exposes `build_sidecars(subject_root=...)`
- run PR Repo Validation for this workflow-only repair
- dispatch Release Audit with `release_ref=v0.6.1`
- compare the rerun against the immutable tag, Release, and existing artifact
  record; do not infer runtime or human acceptance
