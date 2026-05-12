# Adverse Effects Review

## Technique

- id: AOA-T-0062
- name: episode-bounded-agent-loop

## Review focus

- current role: canonical default for dividing longer agent work into bounded checkpointed episodes or equivalent durable steps before deciding whether to continue, stop, or escalate
- current watch seam: preserve the episode loop without turning it into session-opening ritual, handoff packet doctrine, git-claim verification, proof-gate policy, durable-job orchestration, or full autonomous-agent lifecycle governance

## Failure modes

- an episode goal is too broad, so the checkpoint becomes a vague progress note rather than a real boundary
- continuation happens automatically after a checkpoint without a visible continue, stop, or escalate decision
- the next episode starts from hidden model memory or inherited narration instead of the checkpointed state
- failed, blocked, or unsafe episode outcomes are normalized as "continue later" without being marked as stop or escalation triggers

## Negative effects

- small tasks can gain unnecessary ceremony when one bounded pass would have been clearer
- teams can mistake segmented work for governed work even when the checkpoints are weak
- checkpoint artifacts can become noisy if they collect every runtime detail instead of the state needed for the next bounded slice
- the technique can invite broad platform language if schedules, fibers, child agents, budgets, supervision, or proof gates are folded into the episode seam

## Misuse patterns

- treating any multi-step plan as an episode loop even when there is no reviewable boundary between steps
- using checkpoints as decorative summaries while continuing by momentum
- hiding escalation behind retries, schedules, or background workers
- importing workflow engines, Durable Object lifecycle, budget caps, task integrity systems, or proof-pack settlement into the technique
- merging the episode loop with startup rituals, structured handoff packets, receipt gates, or git-backed claim verification

## Detection signals

- the checkpoint cannot explain where the next episode should start
- the operator cannot say why the previous episode continued, stopped, or escalated
- failure state is recorded but the next slice opens anyway without re-planning or review
- the artifact starts naming platform primitives more often than episode goal, checkpoint, and decision state
- adjacent techniques are needed but are being copied into this bundle instead of linked or routed

## Mitigations

- keep each episode goal short enough that its end condition can be reviewed
- require one checkpoint artifact or checkpoint state before a new episode opens
- record the next decision as continue, stop, or escalate rather than implying it from progress
- route session-opening ritual to AOA-T-0060 and handoff packet shape to AOA-T-0057
- keep proof gates, durable-job infrastructure, supervision, budgets, and runtime lifecycle in their owning layers

## Recommendation

- move `AOA-T-0062` to `canonical` and use this note as the watch surface for checkpoint theater, implicit continuation, hidden-memory starts, platform creep, and accidental absorption of sibling continuation or governance techniques
