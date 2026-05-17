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
- root-level public-safe legacy provenance, archive, and migration receipts for repo-wide technique-canon history
- generated technique catalogs, capsules, feat-card reader surfaces, and source-lift surfaces

It does not own:

- skill workflow meaning, proof doctrine, routing, role contracts, memory, playbooks, KAG substrate meaning, or stats summaries
- private project operations, secrets, or infrastructure detail

[DESIGN](DESIGN.md) names the repository system form. [DESIGN.AGENTS](DESIGN.AGENTS.md)
names the agent-facing surface form. This card is the operational route card
for agents.

## Read before editing

1. [README](README.md)
2. [CHARTER](CHARTER.md)
3. [DESIGN](DESIGN.md)
4. [DESIGN.AGENTS](DESIGN.AGENTS.md)
5. [START_HERE](docs/START_HERE.md)
6. [TECHNIQUE_ATOM_CONTRACT](docs/TECHNIQUE_ATOM_CONTRACT.md)
7. [TECHNIQUE_TOPOLOGY_CONTRACT](docs/TECHNIQUE_TOPOLOGY_CONTRACT.md)
8. [TECHNIQUE_TREE_CONTRACT](docs/TECHNIQUE_TREE_CONTRACT.md) when corpus path architecture, tree projection, or bundle moves matter
9. [ROADMAP](ROADMAP.md) when direction, horizons, or repo-level future triggers move
10. [ROOT_SURFACE_LAW](docs/ROOT_SURFACE_LAW.md) when root or docs-root placement changes
11. [AGENTS_MESH_PROTOCOL](docs/guardrails/AGENTS_MESH_PROTOCOL.md) when agent-card coverage, shape, or generated mesh surfaces move
12. [Root Legacy](legacy/README.md) when root-wide raw, archive, or receipt provenance changes
13. [Mechanics](mechanics/README.md) when the change touches AoA mechanics or practice movement around canon
14. [Examples](examples/README.md) when a public worked example changes
15. [TECHNIQUE_SELECTION](docs/readers/selection/TECHNIQUE_SELECTION.md)
16. [TECHNIQUE_KIND_GUIDE](docs/selection/TECHNIQUE_KIND_GUIDE.md)
17. the target `techniques/**/TECHNIQUE.md`
18. affected generated catalogs, capsules, feat cards, agent-mesh mirrors, or source-lift outputs
19. the nearest local `AGENTS.md` under the touched path when a branch needs
    more detail than this root route card

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

## AGENTS stack law

- Start with this root card, then follow the nearest nested `AGENTS.md` for every touched path.
- Root guidance owns repository identity, owner boundaries, route choice, and the shortest honest verification path.
- Nested guidance owns local contracts, local risk, exact files, and local checks.
- Authored source surfaces own meaning. Generated, exported, compact, derived, runtime, and adapter surfaces summarize, transport, or support meaning.
- Self-agency, recurrence, quest, progression, checkpoint, or growth language must stay bounded, reviewable, evidence-linked, and reversible.
- Report what changed, what was verified, what was not verified, and where the next agent should resume.

## GitHub landing workflow

Root [AGENTS](AGENTS.md) owns the repository-wide branch, PR, CI, and merge route.
[.github/AGENTS](.github/AGENTS.md) owns the GitHub-native files that support it.

When the user asks to commit, push, and merge in this repository, use this
route:

1. Start from a clean branch based on current `origin/main`.
2. Commit only the intended diff with a message that names the changed surface.
3. Push the branch and open a pull request with changed surfaces, validation,
   skipped checks, generated parity, public-safety posture, and remaining risk.
4. Wait for GitHub `Repo Validation` to finish. If it fails, fix the branch and
   wait for the new result.
5. Merge through GitHub after green validation. Use squash unless repository
   settings require a different allowed method. If GitHub reports a different
   allowed method, use that method and report which method landed.
6. Return to `main`, fast-forward from `origin/main`, and confirm the worktree
   is clean before closeout.

If GitHub status or merge permissions cannot be observed, stop the landing route
and report the exact blocker instead of guessing.

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
- Do not treat generated catalogs, capsules, source-lift outputs, or AGENTS
  mesh mirrors as authored meaning.
- Do not hide project-private residue, secrets, unreduced transcripts, or
  machine-local assumptions inside portable practice.
- Do not let a local `AGENTS.md` card override `TECHNIQUE.md`, source docs,
  schemas, builders, validators, or a stronger sibling owner.
- Do not make root files, docs-root files, or top-level directories without
  checking [ROOT_SURFACE_LAW](docs/ROOT_SURFACE_LAW.md).

## Route away when

- the object is an executable workflow, not a reusable practice
- the object needs a chain of several independent moves instead of one atomic technique
- the change is proof, routing, memory, role, playbook, KAG, or stats meaning
- the idea is vague philosophy without an operational method

## Validation

Default validation:

```bash
python scripts/validate_repo.py
python scripts/run_tests.py
```

Use release checks when publication posture, broad generated outputs, or
companion-candidate surfaces change. For mechanic-specific companions such as
Agon, use the owning mechanic `AGENTS.md` and part README rather than preserved
root-era guidance.

For agent-surface changes, run the AGENTS mesh lane:

```bash
python scripts/validate_agents_md_shape.py
python scripts/validate_agents_mesh.py
python scripts/build_agents_mesh_index.py --check
python scripts/validate_agents_mesh_index.py
```

## Closeout

State the technique, technique family, root surface, mechanic, or GitHub
platform surface changed; whether IDs, kind, domain, state, adaptation notes,
generated companions, or source-lift surfaces changed; and exactly what
validation ran. If a PR was merged, name the GitHub merge method that landed.

## Historical Reference

The former detailed root guidance is preserved only as legacy archive material
at [AGENTS_ROOT_REFERENCE](legacy/archive/AGENTS_ROOT_REFERENCE.md). Do not use
it as current route law; lift any surviving rule into this card or the nearest
owner surface before relying on it.
