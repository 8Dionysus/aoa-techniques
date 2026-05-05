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

The first pilot migration moves `AOA-T-0051`, `AOA-T-0052`, and `AOA-T-0054`
into `techniques/continuity/review-compaction/` without changing `domain`,
`kind`, or `tree_path` frontmatter. The root receipt is
[`legacy/receipts/2026-05-04-review-compaction-tree-pilot.md`](../legacy/receipts/2026-05-04-review-compaction-tree-pilot.md).
The current landed pilot review is
[Landed Review-Compaction Pilot Review](../mechanics/distillation/parts/technique-reform-ingress/reviews/landed-review-compaction-pilot-review.md).

The second migration review is
[Handoff-Continuation Direct-Read Migration Review](../mechanics/distillation/parts/technique-reform-ingress/reviews/handoff-continuation-direct-read-migration-review.md).
It accepted `handoff-continuation` as the second bounded migration pilot after
directly reading `AOA-T-0056` through `AOA-T-0062`.

The second pilot migration moves `AOA-T-0056` through `AOA-T-0062` into
`techniques/continuity/handoff-continuation/` without changing `domain`,
`kind`, or `tree_path` frontmatter. The root receipt is
[`legacy/receipts/2026-05-04-handoff-continuation-tree-pilot.md`](../legacy/receipts/2026-05-04-handoff-continuation-tree-pilot.md).

The landed second pilot review is
[Landed Handoff-Continuation Pilot Review](../mechanics/distillation/parts/technique-reform-ingress/reviews/landed-handoff-continuation-pilot-review.md).
It validates the `handoff-continuation` migration and chooses `media-ingest`
for the next direct-read migration review.

The third migration review is
[Media-Ingest Direct-Read Migration Review](../mechanics/distillation/parts/technique-reform-ingress/reviews/media-ingest-direct-read-migration-review.md).
It accepts `media-ingest` as the first non-continuity migration pilot after
directly reading `AOA-T-0070` through `AOA-T-0074`.

The third pilot migration moves `AOA-T-0070` through `AOA-T-0074` into
`techniques/ingest/media-ingest/` without changing `domain`, `kind`, or
`tree_path` frontmatter. The root receipt is
[`legacy/receipts/2026-05-04-media-ingest-tree-pilot.md`](../legacy/receipts/2026-05-04-media-ingest-tree-pilot.md).

The landed third pilot review is
[Landed Media-Ingest Pilot Review](../mechanics/distillation/parts/technique-reform-ingress/reviews/landed-media-ingest-pilot-review.md).
It validates the `media-ingest` migration as the first successful
non-continuity trunk test and chooses `diagnosis-repair` for the next
direct-read migration review.

The fourth migration review is
[Diagnosis-Repair Direct-Read Migration Review](../mechanics/distillation/parts/technique-reform-ingress/reviews/diagnosis-repair-direct-read-migration-review.md).
It accepts `diagnosis-repair` as the fourth migration pilot after directly
reading `AOA-T-0080` through `AOA-T-0083`.

The fourth pilot migration moves `AOA-T-0080` through `AOA-T-0083` into
`techniques/recovery/diagnosis-repair/` without changing `domain`, `kind`, or
`tree_path` frontmatter. The root receipt is
[`legacy/receipts/2026-05-04-diagnosis-repair-tree-pilot.md`](../legacy/receipts/2026-05-04-diagnosis-repair-tree-pilot.md).

The landed fourth pilot review is
[Landed Diagnosis-Repair Pilot Review](../mechanics/distillation/parts/technique-reform-ingress/reviews/landed-diagnosis-repair-pilot-review.md).
It validates the `diagnosis-repair` migration as the first successful recovery
trunk test and chooses `instruction-surface` for the next direct-read review.

The fifth migration review is
[Instruction-Surface Direct-Read Migration Review](../mechanics/distillation/parts/technique-reform-ingress/reviews/instruction-surface-direct-read-migration-review.md).
It accepts `instruction-surface` as the fifth migration pilot after directly
reading `AOA-T-0012`, `AOA-T-0013`, `AOA-T-0024`, `AOA-T-0027`, `AOA-T-0029`,
`AOA-T-0030`, and `AOA-T-0035`.

The fifth pilot migration moves `AOA-T-0012`, `AOA-T-0013`, `AOA-T-0024`,
`AOA-T-0027`, `AOA-T-0029`, `AOA-T-0030`, and `AOA-T-0035` into
`techniques/instruction/instruction-surface/` without changing `domain`,
`kind`, or `tree_path` frontmatter. The root receipt is
[`legacy/receipts/2026-05-04-instruction-surface-tree-pilot.md`](../legacy/receipts/2026-05-04-instruction-surface-tree-pilot.md).

The landed fifth pilot review is
[Landed Instruction-Surface Pilot Review](../mechanics/distillation/parts/technique-reform-ingress/reviews/landed-instruction-surface-pilot-review.md).
It validates the `instruction-surface` migration as the first successful
instruction trunk test and chooses `kag-source-lift` for the next direct-read
migration review.

The sixth migration review is
[Kag-Source-Lift Direct-Read Migration Review](../mechanics/distillation/parts/technique-reform-ingress/reviews/kag-source-lift-direct-read-migration-review.md).
It accepts `kag-source-lift` as the first `knowledge-lift` migration pilot after
directly reading `AOA-T-0018`, `AOA-T-0019`, `AOA-T-0020`, `AOA-T-0021`,
`AOA-T-0022`, `AOA-T-0046`, `AOA-T-0047`, and `AOA-T-0048`.

The sixth pilot migration moves `AOA-T-0018`, `AOA-T-0019`, `AOA-T-0020`,
`AOA-T-0021`, `AOA-T-0022`, `AOA-T-0046`, `AOA-T-0047`, and `AOA-T-0048` into
`techniques/knowledge-lift/kag-source-lift/` without changing `domain`,
`kind`, or `tree_path` frontmatter. The root receipt is
[`legacy/receipts/2026-05-04-kag-source-lift-tree-pilot.md`](../legacy/receipts/2026-05-04-kag-source-lift-tree-pilot.md).

The landed sixth pilot review is
[Landed Kag-Source-Lift Pilot Review](../mechanics/distillation/parts/technique-reform-ingress/reviews/landed-kag-source-lift-pilot-review.md).
It validates `kag-source-lift` as the first successful `knowledge-lift` trunk
test and chooses `docs-boundary` for the next direct-read migration review.

The seventh migration review is
[Docs-Boundary Direct-Read Migration Review](../mechanics/distillation/parts/technique-reform-ingress/reviews/docs-boundary-direct-read-migration-review.md).
It accepts `docs-boundary` as the seventh migration pilot after directly
reading `AOA-T-0002`, `AOA-T-0009`, `AOA-T-0034`, and `AOA-T-0033`.

The seventh pilot migration moves `AOA-T-0002`, `AOA-T-0009`, `AOA-T-0034`,
and `AOA-T-0033` into `techniques/instruction/docs-boundary/` without changing
`domain`, `kind`, or `tree_path` frontmatter. The root receipt is
[`legacy/receipts/2026-05-04-docs-boundary-tree-pilot.md`](../legacy/receipts/2026-05-04-docs-boundary-tree-pilot.md).

The landed seventh pilot review is
[Landed Docs-Boundary Pilot Review](../mechanics/distillation/parts/technique-reform-ingress/reviews/landed-docs-boundary-pilot-review.md).
It validates the `docs-boundary` migration as the second successful
instruction trunk shelf and chooses `capability-registry` for the next
direct-read migration review.

The eighth migration review is
[Capability-Registry Direct-Read Migration Review](../mechanics/distillation/parts/technique-reform-ingress/reviews/capability-registry-direct-read-migration-review.md).
It accepts `capability-registry` as the eighth migration pilot after directly
reading `AOA-T-0025`, `AOA-T-0063`, and `AOA-T-0064`.

The eighth pilot migration moves `AOA-T-0025`, `AOA-T-0063`, and `AOA-T-0064`
into `techniques/instruction/capability-registry/` without changing `domain`,
`kind`, or `tree_path` frontmatter. The root receipt is
[`legacy/receipts/2026-05-04-capability-registry-tree-pilot.md`](../legacy/receipts/2026-05-04-capability-registry-tree-pilot.md).

The landed eighth pilot review is
[Landed Capability-Registry Pilot Review](../mechanics/distillation/parts/technique-reform-ingress/reviews/landed-capability-registry-pilot-review.md).
It validates `capability-registry` as the third successful instruction trunk
shelf and chooses `capability-boundary` for the next direct-read migration
review.

The ninth migration review is
[Capability-Boundary Direct-Read Migration Review](../mechanics/distillation/parts/technique-reform-ingress/reviews/capability-boundary-direct-read-migration-review.md).
It accepts `capability-boundary` as the ninth migration pilot after directly
reading `AOA-T-0040`, `AOA-T-0043`, and `AOA-T-0093`.

The ninth pilot migration moves exactly `AOA-T-0040`, `AOA-T-0043`, and
`AOA-T-0093` into `techniques/instruction/capability-boundary/` without
changing `domain`, `kind`, or `tree_path` frontmatter. The root receipt is
[`legacy/receipts/2026-05-04-capability-boundary-tree-pilot.md`](../legacy/receipts/2026-05-04-capability-boundary-tree-pilot.md).

The landed ninth pilot review is
[Landed Capability-Boundary Pilot Review](../mechanics/distillation/parts/technique-reform-ingress/reviews/landed-capability-boundary-pilot-review.md).
It validates `capability-boundary` as the fourth successful instruction trunk
shelf and chooses `skill-discovery` for the next direct-read migration review.

The tenth migration review is
[Skill-Discovery Direct-Read Migration Review](../mechanics/distillation/parts/technique-reform-ingress/reviews/skill-discovery-direct-read-migration-review.md).
It accepts `skill-discovery` as the tenth migration pilot after directly
reading `AOA-T-0041` and `AOA-T-0042`.

The tenth pilot migration moves exactly `AOA-T-0041` and `AOA-T-0042` into
`techniques/instruction/skill-discovery/` without changing `domain`, `kind`,
or `tree_path` frontmatter. The root receipt is
[`legacy/receipts/2026-05-05-skill-discovery-tree-pilot.md`](../legacy/receipts/2026-05-05-skill-discovery-tree-pilot.md).

The landed tenth pilot review is
[Landed Skill-Discovery Pilot Review](../mechanics/distillation/parts/technique-reform-ingress/reviews/landed-skill-discovery-pilot-review.md).
It validates `skill-discovery` as the fifth successful instruction trunk shelf
and chooses `skill-support` for the next direct-read migration review.

The eleventh migration review is
[Skill-Support Direct-Read Migration Review](../mechanics/distillation/parts/technique-reform-ingress/reviews/skill-support-direct-read-migration-review.md).
It accepts `skill-support` as the eleventh migration pilot after directly
reading `AOA-T-0016`, `AOA-T-0015`, and `AOA-T-0017`.

The eleventh pilot migration moves exactly `AOA-T-0016`, `AOA-T-0015`, and
`AOA-T-0017` into `techniques/proof/skill-support/` without changing
`domain`, `kind`, or `tree_path` frontmatter. The root receipt is
[`legacy/receipts/2026-05-05-skill-support-tree-pilot.md`](../legacy/receipts/2026-05-05-skill-support-tree-pilot.md).

The landed eleventh pilot review is
[Landed Skill-Support Pilot Review](../mechanics/distillation/parts/technique-reform-ingress/reviews/landed-skill-support-pilot-review.md).
It validates `skill-support` as the first successful proof trunk shelf and
chooses `evaluation-chain` for the next direct-read migration review.

The twelfth migration review is
[Evaluation-Chain Direct-Read Migration Review](../mechanics/distillation/parts/technique-reform-ingress/reviews/evaluation-chain-direct-read-migration-review.md).
It accepts `evaluation-chain` as the twelfth migration pilot after directly
reading `AOA-T-0003`, `AOA-T-0007`, and `AOA-T-0032`.

The twelfth pilot migration moves exactly `AOA-T-0003`, `AOA-T-0007`, and
`AOA-T-0032` into `techniques/proof/evaluation-chain/` without changing
`domain`, `kind`, or `tree_path` frontmatter. The root receipt is
[`legacy/receipts/2026-05-05-evaluation-chain-tree-pilot.md`](../legacy/receipts/2026-05-05-evaluation-chain-tree-pilot.md).

The landed twelfth pilot review is
[Landed Evaluation-Chain Pilot Review](../mechanics/distillation/parts/technique-reform-ingress/reviews/landed-evaluation-chain-pilot-review.md).
It validates `evaluation-chain` as the second successful proof trunk shelf,
completes the previous step to review the landed `evaluation-chain` pilot
before choosing any thirteenth shelf, and chooses `published-summary` for the
next direct-read migration review.

The thirteenth migration review is
[Published-Summary Direct-Read Migration Review](../mechanics/distillation/parts/technique-reform-ingress/reviews/published-summary-direct-read-migration-review.md).
It accepts `published-summary` as the thirteenth migration pilot after
directly reading `AOA-T-0006`, `AOA-T-0008`, `AOA-T-0010`, and `AOA-T-0011`.

The thirteenth pilot migration moves exactly `AOA-T-0006`, `AOA-T-0008`,
`AOA-T-0010`, and `AOA-T-0011` into
`techniques/proof/published-summary/` without changing `domain`, `kind`, or
`tree_path` frontmatter. The root receipt is
[`legacy/receipts/2026-05-05-published-summary-tree-pilot.md`](../legacy/receipts/2026-05-05-published-summary-tree-pilot.md).

The landed thirteenth pilot review is
[Landed Published-Summary Pilot Review](../mechanics/distillation/parts/technique-reform-ingress/reviews/landed-published-summary-pilot-review.md).
It validates `published-summary` as the third successful proof trunk shelf,
completes the previous step to review the landed `published-summary` pilot
before choosing any fourteenth shelf, and chooses `history-artifacts` for the
next direct-read migration review.

The fourteenth direct-read review is
[History-Artifacts Direct-Read Migration Review](../mechanics/distillation/parts/technique-reform-ingress/reviews/history-artifacts-direct-read-migration-review.md).
It accepts exactly `AOA-T-0044`, `AOA-T-0053`, `AOA-T-0026`, `AOA-T-0045`,
`AOA-T-0066`, and `AOA-T-0067` as the next bounded migration pilot while
keeping the review non-mutating, preserving flat `history/` paths for now, and
leaving memory doctrine, instruction authority, private transcript
publication, hidden capture policy, hosted viewer product doctrine, repo
analytics, retention policy, recall substrate, and proof authority outside the
shelf.

The fourteenth pilot migration moves exactly those six bundles into
`techniques/history/history-artifacts/` without changing `domain`, `kind`, or
`tree_path` frontmatter. The root receipt is
[`legacy/receipts/2026-05-05-history-artifacts-tree-pilot.md`](../legacy/receipts/2026-05-05-history-artifacts-tree-pilot.md).

The landed fourteenth pilot review is
[Landed History-Artifacts Pilot Review](../mechanics/distillation/parts/technique-reform-ingress/reviews/landed-history-artifacts-pilot-review.md).
It validates `history-artifacts` as the first successful history trunk shelf,
completes the previous step to review the landed `history-artifacts` pilot
before choosing any fifteenth shelf, and chooses
`recovery/antifragility-recovery` for the next direct-read migration review.

The fifteenth direct-read review is
[Antifragility-Recovery Direct-Read Migration Review](../mechanics/distillation/parts/technique-reform-ingress/reviews/antifragility-recovery-direct-read-migration-review.md).
It accepts exactly `AOA-T-0097`, `AOA-T-0099`, `AOA-T-0100`, and `AOA-T-0098`
as the next bounded migration pilot while keeping the review non-mutating,
preserving `AOA-T-0098` as `domain: validation-patterns` and
`kind: validation`, and leaving Agents-of-Abyss Antifragility doctrine,
incident response doctrine, runtime ownership, proof authority, rollback
policy, deployment lifecycle law, service catalog ownership, KAG authority,
stats meaning, playbook choreography, and generic resilience platform
authority outside the shelf.

The fifteenth pilot migration moves exactly those four bundles into
`techniques/recovery/antifragility-recovery/` without changing `domain`,
`kind`, or `tree_path` frontmatter. The root receipt is
[`legacy/receipts/2026-05-05-antifragility-recovery-tree-pilot.md`](../legacy/receipts/2026-05-05-antifragility-recovery-tree-pilot.md).

The landed fifteenth pilot review is
[Landed Antifragility-Recovery Pilot Review](../mechanics/distillation/parts/technique-reform-ingress/reviews/landed-antifragility-recovery-pilot-review.md).
It validates `antifragility-recovery` as the second successful recovery trunk
shelf, completes the previous step to review the landed
`antifragility-recovery` pilot before choosing any sixteenth shelf, preserves
`AOA-T-0098` as `domain: validation-patterns` and `kind: validation`, and
chooses `execution/ready-work-graphs` for the next direct-read migration
review.

The sixteenth direct-read review is
[Ready-Work-Graphs Direct-Read Migration Review](../mechanics/distillation/parts/technique-reform-ingress/reviews/ready-work-graphs-direct-read-migration-review.md).
It accepts exactly `AOA-T-0049`, `AOA-T-0050`, and `AOA-T-0055` as the next
bounded migration pilot while keeping the review non-mutating, preserving
`AOA-T-0055` as a readiness ladder rather than methodology or execution
workflow, and leaving project-management doctrine, scheduling, staffing,
dispatch policy, backlog governance, graph database doctrine, memory
substrate, hidden orchestration, proof of readiness, and execution validation
outside the shelf.

The next reform slice should run the sixteenth pilot migration into
`techniques/execution/ready-work-graphs/` before reviewing any seventeenth
shelf.

This keeps the future tree beautiful enough to grow while preserving current
bundle truth.
