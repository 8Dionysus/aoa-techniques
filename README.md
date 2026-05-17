# aoa-techniques

`aoa-techniques` is the public practice canon of AoA: a library of reusable,
sanitized, bounded engineering techniques for coding agents and humans.

A technique here is not a snippet, checklist dump, skill bundle, playbook,
role, proof verdict, or runtime behavior. It is one atomic executable move:
small enough to classify, template, verify, and hand to a small agent after
orchestration supplies the right context.

This repository has a dual posture. It must work as a standalone public
library, where an external builder can reuse one technique, capsule, or bundle
without deploying OS Abyss. It also works as an AoA organ, where authored
techniques keep stable IDs, topology, provenance, review posture, mechanics,
and generated companions for sibling repositories to consume.

Use this README as the public front door. Use the linked source surfaces when
the work becomes authoring, classification, review, release, mechanics, or
agent-route work.

> Current release: `v0.4.2`. See [CHANGELOG](CHANGELOG.md) for release notes.

## What This Repository Does

| Function | Surface |
|---|---|
| Defines the practice-canon authority boundary | [CHARTER](CHARTER.md) |
| Describes the system form the technique canon should preserve | [DESIGN](DESIGN.md) |
| Describes the shape of agent-facing route cards and the AGENTS mesh | [DESIGN.AGENTS](DESIGN.AGENTS.md) |
| Positions this repository inside the AoA layer map | [ECOSYSTEM_CONTEXT](docs/ECOSYSTEM_CONTEXT.md) |
| Routes new readers into the shortest repo-owned path | [START_HERE](docs/START_HERE.md) |
| Keeps the public corpus map by ID, status, domain, kind, and path | [TECHNIQUE_INDEX](TECHNIQUE_INDEX.md) |
| Defines what counts as one atomic technique | [TECHNIQUE_ATOM_CONTRACT](docs/TECHNIQUE_ATOM_CONTRACT.md) |
| Defines corpus classification and path architecture | [TECHNIQUE_TOPOLOGY_CONTRACT](docs/TECHNIQUE_TOPOLOGY_CONTRACT.md), [TECHNIQUE_TREE_CONTRACT](docs/TECHNIQUE_TREE_CONTRACT.md) |
| Holds repo-level direction without becoming a changelog or mechanic ledger | [ROADMAP](ROADMAP.md) |
| Preserves durable obligations without turning them into roadmap history | [QUESTBOOK](QUESTBOOK.md) |

This repository is strongest when it extracts one reusable move cleanly. It is
weakest when it absorbs workflow orchestration, sibling-repo authority, private
project residue, raw logs, or broad method chains.

## Start Here

Read only what matches the entry need.

| Need | Route |
|---|---|
| Shortest bounded overview | this README, then [CHARTER](CHARTER.md), [START_HERE](docs/START_HERE.md), and [TECHNIQUE_INDEX](TECHNIQUE_INDEX.md) |
| One concrete example bundle | [plan-diff-apply-verify-report](techniques/execution/agent-workflows-core/plan-diff-apply-verify-report/TECHNIQUE.md) |
| Decide whether a candidate belongs here | [CHARTER](CHARTER.md), then [TECHNIQUE_ATOM_CONTRACT](docs/TECHNIQUE_ATOM_CONTRACT.md) |
| Classify or place a technique | [TECHNIQUE_TOPOLOGY_CONTRACT](docs/TECHNIQUE_TOPOLOGY_CONTRACT.md), [TECHNIQUE_KIND_GUIDE](docs/selection/TECHNIQUE_KIND_GUIDE.md), [TECHNIQUE_KIND_HANDOFF_PACK](docs/selection/TECHNIQUE_KIND_HANDOFF_PACK.md), and [TECHNIQUE_TREE_CONTRACT](docs/TECHNIQUE_TREE_CONTRACT.md) |
| Pick a compact runtime card | [TECHNIQUE_CAPSULES](docs/readers/runtime/TECHNIQUE_CAPSULES.md) or [technique_capsules.min.json](generated/technique_capsules.min.json) |
| Understand maturity, review, or promotion posture | [Canonical Review Guide](docs/review/CANONICAL_REVIEW_GUIDE.md), [Canonical Rubric](docs/review/CANONICAL_RUBRIC.md), and [mechanics/audit](mechanics/audit/README.md) |
| Understand current direction or parked work | [ROADMAP](ROADMAP.md) and [QUESTBOOK](QUESTBOOK.md) |
| Work on root or docs-root placement | [ROOT_SURFACE_LAW](docs/ROOT_SURFACE_LAW.md) |
| Work as an agent in this repo | [AGENTS](AGENTS.md), then the nearest nested `AGENTS.md` |
| Need the deeper docs tree | [Documentation Map](docs/README.md) and [Repo Doc Surfaces](docs/readers/repo/REPO_DOC_SURFACES.md) |

Deep mechanic runbooks, review packets, ledgers, scout reports, generated
readers, and shadow or semantic review artifacts are intentionally not
re-indexed here. Start from the docs map or the owning `mechanics/<slug>/`
route when you need that detail.

## Route Modes

| Route mode | Use when | Start surface |
|---|---|---|
| `first-reading` | you need the shortest public overview | [README](README.md) |
| `technique-authoring` | you will add, split, promote, or revise one technique | [TECHNIQUE_ATOM_CONTRACT](docs/TECHNIQUE_ATOM_CONTRACT.md) |
| `classification` | domain, kind, topology, relation, or path placement matters | [TECHNIQUE_TOPOLOGY_CONTRACT](docs/TECHNIQUE_TOPOLOGY_CONTRACT.md) |
| `tree-structure` | corpus path architecture or bundle moves matter | [TECHNIQUE_TREE_CONTRACT](docs/TECHNIQUE_TREE_CONTRACT.md) |
| `review-posture` | maturity, canonical readiness, or evidence posture matters | [Canonical Review Guide](docs/review/CANONICAL_REVIEW_GUIDE.md) |
| `mechanic-change` | donor intake, audit, recurrence, checkpoint, release-support, or practice movement changes | [mechanics](mechanics/README.md) |
| `root-editing` | root or docs-root surfaces move | [ROOT_SURFACE_LAW](docs/ROOT_SURFACE_LAW.md) |
| `agent-surface-design` | local `AGENTS.md` cards or generated mesh surfaces move | [DESIGN.AGENTS](DESIGN.AGENTS.md) |
| `generated-parity` | generated catalogs, capsules, source-lift, or repo-doc mirrors move | source doc, builder, generated output, then validator |

## Technique Check

Before adding, promoting, or trusting a technique, route the claim through the
smallest source that can answer it.

| Question | Check |
|---|---|
| Is this one atomic executable move? | [TECHNIQUE_ATOM_CONTRACT](docs/TECHNIQUE_ATOM_CONTRACT.md) |
| Can it stand alone outside the private AoA workspace? | [CHARTER](CHARTER.md) and [TECHNIQUE_ATOM_CONTRACT](docs/TECHNIQUE_ATOM_CONTRACT.md) |
| Is the classification honest? | [TECHNIQUE_TOPOLOGY_CONTRACT](docs/TECHNIQUE_TOPOLOGY_CONTRACT.md), [TECHNIQUE_KIND_GUIDE](docs/selection/TECHNIQUE_KIND_GUIDE.md), and [TECHNIQUE_INDEX](TECHNIQUE_INDEX.md) |
| Does the path match the current corpus tree? | [TECHNIQUE_TREE_CONTRACT](docs/TECHNIQUE_TREE_CONTRACT.md) |
| Is the text technique meaning rather than a skill, eval, route, playbook, memory object, role, or runtime behavior? | [CHARTER](CHARTER.md) and [AGENTS](AGENTS.md) |
| Is this current direction rather than released history, durable obligation, or mechanic-local planning? | [ROADMAP](ROADMAP.md), [CHANGELOG](CHANGELOG.md), [QUESTBOOK](QUESTBOOK.md), and `mechanics/<slug>/ROADMAP.md` |
| Does a generated companion still match its authored source? | the owning source surface and generated mirror listed in [Repo Doc Surfaces](docs/readers/repo/REPO_DOC_SURFACES.md) |

## Current Contour

The current public corpus is a tree of technique bundles under
`techniques/<trunk>/<shelf>/<slug>/`, with authored meaning in each
`TECHNIQUE.md`.

Current anchors:

- [CHARTER](CHARTER.md), [DESIGN](DESIGN.md), and [DESIGN.AGENTS](DESIGN.AGENTS.md)
  for repo authority, system form, and agent-surface form
- [TECHNIQUE_INDEX](TECHNIQUE_INDEX.md) and
  [technique_catalog.min.json](generated/technique_catalog.min.json) for the
  current corpus map
- [TECHNIQUE_ATOM_CONTRACT](docs/TECHNIQUE_ATOM_CONTRACT.md),
  [TECHNIQUE_TOPOLOGY_CONTRACT](docs/TECHNIQUE_TOPOLOGY_CONTRACT.md), and
  [TECHNIQUE_TREE_CONTRACT](docs/TECHNIQUE_TREE_CONTRACT.md) for authoring,
  classification, and path law
- [ROADMAP](ROADMAP.md) for live repo direction and future triggers
- [mechanics](mechanics/README.md) for practice movement around the canon
- [generated](generated/) for compact machine companions

Live counts and generated views belong in generated outputs and roadmap
contour, not in this README.

## Practice Mechanics

Mechanics live under [mechanics](mechanics/README.md). They preserve movement,
provenance, review posture, donor intake, recurrence, checkpoint, RPG,
release-support, and other practice-canon work around the published technique
bundles.

Use a mechanic package when the question is how a technique candidate moves
toward canon, how evidence is prepared, how a review packet is interpreted, or
where historical movement should be preserved. Use a technique bundle when the
question is the reusable practice itself.

## Technical Districts

Root-adjacent technical districts have local gates:

| District | Use for |
|---|---|
| [techniques](techniques/) | authored technique bundles |
| [docs](docs/README.md) | contracts, route maps, review guides, release docs, and generated-reader interpretation |
| [mechanics](mechanics/README.md) | practice movement, evidence, provenance, and mechanic-local routes |
| [generated](generated/) | reproducible catalogs, capsules, source-lift, review, and mesh companions |
| [examples](examples/README.md) | public-safe repo-wide worked examples |
| [templates](templates/) | technique authoring and promotion scaffolds |
| [legacy](legacy/README.md) | public-safe repo-wide raw, archive, and migration receipts after active distillation |
| [.agents](.agents/AGENTS.md) | agent-facing companion lanes and local route support |
| [scripts](scripts/) | repo-wide builders and validators |
| [tests](tests/AGENTS.md) | repo-wide validation surfaces |

District gates explain local handling. They do not replace technique meaning,
source docs, mechanic packages, or sibling-owner repositories.

## Machine Companions

Machine-facing surfaces summarize and validate the human route:

| Surface | Role |
|---|---|
| [technique_catalog.min.json](generated/technique_catalog.min.json) | compact corpus catalog |
| [technique_capsules.min.json](generated/technique_capsules.min.json) | small runtime technique cards |
| [repo_doc_surface_manifest.min.json](generated/repo_doc_surface_manifest.min.json) | compact map of bounded public route/canon/status docs |
| [agents_mesh.min.json](generated/agents_mesh.min.json) | compact AGENTS mesh coverage companion |
| [kag_export.min.json](generated/kag_export.min.json) | source-owned KAG export companion |

Generated surfaces are companions, not authority. Authored technique bundles,
contracts, route docs, and owner-local mechanics keep meaning.

## Working Rule

Grow the canon by extracting one reusable move cleanly.

When a detail belongs to another repository, mechanic, generated mirror,
roadmap, changelog, quest, decision record, or legacy receipt, route it there
instead of making the root README carry it.
