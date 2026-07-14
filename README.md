# aoa-techniques

`aoa-techniques` is the public AoA practice canon: reusable, sanitized,
bounded engineering techniques for coding agents and humans.

A technique here is one atomic executable move. It is not a snippet dump,
skill bundle, playbook, proof verdict, role contract, routing policy, memory
object, or runtime behavior.

This README is only the public front door. When the question becomes authority,
authoring, classification, review, release, mechanics, or agent routing, follow
the linked owner surface instead of expanding root prose.

> Current release: `v0.5.0`. See [CHANGELOG](CHANGELOG.md) for release notes.

## What This Repository Does

This repository keeps portable practice small enough to select, adapt, verify,
and hand to a small agent after orchestration supplies context.

- Repository boundary: [CHARTER](CHARTER.md)
- System form: [DESIGN](DESIGN.md)
- Agent-surface form: [DESIGN.AGENTS](DESIGN.AGENTS.md)
- AoA layer position: [ECOSYSTEM_CONTEXT](docs/ECOSYSTEM_CONTEXT.md)
- First repo-owned route: [START_HERE](docs/START_HERE.md)
- Live corpus map: [TECHNIQUE_INDEX](TECHNIQUE_INDEX.md)
- Atomic technique contract: [TECHNIQUE_ATOM_CONTRACT](docs/TECHNIQUE_ATOM_CONTRACT.md)
- Classification and path law: [TECHNIQUE_TOPOLOGY_CONTRACT](docs/TECHNIQUE_TOPOLOGY_CONTRACT.md)
  and [TECHNIQUE_TREE_CONTRACT](docs/TECHNIQUE_TREE_CONTRACT.md)
- Direction and durable follow-through: [ROADMAP](ROADMAP.md) and
  [QUESTBOOK](QUESTBOOK.md)

Keep broad workflows, private residue, raw logs, sibling-repo authority, and
multi-step scenario choreography out of this canon unless they have been
distilled into one reusable move.

## Start Here

Read only the surface that matches the job.

- Short bounded overview: this README -> [CHARTER](CHARTER.md) ->
  [START_HERE](docs/START_HERE.md) -> [TECHNIQUE_INDEX](TECHNIQUE_INDEX.md)
- One concrete example bundle:
  [plan-diff-apply-verify-report](techniques/execution/agent-workflows-core/plan-diff-apply-verify-report/TECHNIQUE.md)
- Decide whether a candidate belongs: [CHARTER](CHARTER.md) ->
  [TECHNIQUE_ATOM_CONTRACT](docs/TECHNIQUE_ATOM_CONTRACT.md)
- Classify or place a bundle:
  [TECHNIQUE_TOPOLOGY_CONTRACT](docs/TECHNIQUE_TOPOLOGY_CONTRACT.md) ->
  [TECHNIQUE_KIND_GUIDE](docs/selection/TECHNIQUE_KIND_GUIDE.md) ->
  [TECHNIQUE_KIND_HANDOFF_PACK](docs/selection/TECHNIQUE_KIND_HANDOFF_PACK.md) ->
  [TECHNIQUE_TREE_CONTRACT](docs/TECHNIQUE_TREE_CONTRACT.md)
- Pick compact runtime cards:
  [TECHNIQUE_CAPSULES](docs/readers/runtime/TECHNIQUE_CAPSULES.md) or
  [technique_capsules.min.json](generated/technique_capsules.min.json)
- Query, explain, or pack one source-linked move:
  [TECHNIQUE_INTELLIGENCE](docs/readers/intelligence/TECHNIQUE_INTELLIGENCE.md),
  [TECHNIQUE_INTELLIGENCE_GUIDE](docs/selection/TECHNIQUE_INTELLIGENCE_GUIDE.md),
  or [technique_intelligence_registry.min.json](generated/technique_intelligence_registry.min.json)
- Inspect docs and route surfaces: [Documentation Map](docs/README.md),
  [Repo Doc Surfaces](docs/readers/repo/REPO_DOC_SURFACES.md), and
  [repo_doc_surface_manifest.min.json](generated/repo_doc_surface_manifest.min.json)
- Work as an agent: [AGENTS](AGENTS.md), then the nearest nested `AGENTS.md`

Deep mechanic runbooks, review packets, scout reports, generated readers, and
semantic or shadow review artifacts stay in the docs map, generated readers, or
owning [mechanics](mechanics/README.md) package.

## Route Modes

- `first-reading`: [README](README.md)
- `technique-authoring`: [TECHNIQUE_ATOM_CONTRACT](docs/TECHNIQUE_ATOM_CONTRACT.md)
- `classification`: [TECHNIQUE_TOPOLOGY_CONTRACT](docs/TECHNIQUE_TOPOLOGY_CONTRACT.md)
- `tree-structure`: [TECHNIQUE_TREE_CONTRACT](docs/TECHNIQUE_TREE_CONTRACT.md)
- `review-posture`: [Canonical Review Guide](docs/review/CANONICAL_REVIEW_GUIDE.md)
- `mechanic-change`: [mechanics](mechanics/README.md)
- `root-editing`: [ROOT_SURFACE_LAW](docs/ROOT_SURFACE_LAW.md)
- `agent-surface-design`: [DESIGN.AGENTS](DESIGN.AGENTS.md)
- `generated-parity`: authored source -> builder -> generated output -> validator
- `local-stats`: [stats](stats/README.md) -> owning source -> consuming mechanic

## Technique Check

Before adding, promoting, or trusting a technique, ask the narrowest owner:

- Atomic move: [TECHNIQUE_ATOM_CONTRACT](docs/TECHNIQUE_ATOM_CONTRACT.md)
- Portability: [CHARTER](CHARTER.md) and
  [TECHNIQUE_ATOM_CONTRACT](docs/TECHNIQUE_ATOM_CONTRACT.md)
- Classification: [TECHNIQUE_TOPOLOGY_CONTRACT](docs/TECHNIQUE_TOPOLOGY_CONTRACT.md),
  [TECHNIQUE_KIND_GUIDE](docs/selection/TECHNIQUE_KIND_GUIDE.md), and
  [TECHNIQUE_INDEX](TECHNIQUE_INDEX.md)
- Corpus path: [TECHNIQUE_TREE_CONTRACT](docs/TECHNIQUE_TREE_CONTRACT.md)
- Neighboring-object boundary: [CHARTER](CHARTER.md) and [AGENTS](AGENTS.md)
- Direction, history, obligation, or mechanic-local planning: [ROADMAP](ROADMAP.md),
  [CHANGELOG](CHANGELOG.md), [QUESTBOOK](QUESTBOOK.md), or the owning mechanic roadmap
- Generated freshness: source and mirror in
  [Repo Doc Surfaces](docs/readers/repo/REPO_DOC_SURFACES.md)

## Current Contour

The corpus is a tree of bundles under `techniques/<trunk>/<shelf>/<slug>/`.
Each bundle's authored meaning lives in `TECHNIQUE.md`.

Use [TECHNIQUE_INDEX](TECHNIQUE_INDEX.md) and
[technique_catalog.min.json](generated/technique_catalog.min.json) for the live
map. Use [ROADMAP](ROADMAP.md) for current direction and corpus-scale pressure.
Do not treat this README as a status ledger.

## Practice Mechanics

[Mechanics](mechanics/README.md) preserve practice movement around the canon:
donor intake, audit, evidence, recurrence, checkpoint, release support,
provenance, and package-local routes.

Use `mechanics/<slug>/` when a candidate is still moving toward canon. Use the
technique bundle when the reusable practice itself is already authored.

## Technical Districts

| District | Use for |
|---|---|
| [techniques](techniques/) | authored technique bundles |
| [docs](docs/README.md) | contracts, route maps, review guides, release docs, and generated-reader interpretation |
| [mechanics](mechanics/README.md) | practice movement, evidence, provenance, and mechanic-local routes |
| [generated](generated/) | reproducible catalogs, capsules, source-lift, review, and mesh companions |
| [stats](stats/README.md) | owner-local corpus questions, measurement contracts, and public reference packets |
| [examples](examples/README.md) | public-safe repo-wide worked examples |
| [templates](templates/) | technique authoring and promotion scaffolds |
| [legacy](legacy/README.md) | public-safe repo-wide raw, archive, and migration receipts |
| [.agents](.agents/AGENTS.md) | agent-facing companion lanes and local route support |
| [scripts](scripts/) | repo-wide builders and validators |
| [tests](tests/AGENTS.md) | repo-wide validation surfaces |

District gates narrow local handling. They do not replace source docs, bundle
meaning, mechanic packages, or sibling-owner repositories.

## Machine Companions

Machine-facing companions summarize the route:

- [technique_catalog.min.json](generated/technique_catalog.min.json): compact corpus catalog
- [technique_capsules.min.json](generated/technique_capsules.min.json): small runtime technique cards
- [technique_intelligence_registry.min.json](generated/technique_intelligence_registry.min.json):
  source-linked query, explanation, and packing packets for atomic moves
- [technique_intelligence_dag.min.json](generated/technique_intelligence_dag.min.json):
  navigation DAG over domains, kinds, family hints, and load refs
- [repo_doc_surface_manifest.min.json](generated/repo_doc_surface_manifest.min.json):
  compact map of bounded public route/canon/status docs
- [agents_mesh.min.json](generated/agents_mesh.min.json): compact AGENTS mesh coverage companion
- [kag_export.min.json](generated/kag_export.min.json): source-owned KAG export companion

Generated files route and compress. Authored bundles, contracts, route docs,
and owner-local mechanics keep authority.

## Working Rule

Grow the canon by extracting one reusable move cleanly.

If a detail belongs to a sibling repository, mechanic, generated mirror,
roadmap, changelog, quest, decision record, or legacy receipt, route it there
instead of making this README carry it.
