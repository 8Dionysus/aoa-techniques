# Start Here

This is the repo-owned self-serve entrypoint for `aoa-techniques`.

Use it when you want one bounded answer to what to open next without guessing between the root README, the docs map, generated surfaces, or sibling repositories.

## What This Repo Is

- the public practice canon of AoA
- the source of truth for technique meaning, IDs, bounded contracts, adaptation notes, and generated technique surfaces built from those authored sources
- a repository for reusable techniques, not for bounded execution workflows, verdict logic, routing policy, or private project operations
- the technique-layer home inside the AoA ontology spine; open [Ecosystem Context](ECOSYSTEM_CONTEXT.md) when the question is why this layer exists separately from skills, playbooks, evals, or runtime repos

## If You Need One Technique Now

- open [`plan-diff-apply-verify-report`](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) when you want one concrete canonical bundle before any chooser or generated surface
- open [Technique Selection Guide](TECHNIQUE_SELECTION_GUIDE.md) when the question is how the selection family stays bounded before you trust any chooser surface
- open [Technique Kind Guide](TECHNIQUE_KIND_GUIDE.md) when the second selector axis or a kind tie-break matters
- open [Technique Kind Handoff Pack](TECHNIQUE_KIND_HANDOFF_PACK.md) when a neighboring AoA repo needs the bounded `domain + kind` handoff
- open [Technique Selection](TECHNIQUE_SELECTION.md) for one bounded pick by domain and current defaults
- open [Selection Patterns](SELECTION_PATTERNS.md) when adjacency, working sets, or common next moves matter more than a flat list
- open [Technique Kinds Seed](TECHNIQUE_KINDS_SEED.md) only when you need the historical wave1 note and source pointers
- open [TECHNIQUE_INDEX](../TECHNIQUE_INDEX.md) when you want the whole corpus map first
- if you are an agent and want the smallest repo-owned runtime card before expanding markdown, open [Technique Capsules](TECHNIQUE_CAPSULES.md) or `../generated/technique_capsules.min.json`

## If You Need To Understand Maturity And Review

- open [Canonical Rubric](CANONICAL_RUBRIC.md) for the current frontmatter review fields and evidence kinds
- open [Canonical Review Guide](CANONICAL_REVIEW_GUIDE.md) for `promoted -> canonical` doctrine
- open [Promotion Readiness Matrix](PROMOTION_READINESS_MATRIX.md) when the question is which `promoted` bundle can be honestly strengthened next and what proof is still missing
- open [Promotion Wave A Runbook](PROMOTION_WAVE_A_RUNBOOK.md) when the question is how to run the current first evidence-prep swarm without widening bundle meaning or faking closure
- open [External Evidence Sprint Runbook](EXTERNAL_EVIDENCE_SPRINT_RUNBOOK.md) when the question is how to run the live external-proof search over the remaining `promoted` queue without repeating stale lanes
- open [External Evidence Ledger](EXTERNAL_EVIDENCE_LEDGER.md) when the question is which external lanes have already been searched, rejected as adjacent, or honestly closed
- open [Donor Refinery Rubric](DONOR_REFINERY_RUBRIC.md) when the question is what can be extracted from an external donor without importing foreign doctrine
- open [External Import Runbook](EXTERNAL_IMPORT_RUNBOOK.md) when the question is how to take one bounded donor from triage to merge without inventing a new maintainer path
- open [Long-Gap Canon Design](LONG_GAP_CANON_DESIGN.md) when the question is why a remaining `promoted` technique still needs an external donor path
- open [Roadmap](../ROADMAP.md) when the question is which repo-only hardening, review refresh, or external evidence wave should open next
- open [External Technique Candidates](EXTERNAL_TECHNIQUE_CANDIDATES.md) when the question is which remaining external seed idea is actually worth distilling into a future bundle
- open [Cross-Layer Technique Candidates](CROSS_LAYER_TECHNIQUE_CANDIDATES.md) when the question is how the Dionysus donor-note candidate set should be filtered without widening the external-only intake surface
- open [Agon Move Technique Bridge](AGON_MOVE_TECHNIQUE_BRIDGE.md), [Agon Wave IV Technique Landing](AGON_WAVE4_TECHNIQUE_LANDING.md), and `../generated/agon_technique_binding_candidates.min.json` when the question is how Agon lawful moves request future practice without creating canonical techniques yet
- use [TECHNIQUE_INDEX](../TECHNIQUE_INDEX.md) as the live corpus split

## If You Need Derived Surfaces

- open [Repo Doc Surfaces](REPO_DOC_SURFACES.md) when the question is which authoritative repo doc to read next
- open [Technique Capsules](TECHNIQUE_CAPSULES.md) when one small runtime card is enough
- open [KAG Source Lift Guide](KAG_SOURCE_LIFT_GUIDE.md) when you need section, checklist, example, evidence-note, or bounded relation lift surfaces
- open [SHADOW_PATTERNS.md](SHADOW_PATTERNS.md) and the semantic review docs when the question is about caution seams or boundary drift rather than first-pick selection
- open [Semantic Review Guide](SEMANTIC_REVIEW_GUIDE.md) when the question is how authored review docs relate to working sets and the semantic-review manifest without becoming policy

## Current Corpus Posture

- current corpus posture is generated from `../generated/technique_catalog.min.json` and the selection surfaces, not hand-maintained here
- open `TECHNIQUE_SELECTION.md` for the live domain/kind/status split before you trust any snapshot count
- use `../generated/technique_catalog.min.json` when you need the current machine-readable corpus view
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

- run `python -m pip install -r requirements-dev.txt` once before local validation if this checkout does not already have the repo dev dependencies
- for a read-only current-state pass, run `python scripts/validate_repo.py` and `python -m unittest discover -s tests`
- open [Releasing `aoa-techniques`](RELEASING.md) for the current release-prep doctrine
- for the bounded release-prep parity path, run `python scripts/release_check.py`, then confirm `git status -sb` stayed clean
- use the individual `build_*` commands only when you are intentionally regenerating one surface family during authored edits
