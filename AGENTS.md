# AGENTS.md

Root route card for `aoa-techniques`.

## Applies to

This card applies to the whole `aoa-techniques` repository. For any touched
path, read this card first and then the nearest nested `AGENTS.md`.

## Role

`aoa-techniques` is the public practice canon of AoA.
It stores reusable, sanitized, bounded, reviewable engineering techniques that can later be lifted into skills, evals, routing, KAG exports, or other derived artifacts.
A technique is a portable unit of method, not a skill bundle, proof surface, questline, or agent identity.
The corpus must work both as an AoA organ and as a standalone public library: external builders should be able to reuse a technique without deploying OS Abyss.
The primary unit is an atomic executable move: one compact technique should be small enough to classify, template, and hand to a small agent after orchestration supplies the right context.
Technique classification is faceted: `domain` and `kind` are current frontmatter truth, while family, capability, substrate, execution profile, risk posture, and relation topology should stay explicit design axes instead of being collapsed into tags.

## Owner lane

This repository owns:

- technique bundle meaning, IDs, intent, contracts, and adaptation notes
- public-safe technique wording and topology selection, including current
  domain/kind truth and future family/capability/substrate/risk axes
- owner-local participation in AoA cross-mechanics around reusable practice movement
- owner-local statistical questions, measurement meaning, and public reference
  packets about the technique canon
- root-level public-safe legacy provenance, archive, and migration receipts for repo-wide technique-canon history
- generated technique catalogs, capsules, feat-card reader surfaces, and source-lift surfaces

It does not own:

- skill workflow meaning, proof doctrine, routing, role contracts, memory,
  playbooks, KAG substrate meaning, cross-owner aggregation, or stats summaries
- private project operations, secrets, or infrastructure detail

## Skill home boundary

`aoa-techniques` currently owns no repository-local skill bundle. Do not create
an empty top-level `skills/` port and do not copy shared AoA bundles into
`.agents/skills/`. Shared skills reach agents through host or user-profile
projections outside this repository; technique discovery starts from authored
routes, `TECHNIQUE.md` bundles, and derived readers that return to those
sources.

A future repository-local skill is admissible only after one concrete
`aoa-techniques` capability demonstrates a distinct trigger, input/output
contract, independent composition value, failure boundary, and repeatable
benefit in manual no-skill and coexistence trials. A technique-to-skill idea is
only a proposal: route it through Method-growth and AOA-T-0102 to the receiving
owner without treating proposal, acceptance, activation, or projection as the
same event.

[DESIGN](DESIGN.md) names the repository system form. [DESIGN.AGENTS](DESIGN.AGENTS.md)
names the agent-facing surface form. This card is the operational route card
for agents.

## Read before editing

Read this root card first for repository identity, owner boundaries, and route selection.
For the selected surface, read the nearest local card and the exact stronger source: the authored technique bundle, source contract, schema, mechanic packet, builder, validator, or generated owner named by that route.
Use [DESIGN.AGENTS](DESIGN.AGENTS.md), [START_HERE](docs/START_HERE.md),
[TECHNIQUE_ATOM_CONTRACT](docs/TECHNIQUE_ATOM_CONTRACT.md),
[TECHNIQUE_TOPOLOGY_CONTRACT](docs/TECHNIQUE_TOPOLOGY_CONTRACT.md), and
[TECHNIQUE_TREE_CONTRACT](docs/TECHNIQUE_TREE_CONTRACT.md) only when the
agent-surface, authoring, topology, or tree question requires them.
Read `README.md` only when the selected task needs its human map; do not preload unrelated maps.

## Route modes

| Route mode | Use when | Start surface |
|---|---|---|
| `first-reading` | you need the shortest public overview | [README](README.md) -> [CHARTER](CHARTER.md) -> [START_HERE](docs/START_HERE.md) |
| `technique-authoring` | you will add, split, promote, or revise one technique | [TECHNIQUE_ATOM_CONTRACT](docs/TECHNIQUE_ATOM_CONTRACT.md) -> [TECHNIQUE_TOPOLOGY_CONTRACT](docs/TECHNIQUE_TOPOLOGY_CONTRACT.md) -> target bundle |
| `tree-structure` | you will design, project, or migrate corpus path architecture | [TECHNIQUE_TREE_CONTRACT](docs/TECHNIQUE_TREE_CONTRACT.md) -> [TECHNIQUE_TOPOLOGY_CONTRACT](docs/TECHNIQUE_TOPOLOGY_CONTRACT.md) -> affected generated surfaces |
| `root-editing` | you will add, move, delete, or rewrite a root or docs-root surface | [CHARTER](CHARTER.md) -> [ROOT_SURFACE_LAW](docs/ROOT_SURFACE_LAW.md) |
| `agent-surface-design` | you will add, move, normalize, or validate agent-facing cards | [DESIGN.AGENTS](DESIGN.AGENTS.md) -> [AGENTS_MESH_PROTOCOL](docs/guardrails/AGENTS_MESH_PROTOCOL.md) -> nearest `AGENTS.md` |
| `legacy-provenance` | you will preserve repo-wide raw packets, archived tails, or path-migration receipts | [Root Legacy](legacy/README.md) -> [Legacy Index](legacy/INDEX.md) -> active owner route |
| `direction-change` | roadmap, corpus-scale pressure, portability posture, or future triggers change | [ROADMAP](ROADMAP.md) |
| `mechanic-change` | practice movement, donor intake, audit, recurrence, checkpoint, RPG, or release-support surfaces change | [Mechanics](mechanics/README.md) -> nearest mechanic `AGENTS.md` |
| `generated-parity` | generated catalogs, capsules, source-lift, or repo-doc surfaces change | source doc -> builder -> generated output -> validator/test |
| `local-stats` | owner-local technique-canon measurement meaning or reference packets change | [Stats](stats/README.md) -> owning source -> consuming mechanic |

## AGENTS stack law

- Start with this root card, then follow the nearest nested `AGENTS.md` for every touched path.
- Root guidance owns repository identity, owner boundaries, route choice, and the shortest honest verification path.
- Nested guidance owns local contracts, local risk, exact files, and local checks.
- Authored source surfaces own meaning. Generated, exported, compact, derived, runtime, and adapter surfaces summarize, transport, or support meaning.
- Self-agency, recurrence, quest, progression, checkpoint, or growth language must stay bounded, reviewable, evidence-linked, and reversible.
- Report what changed, what was verified, what was not verified, and where the next agent should resume.

## Memory route

For technique-canon recall, continuity, compaction recovery, comparison with
past work, or preserved lessons, start with `aoa-memo` and the workspace memory
map. Session grounding routes through `.aoa`; local candidate writing routes
through this repository's `memo/` port when that port exists; durable reviewed
memory lands through `aoa-memo`.

## Post-change route review

Before closeout, check whether the change actually affects these surfaces.
Update only the ones that moved; otherwise say no update was needed.

- [ROADMAP](ROADMAP.md) when repo-level direction, corpus topology, standalone
  portability, mechanics-to-canon interface, root source-of-truth posture, or a
  concrete future trigger changed.
- [CHANGELOG](CHANGELOG.md) when public docs, validation, repository structure, GitHub
  intake, generated readers, or release-visible behavior changed.
- [decisions](docs/decisions/) when future agents need the rationale for a route,
  workflow, topology, validator, source-of-truth, or ownership choice.
- generated surfaces, builders, validators, and tests when a source-backed
  machine companion changed.
- mechanic `ROADMAP.md`, `LANDING_LOG.md`, `REQUEST_RECEIPTS.md`, `PARTS.md`,
  or `PROVENANCE.md` when mechanic direction, landing, owner-request receipt,
  active part, or legacy bridge changed.
- [QUESTBOOK](QUESTBOOK.md) or [quests](quests/) when a durable obligation should survive the diff.
- neighboring owner repositories when the change routes or constrains their
  truth.

## Boundaries

- Do not turn a technique into a skill, eval, route, playbook, memory object,
  role contract, runtime behavior, or ToS source.
- Do not recreate `.agents/skills/` as a repository cache for shared bundles or
  add an empty `skills/` home without an admitted repo-owned capability.
- Do not treat generated catalogs, capsules, source-lift outputs, or AGENTS
  mesh mirrors as authored meaning.
- Do not hide project-private residue, secrets, unreduced transcripts, or
  machine-local assumptions inside portable practice.
- Do not let a local `AGENTS.md` card override `TECHNIQUE.md`, source docs,
  schemas, builders, validators, or a stronger sibling owner.
- Do not make root files, docs-root files, or top-level directories without
  checking [ROOT_SURFACE_LAW](docs/ROOT_SURFACE_LAW.md).
- Do not infer quality, adoption, runtime use, or promotion decisions from a
  local stats packet; return to authored technique and review owners.

## Route away when

- the object is an executable workflow, not a reusable practice
- the object needs a chain of several independent moves instead of one atomic technique
- the change is proof, routing, memory, role, playbook, KAG, or stats meaning
- the idea is vague philosophy without an operational method

## Validation

Select the narrowest route in [VALIDATION.md](VALIDATION.md): `source-fast`, `generated`, `mechanics/part-local`, or `release` for the changed evidence class.
Exact order is owned by `config/validation_lanes.json`; focused procedure stays with the nearest owner. Report checks, skips, blockers, and supported claims.

## Closeout

Report changed surfaces, source owners, validation lanes and focused checks run, generated parity, skipped routes, external blockers, remaining risk, and the next owner route.
Keep local validation, CI, review, merge, publication, runtime use, adoption, and owner acceptance as separate claims; this card does not claim any unobserved state.

## Historical Reference

The former detailed root guidance is preserved only as legacy archive material
at [AGENTS_ROOT_REFERENCE](legacy/archive/AGENTS_ROOT_REFERENCE.md). Do not use
it as current route law; lift any surviving rule into this card or the nearest
owner surface before relying on it.
