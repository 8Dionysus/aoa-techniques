# External Origin Note

Use this note when a technique is adapted from an external open-source or public documentation source.
It complements `TECHNIQUE.md` and records provenance, adaptation boundaries, and public-safety review.

## Source

- source_repo: `https://github.com/thebasedcapital/nightcrawler`
- source_license: `MIT`
- adapted_from: `README.md` and `skills/nightcrawler-episode.md` from `thebasedcapital/nightcrawler`

## What changed

- what_changed: narrowed the donor to one bounded workflow object: longer work is divided into explicit episodes with checkpoints and visible continue-or-stop decisions
- invariant core kept: episode boundaries are explicit, checkpoint state is reviewable, and continuation does not proceed silently past stop or escalation rules
- project-shaped details removed or generalized: launchd supervision, budget caps, mission templates, `STATE.json`, immutable `tasks.json`, crash recovery, cooldown timers, notifications, and the donor's total autonomous runtime

## Public-safety review

- secrets or tokens removed: none from the donor surfaces used for this import
- private paths, URLs, or IDs removed: donor home-directory paths and launchd service paths were omitted
- environment-specific assumptions generalized: the public technique does not depend on one mission harness, one state-file family, or one supervisor stack
- remaining public-safety concerns: the main risks are drift into a whole autonomous agent doctrine on one side and drift into handoff-artifact or startup-ritual siblings on the other

## Review notes

- why this adaptation is reusable here: long-running coding work often needs a bounded way to segment progress into reviewable slices without importing a whole autonomous system
- limits or follow-up review concerns: startup rituals, handoff packet structure, git verification, budgeting, supervision, and task integrity remain separate sibling surfaces rather than part of this import
