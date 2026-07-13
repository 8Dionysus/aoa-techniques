# Method-Growth Skill Proposal Handoff

Status: accepted

Date: 2026-05-03

## Index Metadata

- Decision ID: AOA-TECH-D-0030
- Original date: 2026-05-03
- Surface classes: mechanic package
- Technique axes: mechanic bridge
- Mechanic parents: method-growth
- Guard families: mechanic topology, sibling-owner boundary
- Posture: accepted

## Context

Method-growth already carried a `technique-to-skill-handoff` part. Its core
signal was not that a technique should become a skill automatically. The signal
was that technique adoption can create pressure for a skill proposal while
technique canon and skill execution stay separate owner truths.

The repository direction now favors one atomic executable move per technique.
Promoting the whole handoff lifecycle would blur adoption, owner consent,
skill authorship, activation, retention, and sibling-owner acceptance.

## Options

- Keep the whole `technique-to-skill-handoff` part mechanics-only.
- Promote the full technique-to-skill lifecycle as one broad technique.
- Extract only the proposal packet handoff and keep acceptance or activation
  outside the technique.

## Decision

Promote one atomic technique:
`AOA-T-0102 skill-proposal-handoff-packet`.

The technique owns one move: from a technique-side adoption review, emit a
bounded proposal packet for a receiving skill owner. The packet carries
technique references, trigger boundary, workflow shape, risks, approval seams,
rollback needs, verification hints, and a non-acceptance stop-line.

It does not create, accept, install, or activate a skill. The receiving skill
owner still owns any accepted skill workflow, trigger contract, packaging,
verification, and activation discipline.

## Consequences

- Method-growth now has a second mechanics-to-canon bridge without collapsing
  mechanics into skill authority.
- External readers can reuse the packet format without deploying OS Abyss.
- `aoa-techniques` gains one more promoted bundle, moving the working corpus to
  `102` bundles: `25` canonical and `77` promoted.
- Promotion-readiness and roadmap counters must track the new working corpus
  while the released version remains `v0.4.2`.
- Future Method-growth retention and obsolescence passes should still extract
  only one atomic practice when the atom survives the contract.

## Verification

The bundle is checked through normal technique validation and generated parity:

Verification was routed through the targeted owner checks and repository validation lanes.
