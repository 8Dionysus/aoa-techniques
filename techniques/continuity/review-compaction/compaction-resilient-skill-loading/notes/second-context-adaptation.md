# Second Context Adaptation

## Technique
- id: AOA-T-0054
- name: compaction-resilient-skill-loading

## Target project
- name: aoa-techniques
- environment: public technique repository with authored bundle contracts, generated routing surfaces, and validator-backed markdown discipline
- runtime: documentation-first corpus that records one bounded post-compaction recovery contract rather than shipping the donor plugin, skill tools, or runtime event system

## What changed
- paths: the donor uses an OpenCode plugin with discovery paths, tool wiring, and synthetic-message injection; this adaptation keeps the generic compaction boundary plus bounded skill-availability recovery contract without depending on one runtime
- services: marketplace discovery, install flow, semantic matching, embeddings, and optional Superpowers bootstrap were removed from the reusable contract
- dependencies: the adaptation depends on canonical skill sources and one explicit compaction event, not on the donor plugin stack
- operating assumptions: contributors should read the technique as a post-compaction recovery seam for skill availability, not as product setup guidance

## What stayed invariant
- contract: after compaction, the session receives a small skill-availability recovery surface so needed skills can be reloaded from canonical sources
- validation logic: skill availability survives compaction through explicit rediscovery and bootstrap, not through hidden full-state replay
- safety rules: canonical skill sources stay authoritative, and the technique remains outside full context composition, marketplace, and memory semantics

## Risks introduced by adaptation
- the pattern can collapse back into [AOA-T-0012](../../../../instruction/instruction-surface/deterministic-context-composition/TECHNIQUE.md) or [AOA-T-0030](../../../../instruction/instruction-surface/fragmented-agent-context/TECHNIQUE.md) if repositories cannot explain what recovery adds after context has already been authored
- teams may over-associate the technique with general skill discovery because the donor plugin also handles discovery, matching, and tool exposure
- the public bundle could drift into hidden-state replay if contributors forget that the donor explicitly resets ephemeral loaded-skill bookkeeping after compaction

## Evidence
- the donor README lists `Compaction resilient - Skills survive context compaction in long sessions` as a headline feature
- the same README says the plugin listens for `session.compacted` events and re-injects the available skills list so the agent maintains access to skills throughout long sessions
- the donor `event` handler for `session.compacted` calls `injectSkillsList(...)` and then deletes `loadedSkillsPerSession`, which shows the recovery seam restores bounded availability rather than pretending exact prior skill state survived untouched
- the donor test command `test-compaction.md` verifies the re-injected skills list remains visible and that `use_skill` still works after manual compaction
- Claude Code's official skills documentation at `https://code.claude.com/docs/en/skills` (accessed 2026-05-12) records an independent skill content lifecycle: invoked skills load into the conversation, auto-compaction carries invoked skills forward within a token budget, compaction re-attaches recent skill invocations after the summary, and a dropped or truncated skill can be re-invoked after compaction to restore the full content
- the Claude Code surface is exact-fit second-context evidence because it treats post-compaction skill recovery as bounded skill-content availability and reload behavior, not as long-term memory, marketplace installation, arbitrary prompt-history replay, or full context reconstruction

## Result
- works as a cross-context adaptation: the donor plugin and Claude Code skill lifecycle both preserve the same bounded post-compaction skill-recovery contract while rejecting plugin-host, marketplace, long-term memory, and product-width context restoration behavior
