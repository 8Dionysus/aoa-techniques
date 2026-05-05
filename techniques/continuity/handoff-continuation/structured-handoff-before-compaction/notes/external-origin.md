# External Origin Note

Use this note when a technique is adapted from an external open-source or public documentation source.
It complements `TECHNIQUE.md` and records provenance, adaptation boundaries, and public-safety review.

## Source

- source_repo: `https://github.com/thebasedcapital/nightcrawler`
- source_license: `MIT`
- inspired_by: `https://github.com/yan5xu/code-relay` README checkpoint and handoff framing used as supporting public-doc reinforcement for pre-compression continuation packets
- adapted_from: `README.md` and `skills/nightcrawler-episode.md` from `thebasedcapital/nightcrawler`, plus `README.md` from `yan5xu/code-relay`

## What changed

- what_changed: narrowed the donors to one bounded workflow object: a structured handoff artifact written before compaction or rollover so continuation stays explicit
- invariant core kept: the boundary is named before context loss, one handoff packet records completed work plus blocked or in-progress work and next work, and the next session reads that packet before continuing
- project-shaped details removed or generalized: overnight mission framing, launchd supervision, budget caps, immutable `tasks.json`, `STATE.json`, macOS-specific paths, worktree isolation, local versus GitHub collaboration modes, and broader orchestration or boot stacks

## Public-safety review

- secrets or tokens removed: none from the donor surfaces used for this import
- private paths, URLs, or IDs removed: donor home-directory paths, launchd commands, and project-specific workspace layout were omitted
- environment-specific assumptions generalized: the public technique does not depend on one `HANDOFF.md` location, one orchestrator, one checkpoint file family, or one session runner
- remaining public-safety concerns: the main risks are drift into transcript packaging on one side and drift into continuation-governance or delivery protocol doctrine on the other

## Review notes

- why this adaptation is reusable here: many long-running coding workflows need one explicit continuation packet before compaction without needing a full transcript, witness trace, or orchestration framework
- limits or follow-up review concerns: git verification, receipt acknowledgment, mailbox transport, and broader phase-based continuation rules remain separate sibling surfaces rather than part of this import
