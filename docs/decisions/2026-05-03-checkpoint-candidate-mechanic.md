# Checkpoint Candidate Mechanic

Status: accepted

Date: 2026-05-03

## Context

`Agents-of-Abyss` now has a landed Checkpoint mechanic that owns checkpoint law,
vocabulary, owner map, stop-lines, and cross-owner route grammar. The center
owner map routes implementation controls to `aoa-sdk`, protocol and closeout
bridge behavior to `aoa-skills`, actor posture to `aoa-agents`, memory and
relaunch surfaces to `aoa-memo`, proof to `aoa-evals`, routing hints to
`aoa-routing`, derived visibility to `aoa-stats`, runtime exports to
`abyss-stack`, and reviewed seed lineage to `Dionysus`.

`aoa-techniques` already carries checkpoint-adjacent practice: structured
handoff before compaction, receipt-confirmed handoff packets, episode-bounded
loops, checkpoint-bound self-repair, session capture, witness traces, and the
live `phase_sync_for_agents` to `phase-synchronized-agent-handoff` candidate
lane in distillation.

The current AoA queue has no direct `ORQ-CHECKPOINT-TECHNIQUES-*` request, so
this repo should not present checkpoint work as center request acceptance.

## Decision

Add a local `mechanics/checkpoint/` package as candidate-only practice
pressure.

Create active package route files:

- `AGENTS.md`
- `README.md`
- `DIRECTION.md`
- `PARTS.md`
- `PROVENANCE.md`
- `LANDING_LOG.md`
- `ROADMAP.md`
- `parts/AGENTS.md`
- `parts/README.md`

Create two active parts:

- `parts/phase-handoff-candidate/README.md`
- `parts/technique-anchors/README.md`

Do not create `legacy/raw/` in this pass because no local pre-split checkpoint
wave receipt or raw source packet is being moved.

Add Checkpoint to `mechanics/REQUEST_RECEIPTS.md` only under Non-ORQ Center
Pressure, with `candidate-only` posture.

## Consequences

- Checkpoint pressure becomes discoverable in the mechanics map without
  importing AoA center law as local implementation authority.
- The phase handoff candidate stays staged until evidence shows a standalone
  atomic move with phase boundary, handoff packet, continuation permission, and
  stop/return/escalation rule.
- Existing checkpoint-adjacent technique bundles remain canonical only through
  their `techniques/**/TECHNIQUE.md` homes.
- Checkpoint controls, note protocol, closeout bridge execution, actor
  posture, memory writeback, proof verdicts, runtime activation, route
  authority, stats truth, owner acceptance, hidden scheduler behavior,
  autonomous self-repair, and technique promotion stay outside this package.

## Verification

Verify with:

```bash
python -m unittest tests.test_checkpoint_mechanics_topology tests.test_mechanics_request_receipts tests.test_validate_repo
python scripts/validate_repo.py
python -m unittest discover -s tests
```
