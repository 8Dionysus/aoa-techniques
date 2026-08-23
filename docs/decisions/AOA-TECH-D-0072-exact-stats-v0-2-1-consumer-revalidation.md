# Revalidate Exact aoa-stats v0.2.1 Before the Next Techniques Release

Status: accepted
Date: 2026-08-23

## Index Metadata

- Decision ID: AOA-TECH-D-0072
- Original date: 2026-08-23
- Surface classes: release, CI, provider validation
- Technique axes: provenance, validation, lifecycle
- Mechanic parents: none
- Guard families: release identity, provider currentness, workflow topology
- Posture: corrective release law

## Context

The published `aoa-stats@v0.2.1` release advances the exact provider commit
from `dc608fd5de3fcaf0301f356c9efd52e2bdd350ce` to
`339ecb2db22ac4552fa88756b650896ebbff5b56`. The immutable `aoa-techniques`
`v0.6.1` release predates that provider transition. Its tag-scoped Release
Audit also exposed a separate workflow contract drift: the owner validator
passed `subject_root` to `build_sidecars`, while the tag workflow checked out
an older `abyss-machine` API that rejected the keyword.

## Options considered

1. Keep the old stats pin because the current main Release Audit was green.
2. Move current consumer lanes to the exact published stats commit, enforce
   that identity in the local adapter, and retain the immutable `v0.6.1`
   history unchanged.
3. Rewrite or retag `v0.6.1` after repairing the workflow provider.

## Decision

Choose option 2. Current repo-validation, release-audit, and nightly lanes
must checkout the exact published stats commit `339ecb2d…`; the local stats
adapter must reject any checkout whose `HEAD` differs from that commit. The
release-audit and nightly artifact-tool lanes remain pinned to the exact
`abyss-machine` commit that accepts `build_sidecars(subject_root=...)`, and
the manual `release_ref` route remains the way to audit an immutable target
without changing its tag or Release.

The published `v0.6.1` changelog, tag, Release, and artifact record remain
historical evidence. The exact KAG provider pin remains
`813a7f69dc96ec031dad9b897a6991792cc48b7a`; this decision does not claim that
the KAG provider's own historical stats edge has been rewritten or that a
derived KAG index is current merely because its MCP projection is stale.

## Rationale

An exact published provider commit is the smallest identity that makes a
consumer revalidation reproducible. A green check against a later main commit
does not repair a failed immutable tag audit, and a moving local sibling
checkout cannot prove which provider contract was exercised. Keeping the
artifact-owner repair and stats-provider transition as separate source claims
preserves the owner boundaries while making the next release auditable.

## Consequences

- Current source and release lanes fail closed on stale or ancestor-only stats
  checkouts.
- The immutable `v0.6.1` tag and GitHub Release remain unchanged; a future
  patch successor carries the new provider contract if the release lane and
  tag-scoped audit pass.
- The artifact registry remains the authority for artifact admission. Its
  `agent`, `release_consumer`, and `public_release` verdicts are retained
  independently and are not rewritten by this source change.
- KAG MCP/index freshness remains a bounded federation observation, not a
  source or release authority claim.

## Source surfaces

- `.github/workflows/repo-validation.yml`
- `.github/workflows/release-audit.yml`
- `.github/workflows/nightly-sentinel.yml`
- `scripts/validate_local_stats_port.py`
- `scripts/validate_abyss_machine_kag_export_bundle.py`
- `tests/test_github_workflow_topology.py`
- `tests/test_local_stats_port.py`
- `CHANGELOG.md`

## Follow-up route

After the source PR lands, run the release lane with the exact published
provider set, prepare the patch release only if that source result is green,
then run the tag-scoped Release Audit with its exact release ref. Refresh the
artifact binding to the successor commit through the artifact owner route;
preserve raw manual-review verdicts and report runtime, proof, delivery,
closure, and acceptance separately.

## Verification

- `source-fast` checks the exact local provider and source contracts.
- `generated` checks decision indexes and derived parity.
- `release` checks the frozen release snapshot and KAG artifact validator.
- Workflow topology tests check both exact provider pins and the
  `build_sidecars(subject_root=...)` owner contract.
