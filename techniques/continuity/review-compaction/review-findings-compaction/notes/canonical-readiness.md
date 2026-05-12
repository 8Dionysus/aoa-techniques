# Canonical Readiness

## Technique

- id: AOA-T-0052
- name: review-findings-compaction

## Verdict

- approve for canonical promotion

## Evidence summary

- external origin: the imported technique has a bounded donor contract and
  explicit exclusions around trigger logic, fix loops, queue product breadth,
  and runtime specifics
- second context: `aoa-techniques` records the same findings-compaction
  contract as a documentation-first landing aid with one example and one
  checklist
- external reinforcement: Qodo's persistent review comments update an existing
  review comment when new commits are pushed instead of posting a fresh review
  every time, keeping the active findings surface compact during repeated
  review cycles
- public docs reinforcement: Qodo records findings added per commit and
  findings resolved per commit, while its update flow detects the latest delta,
  generates suggestions from recent changes, merges them with overall PR
  feedback, and marks recent findings distinctly
- implementation reinforcement: open-source PR-Agent preserves a persistent
  latest-suggestions comment with previous suggestions folded into history,
  trims old history by configured length, validates suggestions against current
  diff hunks, and uses incremental review logic to find new commits since the
  previous review
- validation strength: the bundle now has donor evidence, repo-local
  adaptation, public product documentation, open-source implementation
  surfaces, a checklist, an example, and an explicit adverse-effects review

## Default-use rationale

- this is the right canonical default when the main reusable object is keeping
  review findings current, smaller, and traceable across repeated review runs
- it remains distinct from `AOA-T-0051`, which owns the review trigger and
  artifact production step rather than the later compaction and refresh pass
- it stays narrower than backlog policy, remediation automation, issue
  triage, auto-approval, or full PR governance

## Fresh public-safety check

- review date: 2026-05-12
- result: pass
- sanitization still holds: the bundle keeps only the reusable
  findings-compaction contract and excludes donor-specific runtime, auto-fix,
  approval, merge, and issue-management breadth
- public reuse check: the example, checklist, adaptation notes, and Qodo /
  PR-Agent evidence are understandable without hidden donor-repo context

## Remaining gaps

- no blocker remains for canonical promotion
- later evidence may strengthen provider-specific stale-finding policies, but
  it should not widen this bundle into remediation, backlog ownership, or
  platform governance

## Recommendation

- move `AOA-T-0052` to `canonical`
- keep `AOA-T-0051` as the separate trigger-and-artifact sibling when the real
  question is when review starts rather than how findings stay compact and
  current
