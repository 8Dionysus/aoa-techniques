# RPG Candidate Mechanic

Status: accepted

Date: 2026-05-03

## Context

`Agents-of-Abyss` already has a center RPG mechanic that frames RPG as world
grammar for progression, quests, campaigns, skills, feats, public presentation,
runtime projection, and owner handoffs. `aoa-techniques` also already has
landed local bundles and mechanics surfaces that carry the technique-layer
side of that pressure, especially progression evidence, multi-axis quest
overlay, owner-layer triage, quest promotion review, nearest-wrong-target
rejection, and the growth-cycle Technique Feat Model.

The local repo needed an RPG mechanics route so future agents can find those
anchors. At the same time, copying the center mechanic or writing broad RPG
law into `aoa-techniques` would blur owner boundaries.

## Decision

Add `mechanics/rpg/` as a candidate-only local mechanics package.

The package maps four local pressure areas:

- source-boundary anchors
- feat-progression anchors
- quest-overlay anchors
- owner-handoff anchors

Create the `legacy/` scaffold for source-to-active accounting. Keep raw
inventory empty because no local pre-split RPG receipt is preserved inside
this repo. Do not claim a direct `ORQ-RPG-TECHNIQUES-*` request or AoA center
acceptance.

## Consequences

- Future agents can route RPG-shaped technique pressure without inventing a
  hidden ontology or local role system.
- Existing RPG-adjacent techniques stay canonical only in their
  `techniques/**/TECHNIQUE.md` homes.
- Feat cards, generated projections, quest overlays, and progression deltas
  remain reader or reflection surfaces until a source owner changes them.
- Stronger owner routes stay explicit: `aoa-agents`, `aoa-skills`,
  `aoa-playbooks`, `aoa-evals`, `aoa-memo`, `abyss-stack`, `aoa-stats`, and
  source-owned `quests/`.
- Stable reusable practice can still graduate later, but only as one bounded
  technique bundle with normal review.

## Verification

Verify with:

```bash
python -m unittest tests.test_rpg_mechanics_topology tests.test_mechanics_request_receipts
python scripts/validate_nested_agents.py
python scripts/validate_repo.py
python -m unittest discover -s tests
```
