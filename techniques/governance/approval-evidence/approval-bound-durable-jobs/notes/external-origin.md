# External Origin Note

Use this note when a technique is adapted from an external open-source or public documentation source.
It complements `TECHNIQUE.md` and records provenance, adaptation boundaries, and public-safety review.

## Source

- source_repo: `https://github.com/Clyra-AI/gait`
- source_license: `Apache-2.0`
- inspired_by: not used in this import
- adapted_from: `docs/durable_jobs.md` and `README.md`

## What changed

- what_changed: narrowed the donor to one bounded seam: a longer-running job remains durable across checkpoint, approval, and resume instead of continuing implicitly
- invariant core kept: job identity survives pause and resume, approval is explicit before continuation, and durable state supports later inspection and resume
- project-shaped details removed or generalized: broader orchestration platform features, queue or scheduler semantics, trust product posture, pack formats, and wider governance stacks

## Public-safety review

- secrets or tokens removed: none from the donor surfaces used for this import
- private paths, URLs, or IDs removed: donor runtime names, environment-specific backends, and platform-specific job wiring were omitted
- environment-specific assumptions generalized: the public technique does not depend on one queue system, one job store, or one command family
- remaining public-safety concerns: the main risks are drift into scheduler-platform doctrine on one side and drift into broad governance or orchestration doctrine on the other

## Review notes

- why this adaptation is reusable here: many longer-running workflows need one bounded durable job seam across an explicit approval boundary without adopting a whole orchestration platform
- primary evidence used: the donor durable-jobs docs describe stable job identity plus status, checkpoint, approval, and resume surfaces, while the README reinforces the broader longer-running governed-job context that this import intentionally narrows
- limits or follow-up review concerns: immediate boundary gates, signed evidence, broader queueing semantics, and platform governance remain intentionally outside this import
