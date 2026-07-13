# Instruction-Surface Direct-Read Migration Review

Source packet:
[Technique Reform Ingress](../README.md)

Projection packet:
[Technique Tree Projection](../reports/technique_tree_projection.md)

Prior pilot review:
[Landed Diagnosis-Repair Pilot Review](landed-diagnosis-repair-pilot-review.md)

Generated lens:
[Technique Tree Projection](../reports/technique_tree_projection.md)

Tree contract:
[Technique Tree Contract](../../../../../docs/TECHNIQUE_TREE_CONTRACT.md)

Status: accepted-for-fifth-migration-pilot, not path migration, not
`tree_path` frontmatter.

## Verdict

Accept `instruction-surface` as the fifth migration pilot.

The move is clearer than current placement because the seven bundles share one
instruction-surface question: how agent-facing context, rules, mirrored
sources, nested layers, fragments, and profile/preset surfaces stay explicit,
managed, reviewable, and subordinate to their real source of truth. `docs`
remains true as their current `domain`, but it is too broad as a browsing
neighborhood for this instruction-surface cluster.

This review does not move files. It only decides that the next bounded wave may
move exactly this shelf if route cards, root legacy receipts, link repair,
generated surfaces, and validation move together.

## Sources Read

- [AOA-T-0012 deterministic-context-composition](../../../../../techniques/instruction/instruction-surface/deterministic-context-composition/TECHNIQUE.md)
- [AOA-T-0013 single-source-rule-distribution](../../../../../techniques/instruction/instruction-surface/single-source-rule-distribution/TECHNIQUE.md)
- [AOA-T-0024 upstream-mirroring-with-provenance](../../../../../techniques/instruction/instruction-surface/upstream-mirroring-with-provenance/TECHNIQUE.md)
- [AOA-T-0027 cross-agent-skill-propagation](../../../../../techniques/instruction/instruction-surface/cross-agent-skill-propagation/TECHNIQUE.md)
- [AOA-T-0029 nested-rule-loading](../../../../../techniques/instruction/instruction-surface/nested-rule-loading/TECHNIQUE.md)
- [AOA-T-0030 fragmented-agent-context](../../../../../techniques/instruction/instruction-surface/fragmented-agent-context/TECHNIQUE.md)
- [AOA-T-0035 profile-preset-composition](../../../../../techniques/instruction/instruction-surface/profile-preset-composition/TECHNIQUE.md)
- canonical-readiness notes for `AOA-T-0012`, `AOA-T-0013`, `AOA-T-0024`,
  `AOA-T-0027`, `AOA-T-0029`, `AOA-T-0030`, and `AOA-T-0035`
- checklists for all seven bundles
- `mechanics/distillation/parts/technique-reform-ingress/reports/technique_tree_projection.md` rows for `instruction-surface`
- `mechanics/distillation/parts/technique-reform-ingress/reports/technique_topology_scout.md` rows for `instruction-surface`
- `mechanics/distillation/parts/technique-reform-ingress/reports/technique_family_scout.md` `instruction-surface` family section
- `mechanics/audit/parts/promotion-readiness-matrix/README.md` rows for the
  promoted instruction-surface siblings

## Direct Read

| technique | current kind | center of gravity | pilot reading |
|---|---|---|---|
| `AOA-T-0012` `deterministic-context-composition` | `composition` | composes many source fragments into one deterministic generated context artifact | one-output instruction context composition, not multi-target rule distribution |
| `AOA-T-0013` `single-source-rule-distribution` | `distribution` | keeps one canonical rule source and fans it out to managed instruction targets | local source-to-target instruction distribution, not fragment composition or nested precedence |
| `AOA-T-0024` `upstream-mirroring-with-provenance` | `distribution` | mirrors externally owned content with manifest and attribution preserved | upstream-owned instruction/source mirroring, not local canonical rule fan-out |
| `AOA-T-0027` `cross-agent-skill-propagation` | `distribution` | propagates one shared skill or rule core to multiple agent-facing targets | shared skill/rule propagation, not marketplace policy or runtime role semantics |
| `AOA-T-0029` `nested-rule-loading` | `composition` | loads parent and nested rule layers with explicit precedence | hierarchical instruction loading, not broad multi-target distribution |
| `AOA-T-0030` `fragmented-agent-context` | `composition` | keeps agent context authored in bounded fragments before any generated aggregate | fragment-first instruction authoring, not deterministic assembly itself |
| `AOA-T-0035` `profile-preset-composition` | `composition` | composes modules, profiles, and presets into reviewable runtime posture definitions | profile/preset surface composition, not render truth, lifecycle control, or runtime authority |

The shelf is not "all docs techniques." It is the narrower cluster where
agent-facing instruction and context surfaces are authored, composed,
distributed, mirrored, loaded, or named in a reviewable way without letting the
derived or target surface become hidden primary truth.

## Boundary Read

The shelf remains useful only if the bundle boundaries stay sharp:

- `AOA-T-0012` owns many fragments into one deterministic output, not one source
  into many targets.
- `AOA-T-0013` owns one canonical local rule source fanning out to many managed
  targets, not nested loading or upstream mirroring.
- `AOA-T-0024` owns upstream-owned mirroring with provenance, not local source
  ownership.
- `AOA-T-0027` owns shared skill/rule propagation, not marketplace curation,
  MCP propagation, runtime role semantics, or nested loading.
- `AOA-T-0029` owns hierarchical precedence, not multi-target distribution.
- `AOA-T-0030` owns fragment-first authoring, not final deterministic assembly.
- `AOA-T-0035` owns reviewable profile/preset composition, not rendered runtime
  truth, readiness verdicts, lifecycle commands, or deployment detail.

These seven techniques are adjacent and composition-friendly, but they are not
one instruction framework bundle. Keeping them as separate leaves is what makes
the future `instruction-surface` shelf legible.

## Mixed Kind Stress

`instruction-surface` is a useful fifth pilot because it tests
tree-versus-facets after four smaller migrations:

- `AOA-T-0012`, `AOA-T-0029`, `AOA-T-0030`, and `AOA-T-0035` are
  `kind: composition`
- `AOA-T-0013`, `AOA-T-0024`, and `AOA-T-0027` are `kind: distribution`
- all seven belong in an instruction district because the browsing question is
  agent-facing instruction/context surface management, not the local operation
  shape

This preserves the point of the tree: the path groups a practice neighborhood,
while `kind` still tells a small agent whether it is composing or distributing.

## Profile Edge

`AOA-T-0035` is the sharpest edge in the shelf because it came from
`abyss-stack` profile/preset composition and touches runtime posture language.
It still belongs in the pilot because the bundle itself keeps the reusable move
at the reviewable surface-definition layer: modules, profiles, presets, and
read-only inspection before launch.

It must stay out of runtime truth, readiness checks, lifecycle control,
deployment roots, host details, and one-command service behavior. If a future
direct migration cannot keep that line crisp, `AOA-T-0035` should be held back
rather than forcing the shelf.

## Why Not Keep This As Docs

`docs` remains true as `domain`: all seven bundles are
documentation/source-surface techniques.

The directory tree now answers a browsing and placement question. On that
question, `instruction/instruction-surface` is tighter than the old broad
folder:

- the seven bundles all protect source/target/fragment/layer/preset boundaries
  for agent-facing instruction or context surfaces
- the two canonical anchors, `AOA-T-0012` and `AOA-T-0013`, already define the
  main composition-vs-distribution seam
- the promoted siblings have explicit canonical-readiness gaps without
  undermining their shelf placement
- the shelf tests a docs-rooted trunk after continuity, ingest, and recovery
  have already landed
- it stays away from `kag-source-lift`, `capability-*`, `skill-discovery`,
  proof-boundary, governance, and singleton shelves

## Pilot Scope

Move exactly these seven bundles in the next migration wave:

| technique | current path | pilot path |
|---|---|---|
| `AOA-T-0012` | `techniques/docs/deterministic-context-composition/` | `techniques/instruction/instruction-surface/deterministic-context-composition/` |
| `AOA-T-0013` | `techniques/docs/single-source-rule-distribution/` | `techniques/instruction/instruction-surface/single-source-rule-distribution/` |
| `AOA-T-0024` | `techniques/docs/upstream-mirroring-with-provenance/` | `techniques/instruction/instruction-surface/upstream-mirroring-with-provenance/` |
| `AOA-T-0027` | `techniques/docs/cross-agent-skill-propagation/` | `techniques/instruction/instruction-surface/cross-agent-skill-propagation/` |
| `AOA-T-0029` | `techniques/docs/nested-rule-loading/` | `techniques/instruction/instruction-surface/nested-rule-loading/` |
| `AOA-T-0030` | `techniques/docs/fragmented-agent-context/` | `techniques/instruction/instruction-surface/fragmented-agent-context/` |
| `AOA-T-0035` | `techniques/docs/profile-preset-composition/` | `techniques/instruction/instruction-surface/profile-preset-composition/` |

Keep bundle IDs, `domain`, `kind`, `status`, owners, evidence, relations,
checklists, examples, notes, and public-safety posture unchanged.

## Migration Blast Radius

A later migration wave should expect to update:

- authored sibling links inside the seven moved bundles
- generated reader docs such as `TECHNIQUE_INDEX.md`, `docs/TECHNIQUE_*`,
  `docs/readers/source-lift/EVIDENCE_NOTE_SURFACES.md`, and generated manifests
- generated reports for family, topology, and tree projection
- a new `techniques/instruction/AGENTS.md` route card, because `instruction/`
  would become the next migrated trunk
- root `legacy/receipts/` and `legacy/INDEX.md` accounting for the authored
  path migration
- docs-domain active references such as selection patterns, audit readiness
  anchors, and any current authored links that still point to old homes
- release-check output touched by regenerated catalogs, capsules, sections,
  examples, checklists, evidence notes, and repo-doc surfaces

Do not create mechanic-style `parts/` packages or shelf READMEs for these
technique leaves.

## Stop Lines

- Do not move files from this review pack alone.
- Do not add `family` or `tree_path` frontmatter.
- Do not move another `pilot-candidate` shelf in the same wave.
- Do not rename `instruction-surface` during the pilot move.
- Do not change `domain`; the pilot tests path architecture, not owner-lane
  frontmatter.
- Do not move `kag-source-lift`, `docs-boundary`, `capability-registry`,
  `capability-boundary`, `skill-discovery`, or any proof/governance shelf in
  the same wave.
- Do not widen instruction into AoA constitutional law, skill acceptance,
  runtime authority, generated context authority, or public source-of-truth
  replacement.
- Do not collapse the seven leaves into one instruction framework bundle.

## Next Honest Move

Run the fifth pilot migration.

Move exactly `AOA-T-0012`, `AOA-T-0013`, `AOA-T-0024`, `AOA-T-0027`,
`AOA-T-0029`, `AOA-T-0030`, and `AOA-T-0035` into
`techniques/instruction/instruction-surface/`, add the minimal `instruction/`
route card, repair authored links, preserve a root legacy receipt, rebuild
generated surfaces, and run the release lane.
