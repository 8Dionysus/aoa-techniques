# Deep Audit Roadmap

This doc records the current repo-first closure audit for `aoa-techniques`.

Use it when the question is not "which technique should I open?", but "which repo-only hardening, review refresh, or external evidence wave should open next?"

It is an audit and closure-roadmap surface. It does not change technique status, generated contracts, or validator behavior by itself.

## Baseline

- baseline verification path: `python -m unittest discover -s tests` and `python scripts/validate_repo.py`
- current corpus split: `22` bundles, `17 canonical`, `5 promoted`
- current promoted backlog:
  - [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md)
  - [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md)
  - [AOA-T-0018](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md)
  - [AOA-T-0020](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md)
  - [AOA-T-0022](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md)
- audit stance: if no structural red flag appears, prioritize semantic quality, surface coherence, governance consistency, and external dependency closure over new infrastructure

## Finding Classes

- `repo-only closure`
  - can be fixed inside this repository without new donor evidence
- `review refresh`
  - needs a new or refreshed authored review surface, but still stays inside this repository
- `external dependency`
  - needs a committed donor or consumer outside this repository
- `long-gap design`
  - already depends on a future external product surface and should not be faked by wording

## Phase 1 - Structural Integrity Audit

### Wave 1A - Source/Generated Contract Audit

| family | authoritative source | reader companion | derived manifest or payload | builder and validator coverage | audit verdict |
|---|---|---|---|---|---|
| technique catalog / selection | `techniques/**/TECHNIQUE.md`, frontmatter, `relations`, review-backed working-set specs in [scripts/validate_repo.py](../scripts/validate_repo.py) | [TECHNIQUE_SELECTION.md](TECHNIQUE_SELECTION.md), [SELECTION_PATTERNS.md](SELECTION_PATTERNS.md), [SHADOW_PATTERNS.md](SHADOW_PATTERNS.md) | `generated/technique_catalog.json`, `generated/technique_catalog.min.json` | `build_catalog.py`, `validate_catalogs`, `validate_selection_surface`, navigation-spec tests in [tests/test_validate_repo.py](../tests/test_validate_repo.py) | `repo-only closure`: strong generated parity and tests, but no single authored contract guide for the selection family |
| capsules | `TECHNIQUE.md` `summary` plus fixed bounded sections, defined in [TECHNIQUE_CAPSULE_GUIDE.md](TECHNIQUE_CAPSULE_GUIDE.md) | [TECHNIQUE_CAPSULES.md](TECHNIQUE_CAPSULES.md) | `generated/technique_capsules.json`, `generated/technique_capsules.min.json` | `build_capsules.py`, `validate_capsules`, multiple capsule regression tests | `keep`: family is 1:1 mapped and well locked |
| repo-doc surfaces | bounded source set defined in [REPO_DOC_SURFACE_LIFT_GUIDE.md](REPO_DOC_SURFACE_LIFT_GUIDE.md) | [REPO_DOC_SURFACES.md](REPO_DOC_SURFACES.md) | `generated/repo_doc_surface_manifest.json`, `generated/repo_doc_surface_manifest.min.json` | `build_repo_doc_surface_manifest.py`, `validate_repo_doc_surface_manifests`, `validate_repo_doc_navigation_specs` | `repo-only closure`: source/reader/manifest contract is clear, but [docs/README.md](README.md) still describes the source set as `10` docs while the current contract is `11` |
| section / checklist / example / evidence-note readers | authored markdown bundles plus bounded lift guides | [TECHNIQUE_SECTIONS.md](TECHNIQUE_SECTIONS.md), [TECHNIQUE_CHECKLISTS.md](TECHNIQUE_CHECKLISTS.md), [TECHNIQUE_EXAMPLES.md](TECHNIQUE_EXAMPLES.md), [EVIDENCE_NOTE_SURFACES.md](EVIDENCE_NOTE_SURFACES.md) | `generated/technique_section_manifest.json`, `generated/technique_checklist_manifest.json`, `generated/technique_example_manifest.json`, `generated/technique_evidence_note_manifest.json` | dedicated `build_*` scripts plus manifest parity validators and tests | `keep`: the family already has explicit lift guides and bounded manifests |
| semantic review manifests | authored semantic review docs, working-set specs in [scripts/validate_repo.py](../scripts/validate_repo.py) | review docs themselves plus [SELECTION_PATTERNS.md](SELECTION_PATTERNS.md) working sets | `generated/semantic_review_manifest.json`, `generated/semantic_review_manifest.min.json` | `build_semantic_review_manifest.py`, `validate_semantic_review_manifests`, working-set tests | `review refresh`: manifest coverage exists, but there is no single authored contract guide for the semantic-review family |
| shadow review manifests | authored shadow review docs plus canonical `adverse_effects_review` notes, explained in [TECHNIQUE_SHADOW_GUIDE.md](TECHNIQUE_SHADOW_GUIDE.md) | [SHADOW_PATTERNS.md](SHADOW_PATTERNS.md) plus the shadow review docs | `generated/shadow_review_manifest.json`, `generated/shadow_review_manifest.min.json` | `build_shadow_review_manifest.py`, `validate_shadow_review_manifests`, shadow-spec tests | `keep`: guide, manifest, reader, and validator parity are already aligned |

Wave 1A backlog:

- `repo-only closure`: add one authored selection-family contract guide so the current contract is not split between generated readers and validator specs.
- `review refresh`: add one authored semantic-review family contract guide so the manifest family does not rely on code plus pilot docs alone.
- `repo-only closure`: fix the `10` vs `11` authoritative repo-doc count drift in [docs/README.md](README.md).

### Wave 1B - Validation And Release Hardening Audit

Findings:

- [scripts/release_check.py](../scripts/release_check.py) covers every current repo-owned builder family, then runs tests and [scripts/validate_repo.py](../scripts/validate_repo.py). No hidden generated family was found outside that path.
- The release path is structurally sound: builder order is explicit, worktree stabilization is checked, and a clean repo must stay diff-clean after the bounded release pass.
- `repo-only closure`: dirty-worktree drift detection is weaker than clean-worktree drift detection. The current stabilization logic compares `git status --porcelain` snapshots, so a tracked file that was already `M` can still change content without changing the snapshot shape.
- `repo-only closure`: there is no targeted regression test for the dirty-worktree masking case in [tests/test_validate_repo.py](../tests/test_validate_repo.py).
- `repo-only closure`: release doctrine is still described in more than one place. [docs/RELEASING.md](RELEASING.md) treats `python scripts/release_check.py` as the bounded path, while [CONTRIBUTING.md](../CONTRIBUTING.md) still only names `unittest` plus `validate_repo.py`.
- `repo-only closure`: generated parity is well locked, but route prose is not. The stale `10` vs `11` repo-doc wording survived because current tests do not lock that docs-map claim.

Wave 1B backlog:

- align [CONTRIBUTING.md](../CONTRIBUTING.md) with the current release-check doctrine without removing the explicit lower-level commands.
- harden [scripts/release_check.py](../scripts/release_check.py) so dirty tracked files cannot hide generated drift.
- add one regression test for dirty-worktree stabilization behavior.
- add one small regression lock for repo-doc source-count wording so route prose does not drift silently after repo-doc family changes.

### Wave 1C - Public Hygiene And Safety Audit

Findings:

- public-hygiene scanning already covers root markdown plus `.github`, `docs`, `generated`, `techniques`, and `templates`.
- the current scanner correctly blocks obvious local paths, loopback references, token markers, and private-key markers on public surfaces.
- `repo-only closure`: the scanner does not currently block arbitrary internal-only HTTPS URLs. That is weaker than the public-hygiene doctrine in [AGENTS.md](../AGENTS.md) and [SECURITY.md](../SECURITY.md), which both forbid internal-only URLs on public surfaces.
- `repo-only closure`: the current root-file scan only covers root `.md` files. If a future public root surface appears as JSON, YAML, or another text format outside the listed scan directories, it would be missed.
- `keep with wording follow-up`: the distinction between public-safe wording and safe generated export is present in [CANONICAL_RUBRIC.md](CANONICAL_RUBRIC.md), but it is still spread across several docs rather than summarized in one hygiene-oriented place.

Wave 1C backlog:

- harden [scripts/validate_repo.py](../scripts/validate_repo.py) against internal-only public URLs.
- document the current root-scan limitation so future public surfaces do not quietly escape hygiene checks.
- add one short hygiene note to the repo-only hardening pack instead of creating a new doc family.

## Phase 2 - Corpus Meaning Audit

### Wave 2A - Canonical Bundle Quality Audit

| cluster | techniques | audit verdict | notes |
|---|---|---|---|
| agent-workflows canonical core | `AOA-T-0001`, `AOA-T-0004`, `AOA-T-0014` | `clear` | [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) has a clear default-use rationale and a bounded adverse-effects note, [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) stays distinct from rollout extension work, and [AOA-T-0014](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) remains a bounded execution slice technique. The main gap is review coverage, not bundle quality. |
| docs canonical core | `AOA-T-0002`, `AOA-T-0009`, `AOA-T-0012`, `AOA-T-0016` | `clear with one wording watch` | [DOCS_BOUNDARY_SEMANTIC_REVIEW.md](DOCS_BOUNDARY_SEMANTIC_REVIEW.md) keeps `0002` vs `0009` clear; [INSTRUCTION_SURFACE_SEMANTIC_REVIEW.md](INSTRUCTION_SURFACE_SEMANTIC_REVIEW.md) keeps `0012` distinct from `0013`; [SKILL_SUPPORT_SEMANTIC_REVIEW.md](SKILL_SUPPORT_SEMANTIC_REVIEW.md) explicitly watches [AOA-T-0016](../techniques/docs/bounded-context-map/TECHNIQUE.md) for drift into generic architecture formalism. |
| evaluation canonical core | `AOA-T-0003`, `AOA-T-0006`, `AOA-T-0007`, `AOA-T-0008`, `AOA-T-0010`, `AOA-T-0011`, `AOA-T-0015` | `clear with two watch seams` | [PUBLISHED_SUMMARY_SEMANTIC_REVIEW.md](PUBLISHED_SUMMARY_SEMANTIC_REVIEW.md) keeps `0006/0008/0010/0011` distinct and explicitly watches [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) for package-appendix drift. [EVALUATION_CHAIN_SEMANTIC_REVIEW.md](EVALUATION_CHAIN_SEMANTIC_REVIEW.md) keeps `0003` vs `0007` clear and watches `0007` adjacency to `0006`. [SKILL_SUPPORT_SEMANTIC_REVIEW.md](SKILL_SUPPORT_SEMANTIC_REVIEW.md) keeps [AOA-T-0015](../techniques/evaluation/contract-test-design/TECHNIQUE.md) distinct from `0017`, but that seam remains the strongest evaluation watch point. |
| KAG canon pair | `AOA-T-0019`, `AOA-T-0021` | `clear` | [KAG_SOURCE_LIFT_SEMANTIC_REVIEW.md](KAG_SOURCE_LIFT_SEMANTIC_REVIEW.md) keeps [AOA-T-0019](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) narrow as the metadata spine and [AOA-T-0021](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) narrow as one-hop direct relation hints. The active watch seams are schema creep and graph creep, not status weakness. |
| recent canon additions | `AOA-T-0016`, `AOA-T-0017` | `clear` | Both bundles now have explicit approval verdicts plus bounded adverse-effects notes. The active risk is wording drift back toward generic architecture formalism for `0016` and generic "better tests" language for `0017`, not lack of evidence. |

Bundle-level result:

- `clear`: `AOA-T-0001`, `AOA-T-0002`, `AOA-T-0003`, `AOA-T-0004`, `AOA-T-0006`, `AOA-T-0007`, `AOA-T-0008`, `AOA-T-0009`, `AOA-T-0010`, `AOA-T-0012`, `AOA-T-0014`, `AOA-T-0016`, `AOA-T-0017`, `AOA-T-0019`, `AOA-T-0021`
- `tighten wording watch`: `AOA-T-0011`, `AOA-T-0015`
- `needs semantic review refresh`: no canonical bundle requires immediate bundle-local refresh, but the agent-workflows canonical core lacks a dedicated review surface
- `candidate for bounded demotion watch`: none right now

### Wave 2B - Remaining Promoted Backlog Audit

| technique | current smallest gap | repo-local vs external gap | phase placement | next honest promotion trigger |
|---|---|---|---|---|
| [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) | one live second-context reuse beyond the repo-local rollout sketch | external | `long-gap design only` | one public second rollout record in `atm10-agent` that proves the same checklist on a real new-intent extension path |
| [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) | one real one-source -> many-target managed instruction flow | external | `long-gap design only` | validator-backed or generated one-source -> many-target distribution in `aoa-skills`, then later reinforcement in `aoa-agents` |
| [AOA-T-0018](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) | one second independent markdown-first consumer beyond the current bridge pattern | mostly external evidence, contract already stable here | `evidence-prep now` | a second committed markdown-first consumer outside the current `aoa-skills` bridge shape |
| [AOA-T-0020](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) | one second non-eval markdown-first corpus using typed note kind and path lift | external | `external dependency first` | a committed non-eval corpus that reuses typed note-kind and note-path provenance without note-graph widening |
| [AOA-T-0022](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) | one second committed corpus using the exact five-part `Risks` split | external | `long-gap design only` | a committed authored bundle in another repo that reuses `Failure modes`, `Negative effects`, `Misuse patterns`, `Detection signals`, and `Mitigations` as the same contract |

Backlog verdict:

- `evidence-prep now`: `AOA-T-0018`
- `external dependency first`: `AOA-T-0020`
- `long-gap design only`: `AOA-T-0005`, `AOA-T-0013`, `AOA-T-0022`

No promoted bundle is vague anymore. The backlog is now staged by the kind of proof it still needs.

### Wave 2C - Semantic And Shadow Review Coverage Audit

Semantic review verdicts:

- `keep`: [PUBLISHED_SUMMARY_SEMANTIC_REVIEW.md](PUBLISHED_SUMMARY_SEMANTIC_REVIEW.md), [EVALUATION_CHAIN_SEMANTIC_REVIEW.md](EVALUATION_CHAIN_SEMANTIC_REVIEW.md), [DOCS_BOUNDARY_SEMANTIC_REVIEW.md](DOCS_BOUNDARY_SEMANTIC_REVIEW.md), [INTENT_CHAIN_SEMANTIC_REVIEW.md](INTENT_CHAIN_SEMANTIC_REVIEW.md), [INSTRUCTION_SURFACE_SEMANTIC_REVIEW.md](INSTRUCTION_SURFACE_SEMANTIC_REVIEW.md), [KAG_SOURCE_LIFT_SEMANTIC_REVIEW.md](KAG_SOURCE_LIFT_SEMANTIC_REVIEW.md)
- `refresh later`: [SKILL_SUPPORT_SEMANTIC_REVIEW.md](SKILL_SUPPORT_SEMANTIC_REVIEW.md) should remain the skill-support cluster anchor, but it now carries most of the cross-domain pressure and is the first candidate for a future wording refresh if `0015` vs `0017` or `0016` examples drift
- `expand`: the main non-reviewed collision zone is the agent-workflows canonical core around `AOA-T-0001`, `AOA-T-0004`, and `AOA-T-0014`

Shadow review verdicts:

- `keep`: [PUBLISHED_SUMMARY_SHADOW_REVIEW.md](PUBLISHED_SUMMARY_SHADOW_REVIEW.md) and [EVALUATION_CHAIN_SHADOW_REVIEW.md](EVALUATION_CHAIN_SHADOW_REVIEW.md) are coherent and bounded
- `do not expand yet`: no additional canonical family currently shows the same caution-density that justified repo-level shadow lookup for the two existing clusters
- `accepted non-reviewed zone`: docs-boundary and skill-support clusters still look better served by bundle-local `Risks` plus `adverse-effects-review` notes than by a new repo-level shadow family

## Phase 3 - Surface Usability Audit

### Wave 3A - Self-Serve Reader Journey Audit

| journey | current verdict | notes |
|---|---|---|
| `README -> START_HERE -> selection/index -> one technique` | `keep` | The shortest reader path is clear and bounded. [docs/START_HERE.md](START_HERE.md) now does the right first-hop routing job. |
| `README -> START_HERE -> repo-doc surfaces -> release/governance` | `keep with route-friction note` | The path works, but [docs/README.md](README.md) still duplicates some `START_HERE` routing instead of clearly behaving as the deeper map. |
| `START_HERE -> KAG/source-lift guides -> generated readers` | `keep` | [KAG_SOURCE_LIFT_GUIDE.md](KAG_SOURCE_LIFT_GUIDE.md) is still the right contract anchor and keeps reader surfaces bounded. |
| `selection -> inspect -> expand -> object use` | `keep` | The runtime contract is explicit in [docs/START_HERE.md](START_HERE.md) and still matches the generated selection surfaces. |

Route-friction findings:

- `repo-only closure`: [README.md](../README.md) still routes new readers through [docs/README.md](README.md) before the first concrete technique, even though [START_HERE.md](START_HERE.md) now owns the primary branching logic.
- `repo-only closure`: [docs/README.md](README.md) still contains one stale repo-doc count claim and a mild loop in its `New reader path`, which starts at `Start Here` and then routes back to `README`.
- `repo-only closure`: the `KAG / lift path` in [docs/README.md](README.md) is still too long for a shortest-path journey because it mixes guides, readers, manifests, and reusable lift bundles before naming one bounded next surface.
- `repo-only closure`: [README.md](../README.md) still has one dense `Deeper routes` bullet that lumps repo-doc routing, reader families, manifests, guides, and reusable lift bundles together.
- `repo-only closure`: the audit and closure roadmap itself is not yet part of the documented maintainer route.

### Wave 3B - Surface Family Vocabulary Audit

Findings:

- `keep`: [TECHNIQUE_CAPSULE_GUIDE.md](TECHNIQUE_CAPSULE_GUIDE.md), [REPO_DOC_SURFACE_LIFT_GUIDE.md](REPO_DOC_SURFACE_LIFT_GUIDE.md), [TECHNIQUE_SHADOW_GUIDE.md](TECHNIQUE_SHADOW_GUIDE.md), and several KAG guides already use the stable vocabulary of `authoritative source`, `reader companion`, `derived manifest`, and `what it must not become`.
- `repo-only closure`: [docs/README.md](README.md) and [README.md](../README.md) still describe some families in a more ad hoc route-map voice rather than the same stable contract vocabulary.
- `review refresh`: the semantic-review family has no authored contract guide, so its vocabulary currently lives in individual pilot docs and validator code rather than one stable description.

### Wave 3C - Selector And Reader Boundedness Audit

Findings:

- [SELECTION_PATTERNS.md](SELECTION_PATTERNS.md) stays bounded to direct relations, working sets, and common moves. No scoring, ranking, or multi-hop drift found.
- [SHADOW_PATTERNS.md](SHADOW_PATTERNS.md) stays canonical-only and lookup-only. No policy-engine drift found.
- [REPO_DOC_SURFACES.md](REPO_DOC_SURFACES.md) stays a bounded routing aid and does not claim deeper-guide authority.
- [KAG_SOURCE_LIFT_GUIDE.md](KAG_SOURCE_LIFT_GUIDE.md) still explicitly defers graph inference, scoring, rationale layers, and policy routing.
- overall verdict: `keep`

No selector-like surface currently needs a boundedness rollback.

## Phase 4 - Governance And Boundary Audit

### Wave 4A - Governance Surface Consistency Audit

Findings:

- `keep`: [AGENTS.md](../AGENTS.md), [README.md](../README.md), [docs/START_HERE.md](START_HERE.md), [docs/RELEASING.md](RELEASING.md), [docs/CANONICAL_RUBRIC.md](CANONICAL_RUBRIC.md), and [docs/CANONICAL_REVIEW_GUIDE.md](CANONICAL_REVIEW_GUIDE.md) are broadly coherent about what the repo owns and how promotion works.
- `repo-only closure`: [CONTRIBUTING.md](../CONTRIBUTING.md) still points contributors to `unittest` plus `validate_repo.py` without also naming [scripts/release_check.py](../scripts/release_check.py) as the bounded release-prep path now used elsewhere.
- `repo-only closure`: [docs/README.md](README.md) still says the repo-doc surface manifest lifts `10` authoritative docs/status files, while [REPO_DOC_SURFACE_LIFT_GUIDE.md](REPO_DOC_SURFACE_LIFT_GUIDE.md) and [REPO_DOC_SURFACES.md](REPO_DOC_SURFACES.md) already use `11`.

Overall verdict: `coherent with a small docs-path cleanup queue`

### Wave 4B - Cross-Repo Boundary Seam Audit

| seam | audit verdict | note |
|---|---|---|
| `aoa-skills` | `healthy boundary` | The repo uses `aoa-skills` as evidence and consumer context for `AOA-T-0016`, `AOA-T-0017`, and `AOA-T-0018`, but technique meaning still stays here. |
| `aoa-evals` | `healthy boundary` | `aoa-evals` is still a donor for proof surfaces and direct relation consumption, especially for `AOA-T-0020` and `AOA-T-0021`, without shifting ownership of the technique contracts. |
| `aoa-routing` | `dependency watch` | The current `AOA-T-0021` consumer is still one-hop and bounded, but future routing work must keep relation hints away from graph or traversal creep. |
| `atm10-agent` | `future donor wave required` | [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) still needs a real second rollout record here before another honest canonical review makes sense. |

No current repo-owned doc appears to overclaim ownership of skills, evals, or routing behavior, but the promoted backlog still depends on those seams for closure.

### Wave 4C - Long-Gap Backlog Design Audit

Verdict on [LONG_GAP_CANON_DESIGN.md](LONG_GAP_CANON_DESIGN.md): `decision-complete for the current three-technique long-gap set`

Why:

- donor choice is explicit for `AOA-T-0005`, `AOA-T-0013`, and `AOA-T-0022`
- each target has one exact external contract to look for
- each target has shortcuts-to-reject written down
- each target has a clear future donor wave trigger

No missing fields were found that would justify reopening the long-gap design doc before the next external donor wave.

## Phase 5 - Closure Program Synthesis

### Wave 5A - Immediate Repo-Only Fix Queue

Open this queue in strict order:

1. `docs/governance wording hardening`
   - target surfaces:
     - [docs/README.md](README.md)
     - [CONTRIBUTING.md](../CONTRIBUTING.md)
     - route references from [docs/START_HERE.md](START_HERE.md)
   - close:
     - `10` vs `11` repo-doc source-count drift
     - missing mention of `python scripts/release_check.py` in contribution guidance
     - missing route to this audit roadmap
2. `selection and semantic-review contract hardening`
   - target surfaces:
     - new authored selection-family guide
     - new authored semantic-review family guide
     - minimal docs-map links to those guides
   - close:
     - missing authored contract guide for the selection family
     - missing authored contract guide for the semantic-review manifest family
3. `validator and test hardening`
   - target surfaces:
     - [scripts/validate_repo.py](../scripts/validate_repo.py)
     - [tests/test_validate_repo.py](../tests/test_validate_repo.py)
   - close:
     - internal-only public URL blind spot
     - root non-markdown public-surface blind spot
     - missing regression lock on repo-doc source-count wording

### Wave 5B - External Evidence Dependency Queue

| target technique | external repo | exact proof surface needed | what must not be faked by wording |
|---|---|---|---|
| `AOA-T-0005` | `atm10-agent` | one second public-safe authored new-intent rollout record over an existing intent chain | another repo-local sketch or private rollout note |
| `AOA-T-0013` | `aoa-skills`, then `aoa-agents` | one-source -> many-target managed instruction flow with validator-backed or generated drift control | single-target sync or hand-edited copied rule blocks |
| `AOA-T-0018` | open donor slot | one second committed markdown-first consumer outside the current bridge pattern | metadata-spine evidence relabeled as section-lift proof |
| `AOA-T-0020` | open donor slot, but not `aoa-evals` again | one second non-eval markdown-first corpus using typed note kind and path lift | note-graph behavior, note IDs, or another near-identical eval donor |
| `AOA-T-0022` | `aoa-skills` | one committed authored bundle using the exact five-part `Risks` contract | adjacent caution prose, blind-spot language, or generated caution outputs |

### Wave 5C - Next Implementation Wave Pack

#### Repo-Only Hardening Pack

- goal:
  - close route drift, governance wording drift, and validator hygiene blind spots without touching technique statuses
- constraints:
  - no new technique IDs
  - no status changes
  - no new generated family
- target surfaces:
  - [docs/README.md](README.md)
  - [CONTRIBUTING.md](../CONTRIBUTING.md)
  - one authored selection-family guide
  - one authored semantic-review family guide
  - [scripts/validate_repo.py](../scripts/validate_repo.py)
  - [tests/test_validate_repo.py](../tests/test_validate_repo.py)
- tests and validation:
  - `python -m unittest discover -s tests`
  - `python scripts/validate_repo.py`
  - `python scripts/release_check.py` only if generated-family parity is touched
- merge order:
  - docs wording first
  - guides second
  - validator and tests last
- what must stay unchanged:
  - corpus split
  - generated surface shapes
  - review-backed working-set semantics

#### Review Coverage Refresh Pack

- goal:
  - refresh review coverage where current canonical defaults or cross-domain seams are still only implied
- constraints:
  - review docs only
  - no status flips
  - no shadow-family expansion unless a new caution-density case is proven
- target surfaces:
  - new agent-workflows canonical-core semantic review for `AOA-T-0001`, `AOA-T-0004`, and `AOA-T-0014`
  - optional wording refresh for [SKILL_SUPPORT_SEMANTIC_REVIEW.md](SKILL_SUPPORT_SEMANTIC_REVIEW.md)
- tests and validation:
  - `python scripts/build_semantic_review_manifest.py` if a new review doc is added
  - `python -m unittest discover -s tests`
  - `python scripts/validate_repo.py`
- merge order:
  - author review doc
  - sync semantic-review manifest
  - validate working-set and navigation parity
- what must stay unchanged:
  - technique bundle meaning
  - shadow-review scope
  - selection engine boundedness

#### External Evidence Pack

- goal:
  - reopen only the promoted techniques whose next honest step requires new donor proof
- constraints:
  - do not fake closure with wording-only notes
  - do not widen contracts just to manufacture evidence
  - keep `aoa-techniques` as the source of meaning
- target surfaces:
  - `AOA-T-0005`, `AOA-T-0013`, `AOA-T-0018`, `AOA-T-0020`, `AOA-T-0022`
  - donor repos named in [LONG_GAP_CANON_DESIGN.md](LONG_GAP_CANON_DESIGN.md) or the open evidence-prep slots above
- tests and validation:
  - donor-repo native validation first
  - then reopen the corresponding notes and reviews in `aoa-techniques`
- merge order:
  - donor evidence first
  - then reopen `aoa-techniques`
  - then run the full `aoa-techniques` validation path
- what must stay unchanged:
  - no schema or frontmatter expansion
  - no graph inference or policy routing creep
  - no status changes without explicit new evidence and review

## Audit Exit Criteria

This audit is complete when future implementation work can route every finding into exactly one of these tracks:

- `repo-only closure`
- `review refresh`
- `external dependency`
- `long-gap design`

Current outcome:

- no structural red flag requiring emergency rollback
- one clear repo-only hardening queue
- one clear review-refresh queue
- one clear external dependency queue
- one already decision-complete long-gap design surface
