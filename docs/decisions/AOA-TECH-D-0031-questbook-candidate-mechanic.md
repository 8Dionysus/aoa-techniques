# Questbook Candidate Mechanic

Status: accepted

Date: 2026-05-03

## Index Metadata

- Decision ID: AOA-TECH-D-0031
- Original date: 2026-05-03
- Surface classes: mechanic package, quest/lane
- Technique axes: mechanic bridge
- Mechanic parents: questbook
- Guard families: mechanic topology, questbook
- Posture: accepted

## Context

`Agents-of-Abyss` has a landed Questbook mechanic that owns common Questbook
law, lifecycle vocabulary, lane-first source model, relation posture,
owner-request packets, and cross-owner route grammar. Its owner request packet
routes recurring quest choreography to `aoa-playbooks`, closure proof to
`aoa-evals`, lessons and recall to `aoa-memo`, and cross-repo handoff routing
to `aoa-routing`.

`aoa-techniques` already has a local Questbook substrate: `QUESTBOOK.md`,
`quests/`, `schemas/quest.schema.json`,
`schemas/quest_dispatch.schema.json`, `generated/quest_catalog.min.json`,
`generated/quest_dispatch.min.json`, and Growth-cycle Questbook integration.
It also has quest-adjacent technique bundles for donor harvest, owner
placement, harvest packets, decision forks, quest-unit promotion review,
nearest-wrong-target rejection, and quest overlays.

The current AoA queue has no direct `ORQ-QUESTBOOK-TECHNIQUES-*` request, so
this repo should not present questbook work as center request acceptance.

## Decision

Add a local `mechanics/questbook/` package as candidate-only practice
pressure around already-landed local Questbook source and projection surfaces.

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

Create three active parts:

- `parts/source-index-anchors/README.md`
- `parts/technique-obligation-anchors/README.md`
- `parts/harvest-promotion-anchors/README.md`

Create the `legacy/` scaffold for source-to-active accounting. Keep raw
inventory empty because no local pre-split Questbook wave receipt or raw source
packet is being preserved.

Do not move `QUESTBOOK.md`, root `quests/`, schemas, or generated quest
projections into the mechanics package. They remain source and projection
surfaces that the mechanics package explains.

Add Questbook to `mechanics/REQUEST_RECEIPTS.md` only under Non-ORQ Center
Pressure, with `candidate-only` posture.

## Consequences

- Questbook pressure becomes discoverable in the mechanics map without
  importing AoA center law as local implementation authority.
- Existing local quest source files and generated quest projections keep their
  current homes and remain validated through existing repo checks.
- Existing quest-adjacent technique bundles remain canonical only through
  their `techniques/**/TECHNIQUE.md` homes.
- A second roadmap, private scratchpad, raw donor backlog, owner acceptance,
  closure proof, proof verdicts, playbook choreography, memory canon, routing
  authority, generated quest truth, RPG playable reading authority, and
  technique promotion stay outside this package.

## Verification

Verify with:

```bash
python -m unittest tests.test_questbook_mechanics_topology tests.test_mechanics_request_receipts tests.test_validate_repo
python scripts/validate_repo.py
python -m unittest discover -s tests
```
