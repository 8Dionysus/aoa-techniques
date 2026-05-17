# Roadmap

This roadmap tracks the current direction of `aoa-techniques` as a public
practice canon and standalone technique library.

Use it when the question is not "which technique should I open?", but "which
repo-level direction should shape the next change?"

## Authority

Root [ROADMAP](ROADMAP.md) owns:

- repo-level direction
- technique-canon horizons
- corpus-scale pressure
- standalone portability pressure
- root entry and source-of-truth pressure
- mechanics-to-canon interface pressure
- concrete future triggers that belong to this repository

It does not own technique status by itself, generated manifest truth, mechanic
local roadmaps, checked mechanic landings, release history, quest state, donor
raw evidence, proof verdicts, or sibling-repository implementation direction.

Use the stronger surface when the change is narrower:

- technique meaning: bundle `TECHNIQUE.md` files under [techniques](techniques/)
- atomicity and portability: [TECHNIQUE_ATOM_CONTRACT](docs/TECHNIQUE_ATOM_CONTRACT.md)
- classification topology: [TECHNIQUE_TOPOLOGY_CONTRACT](docs/TECHNIQUE_TOPOLOGY_CONTRACT.md)
- corpus path architecture: [TECHNIQUE_TREE_CONTRACT](docs/TECHNIQUE_TREE_CONTRACT.md)
- root and docs placement: [ROOT_SURFACE_LAW](docs/ROOT_SURFACE_LAW.md)
- promotion readiness and evidence lanes: [Audit parts](mechanics/audit/parts/)
- donor intake and candidate extraction: [Distillation parts](mechanics/distillation/parts/)
- checked mechanic landings: `mechanics/<slug>/LANDING_LOG.md`
- mechanic-local future pressure: `mechanics/<slug>/ROADMAP.md`
- durable obligations: [QUESTBOOK](QUESTBOOK.md) and [quests](quests/)
- released history: [CHANGELOG](CHANGELOG.md)

Historical tree migration, closure audit, scout, and bundle-reform detail lives
in the owner surfaces that produced or reviewed it:

- [Distillation roadmap](mechanics/distillation/ROADMAP.md)
- [final tree migration ledger](mechanics/distillation/parts/technique-reform-ingress/reviews/final-tree-migration-ledger.md)
- [whole tree closeout review](mechanics/distillation/parts/technique-reform-ingress/reviews/whole-tree-closeout-review.md)
- [bundle anatomy final closeout ledger](mechanics/distillation/parts/technique-reform-ingress/reviews/bundle-anatomy-final-closeout-ledger.md)
- [root roadmap tree migration breadcrumbs receipt](mechanics/distillation/legacy/raw/ROOT_ROADMAP_TREE_MIGRATION_BREADCRUMBS_2026-05-14.md)
- [root closure audit roadmap receipt](mechanics/audit/legacy/raw/ROOT_CLOSURE_AUDIT_ROADMAP_2026-05-03.md)

Treat those as evidence and mechanic-local direction, not as live root roadmap
text.

## Update Rule

Update this roadmap when a change moves repo-level direction, corpus topology,
root source-of-truth posture, standalone portability, mechanics-to-canon
interface, or a concrete future trigger for this repository.

Do not update this roadmap for a local mechanic landing, generated refresh,
bundle-local evidence note, quest lifecycle move, release note, or donor ledger
entry unless it changes one of those repo-level directions. Route those changes
to their owning surfaces.

Before closeout, ask: did this change move the practice canon's direction, or
did it only land a local surface?

## Current Direction

`aoa-techniques` is moving from closure-audit hardening into canon-scale
architecture.

The current direction is:

- keep root entry surfaces compact, with [README](README.md) as a front door rather
  than a warehouse for every route
- keep [CHARTER](CHARTER.md), [DESIGN](DESIGN.md),
  [DESIGN.AGENTS](DESIGN.AGENTS.md), [START_HERE](docs/START_HERE.md),
  [TECHNIQUE_ATOM_CONTRACT](docs/TECHNIQUE_ATOM_CONTRACT.md),
  [TECHNIQUE_TOPOLOGY_CONTRACT](docs/TECHNIQUE_TOPOLOGY_CONTRACT.md),
  [TECHNIQUE_TREE_CONTRACT](docs/TECHNIQUE_TREE_CONTRACT.md), and
  [ROOT_SURFACE_LAW](docs/ROOT_SURFACE_LAW.md) aligned as the route and
  contract stack
- keep the repository usable as a standalone public technique library, not only
  as an OS Abyss organ
- keep each technique as one atomic executable move suitable for templating,
  capsule projection, validation, and small-agent execution after orchestration
  supplies context
- grow toward `1000+` techniques through faceted topology rather than overloaded
  root categories
- keep mechanics active as movement, provenance, review, and candidate routes
  around canon rather than as substitutes for technique bundles
- keep generated catalogs, capsules, source-lift readers, and manifests
  subordinate to authored sources
- keep agent-facing route cards and generated agent mesh mirrors checkable
  without letting them replace public docs or technique meaning

## Current Checked Contour

Current public corpus after the latest validation:

| Measure | Current |
|---|---:|
| authored technique bundles | `107` |
| canonical bundles | `98` |
| promoted bundles | `9` |
| deprecated bundles | `0` |
| active trunks | `10` |
| active shelves | `28` |

Current anchors:

| Anchor | Surface |
|---|---|
| Repository authority | [CHARTER](CHARTER.md) |
| Public front door | [README](README.md) |
| Shortest route | [START_HERE](docs/START_HERE.md) |
| Root placement law | [ROOT_SURFACE_LAW](docs/ROOT_SURFACE_LAW.md) |
| Technique atom contract | [TECHNIQUE_ATOM_CONTRACT](docs/TECHNIQUE_ATOM_CONTRACT.md) |
| Technique topology contract | [TECHNIQUE_TOPOLOGY_CONTRACT](docs/TECHNIQUE_TOPOLOGY_CONTRACT.md) |
| Technique tree contract | [TECHNIQUE_TREE_CONTRACT](docs/TECHNIQUE_TREE_CONTRACT.md) |
| Corpus map | [TECHNIQUE_INDEX](TECHNIQUE_INDEX.md), [technique catalog](generated/technique_catalog.min.json) |
| Small runtime cards | [TECHNIQUE_CAPSULES](docs/readers/runtime/TECHNIQUE_CAPSULES.md), [technique capsules](generated/technique_capsules.min.json) |
| Mechanics atlas | [mechanics README](mechanics/README.md), [mechanics AGENTS](mechanics/AGENTS.md), mechanic package `README.md` files |
| Audit and evidence posture | [Audit parts](mechanics/audit/parts/) |
| Donor and candidate extraction | [Distillation parts](mechanics/distillation/parts/) |
| Durable obligations | [QUESTBOOK](QUESTBOOK.md), [quests](quests/) |
| Release history and release path | [CHANGELOG](CHANGELOG.md), [RELEASING](docs/RELEASING.md) |

[ROADMAP](ROADMAP.md) keeps current direction and future contour. Mechanic
`LANDING_LOG.md` surfaces keep checked mechanic landings.
[CHANGELOG](CHANGELOG.md) keeps released history. [QUESTBOOK](QUESTBOOK.md)
keeps durable obligations.

## Horizon: Root Clarity

| Field | Direction |
|---|---|
| Current posture | The root file set is small and allowed, but old root prose has repeatedly tried to become a route maze. |
| Next honest move | Keep root Markdown short and role-bound: entry, authority, direction, obligation, release, contribution, agent route, and one example. Put detailed inventories in [Documentation Map](docs/README.md), [Repo Doc Surfaces](docs/readers/repo/REPO_DOC_SURFACES.md), generated manifests, or owner-local mechanics. |
| Guardrail | Root files should not become warehouses for audit history, generated detail, donor ledgers, mechanic-local runbooks, or semantic/shadow review packets. |

## Horizon: Technique Atom

| Field | Direction |
|---|---|
| Current posture | The technique atom contract names one atomic executable move as the unit of canon. |
| Next honest move | Pressure every new candidate through atom checks before drafting a bundle, especially mechanics candidates and donor imports. |
| Guardrail | Do not patch broad candidates with more prose; split, narrow, keep in mechanics, or route to a stronger owner. |

## Horizon: Corpus Topology

| Field | Direction |
|---|---|
| Current posture | `domain` and `kind` are authoritative frontmatter; family, capability, substrate, execution profile, risk posture, and richer relations are explicit design axes. |
| Next honest move | Enter selector and relation work through [Technique Reform Ingress](mechanics/distillation/parts/technique-reform-ingress/README.md). Keep [technique_topology_axes.yaml](mechanics/distillation/parts/technique-reform-ingress/config/technique_topology_axes.yaml) and [technique_topology_scout.md](mechanics/distillation/parts/technique-reform-ingress/reports/technique_topology_scout.md) as scout evidence, and strengthen relations only when bundle inputs and contracts justify an existing relation type. |
| Guardrail | Do not turn `agent-workflows`, `docs`, or tags into junk drawers for missing topology. |

## Horizon: Corpus Tree

| Field | Direction |
|---|---|
| Current posture | The full tree migration is closed: `107` bundles now sit under active `techniques/<trunk>/<shelf>/<slug>/` paths across `10` active trunks and `28` shelves, with generated path parity and root legacy receipts validated by the Distillation closeout surfaces. |
| Next honest move | Keep the landed tree stable while reform waves work through selector, relation, portability, execution-profile, and bundle-anatomy evidence. Use the Distillation ingress packet before any new broad path, schema, or classification movement. |
| Guardrail | Do not put shelf-by-shelf migration breadcrumbs, pilot queues, or parity ledgers back into root roadmap. Do not add `tree_path` frontmatter or move paths without a fresh owner-local review surface. |

## Horizon: Small-Agent Usability

| Field | Direction |
|---|---|
| Current posture | Capsules and generated catalogs provide compact lookup surfaces; template-modernization and bundle-anatomy closeouts have already moved broad usability pressure into targeted reform surfaces. |
| Next honest move | Move from template-shape review to concrete content-level technique reform only where direct bundle reading finds a real source, selector, relation, portability, owner-boundary, or execution-shape problem. |
| Guardrail | Small-agent usability does not mean autonomous selection; routing and composition may belong to larger agents or neighboring layers. |

## Horizon: Mechanics To Canon

| Field | Direction |
|---|---|
| Current posture | Mechanics packages keep active routes, parts, provenance, landing logs, package roadmaps, and legacy scaffolds; the root mechanics surface stays an atlas and local law route rather than a second roadmap authority. |
| Next honest move | Use mechanics to preserve lineage and candidate pressure while extracting only one atomic practice at a time into [techniques](techniques/), and keep package roadmaps strong enough for small-agent route choice without importing AoA center authority. |
| Guardrail | Mechanics can prepare canon. They do not replace canon or silently change status. |

## Horizon: Evidence And Promotion

| Field | Direction |
|---|---|
| Current posture | Audit parts carry promotion readiness, evidence sprinting, searched-lane memory, and canonical retro-audit work. |
| Next honest move | Keep external-evidence work routed through the Audit and Distillation parts, then update bundle-local notes before shared queues. |
| Guardrail | Root roadmap should name evidence pressure only at the horizon level; ledgers and queue details belong in Audit. |

## Horizon: Standalone Portability

| Field | Direction |
|---|---|
| Current posture | The repository explicitly serves both external builders and AoA sibling repos. |
| Next honest move | Keep AoA references as provenance and integration context while making the portable practice understandable without OS Abyss. |
| Guardrail | Do not let AoA organ fidelity become a hidden dependency for public reuse. |

## Horizon: Generated Companions

| Field | Direction |
|---|---|
| Current posture | Generated catalogs, capsules, source-lift readers, repo-doc surfaces, and agent mesh mirrors give machines compact routes over authored sources. |
| Next honest move | Keep generated parity validator-backed whenever source docs, templates, route maps, mesh config, or surface specs change. |
| Guardrail | Generated outputs route and compress; they do not author technique meaning, root law, agent law, or status. |

## When The Time Comes

Use this block for likely repo-level work that is not useful to land until its
trigger is real.

- Promote `family` from scout-only to optional reviewed frontmatter only after
  examples and tie-break rules stay stable across multiple technique waves.
- Add generated projections for `capability_class`, `substrate`,
  `execution_profile`, and `risk_posture` only after mechanics candidates prove
  the axes help selection without false precision.
- Use the technique reform ingress packet before any broad classification
  change so the first reform pass stays bounded and evidence-linked.
- Add richer typed relation guidance only when direct relations are repeatedly
  useful for composition, conflict, sequence, or prerequisite routing.
- Keep [examples](examples/README.md) as the home for public worked examples;
  move any technique-local tutorial back to the owning bundle before root grows
  another example article.
- Add a machine-facing root route capsule only after the human route stabilizes
  enough that a generated companion would reduce real reader load.

An item belongs here only when its trigger is concrete and repo-level. If the
future pressure is mechanic-local, use `mechanics/<slug>/ROADMAP.md`. If it is
a durable obligation, use [QUESTBOOK](QUESTBOOK.md) and [quests](quests/).

## Standing Direction

Across all horizons:

- keep one technique small
- keep the corpus navigable at scale
- keep portable practice stronger than local lore
- keep mechanics, generated surfaces, and sibling consumers subordinate to
  authored technique truth
- make every route clearer for both humans and small agents
