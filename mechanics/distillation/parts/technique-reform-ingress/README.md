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

Use the first tree projection review pack as the close of the projection pass.
The generated projection covers all `107` bundles, keeps future paths
non-authoritative, and selects `review-compaction` for direct-read pilot review.
The next move is to read the three `review-compaction` bundles and decide
whether that one shelf should become the first migration pilot.
