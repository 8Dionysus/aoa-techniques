---
id: AOA-T-0062
name: episode-bounded-agent-loop
domain: agent-workflows
kind: handoff
status: promoted
origin:
  project: thebasedcapital/nightcrawler
  path: README.md + skills/nightcrawler-episode.md
  note: Adapted from Nightcrawler's episode-based mission loop to keep bounded work slices, checkpoints, and explicit continue-or-stop decisions visible without importing the donor's orchestration runtime, budgets, or supervision stack.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - episodes
  - checkpoints
  - continuation
  - stop-rules
summary: Break longer work into explicit episodes with checkpoints and continue, stop, or escalate decisions so continuation stays reviewable instead of slipping into open-ended autonomy.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-28
export_ready: true
relations:
  - type: complements
    target: AOA-T-0057
evidence:
  - kind: external_origin
    path: notes/external-origin.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: external_review
    path: notes/external-import-review.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# episode-bounded-agent-loop

## Intent

Break longer work into explicit episodes with checkpoints and continue, stop, or escalate decisions so continuation stays reviewable instead of slipping into open-ended autonomy.

## When to use

- the work is too large or risky for one bounded pass
- checkpoints are needed between slices of progress
- stop or escalation decisions matter as much as progress itself
- the reusable object is one bounded episode loop, not a whole autonomous agent platform

## When not to use

- one bounded single-shot pass is enough
- the main missing seam is just handoff writing, startup ritual, or a generic change workflow
- the workflow only makes sense when bundled with budgets, supervision, task trackers, or a total orchestration runtime
- there is no meaningful checkpoint where a continue-or-stop decision could be reviewed

## Inputs

- one current episode goal
- one checkpoint artifact or checkpoint criterion
- one visible rule for continue, stop, or escalate

## Outputs

- one bounded episode result
- one explicit checkpoint artifact or checkpoint state
- one visible decision to continue, stop, or escalate before a new episode begins

## Core procedure

1. Define one bounded goal for the current episode rather than treating the entire mission as one uninterrupted run.
2. Work only until the checkpoint condition or stop rule is reached.
3. Produce one checkpoint artifact or equivalent visible checkpoint state before the episode ends.
4. Decide explicitly whether the next move is continue, stop, or escalate instead of letting the loop drift onward by default.
5. Open a later episode only from that visible checkpoint rather than from hidden memory or an implicit assumption of progress.
6. Keep the episode seam narrow enough that it remains a bounded loop contract rather than a full orchestrator, scheduler, or autonomous platform.
7. Route startup rituals, handoff packet structure, git-claim verification, budgets, task integrity systems, and runtime supervision to sibling techniques when they become the real center of gravity.

## Contracts

- each episode has one bounded goal
- each episode reaches a visible checkpoint or stop condition before the next episode opens
- continue, stop, or escalate decisions remain explicit
- continuation reads from the checkpointed state rather than from hidden memory
- the technique stays smaller than autonomous agent doctrine, orchestration runtimes, and total workflow governance

Relationship to adjacent techniques: unlike [AOA-T-0057](../structured-handoff-before-compaction/TECHNIQUE.md), this technique does not define the shape of the handoff artifact itself; it defines the bounded loop that says work proceeds in episodes separated by checkpoints. Unlike [AOA-T-0060](../session-opening-ritual-before-work/TECHNIQUE.md), it does not own the pre-mutation ritual at the start of an episode; it owns the fact that long work is broken into reviewable slices with explicit stop and continue decisions. Unlike [AOA-T-0001](../plan-diff-apply-verify-report/TECHNIQUE.md), it does not define the internal workflow of each episode's change application; it constrains how longer work is segmented over time.

## Risks

### Failure modes

- episodes are too large to review safely
- checkpoint criteria are too vague to stop the loop honestly
- continuation happens by inertia even when the checkpoint says the work should stop or escalate

### Negative effects

- the workflow can gain ceremony if the work was already small enough for one bounded pass
- teams may mistake the presence of episodes for proof that the work is well-governed
- the seam can drift into a full autonomy framework if budgets, supervision, and runtime policy start accumulating inside it

### Misuse patterns

- treating any long task as permission for indefinite continuation
- skipping checkpoint review to preserve momentum
- widening the technique into task-tracker policy, process supervision, or whole-agent mission doctrine

### Detection signals

- episodes have no clear end condition
- continuation happens without a visible checkpoint artifact or checkpoint state
- stop or escalation rules are named vaguely enough that they never really fire
- the bundle starts accreting budgets, watchdogs, task integrity rules, or runtime-management logic unrelated to the bounded episode seam

### Mitigations

- keep episode goals short and explicit
- require one visible checkpoint before the next episode opens
- keep continue, stop, and escalate as explicit outcomes
- route supervision, budgeting, task integrity, and runtime policy to sibling layers

## Validation

Verify the technique by confirming that:
- each episode has a bounded goal
- every episode ends at a checkpoint or stop condition
- the continue, stop, or escalate decision is explicit
- the next episode can explain its starting point from the checkpoint alone
- the technique still makes sense without an orchestrator runtime, budget stack, or autonomous platform doctrine

See `checks/episode-bounded-agent-loop-checklist.md`.

## Adaptation notes

What can vary across projects:
- episode length
- how checkpoint artifacts are represented
- whether escalation goes to a human, another agent, or a later planning surface
- whether the decision is recorded in markdown, YAML, JSON, or another reviewable format
- how strict the stop threshold is

What should stay invariant:
- longer work is segmented into explicit episodes
- episodes end at checkpoints or stop conditions
- the continue, stop, or escalate decision stays visible
- later work starts from the checkpoint rather than from hidden memory

Project-shaped details that should not be treated as invariant:
- one `STATE.json`, `tasks.json`, or mission-template contract
- one maximum-episode count, budget cap, or cooldown timer
- launchd supervision, crash-recovery stacks, or notification systems
- one CLI harness or pipe-mode runtime
- a whole autonomous mission platform

## Public sanitization notes

This import narrows the donor to one bounded pattern: longer work proceeds in explicit episodes separated by checkpoints and visible continue, stop, or escalate decisions. Budgets, launchd supervision, immutable task trackers, mission templates, crash-recovery mechanics, and the broader autonomous runtime were intentionally left out of the public contract.

## Example

See `examples/minimal-episode-bounded-agent-loop.md`.

## Checks

See `checks/episode-bounded-agent-loop-checklist.md`.

## Promotion history

- adapted from open-source `thebasedcapital/nightcrawler`
- staged through the chat wave 3 handoff-bounded-continuation lane inside `aoa-techniques`
- promoted into `aoa-techniques` on 2026-03-28 as a bounded external-import technique for episode-sliced continuation loops

## Future evolution

- keep handoff packet structure separate instead of widening this bundle into a total continuation artifact doctrine
- keep startup rituals separate instead of treating the episode loop as a full boot protocol
- keep supervision, budgeting, and task-integrity systems separate instead of importing a whole autonomous platform
