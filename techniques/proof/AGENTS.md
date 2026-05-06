# AGENTS.md

Guidance for coding agents and humans working under `techniques/proof/`.

## Purpose

This trunk stores technique bundles that support validation, review evidence,
summary integrity, owner-truth checks, and related proof-facing practice.

The trunk is a placement aid for browseable technique canon. It is not
`aoa-evals`, not proof verdict authority, and not a replacement for an owning
repository's validation policy.

This is a tree trunk, not a frontmatter domain. Technique bundles here may keep
their existing `domain` and `kind` values when the reviewed move is only path
architecture.

## Current Shelves

Current shelves:

- `skill-support/`: bounded-context vocabulary, consumer-visible contract
  validation, and invariant-oriented coverage around capability or subsystem
  boundaries.
- `evaluation-chain/`: machine-readable validation summaries, staged signal
  promotion, and read-only CI context reporting without becoming CI ownership,
  release policy, eval-suite authority, proof verdict law, or generic quality
  gate doctrine.
- `published-summary/`: stable latest alias storage, bounded remediation
  snapshots, diagnostic integrity snapshots, and required-versus-optional
  summary-source rendering without becoming telemetry owner doctrine,
  dashboard ownership, runtime storage policy, archive governance, remediation
  execution, integrity verdict law, release policy, proof verdict law, or a
  generic reporting platform.
- `review-evidence/`: one-locus claim pressure, one missing-evidence request,
  and one scoped evidence reference without becoming proof verdict authority,
  eval-suite ownership, review-board workflow, Agon move law, actor
  eligibility, source-truth transfer, or evidence adequacy scoring.
- `owner-truth-closeout/`: workspace ingress and mutation guard posture,
  proof-backed finding closeout, GitHub-native owner endcaps, workflow-pinned
  generated publish validation, and canonical-owner mirror parity without
  becoming AoA constitutional authority, root `AGENTS.md` law, workspace
  install doctrine, public-share approval policy, GitHub platform policy,
  release governance, cross-repo mirror co-ownership, skill activation,
  checkpoint automation, or closeout automation.

## Trunk Rules

Keep proof-facing techniques narrow, portable, and explicit about what their
evidence does and does not prove.

## Boundary

Do not widen a proof technique into an eval suite, release gate, runtime
doctor, owner-truth law, security policy, or generic testing doctrine.

If the object becomes a concrete reusable eval bundle, route it to `aoa-evals`.
If it becomes an execution workflow or operational runbook, route it to the
owning repo or `aoa-skills`. If it becomes AoA constitutional direction, route
it to `Agents-of-Abyss`.

## Hard NO

Do not:

- claim that a technique path proves quality by itself
- change `domain` or `kind` frontmatter merely because the bundle now lives
  under `proof/`
- Do not add `tree_path` frontmatter merely because a bundle lives under this
  trunk
- collapse context mapping, contract testing, and invariant coverage into one
  combined proof technique
- collapse summary-contract generation, staged signal promotion, and CI
  context reporting into one combined gate technique
- collapse latest alias storage, remediation snapshot, integrity diagnosis,
  and required-versus-optional rendering into one published-summary package
  technique
- collapse claim challenge, missing-evidence request, and scoped evidence
  reference into one combined proof technique
- collapse ingress guard, audit closeout, GitHub owner endcap, generated
  publish validation, and canonical-owner mirror parity into one combined
  closeout technique
- import sibling-owner authority into a portable technique bundle

## Validation

After changing proof-trunk technique bundles, run:

- `python scripts/validate_nested_agents.py`
- `python scripts/validate_repo.py`

Run `python scripts/release_check.py` when paths, generated reader surfaces, or
catalog outputs change.
