# External Origin Note

Use this note when a technique is adapted from an external open-source or public documentation source.
It complements `TECHNIQUE.md` and records provenance, adaptation boundaries, and public-safety review.

## Source

- source_repo: `https://github.com/wesm/agentsview`
- source_license: `MIT`
- inspired_by: not used in this import
- adapted_from: `README.md`, `internal/db/search.go`, `internal/db/sessions.go`, and `internal/server/search.go`

## What changed

- what_changed: narrowed the donor to one bounded post-capture pattern: already-saved AI session artifacts can be discovered locally, synchronized into a local searchable index, and reopened through stable references back to the source artifacts
- invariant core kept: the index is local-first, derived from existing artifacts, searchable by text or metadata, and subordinate to the saved source artifacts
- project-shaped details removed or generalized: desktop and web shells, analytics dashboards, live SSE updates, export and publish flows, PostgreSQL sync, reverse-proxy setup, and wider product configuration doctrine

## Public-safety review

- secrets or tokens removed: none from the donor surfaces used for this import
- private paths, URLs, or IDs removed: donor product URLs, installation commands, browser publication settings, and reverse-proxy examples were omitted
- environment-specific assumptions generalized: the public technique does not depend on one UI shell, one database engine, or one hosted access path
- remaining public-safety concerns: the main risks are overlap with capture on one side and drift into dashboard, analytics, or memory-style authority on the other

## Review notes

- why this adaptation is reusable here: many repositories can benefit from a local searchable index over already-saved session artifacts without needing the donor's full product surface
- limits or follow-up review concerns: this import intentionally excludes session capture, transcript export, analytics dashboards, publish flows, PostgreSQL sync, and hosted multi-machine viewing
