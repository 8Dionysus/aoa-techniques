# Technique Tree Contract

This guide defines the repository tree shape for published technique bundles.

Use it when the question is where a technique should live under `techniques/`,
how a future path change should be staged, or how the corpus can scale without
falling back into broad domain folders or a flat list.

Use [Technique Atom Contract](TECHNIQUE_ATOM_CONTRACT.md) first for candidate
boundedness. Use [Technique Topology Contract](TECHNIQUE_TOPOLOGY_CONTRACT.md)
for `domain`, `kind`, family, and other selector axes.

## Purpose

The corpus needs a root tree that is pleasant for humans to browse, stable for
agents to route through, and large enough for `1000+` techniques.

The current path shape is the landed corpus tree for all current bundles:
`techniques/<trunk>/<shelf>/<slug>/`. It replaced broad direct folders such as
`agent-workflows` and `docs` as path homes while preserving those values as
frontmatter review lanes.

## Tree Law

The authored directory tree is the placement spine for technique bundles.

It answers:

- Which large practice district does this technique belong to?
- Which stable shelf helps a reader find nearby techniques?
- Which single leaf bundle owns the executable move?

It does not answer every selector question. `domain`, `kind`, family,
capability, substrate, execution profile, risk posture, and relations stay
distinct from path placement.

## Tree Stack

The target shape is:

```text
techniques/<trunk>/<shelf>/<technique-slug>/
  TECHNIQUE.md
  checks/
  examples/
  notes/
```

| level | role | constraint |
|---|---|---|
| `trunk` | root practice district | few, durable, browsable, and not tied to one current frontmatter value |
| `shelf` | stable semantic neighborhood | usually aligned with a reviewed family, but not a quality score |
| `technique-slug` | one leaf bundle | one atomic executable move with its own authored truth |

The bundle remains the source of technique meaning. The path gives readers a
first location and generated surfaces a stable placement hint.

## Current Trunks

| trunk | intended surface | current shelf examples |
|---|---|---|
| `execution` | bounded work, planning, runtime posture, task flow | `agent-workflows-core`, `intent-chain`, `ready-work-graphs` |
| `instruction` | instruction, docs, capability contracts | `docs-boundary`, `instruction-surface`, `skill-discovery` |
| `proof` | validation, review evidence, summary integrity | `evaluation-chain`, `published-summary`, `review-evidence` |
| `continuity` | handoff, compaction, donor harvest, return surfaces | `handoff-continuation`, `review-compaction`, `donor-harvest` |
| `governance` | approval, decision routing, automation boundaries | `approval-evidence`, `decision-routing`, `promotion-boundary` |
| `knowledge-lift` | source lift and bounded derived knowledge projection | `kag-source-lift` |
| `ingest` | external media, document, and data intake moves | `media-ingest` |
| `recovery` | diagnosis, repair, degraded mode, antifragile continuation | `diagnosis-repair`, `antifragility-recovery` |
| `history` | session and witness artifacts as reviewable history | `history-artifacts` |
| `tool-use` | bounded tool gateway or API caller surfaces | `tool-gateway` |

These trunks are current path truth, not full classification truth.

## Tree Versus Facets

The tree and topology facets work together:

| Surface | Answers |
|---|---|
| `tree_path` | where the bundle lives |
| `domain` | current owner and review lane |
| `kind` | atomic move shape |
| `family` | semantic shelf |
| `capability_class` | what the agent is doing |
| `substrate` | what object or medium is acted on |
| `execution_profile` | what size or orchestration level can execute it |
| `risk_posture` | what operational caution should route around it |
| `relations` | direct composition, sequence, conflict, or alternative hints |

Do not collapse these into one tree. Do not use the tree as hidden frontmatter.

## Path Change Rules

Future path changes happen in projection-first waves:

1. refresh the full tree projection without moving files
2. review assignments against authored bundle meaning
3. choose one bounded trunk, shelf, split, merge, or hold
4. move only that bounded subtree after direct reading accepts the change
5. preserve a compact migration receipt in root `legacy/receipts/`
6. update links, generated catalogs, capsules, docs, validators, and decisions
7. stop after validation proves the new path is easier to read

## Leaf Bundle Rules

Every leaf bundle keeps the familiar technique shape:

- `TECHNIQUE.md` owns the move
- `checks/` holds minimal verification aids
- `examples/` holds portable examples
- `notes/` holds provenance, evidence, readiness, adverse-effect, or adaptation
  notes

Tree migration must not mix several techniques into one folder, hide broad
workflow chains inside one leaf, or turn shelves into mechanic-style `parts/`
directories.

## Generated Projection Path

The generated tree projection is an audit lens, not required frontmatter. It is
useful for drift detection, hold-count visibility, and future bounded path
reviews.

The current projection surfaces are:

- [Technique Tree Projection](../mechanics/distillation/parts/technique-reform-ingress/reports/technique_tree_projection.md)
- [Technique Tree Projection JSON](../mechanics/distillation/parts/technique-reform-ingress/reports/technique_tree_projection.json)

They do not add `tree_path` frontmatter and do not authorize path movement by
themselves.

## Stop Lines

- Do not move broad technique surfaces in one wave.
- Do not move active technique bundles through root `legacy/`; preserve only
  receipts there.
- Do not require `tree_path` frontmatter before projection review proves value.
- Do not treat `domain`, `kind`, generated family assignments, or mechanic
  package shape as automatic path authority.

## Current Closeout

The whole-tree migration pass is closed for the current corpus.

The closeout review is [Whole-Tree Closeout Review](../mechanics/distillation/parts/technique-reform-ingress/reviews/whole-tree-closeout-review.md).
It validates the current tree as `107` bundles across `10` trunks and `28`
shelves, with current paths matching projected paths and no remaining projection
holds.

Historical movement evidence now lives in:

- [Final Tree Migration Ledger](../mechanics/distillation/parts/technique-reform-ingress/reviews/final-tree-migration-ledger.md)
- [Root Legacy Index](../legacy/INDEX.md)
- [legacy/receipts/](../legacy/receipts/)
- [Distillation tree migration breadcrumbs](../mechanics/distillation/legacy/raw/ROOT_ROADMAP_TREE_MIGRATION_BREADCRUMBS_2026-05-14.md)

The authored tree is current path architecture. It does not add `tree_path`,
`family`, capability, substrate, execution-profile, or risk frontmatter; it does
not change `domain`, `kind`, ID, status, evidence, relations, or promotion
posture; and it does not make generated projection stronger than bundle meaning.

## Next Honest Build Path

Future path changes should start from the current tree, refresh the projection,
read affected bundles directly, and preserve compact receipts under
`legacy/receipts/`.

The next reform program should start with a corpus-wide bundle anatomy and
small-agent usability audit before changing individual leaves.

This keeps the current tree clear enough to grow while preserving bundle truth.
