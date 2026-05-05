# Technique Reform Ingress

This part is the entry packet for future classification reform in
`aoa-techniques`.

Use it when the next task is not to add one technique, but to prepare a bounded
reform wave over technique classification, selection, generated topology, or
future axis promotion.

It is not a schema migration, not a generated-catalog rewrite, and not a
permission slip to remap techniques automatically.

## Current Contour

- public corpus: `107` bundles, `25` canonical, `82` promoted
- authoritative frontmatter axes: `domain`, `kind`
- corpus tree: design contract only, not migrated path truth
- scout or design axes: `family`, `capability_class`, `substrate`,
  `execution_profile`, `risk_posture`, richer `relations`
- family seed: `26` scout families, still weaker than bundle frontmatter
- topology scout review pack: landed as a human review layer, not schema truth
- kind ambiguity review pack: landed from direct bundle reading, not remap
  authority
- second kind ambiguity review pack: landed as the updated-audit read; it holds
  old false positives and routes `AOA-T-0054` to a destination check
- `AOA-T-0054` destination check: landed as a bounded correction from
  `handoff` to `recovery`
- post-`AOA-T-0054` kind-audit hold review: landed as the close of the current
  remap lane; no new frontmatter candidate chosen
- family shelf review: landed as a tree-fitness review over `26` scout
  families; `family` remains scout-only and the corpus tree remains unmigrated
- tree projection: landed as a generated, non-authoritative tree projection
  and placement review over all `107` bundles
- first tree projection review: landed with `review-compaction` selected for
  direct-read migration review, not path movement
- review-compaction direct-read review: landed as
  `accepted-for-first-migration-pilot`; still not path movement
- landed review-compaction pilot review: landed as `pilot-validated`, with
  `handoff-continuation` chosen for the next direct-read migration review
- handoff-continuation direct-read review: landed as
  `accepted-for-second-migration-pilot`; still not path movement
- handoff-continuation migration: landed exactly `AOA-T-0056` through
  `AOA-T-0062` under `techniques/continuity/handoff-continuation/`
  without frontmatter changes
- landed handoff-continuation pilot review: landed as `pilot-validated`, with
  `media-ingest` chosen for the next direct-read migration review
- media-ingest direct-read review: landed as
  `accepted-for-third-migration-pilot`; still not path movement
- media-ingest migration: landed exactly `AOA-T-0070` through `AOA-T-0074`
  under `techniques/ingest/media-ingest/` without frontmatter changes
- landed media-ingest pilot review: landed as `pilot-validated`, with
  `diagnosis-repair` chosen for the next direct-read migration review
- diagnosis-repair direct-read review: landed as
  `accepted-for-fourth-migration-pilot`; still not path movement
- diagnosis-repair migration: landed exactly `AOA-T-0080` through `AOA-T-0083`
  under `techniques/recovery/diagnosis-repair/` without frontmatter changes
- landed diagnosis-repair pilot review: landed as `pilot-validated`, with
  `instruction-surface` chosen for the next direct-read migration review
- instruction-surface direct-read review: landed as
  `accepted-for-fifth-migration-pilot`; still not path movement
- instruction-surface migration: landed exactly `AOA-T-0012`, `AOA-T-0013`,
  `AOA-T-0024`, `AOA-T-0027`, `AOA-T-0029`, `AOA-T-0030`, and `AOA-T-0035`
  under `techniques/instruction/instruction-surface/` without frontmatter
  changes
- landed instruction-surface pilot review: landed as `pilot-validated`, with
  `kag-source-lift` chosen for the next direct-read migration review
- kag-source-lift direct-read review: landed as
  `accepted-for-sixth-migration-pilot`; still not path movement
- kag-source-lift migration: landed exactly `AOA-T-0018`, `AOA-T-0019`,
  `AOA-T-0020`, `AOA-T-0021`, `AOA-T-0022`, `AOA-T-0046`, `AOA-T-0047`,
  and `AOA-T-0048` under
  `techniques/knowledge-lift/kag-source-lift/` without frontmatter changes
- landed kag-source-lift pilot review: landed as `pilot-validated`, with
  `docs-boundary` chosen for the next direct-read migration review
- docs-boundary direct-read review: landed as
  `accepted-for-seventh-migration-pilot`; still not path movement
- docs-boundary migration: landed exactly `AOA-T-0002`, `AOA-T-0009`,
  `AOA-T-0034`, and `AOA-T-0033` under
  `techniques/instruction/docs-boundary/` without frontmatter changes
- landed docs-boundary pilot review: landed as `pilot-validated`, with
  `capability-registry` chosen for the next direct-read migration review
- Agon handoff proof point: `3` gate-to-bundle routes landed, `8` ungated
  first-narrowing candidates remain in `first_narrowing_frontier`

## Evidence Stack

| Surface | What it proves | What it does not prove |
|---|---|---|
| [Technique Atom Contract](../../../../docs/TECHNIQUE_ATOM_CONTRACT.md) | technique unit is one atomic executable move, portable and small-agent shaped | which future classification axis should become schema truth |
| [Technique Topology Contract](../../../../docs/TECHNIQUE_TOPOLOGY_CONTRACT.md) | classification is faceted and `domain + kind` are current truth | readiness to migrate every bundle frontmatter field |
| [Technique Tree Contract](../../../../docs/TECHNIQUE_TREE_CONTRACT.md) | future root path architecture should be a tree of trunks, shelves, and leaf bundles | authority to move every bundle or make `tree_path` required frontmatter |
| [Technique Kind Registry](../../../../config/technique_kind_registry.yaml) | current `kind` values and tie-break rules | that Agon handoff labels like `trace-probe` or `review` are valid kind values |
| [Technique Family Seed](../../../../config/technique_family_seed.yaml) | scout shelf candidates and family constraints | authoritative family assignment for every bundle |
| [Technique Topology Axes Registry](../../../../config/technique_topology_axes.yaml) | scout values for `capability_class`, `substrate`, `execution_profile`, and `risk_posture` | required frontmatter fields or automatic bundle remapping |
| [Technique Topology Scout](../../../../reports/technique_topology_scout.md) | current generated projection over scout axes for review pressure | schema truth, migration authority, or bundle meaning |
| [First Topology Scout Review Pack](reviews/first-topology-scout-review-pack.md) | first human readout from the scout projection and the next review lane | schema migration, bundle remap authority, or proof of generated correctness |
| [Technique Family Scout](../../../../reports/technique_family_scout.md) | generated family counts and likely clusters | automatic frontmatter migration authority |
| [Technique Tree Projection](../../../../reports/technique_tree_projection.md) | generated future trunk/shelf/path projection over all `107` bundles | path migration, `tree_path` frontmatter truth, or proof that future paths are current links |
| [Kind Ambiguity Audit](../../../../reports/kind_ambiguity_audit.md) | tie-break seams that deserve human review | automatic remap authority |
| [First Kind Ambiguity Review Pack](reviews/first-kind-ambiguity-review-pack.md) | direct-read shortlist for later narrow remap work | frontmatter mutation, new kind authority, or status change |
| [Second Kind Ambiguity Review Pack](reviews/second-kind-ambiguity-review-pack.md) | updated-audit read that routes `AOA-T-0054` to a `handoff` / `workflow` / `recovery` destination check | frontmatter mutation or proof that `AOA-T-0054` must move |
| [AOA-T-0054 Kind Destination Check](reviews/0054-kind-destination-check.md) | direct-read destination verdict for `AOA-T-0054` from `handoff` toward `recovery` | schema migration, status promotion, or sibling-owner authority |
| [Post-0054 Kind Audit Hold Review](reviews/post-0054-kind-audit-hold-review.md) | closes the current kind-audit remap lane and classifies remaining generated pressure as holds or calibration | frontmatter mutation, family promotion, tree migration, or proof of generated correctness |
| [First Family Shelf Review Pack](reviews/first-family-shelf-review-pack.md) | reviews all `26` scout families for stable shelf candidates, boundary watch, split pressure, singleton holds, and trunk fitness | `family` frontmatter truth, path migration, schema change, or proof that the draft tree is final |
| [First Tree Projection Review Pack](reviews/first-tree-projection-review-pack.md) | accepts the generated projection as a review surface and chooses `review-compaction` for direct-read pilot review | path movement, `tree_path` frontmatter, bulk migration, or trunk finality |
| [Review-Compaction Direct-Read Migration Review](reviews/review-compaction-direct-read-migration-review.md) | reads `AOA-T-0051`, `AOA-T-0052`, and `AOA-T-0054` directly and accepts the shelf as the first migration pilot | `tree_path` frontmatter, domain change, or permission to move any other shelf |
| [Landed Review-Compaction Pilot Review](reviews/landed-review-compaction-pilot-review.md) | confirms the first migrated shelf stayed clearer, validated, and bounded after landing | movement of `handoff-continuation`, `tree_path` frontmatter, or proof that all continuity shelves are safe |
| [Handoff-Continuation Direct-Read Migration Review](reviews/handoff-continuation-direct-read-migration-review.md) | reads `AOA-T-0056` through `AOA-T-0062` directly and accepts the shelf as the second migration pilot | path movement, `tree_path` frontmatter, domain change, or permission to move any other shelf |
| [Landed Handoff-Continuation Pilot Review](reviews/landed-handoff-continuation-pilot-review.md) | confirms the second migrated shelf stayed clearer, validates the continuity trunk machinery, and chooses `media-ingest` for the next direct-read review | movement of `media-ingest`, `tree_path` frontmatter, or proof that every trunk is ready |
| [Media-Ingest Direct-Read Migration Review](reviews/media-ingest-direct-read-migration-review.md) | reads `AOA-T-0070` through `AOA-T-0074` directly and accepts the shelf as the third migration pilot | path movement, `tree_path` frontmatter, domain change, or permission to move another shelf |
| [Landed Media-Ingest Pilot Review](reviews/landed-media-ingest-pilot-review.md) | confirms the third migrated shelf stayed clearer, validates the first non-continuity trunk test, and chooses `diagnosis-repair` for the next direct-read review | movement of `diagnosis-repair`, `tree_path` frontmatter, or proof that every non-continuity trunk is safe |
| [Diagnosis-Repair Direct-Read Migration Review](reviews/diagnosis-repair-direct-read-migration-review.md) | reads `AOA-T-0080` through `AOA-T-0083` directly and accepts the shelf as the fourth migration pilot | path movement, `tree_path` frontmatter, domain change, or permission to move another shelf |
| [Landed Diagnosis-Repair Pilot Review](reviews/landed-diagnosis-repair-pilot-review.md) | confirms the fourth migrated shelf stayed clearer, validates the recovery trunk machinery, and chooses `instruction-surface` for the next direct-read review | movement of `instruction-surface`, `tree_path` frontmatter, or proof that every docs-domain shelf is safe |
| [Instruction-Surface Direct-Read Migration Review](reviews/instruction-surface-direct-read-migration-review.md) | reads `AOA-T-0012`, `AOA-T-0013`, `AOA-T-0024`, `AOA-T-0027`, `AOA-T-0029`, `AOA-T-0030`, and `AOA-T-0035` directly and accepts the shelf as the fifth migration pilot | path movement by review alone, `tree_path` frontmatter, domain change, or permission to move another shelf |
| [Landed Instruction-Surface Pilot Review](reviews/landed-instruction-surface-pilot-review.md) | confirms the fifth migrated shelf stayed clearer, validates the first instruction trunk machinery, and chooses `kag-source-lift` for the next direct-read review | movement of `kag-source-lift`, `tree_path` frontmatter, KAG owner authority, or proof that every docs-lift shelf is safe |
| [Kag-Source-Lift Direct-Read Migration Review](reviews/kag-source-lift-direct-read-migration-review.md) | reads `AOA-T-0018`, `AOA-T-0019`, `AOA-T-0020`, `AOA-T-0021`, `AOA-T-0022`, `AOA-T-0046`, `AOA-T-0047`, and `AOA-T-0048` directly and accepts the shelf as the sixth migration pilot | path movement by review alone, `tree_path` frontmatter, KAG owner doctrine, graph authority, scoring, policy, or generated verdicts |
| [Landed Kag-Source-Lift Pilot Review](reviews/landed-kag-source-lift-pilot-review.md) | confirms the sixth migrated shelf stayed clearer, validates the first knowledge-lift trunk machinery, and chooses `docs-boundary` for the next direct-read review | movement of `docs-boundary`, `tree_path` frontmatter, KAG owner authority, or proof that every instruction boundary shelf is safe |
| [Docs-Boundary Direct-Read Migration Review](reviews/docs-boundary-direct-read-migration-review.md) | reads `AOA-T-0002`, `AOA-T-0009`, `AOA-T-0034`, and `AOA-T-0033` directly and accepts the shelf as the seventh migration pilot | path movement by review alone, `tree_path` frontmatter, source-of-truth governance, approval policy, skill acceptance, proof authority, runtime role law, or architecture taxonomy |
| [Landed Docs-Boundary Pilot Review](reviews/landed-docs-boundary-pilot-review.md) | confirms the seventh migrated shelf stayed clearer, validates the second instruction trunk shelf, and chooses `capability-registry` for the next direct-read review | movement of `capability-registry`, `tree_path` frontmatter, registry product doctrine, discovery ranking, trust policy, marketplace curation, graph semantics, runtime resolution, or agent-role authority |
| [Agon First-Narrowing Frontier](../agon-candidate-handoff/gates/frontier/first-narrowing-frontier-review.md) | why capability, substrate, execution, and risk axes matter before new kinds | readiness to add new required fields or promote Agon source status |
| [Agon Handoff Generated Index](../agon-candidate-handoff/generated/agon_candidate_handoff.min.json) | current machine-readable frontier, pipeline counts, and topology cues | technique canon or Agon acceptance |

## First Reform Pass Shape

A first reform pass may:

- add or improve non-required generated projections for scout/design axes
- review `family` as an optional shelf axis without making it required
- use the kind ambiguity audit to choose a small remap review pack
- add tests that keep generated topology weaker than authored bundle meaning
- add a decision note before any schema, template, or validator contract changes

It should continue one bounded slice at a time:

1. `family` optional shelf review, now landed as review evidence only
2. non-authoritative `tree_path` projection after family shelves are reviewed,
   now landed as generated review evidence only
3. generated `capability_class` / `substrate` / `execution_profile` /
   `risk_posture` scout projection
4. one kind tie-break review pack from `reports/kind_ambiguity_audit.md`
5. relation topology guidance only after direct relations repeatedly help
   composition, conflict, sequence, or prerequisite routing

## Stop Lines

- Do not add new required frontmatter fields in the first ingress pass.
- Do not migrate the `techniques/` directory tree before a projection-first
  review identifies one bounded pilot subtree.
- Do not add new `kind` values from handoff cues like `trace-probe`,
  `diagnosis`, `review`, `comparison`, `boundary`, or `stress-case`.
- Do not remap bundle frontmatter from generated reports without reading the
  bundle meaning.
- Do not turn `family` into status, quality score, or promotion readiness.
- Do not collapse `capability_class`, `substrate`, `execution_profile`, or
  `risk_posture` into tags forever if they keep proving selection value.
- Do not let mechanics rewrite canonical technique meaning; reform must land
  through docs, config, schema, templates, generated surfaces, tests, and
  decision records together.

## Entry Checklist

- [ ] Read the atom contract and topology contract.
- [ ] Read the kind registry and kind guide before proposing a `kind` change.
- [ ] Read the family seed, family scout, and kind ambiguity audit.
- [ ] Read the technique tree contract before proposing path migration.
- [ ] Read the Agon frontier review and generated handoff lens for fresh
      topology pressure.
- [ ] Choose one bounded reform slice and state what remains scout-only.
- [ ] Add or update the decision note before schema, template, or validator
      changes.
- [ ] Run the narrow builders touched by the slice plus `python scripts/release_check.py`.

## Next Honest Move

The first pilot migration has moved exactly `AOA-T-0051`, `AOA-T-0052`, and
`AOA-T-0054` into `techniques/continuity/review-compaction/` without changing
frontmatter, adding `tree_path`, or moving another shelf.

The second pilot migration moved exactly `AOA-T-0056` through `AOA-T-0062`
into `techniques/continuity/handoff-continuation/` without changing
frontmatter or adding `tree_path`.

The third pilot migration moved exactly `AOA-T-0070` through `AOA-T-0074`
into `techniques/ingest/media-ingest/` without changing frontmatter or adding
`tree_path`.

The landed `media-ingest` pilot review is now landed as `pilot-validated` and
chooses `diagnosis-repair` for the next direct-read migration review.

The `diagnosis-repair` direct-read review is now landed and accepts exactly
`AOA-T-0080` through `AOA-T-0083` as the fourth migration pilot.

The fourth pilot migration is now landed: those four bundles live under
`techniques/recovery/diagnosis-repair/`, the `recovery/` route card and root
legacy receipt are in place, authored links were repaired, generated surfaces
were rebuilt, and frontmatter stayed unchanged.

The landed `diagnosis-repair` pilot review is now landed as `pilot-validated`
and chooses `instruction-surface` for the next direct-read migration review.

The `instruction-surface` direct-read review is now landed and accepts exactly
`AOA-T-0012`, `AOA-T-0013`, `AOA-T-0024`, `AOA-T-0027`, `AOA-T-0029`,
`AOA-T-0030`, and `AOA-T-0035` as the fifth migration pilot.

The fifth pilot migration is now landed: those seven bundles live under
`techniques/instruction/instruction-surface/`, the `instruction/` route card
and root legacy receipt are in place, authored links were repaired, generated
surfaces were rebuilt, and frontmatter stayed unchanged.

The landed `instruction-surface` pilot review is now landed as
`pilot-validated` and chooses `kag-source-lift` for the next direct-read
migration review.

The `kag-source-lift` direct-read review is now landed and accepts exactly
`AOA-T-0018`, `AOA-T-0019`, `AOA-T-0020`, `AOA-T-0021`, `AOA-T-0022`,
`AOA-T-0046`, `AOA-T-0047`, and `AOA-T-0048` as the sixth migration pilot.

The sixth pilot migration is now landed: those eight bundles live under
`techniques/knowledge-lift/kag-source-lift/`, the `knowledge-lift/` route card
and root legacy receipt are in place, authored links were repaired, generated
surfaces were rebuilt, and frontmatter stayed unchanged.

The landed `kag-source-lift` pilot review is now landed as `pilot-validated`
and chooses `docs-boundary` for the next direct-read migration review.

The `docs-boundary` direct-read review is now landed and accepts exactly
`AOA-T-0002`, `AOA-T-0009`, `AOA-T-0034`, and `AOA-T-0033` as the seventh
migration pilot.

The seventh pilot migration is now landed: those four bundles live under
`techniques/instruction/docs-boundary/`, the `instruction/` route card and
root legacy receipt are in place, authored links were repaired, generated
surfaces were rebuilt, and frontmatter stayed unchanged.

The landed `docs-boundary` pilot review is now landed as `pilot-validated` and
chooses `capability-registry` for the next direct-read migration review.

The next move is a direct-read migration review for `capability-registry`
before any eighth shelf moves.
