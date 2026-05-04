# Technique Tree Contract

This guide defines the repository tree shape for published technique bundles.

Use it when the question is where a technique should live in the root
`techniques/` directory, how a future path migration should be staged, or how
the corpus can scale beyond the current broad domain folders without becoming a
flat list.

Use [Technique Atom Contract](TECHNIQUE_ATOM_CONTRACT.md) first when the
question is whether a candidate is one technique. Use
[Technique Topology Contract](TECHNIQUE_TOPOLOGY_CONTRACT.md) next when the
question is how that technique is classified by `domain`, `kind`, family, and
other selector axes.

## Purpose

The technique corpus needs a root tree that is pleasant for humans to browse,
stable for agents to route through, and large enough for `1000+` techniques.

The current `techniques/<domain>/<slug>/` layout is valid for the present
corpus, but it puts too much future pressure on broad folders such as
`agent-workflows` and `docs`. Those folders are useful review lanes, not enough
architecture by themselves.

The long-term tree should make the library feel like a canon with clear
districts, shelves, and leaves. It should not become a mechanical dump of every
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

## Trunk Draft

The first tree projection should test a compact trunk set before any file
migration.

| trunk | intended surface | likely current shelves |
|---|---|---|
| `execution` | doing bounded work, planning, runtime posture, and task flow | `agent-workflows-core`, `intent-chain`, `ready-work-graphs`, `runtime-truth-lifecycle` |
| `instruction` | instruction, documentation, capability contracts, and owner-facing surfaces | `docs-boundary`, `instruction-surface`, `capability-registry`, `capability-boundary`, `skill-discovery` |
| `proof` | validation, review evidence, summary integrity, and owner-truth checks | `evaluation-chain`, `published-summary`, `skill-support`, `review-evidence`, `owner-truth-closeout` |
| `continuity` | handoff, compaction, donor harvest, session carry, and return surfaces | `handoff-continuation`, `review-compaction`, `donor-harvest` |
| `governance` | approval, decision routing, automation boundaries, and promotion caution | `approval-evidence`, `decision-routing`, `automation-governance` |
| `knowledge-lift` | source lift and bounded derived knowledge projection | `kag-source-lift` |
| `ingest` | external media, document, and data intake moves | `media-ingest` |
| `recovery` | diagnosis, repair, degraded mode, and antifragile continuation | `diagnosis-repair`, `antifragility-recovery` |
| `history` | session and witness artifacts as reviewable history | `history-artifacts` |
| `tool-use` | bounded tool gateway or API caller surfaces | `tool-gateway` |

This draft is a review target, not migration authority. Trunks may be renamed,
merged, or split after a projection over the full corpus shows real pressure.

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

## Migration Rules

A future tree migration should happen in projection-first waves:

1. generate a full proposed `tree_path` projection without moving files
2. review trunk and shelf assignments against authored bundle meaning
3. choose one pilot trunk or shelf
4. move only that bounded subtree
5. preserve a compact migration receipt in root `legacy/receipts/` when
   authored paths change
6. update bundle links, generated catalogs, capsules, docs, validators, and
   decision records in the same wave
7. repeat only after validation stays green and the resulting path feels easier
   to read

Moving paths is allowed only after the tree projection and review pack make the
move more legible than the current layout.

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

Before migration, the tree belongs in generated or review surfaces, not in
required frontmatter.

The first family shelf review remains the pressure test for whether a proposed
shelf is real enough to browse before any file movement.

The first build path should add a projection that maps:

- technique ID
- current source path
- proposed `trunk`
- proposed `shelf`
- proposed future path
- rationale cues from family, domain, kind, and direct bundle reading
- review status such as `candidate`, `hold`, or `accepted-for-pilot`

That projection should stay weaker than authored bundle meaning until a reviewed
migration wave lands.

The current projection surfaces are:

- [Technique Tree Projection](../reports/technique_tree_projection.md)
- [Technique Tree Projection JSON](../reports/technique_tree_projection.json)

They are generated review surfaces only. They do not make future paths current
links, do not add `tree_path` frontmatter, and do not authorize path movement.

## Stop Lines

- Do not move all technique bundles in one wave.
- Do not move active technique bundles through root `legacy/`; preserve the
  receipt there and move bundles directly between authored homes.
- Do not make `tree_path` required frontmatter before projection review proves
  value.
- Do not treat `domain` folders as the final tree or as junk drawers.
- Do not turn `kind` into the main directory tree.
- Do not use generated family assignments as automatic path-move authority.
- Do not copy the mechanics package shape blindly; techniques need leaf
  bundles, not active mechanic `parts/` packages.

## Next Honest Build Path

The current landed pilot review is
[Review-Compaction Direct-Read Migration Review](../mechanics/distillation/parts/technique-reform-ingress/reviews/review-compaction-direct-read-migration-review.md).
The review-compaction direct-read review accepted the first pilot shelf.

The first pilot migration moves `AOA-T-0051`, `AOA-T-0052`, and `AOA-T-0054`
into `techniques/continuity/review-compaction/` without changing `domain`,
`kind`, or `tree_path` frontmatter. The root receipt is
[`legacy/receipts/2026-05-04-review-compaction-tree-pilot.md`](../legacy/receipts/2026-05-04-review-compaction-tree-pilot.md).

The next reform slice should:

1. inspect the landed `review-compaction` pilot after validation
2. confirm whether the new path is easier to read than the old broad domain
   placement
3. choose one next shelf only through projection-first review
4. preserve a root legacy receipt and run the release check before considering
   any broader tree migration

This keeps the future tree beautiful enough to grow while preserving current
bundle truth.
