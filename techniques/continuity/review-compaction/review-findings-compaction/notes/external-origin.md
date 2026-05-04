# External Origin Note

## Source

- source_repo: `https://github.com/roborev-dev/roborev`
- source_license: MIT
- inspired_by: not used in this import
- adapted_from: `README.md`, `cmd/roborev/compact.go`, `internal/review/synthesis.go`, and `internal/review/synthesize.go`

## What changed

- what_changed: narrowed the donor repository to one bounded pattern: verify and consolidate open review findings against the current codebase so the active review surface stays smaller and fresher
- invariant core kept: duplicate or related findings are grouped, current code is checked before findings survive, and the output keeps only the current consolidated findings surface
- project-shaped details removed or generalized: post-commit trigger behavior, fix and refine loops, daemon/runtime specifics, queue UI, branch-wide job handling, and provider-specific synthesis wiring

## Public-safety review

- secrets or tokens removed: none from the donor surfaces used for this import
- private paths, URLs, or IDs removed: donor-specific job IDs, queue paths, runtime endpoints, and internal wiring details were generalized away
- environment-specific assumptions generalized: the public technique does not depend on one daemon, one synthesis agent, one local review runtime, or one queue implementation
- remaining public-safety concerns: the main risk is contract widening into remediation or issue-management doctrine, not data leakage

## Review notes

- why this adaptation is reusable here: many review workflows need a bounded pass that keeps current findings smaller and fresher before people or tools act on them
- limits or follow-up review concerns: this first import intentionally excludes trigger logic, fix loops, backlog policy, and broader platform behavior
