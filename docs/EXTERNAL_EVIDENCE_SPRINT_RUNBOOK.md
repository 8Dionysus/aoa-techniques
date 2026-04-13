# External Evidence Sprint Runbook

This runbook records the live maintainer path for external-evidence work over the remaining `promoted` queue in `aoa-techniques`.

Use it when the question is not "which promoted bundle is generally closest to `canonical`?", but "how should the next external proof sprint run without repeating stale searches, widening bundle meaning, or faking closure?"

See also:
- [Promotion Readiness Matrix](PROMOTION_READINESS_MATRIX.md)
- [Promotion Wave A Runbook](PROMOTION_WAVE_A_RUNBOOK.md)
- [External Evidence Ledger](EXTERNAL_EVIDENCE_LEDGER.md)
- [Long-Gap Canon Design](LONG_GAP_CANON_DESIGN.md)
- [Roadmap](../ROADMAP.md)
- [External Import Runbook](EXTERNAL_IMPORT_RUNBOOK.md)

## When To Open This

Open this runbook only when all of the following are already true:

- the bundle is already `promoted`
- the bundle already has the normal local note package for its current maturity claim
- the remaining blocker is external evidence, not missing bundle structure
- the next move should reduce uncertainty even if no status changes happen

If the problem is really donor intake or a new extraction, use [External Import Runbook](EXTERNAL_IMPORT_RUNBOOK.md) instead.

## Non-Goals

- no status flips unless bundle-local notes can honestly support them
- no donor-import workflow inside this runbook
- no bundle widening just to fit a tempting external surface
- no repeated searching of a lane that is already logged as exhausted without a new signal
- no multi-technique promotion PRs

## Current Sprint Order

Run the external evidence queue in this order:

1. lead queue:
   - [AOA-T-0032](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md)
   - [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md)
   - [AOA-T-0036](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md)
2. shell-agent follow-through:
   - [AOA-T-0028](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md)
   - [AOA-T-0031](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md)
3. markdown-first and fresh-extraction follow-through:
   - [AOA-T-0020](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md)
   - [AOA-T-0046](../techniques/docs/repo-doc-surface-lift/TECHNIQUE.md)
   - [AOA-T-0047](../techniques/docs/github-review-template-lift/TECHNIQUE.md)
   - [AOA-T-0048](../techniques/docs/semantic-review-surface-lift/TECHNIQUE.md)
4. long-gap holds:
   - [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md)
   - [AOA-T-0022](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md)

Why this order:

- `AOA-T-0032`, `AOA-T-0026`, and `AOA-T-0036` are the current closest live queue items
- `AOA-T-0028` and `AOA-T-0031` share a tighter shell-agent search shape and can reuse operator search muscle once the lead trio is clearer
- `AOA-T-0020` plus `AOA-T-0046` through `AOA-T-0048` should not reopen until a real non-origin consumer exists
- `AOA-T-0005` and `AOA-T-0022` stay long-gap by design and should not consume the same sprint energy as the lead queue

## Swarm Layout

- main agent owns:
  - sprint order
  - exact-fit versus overlap verdicts
  - updates to [Promotion Readiness Matrix](PROMOTION_READINESS_MATRIX.md)
  - updates to [External Evidence Ledger](EXTERNAL_EVIDENCE_LEDGER.md)
  - any later sync to [Roadmap](../ROADMAP.md)
  - `python -m pip install -r requirements-dev.txt`
  - final `python scripts/release_check.py`
- each worker owns:
  - one technique bundle at a time
  - one bounded search lane
  - bundle-local note edits only when exact-fit evidence is real
- workers must not edit:
  - `TECHNIQUE_INDEX.md`
  - `generated/**`
  - repo-wide semantic-review docs
  - repo-wide roadmap or queue docs unless the main agent requests the sync

## Search Order

1. Read the bundle first.
   - open `TECHNIQUE.md`
   - open `notes/canonical-readiness.md`
   - open `notes/second-context-adaptation.md` when it exists
2. Check shared search memory.
   - open [Promotion Readiness Matrix](PROMOTION_READINESS_MATRIX.md)
   - open [External Evidence Ledger](EXTERNAL_EVIDENCE_LEDGER.md)
   - do not rerun a false-positive lane unless a new public signal exists
3. Search the exact object layer first.
   - look for the same reusable object in a second real public consumer
   - prefer live artifacts, workflows, or repo-owned surfaces over marketing or architectural prose
4. Reject adjacent fits explicitly.
   - if the surface is really a sibling technique, name it and stop
   - if the surface widens into product, platform, or orchestration doctrine, stop
5. Update locally only after the evidence is real.
   - update bundle-local notes first
   - delay any status discussion until the bundle can honestly carry it

## Evidence Verdict Contract

Each search lane should end with one bounded result:

- `exact-fit evidence found`
  - name the second consumer
  - explain why it matches the current bundle contract
  - list the bundle-local files that should change
- `adjacent but insufficient`
  - name the surface
  - explain why it is overlap, sibling, or too broad
  - add the result to [External Evidence Ledger](EXTERNAL_EVIDENCE_LEDGER.md)
- `no fit found in searched lane`
  - name the lane
  - restate the blocker in one sentence
  - name the next honest search shape

## Bundle-Local Update Path

If exact-fit evidence lands, the preferred local update order is:

1. update `notes/second-context-adaptation.md`
2. update `notes/canonical-readiness.md`
3. update `TECHNIQUE.md` only if wording, examples, checks, or frontmatter need honest reinforcement
4. add `notes/adverse-effects-review.md` only if the bundle is actually ready to become `canonical`

## Stop Rules

- if the candidate evidence would require new bundle meaning, stop and log it as overlap
- if the candidate evidence is really a donor for a future new technique, route it to [External Import Runbook](EXTERNAL_IMPORT_RUNBOOK.md)
- if the search result only improves examples but not live reuse, keep the status blocker explicit
- if the same public source appears across multiple bundles, split ownership by target bundle and keep note edits disjoint
- if the sprint finds no exact-fit evidence, that is still a valid result; close the lane cleanly and move on

## Completion Criteria

An external evidence sprint is successful when each active bundle exits with one of these outcomes:

- one exact-fit second consumer is found and bundle-local notes are updated honestly
- one adjacent lane is ruled out and recorded so it is not searched again casually
- one searched lane is exhausted and the next search shape is named concretely

The sprint does not need to increase the canonical count to count as progress.

## Validation And Merge Discipline

- keep bundle edits local until evidence is real
- merge one technique per PR
- run `python scripts/release_check.py` after a merge-ready bundle exists
- update [Promotion Readiness Matrix](PROMOTION_READINESS_MATRIX.md), [External Evidence Ledger](EXTERNAL_EVIDENCE_LEDGER.md), and [Roadmap](../ROADMAP.md) only when the blocker or queue meaning actually changed

## Notes

- This runbook is intentionally narrower than [Roadmap](../ROADMAP.md); it owns live search execution, not the whole historical audit record.
- Expand [External Evidence Ledger](EXTERNAL_EVIDENCE_LEDGER.md) when a real lane search happens or a bundle exits the queue.
