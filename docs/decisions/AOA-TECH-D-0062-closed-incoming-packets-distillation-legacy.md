# Closed Incoming Packets Distillation Legacy

Status: accepted for archive placement; active intake placement superseded by `AOA-TECH-D-0061-candidate-intake-active-part-home.md`
Date: 2026-05-18

## Index Metadata

- Decision ID: AOA-TECH-D-0062
- Original date: 2026-05-18
- Surface classes: mechanic package, mechanic part, mechanic evidence, legacy/provenance
- Technique axes: mechanic bridge, review, source-lift
- Mechanic parents: distillation
- Guard families: mechanic topology, part-local artifact, evidence intake, legacy/provenance
- Posture: accepted

## Context

After the current `incoming/` packets were closed, root `incoming/` still looked
like it contained active quarantine work because the closed packet roots stayed
there.

The packets are not repo-wide provenance: they are Distillation donor-wave
lineage for landed bundles, explicit exclusions, and final non-import
verdicts. Root `legacy/` preserves repo-wide receipts, while Distillation
legacy already owns raw-to-active accounting for donor movement.

## Options considered

1. Keep closed packet roots under `incoming/`.
2. Move them to root `legacy/`.
3. Move them to `mechanics/distillation/legacy/archive/closed-incoming-packets/`.

## Decision

Closed root incoming packet roots move to
`mechanics/distillation/legacy/archive/closed-incoming-packets/`.

Active intake placement is now owned by the follow-up candidate-intake decision.
Closed packet roots must move to the owning legacy route after closeout.

## Rationale

Keeping closed packets in `incoming/` makes finished evidence look like live
work. Moving them to root `legacy/` would lose the owner context and mix
Distillation donor-wave receipts with repo-wide topology receipts.

The Distillation legacy archive keeps the evidence close to the mechanic that
interprets it, while the active route remains lighter: current technique
meaning lives in `techniques/**/TECHNIQUE.md`, active intake lives in
`mechanics/distillation/parts/candidate-intake/`, and old packet evidence lives
in the Distillation archive.

## Consequences

- Root `incoming/` is retired as an active intake district by the follow-up
  candidate-intake decision.
- Closed packet READMEs, docs, manifests, registries, and closeout memos remain
  public-safe evidence.
- The archive records former `incoming/*` roots without turning them back into
  candidate queues.
- Current bundle meaning, technique IDs, frontmatter, statuses, and generated
  topology do not change.

## Source surfaces

- `mechanics/distillation/parts/candidate-intake/AGENTS.md`
- `mechanics/distillation/parts/candidate-intake/README.md`
- `mechanics/distillation/PROVENANCE.md`
- `mechanics/distillation/legacy/README.md`
- `mechanics/distillation/legacy/INDEX.md`
- `mechanics/distillation/legacy/archive/closed-incoming-packets/README.md`

## Follow-up route

Use `mechanics/distillation/parts/candidate-intake/` for new public-safe active
intake. Once a packet is closed, preserve it under the owning legacy route and
update Distillation provenance, legacy index/log, changelog, and topology tests.

## Verification

Validate the resulting route with:

Verification was routed through the targeted owner checks and repository validation lanes.
