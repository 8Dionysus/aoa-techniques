# Canonical Readiness

## Technique
- id: AOA-T-0054
- name: compaction-resilient-skill-loading

## Verdict
- approve for canonical promotion

## Evidence summary
- external origin: the imported technique has a bounded donor contract and explicit exclusions around marketplace discovery, install flow, semantic matching, embeddings, and full prompt-state replay
- donor proof: `joshuadavidthomas/opencode-agent-skills` listens for a compaction event, re-injects the available skills list, and drops stale loaded-skill bookkeeping so the recovered surface is availability plus reload rather than hidden state survival
- second context: Claude Code's official skills documentation records a separate skill content lifecycle where invoked skills are carried through auto-compaction within budget, re-attached after summary, and can be re-invoked after compaction to restore full content if dropped or truncated
- adaptation fit: both source families keep canonical skill files authoritative and preserve post-compaction skill availability without requiring full context reconstruction, long-term memory, marketplace installation, or product-width skill management
- validation strength: the bundle now carries external origin, second-context adaptation, external import review, canonical readiness, checklist, example, and adverse-effects review support

## Default-use rationale
- this is the right canonical default when the main problem is keeping skill availability recoverable after compaction without silently replaying full prompt state
- it remains narrower than [AOA-T-0012](../../../../instruction/instruction-surface/deterministic-context-composition/TECHNIQUE.md) and [AOA-T-0030](../../../../instruction/instruction-surface/fragmented-agent-context/TECHNIQUE.md) because it only owns post-compaction recovery, not source-layer authoring or composition
- it also remains narrower than [AOA-T-0027](../../../../instruction/instruction-surface/cross-agent-skill-propagation/TECHNIQUE.md) because it restores one session's ability to reload skills instead of propagating a canonical source to many managed targets

## Fresh public-safety check
- review date: 2026-05-12
- result: pass
- sanitization still holds: the bundle keeps only the reusable post-compaction recovery seam and excludes plugin install, marketplace breadth, semantic matching, embeddings, donor runtime specifics, memory recall, and full context replay
- public reuse check: the example, checklist, adaptation notes, and Claude Code evidence remain understandable without hidden donor-repo or OS Abyss context

## Remaining gaps
- no promotion blocker remains for the current canonical claim
- future evidence may split sibling techniques only if the object becomes compaction-summary policy, memory recall, full context reconstruction, installer behavior, marketplace curation, or product-wide skill lifecycle governance

## Recommendation
- move `AOA-T-0054` to `canonical`
- keep future post-compaction work bounded to skill availability and explicit reload unless a narrower sibling object is reviewed separately
