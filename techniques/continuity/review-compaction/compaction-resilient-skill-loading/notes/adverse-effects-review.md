# Adverse Effects Review

## Technique
- id: AOA-T-0054
- name: compaction-resilient-skill-loading

## Review focus
- promotion from `promoted` to `canonical` after exact-fit public reinforcement from Claude Code's documented skill content lifecycle
- failure cases where post-compaction skill recovery is mistaken for full context restoration, memory recall, marketplace behavior, or hidden prompt replay

## Failure modes
- a session re-attaches stale skill instructions after compaction even though the canonical source changed
- a large skill is partially preserved after compaction and the agent treats the truncated copy as complete
- the recovery surface lists skills that can no longer be loaded from canonical sources
- post-compaction recovery happens invisibly, leaving reviewers unable to see what capability context was restored

## Negative effects
- operators may over-trust a recovered skill surface and skip re-reading the canonical skill when precision matters
- automatic reattachment can increase token pressure if too many skills are kept alive after compaction
- teams may treat skill recovery as memory continuity and accidentally preserve broader state than the technique permits
- hidden or noisy recovery messages can make the session harder to audit

## Misuse patterns
- replaying arbitrary prior prompt text and calling it skill recovery
- folding marketplace discovery, installer flow, or skill registry policy into the post-compaction recovery seam
- treating post-compaction reattachment as proof that all previously loaded skill content survived unchanged
- using the technique to avoid writing explicit handoff, summary, or verification artifacts

## Detection signals
- recovered skills cannot be traced to current canonical source paths
- the recovery surface grows into full prompt reconstruction or memory recall
- reviewers cannot tell whether a skill was reattached, re-invoked, or guessed from stale context
- post-compaction failures disappear only after manually reloading the skill body

## Mitigations
- keep canonical skill source paths and reload commands explicit
- reattach or re-inject only bounded skill availability or bounded skill content, not arbitrary session history
- re-invoke a skill after compaction when exact instructions matter or when truncation is possible
- record the compaction boundary and recovered skill surface in a visible artifact when the session affects durable work
- route memory recall, marketplace curation, installer behavior, and context reconstruction into sibling techniques instead of widening this one

## Recommendation
- safe to promote as a canonical recovery technique when the implementation keeps recovery bounded to skill availability, reattachment, and explicit reload from canonical sources
- do not use the canonical status as approval for hidden state replay, long-term memory, automatic skill installation, or full prompt reconstruction
