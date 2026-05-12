# Promotion Evidence Runbook

This runbook records the first actionable evidence-prep wave after [Promotion Readiness Matrix](../promotion-readiness-matrix/README.md).

Use it when the question is not "which promoted bundle is generally closest to canonical?", but "how should the next swarm-backed evidence wave run without faking closure, widening bundle meaning, or colliding on shared surfaces?"

This runbook is separate from the already-landed future-import `Wave A`, `Wave B`, and `Wave C` recorded in [Roadmap](../../../../ROADMAP.md).
Those waves landed new techniques.
This runbook is about strengthening existing `promoted` bundles without flipping status before bundle-local canonical review can honestly support it.
`AOA-T-0018`, `AOA-T-0013`, `AOA-T-0034`, `AOA-T-0023`, `AOA-T-0026`, and `AOA-T-0036` have since exited this runbook through separate follow-up canonical reviews, so the active roster below now tracks the one remaining promoted candidate from the original Wave A pack.

## Wave Goal

Close the smallest honest blocker for the remaining strongest current `promoted` candidate:

- [AOA-T-0032](../../../../techniques/proof/evaluation-chain/context-report-for-ci/TECHNIQUE.md)

## Non-Goals

- no status flips before bundle-local `canonical-readiness.md` can honestly approve promotion
- no generated-surface edits while bundle-local evidence work is unresolved
- no synthetic "second context" invented from another note in this repository
- no widening a bundle just to make a candidate fit
- no multi-technique PRs

## Swarm Layout

- main agent owns:
  - wave boundaries
  - exact-fit versus overlap verdicts
  - any updates to [Promotion Readiness Matrix](../promotion-readiness-matrix/README.md)
  - any later `TECHNIQUE_INDEX.md` changes
  - generated-surface sync
  - `python -m pip install -r requirements-dev.txt`
  - final `python scripts/release_check.py`
- each worker owns:
  - one technique bundle only
  - one bounded search lane for a live second consumer or reinforcement surface
  - bundle-local edits only if exact-fit evidence is real
- workers must not edit:
  - `TECHNIQUE_INDEX.md`
  - `generated/**`
  - repo-wide semantic-review docs
  - repo-wide roadmap docs unless the main agent asks for a sync pass

## Worker Output Contract

Each worker should return one bounded result:

- `exact-fit evidence found`
  - name the source surface
  - explain why it matches the current bundle contract
  - list the bundle-local files that should change
- `adjacent but insufficient`
  - name the surface
  - explain why it is overlap, sibling, or too broad
  - leave the bundle unchanged
- `no fit found in the searched lane`
  - name the lane explored
  - restate the blocker in one sentence
  - leave the bundle unchanged

If evidence lands, the preferred local update path is:

1. update `notes/second-context-adaptation.md` when the new surface is the clearest reinforcement of bounded reuse
2. update `notes/canonical-readiness.md` to reflect the stronger evidence and the remaining gap, if any
3. update `TECHNIQUE.md` only when wording, examples, checks, or frontmatter need to reflect the new evidence honestly
4. do not add `notes/adverse-effects-review.md` unless the bundle is actually ready to become `canonical`

## Candidate Table

| technique | why now | smallest blocker | evidence that counts | not enough | likely local files |
|---|---|---|---|---|---|
| [AOA-T-0032](../../../../techniques/proof/evaluation-chain/context-report-for-ci/TECHNIQUE.md) | Clean companion to canonical `AOA-T-0012`. | One live second context beyond donor plus documentation-first adaptation. | A public repo or surface family where the same CI-facing context report exists as a real read-only artifact over composition health. | Composition-engine docs, remediation logic, provider telemetry, or a report that owns fixes rather than reporting drift. | `notes/second-context-adaptation.md`, `notes/canonical-readiness.md`, maybe example/check wording if the artifact shape becomes clearer. |

## Recommended Sequence

Run the wave in this order:

1. [AOA-T-0032](../../../../techniques/proof/evaluation-chain/context-report-for-ci/TECHNIQUE.md)

Why this order:

- `0032` still leads the report-only proof lane after the `0026` history-artifact gap and `0036` render-truth gap both closed through separate canonical reviews

## Worker Briefs

### Worker 1 - `AOA-T-0032`

Question to answer:

- is there one real CI-facing report artifact over context composition health that stays read-only and separate from composition mechanics, remediation policy, or provider telemetry?

Reject if:

- the report owns fix decisions
- the surface is really the composition engine
- the surface is only diagnostics prose with no report artifact shape

## Stop Rules

- if the candidate evidence would require new bundle meaning, stop and report rather than widening the technique
- if the candidate evidence is really a sibling technique, route it to the sibling and leave the current bundle unchanged
- if the evidence only strengthens examples but not live reuse, update examples only if the bundle meaning becomes clearer and the canonical blocker stays explicitly unresolved
- if a worker finds an exact-fit surface but the bundle still lacks clear default-use rationale, stop at evidence capture and keep the `defer` verdict
- if more than one worker needs the same donor or repo, the main agent should split ownership by target bundle and keep note edits disjoint

## Completion Criteria

Wave A is complete when each active candidate exits with one of these outcomes:

- one exact-fit reinforcement surface is found and the bundle-local notes are updated honestly
- one adjacent-but-insufficient surface is recorded and the blocker remains explicit
- one searched lane is exhausted and the next search lane is named concretely

Wave A is successful even if no status changes happen.
The goal is to reduce uncertainty and tighten evidence quality, not to force a canonical count increase.

## Wave A Pass 1 Snapshot

| technique | pass 1 result | note |
|---|---|---|
| [AOA-T-0013](../../../../techniques/instruction/instruction-surface/single-source-rule-distribution/TECHNIQUE.md) | `adjacent but insufficient` | `aoa-agents`, `aoa-routing`, and `aoa-playbooks` show projection and validation discipline, while `aoa-skills` overlay branches stay same-lineage, but none of them prove one-source -> many-managed-target instruction distribution in a second independent context. |
| [AOA-T-0018](../../../../techniques/knowledge-lift/kag-source-lift/markdown-technique-section-lift/TECHNIQUE.md) | `exact-fit evidence found` | `aoa-routing` confirms section surfaces as real `expand` targets beyond the already-strengthened `aoa-skills` and `aoa-evals` evidence. |
| [AOA-T-0034](../../../../techniques/instruction/docs-boundary/public-safe-artifact-sanitization/TECHNIQUE.md) | `adjacent but insufficient` | `aoa-playbooks` and `aoa-skills` keep sanitization as a prerequisite or origin-lineage surface, not as a second exact-fit live consumer. |
| [AOA-T-0023](../../../../techniques/execution/agent-workflows-core/stateless-single-shot-agent/TECHNIQUE.md) | `adjacent but insufficient` | checkpointed or swarm-governed flows exist, but not the same shell-side single-shot fast path. |
| [AOA-T-0032](../../../../techniques/proof/evaluation-chain/context-report-for-ci/TECHNIQUE.md) | `adjacent but insufficient` | drift reports, composition audits, and evaluation matrices exist, but not the same CI-facing context-report artifact. |
| [AOA-T-0026](../../../../techniques/history/history-artifacts/session-capture-as-repo-artifact/TECHNIQUE.md) | `adjacent but insufficient` | downstream witness and artifact-transition consumers existed locally, but not a second capture-as-artifact contract; this was later closed by the external Aider artifact-family pass below. |
| [AOA-T-0036](../../../../techniques/execution/runtime-truth-lifecycle/render-truth-before-startup/TECHNIQUE.md) | `no exact-fit local consumer found` | the searched local lane shows origin and seed-soil, but not a second independent runtime consumer. |
| [AOA-T-0026](../../../../techniques/history/history-artifacts/session-capture-as-repo-artifact/TECHNIQUE.md) | `exact-fit evidence found` | Aider plus committed public `.aider.chat.history.md` artifacts close the capture-as-project-artifact gap without widening into memory, search, or instruction policy. |
| [AOA-T-0036](../../../../techniques/execution/runtime-truth-lifecycle/render-truth-before-startup/TECHNIQUE.md) | `exact-fit evidence found` | Dockform's plan/render-before-apply seam closes the render-truth review gap without widening into lifecycle control, readiness, deployment preview, or secret-publication authority. |

Current implication:

- `AOA-T-0018`, `AOA-T-0013`, `AOA-T-0034`, `AOA-T-0023`, `AOA-T-0026`, and `AOA-T-0036` have since exited Wave A through separate follow-up canonical reviews and are now `canonical`
- `AOA-T-0032` remains `promoted` after the 2026-05-12 Stage 1 long-pass sweep over context-compiler, context-drift, fragment-assembly, dependency-graph, and repo-quality report surfaces
- do not rerun those adjacent lanes casually; reopen `AOA-T-0032` only when an artifact-first public workflow appears that compares expected source or fragment inventory against an assembled prompt/context artifact plus token deltas
- the next matrix-wide continuation should move beyond the old Wave A lead queue and use the full promotion-readiness matrix order

## Validation And Merge Discipline

- keep bundle edits narrow and local while evidence work is in flight
- merge one technique per PR
- after a merge-ready bundle exists, run `python scripts/release_check.py`
- only update shared docs such as [Promotion Readiness Matrix](../promotion-readiness-matrix/README.md) when the bundle's blocker or lane meaning actually changed

## Notes

- This runbook should stay short-lived and practical. If Wave A closes and a different roster becomes the leading queue, replace this runbook with the next promotion wave rather than stacking many active runbooks.
- `promoted` remains the correct status for every active candidate still listed in this runbook today.
