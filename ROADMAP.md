# Roadmap

This roadmap tracks current direction for `aoa-techniques` as a public
practice canon and standalone technique library.

Use it when the question is "what repo-level direction should shape the next
change?", not "which technique should I open?"

## Authority

Root [ROADMAP](ROADMAP.md) owns repo-level direction, technique-canon horizons,
corpus-scale pressure, standalone portability pressure, root source-of-truth
pressure, mechanics-to-canon interface pressure, and concrete future triggers
that belong to this repository.

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
- durable obligations: [QUESTBOOK](QUESTBOOK.md) and [quests](quests/)
- released history: [CHANGELOG](CHANGELOG.md)

Historical migration, closure audit, scout, and bundle-reform detail stays with
the surfaces that produced or reviewed it:

- [Distillation roadmap](mechanics/distillation/ROADMAP.md)
- [final tree migration ledger](mechanics/distillation/parts/technique-reform-ingress/reviews/final-tree-migration-ledger.md)
- [whole tree closeout review](mechanics/distillation/parts/technique-reform-ingress/reviews/whole-tree-closeout-review.md)
- [bundle anatomy final closeout ledger](mechanics/distillation/parts/technique-reform-ingress/reviews/bundle-anatomy-final-closeout-ledger.md)
- [root roadmap tree migration breadcrumbs receipt](mechanics/distillation/legacy/raw/ROOT_ROADMAP_TREE_MIGRATION_BREADCRUMBS_2026-05-14.md)
- [root closure audit roadmap receipt](mechanics/audit/legacy/raw/ROOT_CLOSURE_AUDIT_ROADMAP_2026-05-03.md)

Those are evidence, not live root-roadmap body.

## Update Rule

Update this roadmap only when a change moves repo-level direction, corpus
topology, root source-of-truth posture, standalone portability,
mechanics-to-canon interface, or a concrete future trigger for this repository.

Do not update it for a local mechanic landing, generated refresh,
bundle-local evidence note, quest lifecycle move, release note, or donor ledger
entry unless that local change alters a repo-level direction.

## Current Direction

`aoa-techniques` is moving from closure-audit hardening into canon-scale
architecture:

- keep root entry surfaces compact, with [README](README.md) as a front door
  rather than a warehouse
- keep [CHARTER](CHARTER.md), [DESIGN](DESIGN.md),
  [DESIGN.AGENTS](DESIGN.AGENTS.md), [START_HERE](docs/START_HERE.md),
  [TECHNIQUE_ATOM_CONTRACT](docs/TECHNIQUE_ATOM_CONTRACT.md),
  [TECHNIQUE_TOPOLOGY_CONTRACT](docs/TECHNIQUE_TOPOLOGY_CONTRACT.md),
  [TECHNIQUE_TREE_CONTRACT](docs/TECHNIQUE_TREE_CONTRACT.md), and
  [ROOT_SURFACE_LAW](docs/ROOT_SURFACE_LAW.md) aligned without restating each
  other
- keep the corpus usable outside OS Abyss while preserving AoA provenance and
  sibling-owner routes
- keep each technique one atomic executable move suitable for templating,
  capsule projection, validation, and small-agent use after orchestration
  supplies context
- grow toward `1000+` techniques through faceted topology, not overloaded root
  categories
- keep mechanics as movement, provenance, review, and candidate routes around
  canon
- keep generated catalogs, capsules, source-lift readers, repo-doc manifests,
  and agent-mesh mirrors subordinate to authored sources

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

- Claim boundary: [CHARTER](CHARTER.md)
- Reader entry: [README](README.md), then [START_HERE](docs/START_HERE.md)
- Atomic technique: [TECHNIQUE_ATOM_CONTRACT](docs/TECHNIQUE_ATOM_CONTRACT.md)
- Classification and placement:
  [TECHNIQUE_TOPOLOGY_CONTRACT](docs/TECHNIQUE_TOPOLOGY_CONTRACT.md),
  [TECHNIQUE_TREE_CONTRACT](docs/TECHNIQUE_TREE_CONTRACT.md), and
  [TECHNIQUE_INDEX](TECHNIQUE_INDEX.md)
- Generated views: [technique catalog](generated/technique_catalog.min.json),
  [technique capsules](generated/technique_capsules.min.json), and
  [repo doc surface manifest](generated/repo_doc_surface_manifest.min.json)
- Movement and evidence: [mechanics README](mechanics/README.md),
  [Audit parts](mechanics/audit/parts/), and
  [Distillation parts](mechanics/distillation/parts/)
- Obligations and history: [QUESTBOOK](QUESTBOOK.md), [quests](quests/),
  [CHANGELOG](CHANGELOG.md), and [RELEASING](docs/RELEASING.md)

[ROADMAP](ROADMAP.md) keeps direction. Mechanic landing logs keep checked
mechanic landings. [CHANGELOG](CHANGELOG.md) keeps released history.
[QUESTBOOK](QUESTBOOK.md) keeps durable obligations.

## Horizon: Root Clarity

Root Markdown should remain role-bound: entry, authority, system form,
agent-surface form, direction, obligation, release history, contribution route,
conduct, security, and the corpus index.

Next: keep inventories in [Documentation Map](docs/README.md),
[Repo Doc Surfaces](docs/readers/repo/REPO_DOC_SURFACES.md), generated
manifests, or owner-local mechanics. Stop: do not move audit history, generated
detail, donor ledgers, mechanic-local runbooks, or semantic/shadow review
packets back into root.

## Horizon: Technique Atom

The technique atom contract names one atomic executable move as the unit of
canon.

Next: pressure every candidate through [TECHNIQUE_ATOM_CONTRACT](docs/TECHNIQUE_ATOM_CONTRACT.md)
before drafting or promoting. Stop: split, narrow, hold in mechanics, or route
to a stronger owner instead of padding broad candidates with prose.

## Horizon: Corpus Topology

`domain` and `kind` are authoritative frontmatter. Family, capability,
substrate, execution profile, risk posture, and richer relations remain design
axes until evidence justifies stronger status.

Next: enter selector and relation work through
[Technique Reform Ingress](mechanics/distillation/parts/technique-reform-ingress/README.md),
with [technique_topology_axes.yaml](mechanics/distillation/parts/technique-reform-ingress/config/technique_topology_axes.yaml)
and [technique_topology_scout.md](mechanics/distillation/parts/technique-reform-ingress/reports/technique_topology_scout.md)
as scout evidence. Stop: do not turn `agent-workflows`, `docs`, or tags into
junk drawers for missing topology.

## Horizon: Corpus Tree

The full tree migration is closed: `107` bundles sit under active
`techniques/<trunk>/<shelf>/<slug>/` paths across `10` trunks and `28` shelves.

Next: keep the landed tree stable while reform waves work through selector,
relation, portability, execution-profile, and bundle-anatomy evidence. Stop:
do not put shelf-by-shelf breadcrumbs, pilot queues, or parity ledgers back
into root roadmap, and do not add `tree_path` frontmatter without a fresh
owner-local review surface.

## Horizon: Small-Agent Usability

Capsules and generated catalogs provide compact lookup surfaces, while
bundle-anatomy work handles content-level usability.

Next: reform only where direct bundle reading finds a real source, selector,
relation, portability, owner-boundary, or execution-shape problem. Stop:
small-agent usability does not mean autonomous selection; routing and
composition can belong to larger agents or neighboring layers.

## Horizon: Mechanics To Canon

Mechanics packages keep active routes, parts, provenance, landing logs, package
roadmaps, and legacy scaffolds around canon.

Next: use mechanics to preserve lineage and candidate pressure while
extracting only one atomic practice at a time into [techniques](techniques/).
Stop: mechanics can prepare canon, but they do not replace canon or silently
change status.

## Horizon: Evidence And Promotion

Audit parts carry promotion readiness, evidence sprinting, searched-lane
memory, and canonical retro-audit work.

Next: route external-evidence work through Audit and Distillation, then update
bundle-local notes before shared queues. Stop: root roadmap names evidence
pressure only at horizon level; ledgers and queue detail belong in Audit.

## Horizon: Standalone Portability

The repository serves both external builders and AoA sibling repos.

Next: keep AoA references as provenance and integration context while making
portable practice understandable without OS Abyss. Stop: do not let AoA organ
fidelity become a hidden dependency for public reuse.

## Horizon: Generated Companions

Generated catalogs, capsules, source-lift readers, repo-doc surfaces, and
agent-mesh mirrors give machines compact routes over authored sources.

Next: keep generated parity validator-backed whenever source docs, templates,
route maps, mesh config, or surface specs change. Stop: generated outputs
route and compress; they do not author technique meaning, root law, agent law,
or status.

## When The Time Comes

These are repo-level triggers that should wait for real evidence:

- promote `family` from scout-only to optional reviewed frontmatter after
  examples and tie-break rules stay stable across multiple waves
- add projections for `capability_class`, `substrate`, `execution_profile`,
  and `risk_posture` after mechanics candidates prove the axes improve
  selection without false precision
- use the technique reform ingress packet before any broad classification
  change
- add richer typed relation guidance only when relations repeatedly help
  composition, conflict, sequence, or prerequisite routing
- keep [examples](examples/README.md) as the home for public worked examples
- add a machine-facing root route capsule only after the human route stabilizes
  enough that a generated companion reduces real reader load

Mechanic-local future pressure belongs in the owning mechanic roadmap. Durable
obligation belongs in [QUESTBOOK](QUESTBOOK.md) and [quests](quests/).

## Standing Direction

Across all horizons:

- keep one technique small
- keep the corpus navigable at scale
- keep portable practice stronger than local lore
- keep mechanics, generated surfaces, and sibling consumers subordinate to
  authored technique truth
- make every route clearer for both humans and small agents
