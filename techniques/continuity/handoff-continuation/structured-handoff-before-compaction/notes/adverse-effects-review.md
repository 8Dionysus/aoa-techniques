# Adverse Effects Review

## Technique

- id: AOA-T-0057
- name: structured-handoff-before-compaction

## Review focus

- current role: canonical default for writing one structured continuation packet before compaction, rollover, or restart reduces working context
- current watch seam: preserve the packet contract without turning it into transcript packaging, mailbox delivery, receipt approval, memory search, hook governance, or a full long-running-agent harness

## Failure modes

- the packet is created after context loss, so missing details have already been summarized away
- completed, blocked, and next-step fields collapse into vague narrative prose
- references omit concrete files, commits, commands, artifacts, or validation already run
- the next session skips the packet and resumes from memory or chat fragments
- a progress or handoff file is updated mechanically but no longer reflects current work

## Negative effects

- small tasks can gain unnecessary ceremony if every pause becomes a full handoff packet
- agents can overtrust the packet and stop checking git state, files, tests, or current instructions
- a constantly growing packet can become a transcript substitute that crowds out the next session
- hook or cron automation can hide the fact that the packet was stale, incomplete, or never read

## Misuse patterns

- treating a freeform summary as if it satisfies the structured handoff contract
- using the packet as approval for continuation instead of routing receipt, verification, or permission to sibling techniques
- storing secrets, private paths, or unreviewed drafts because "the next agent needs context"
- importing memory-search, session-history, vector database, scheduling, or harness-loop machinery into a technique that only needs a small packet
- replacing source-state verification with the handoff's claims

## Detection signals

- the incoming session cannot name its first honest move from the packet alone
- the packet has a "next" field but no blocker, reference, or validation history
- handoff claims cite work done but no files, commits, artifacts, or commands
- repeated compactions produce summaries of summaries instead of one current packet
- discussion shifts from continuation fields to cron schedules, vector memory, session databases, or lifecycle policy

## Mitigations

- create or refresh the packet before compaction, rollover, or restart pressure becomes active
- keep done, in-progress or blocked, next, and references as explicit fields
- require the next session to read the packet before the first mutation and then verify source state separately
- keep the packet short enough to be scanned cold; move transcript history, witness traces, mailbox receipt, and git-claim verification to sibling techniques
- mark automated handoff writers as backstops, not proof that the packet was accurate or consumed

## Recommendation

- move `AOA-T-0057` to `canonical` and use this note as the watch surface for late packets, vague summaries, packet-overtrust, transcript drift, automation-staleness, and memory/harness overreach
