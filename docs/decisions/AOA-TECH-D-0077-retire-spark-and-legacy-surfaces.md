# Retire Spark and Legacy Technique Surfaces

- Status: Accepted on 2026-09-04
- Baseline commit: [`feffba63dc22fd921512ba5a3ff1b5d78606f93b`](https://github.com/8Dionysus/aoa-techniques/tree/feffba63dc22fd921512ba5a3ff1b5d78606f93b)

## Index Metadata

- Decision ID: AOA-TECH-D-0077
- Original date: 2026-09-04
- Surface classes: root/topology, legacy/provenance, agent mesh, validation guard
- Technique axes: tree placement, source history, owner boundaries
- Mechanic parents: distillation, audit, agon
- Guard families: AGENTS/mesh, roadmap parity, root surface, mechanic topology
- Posture: accepted retirement; historical recovery remains pinned in Git

## Decision

Retire the following historical-only subtrees from the active source tree:

- [`.agents/spark`](https://github.com/8Dionysus/aoa-techniques/tree/feffba63dc22fd921512ba5a3ff1b5d78606f93b/.agents/spark)
- [`legacy`](https://github.com/8Dionysus/aoa-techniques/tree/feffba63dc22fd921512ba5a3ff1b5d78606f93b/legacy)
- [`mechanics/agon/legacy`](https://github.com/8Dionysus/aoa-techniques/tree/feffba63dc22fd921512ba5a3ff1b5d78606f93b/mechanics/agon/legacy)
- [`mechanics/antifragility/legacy`](https://github.com/8Dionysus/aoa-techniques/tree/feffba63dc22fd921512ba5a3ff1b5d78606f93b/mechanics/antifragility/legacy)
- [`mechanics/audit/legacy`](https://github.com/8Dionysus/aoa-techniques/tree/feffba63dc22fd921512ba5a3ff1b5d78606f93b/mechanics/audit/legacy)
- [`mechanics/boundary-bridge/legacy`](https://github.com/8Dionysus/aoa-techniques/tree/feffba63dc22fd921512ba5a3ff1b5d78606f93b/mechanics/boundary-bridge/legacy)
- [`mechanics/checkpoint/legacy`](https://github.com/8Dionysus/aoa-techniques/tree/feffba63dc22fd921512ba5a3ff1b5d78606f93b/mechanics/checkpoint/legacy)
- [`mechanics/distillation/legacy`](https://github.com/8Dionysus/aoa-techniques/tree/feffba63dc22fd921512ba5a3ff1b5d78606f93b/mechanics/distillation/legacy)
- [`mechanics/experience/legacy`](https://github.com/8Dionysus/aoa-techniques/tree/feffba63dc22fd921512ba5a3ff1b5d78606f93b/mechanics/experience/legacy)
- [`mechanics/growth-cycle/legacy`](https://github.com/8Dionysus/aoa-techniques/tree/feffba63dc22fd921512ba5a3ff1b5d78606f93b/mechanics/growth-cycle/legacy)
- [`mechanics/method-growth/legacy`](https://github.com/8Dionysus/aoa-techniques/tree/feffba63dc22fd921512ba5a3ff1b5d78606f93b/mechanics/method-growth/legacy)
- [`mechanics/questbook/legacy`](https://github.com/8Dionysus/aoa-techniques/tree/feffba63dc22fd921512ba5a3ff1b5d78606f93b/mechanics/questbook/legacy)
- [`mechanics/recurrence/legacy`](https://github.com/8Dionysus/aoa-techniques/tree/feffba63dc22fd921512ba5a3ff1b5d78606f93b/mechanics/recurrence/legacy)
- [`mechanics/release-support/legacy`](https://github.com/8Dionysus/aoa-techniques/tree/feffba63dc22fd921512ba5a3ff1b5d78606f93b/mechanics/release-support/legacy)
- [`mechanics/rpg/legacy`](https://github.com/8Dionysus/aoa-techniques/tree/feffba63dc22fd921512ba5a3ff1b5d78606f93b/mechanics/rpg/legacy)

The baseline preserves all 205 retired blobs at their original paths. Active
technique meaning remains under `techniques/**/TECHNIQUE.md`; current Agon
technique binding remains in the move-technique-bridge source, generated
projection, and validator. Historical roadmap and wave references are
recoverable only through this immutable baseline link.

## Consequences

Archive-only cards, Spark validators, and tests that require retired receipts
no longer participate in current topology. Active source, generated catalogs,
and boundary checks remain governed by their existing owners. No archive
directory, service, runtime, or memory artifact is introduced.
