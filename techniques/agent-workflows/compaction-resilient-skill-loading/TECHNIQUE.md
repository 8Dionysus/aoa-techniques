---
id: AOA-T-0054
name: compaction-resilient-skill-loading
domain: agent-workflows
kind: handoff
status: promoted
origin:
  project: joshuadavidthomas/opencode-agent-skills
  path: README.md + src/plugin.ts + src/skills.ts + .opencode/command/test-compaction.md
  note: Adapted from the open-source opencode-agent-skills plugin, which listens for session compaction and re-injects a bounded skills-availability surface so agents can rediscover and reload skills from canonical sources.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - skills
  - compaction
  - recovery
  - context
summary: Re-seed skill availability after context compaction so agents can reload needed skills from canonical sources without widening into full context reconstruction or prompt stuffing.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-28
export_ready: true
relations:
  - type: complements
    target: AOA-T-0040
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

# compaction-resilient-skill-loading

## Intent

Restore a bounded skill-availability surface after context compaction so the session can rediscover and reload needed skills from canonical sources instead of losing capability context or silently rebuilding the whole prompt state.

## When to use

- long-running sessions are expected to compact older context
- skills are real capability artifacts with canonical sources
- post-compaction sessions still need a visible path to reload needed skills
- the reusable object is compaction-bound skill recovery, not general context composition or memory recall

## When not to use

- the real problem is how skills or context are authored before runtime
- the workflow needs deterministic multi-fragment context composition across the whole repo
- the system would silently replay arbitrary prompt history or hidden state after compaction
- exact restoration of all previously loaded content is required rather than bounded rediscovery and reload
- skills are not actually canonical capability sources

## Inputs

- one canonical skill source or discoverable skill set
- one explicit compaction event or reduced-context boundary
- one bounded post-compaction bootstrap surface such as an available-skills list or equivalent reminder
- one reload path that can pull specific needed skills from canonical sources
- optional baseline bootstrap skills that must survive as part of the narrow contract

## Outputs

- one refreshed post-compaction skill-availability surface
- one explicit path for reloading needed skills from canonical sources
- lower risk that compaction erases capability discoverability
- one bounded recovery seam that stays smaller than full context reconstruction

## Core procedure

1. Name the compaction boundary explicitly instead of treating context loss as invisible background behavior.
2. Rediscover or re-read the canonical skill set after compaction.
3. Re-inject a small post-compaction bootstrap surface that tells the session which skills are available and how to reload them.
4. Reload only the skills that are still needed from canonical sources rather than replaying all prior prompt state.
5. Reset or drop any ephemeral loaded-skill bookkeeping that no longer matches the compacted session state.
6. Keep the recovered surface visible enough that reviewers can tell what capability context was restored.
7. Split broader context composition, memory recall, marketplace discovery, or installation behavior into sibling techniques when they become the real object.

## Contracts

- canonical skill sources remain authoritative
- compaction recovery is explicit rather than hidden
- the recovered surface restores discoverability or bounded bootstrap context, not arbitrary full session state
- needed skills can be reloaded from canonical sources after compaction
- post-compaction capability state remains more reviewable than silent prompt stuffing
- the technique stays smaller than full context reconstruction, memory recall, or product-width skill management

Relationship to adjacent techniques: unlike [AOA-T-0012](../../docs/deterministic-context-composition/TECHNIQUE.md) and [AOA-T-0030](../../docs/fragmented-agent-context/TECHNIQUE.md), this technique does not own how context or skill files are authored and composed before runtime. Unlike [AOA-T-0027](../../docs/cross-agent-skill-propagation/TECHNIQUE.md), it does not fan one canonical skill source out to many managed targets. Unlike [AOA-T-0040](../../docs/skill-vs-command-boundary/TECHNIQUE.md), it does not define what a skill is; it assumes bounded skill artifacts already exist and keeps them reloadable after compaction.

## Risks

### Failure modes

- the wrong skill list is reintroduced after compaction
- compaction recovery silently replays more prompt state than intended
- post-compaction sessions cannot tell which skills are actually available again
- recovery logic depends on stale in-memory bookkeeping rather than canonical sources

### Negative effects

- operators may assume every previously loaded skill body was preserved when only discoverability was restored
- compaction recovery can feel magical if the injected bootstrap surface is too hidden
- skill recovery can drift into general prompt-restoration doctrine if its boundary is not kept tight

### Misuse patterns

- treating any repeated prompt text as a skill worth replaying after compaction
- rebuilding the whole session context instead of a bounded skill-availability surface
- widening the technique into plugin installation, marketplace discovery, or general memory behavior

### Detection signals

- restored skills cannot be traced back to canonical sources
- reviewers cannot tell whether a post-compaction skill came from a bootstrap surface or stale hidden state
- the recovery path keeps growing beyond a short availability reminder plus explicit reload path
- discussions drift toward context composition, memory recall, or product setup rather than compaction recovery

### Mitigations

- keep canonical source paths explicit
- reintroduce only an availability surface or baseline bootstrap, not the whole prompt history
- make post-compaction recovery visible in session artifacts or equivalent review surfaces
- split composition, discovery, installation, and memory concerns into narrower sibling techniques

## Validation

Verify the technique by confirming that:
- a compaction event can happen without permanently losing skill discoverability
- post-compaction sessions can still identify or reload needed skills from canonical sources
- the recovered surface remains smaller than full context reconstruction
- restored skills or skill reminders trace back to a canonical source or manifest
- the explanation does not require marketplace, install, or memory doctrine to make sense

See `checks/compaction-resilient-skill-loading-checklist.md`.

## Adaptation notes

What can vary across projects:
- the exact compaction event or trigger
- the source locations used for skill discovery
- whether the bootstrap surface is an available-skills list, a baseline reminder, or another bounded capability summary
- how explicit reload is invoked after compaction
- whether baseline bootstrap skills accompany the availability surface

What should stay invariant:
- compaction is named explicitly
- canonical skill sources remain authoritative
- post-compaction recovery stays bounded and reviewable
- capability rediscovery remains possible after compaction

Project-shaped details that should not be treated as invariant:
- one plugin runtime or SDK
- semantic-similarity matching or embeddings
- one Superpowers bootstrap mode
- marketplace cache layout or install commands
- hidden synthetic-message implementation details beyond the fact that recovery is explicit

## Public sanitization notes

This import narrows the donor repository to one bounded pattern: after context compaction, re-seed a small skills-availability surface so needed skills can be reloaded from canonical sources. Marketplace discovery, plugin installation, semantic matching, embeddings, Superpowers mode, and broader product semantics were intentionally left out of the public contract.

## Example

See `examples/minimal-compaction-resilient-skill-loading.md`.

## Checks

See `checks/compaction-resilient-skill-loading-checklist.md`.

## Promotion history

- adapted from open-source `joshuadavidthomas/opencode-agent-skills`
- staged through the chat wave 2 graph-review-mailbox lane inside `aoa-techniques`
- promoted into `aoa-techniques` on 2026-03-28 as a bounded external-import technique for post-compaction skill-availability recovery

## Future evolution

- keep general context composition as a separate docs-side sibling instead of widening this bundle into full prompt reconstruction
- keep marketplace discovery and install surfaces separate instead of folding them into recovery
- add a stronger second live context if another public repository uses the same bounded post-compaction skill-recovery seam in practice
