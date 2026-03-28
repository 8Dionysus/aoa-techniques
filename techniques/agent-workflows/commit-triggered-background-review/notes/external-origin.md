# External Origin Note

## Source

- source_repo: `https://github.com/roborev-dev/roborev`
- source_license: MIT
- inspired_by: not used in this import
- adapted_from: `README.md`, `cmd/roborev/postcommit.go`, `cmd/roborev/review.go`, and `internal/review/result.go`

## What changed

- what_changed: narrowed the donor repository to one bounded pattern: a visible commit boundary triggers an asynchronous review run that emits inspectable findings as an artifact
- invariant core kept: post-commit review is triggered after a visible commit boundary, findings survive as an artifact tied to the reviewed commit, and remediation stays outside the review run
- project-shaped details removed or generalized: auto-fix and refine loops, TUI review queue, alerting hooks, daemon/runtime specifics, provider-specific prompt wiring, and broader event automation

## Public-safety review

- secrets or tokens removed: none from the donor surfaces used for this import
- private paths, URLs, or IDs removed: donor-specific job IDs, queue paths, runtime endpoints, and internal wiring details were generalized away
- environment-specific assumptions generalized: the public technique does not depend on one daemon, one TUI, one agent provider, or one local review runtime
- remaining public-safety concerns: the main risk is contract widening into remediation or CI-governance doctrine, not data leakage

## Review notes

- why this adaptation is reusable here: many repositories want review to happen automatically after commits while still keeping findings inspectable before any action is taken
- limits or follow-up review concerns: this first import intentionally excludes auto-fix loops, branch-wide policy enforcement, dashboard behavior, and alert or queue product semantics
