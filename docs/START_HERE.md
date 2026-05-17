# Start Here

This is the shortest repo-owned self-serve entrypoint for `aoa-techniques`.

Use it when you need one bounded answer to what to open next before entering
the deeper [Documentation Map](README.md), generated readers, mechanics
packages, or sibling repositories.

## What This Repo Is

- the public practice canon of AoA
- the source of truth for technique meaning, IDs, bounded contracts,
  adaptation notes, and generated companions built from authored sources
- the home for atomic executable moves that can be selected, expanded,
  verified, and handed to a small agent after orchestration supplies context
- a standalone public library: external builders should be able to reuse one
  technique, capsule, or bundle without deploying OS Abyss or the whole AoA
  ecosystem
- the owner of current technique classification contracts: [Technique Atom Contract](TECHNIQUE_ATOM_CONTRACT.md), [Technique Topology Contract](TECHNIQUE_TOPOLOGY_CONTRACT.md), and [Technique Tree Contract](TECHNIQUE_TREE_CONTRACT.md)
- the technique-layer home inside the AoA ontology spine; open [Ecosystem Context](ECOSYSTEM_CONTEXT.md) when the question is why this layer exists separately from skills, playbooks, evals, routing, or runtime repos

## If You Need One Technique Now

- open [Technique Atom Contract](TECHNIQUE_ATOM_CONTRACT.md) when the question is whether a candidate is one reusable technique
- open [Technique Topology Contract](TECHNIQUE_TOPOLOGY_CONTRACT.md) when `domain`, `kind`, family, capability, substrate, execution profile, risk posture, or relations matter
- keep scout values for capability, substrate, execution profile, and risk posture behind [Technique Topology Contract](TECHNIQUE_TOPOLOGY_CONTRACT.md); they are not frontmatter truth
- open [Technique Tree Contract](TECHNIQUE_TREE_CONTRACT.md) before proposing new root technique folders, tree trunks, shelves, or bundle moves
- open [Root Surface Law](ROOT_SURFACE_LAW.md), [Thematic District Protocol](guardrails/THEMATIC_DISTRICT_PROTOCOL.md), and [Current Surface Index](guardrails/CURRENT_SURFACE_INDEX.md) before adding, moving, or rewriting root or docs-root surfaces
- open [TECHNIQUE_INDEX](../TECHNIQUE_INDEX.md) for the whole corpus map
- open [Technique Selection Guide](selection/TECHNIQUE_SELECTION_GUIDE.md) before trusting chooser output
- open [Technique Selection](readers/selection/TECHNIQUE_SELECTION.md) for one bounded pick by domain and current defaults
- open [Selection Patterns](readers/selection/SELECTION_PATTERNS.md) when adjacency, working sets, or common next moves matter
- open [Technique Kind Guide](selection/TECHNIQUE_KIND_GUIDE.md) when the second selector axis matters
- open [Technique Kind Handoff Pack](selection/TECHNIQUE_KIND_HANDOFF_PACK.md) when a neighboring AoA repo needs the bounded `domain + kind` handoff
- open [`plan-diff-apply-verify-report`](../techniques/execution/agent-workflows-core/plan-diff-apply-verify-report/TECHNIQUE.md) when you want one concrete canonical bundle before any chooser surface; path: `techniques/execution/agent-workflows-core/plan-diff-apply-verify-report/TECHNIQUE.md`
- open [Technique Capsules](readers/runtime/TECHNIQUE_CAPSULES.md) or [technique capsules min JSON](../generated/technique_capsules.min.json) when a small runtime card is enough before expanding authored markdown

## If You Need To Understand Maturity And Review

- open [Canonical Rubric](review/CANONICAL_RUBRIC.md) for current frontmatter review fields and evidence kinds
- open [Canonical Review Guide](review/CANONICAL_REVIEW_GUIDE.md) for `promoted -> canonical` doctrine
- open [Mechanics](../mechanics/README.md) when the question is which AoA cross-mechanic owns practice movement before, around, or after canon; path: `mechanics/README.md`
- open [Audit](../mechanics/audit/README.md) for promotion readiness, evidence sprinting, external-proof ledgers, and canonical retro-check routes; path: `mechanics/audit/README.md`
- open [Distillation](../mechanics/distillation/README.md) for donor import, long-gap re-entry, external candidates, cross-layer candidates, Agon handoff, and technique-reform ingress routes; path: `mechanics/distillation/README.md`
- open [Agon](../mechanics/agon/README.md) or [Antifragility](../mechanics/antifragility/README.md) only after the mechanics atlas says the movement belongs there

## If You Need Derived Surfaces

- open [Repo Doc Surfaces](readers/repo/REPO_DOC_SURFACES.md) when the question is which authoritative repo doc to read next
- open [KAG Source Lift Guide](source-lift/KAG_SOURCE_LIFT_GUIDE.md) when you need section, checklist, example, evidence-note, metadata, relation, or risk lift boundaries
- open [Technique Sections](readers/source-lift/TECHNIQUE_SECTIONS.md), [Technique Checklists](readers/source-lift/TECHNIQUE_CHECKLISTS.md), [Technique Examples](readers/source-lift/TECHNIQUE_EXAMPLES.md), or [Evidence Note Surfaces](readers/source-lift/EVIDENCE_NOTE_SURFACES.md) for reader-facing generated companions
- open [Semantic Review Guide](review/SEMANTIC_REVIEW_GUIDE.md) when authored review packets and generated semantic-review manifests need interpretation
- open [SHADOW_PATTERNS.md](readers/review/SHADOW_PATTERNS.md), [Technique Shadow Guide](review/TECHNIQUE_SHADOW_GUIDE.md), and [Risk And Negative-Effect Lift Guide](source-lift/RISK_AND_NEGATIVE_EFFECT_LIFT_GUIDE.md) when the question is about caution seams or boundary drift
- open [AGENTS Mesh Protocol](guardrails/AGENTS_MESH_PROTOCOL.md), [AGENTS Mesh Index](guardrails/AGENTS_MESH_INDEX.md), and [agents mesh min JSON](../generated/agents_mesh.min.json) for local agent-card coverage

## Current Corpus Posture

- current corpus posture is generated from `../generated/technique_catalog.min.json` and the selection surfaces, not hand-maintained here
- open [Technique Selection](readers/selection/TECHNIQUE_SELECTION.md) for the live domain/kind/status split before trusting any snapshot count
- use [technique catalog min JSON](../generated/technique_catalog.min.json) when you need the current machine-readable corpus view
- use [Roadmap](../ROADMAP.md) for repo-level direction and [Root Legacy](../legacy/README.md) for repo-wide public-safe receipts, archives, and raw snapshots
- the intended growth shape remains `1000+` compact, well-classified, template-backed techniques, with a tree of trunks, shelves, and leaf bundles instead of junk drawers
- the repo-wide operating shape is `pick -> inspect -> expand -> object use`

## Repo-Only Operating Contract

- `pick`: choose one route from this page, [Technique Selection](readers/selection/TECHNIQUE_SELECTION.md), or [Repo Doc Surfaces](readers/repo/REPO_DOC_SURFACES.md)
- `inspect`: open one `TECHNIQUE.md`, one guide, or one review surface
- `expand`: only then open a generated manifest or full markdown section/body
- `object use`: use one atomic technique meaning or derived routing surface from this repo before jumping to execution, verdict, or routing repositories

## When To Leave This Repo

- stay in `aoa-techniques` when the question is technique meaning, selection, promotion posture, review posture, or repo-owned generated companions
- go to [aoa-skills](https://github.com/8Dionysus/aoa-skills) for bounded execution workflows built from these techniques
- go to [aoa-evals](https://github.com/8Dionysus/aoa-evals) for verdict doctrine, proof surfaces, and bounded claim checks
- go to [aoa-routing](https://github.com/8Dionysus/aoa-routing) for smallest-next-surface routing and dispatch hints

## Release And Validation

- run `python -m pip install -r requirements-dev.txt` once before local validation if this checkout does not already have repo dev dependencies
- for a read-only current-state pass, run `python scripts/validate_repo.py` and `python scripts/run_tests.py`
- open [Releasing `aoa-techniques`](RELEASING.md) for release-prep doctrine
- for bounded release-prep parity, run `python scripts/release_check.py`, then confirm `git status -sb` stayed clean
- use individual `build_*` commands only when intentionally regenerating one surface family during authored edits
