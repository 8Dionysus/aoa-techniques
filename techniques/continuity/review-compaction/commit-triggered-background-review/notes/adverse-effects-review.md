# Adverse Effects Review

## Technique
- id: AOA-T-0051
- name: commit-triggered-background-review

## Review focus
- current role: canonical default for launching bounded background review after a visible commit or push boundary and preserving inspectable findings before later action
- current watch seam: keep the bundle centered on trigger identity, background review output, persistent inspectable artifacts, and separation from remediation rather than widening into auto-fix, auto-approval, merge policy, alerting, broad CI, or PR-governance behavior

## Failure modes
- asynchronous review lag makes old findings look current because the artifact lacks the triggering commit or scope
- repeated triggers accumulate multiple comments instead of preserving one inspectable current artifact
- review output becomes detached from the commit, push, or diff that caused it
- provider-adjacent auto-fix or auto-approval behavior is treated as part of the review trigger
- reviewers treat a background review artifact as final proof instead of one inspectable input

## Negative effects
- delayed review output can create a confusing gap between commit landing and finding inspection
- automatic triggers can add notification noise if the artifact surface is not compact
- teams can overtrust the background loop and skip explicit human review or validation
- provider products can pull the technique toward broader PR governance when the narrow artifact seam is not guarded

## Misuse patterns
- attaching auto-fix, auto-merge, auto-approval, or branch-policy changes to the same technique
- widening the trigger to every repository event without preserving one visible commit-like boundary
- treating a review comment as CI authority or merge readiness
- hiding remediation steps behind the background review run

## Detection signals
- findings cannot be tied back to a commit, push, PR event, or diff
- review output mutates code, approval state, or branch policy directly
- reviewers cannot tell whether the artifact reflects current code or an older commit
- queue behavior, chat behavior, or provider dashboard behavior becomes more important than the bounded review artifact

## Mitigations
- keep commit, push, or diff identity in the artifact
- keep review production separate from remediation, approval, merge, and policy actions
- revalidate or rerun review when code moves beyond the triggering commit
- split queue compaction, review chat, auto-fix, and policy behavior into separate techniques or owner surfaces

## Recommendation
- move `AOA-T-0051` to `canonical` and use this note as the watch surface for stale-review drift, trigger-identity loss, artifact-as-verdict drift, and expansion into auto-remediation, approval, merge, CI, or PR-governance authority
