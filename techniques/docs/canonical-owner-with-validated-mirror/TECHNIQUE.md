---
id: AOA-T-0094
name: canonical-owner-with-validated-mirror
domain: docs
status: promoted
origin:
  project: Dionysus + aoa-stats + aoa-evals + aoa-skills
  path: reports/ecosystem-audits/2026-04-07.cross-repo.aoa-stats-fixpack-rollout-session-harvest.md + aoa-stats/schemas/stats-event-envelope.schema.json + aoa-stats/scripts/build_views.py + aoa-evals/schemas/stats-event-envelope.schema.json + aoa-evals/scripts/validate_repo.py + aoa-skills/config/project_core_skill_kernel.json
  note: Extracted from a live cross-repo contract repair where one shared envelope and event vocabulary moved to a single canonical owner while neighboring mirrors stayed legal only through explicit parity validation.
owners:
  - 8Dionysus
tags:
  - docs
  - source-of-truth
  - mirrors
  - validation
  - schemas
summary: Keep one canonical cross-repo contract owner and allow local mirrors only when explicit parity validation keeps owner metadata and vocabulary exactly aligned.
maturity_score: 3
rigor_level: bounded
reversibility: moderate
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-04-07
export_ready: true
relations:
  - type: complements
    target: AOA-T-0013
  - type: complements
    target: AOA-T-0024
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# canonical-owner-with-validated-mirror

## Intent

Keep one canonical owner for a cross-repo contract while still permitting nearby mirrors, as long as each mirror proves exact parity instead of becoming a second drifting source of truth.

## When to use

- one shared schema, contract, or vocabulary is consumed across several repositories
- a neighboring repository needs a local mirror for bounded workflow reasons such as local validation, docs, or packaging
- ownership metadata and allowed values must stay exact across the canonical copy and every mirror
- the main risk is split-brain drift rather than absence of any shared contract
- consumers should fail fast when a producer invents or misspells a contract token

## When not to use

- every repository can depend directly on the canonical contract and no local mirror is needed
- two repositories genuinely co-own different parts of the contract and the real need is a clearer boundary split
- the local copy is intended to become the new primary editable home
- the real need is only generic single-source distribution inside one repository
- the real need is a runtime rollout route rather than a contract ownership law

## Inputs

- one shared contract that several repositories already consume
- one explicit canonical owner for that contract
- zero or more local mirrors with bounded reasons to exist
- one parity rule covering both ownership metadata and payload vocabulary
- one consumer-side validation path that can reject unknown or drifted tokens

## Outputs

- one explicit canonical contract home
- zero or more legal mirrors that stay subordinate to the canonical source
- one fail-fast parity check for mirrors
- one fail-fast consumer validation path for contract tokens
- lower split-brain risk during cross-repo contract evolution

## Core procedure

1. Name one repository as the canonical owner of the shared contract and make that ownership explicit in the contract metadata.
2. Reduce every neighboring copy to a mirror posture rather than treating it as a second editable source.
3. Encode a small parity rule that checks owner metadata, canonical-reference metadata, and bounded vocabulary values between canonical and mirror copies.
4. Keep consumer intake validation anchored to the canonical vocabulary so unknown tokens fail early.
5. Land contract migrations in the canonical owner first, then update mirrors through parity-preserving sync rather than independent edits by default.
6. If a mirror needs local wrapper logic, keep that wrapper outside the mirrored contract payload.
7. Stop the rollout when parity or intake validation fails instead of normalizing drift as local convenience.

## Contracts

- exactly one repository owns the shared contract
- a mirror is legal only when it stays subordinate to the canonical owner
- parity covers ownership metadata and bounded vocabulary, not just loose shape compatibility
- consumers reject unknown contract tokens early
- migrations move through the canonical owner before mirrors
- local wrappers stay separate from the mirrored contract payload
- this technique stays smaller than rollout sequencing, playbook composition, or runtime publication policy

Relationship to adjacent techniques: unlike [AOA-T-0013](../single-source-rule-distribution/TECHNIQUE.md), this technique governs a cross-repo contract that still permits local mirrors rather than pure fan-out from one source inside one rule-distribution system. Unlike [AOA-T-0024](../upstream-mirroring-with-provenance/TECHNIQUE.md), the mirror here stays inside one federated ecosystem and must prove exact parity rather than mainly preserving external provenance. Unlike [AOA-T-0019](../frontmatter-metadata-spine/TECHNIQUE.md), the goal is not metadata routing in one corpus; it is split-brain prevention for one shared cross-repo contract.

## Risks

### Failure modes

- a mirror starts accepting local edits and becomes a shadow source of truth
- parity checks compare only shape and miss vocabulary drift
- consumer validation stays permissive, so unknown tokens reach derived views before failing
- migration order reverses and a mirror introduces tokens before the canonical owner does

### Negative effects

- strict parity can slow local iteration when contributors are used to editing the nearest copy
- fail-fast vocabulary validation can surface more red checks during migration windows
- a canonical-owner rule adds one more governance boundary contributors need to understand

### Misuse patterns

- using mirrors as convenience patch points because they are closer to the current repository
- claiming a mirror is "temporary" while never adding parity validation
- widening the technique into full rollout orchestration, publisher readiness, or runtime incident handling
- treating consumer tolerance as a safer default than explicit drift detection

### Detection signals

- different repositories list different allowed contract tokens for the same shared envelope
- ownership metadata disagrees between the canonical copy and its mirror
- derived consumers accept unexpected token families or silently ignore them
- a migration requires hand-edited fixes in several mirrors before the canonical copy is stable

### Mitigations

- keep one explicit canonical owner field and one canonical-reference field in mirrored copies
- validate mirror parity against the canonical copy on every repository-level verification path
- reject unknown tokens in consumer intake rather than only in downstream summaries
- land migrations in canonical-first order and keep local wrapper logic outside the mirrored contract file

## Validation

Verify the technique by confirming that:
- the shared contract names exactly one canonical owner
- each mirror carries explicit canonical-reference metadata
- parity validation fails when owner metadata or allowed vocabulary diverges
- consumer validation rejects unknown tokens before derived outputs are built
- local wrapper or packaging logic stays outside the mirrored contract payload

See `checks/canonical-owner-with-validated-mirror-checklist.md`.

## Adaptation notes

What can vary across projects:
- the exact contract format such as JSON Schema, YAML, or typed config
- how mirrors are packaged or referenced locally
- the specific vocabulary being parity-checked
- the exact validator or check command that enforces parity

What should stay invariant:
- one canonical owner remains explicit
- mirrors stay subordinate to that owner
- parity checks cover metadata and bounded vocabulary
- consumer intake rejects unknown tokens early

Project-shaped details that should not be treated as invariant:
- one exact field name such as `x-owner_repo`
- one exact consumer script name such as `build_views.py`
- one exact mirrored repository such as `aoa-evals`
- one exact event family such as receipt envelopes

AoA adaptation example:
- keep the shared stats event envelope canonical in `aoa-stats`
- allow `aoa-evals` to keep a local mirror only when owner metadata and event-kind enum stay exact
- validate `event_kind` against the canonical vocabulary during stats intake so drift fails before summary generation

## Public sanitization notes

This public bundle keeps only the reusable contract law: one canonical owner, legal mirrors only with parity validation, and fail-fast consumer vocabulary checks. Session-local terminal output, private operator context, and repo-specific rollout chatter were left out.

## Example

See `examples/minimal-canonical-owner-with-validated-mirror.md`.

## Checks

See `checks/canonical-owner-with-validated-mirror-checklist.md`.

## Promotion history

- born from the 2026-04-07 cross-repo `aoa-stats` fixpack rollout and follow-on harvest
- promoted into `aoa-techniques` on 2026-04-07 as a bounded law for canonical contract ownership with validated mirrors

## Future evolution

- add a second live context outside the current receipt-envelope lineage before considering canonical promotion
- keep publisher-activation ordering in a sibling playbook instead of widening this bundle into rollout doctrine
- revisit stronger mirror tooling only if more than one federated contract needs the same parity pattern
