# Start Here

This is the repo-owned self-serve entrypoint for `aoa-techniques`.

Use it when you want one bounded answer to what to open next without guessing between the root README, the docs map, generated surfaces, or sibling repositories.

## What This Repo Is

- the public practice canon of AoA
- the source of truth for technique meaning, IDs, bounded contracts, adaptation notes, and generated technique surfaces built from those authored sources
- a repository for reusable techniques, not for bounded execution workflows, verdict logic, routing policy, or private project operations

## If You Need One Technique Now

- open [Technique Selection Guide](TECHNIQUE_SELECTION_GUIDE.md) when the question is how the selection family stays bounded before you trust any chooser surface
- open [Technique Selection](TECHNIQUE_SELECTION.md) for one bounded pick by domain and current defaults
- open [Selection Patterns](SELECTION_PATTERNS.md) when adjacency, working sets, or common next moves matter more than a flat list
- open [TECHNIQUE_INDEX](../TECHNIQUE_INDEX.md) when you want the whole corpus map first
- if you are an agent and want the smallest repo-owned runtime card before expanding markdown, open [Technique Capsules](TECHNIQUE_CAPSULES.md) or `../generated/technique_capsules.min.json`

## If You Need To Understand Maturity And Review

- open [Canonical Rubric](CANONICAL_RUBRIC.md) for the current frontmatter review fields and evidence kinds
- open [Canonical Review Guide](CANONICAL_REVIEW_GUIDE.md) for `promoted -> canonical` doctrine
- open [Promotion Readiness Matrix](PROMOTION_READINESS_MATRIX.md) when the question is which `promoted` bundle can be honestly strengthened next and what proof is still missing
- open [Promotion Wave A Runbook](PROMOTION_WAVE_A_RUNBOOK.md) when the question is how to run the current first evidence-prep swarm without widening bundle meaning or faking closure
- open [Donor Refinery Rubric](DONOR_REFINERY_RUBRIC.md) when the question is what can be extracted from an external donor without importing foreign doctrine
- open [External Import Runbook](EXTERNAL_IMPORT_RUNBOOK.md) when the question is how to take one bounded donor from triage to merge without inventing a new maintainer path
- open [Long-Gap Canon Design](LONG_GAP_CANON_DESIGN.md) when the question is why a remaining `promoted` technique still needs an external donor path
- open [Deep Audit Roadmap](DEEP_AUDIT_ROADMAP.md) when the question is which repo-only hardening, review refresh, or external evidence wave should open next
- open [External Technique Candidates](EXTERNAL_TECHNIQUE_CANDIDATES.md) when the question is which remaining external seed idea is actually worth distilling into a future bundle
- open [Cross-Layer Technique Candidates](CROSS_LAYER_TECHNIQUE_CANDIDATES.md) when the question is how the Dionysus donor-note candidate set should be filtered without widening the external-only intake surface
- use [TECHNIQUE_INDEX](../TECHNIQUE_INDEX.md) as the live corpus split

## If You Need Derived Surfaces

- open [Repo Doc Surfaces](REPO_DOC_SURFACES.md) when the question is which authoritative repo doc to read next
- open [Technique Capsules](TECHNIQUE_CAPSULES.md) when one small runtime card is enough
- open [KAG Source Lift Guide](KAG_SOURCE_LIFT_GUIDE.md) when you need section, checklist, example, evidence-note, or bounded relation lift surfaces
- open [SHADOW_PATTERNS.md](SHADOW_PATTERNS.md) and the semantic review docs when the question is about caution seams or boundary drift rather than first-pick selection
- open [Semantic Review Guide](SEMANTIC_REVIEW_GUIDE.md) when the question is how authored review docs relate to working sets and the semantic-review manifest without becoming policy

## Current Corpus Posture

- current split: `18 canonical`, `30 promoted`
- latest canonical promotion: `AOA-T-0018`
- current closest promoted queue item: `AOA-T-0013`
- current internal-origin promoted techniques: `AOA-T-0033`, `AOA-T-0034`, `AOA-T-0046`, `AOA-T-0047`, `AOA-T-0048`
- current future-import-wave promoted techniques: `AOA-T-0035`, `AOA-T-0036`, `AOA-T-0037`, `AOA-T-0038`, `AOA-T-0039`, `AOA-T-0040`, `AOA-T-0041`, `AOA-T-0042`, `AOA-T-0043`, `AOA-T-0044`, `AOA-T-0045`
- current external-dependency-first promoted techniques: `AOA-T-0005`, `AOA-T-0023`, `AOA-T-0028`, `AOA-T-0031`, `AOA-T-0013`, `AOA-T-0020`, `AOA-T-0022`, `AOA-T-0027`, `AOA-T-0024`, `AOA-T-0025`, `AOA-T-0029`, `AOA-T-0030`, `AOA-T-0032`, `AOA-T-0026`
- current bounded `history` domain covers session/history artifacts only; memory objects and recall surfaces still stay outside this repo's ownership boundary
- the current repo-wide operating shape is still `pick -> inspect -> expand -> object use`

## Repo-Only Operating Contract

- `pick`: choose one route from this page, `TECHNIQUE_SELECTION.md`, or `REPO_DOC_SURFACES.md`
- `inspect`: open one `TECHNIQUE.md`, one guide, or one review surface
- `expand`: only then open a generated manifest or full markdown section/body
- `object use`: use the technique meaning or derived routing surface from this repo before jumping to execution or routing repos

## When To Leave This Repo

- stay in `aoa-techniques` when the question is technique meaning, selection, promotion posture, review posture, or repo-owned derived surfaces
- go to [aoa-skills](https://github.com/8Dionysus/aoa-skills) for bounded execution workflows built from these techniques
- go to [aoa-evals](https://github.com/8Dionysus/aoa-evals) for verdict doctrine, proof surfaces, and bounded claim checks
- go to [aoa-routing](https://github.com/8Dionysus/aoa-routing) for smallest-next-surface routing and dispatch hints

## Release And Validation

- open [Releasing `aoa-techniques`](RELEASING.md) for the current release-prep doctrine
- run `python scripts/release_check.py` for the repo-owned bounded release-check path
- use the individual `build_*` commands only when you are intentionally regenerating one surface family during authored edits
