# Technique Tree Contract

This guide defines the repository tree shape for published technique bundles.

Use it when the question is where a technique should live in the root
`techniques/` directory, how a future path change should be staged, or how the
corpus can keep scaling without falling back into broad domain folders or a
flat list.

Use [Technique Atom Contract](TECHNIQUE_ATOM_CONTRACT.md) first when the
question is whether a candidate is one technique. Use
[Technique Topology Contract](TECHNIQUE_TOPOLOGY_CONTRACT.md) next when the
question is how that technique is classified by `domain`, `kind`, family, and
other selector axes.

## Purpose

The technique corpus needs a root tree that is pleasant for humans to browse,
stable for agents to route through, and large enough for `1000+` techniques.

The current `techniques/<trunk>/<shelf>/<slug>/` layout is the landed corpus
tree for all current bundles. It replaced broad direct folders such as
`agent-workflows` and `docs` as authored path homes while preserving those
values as frontmatter review lanes.

The tree should make the library feel like a canon with clear districts,
shelves, and leaves. It should not become a mechanical dump of every
frontmatter axis.

## Tree Law

The authored directory tree is the placement spine for technique bundles.

It must answer:

- Which large practice district does this technique belong to?
- Which stable shelf helps a reader find nearby techniques?
- Which single leaf bundle owns the executable move?

It must not pretend to answer every selector question. A path is not a full
classification record. `domain`, `kind`, family, capability, substrate,
execution profile, risk posture, and relations still carry distinct meanings.

## Tree Stack

The target path shape is:

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

The bundle remains the source of technique meaning. The tree path gives the
reader a first location and gives generated surfaces a stable placement hint.

## Current Trunks

The current tree uses a compact trunk set landed through reviewed migration
waves. Future trunks may still be renamed, merged, or split, but only after
projection, direct reading, receipts, and validation show the current shape has
become less honest than the alternative.

| trunk | intended surface | likely current shelves |
|---|---|---|
| `execution` | doing bounded work, planning, runtime posture, and task flow | `agent-workflows-core`, `intent-chain`, `ready-work-graphs`, `runtime-truth-lifecycle` |
| `instruction` | instruction, documentation, capability contracts, and owner-facing surfaces | `docs-boundary`, `instruction-surface`, `capability-registry`, `capability-boundary`, `skill-discovery` |
| `proof` | validation, review evidence, summary integrity, and owner-truth checks | `evaluation-chain`, `published-summary`, `skill-support`, `review-evidence`, `owner-truth-closeout` |
| `continuity` | handoff, compaction, donor harvest, session carry, and return surfaces | `handoff-continuation`, `review-compaction`, `donor-harvest` |
| `governance` | approval, decision routing, automation boundaries, and promotion caution | `approval-evidence`, `decision-routing`, `automation-readiness`, `promotion-boundary`, `practice-adoption-lifecycle` |
| `knowledge-lift` | source lift and bounded derived knowledge projection | `kag-source-lift` |
| `ingest` | external media, document, and data intake moves | `media-ingest` |
| `recovery` | diagnosis, repair, degraded mode, and antifragile continuation | `diagnosis-repair`, `antifragility-recovery` |
| `history` | session and witness artifacts as reviewable history | `history-artifacts` |
| `tool-use` | bounded tool gateway or API caller surfaces | `tool-gateway` |

These trunks are current path truth, not full classification truth. They are
still weaker than authored bundle meaning and do not replace `domain`, `kind`,
family, capability, substrate, execution profile, risk posture, or relation
axes.

## Tree Versus Facets

The tree and the topology facets work together.

- `tree_path` answers where the bundle lives.
- `domain` answers the current owner and review lane.
- `kind` answers the atomic move shape.
- `family` answers the semantic shelf and may guide the second path segment.
- `capability_class` answers what the agent is doing.
- `substrate` answers what object or medium the technique acts on.
- `execution_profile` answers what size or orchestration level can execute it.
- `risk_posture` answers what operational caution should route around it.
- `relations` answer direct composition, sequence, conflict, or alternative
  hints.

Do not collapse these into one tree. Do not use the tree as a hidden
replacement for frontmatter.

## Path Change Rules

Any future tree path change should happen in projection-first waves:

1. generate or refresh the full tree projection without moving files
2. review trunk and shelf assignments against authored bundle meaning
3. choose one bounded trunk, shelf, split, merge, or hold
4. move only that bounded subtree if direct reading accepts the change
5. preserve a compact migration receipt in root `legacy/receipts/` when
   authored paths change
6. update bundle links, generated catalogs, capsules, docs, validators, and
   decision records in the same wave
7. repeat only after validation stays green and the resulting path feels easier
   to read

Moving paths is allowed only after the tree projection and review packet make
the move more legible than the current layout.

## Leaf Bundle Rules

Every leaf bundle should keep the familiar technique shape:

- `TECHNIQUE.md` owns the move
- `checks/` holds minimal verification aids
- `examples/` holds portable examples
- `notes/` holds provenance, evidence, readiness, adverse-effect, or adaptation
  notes

Tree migration should not mix several techniques into one folder, hide broad
workflow chains inside one leaf, or turn shelves into mechanic-style `parts/`
directories.

## Generated Projection Path

The generated tree projection remains an audit lens, not required frontmatter.
After the first whole-tree migration pass, its strongest current use is to
detect drift between authored paths and projected paths, keep hold counts
visible, and guide future bounded path-change reviews.

The family shelf review remains the original pressure test that made the first
tree pass possible. It does not become active family frontmatter by being
useful for tree placement.

The projection maps:

- technique ID
- current source path
- proposed `trunk`
- proposed `shelf`
- proposed future path, which should match current path after a landed
  migration wave
- rationale cues from family, domain, kind, and direct bundle reading
- review status such as `candidate`, `hold`, or `accepted-for-pilot`

That projection stays weaker than authored bundle meaning even after reviewed
migration waves land.

The current projection surfaces are:

- [Technique Tree Projection](../mechanics/distillation/parts/technique-reform-ingress/reports/technique_tree_projection.md)
- [Technique Tree Projection JSON](../mechanics/distillation/parts/technique-reform-ingress/reports/technique_tree_projection.json)

They are generated review surfaces only. They do not add `tree_path`
frontmatter and do not authorize path movement by themselves.

## Stop Lines

- Do not move broad technique surfaces in one wave.
- Do not move active technique bundles through root `legacy/`; preserve the
  receipt there and move bundles directly between authored homes.
- Do not make `tree_path` required frontmatter before projection review proves
  value.
- Do not treat `domain` frontmatter lanes as path authority or as junk drawers.
- Do not turn `kind` into the main directory tree.
- Do not use generated family assignments as automatic path-move authority.
- Do not copy the mechanics package shape blindly; techniques need leaf
  bundles, not active mechanic `parts/` packages.

## Current Closeout

The whole-tree migration pass is closed for the current corpus.

The closeout review is [Whole-Tree Closeout Review](../mechanics/distillation/parts/technique-reform-ingress/reviews/whole-tree-closeout-review.md).
It validates the current tree as `107` bundles across `10` trunks and `28`
shelves, with `107/107` current paths matching projected paths, `28/28`
root legacy receipt coverage, and no remaining `split-review-needed`,
`singleton-hold`, or `unassigned-hold` projection rows.

The detailed wave-by-wave ledger is no longer current route law. Use these
owner surfaces when historical movement evidence matters:

- [Final Tree Migration Ledger](../mechanics/distillation/parts/technique-reform-ingress/reviews/final-tree-migration-ledger.md)
- [Root Legacy Index](../legacy/INDEX.md)
- [legacy/receipts/](../legacy/receipts/)
- [Distillation tree migration breadcrumbs](../mechanics/distillation/legacy/raw/ROOT_ROADMAP_TREE_MIGRATION_BREADCRUMBS_2026-05-14.md)

This closeout makes the authored tree the current path architecture. It does
not add `tree_path`, `family`, capability, substrate, execution-profile, or
risk frontmatter; it does not change `domain`, `kind`, ID, status, evidence,
relations, or promotion posture; and it does not make the generated projection
stronger than authored bundle meaning.

## Next Honest Build Path

The next honest path is not another migration wave over already-landed shelves.
Future path changes should start from the current tree, refresh the projection,
read the affected bundles directly, and preserve only compact receipts under
`legacy/receipts/`.

The next reform program should start with a corpus-wide bundle anatomy and
small-agent usability audit before changing individual leaves.

This keeps the current tree clear enough to grow while preserving bundle truth.
