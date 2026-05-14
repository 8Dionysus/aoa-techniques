# Canonical Readiness

## Technique
- id: AOA-T-0048
- name: semantic-review-surface-lift

## Verdict
- approve for canonical promotion

## Evidence summary
- origin evidence: `aoa-techniques` already has authored semantic-review docs and a derived semantic-review manifest.
- second context: `aoa-playbooks` keeps authored gate-review markdown and reviewed-run summaries as source surfaces, then derives `generated/playbook_review_status.min.json` through `scripts/generate_playbook_review_status.py`.
- validation strength: the bundle now has origin evidence plus one non-origin sibling repository that reuses the same source-review to derived-reader split without turning the reader into scoring, policy, or status automation.
- searched lane: the 2026-05-12 Pack 6 pass correctly rejected generic AI/code review, quality-report, scoring, and summary products; the 2026-05-14 follow-up found an exact review-status reader in `aoa-playbooks`.

## Default-use rationale
- the technique is the right shape when a repository has authored cluster or boundary review docs and needs a subordinate reader surface.
- it is not the right shape for AI review scoring, code review summaries, quality dashboards, policy checks, or automated semantic verdicts.
- it is now the canonical default for a bounded authored review-note corpus that needs a derived reader exposing scope, evidence refs, findings or signal summary, and next-step posture while routing meaning back to markdown.
- it still must not absorb playbook composition governance, eval verdicts, owner acceptance, release gates, graph semantics, or promotion policy.

## Fresh public-safety check
- review date: 2026-05-14
- result: pass
- sanitization still holds: the bundle and this note keep review meaning public, authored, and source-linked.
- public reuse check: an external reader can understand the pattern from public repository paths and source-to-derived review boundaries without private transcript state.

## Remaining gaps
- no blocking gap remains for canonical use as long as the generated review reader stays subordinate to authored review notes.
- future review should watch for reader overreach into scoring, automatic verdicts, policy enforcement, relation cleanup, composition governance, or graph behavior.

## Recommendation
- promote `AOA-T-0048` to `canonical`
- use it when authored semantic-review, boundary-review, or gate-review markdown needs a derived lookup surface that preserves source authority and does not automate the review verdict
