# Canonical Readiness

## Technique
- id: AOA-T-0057
- name: structured-handoff-before-compaction

## Verdict
- approve for canonical promotion

## Evidence summary

- external origin: the imported technique has a bounded donor contract and explicit exclusions around launchd supervision, mission loops, immutable task tracking, checkpoint stacks, mailbox delivery semantics, and broader orchestration doctrine
- second context: `aoa-techniques` now records the same pre-compaction handoff seam as a documentation-first adaptation with one example and one checklist
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- `anthropics/cwc-long-running-agents` provides exact-fit public reinforcement beyond the donor family: long-running agent sessions keep a structured `PROGRESS.md`, read it first on restart, update it after completed items, and use git checkpointing plus a stop-hook backstop because fresh sessions and context-window summaries lose detail
- `AlekseiUL/openclaw-memory-kit` provides supporting compaction-specific reinforcement: its OpenClaw compaction config writes `memory/handoff.md` before compression with fixed topic, decisions, TODO, files, context, and drafts fields, and its bootstrap template reads that handoff before continuing after wake-up or compaction
- adjacent pressure: Codex and Hermes public issues request compact handoff or fresh-session handoff behavior, but those issue threads are treated only as evidence of need, not as primary workflow proof
- validation strength: the bundle now carries one checklist, one example, a clean external-origin note, a documentation-first second context, and two public reinforcement surfaces for structured handoff artifacts across restart or compaction boundaries

## Default-use rationale

- this is the right canonical default when the main problem is preserving bounded continuation state across compaction, session rollover, restart, or fresh-session handoff
- it remains narrower than transcript and history artifacts because it owns one continuation packet, not post-capture packaging or searchable history
- it also remains narrower than mailbox transport and the active phase-synchronized handoff lane because it does not own delivery, receipt, or continuation-permission doctrine
- it is now strong enough as a default because the external reinforcement repeats the same fields-and-read-before-work shape without requiring the bundle to absorb long-running harness loops, cron memory, vector search, session databases, or hook policy

## Fresh public-safety check

- review date: 2026-05-12
- result: pass
- sanitization still holds: the bundle keeps only the reusable pre-compaction handoff seam and excludes donor runtime stacks, task-tracker policies, checkpoint machinery, and broader orchestration semantics
- public reuse check: the example, checklist, and adaptation notes remain understandable without hidden donor-repo context; `cwc-long-running-agents` is Apache-2.0 public evidence and `openclaw-memory-kit` is MIT public evidence, with no source code, private data, credentials, or restricted workflow details copied into the technique

## Remaining gaps

- no blocker remains for canonical status
- future work can add another pre-compaction hook, fresh-session handoff, or progress-file implementation, but it must preserve the narrow boundary: one structured packet, written before context loss or kept current ahead of restart, read before continuation, and verified separately against source state
- keep the automation caveat visible: hooks, crons, and stop callbacks can help write the packet, but they are not proof that the packet is accurate, current, or consumed

## Recommendation

- move `AOA-T-0057` to `canonical`
- add an adverse-effects review to preserve the boundary between structured continuation packets, transcript packaging, mailbox receipt, git verification, memory search, hook policy, and full long-running-agent harnesses
