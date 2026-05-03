# Checkpoint

This package owns the `aoa-techniques` side of Checkpoint: phase handoff,
handoff packet, compaction/re-entry, and checkpoint-bound repair pressure that
is not yet a new technique bundle.

Checkpoint here is thinner than the center mechanic in `Agents-of-Abyss`.
The center owns checkpoint law, vocabulary, owner map, stop-lines, and
cross-owner route grammar. This repo only owns reusable practice-shaped
pressure that may later distill into `techniques/**/TECHNIQUE.md`.

## Active route

- [Direction](DIRECTION.md)
- [Parts](PARTS.md)
- [Provenance](PROVENANCE.md)
- [Landing Log](LANDING_LOG.md)
- [Roadmap](ROADMAP.md)

## Functioning parts

- [Phase Handoff Candidate](parts/phase-handoff-candidate/README.md): keeps
  `phase_sync_for_agents` and `phase-synchronized-agent-handoff` visible as an
  active narrowing lane without drafting a premature bundle.
- [Technique Anchors](parts/technique-anchors/README.md): maps current
  checkpoint-adjacent technique bundles without changing their status.

## Boundary

Checkpoint can prepare and document technique-layer practice. It does not
define checkpoint implementation authority, memory canon, proof verdicts,
runtime activation, owner acceptance, hidden scheduler behavior, autonomous
self-repair, route authority, stats truth, or automatic technique promotion.

Stable reusable checkpoint practices may later become technique bundles, but
only through the normal `techniques/**/TECHNIQUE.md` review path.

## AoA relation

`Agents-of-Abyss` owns the center Checkpoint mechanic and current owner map.
The current center queue has no direct `ORQ-CHECKPOINT-TECHNIQUES-*` request,
so local checkpoint pressure is recorded as candidate-only practice pressure in
[Owner Request Receipts](../REQUEST_RECEIPTS.md).
