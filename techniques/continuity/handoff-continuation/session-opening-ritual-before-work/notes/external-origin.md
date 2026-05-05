# External Origin Note

Use this note when a technique is adapted from an external open-source or public documentation source.
It complements `TECHNIQUE.md` and records provenance, adaptation boundaries, and public-safety review.

## Source

- source_repo: `https://github.com/thebasedcapital/nightcrawler`
- source_license: `MIT`
- adapted_from: `README.md` and `skills/nightcrawler-episode.md` from `thebasedcapital/nightcrawler`

## What changed

- what_changed: narrowed the donor to one bounded workflow object: read the current session context and verify a visible baseline before the first mutation in a resumed session
- invariant core kept: session start includes a visible read step, one current-state check, and explicit mismatch handling before work continues
- project-shaped details removed or generalized: overnight mission framing, `STATE.json`, `MISSION.md`, `tasks.json`, launchd supervision, budget limits, autonomous task picking, baseline test and lint requirements, state updates, and broader orchestrator rules

## Public-safety review

- secrets or tokens removed: none from the donor surfaces used for this import
- private paths, URLs, or IDs removed: donor home-directory paths and launchd service paths were omitted
- environment-specific assumptions generalized: the public technique does not depend on one state-file family, one mission template, one collaboration mode, or one startup command suite
- remaining public-safety concerns: the main risks are drift into full startup doctrine on one side and drift into handoff verification or packet-authoring siblings on the other

## Review notes

- why this adaptation is reusable here: many multi-session coding workflows need one honest pre-mutation realignment step without importing a full mission harness or task-governance stack
- limits or follow-up review concerns: packet authoring, concrete git-claim verification, task selection, and baseline testing remain separate sibling surfaces rather than part of this import
