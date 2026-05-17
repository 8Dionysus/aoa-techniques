# QUESTBOOK.md — aoa-techniques

This file is the compact public index for durable technique-canon obligations
that should survive the current diff.

It holds repo-level obligations for canon hardening, donor-refinery follow-up,
and generated/source alignment. It is not a second roadmap, not a donor dump,
and not a substitute for technique meaning.

Program direction belongs in [ROADMAP](ROADMAP.md). Technique meaning belongs
in [techniques](techniques/). Candidate movement belongs in
[mechanics](mechanics/README.md).

Use it for:
- promotion-readiness follow-through
- donor-refinery debts that survive the current diff
- generated/source alignment around capsules, exports, and manifests
- repeat routes that should be harvested into durable technique canon

Do not use it for:
- raw donor notes that still belong in intake or review
- snippet ideas that have not survived a bounded diff
- private working chatter or local-only paths
- re-explaining technique meaning that already lives in source docs
- roadmap horizons, release history, or mechanic-local landing history

## Update trigger

Update this root index when an obligation should remain visible across future
work and belongs to the technique canon as a repo-level follow-through.

Use the nearest owner route instead when the obligation is local to one bundle,
mechanic, generated surface, or release:

- [ROADMAP](ROADMAP.md) for direction, horizon posture, and future trigger contours
- [CHANGELOG](CHANGELOG.md) for released repository history
- mechanic landing logs for checked mechanic landings
- mechanic roadmaps for mechanic-local future pressure
- [decisions](docs/decisions/README.md) for durable rationale
- bundle-local notes for technique evidence and review notes

If a closeout leaves a durable obligation but this file stays unchanged, say why
the obligation belongs to another owner route.

## Frontier
- none yet

## Near
- `AOA-TECH-Q-0003` — keep technique capsules, KAG export, and repo-doc surface manifests aligned with source-owned technique sections
- `AOA-TECH-Q-0005` — reflect reviewed techniques as feat cards with mastery-harvest posture
- `AOA-TECH-Q-0006` — reanchor chaos-wave1 technique follow-through at promotion readiness
- `AOA-TECH-Q-0007` — reanchor Agents-of-Abyss v0.4.0 technique follow-through at promotion readiness

## Latent / parked
- `AOA-TECH-Q-0004` — harvest repeated review and evidence-note repair routes into durable technique canon

## Harvest candidates
- `AOA-TECH-Q-0004` — harvest repeated review and evidence-note repair routes into durable technique canon
- `AOA-TECH-Q-0006` — reanchor chaos-wave1 technique follow-through at promotion readiness
- `AOA-TECH-Q-0007` — reanchor Agents-of-Abyss v0.4.0 technique follow-through at promotion readiness

## Backing files

- [quests](quests/) with lane/state layout `quests/<lane>/<state>/`
- [quest schema](schemas/quest.schema.json)
- [quest dispatch schema](schemas/quest_dispatch.schema.json)
- [quest catalog example](generated/quest_catalog.min.example.json)
- [quest dispatch example](generated/quest_dispatch.min.example.json)

## Rule

A quest can survive in this root index only if it keeps repo-level technique
canon follow-through visible without replacing roadmap direction, release
history, mechanic-local ledgers, or bundle-local evidence.
