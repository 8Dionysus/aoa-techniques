# Deep Audit Roadmap

This doc records the current repo-first closure audit for `aoa-techniques`.

Use it when the question is not "which technique should I open?", but "which repo-only hardening, review refresh, or external evidence wave should open next?"

It is an audit and closure-roadmap surface. It does not change technique status, generated contracts, or validator behavior by itself.

Historical note:

- the Phase 1 and Phase 3 repo-only findings below record the baseline that drove the already-landed hardening wave
- the detailed phase findings below remain historical audit record unless a later live snapshot says otherwise
- use the `Current Live Closure Snapshot`, [Promotion Readiness Matrix](PROMOTION_READINESS_MATRIX.md), [Promotion Wave A Runbook](PROMOTION_WAVE_A_RUNBOOK.md), [External Evidence Sprint Runbook](EXTERNAL_EVIDENCE_SPRINT_RUNBOOK.md), and [External Evidence Ledger](EXTERNAL_EVIDENCE_LEDGER.md) as the live roadmap for what is still open now

## Current Live Closure Snapshot

- current verification path: `python scripts/release_check.py`
- current corpus split: `74` bundles, `25 canonical`, `49 promoted`
- repo-only hardening is largely landed; the main open work is now external-evidence execution rather than missing internal infrastructure
- recent canonical closures since the baseline below:
  - [AOA-T-0018](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md)
  - [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md)
  - [AOA-T-0034](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md)
  - [AOA-T-0023](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md)
  - [AOA-T-0028](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md)
  - [AOA-T-0031](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md)
  - [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md)
  - [AOA-T-0053](../techniques/history/local-first-session-index/TECHNIQUE.md)
- live promotion and evidence operating surfaces now are:
  - [Promotion Readiness Matrix](PROMOTION_READINESS_MATRIX.md)
  - [Promotion Wave A Runbook](PROMOTION_WAVE_A_RUNBOOK.md)
  - [External Evidence Sprint Runbook](EXTERNAL_EVIDENCE_SPRINT_RUNBOOK.md)
  - [External Evidence Ledger](EXTERNAL_EVIDENCE_LEDGER.md)
- current closest promoted queue item: [AOA-T-0032](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md)
- current external-evidence lead sprint:
  - [AOA-T-0032](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md)
  - [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md)
  - [AOA-T-0036](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md)
- latest external-evidence lane closures in that sprint:
  - [AOA-T-0032](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md): public prompt-eval CI surfaces remain adjacent and do not yet prove the same composition coverage or token-drift artifact
  - [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md): public local session-browser and session-search tools remain adjacent and do not yet prove project-scoped history artifacts
  - [AOA-T-0036](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md): public render-before-apply and dry-run surfaces remain adjacent and do not yet prove a named pre-start render-review seam over effective local runtime truth
- latest off-sprint lane closure:
  - [AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md): public transcript-log export surfaces remain adjacent and do not yet prove a structured witness trace with explicit state-delta review notes and pre-writeback summary posture
- current long-gap holds remain:
  - [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md)
  - [AOA-T-0022](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md)

## Baseline

- baseline verification path: `python -m unittest discover -s tests` and `python scripts/validate_repo.py`
- current corpus split: `34` bundles, `17 canonical`, `17 promoted`
- current promoted backlog:
  - [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md)
  - [AOA-T-0023](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md)
  - [AOA-T-0028](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md)
  - [AOA-T-0031](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md)
  - [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md)
  - [AOA-T-0018](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md)
  - [AOA-T-0020](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md)
  - [AOA-T-0022](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md)
  - [AOA-T-0027](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md)
  - [AOA-T-0024](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md)
  - [AOA-T-0025](../techniques/docs/capability-spec-versioning/TECHNIQUE.md)
  - [AOA-T-0029](../techniques/docs/nested-rule-loading/TECHNIQUE.md)
  - [AOA-T-0030](../techniques/docs/fragmented-agent-context/TECHNIQUE.md)
  - [AOA-T-0033](../techniques/docs/decision-rationale-recording/TECHNIQUE.md)
  - [AOA-T-0034](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md)
  - [AOA-T-0032](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md)
  - [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md)
- audit stance: if no structural red flag appears, prioritize semantic quality, surface coherence, governance consistency, and external dependency closure over new infrastructure

## Current Closure State

- `repo-only hardening` is landed: selection and semantic-review guides exist, release and hygiene hardening are in place, and the self-serve route is aligned around `START_HERE`
- `review refresh` is landed: [AGENT_WORKFLOWS_CORE_SEMANTIC_REVIEW.md](AGENT_WORKFLOWS_CORE_SEMANTIC_REVIEW.md) now covers `AOA-T-0001`, `AOA-T-0004`, and `AOA-T-0014`, and [SKILL_SUPPORT_SEMANTIC_REVIEW.md](SKILL_SUPPORT_SEMANTIC_REVIEW.md) is now narrowed to `AOA-T-0015`, `AOA-T-0016`, and `AOA-T-0017`
- the first external donor wave is landed:
  - `ATM10-Agent@7cf55f70badbe8b1a51e2eabbe1424f35b833dd3` strengthens `AOA-T-0005`
  - `aoa-skills@b1b3fc7b330f2fecc5412c0444bc108b4aecc67c` strengthens `AOA-T-0013` and `AOA-T-0022`
- seeded external donor intake is now explicit:
  - `ruler` is a bounded `pass` as the origin donor for `AOA-T-0013`
  - `agents-md` is a `hold because overlap` against `AOA-T-0012`
  - `n-skills` now lands the adjacent [AOA-T-0024](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) and [AOA-T-0041](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) imports, but it still does not count as live closure evidence for `AOA-T-0013`
  - `qqqa` now lands the adjacent [AOA-T-0023](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) import as a bounded shell-side fast-path technique rather than as backlog-closure evidence for an existing promoted bundle
  - `qqqa` now also lands the adjacent [AOA-T-0028](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) import as a bounded confirmation-boundary technique rather than as proof for `AOA-T-0023`
  - `agentic` now lands the adjacent [AOA-T-0025](../techniques/docs/capability-spec-versioning/TECHNIQUE.md) import as a bounded capability-contract technique rather than as proof for any current promoted backlog item
  - `getspecstory` now lands [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) and the bounded `history` domain as a local-first session-artifact contract rather than a memory-system import
  - `ruler` now also lands the adjacent [AOA-T-0027](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) import as a bounded managed-target propagation technique rather than as proof for `AOA-T-0013`
  - `n-skills` plus MCP Gateway Registry now land the adjacent [AOA-T-0042](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md) import as a bounded pre-surface source-readiness technique rather than as registry governance or security-scanning doctrine
  - `OpenMemory-Code` no longer stays fully blocked by memory-boundary overlap: [AOA-T-0038](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) now lands one bounded local-lifecycle import, while memory-substrate candidates remain held or incubating against `aoa-memo`
  - `agentwise` is a `future import candidate` with orchestration overlap and license caution, not an automatic intake
  - the latest public `agentwise` read exposes `phase-based synchronization across all agents` and `Phase Controller`, but those signals still sit inside a broader orchestration package with `Smart Model Router`, `Dynamic Task Distributor`, `SharedContextServer`, context coordination, and monitoring, so the `phase-synchronized-agent-handoff` lane remains active but not bundle-ready
  - no exact-fit seeded external donor currently displaces the open donor slots for `AOA-T-0005` or `AOA-T-0022`
- external donor intake now follows one canonical-home rule: other `aoa-*` repos may incubate or prove a pattern, but once a reusable bounded technique is extracted, it belongs in `aoa-techniques`
- clean top-4 expansion wave is now landed:
  - `ruler` now also lands the adjacent [AOA-T-0029](../techniques/docs/nested-rule-loading/TECHNIQUE.md) import as a bounded hierarchical-loading technique rather than as proof for `AOA-T-0013`
  - `agents-md` now also lands the adjacent [AOA-T-0030](../techniques/docs/fragmented-agent-context/TECHNIQUE.md) import as a bounded fragment-authoring technique rather than as proof for `AOA-T-0012`
  - `qqqa` now also lands the adjacent [AOA-T-0031](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) import as a bounded shell-composability technique rather than as proof for `AOA-T-0023`
  - `agents-md` now also lands the adjacent [AOA-T-0032](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md) import as a bounded CI-facing report technique rather than as proof for `AOA-T-0012`
  - [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) and [AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) now land the post-capture history-artifact pair around [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md), while `project_memory_bootstrap` remains outside the immediate wave as a history-overlap watch
- the remaining `13` external donor-derived seed ideas are now staged in [EXTERNAL_TECHNIQUE_CANDIDATES.md](EXTERNAL_TECHNIQUE_CANDIDATES.md) as `ready to distill here`, `future import here`, `hold because overlap`, `needs layer incubation before distillation here`, or `substrate or architecture pattern, not yet a technique`
- the `24` cross-layer candidates pulled from the Dionysus donor note are now staged in [CROSS_LAYER_TECHNIQUE_CANDIDATES.md](CROSS_LAYER_TECHNIQUE_CANDIDATES.md) as `already staged elsewhere`, `future import here`, `hold because overlap`, `needs layer incubation before distillation here`, or `substrate or architecture pattern, not yet a technique`
- the current `future import here` lane is now staged as a wave program rather than a flat queue:
  - Wave A: runtime truth and local lifecycle, now fully landed across [AOA-T-0035](../techniques/docs/profile-preset-composition/TECHNIQUE.md), [AOA-T-0036](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md), [AOA-T-0037](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md), [AOA-T-0038](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md), and [AOA-T-0039](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md), with exact candidate membership split across the external and cross-layer intake surfaces and bounded to profile composition, rendered truth, profile-scoped preflight, additive comparison discipline, and local lifecycle
  - Wave B: curated input surfaces and capability boundaries, now fully landed across [AOA-T-0040](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md), [AOA-T-0041](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md), [AOA-T-0042](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md), and [AOA-T-0043](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md), with exact candidate membership split across the external and cross-layer intake surfaces and bounded to curated discoverability, artifact boundaries, upstream shape and availability checks, and primary-vs-supporting provenance ordering
  - Wave C: history as reviewable artifact is now fully landed across [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) and [AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md), both kept artifact-first and out of memory substrate or hidden-instruction behavior
  - active narrowing lane: `phase-synchronized-agent-handoff` stays outside the wave packs until the handoff contract can name the phase boundary, handoff packet, continuation permission, and explicit stop, return, or escalation rules without widening into orchestration doctrine
- per-technique import rules remain narrow inside the wave program:
  - one technique per PR
  - external donors use the normal bounded external-import package
  - cross-layer or internal-origin candidates use donor-appropriate origin and adaptation notes without forcing external-import note names
- the remaining promoted backlog is now staged as:
  - `evidence-prep now`: `AOA-T-0018`
  - `internal-origin review path`: `AOA-T-0033`, `AOA-T-0034`
  - `external dependency first`: `AOA-T-0005`, `AOA-T-0023`, `AOA-T-0028`, `AOA-T-0031`, `AOA-T-0013`, `AOA-T-0020`, `AOA-T-0022`, `AOA-T-0027`, `AOA-T-0024`, `AOA-T-0025`, `AOA-T-0029`, `AOA-T-0030`, `AOA-T-0032`, `AOA-T-0026`

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
- `needs semantic review refresh`: none
- `candidate for bounded demotion watch`: none right now

### Wave 2B - Remaining Promoted Backlog Audit

| technique | current smallest gap | repo-local vs external gap | phase placement | next honest promotion trigger |
|---|---|---|---|---|
| [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) | one non-origin live second-context reuse beyond `atm10-agent` and the repo-local rollout sketch | external | `external dependency first` | one public second rollout record in another repo that proves the same checklist on a real new-intent extension path |
| [AOA-T-0023](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) | one live second context beyond the donor and docs-first adaptation | external | `external dependency first` | a public workflow surface that uses the same stateless, confirmation-gated single-shot fast path as real operator practice |
| [AOA-T-0028](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) | one live second context beyond the donor and docs-first adaptation | external | `external dependency first` | a public workflow surface that uses the same explicit confirmation seam before mutation as a real bounded fast path |
| [AOA-T-0031](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) | one live second context beyond the donor and docs-first adaptation | external | `external dependency first` | a public workflow surface that keeps one-shot agent work shell-composable through explicit stdin, stdout, files, or pipes without widening into a hidden long-lived session |
| [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) | one second independent live instruction-distribution context beyond the first `aoa-skills` donor; the bounded `ruler` origin package no longer counts as the missing reinforcement | external | `external dependency first` | reinforcement in `aoa-agents` or another instruction-heavy repo that keeps one-source -> many-target distribution validator-backed or generated |
| [AOA-T-0018](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) | one second independent markdown-first consumer beyond the current bridge pattern | mostly external evidence, contract already stable here | `evidence-prep now` | a second committed markdown-first consumer outside the current `aoa-skills` bridge shape |
| [AOA-T-0020](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) | one second non-eval markdown-first corpus using typed note kind and path lift | external | `external dependency first` | a committed non-eval corpus that reuses typed note-kind and note-path provenance without note-graph widening |
| [AOA-T-0022](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) | one more committed corpus beyond the first `aoa-skills` donor using the exact five-part `Risks` split | external | `external dependency first` | a committed authored bundle or corpus in another repo that reuses `Failure modes`, `Negative effects`, `Misuse patterns`, `Detection signals`, and `Mitigations` as the same contract |
| [AOA-T-0027](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) | one live second context beyond the donor and docs-first adaptation | external | `external dependency first` | a public repository or surface family that keeps one canonical skill or rule source fanning out to multiple managed agent-facing targets without turning targets into new sources of truth |
| [AOA-T-0024](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) | one live second context beyond the donor and docs-first adaptation | external | `external dependency first` | a public curated collection that mirrors upstream-owned content with explicit manifest plus adjacent provenance without claiming local source ownership |
| [AOA-T-0025](../techniques/docs/capability-spec-versioning/TECHNIQUE.md) | one live second context beyond the donor and docs-first adaptation | external | `external dependency first` | a public agent-facing surface that uses a versioned capability spec as a real contract rather than only as imported documentation |
| [AOA-T-0029](../techniques/docs/nested-rule-loading/TECHNIQUE.md) | one live second context beyond the donor and docs-first adaptation | external | `external dependency first` | a public repository or surface family that keeps hierarchical rule layers under explicit precedence while preserving one-way source ownership |
| [AOA-T-0030](../techniques/docs/fragmented-agent-context/TECHNIQUE.md) | one live second context beyond the donor and docs-first adaptation | external | `external dependency first` | a public repository that keeps agent context in bounded fragments as the real source layer before any later deterministic assembly |
| [AOA-T-0032](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md) | one live second context beyond the donor and docs-first adaptation | external | `external dependency first` | a public CI surface that reports context composition coverage or token-drift signals without widening into the composition engine or a remediation snapshot |
| [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) | one live second context beyond the donor and docs-first adaptation | external | `external dependency first` | a public repository or surface family that persists local-first session history as a real project artifact layer without widening into memory substrate or instruction policy |

Backlog verdict:

- `evidence-prep now`: `AOA-T-0018`
- `external dependency first`: `AOA-T-0005`, `AOA-T-0023`, `AOA-T-0028`, `AOA-T-0031`, `AOA-T-0013`, `AOA-T-0020`, `AOA-T-0022`, `AOA-T-0027`, `AOA-T-0024`, `AOA-T-0025`, `AOA-T-0029`, `AOA-T-0030`, `AOA-T-0032`, `AOA-T-0026`

No promoted bundle is vague anymore. The backlog is now staged by the kind of proof it still needs.

### Wave 2C - Semantic And Shadow Review Coverage Audit

Semantic review verdicts:

- `keep`: [AGENT_WORKFLOWS_CORE_SEMANTIC_REVIEW.md](AGENT_WORKFLOWS_CORE_SEMANTIC_REVIEW.md), [PUBLISHED_SUMMARY_SEMANTIC_REVIEW.md](PUBLISHED_SUMMARY_SEMANTIC_REVIEW.md), [EVALUATION_CHAIN_SEMANTIC_REVIEW.md](EVALUATION_CHAIN_SEMANTIC_REVIEW.md), [DOCS_BOUNDARY_SEMANTIC_REVIEW.md](DOCS_BOUNDARY_SEMANTIC_REVIEW.md), [INTENT_CHAIN_SEMANTIC_REVIEW.md](INTENT_CHAIN_SEMANTIC_REVIEW.md), [INSTRUCTION_SURFACE_SEMANTIC_REVIEW.md](INSTRUCTION_SURFACE_SEMANTIC_REVIEW.md), [KAG_SOURCE_LIFT_SEMANTIC_REVIEW.md](KAG_SOURCE_LIFT_SEMANTIC_REVIEW.md)
- `refresh later`: [SKILL_SUPPORT_SEMANTIC_REVIEW.md](SKILL_SUPPORT_SEMANTIC_REVIEW.md) should remain the skill-support cluster anchor, but it is still the first candidate for a future wording refresh if `0015` vs `0017` or `0016` examples drift
- `expand`: none right now

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
| `aoa-skills` | `healthy boundary` | The repo uses `aoa-skills` as evidence and consumer context for `AOA-T-0013`, `AOA-T-0016`, `AOA-T-0017`, `AOA-T-0018`, and `AOA-T-0022`, but technique meaning still stays here. |
| `aoa-evals` | `healthy boundary` | `aoa-evals` is still a donor for proof surfaces and direct relation consumption, especially for `AOA-T-0020` and `AOA-T-0021`, without shifting ownership of the technique contracts. |
| `aoa-routing` | `dependency watch` | The current `AOA-T-0021` consumer is still one-hop and bounded, but future routing work must keep relation hints away from graph or traversal creep. |
| `atm10-agent` | `dependency watch` | [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) now has a landed public donor wave here, but it still needs one non-origin live context before another honest canonical review makes sense. |

No current repo-owned doc appears to overclaim ownership of skills, evals, or routing behavior, but the promoted backlog still depends on those seams for closure.

### Wave 4C - Long-Gap Backlog Design Audit

Verdict on [LONG_GAP_CANON_DESIGN.md](LONG_GAP_CANON_DESIGN.md): `still decision-complete, now with the first donor wave landed for the current three-technique set`

Why:

- donor choice is explicit for `AOA-T-0005`, `AOA-T-0013`, and `AOA-T-0022`
- each target has one exact external contract to look for
- each target has shortcuts-to-reject written down
- each target now has one landed donor plus one clear next reinforcement trigger

No missing fields were found that would justify reopening the long-gap design doc before the next external donor wave.

## Phase 5 - Closure Program Synthesis

### Wave 5A - Immediate Repo-Only Fix Queue

Status: `completed`

The queue below is now historical and shipped:

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
| `AOA-T-0005` | open donor slot beyond `atm10-agent` | one non-origin public-safe authored new-intent rollout record over an existing intent chain | another repo-local sketch or another origin-only rollout restatement |
| `AOA-T-0023` | open donor slot beyond the current external seed import | one public workflow surface that keeps a stateless, confirmation-gated single-shot agent path as a real operator contract | shell-command convenience or general "one task at a time" prose without the same bounded single-shot discipline |
| `AOA-T-0028` | open donor slot beyond the current external seed import | one public workflow surface that keeps an explicit confirmation seam before mutation as a real bounded operator contract | generic caution wording or vague approval prompts that never act as a real gate |
| `AOA-T-0013` | `aoa-agents` or another instruction-heavy repo | one-source -> many-target managed instruction flow with validator-backed or generated drift control in a second live context; seeded donor intake now fixes `ruler` as origin, keeps `agents-md` as overlap, and lands `n-skills` as adjacent import rather than closure proof | single-target sync, hand-edited copied rule blocks, or another import-only donor note |
| `AOA-T-0018` | open donor slot | one second committed markdown-first consumer outside the current bridge pattern | metadata-spine evidence relabeled as section-lift proof |
| `AOA-T-0020` | open donor slot, but not `aoa-evals` again | one second non-eval markdown-first corpus using typed note kind and path lift | note-graph behavior, note IDs, or another near-identical eval donor |
| `AOA-T-0022` | open donor slot beyond the first `aoa-skills` bundle | one more committed authored bundle or corpus using the exact five-part `Risks` contract | adjacent caution prose, blind-spot language, or generated caution outputs |
| `AOA-T-0027` | open donor slot beyond the current external seed import | one second public managed-target fan-out that keeps one canonical skill or rule core subordinate to local source ownership | broader instruction-distribution prose mislabeled as managed-target propagation or any import that widens into MCP or role semantics |
| `AOA-T-0024` | open donor slot beyond the current external seed import | one second curated mirror context that preserves upstream ownership, explicit provenance, and repeatable local resync | local-source fan-out mislabeled as mirroring or a copy that drops explicit source attribution |
| `AOA-T-0025` | open donor slot beyond the current external seed import | one public agent-facing surface that uses a versioned capability spec as a real bounded contract | capability prose that drifts into routing policy, role registry semantics, or execution-history learning |
| `AOA-T-0026` | open donor slot beyond the current external seed import | one public repository or surface family that persists local-first session history as a reviewable project artifact | memory recall semantics, vector retrieval behavior, or treating session history as instruction authority |

### Wave 5C - Next Implementation Wave Pack

#### Repo-Only Hardening Pack

Status: `completed`

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

Status: `completed`

- goal:
  - refresh review coverage where current canonical defaults or cross-domain seams were still only implied
- constraints:
  - review docs only
  - no status flips
  - no shadow-family expansion unless a new caution-density case is proven
- target surfaces:
  - landed agent-workflows canonical-core semantic review for `AOA-T-0001`, `AOA-T-0004`, and `AOA-T-0014`
  - landed wording refresh for [SKILL_SUPPORT_SEMANTIC_REVIEW.md](SKILL_SUPPORT_SEMANTIC_REVIEW.md)
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

Status: `partially executed`

- goal:
  - reopen only the promoted techniques whose next honest step requires new donor proof, then restage the remaining backlog honestly
- constraints:
  - do not fake closure with wording-only notes
  - do not widen contracts just to manufacture evidence
  - keep `aoa-techniques` as the source of meaning
- target surfaces:
  - `AOA-T-0005`, `AOA-T-0023`, `AOA-T-0028`, `AOA-T-0031`, `AOA-T-0013`, `AOA-T-0018`, `AOA-T-0020`, `AOA-T-0022`, `AOA-T-0027`, `AOA-T-0024`, `AOA-T-0025`, `AOA-T-0029`, `AOA-T-0030`, `AOA-T-0032`, `AOA-T-0026`
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

#### Future Import Wave Program

Status: `active`

- goal:
  - turn the current `future import here` intake lane into one coherent wave program without reopening overlap, incubation, or substrate lanes
  - close Wave A as fully landed now that [AOA-T-0035](../techniques/docs/profile-preset-composition/TECHNIQUE.md), [AOA-T-0036](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md), [AOA-T-0037](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md), [AOA-T-0038](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md), and [AOA-T-0039](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) have landed, then close Wave B as fully landed through [AOA-T-0040](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md), [AOA-T-0041](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md), [AOA-T-0042](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md), and [AOA-T-0043](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md)
- swarm layout:
  - main agent owns wave boundaries, final wording, intake/roadmap sync, shared generated surfaces, and `python scripts/release_check.py`
  - each worker owns one candidate bundle at a time, plus only its `notes/`, `checks/`, and `examples/`
  - shared catalog, index, and other generated surfaces are synchronized only after a merge-ready bundle draft exists
- wave order:
  - Wave A: `profile-preset-composition`, `render-truth-before-startup`, `contextual-host-doctor`, `one-command-service-lifecycle`, `baseline-first-additive-profile-benchmarks`
  - Wave B: `skill-vs-command-boundary`, `skill-marketplace-curation`, `upstream-skill-health-checking`, `multi-source-primary-input-provenance`
  - keep `phase-synchronized-agent-handoff` as the active narrowing lane in parallel, but do not promote it into a wave yet
  - Wave C is now fully landed through [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) and [AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md), both kept behind the same seam around [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md)
- wave-specific sequencing:
  - Wave A starts with `profile-preset-composition`, then `render-truth-before-startup`, then `contextual-host-doctor`, then `one-command-service-lifecycle`, and ends with `baseline-first-additive-profile-benchmarks`
  - Wave A is now fully landed as [AOA-T-0035](../techniques/docs/profile-preset-composition/TECHNIQUE.md), [AOA-T-0036](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md), [AOA-T-0037](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md), [AOA-T-0038](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md), and [AOA-T-0039](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md); keep Wave A closed while later sequencing stays on the narrowing lane
  - Wave B starts with `skill-vs-command-boundary`, then `skill-marketplace-curation`, then `upstream-skill-health-checking`, and ends with `multi-source-primary-input-provenance`
  - Wave B first step is now landed as [AOA-T-0040](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md), its external curation anchor now lands as [AOA-T-0041](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md), its source-readiness sibling now lands as [AOA-T-0042](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md), and its provenance-ordering close-out now lands as [AOA-T-0043](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md); keep the next sequencing on the narrowing lane instead of widening Wave B into propagation, marketplace doctrine, monitoring, or bridge architecture
  - Wave C begins with `versionable-session-transcripts`, landed as [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md), and closes with `witness-trace-as-reviewable-artifact`, landed as [AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md), both kept behind the export/review-only seam rather than widening into witness runtime or memory behavior
  - if any candidate starts needing launcher, registry, routing, or graph doctrine to explain its value, it moves out of the current wave instead of widening the wave
- gating rules:
  - Wave C must stay artifact-first and must not widen into memory substrate, recall, or hidden instruction authority
  - [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) keeps ownership of session capture, project-scoped persistence, and local-first artifact availability itself
  - [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) now owns the post-capture transcript-shaping sibling because the donor shows selected conversations saved into one Markdown document, review or edit before saving, and timestamped transcript artifacts ready for code review or knowledge sharing
  - any future transcript-history sibling still fails the seam if its value proposition is merely `save sessions locally` instead of shaping or packaging an already-saved transcript for review
  - [AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) now owns export/review/citation discipline for one structured witness trace plus summary without becoming a new memory-object kind
  - any future witness-history sibling still fails the seam if it needs runtime witness generation, memory writeback, or future-instruction derivation to explain its value
  - the narrowing lane must not move forward until the handoff contract can name the phase boundary, handoff packet, continuation permission, and stop, return, or escalation rule explicitly
  - donor evidence refresh checked on `2026-03-23` still reaches only a partial phase-boundary signal: the public GitHub README and `agentwise-docs.vercel.app` home keep foregrounding orchestration, routing, context sharing, and monitoring rather than one bounded handoff contract
  - public GitHub README and docs home still do not expose `checkpoint`, `handoff`, or `packet`, so the packet shape, continuation permission, and stop/return/escalation rule remain implicit inside the larger `agentwise` orchestration package and the lane stays closed for drafting
  - `phase-synchronized-agent-handoff` stays out of Wave A and Wave B until those readiness criteria are met
- narrowing-lane readiness fields:
  - minimum packet shape: `phase/checkpoint`, `done`, `blocked`, `next action`, `next owner`, `entry/exit condition`, and `stop/return/escalation`
- what must stay unchanged:
  - verdict classes and unrelated hold, incubation, and substrate placements in the intake surfaces
  - one-technique-per-PR import discipline
  - existing overlap, incubation, and substrate holds

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
