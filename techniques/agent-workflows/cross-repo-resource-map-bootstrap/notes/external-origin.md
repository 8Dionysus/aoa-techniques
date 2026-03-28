# External Origin Note

Use this note when a technique is adapted from an external open-source or public documentation source.
It complements `TECHNIQUE.md` and records provenance, adaptation boundaries, and public-safety review.

## Source

- source_repo: `https://github.com/yan5xu/code-relay`
- source_license: `MIT`
- adapted_from: `README.md`, `local/orchestrator/ALWAYS/RESOURCE-MAP.yml`, and `github/orchestrator/ALWAYS/RESOURCE-MAP.yml` from `yan5xu/code-relay`

## What changed

- what_changed: narrowed the donor to one bounded workflow object: a task-bounded cross-repo resource map that names which repos and surfaces matter before the next step begins
- invariant core kept: startup context stays explicit across repo boundaries, repo roles are named, and the next reader can identify where to look first
- project-shaped details removed or generalized: organization metadata, project-board metadata, worktree conventions, infrastructure inventories, local versus GitHub collaboration modes, boot-sequence steps, and the broader workspace platform model

## Public-safety review

- secrets or tokens removed: none from the donor surfaces used for this import
- private paths, URLs, or IDs removed: donor organization placeholders, example git URLs, and global orchestrator paths were omitted
- environment-specific assumptions generalized: the public technique does not depend on one `RESOURCE-MAP.yml` location, one collaboration mode, or one workspace layout
- remaining public-safety concerns: the main risks are drift into a full architecture or infrastructure inventory on one side and drift into broader startup doctrine on the other

## Review notes

- why this adaptation is reusable here: multi-repo coding work often needs one bounded startup index for where to look across repos before deeper continuation begins
- limits or follow-up review concerns: semantic context mapping, startup rituals, infrastructure inventories, and platform coordination semantics remain separate sibling surfaces rather than part of this import
