# Start Here

This is the shortest repo-owned self-serve entrypoint for `aoa-techniques`.

Use it when you need the next correct surface before entering the deeper
[Documentation Map](README.md), generated readers, mechanics packages, or
sibling repositories.

## What This Repo Is

`aoa-techniques` is the public practice canon of AoA: atomic executable moves,
their IDs, contracts, notes, review posture, and generated companions derived
from authored sources.

The core contracts are [Technique Atom Contract](TECHNIQUE_ATOM_CONTRACT.md),
[Technique Topology Contract](TECHNIQUE_TOPOLOGY_CONTRACT.md), and
[Technique Tree Contract](TECHNIQUE_TREE_CONTRACT.md). Open
[Ecosystem Context](ECOSYSTEM_CONTEXT.md) when the question is why techniques
are separate from skills, evals, routing, playbooks, runtime, memory, or KAG
repos.

The repo-wide operating shape is `pick -> inspect -> expand -> object use`.
Pick one surface, inspect one bundle or guide, expand only when needed, then
use the technique meaning or derived route without importing another layer's
authority.

## If You Need One Technique Now

| Need | Open |
|---|---|
| A concrete canonical bundle before any chooser | [`plan-diff-apply-verify-report`](../techniques/execution/agent-workflows-core/plan-diff-apply-verify-report/TECHNIQUE.md); path: `techniques/execution/agent-workflows-core/plan-diff-apply-verify-report/TECHNIQUE.md` |
| Whole corpus map | [TECHNIQUE_INDEX](../TECHNIQUE_INDEX.md) |
| One bounded pick by domain and defaults | [Technique Selection](readers/selection/TECHNIQUE_SELECTION.md) after [Technique Selection Guide](selection/TECHNIQUE_SELECTION_GUIDE.md) |
| Adjacency, working sets, or common next moves | [Selection Patterns](readers/selection/SELECTION_PATTERNS.md) |
| The second selector axis | [Technique Kind Guide](selection/TECHNIQUE_KIND_GUIDE.md) |
| Neighboring-repo `domain + kind` handoff | [Technique Kind Handoff Pack](selection/TECHNIQUE_KIND_HANDOFF_PACK.md) |
| A small runtime card | [Technique Capsules](readers/runtime/TECHNIQUE_CAPSULES.md) or [technique capsules min JSON](../generated/technique_capsules.min.json) |
| Root or docs placement | [Root Surface Law](ROOT_SURFACE_LAW.md), [Thematic District Protocol](guardrails/THEMATIC_DISTRICT_PROTOCOL.md), [Current Surface Index](guardrails/CURRENT_SURFACE_INDEX.md) |

Use [Technique Topology Contract](TECHNIQUE_TOPOLOGY_CONTRACT.md) for `domain`,
`kind`, family, capability, substrate, execution profile, risk posture, and
relations. Scout values for capability, substrate, execution profile, and risk
posture are not frontmatter truth.

## If You Need To Understand Maturity And Review

Use [Canonical Rubric](review/CANONICAL_RUBRIC.md) for current review fields and
evidence kinds. Use [Canonical Review Guide](review/CANONICAL_REVIEW_GUIDE.md)
for `promoted -> canonical` doctrine.

Use [Mechanics](../mechanics/README.md) when practice movement, candidate
pressure, or evidence work is not yet a technique bundle; path:
`mechanics/README.md`. The common entrypoints are [Audit](../mechanics/audit/README.md)
for readiness and proof movement, path: `mechanics/audit/README.md`, and
[Distillation](../mechanics/distillation/README.md) for donor import,
cross-layer candidates, and reform ingress, path:
`mechanics/distillation/README.md`.

## If You Need Derived Surfaces

Generated readers help orientation; authored sources still win.

| Need | Open |
|---|---|
| Which authoritative repo doc to read | [Repo Doc Surfaces](readers/repo/REPO_DOC_SURFACES.md) |
| Section, checklist, example, evidence-note, metadata, relation, or risk lift boundaries | [KAG Source Lift Guide](source-lift/KAG_SOURCE_LIFT_GUIDE.md) |
| Reader-facing source-lift companions | [Technique Sections](readers/source-lift/TECHNIQUE_SECTIONS.md), [Technique Checklists](readers/source-lift/TECHNIQUE_CHECKLISTS.md), [Technique Examples](readers/source-lift/TECHNIQUE_EXAMPLES.md), [Evidence Note Surfaces](readers/source-lift/EVIDENCE_NOTE_SURFACES.md) |
| Semantic review interpretation | [Semantic Review Guide](review/SEMANTIC_REVIEW_GUIDE.md) |
| Caution seams or boundary drift | [SHADOW_PATTERNS.md](readers/review/SHADOW_PATTERNS.md), [Technique Shadow Guide](review/TECHNIQUE_SHADOW_GUIDE.md), [Risk And Negative-Effect Lift Guide](source-lift/RISK_AND_NEGATIVE_EFFECT_LIFT_GUIDE.md) |
| Local agent-card coverage | [AGENTS Mesh Protocol](guardrails/AGENTS_MESH_PROTOCOL.md), [AGENTS Mesh Index](guardrails/AGENTS_MESH_INDEX.md), [agents mesh min JSON](../generated/agents_mesh.min.json) |

## Current Corpus Posture

The current corpus posture is generated from
`../generated/technique_catalog.min.json` and the selection surfaces, not
hand-maintained here.

Open [Technique Selection](readers/selection/TECHNIQUE_SELECTION.md) for the
live domain/kind/status split. Use [technique catalog min JSON](../generated/technique_catalog.min.json)
for the current machine-readable corpus view. Use [Roadmap](../ROADMAP.md) for
direction and [Root Legacy](../legacy/README.md) for public-safe receipts,
archives, and raw snapshots.

The growth target remains `1000+` compact, well-classified, template-backed
techniques in trunks, shelves, and leaf bundles.

## Repo-Only Operating Contract

`pick`: choose one route from this page, [Technique Selection](readers/selection/TECHNIQUE_SELECTION.md),
or [Repo Doc Surfaces](readers/repo/REPO_DOC_SURFACES.md).

`inspect`: open one `TECHNIQUE.md`, one guide, or one review surface.

`expand`: only then open a generated manifest or full markdown section/body.

`object use`: use one atomic technique meaning or derived routing surface from
this repo before jumping to execution, verdict, or routing repositories.

## When To Leave This Repo

Stay in `aoa-techniques` for technique meaning, selection, promotion posture,
review posture, and repo-owned generated companions.

Leave when the object class changes: [aoa-skills](https://github.com/8Dionysus/aoa-skills)
owns bounded execution workflows, [aoa-evals](https://github.com/8Dionysus/aoa-evals)
owns verdict doctrine and proof surfaces, and [aoa-routing](https://github.com/8Dionysus/aoa-routing)
owns smallest-next-surface routing and dispatch hints.

## Release And Validation

Install dev dependencies once when needed:

```bash
python -m pip install -r requirements-dev.txt
```

Use the narrowest check that matches the change:

```bash
python scripts/validate_repo.py
python scripts/run_tests.py
python scripts/release_check.py
git status -sb
```

Open [Releasing `aoa-techniques`](RELEASING.md) for release-prep doctrine. Use
individual `build_*` commands only when intentionally regenerating one surface
family during authored edits.
