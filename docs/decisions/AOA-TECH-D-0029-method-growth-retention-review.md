# Method-Growth Retention Review

Status: accepted

Date: 2026-05-03

## Index Metadata

- Decision ID: AOA-TECH-D-0029
- Original date: 2026-05-03
- Surface classes: mechanic package
- Technique axes: mechanic bridge, promotion
- Mechanic parents: method-growth
- Guard families: mechanic topology
- Posture: accepted

## Context

Method-growth already carried a `retention-checks` part. Its source signal was
that adopted practice should not remain active forever by inertia. Durable
behavior change needs evidence, rollback, and retention.

The current repository direction requires mechanics-to-canon movement to
extract one atomic practice at a time. Promoting the full retention lifecycle
would blur adoption, activation, obsolescence, proof, memory writeback, and
sibling-owner acceptance.

## Options

- Keep all retention-check material mechanics-only.
- Promote the full retention lifecycle as one broad technique.
- Extract only the post-adoption retention review and leave obsolescence,
  proof, memory, skill, and runtime movement outside the technique.

## Decision

Promote one atomic technique:
`AOA-T-0103 adopted-practice-retention-review`.

The technique owns one assessment: review an already adopted or shadowed
practice against current evidence, owner fit, drift, negative effects, support
cost, rollback or quarantine posture, and next review needs.

It does not adopt a new practice, remove an old practice, activate a skill,
issue proof, write memory truth, or mutate runtime behavior.

## Consequences

- `retention-checks` now has a real bridge from mechanics into canon without
  treating old adoption as permanent approval.
- The new bundle can be used by external readers without deploying OS Abyss.
- `aoa-techniques` gains one more promoted bundle, moving the working corpus to
  `103` bundles: `25` canonical and `78` promoted.
- Promotion-readiness and roadmap counters must track the new working corpus
  while the released version remains `v0.4.2`.
- The remaining Method-growth obsolescence pass should still decide separately
  whether a removable/superseded-practice atom exists.

## Verification

The bundle is checked through normal technique validation and generated parity:

Verification was routed through the targeted owner checks and repository validation lanes.
