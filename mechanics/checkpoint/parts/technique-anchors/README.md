# Technique Anchors

This part maps current checkpoint-adjacent technique bundles so future
checkpoint work starts from the existing canon instead of redrafting it inside
mechanics.

It does not change technique status. The canonical or promoted meaning remains
inside each `techniques/**/TECHNIQUE.md` file.

## Anchor Map

| Technique | Checkpoint-side relevance | Boundary |
|---|---|---|
| [AOA-T-0057 structured-handoff-before-compaction](../../../../techniques/continuity/handoff-continuation/structured-handoff-before-compaction/TECHNIQUE.md) | Writes one continuation packet before compaction or session rollover. | Does not decide continuation permission, stop, return, or escalation rules across a general phase system. |
| [AOA-T-0058 receipt-confirmed-handoff-packet](../../../../techniques/continuity/handoff-continuation/receipt-confirmed-handoff-packet/TECHNIQUE.md) | Requires visible receipt before the receiver continues from a handoff packet. | Does not author the packet, own transport, or define broader rejection and phase-control policy. |
| [AOA-T-0062 episode-bounded-agent-loop](../../../../techniques/continuity/handoff-continuation/episode-bounded-agent-loop/TECHNIQUE.md) | Breaks longer work into checkpointed episodes with explicit continue, stop, or escalate decisions. | Does not define the handoff artifact shape, startup ritual, budgets, scheduler, or full autonomous platform. |
| [AOA-T-0083 checkpoint-bound-self-repair](../../../../techniques/recovery/diagnosis-repair/checkpoint-bound-self-repair/TECHNIQUE.md) | Keeps self-repair behind approval, rollback, health-check, iteration-limit, and improvement-log posture. | Does not choose the repair shape or authorize autonomous self-modification. |
| [AOA-T-0026 session-capture-as-repo-artifact](../../../../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) | Preserves session history as project-scoped artifacts that can later support review or handoff. | Does not create memory recall semantics, policy authority, or checkpoint implementation truth. |
| [AOA-T-0045 witness-trace-as-reviewable-artifact](../../../../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) | Preserves a bounded run trace before writeback, compost promotion, or canon lift. | Does not own runtime witness generation, memory writeback, proof, or promotion policy. |

## Use

Use this map when a checkpoint-shaped request appears and the smaller existing
technique may already answer it.

If the request needs a new atomic move, send it back through candidate review
instead of editing these anchors into a larger checkpoint doctrine.

## Stop-lines

- Do not treat this map as a generated catalog or technique index replacement.
- Do not change bundle status from this part.
- Do not let checkpoint language override bundle-local contracts, risks,
  validation, or adjacent-technique boundaries.
