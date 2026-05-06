# RPG Provenance

## Status

This package is a local candidate-only mechanics surface. The
[legacy scaffold](legacy/README.md) is present for source-to-active accounting,
and its current raw inventory is empty because no local pre-split RPG wave,
seed, or raw receipt is preserved inside `aoa-techniques`.

The active package was assembled from two kinds of source:

- the AoA center RPG mechanic, which owns the cross-project RPG grammar
- already-landed `aoa-techniques` bundles and mechanics surfaces that carry
  the local technique-layer side of progression, feat, quest-overlay, owner
  placement, and promotion pressure

## AoA Center Bridge

The center bridge was read from `Agents-of-Abyss:mechanics/rpg/`:

- `README.md`
- `DIRECTION.md`
- `PARTS.md`
- `PROVENANCE.md`
- center part surfaces for source boundary, vocabulary overlay, quest/campaign,
  progression/unlocks, runtime projection, and owner handoffs

Those surfaces are constitutional and ecosystem-facing. This package does not
copy them. It keeps only the local technique-layer route that can be reviewed
inside `aoa-techniques`.

## Local Source Bridge

Current local anchors include:

- `techniques/continuity/donor-harvest/progression-evidence-lift/TECHNIQUE.md`
  (`AOA-T-0084`)
- `techniques/continuity/donor-harvest/multi-axis-quest-overlay/TECHNIQUE.md`
  (`AOA-T-0085`)
- `techniques/governance/decision-routing/owner-layer-triage/TECHNIQUE.md`
  (`AOA-T-0076`)
- `techniques/agent-workflows/quest-unit-promotion-review/TECHNIQUE.md`
  (`AOA-T-0089`)
- `techniques/agent-workflows/nearest-wrong-target-rejection/TECHNIQUE.md`
  (`AOA-T-0090`)
- `techniques/proof/skill-support/bounded-context-map/TECHNIQUE.md` (`AOA-T-0016`)
- `mechanics/growth-cycle/parts/technique-feat-model/README.md`
- `mechanics/growth-cycle/parts/mastery-harvest/README.md`
- `mechanics/growth-cycle/parts/promotion-readiness-incubation/README.md`
- `mechanics/questbook/README.md`
- `quests/` and generated quest projection surfaces, as source/projection
  context only
- `generated/technique_feat_cards.min.example.json`, as reader evidence only

## Active Part Bridge

The current local parts are:

- `source-boundary-anchors`
- `feat-progression-anchors`
- `quest-overlay-anchors`
- `owner-handoff-anchors`

## Non-Authority Notes

The local bridge does not establish:

- a direct `ORQ-RPG-TECHNIQUES-*` landing
- AoA center RPG acceptance
- runtime state, role canon, skill truth, playbook choreography, proof
  verdict, quest closure, memory canon, routing authority, owner acceptance,
  universal scoring, or automatic technique promotion

Any future local RPG technique must cite its own source evidence and pass the
normal `techniques/**/TECHNIQUE.md` review path.
