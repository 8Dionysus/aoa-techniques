# Docs-Boundary Direct-Read Migration Review

Source packet:
[Technique Reform Ingress](../README.md)

Projection packet:
[Technique Tree Projection](../../../../../reports/technique_tree_projection.md)

Prior pilot review:
[Landed Kag-Source-Lift Pilot Review](landed-kag-source-lift-pilot-review.md)

Tree contract:
[Technique Tree Contract](../../../../../docs/TECHNIQUE_TREE_CONTRACT.md)

Status: accepted-for-seventh-migration-pilot, not path migration, not
`tree_path` frontmatter.

## Verdict

Accept `docs-boundary` as the seventh migration pilot.

The move is clearer than current placement because the four bundles share one
document-boundary question: how a repository keeps document truth, status
snapshots, public-share artifacts, and decision rationale legible without
turning any of those practices into governance doctrine, owner law, approval
policy, execution workflow, or architecture taxonomy.

`docs` remains true as their current `domain`, but it is too broad as a
browsing neighborhood for this boundary-maintenance cluster. The proposed path
under `techniques/instruction/docs-boundary/` fits the instruction trunk
because these techniques shape how authored document surfaces instruct humans
and agents where truth, status, shareability, and rationale live.

This review does not move files. It only decides that the next bounded wave may
move exactly this shelf if route-card update, root legacy receipt, link repair,
generated surfaces, and validation move together.

## Sources Read

- [AOA-T-0002 source-of-truth-layout](../../../../../techniques/instruction/docs-boundary/source-of-truth-layout/TECHNIQUE.md)
- [AOA-T-0009 lightweight-status-snapshot](../../../../../techniques/instruction/docs-boundary/lightweight-status-snapshot/TECHNIQUE.md)
- [AOA-T-0034 public-safe-artifact-sanitization](../../../../../techniques/instruction/docs-boundary/public-safe-artifact-sanitization/TECHNIQUE.md)
- [AOA-T-0033 decision-rationale-recording](../../../../../techniques/instruction/docs-boundary/decision-rationale-recording/TECHNIQUE.md)
- [Docs domain route card](../../../../../techniques/docs/AGENTS.md)
- [Instruction route card](../../../../../techniques/instruction/AGENTS.md)
- `reports/technique_tree_projection.md` rows for `docs-boundary`,
  `instruction-surface`, `capability-registry`, `capability-boundary`, and
  `skill-discovery`
- [First family shelf review pack](first-family-shelf-review-pack.md)
- [First tree projection review pack](first-tree-projection-review-pack.md)
- [Landed kag-source-lift pilot review](landed-kag-source-lift-pilot-review.md)

## Direct Read

| technique | status | kind | center of gravity | pilot reading |
|---|---|---|---|---|
| `AOA-T-0002` `source-of-truth-layout` | `canonical` | `artifact` | document role map and update routing | canonical-home discipline, not governance constitution or architecture taxonomy |
| `AOA-T-0009` `lightweight-status-snapshot` | `canonical` | `artifact` | short entrypoint status that links to canonical detail | snapshot discipline, not status authority or long history storage |
| `AOA-T-0034` `public-safe-artifact-sanitization` | `canonical` | `guardrail` | public-safe share-prep for sensitive technical artifacts | shareable artifact boundary, not approval gating, execution planning, incident response, or proof that the underlying action is safe |
| `AOA-T-0033` `decision-rationale-recording` | `promoted` | `artifact` | one compact decision note with context, options, rationale, and consequences | decision rationale, not source-of-truth governance, boundary mapping, or architecture classification |

The shelf is not "all docs hygiene" and not "all governance-adjacent
documentation." It is the narrower cluster where the technique teaches a reader
or agent where document truth stops, where compact status belongs, what may be
shared, or why one decision was made.

## Boundary Chain

The shelf has a useful internal sequence without becoming one workflow:

- `AOA-T-0002` sets the document-role map so recurring information has one
  canonical home.
- `AOA-T-0009` keeps top-level status as a short route into those homes rather
  than a duplicate log.
- `AOA-T-0034` protects public-share artifacts when material needs to leave the
  local context.
- `AOA-T-0033` records one meaningful decision when the reason must survive
  future review.

Together they form a `docs-boundary` shelf because each leaf guards a document
boundary that prevents drift, leakage, false authority, or rationale loss. They
should remain four separate leaves because each one has a different input,
output, misuse boundary, and validation cue.

## Instruction Trunk Fit

The proposed trunk is `instruction`, not because the techniques are prompt
instructions, but because they shape instruction-facing repository surfaces:
document roles, status snapshots, public-safe artifacts, and decision notes are
the surfaces that tell future humans and agents where to look, what to trust,
what may be shared, and what tradeoff was accepted.

The existing `techniques/instruction/AGENTS.md` is already the right trunk
route card. A later migration should update its current scope to include
`docs-boundary/` without turning the trunk into AoA doctrine, approval policy,
runtime role law, or source-of-truth governance.

## Mixed Kind Stress

`docs-boundary` mixes `artifact` and `guardrail`:

- `AOA-T-0002`, `AOA-T-0009`, and `AOA-T-0033` are document artifacts.
- `AOA-T-0034` is a public-share guardrail.
- all four are `domain: docs`.
- three are canonical, and one is promoted.

The mixed kind is acceptable because the placement question is not move shape;
it is document-boundary browsing. The guardrail leaf belongs here only because
public-safe artifact preparation protects what may leave a document surface.
It should not pull approval, incident response, dry-run planning, or infra
execution into the shelf.

## Why Not Keep This As Docs

`docs` remains true as `domain`: all four techniques operate on documentation,
status, artifacts, or rationale notes.

The directory tree now answers a browsing and placement question. On that
question, `instruction/docs-boundary` is tighter than the old broad folder:

- `source-of-truth-layout` gives the canonical-home map
- `lightweight-status-snapshot` keeps entrypoints short and linked
- `public-safe-artifact-sanitization` keeps shareable artifacts bounded
- `decision-rationale-recording` keeps one decision's reason reviewable
- the shelf stays away from capability registry, skill discovery, proof,
  governance, runtime, and owner-closeout authority

## Pilot Scope

Move exactly these four bundles in the next migration wave:

| technique | current path | pilot path |
|---|---|---|
| `AOA-T-0002` | `techniques/docs/source-of-truth-layout/` | `techniques/instruction/docs-boundary/source-of-truth-layout/` |
| `AOA-T-0009` | `techniques/docs/lightweight-status-snapshot/` | `techniques/instruction/docs-boundary/lightweight-status-snapshot/` |
| `AOA-T-0034` | `techniques/docs/public-safe-artifact-sanitization/` | `techniques/instruction/docs-boundary/public-safe-artifact-sanitization/` |
| `AOA-T-0033` | `techniques/docs/decision-rationale-recording/` | `techniques/instruction/docs-boundary/decision-rationale-recording/` |

Keep bundle IDs, `domain`, `kind`, `status`, owners, evidence, relations,
checklists, examples, notes, and public-safety posture unchanged.

## Migration Blast Radius

A later migration wave should expect to update:

- authored sibling links inside the four moved bundles
- generated reader docs such as `TECHNIQUE_INDEX.md`, `docs/TECHNIQUE_*`,
  `docs/EVIDENCE_NOTE_SURFACES.md`, and generated manifests
- generated KAG export paths while keeping the export derived and source-owned
- generated reports for family, topology, and tree projection
- `techniques/instruction/AGENTS.md` current scope and domain rules, because
  `instruction/` would gain a second landed shelf
- root `legacy/receipts/` and `legacy/INDEX.md` accounting for the authored
  path migration
- active mechanics review rows that still point to old homes
- release-check output touched by regenerated catalogs, capsules, sections,
  examples, checklists, evidence notes, source-owned KAG export, and repo-doc
  surfaces

Do not create mechanic-style `parts/` packages or shelf READMEs for these
technique leaves.

## Stop Lines

- Do not move files from this review pack alone.
- Do not add `family` or `tree_path` frontmatter.
- Do not move another `candidate` or `pilot-candidate` shelf in the same wave.
- Do not change `domain`; the pilot tests path architecture, not owner-lane
  frontmatter.
- Do not move `capability-registry`, `capability-boundary`,
  `skill-discovery`, proof, governance, runtime, owner-closeout, or
  knowledge-lift shelves in the same wave.
- Do not turn `docs-boundary` into source-of-truth governance, AoA
  constitutional law, approval policy, skill acceptance, proof authority,
  runtime role law, or architecture taxonomy.
- Do not collapse the four leaves into one documentation-governance framework
  bundle.

## Next Honest Move

Run the seventh pilot migration.

Move exactly `AOA-T-0002`, `AOA-T-0009`, `AOA-T-0034`, and `AOA-T-0033` into
`techniques/instruction/docs-boundary/`, update the existing
`instruction/` route card, repair authored links, preserve a root legacy
receipt, rebuild generated surfaces, and run `python scripts/release_check.py`.
