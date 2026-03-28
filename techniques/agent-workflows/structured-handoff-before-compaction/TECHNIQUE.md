---
id: AOA-T-0057
name: structured-handoff-before-compaction
domain: agent-workflows
status: promoted
origin:
  project: thebasedcapital/nightcrawler + yan5xu/code-relay
  path: README.md + skills/nightcrawler-episode.md + README.md
  note: Adapted from Nightcrawler's per-episode handoff protocol, reinforced by Code Relay's checkpoint-before-compression framing, to keep continuation state explicit before context loss.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - handoff
  - compaction
  - checkpoint
  - continuation
summary: Write one structured handoff artifact before compaction or session rollover so the next session can resume from explicit state instead of hidden memory or transcript replay.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-28
export_ready: true
relations:
  - type: complements
    target: AOA-T-0054
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

# structured-handoff-before-compaction

## Intent

Write one structured handoff artifact before compaction or session rollover so the next session can resume from an explicit continuation packet instead of hidden memory, vague summary prose, or full transcript replay.

## When to use

- a real compaction, rollover, or episode boundary may drop useful working context
- unfinished work must survive to a later session or another agent without re-deriving state from memory
- the next session should review one bounded continuation artifact before resuming
- the reusable object is the pre-compaction handoff packet itself, not mailbox transport or transcript packaging

## When not to use

- there is no real context-loss boundary and a normal status note is enough
- the main artifact should be transcript packaging, history indexing, or witness export after the run
- mailbox delivery, replay, or acknowledgment are the real coordination needs
- the workflow needs general continuation permission, stop rules, or orchestration governance to make sense

## Inputs

- the current work state at the compaction or rollover boundary
- explicit done, in-progress, blocked, and next-step information
- key file paths, commits, artifacts, or other continuation references
- one trigger that says the current context is about to be reduced or handed off

## Outputs

- one structured handoff artifact written before context loss
- one explicit continuation packet with status, blockers, next work, and key references
- lower risk that the next session restarts from hidden memory or replays the whole transcript

## Core procedure

1. Detect the compaction, rollover, or episode boundary before context is actually dropped.
2. Freeze the current work state into one structured handoff artifact instead of relying on hidden memory or a late summary.
3. Record the minimum continuation fields: summary, work completed, work in progress or blocked, next step, and key file, commit, or artifact references.
4. Write the handoff artifact to a stable, reviewable location before context loss.
5. Require the next session to read the handoff artifact before resuming work.
6. Keep the artifact narrow enough that it remains a continuation packet rather than a transcript export, witness trace, mailbox protocol, or orchestration framework.
7. Route receipt semantics, git verification, transcript packaging, and broader continuation governance to sibling techniques when they become the real center of gravity.

## Contracts

- the handoff artifact exists before compaction or rollover completes
- the artifact distinguishes completed work, in-progress or blocked work, and the next intended step
- the artifact includes enough concrete references that continuation does not depend on hidden memory
- the next session is expected to read the artifact before continuing
- the technique stays smaller than transcript packaging, mailbox transport, and full handoff-governance doctrine

Relationship to adjacent techniques: unlike [AOA-T-0044](../../history/versionable-session-transcripts/TECHNIQUE.md), this technique does not package an already-saved transcript into a readable history artifact. Unlike [AOA-T-0045](../../history/witness-trace-as-reviewable-artifact/TECHNIQUE.md), it does not preserve a fuller witness trace for later audit. Unlike [AOA-T-0054](../compaction-resilient-skill-loading/TECHNIQUE.md), it records pre-compaction continuation state rather than reloading skills after compaction. Unlike [AOA-T-0056](../channelized-agent-mailbox/TECHNIQUE.md), it does not own delivery, replay, or acknowledgment semantics for the handoff packet. It also stays smaller than the live `phase-synchronized-agent-handoff` narrowing lane because it does not decide continuation permission, stop, return, or escalation rules across a general phase system.

## Risks

### Failure modes

- the handoff artifact is written too late and context is already lost
- the artifact omits a blocker, stale assumption, or concrete next step
- the artifact claims work was completed without enough references to verify it

### Negative effects

- the workflow can gain extra ceremony when the boundary is small enough that a full handoff packet is unnecessary
- teams may overtrust the handoff and stop checking source files or git state
- a supposedly small packet can drift toward a verbose transcript substitute

### Misuse patterns

- treating any freeform summary as if it already satisfies the handoff contract
- using the handoff artifact as a substitute for transcript packaging, witness export, or history indexing
- widening the bundle into generic orchestration, phase control, or continuation-governance doctrine

### Detection signals

- no handoff artifact exists before a known compaction or rollover boundary
- the next session cannot tell what is blocked or what should happen next
- handoff claims mention changed work but cite no files, commits, or artifacts
- the handoff keeps growing until it reads like a full transcript or runbook

### Mitigations

- trigger handoff creation before compaction rather than after memory loss
- keep completed, blocked, and next fields explicit
- include concrete file, commit, or artifact references in the packet
- pair the handoff with a separate verification or receipt technique when those concerns become real

## Validation

Verify the technique by confirming that:
- a handoff artifact is written before the boundary that would reduce context
- the artifact names completed work, in-progress or blocked work, and the next step explicitly
- the artifact includes concrete continuation references such as files, commits, or artifacts
- the next session can explain its first honest move from the handoff artifact alone
- the explanation still makes sense without mailbox transport, transcript packaging, or broad orchestration doctrine

See `checks/structured-handoff-before-compaction-checklist.md`.

## Adaptation notes

What can vary across projects:
- the filename or storage location of the handoff artifact
- the exact section headings or field names
- whether the packet is written for same-user compaction recovery or cross-agent continuation
- whether references point to files, commits, task IDs, or other project artifacts
- whether the handoff is markdown, YAML, or another small structured format

What should stay invariant:
- the handoff is written before context loss
- the continuation packet stays explicit and reviewable
- completed work, blocked work, and next work remain visible
- the next session reads the packet before continuing

Project-shaped details that should not be treated as invariant:
- one `HANDOFF.md` path under a particular home directory
- episode numbering or overnight mission framing
- `STATE.json`, `tasks.json`, or any immutable task-tracker contract
- launchd, worktree, or orchestrator runtime behavior
- multi-repo boot or checkpoint stacks beyond the bounded handoff packet itself

## Public sanitization notes

This import narrows the donors to one bounded pattern: write a structured handoff artifact before compaction or session rollover so continuation state remains explicit and reviewable. Overnight autonomy, launchd supervision, mission budgeting, immutable task trackers, state-checkpoint machinery, worktree policy, and broader orchestration semantics were intentionally left out of the public contract.

## Example

See `examples/minimal-structured-handoff-before-compaction.md`.

## Checks

See `checks/structured-handoff-before-compaction-checklist.md`.

## Promotion history

- adapted from open-source `thebasedcapital/nightcrawler` with supporting checkpoint framing from `yan5xu/code-relay`
- staged through the chat wave 3 handoff-bounded-continuation lane inside `aoa-techniques`
- promoted into `aoa-techniques` on 2026-03-28 as a bounded external-import technique for pre-compaction structured handoff artifacts

## Future evolution

- keep receipt and acknowledgment semantics separate instead of widening this bundle into delivery protocol
- keep git-verification and transcript-packaging siblings separate instead of using the handoff as a total truth surface
- reopen the broader phase-synchronized handoff lane only if continuation permission and stop or return rules can be stated as a smaller bounded contract
