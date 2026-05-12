# Canonical Readiness

## Technique

- id: AOA-T-0051
- name: commit-triggered-background-review

## Verdict

- approve for canonical promotion

## Evidence summary

- external origin: the imported technique has a bounded donor contract and
  explicit exclusions around auto-fix loops, queue product breadth, alerting
  hooks, and daemon/runtime specifics
- second context: `aoa-techniques` records the same commit-triggered review
  artifact contract as a documentation-first landing aid with one example and
  one checklist
- external reinforcement: Qodo / PR-Agent provides a public second workflow
  where PR or push events trigger review output; the open-source PR-Agent
  GitHub Action uses `pull_request` events including `synchronize`, supports
  automatic review, and exposes review output as PR comments or JSON action
  output
- public docs reinforcement: Qodo's persistent review comment surface updates
  the existing review comment whenever new commits are pushed, keeps findings
  visible in the pull request review, and preserves a per-commit findings audit
  trail
- validation strength: the bundle now has donor evidence, repo-local
  adaptation, public product documentation, open-source implementation
  surfaces, a checklist, an example, and an explicit adverse-effects review

## Default-use rationale

- this is the right canonical default when the main reusable object is
  asynchronous post-commit or post-push review that produces a bounded
  inspectable findings artifact
- it remains distinct from remediation and compaction siblings, which should
  not be collapsed back into the trigger-and-artifact contract
- it stays narrower than CI governance, alerting policy, auto-approval,
  auto-fix, autonomous merge, or queue product doctrine even when those
  features sit nearby in the external source family

## Fresh public-safety check

- review date: 2026-05-12
- result: pass
- sanitization still holds: the bundle keeps only the reusable
  commit-triggered review artifact contract and excludes donor-specific
  runtime, auto-remediation, merge, approval, and governance breadth
- public reuse check: the example, checklist, adaptation notes, and Qodo /
  PR-Agent evidence are understandable without hidden donor-repo context

## Remaining gaps

- no blocker remains for canonical promotion
- later evidence may strengthen specific provider variants, but it should not
  widen this bundle into auto-fix, auto-approval, merge policy, or full PR
  governance

## Recommendation

- move `AOA-T-0051` to `canonical`
- keep `AOA-T-0052` as the separate findings hygiene sibling when the real
  question is stale or repeated review findings rather than the commit-bound
  trigger
