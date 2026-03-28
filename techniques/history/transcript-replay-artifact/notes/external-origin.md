# External Origin Note

Use this note when a technique is adapted from an external open-source or public documentation source.
It complements `TECHNIQUE.md` and records provenance, adaptation boundaries, and public-safety review.

## Source

- source_repo: `https://github.com/es617/claude-replay`
- source_license: `MIT`
- inspired_by: `https://github.com/wesm/agentsview`
- adapted_from: `README.md` from `es617/claude-replay`, plus `README.md` from `wesm/agentsview`

## What changed

- what_changed: narrowed the donors to one bounded seam: already-saved session history can be transformed into a replayable artifact for later review or presentation
- invariant core kept: replay begins after capture, preserves bounded flow cues, and remains derivative from saved source artifacts
- project-shaped details removed or generalized: viewer-product branding, publish flows, web app shells, dashboards, live monitoring, export products, and broader hosted viewer semantics

## Public-safety review

- secrets or tokens removed: none from the donor surfaces used for this import
- private paths, URLs, or IDs removed: donor sharing URLs, deployment details, and product-specific viewer configuration were omitted
- environment-specific assumptions generalized: the public technique does not depend on one viewer shell, one hosting path, or one product account model
- remaining public-safety concerns: the main risks are overlap with transcript packaging on one side and drift into hosted replay-platform doctrine on the other

## Review notes

- why this adaptation is reusable here: many teams need a replayable review object over already-saved session history without adopting a whole viewer product
- primary evidence used: the `claude-replay` README describes turning Claude Code, Cursor, and Codex transcripts into self-contained HTML replays, while the `agentsview` README shows a second public context where saved sessions can be exported and revisited through a richer viewing surface
- limits or follow-up review concerns: transcript packaging, history indexing, witness tracing, publish flows, and hosted viewer product behavior remain intentionally outside this import
