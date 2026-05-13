# Adverse Effects Review

## Technique
- id: AOA-T-0083
- name: checkpoint-bound-self-repair
- current role: bounded canonical default

## Review focus

Review the effects of making explicit checkpoint posture the default guard
around a meaningful bounded self-repair.

## Failure modes

- approval, rollback, health check, iteration, or improvement-log posture is partial
- checkpoint posture is used before any bounded repair shape exists
- repair still feels automatic because approval or rollback is implicit
- role-law, proof-law, or playbook scenario design hides behind repair language

## Negative effects

- too much checkpoint ceremony can slow obviously safe tiny repairs
- downstream agents may over-trust a checklist and stop asking whether the
  repair should happen
- improvement logs can become decorative if nobody rereads them

## Misuse patterns

- replacing repair shaping with checkpoint paperwork
- treating approval posture as execution authority
- hiding doctrine or role edits behind self-repair language
- using retry loops as pseudo-progress instead of escalation

## Detection signals

- rollback markers or health checks are missing
- no iteration limit is named for a risky repair route
- reviewers cannot find the improvement-log or audit stub afterward
- important surfaces changed without visible checkpoint evidence

## Mitigations

- require a bounded repair shape before checkpoint posture
- keep approval, rollback, health check, iteration, and improvement log explicit
- escalate when retries fail or the repair widens
- hand role-law, proof-law, playbook, and runtime concerns to their owners

## Recommendation

Keep the canonical bundle and use this note as one bounded watch surface. Future
changes should keep checkpoint-bound self-repair explicit and reversible
without widening it into role contracts, proof doctrine, playbook orchestration,
runtime self-healing, or autonomous self-modification authority.
