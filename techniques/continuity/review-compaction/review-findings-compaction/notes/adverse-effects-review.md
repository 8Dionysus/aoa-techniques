# Adverse Effects Review

## Technique
- id: AOA-T-0052
- name: review-findings-compaction

## Review focus
- current role: canonical default for keeping repeated review findings current, compact, and traceable before later action
- current watch seam: keep the bundle centered on duplicate grouping, stale-finding refresh, current-code checks, and source-finding traceability rather than widening into remediation, issue triage, backlog policy, approval, merge, or PR-governance behavior

## Failure modes
- distinct findings are merged incorrectly because grouping is too aggressive
- stale findings survive as current because the latest-code check is weak or implicit
- current findings lose traceability back to the original comments or review artifacts
- old history grows until the compacted review surface becomes unreadable
- compaction is used to suppress uncomfortable findings instead of refreshing them honestly

## Negative effects
- a compact surface can look more authoritative than the revalidation process supports
- reviewers may lose nuance when repeated findings are collapsed too aggressively
- dropped or resolved findings can be hard to audit if history is not preserved in bounded form
- provider-adjacent auto-fix, approval, or merge behavior can turn findings hygiene into action policy

## Misuse patterns
- using compaction to hide findings rather than remove duplicates or stale results
- treating compacted findings as remediation instructions or approval state
- folding backlog ownership, issue triage, priority scoring, or merge policy into the compaction pass
- keeping only the latest summary while discarding all source-finding references

## Detection signals
- compacted findings cannot name their source comments, prior artifacts, or commit context
- exact duplicates still dominate the active review surface
- old findings remain marked current after code moved past them
- merged findings cite mismatched code locations or unrelated defects
- auto-remediation or approval behavior becomes tied to the compaction result

## Mitigations
- preserve source references while grouping findings
- re-check current code or current diff context before carrying a finding forward
- keep old findings in bounded history when they are useful for audit, not as current truth
- separate compaction from prioritization, remediation, approval, merge, and issue-management surfaces

## Recommendation
- move `AOA-T-0052` to `canonical` and use this note as the watch surface for stale-finding drift, over-compaction, lost traceability, hidden suppression, and expansion into remediation, backlog, approval, merge, or PR-governance authority
