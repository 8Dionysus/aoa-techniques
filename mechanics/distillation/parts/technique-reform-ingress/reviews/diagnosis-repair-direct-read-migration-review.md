# Diagnosis-Repair Direct-Read Migration Review

Source packet:
[Technique Reform Ingress](../README.md)

Projection packet:
[Technique Tree Projection](../../../../../reports/technique_tree_projection.md)

Prior pilot review:
[Landed Media-Ingest Pilot Review](landed-media-ingest-pilot-review.md)

Generated lens:
[Technique Tree Projection](../../../../../reports/technique_tree_projection.md)

Tree contract:
[Technique Tree Contract](../../../../../docs/TECHNIQUE_TREE_CONTRACT.md)

Status: accepted-for-fourth-migration-pilot, not path migration, not
`tree_path` frontmatter.

## Verdict

Accept `diagnosis-repair` as the fourth migration pilot.

The move is clearer than current placement because the four bundles share one
recovery question: reviewed friction must be classified, diagnosed, shaped into
the smallest honest repair, and then kept behind explicit checkpoint posture
before any meaningful self-repair happens. `agent-workflows` remains true as
their current `domain`, but it is too broad as a browsing neighborhood for a
post-review recovery chain.

This review does not move files. It only decides that the next bounded wave may
move exactly this shelf if route cards, root legacy receipts, link repair,
generated surfaces, and validation move together.

## Sources Read

- [AOA-T-0080 session-drift-taxonomy](../../../../../techniques/recovery/diagnosis-repair/session-drift-taxonomy/TECHNIQUE.md)
- [AOA-T-0081 diagnosis-from-reviewed-evidence](../../../../../techniques/recovery/diagnosis-repair/diagnosis-from-reviewed-evidence/TECHNIQUE.md)
- [AOA-T-0082 repair-shape-from-diagnosis](../../../../../techniques/recovery/diagnosis-repair/repair-shape-from-diagnosis/TECHNIQUE.md)
- [AOA-T-0083 checkpoint-bound-self-repair](../../../../../techniques/recovery/diagnosis-repair/checkpoint-bound-self-repair/TECHNIQUE.md)
- canonical-readiness notes for `AOA-T-0080` through `AOA-T-0083`
- origin-evidence notes for `AOA-T-0080` through `AOA-T-0083`
- checklists and minimal examples for `AOA-T-0080` through `AOA-T-0083`
- `reports/technique_tree_projection.md` rows for `AOA-T-0080` through
  `AOA-T-0083`
- `reports/technique_topology_scout.md` rows for `AOA-T-0080` through
  `AOA-T-0083`

## Direct Read

| technique | current kind | center of gravity | pilot reading |
|---|---|---|---|
| `AOA-T-0080` `session-drift-taxonomy` | `assessment` | classifies repeated reviewed friction into bounded drift types before causes or owner hints are named | recovery diagnosis starts with a read-only taxonomy layer, not blame or repair execution |
| `AOA-T-0081` `diagnosis-from-reviewed-evidence` | `assessment` | turns reviewed evidence into one diagnosis packet with symptoms, probable causes, owner hints, and unknowns | read-only diagnosis before mutation, not repair planning or final verdict |
| `AOA-T-0082` `repair-shape-from-diagnosis` | `recovery` | converts a reviewed diagnosis into the smallest honest owner-facing repair shape with validation and escalation cues | repair planning after diagnosis, not checkpoint policy or scenario rollout |
| `AOA-T-0083` `checkpoint-bound-self-repair` | `recovery` | wraps a bounded repair shape in explicit approval, rollback, health-check, iteration-limit, and improvement-log posture | checkpoint posture for self-repair, not general approval doctrine or silent self-modification |

The shelf is not merely "post-session cleanup." It is the narrower recovery
seam where reviewed friction becomes a bounded diagnosis and repair path while
mutation remains explicit, reviewable, and reversible.

## Boundary Read

The shelf remains useful only if the bundle boundaries stay sharp:

- `AOA-T-0080` owns drift taxonomy, not probable cause or owner routing.
- `AOA-T-0081` owns diagnosis from reviewed evidence, not repair execution.
- `AOA-T-0082` owns repair-shape selection, not checkpoint posture itself.
- `AOA-T-0083` owns checkpoint posture around bounded self-repair, not the
  diagnosis or the chosen repair shape.

These four techniques are adjacent and sequence-friendly, but they are not one
combined workflow bundle. Keeping them as separate leaves is what makes the
future `diagnosis-repair` shelf legible.

## Mixed Kind Stress

`diagnosis-repair` is a useful fourth pilot because it tests tree-versus-facets
again:

- `AOA-T-0080` and `AOA-T-0081` are `kind: assessment`
- `AOA-T-0082` and `AOA-T-0083` are `kind: recovery`
- all four belong in a recovery district because the browsing question is
  post-review recovery, not the local operation shape

This is exactly the kind of shelf that should be possible in the future tree:
the path groups a practice neighborhood, while `kind` still tells a small agent
which move shape it is executing.

## Why Not Keep This As Agent Workflows

`agent-workflows` remains true as `domain`: all four bundles are reusable
agent-facing workflow techniques.

The directory tree now answers a browsing and placement question. On that
question, `recovery/diagnosis-repair` is tighter than the old broad folder:

- the four bundles already form a visible relation chain from taxonomy to
  diagnosis to repair shape to checkpoint posture
- all four start from reviewed evidence or a reviewed diagnosis rather than
  live improvisation
- the shelf is small enough to direct-read and migrate in one wave
- it tests a new trunk after continuity and ingest have both landed
- it stays away from `boundary-watch`, `split-review-needed`, and singleton
  shelves

## Pilot Scope

Move exactly these four bundles in the next migration wave:

| technique | current path | pilot path |
|---|---|---|
| `AOA-T-0080` | `techniques/agent-workflows/session-drift-taxonomy/` | `techniques/recovery/diagnosis-repair/session-drift-taxonomy/` |
| `AOA-T-0081` | `techniques/agent-workflows/diagnosis-from-reviewed-evidence/` | `techniques/recovery/diagnosis-repair/diagnosis-from-reviewed-evidence/` |
| `AOA-T-0082` | `techniques/agent-workflows/repair-shape-from-diagnosis/` | `techniques/recovery/diagnosis-repair/repair-shape-from-diagnosis/` |
| `AOA-T-0083` | `techniques/agent-workflows/checkpoint-bound-self-repair/` | `techniques/recovery/diagnosis-repair/checkpoint-bound-self-repair/` |

Keep bundle IDs, `domain`, `kind`, `status`, owners, evidence, relations,
checklists, examples, notes, and public-safety posture unchanged.

## Migration Blast Radius

A later migration wave should expect to update:

- authored sibling links inside the four moved bundles
- generated reader docs such as `TECHNIQUE_INDEX.md`, `docs/TECHNIQUE_*`,
  `docs/EVIDENCE_NOTE_SURFACES.md`, and generated manifests
- generated reports for family, topology, and tree projection
- a new `techniques/recovery/AGENTS.md` route card, because `recovery/` would
  become the next migrated trunk
- root `legacy/receipts/` and `legacy/INDEX.md` accounting for the authored
  path migration
- release-check output touched by regenerated catalogs, capsules, sections,
  examples, checklists, evidence notes, and repo-doc surfaces

Do not create mechanic-style `parts/` packages or shelf READMEs for these
technique leaves.

## Stop Lines

- Do not move files from this review pack alone.
- Do not add `family` or `tree_path` frontmatter.
- Do not move another `pilot-candidate` shelf in the same wave.
- Do not rename `diagnosis-repair` during the pilot move.
- Do not change `domain`; the pilot tests path architecture, not owner-lane
  frontmatter.
- Do not widen recovery into self-improvement rhetoric, hidden doctrine edits,
  role-law changes, proof-law changes, or scenario-scale rollout.
- Do not collapse the four leaves into one diagnosis-repair workflow bundle.

## Next Honest Move

Run the fourth pilot migration.

Move exactly `AOA-T-0080` through `AOA-T-0083` into
`techniques/recovery/diagnosis-repair/`, add the minimal `recovery/` route
card, repair authored links, preserve a root legacy receipt, rebuild generated
surfaces, and run `python scripts/release_check.py`.
