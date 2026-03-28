# Second Context Adaptation

## Technique
- id: AOA-T-0062
- name: episode-bounded-agent-loop

## Target project
- name: aoa-techniques
- environment: public technique repository with authored bundle contracts, generated routing surfaces, and validator-backed markdown discipline
- runtime: documentation-first corpus that records one bounded continuation-loop seam rather than shipping the donor's full orchestrator, supervisor, or mission runtime

## What changed

- paths: the donor uses `MISSION.md`, `STATE.json`, `HANDOFF.md`, and `tasks.json`; this adaptation keeps the generic episode-loop contract without requiring those exact files
- services: launchd supervision, budget tracking, stop files, completion reports, and cooldown timers were removed from the reusable contract
- dependencies: the adaptation depends on bounded episode goals plus visible checkpoints and decisions, not on immutable task trackers, notifications, or a specific CLI harness
- operating assumptions: contributors should read the technique as one bounded continuation loop before broader startup, handoff, git-verification, or runtime-governance layers

## What stayed invariant

- contract: longer work is segmented into explicit episodes that end at checkpoints or stop conditions
- validation logic: each episode produces enough checkpoint state that the next episode can start honestly
- safety rules: the technique remains outside startup ritual doctrine, handoff-artifact structure, git verification, budgeting, supervision, and broader autonomous platform semantics

## Risks introduced by adaptation

- the pattern can collapse into [AOA-T-0001](../../plan-diff-apply-verify-report/TECHNIQUE.md) if repositories stop separating the long-run segmentation seam from the internal workflow of each episode
- teams may over-associate the pattern with a total autonomous harness because the donor also bundles mission files, task integrity rules, budgets, and supervision
- the public bundle could drift into [AOA-T-0057](../../structured-handoff-before-compaction/TECHNIQUE.md) or [AOA-T-0060](../../session-opening-ritual-before-work/TECHNIQUE.md) if checkpoint-artifact shape or episode startup ritual becomes the real center of gravity

## Evidence

- the Nightcrawler README explicitly describes multi-hour missions decomposed into bounded 30-60 minute episodes, each with a fresh context window and explicit termination conditions
- the README lists the episode lifecycle as repeated checkpointed cycles with re-read state, work, handoff, state update, and loop-back to the next episode
- `skills/nightcrawler-episode.md` requires end-of-episode handoff writing and state updates so a later episode can continue from explicit checkpointed state

## Result

- works as a documentation-first second context and preserves one bounded episode-loop contract without carrying over the donor's mission runtime, supervision stack, or broader autonomous-platform semantics
