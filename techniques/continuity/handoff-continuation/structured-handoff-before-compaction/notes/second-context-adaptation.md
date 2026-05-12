# Second Context Adaptation

## Technique
- id: AOA-T-0057
- name: structured-handoff-before-compaction

## Target project
- name: aoa-techniques
- environment: public technique repository with authored bundle contracts, generated routing surfaces, and validator-backed markdown discipline
- runtime: documentation-first corpus that records one bounded continuation-packet seam rather than shipping the donors' orchestrator loops, checkpoint files, or startup automation
- external reinforcement:
  - name: Harness Primitives for Long-Running Claude Agents
  - repository: `anthropics/cwc-long-running-agents`
  - observed revision: `ffd563d668a97a38d4aa092bf0d5b1507c046629`
  - license: Apache-2.0
  - public surfaces: `README.md`, `claude-code-config/.claude/CLAUDE.md`, `claude-code-config/README.md`, and `claude-code-config/.claude/hooks/commit-on-stop.sh`
  - supporting reinforcement: `AlekseiUL/openclaw-memory-kit` at `b154ad075ee96e7c20edcebf2e9aa93a02493262`, MIT, with `config/compaction.json`, `config/memory-flush.json`, `templates/handoff.md`, and `templates/BOOTSTRAP.md`
  - adjacent pressure: `openai/codex#21673`, `NousResearch/hermes-agent#20372`, and `NousResearch/hermes-agent#499` show public demand for compact handoff or handoff-oriented compaction, but are request or design-discussion surfaces rather than primary proof

## What changed

- paths: the donors use `HANDOFF.md` in specific workspace or home-directory layouts; this adaptation keeps the generic pre-compaction handoff contract without requiring one file path
- services: launchd supervision, mission loops, state-checkpoint machinery, GitHub or local collaboration mode, and broader boot or orchestration services were removed from the reusable contract
- dependencies: the adaptation depends on one explicit boundary plus a structured continuation packet with status and references, not on a particular task tracker, scheduler, or runtime shell
- operating assumptions: contributors should read the technique as one pre-compaction handoff artifact seam before broader governance, transcript, or delivery layers
- external reinforcement: `cwc-long-running-agents` repeats the same durable packet pattern through a `PROGRESS.md` convention that fresh sessions read first, while `openclaw-memory-kit` repeats the compaction-specific handoff shape through a memory-flush prompt and bootstrap read path

## What stayed invariant

- contract: one structured handoff packet is written before context loss and read before the next session continues
- validation logic: the packet keeps completed work, blocked or in-progress work, next work, and concrete references visible enough for continuation
- safety rules: the technique remains outside mailbox delivery semantics, transcript packaging, witness export, and broad continuation-governance doctrine
- boundary: automation can refresh or commit the packet, but the reusable technique remains the packet-and-read-before-work contract rather than the hook, cron, vector memory, or harness loop

## Risks introduced by adaptation

- the pattern can collapse into the active `phase-synchronized-agent-handoff` narrowing lane if repositories stop separating one handoff packet from continuation permission and stop or return rules
- teams may over-associate the pattern with a full autonomous loop because the primary donor also bundles mission orchestration, budgets, launchd supervision, and immutable task tracking
- the public bundle could drift into transcript or witness doctrine if the handoff packet becomes a total run artifact instead of a bounded continuation packet
- progress-file and memory-flush reinforcement can tempt a wider memory-system import; the bundle should keep cron schedules, vector search, session-history APIs, and stop-hook policy outside the canonical technique

## Evidence

- the Nightcrawler README describes clean context per episode with structured `HANDOFF.md`, a data flow that includes `HANDOFF.md`, and a session opening ritual that reads the previous handoff before work
- `skills/nightcrawler-episode.md` requires writing a structured handoff before finishing and enumerates explicit handoff sections for summary, completed work, in-progress work, next context, changed files, and decisions
- the Code Relay README frames `HANDOFF / CHECKPOINT` as a structured save and restore alternative to lossy compression and emphasizes done, in-progress, next, and watch-out fields
- both donors present the handoff object as the continuation surface rather than as a hidden memory mechanism
- `cwc-long-running-agents` frames agent-maintained handoff as one of the core long-running primitives because fresh sessions have no memory and context-window summaries lose detail; its convention says the agent reads `PROGRESS.md` before any work, creates it with `Done`, `In progress`, `Next`, and `Notes` sections if absent, updates it after completed items, and uses git history as a second record.
- `cwc-long-running-agents` pairs the convention with a stop-hook backstop that commits tracked changes at session end so work remains durable across restarts without making the handoff file a transcript or mailbox.
- `openclaw-memory-kit` configures compaction safeguard mode with a `memoryFlush` prompt that writes `memory/handoff.md` before compression using fixed `Topic`, `Decisions`, `TODO`, `Files`, `Context`, and `Drafts` sections.
- `openclaw-memory-kit` ships a `handoff.md` template with the same continuation fields and a `BOOTSTRAP.md` that reads the handoff immediately after wake-up or compaction before verifying recent session history.
- Codex and Hermes issue surfaces were inspected as adjacent pressure: they ask for compact handoff, copyable handoff, or handoff-oriented compaction, but they are not used as primary proof because requests and design discussions do not by themselves show a landed workflow surface.

## Result

- works across donor, documentation-first, long-running-harness, and compaction-memory contexts while preserving one bounded pre-compaction handoff contract: a structured continuation packet exists before context loss, stays small enough to read cold, names done or blocked work plus next steps and references, and is read before continuation. It does not carry over donor runtime stacks, cron memory, vector search, session databases, stop-hook policy, transcript packaging, mailbox receipt, or broader orchestration semantics.
