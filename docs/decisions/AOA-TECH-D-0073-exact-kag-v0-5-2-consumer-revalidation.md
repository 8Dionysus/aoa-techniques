# Revalidate Techniques Against Exact aoa-kag v0.5.2

Status: accepted
Date: 2026-08-23

## Index Metadata

- Decision ID: AOA-TECH-D-0073
- Original date: 2026-08-23
- Surface classes: release, CI, provider validation, artifact evidence
- Technique axes: provenance, validation, lifecycle
- Mechanic parents: none
- Guard families: release identity, provider currentness, artifact trust
- Posture: corrective release law

## Context

The published `aoa-kag@v0.5.2` successor revalidated its consumer against the
final `aoa-stats@v0.2.2` provider and changed the KAG provider/generated family
and compatibility-canary boundary. Techniques `v0.6.2` still consumed the
prior published KAG and stats commits. Its next release must be exact-current
against the immutable KAG successor without treating a KAG action identity as
the provider source identity.

## Options considered

1. Keep the `v0.6.2` pins and rely on ancestry or a green historical gate.
2. Move every current consumer lane and local adapter to the exact published
   KAG and stats commits, regenerate owned companions through their builders,
   and preserve the separate KAG action evidence.
3. Reuse or rewrite `v0.6.2` after changing provider declarations.

## Decision

Choose option 2. Direct Techniques consumers must resolve:

- `aoa-kag@v0.5.2` commit
  `8136d3eb629da28cea1206d13a8f1df52ee14739`, annotated tag object
  `251846823f49d18b06c32374b3434e6e11002e96`;
- `aoa-stats@v0.2.2` commit
  `f119805cda69b3edeb2a4c5e407368d70e68650d`, annotated tag object
  `119f434918e8218e43e977b2edec3e4feab6b493`.

The separately observed KAG action identity
`6a79e62c7d20b6b11406dee78f409ada4a51bb3f` remains an action/evidence
identity only; it does not replace the KAG provider tag, peeled commit, or
artifact source ref. The canary pins the exact stats provider but keeps other
scheduled siblings moving by intent and does not become immutable proof.

## Rationale

An exact published commit is the reproducibility boundary for a consumer. A
KAG action or historical evidence commit describes how an owner action ran,
not which KAG source supplied the current provider. Keeping those identities
separate prevents a green action receipt from admitting stale provider source.

## Consequences

- Stale or ancestor-only KAG and stats checkouts fail before local validation.
- The generated KAG export remains subordinate to authored technique bundles
  and is rebuilt rather than hand-edited.
- The required corrective delta is release-bearing, so the successor must
  retain `v0.6.2` and publish a new immutable Techniques release.
- Artifact trust retains the owner's independent `allow`, `warn`, `deny`,
  `manual_review_required`, and `unknown` outcomes. Local agent admission is
  not production/public acceptance.
- The upstream KAG report's missing federation feeds and recovery-only closure
  remain limitations, not silently promoted success claims.

## Source surfaces

- `.github/workflows/repo-validation.yml`
- `.github/workflows/nightly-sentinel.yml`
- `.github/workflows/release-audit.yml`
- `scripts/validate_repo_local_kag_index.py`
- `scripts/validate_local_stats_port.py`
- `CHANGELOG.md`

## Follow-up route

When either published provider tag advances, repeat this exact provider-before-
consumer route. Re-run the artifact-owner trust loop for the landed Techniques
commit and preserve raw consumer verdicts. Runtime deployment, MCP refresh,
proof, delivery, closure, and owner/human acceptance remain separate routes.

## Verification

- `source-fast` checks exact provider identity and authored contracts.
- `generated` checks decision indexes and derived KAG export parity.
- `release` checks the frozen release snapshot and artifact contract.
- The nearest `.github/`, `scripts/`, `generated/`, `kag/`, and
  `docs/decisions/` owner cards remain in force.
