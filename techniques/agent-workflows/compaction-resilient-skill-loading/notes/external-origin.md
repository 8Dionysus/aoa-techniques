# External Origin Note

Use this note when a technique is adapted from an external open-source or public documentation source.
It complements `TECHNIQUE.md` and records provenance, adaptation boundaries, and public-safety review.

## Source

- source_repo: `https://github.com/joshuadavidthomas/opencode-agent-skills`
- source_license: `MIT`
- inspired_by: not used in this import
- adapted_from: `README.md`, `src/plugin.ts`, `src/skills.ts`, and `.opencode/command/test-compaction.md`

## What changed

- what_changed: narrowed the donor to one bounded post-compaction pattern: when session compaction happens, a small skills-availability surface is re-injected so needed skills can be rediscovered and reloaded from canonical sources
- invariant core kept: compaction is explicit, canonical skill sources remain authoritative, and the recovery surface stays smaller than full context reconstruction
- project-shaped details removed or generalized: plugin installation, marketplace cache layout, semantic-similarity matching, embeddings, Superpowers mode, and wider product tooling around skill discovery

## Public-safety review

- secrets or tokens removed: none from the donor surfaces used for this import
- private paths, URLs, or IDs removed: donor-specific install paths, cache directories, and environment-variable setup were omitted
- environment-specific assumptions generalized: the public technique does not depend on one plugin host, one SDK, or one hidden synthetic-message implementation
- remaining public-safety concerns: the main risks are overlap with context composition on one side and drift into memory, marketplace, or install doctrine on the other

## Review notes

- why this adaptation is reusable here: any long-running agent workflow with canonical skill sources and session compaction can benefit from a bounded post-compaction recovery seam
- limits or follow-up review concerns: this import intentionally excludes skill discovery breadth, marketplace semantics, plugin installation, semantic matching, and general prompt-restoration behavior
