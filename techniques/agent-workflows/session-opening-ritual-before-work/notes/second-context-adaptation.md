# Second Context Adaptation

## Technique
- id: AOA-T-0060
- name: session-opening-ritual-before-work

## Target project
- name: aoa-techniques
- environment: public technique repository with authored bundle contracts, generated routing surfaces, and validator-backed markdown discipline
- runtime: documentation-first corpus that records one bounded session-start seam rather than shipping the donor's orchestrator loops, state files, or startup automation

## What changed

- paths: the donor uses `STATE.json`, `MISSION.md`, `HANDOFF.md`, and `tasks.json`; this adaptation keeps the generic read-and-verify ritual without requiring those exact files
- services: launchd supervision, overnight mission loops, budget tracking, stop flags, and broader process-management services were removed from the reusable contract
- dependencies: the adaptation depends on one visible read step plus one visible current-state check, not on immutable task trackers, startup test suites, or a specific CLI harness
- operating assumptions: contributors should read the technique as one pre-mutation session-opening ritual before broader planning, packet-writing, or git-verification layers

## What stayed invariant

- contract: a resumed session reads current context and checks visible current state before the first mutation
- validation logic: the opening ritual names a baseline, checks it against reality, and keeps mismatches explicit
- safety rules: the technique remains outside handoff authoring, detailed git-claim verification, task-priority policy, baseline test doctrine, and orchestration governance

## Risks introduced by adaptation

- the pattern can collapse into [AOA-T-0001](../../plan-diff-apply-verify-report/TECHNIQUE.md) if repositories stop separating the session-opening seam from the full change workflow
- teams may over-associate the pattern with a total autonomous harness because the donor also bundles task picking, baseline testing, budgets, and orchestrator behavior
- the public bundle could drift into [AOA-T-0059](../../git-verified-handoff-claims/TECHNIQUE.md) if concrete claim-by-claim git checks become the real center of gravity

## Evidence

- the Nightcrawler README describes a mandatory session opening ritual before any work, including reading current state, reading the handoff, and verifying what actually changed before continuing
- `skills/nightcrawler-episode.md` requires reading state, mission, handoff, and task surfaces before work, and says this prevents agents from starting from stale assumptions or hallucinated context
- both donor surfaces present the opening ritual as a pre-work trust seam rather than as hidden memory or an optional convenience step

## Result

- works as a documentation-first second context and preserves one bounded pre-mutation session-opening ritual without carrying over the donor's runtime stacks, task-governance layers, or full startup protocol
