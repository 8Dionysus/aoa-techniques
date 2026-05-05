# Second Context Adaptation

## Technique
- id: AOA-T-0057
- name: structured-handoff-before-compaction

## Target project
- name: aoa-techniques
- environment: public technique repository with authored bundle contracts, generated routing surfaces, and validator-backed markdown discipline
- runtime: documentation-first corpus that records one bounded continuation-packet seam rather than shipping the donors' orchestrator loops, checkpoint files, or startup automation

## What changed

- paths: the donors use `HANDOFF.md` in specific workspace or home-directory layouts; this adaptation keeps the generic pre-compaction handoff contract without requiring one file path
- services: launchd supervision, mission loops, state-checkpoint machinery, GitHub or local collaboration mode, and broader boot or orchestration services were removed from the reusable contract
- dependencies: the adaptation depends on one explicit boundary plus a structured continuation packet with status and references, not on a particular task tracker, scheduler, or runtime shell
- operating assumptions: contributors should read the technique as one pre-compaction handoff artifact seam before broader governance, transcript, or delivery layers

## What stayed invariant

- contract: one structured handoff packet is written before context loss and read before the next session continues
- validation logic: the packet keeps completed work, blocked or in-progress work, next work, and concrete references visible enough for continuation
- safety rules: the technique remains outside mailbox delivery semantics, transcript packaging, witness export, and broad continuation-governance doctrine

## Risks introduced by adaptation

- the pattern can collapse into the active `phase-synchronized-agent-handoff` narrowing lane if repositories stop separating one handoff packet from continuation permission and stop or return rules
- teams may over-associate the pattern with a full autonomous loop because the primary donor also bundles mission orchestration, budgets, launchd supervision, and immutable task tracking
- the public bundle could drift into transcript or witness doctrine if the handoff packet becomes a total run artifact instead of a bounded continuation packet

## Evidence

- the Nightcrawler README describes clean context per episode with structured `HANDOFF.md`, a data flow that includes `HANDOFF.md`, and a session opening ritual that reads the previous handoff before work
- `skills/nightcrawler-episode.md` requires writing a structured handoff before finishing and enumerates explicit handoff sections for summary, completed work, in-progress work, next context, changed files, and decisions
- the Code Relay README frames `HANDOFF / CHECKPOINT` as a structured save and restore alternative to lossy compression and emphasizes done, in-progress, next, and watch-out fields
- both donors present the handoff object as the continuation surface rather than as a hidden memory mechanism

## Result

- works as a documentation-first second context and preserves one bounded pre-compaction handoff contract without carrying over the donors' runtime stacks, checkpoint machinery, or broader orchestration semantics
