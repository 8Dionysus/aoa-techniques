# External Origin Note

Use this note when a technique is adapted from an external open-source or public documentation source.
It complements `TECHNIQUE.md` and records provenance, adaptation boundaries, and public-safety review.

## Source

- source_repo: `https://github.com/agentralabs/agentic-comm`
- source_license: `MIT`
- inspired_by: not used in this import
- adapted_from: `README.md`, `GUIDE.md`, `crates/agentic-comm/src/channel.rs`, and `docs/public/SCENARIOS-AGENTIC-COMM.md`

## What changed

- what_changed: narrowed the donor to one bounded mailbox pattern: named channels plus ordered replay and explicit acknowledgment for durable agent communication
- invariant core kept: a bounded coordination lane uses one named channel, messages remain replayable in order, and receipt or handling becomes visible through explicit ack state
- project-shaped details removed or generalized: `.acomm` file format specifics, MCP tool taxonomy, pub/sub wildcard semantics, broadcast scaling, trust and consent layers, benchmark claims, installer flows, and broader messaging-platform product behavior

## Public-safety review

- secrets or tokens removed: none from the donor surfaces used for this import
- private paths, URLs, or IDs removed: donor install URLs, platform-specific commands, and storage implementation details were omitted
- environment-specific assumptions generalized: the public technique does not depend on one binary format, one local file extension, one MCP client, or one SDK
- remaining public-safety concerns: the main risks are overlap with handoff-governance doctrine on one side and drift into full messaging-platform breadth on the other

## Review notes

- why this adaptation is reusable here: many multi-agent or multi-session workflows need one durable mailbox seam before they need a full orchestration or messaging stack
- limits or follow-up review concerns: this import intentionally excludes pub/sub topic governance, federation, trust and consent layers, channel analytics, benchmark posture, and donor product semantics
