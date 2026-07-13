# Kag-Source-Lift Direct-Read Migration Review

Source packet:
[Technique Reform Ingress](../README.md)

Projection packet:
[Technique Tree Projection](../reports/technique_tree_projection.md)

Prior pilot review:
[Landed Instruction-Surface Pilot Review](landed-instruction-surface-pilot-review.md)

Generated lens:
[Technique Tree Projection](../reports/technique_tree_projection.md)

Tree contract:
[Technique Tree Contract](../../../../../docs/TECHNIQUE_TREE_CONTRACT.md)

Status: accepted-for-sixth-migration-pilot, not path migration, not
`tree_path` frontmatter.

## Verdict

Accept `kag-source-lift` as the sixth migration pilot.

The move is clearer than current placement because the eight bundles share one
derived-source question: how authored markdown, frontmatter, sections, notes,
relations, risks, repo docs, review templates, and semantic-review docs can be
lifted into bounded reader surfaces without replacing the authored source.
`docs` remains true as their current `domain`, but it is too broad as a
browsing neighborhood for this source-lift cluster.

This review does not move files. It only decides that the next bounded wave may
move exactly this shelf if route cards, root legacy receipts, link repair,
generated surfaces, and validation move together.

## Sources Read

- [AOA-T-0018 markdown-technique-section-lift](../../../../../techniques/knowledge-lift/kag-source-lift/markdown-technique-section-lift/TECHNIQUE.md)
- [AOA-T-0019 frontmatter-metadata-spine](../../../../../techniques/knowledge-lift/kag-source-lift/frontmatter-metadata-spine/TECHNIQUE.md)
- [AOA-T-0020 evidence-note-provenance-lift](../../../../../techniques/knowledge-lift/kag-source-lift/evidence-note-provenance-lift/TECHNIQUE.md)
- [AOA-T-0021 bounded-relation-lift-for-kag](../../../../../techniques/knowledge-lift/kag-source-lift/bounded-relation-lift-for-kag/TECHNIQUE.md)
- [AOA-T-0022 risk-and-negative-effect-lift](../../../../../techniques/knowledge-lift/kag-source-lift/risk-and-negative-effect-lift/TECHNIQUE.md)
- [AOA-T-0046 repo-doc-surface-lift](../../../../../techniques/knowledge-lift/kag-source-lift/repo-doc-surface-lift/TECHNIQUE.md)
- [AOA-T-0047 github-review-template-lift](../../../../../techniques/knowledge-lift/kag-source-lift/github-review-template-lift/TECHNIQUE.md)
- [AOA-T-0048 semantic-review-surface-lift](../../../../../techniques/knowledge-lift/kag-source-lift/semantic-review-surface-lift/TECHNIQUE.md)
- [Docs domain route card](../../../../../techniques/docs/AGENTS.md)
- `mechanics/distillation/parts/technique-reform-ingress/reports/technique_tree_projection.md` rows for `kag-source-lift`,
  `docs-boundary`, `instruction-surface`, `capability-registry`,
  `capability-boundary`, and `skill-discovery`
- [First family shelf review pack](first-family-shelf-review-pack.md)
- [First tree projection review pack](first-tree-projection-review-pack.md)
- [Landed instruction-surface pilot review](landed-instruction-surface-pilot-review.md)

## Direct Read

| technique | status | center of gravity | pilot reading |
|---|---|---|---|
| `AOA-T-0018` `markdown-technique-section-lift` | `canonical` | stable markdown headings into derived section units | section-level lookup after bundle metadata, not authored section files or graph behavior |
| `AOA-T-0019` `frontmatter-metadata-spine` | `canonical` | shallow frontmatter and catalog routing | bundle-level metadata spine, not metadata-first authorship |
| `AOA-T-0020` `evidence-note-provenance-lift` | `promoted` | note kind and note path handles into provenance lookup | supporting-note handles, not note graph or proof objects |
| `AOA-T-0021` `bounded-relation-lift-for-kag` | `canonical` | direct typed relations into one-step adjacency hints | bounded edge hints, not rationale, weighting, traversal, or graph truth |
| `AOA-T-0022` `risk-and-negative-effect-lift` | `promoted` | authored `Risks` language into caution lookup | caution-oriented read surface, not scoring, metadata, or generated policy |
| `AOA-T-0046` `repo-doc-surface-lift` | `promoted` | public repo docs/status set into routing knowledge | bounded repo-doc routing, not docs taxonomy or status policy |
| `AOA-T-0047` `github-review-template-lift` | `promoted` | authored GitHub templates into intake lookup | prompt-shape inventory, not workflow automation, approval, or triage state |
| `AOA-T-0048` `semantic-review-surface-lift` | `promoted` | authored semantic-review docs into cluster lookup | boundary-review lookup, not scoring, status transitions, or machine judgment |

The shelf is not "all KAG work" and not "all docs lifts." It is the narrower
cluster where authored source surfaces become bounded derived reader surfaces
while source authority stays in markdown, frontmatter, notes, or templates.

## Source-Lift Chain

The shelf has an internal chain, not a single mega-technique:

- `AOA-T-0019` is the bundle-level entrypoint: shallow metadata answers the
  first routing question.
- `AOA-T-0018` opens section-level lookup after bundle metadata is no longer
  enough.
- `AOA-T-0020` carries provenance handles from explicit evidence notes.
- `AOA-T-0021` carries direct relation hints once one-step adjacency helps
  navigation.
- `AOA-T-0022` carries caution language from authored `Risks` without turning
  it into policy.
- `AOA-T-0046` applies the same derived-source discipline to public repo-doc
  routing.
- `AOA-T-0047` applies it to GitHub review prompt shapes.
- `AOA-T-0048` applies it to authored semantic-review clusters.

Together they form a `knowledge-lift` shelf because the shared operation is a
bounded lift from source-owned markdown or template surfaces into derived
reader knowledge. They should still remain eight separate leaves because each
leaf has a different source object, consumer question, and misuse boundary.

## Boundary Read

The shelf remains useful only if the source boundary stays sharp:

- section lift keeps section meaning in markdown and does not create authored
  section files, section IDs, or graph semantics.
- metadata spine keeps frontmatter shallow and does not carry full section
  meaning, caution language, or provenance interpretation.
- evidence-note lift preserves note meaning in authored notes and does not
  create proof objects or cross-note graph truth.
- relation lift keeps edges direct and does not infer transitive truth,
  rankings, or traversal policy.
- risk lift keeps caution in authored `Risks` and does not become scoring,
  policy, shadow metadata, or generated caution output.
- repo-doc lift routes to a bounded public docs/status source set and does not
  become a docs taxonomy, local planning map, status policy, or release policy.
- GitHub template lift routes to prompt shape and does not become workflow
  automation, approval policy, triage logic, or review-state storage.
- semantic-review lift routes to authored review docs and does not become a
  scoring system, status driver, graph engine, or machine judge.

## KAG Name Edge

The shelf keeps the historical `kag-source-lift` name because the bundles were
shaped around KAG/source-lift reader pressure, but the path trunk should be
`knowledge-lift`, not `kag`.

That distinction matters. `aoa-techniques` owns reusable source-lift practice.
It does not own `aoa-kag` substrate semantics, graph authority, retrieval
policy, scoring, or automatic verdict behavior. The future route card should
name this stop-line tersely rather than importing KAG doctrine into the
technique tree.

## Mixed Status Stress

`kag-source-lift` is larger than the first five pilots and mixes canonical and
promoted maturity:

- `AOA-T-0018`, `AOA-T-0019`, and `AOA-T-0021` are canonical anchors.
- `AOA-T-0020`, `AOA-T-0022`, `AOA-T-0046`, `AOA-T-0047`, and `AOA-T-0048`
  are promoted source-lift siblings.
- all eight are `domain: docs` and `kind: lift`.

The shared `lift` kind makes this a cleaner tree-versus-facets case than
`instruction-surface`: the stress is not mixed kind, but authority pressure.
The pilot should prove whether a `knowledge-lift` trunk can stay portable and
source-bound without becoming a generated-knowledge owner.

## Why Not Keep This As Docs

`docs` remains true as `domain`: all eight bundles are documentation/source
surface techniques.

The directory tree now answers a browsing and placement question. On that
question, `knowledge-lift/kag-source-lift` is tighter than the old broad
folder:

- all eight bundles protect authored source authority while making a derived
  reader surface useful
- the three canonical anchors already define the metadata, section, and
  relation backbone
- the promoted siblings extend the same source-lift discipline to notes, risks,
  repo docs, templates, and semantic-review docs
- the shelf tests a new `knowledge-lift` trunk after continuity, ingest,
  recovery, and instruction have already landed
- it stays away from `docs-boundary`, `capability-*`, `skill-discovery`, proof,
  governance, runtime, and owner-closeout shelves

## Pilot Scope

Move exactly these eight bundles in the next migration wave:

| technique | current path | pilot path |
|---|---|---|
| `AOA-T-0018` | `techniques/docs/markdown-technique-section-lift/` | `techniques/knowledge-lift/kag-source-lift/markdown-technique-section-lift/` |
| `AOA-T-0019` | `techniques/docs/frontmatter-metadata-spine/` | `techniques/knowledge-lift/kag-source-lift/frontmatter-metadata-spine/` |
| `AOA-T-0020` | `techniques/docs/evidence-note-provenance-lift/` | `techniques/knowledge-lift/kag-source-lift/evidence-note-provenance-lift/` |
| `AOA-T-0021` | `techniques/docs/bounded-relation-lift-for-kag/` | `techniques/knowledge-lift/kag-source-lift/bounded-relation-lift-for-kag/` |
| `AOA-T-0022` | `techniques/docs/risk-and-negative-effect-lift/` | `techniques/knowledge-lift/kag-source-lift/risk-and-negative-effect-lift/` |
| `AOA-T-0046` | `techniques/docs/repo-doc-surface-lift/` | `techniques/knowledge-lift/kag-source-lift/repo-doc-surface-lift/` |
| `AOA-T-0047` | `techniques/docs/github-review-template-lift/` | `techniques/knowledge-lift/kag-source-lift/github-review-template-lift/` |
| `AOA-T-0048` | `techniques/docs/semantic-review-surface-lift/` | `techniques/knowledge-lift/kag-source-lift/semantic-review-surface-lift/` |

Keep bundle IDs, `domain`, `kind`, `status`, owners, evidence, relations,
checklists, examples, notes, and public-safety posture unchanged.

## Migration Blast Radius

A later migration wave should expect to update:

- authored sibling links inside the eight moved bundles
- generated reader docs such as `TECHNIQUE_INDEX.md`, `docs/TECHNIQUE_*`,
  `docs/readers/source-lift/EVIDENCE_NOTE_SURFACES.md`, and generated manifests
- generated KAG export paths while keeping the export derived and
  source-owned
- generated reports for family, topology, and tree projection
- a new `techniques/knowledge-lift/AGENTS.md` route card, because
  `knowledge-lift/` would become the next migrated trunk
- root `legacy/receipts/` and `legacy/INDEX.md` accounting for the authored
  path migration
- docs-domain active references such as selection patterns, source-lift guides,
  repo-doc surface readers, semantic review readers, and any current authored
  links that still point to old homes
- release-check output touched by regenerated catalogs, capsules, sections,
  examples, checklists, evidence notes, source-owned KAG export, and repo-doc
  surfaces

Do not create mechanic-style `parts/` packages or shelf READMEs for these
technique leaves.

## Stop Lines

- Do not move files from this review pack alone.
- Do not add `family` or `tree_path` frontmatter.
- Do not move another `pilot-candidate` shelf in the same wave.
- Do not rename `kag-source-lift` during the pilot move.
- Do not change `domain`; the pilot tests path architecture, not owner-lane
  frontmatter.
- Do not move `docs-boundary`, `capability-registry`,
  `capability-boundary`, `skill-discovery`, proof, governance, runtime, or
  owner-closeout shelves in the same wave.
- Do not treat `knowledge-lift` as `aoa-kag` owner doctrine, graph semantics,
  generated source of truth, retrieval policy, scoring, or automatic verdict
  authority.
- Do not collapse the eight leaves into one source-lift framework bundle.

## Next Honest Move

Run the sixth pilot migration.

Move exactly `AOA-T-0018`, `AOA-T-0019`, `AOA-T-0020`, `AOA-T-0021`,
`AOA-T-0022`, `AOA-T-0046`, `AOA-T-0047`, and `AOA-T-0048` into
`techniques/knowledge-lift/kag-source-lift/`, add the minimal
`knowledge-lift/` route card, repair authored links, preserve a root legacy
receipt, rebuild generated surfaces, and run the release lane.
