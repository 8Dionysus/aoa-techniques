# Second Context Adaptation

## Technique
- id: AOA-T-0056
- name: channelized-agent-mailbox

## Target project
- name: aoa-techniques
- environment: public technique repository with authored bundle contracts, generated routing surfaces, and validator-backed markdown discipline
- runtime: documentation-first corpus that records one bounded mailbox transport seam rather than shipping the donor's binary format, CLI surface, MCP server, or product packaging

## What changed

- paths: the donor uses `.acomm` storage, CLI commands, MCP tools, and channel-management APIs; this adaptation keeps the generic named-channel mailbox contract without depending on one transport implementation
- services: pub/sub tooling, broadcast behavior, analytics, trust and consent surfaces, and installer flows were removed from the reusable contract
- dependencies: the adaptation depends on visible channel identity, ordered replay, and explicit acknowledgment rather than on one server, one SDK, or one file format
- operating assumptions: contributors should read the technique as a bounded communication seam before handoff or policy layers, not as messaging-platform adoption guidance

## What stayed invariant

- contract: one named mailbox channel keeps messages durable enough for ordered replay and explicit acknowledgment
- validation logic: a receiver can resume from a visible cursor or equivalent last-seen marker and leave behind inspectable ack state
- safety rules: the technique remains outside handoff authorization, transcript packaging, history indexing, and wider platform doctrine

## Risks introduced by adaptation

- the pattern can collapse into the active `phase-synchronized-agent-handoff` narrowing lane if repositories stop separating mailbox delivery from continuation permission
- teams may over-associate the pattern with a full communication product because the donor also bundles pub/sub, trust, federation, analytics, and installation surfaces
- the public bundle could drift into history or transcript doctrine if replay logs are treated as post-capture artifacts instead of as live mailbox transport

## Evidence

- the donor README states that agents communicate through named channels with message ordering, delivery acknowledgment, and replay capability
- the same README frames the reusable center as persistent local communication that survives restarts and session gaps
- `GUIDE.md` shows channel create, send, receive, and search flows as explicit operator-visible mailbox actions
- `crates/agentic-comm/src/channel.rs` implements named-channel lifecycle and validates channel identity as a stable object
- `docs/public/SCENARIOS-AGENTIC-COMM.md` describes concurrent ordered delivery, self-messaging, and ack timeout scenarios, reinforcing that ordering and acknowledgment are part of the bounded contract

## Result

- works as a documentation-first second context and preserves one bounded named-channel mailbox contract without carrying over the donor's platform breadth, file format specifics, or orchestration semantics
