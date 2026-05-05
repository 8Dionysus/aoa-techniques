# External Origin Note

Use this note when a technique is adapted from an external open-source or public documentation source.
It complements `TECHNIQUE.md` and records provenance, adaptation boundaries, and public-safety review.

## Source

- source_repo: `https://github.com/thebasedcapital/nightcrawler`
- source_license: `MIT`
- inspired_by: `https://github.com/jeremiah-k/agor`
- adapted_from: `README.md` and `skills/nightcrawler-episode.md` from `thebasedcapital/nightcrawler`, plus `docs/snapshots.md` from `jeremiah-k/agor`

## What changed

- what_changed: narrowed the donors to one bounded seam: before continuing from a handoff, check its concrete repo claims against visible git state
- invariant core kept: receiving-side trust is anchored to recent commits or diffs, mismatches stay visible, and continuation follows repo evidence over handoff narration
- project-shaped details removed or generalized: overnight episode loops, mission state files, `.agor` snapshot tooling, coordination logs, version checks, baseline-test doctrine, and broader review or provenance systems

## Public-safety review

- secrets or tokens removed: none from the donor surfaces used for this import
- private paths, URLs, or IDs removed: donor home-directory paths, coordination-log paths, and repo-specific branch details were omitted
- environment-specific assumptions generalized: the public technique does not depend on one orchestrator, one handoff path, or one exact git command
- remaining public-safety concerns: the main risks are drift into generic code review on one side and drift into packet-authoring or broader provenance doctrine on the other

## Review notes

- why this adaptation is reusable here: long-running coding workflows often need one small trust check between a handoff summary and the actual repo before work resumes
- limits or follow-up review concerns: packet authoring, receipt confirmation, baseline testing, witness export, and broad review governance remain separate sibling surfaces rather than part of this import
