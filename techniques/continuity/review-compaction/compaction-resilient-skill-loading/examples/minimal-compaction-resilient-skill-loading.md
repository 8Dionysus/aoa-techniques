# Minimal compaction-resilient skill loading

Before compaction:

- the session has already seen an `<available-skills>` block listing `checks` and `release-notes`
- the agent previously loaded `checks`

After compaction:

- older injected context is no longer safe to assume
- the session receives a fresh `<available-skills>` block derived from canonical skill sources

Recovery step:

- the agent re-evaluates which skills are needed
- the agent reloads `checks` from its canonical skill source

The recovery surface is intentionally smaller than replaying the whole prior prompt history.
