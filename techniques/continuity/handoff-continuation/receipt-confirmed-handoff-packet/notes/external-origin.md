# External Origin Note

Use this note when a technique is adapted from an external open-source or public documentation source.
It complements `TECHNIQUE.md` and records provenance, adaptation boundaries, and public-safety review.

## Source

- source_repo: `https://github.com/jeremiah-k/agor`
- source_license: `AGOR ships an MIT-derived attribution license in-repo, while GitHub metadata reports NOASSERTION`
- inspired_by: `https://github.com/ax-platform/ax-platform-mcp`
- adapted_from: `docs/snapshots.md` from `jeremiah-k/agor`, plus `docs/features.md` and `docs/examples.md` from `ax-platform/ax-platform-mcp`

## What changed

- what_changed: narrowed the donors to one bounded seam: once a handoff packet exists, the receiving side records explicit receipt before continuation
- invariant core kept: the packet is reviewed through a visible receiving-side acknowledgment, the receipt is separate from delivery, and continuation remains gated until receipt appears
- project-shaped details removed or generalized: AGOR snapshot tooling, `.agor/agentconvo.md`, coordination logs, strategy layers, aX task routing, wait-mode transport details, auto-assignment logic, and broader platform presence or queue semantics

## Public-safety review

- secrets or tokens removed: none from the donor surfaces used for this import
- private paths, URLs, or IDs removed: platform endpoints, repo-local coordination paths, and task IDs were omitted
- environment-specific assumptions generalized: the public technique does not depend on one threading system, one task tool, or one coordination log path
- remaining public-safety concerns: the main risks are drift into mailbox transport on one side and drift into broader handoff governance or approval workflow doctrine on the other

## Review notes

- why this adaptation is reusable here: multi-session and multi-agent workflows often need visible acceptance of a handoff packet, not just packet creation or message delivery
- limits or follow-up review concerns: packet authoring, transport, truth verification, and broader continuation or rejection policy remain separate sibling surfaces rather than part of this import
