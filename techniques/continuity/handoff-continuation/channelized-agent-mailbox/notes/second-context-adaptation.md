# Second Context Adaptation

## Technique
- id: AOA-T-0056
- name: channelized-agent-mailbox

## Target project
- name: aoa-techniques
- environment: public technique repository with authored bundle contracts, generated routing surfaces, and validator-backed markdown discipline
- runtime: documentation-first corpus that records one bounded mailbox transport seam rather than shipping the donor's binary format, CLI surface, MCP server, or product packaging
- external reinforcement:
  - name: mycel
  - repository: `heurema/mycel`
  - observed revision: `4ffa460f3f5efe36f31ef064f26c514ac703ae7b`
  - license: MIT
  - public surfaces: `README.md`, `docs/architecture.md`, `docs/rfc-v0.2-phase0-contracts.md`, `docs/plan-local-agent-mesh.md`, `src/cli/inbox.rs`, `src/cli/thread.rs`, `src/sync.rs`, `src/store/mod.rs`, `tests/integration.rs`, and `tests/outbox_test.rs`
  - adjacent contrast: `Dicklesworthstone/mcp_agent_mail` at `0fd616a00161da7802594fa4e1e9aa0a8f5fa1ef` shows a close mail-like agent coordination lane with explicit `acknowledge_message`, but its license rider makes it unsuitable as the primary clean canonical evidence source for this public bundle

## What changed

- paths: the donor uses `.acomm` storage, CLI commands, MCP tools, and channel-management APIs; this adaptation keeps the generic named-channel mailbox contract without depending on one transport implementation
- services: pub/sub tooling, broadcast behavior, analytics, trust and consent surfaces, and installer flows were removed from the reusable contract
- dependencies: the adaptation depends on visible channel identity, ordered replay, and explicit acknowledgment rather than on one server, one SDK, or one file format
- operating assumptions: contributors should read the technique as a bounded communication seam before handoff or policy layers, not as messaging-platform adoption guidance

## What stayed invariant

- contract: one named mailbox channel keeps messages durable enough for ordered replay and explicit acknowledgment
- validation logic: a receiver can resume from a visible cursor or equivalent last-seen marker and leave behind inspectable ack state
- safety rules: the technique remains outside handoff authorization, transcript packaging, history indexing, and wider platform doctrine
- external reinforcement: `mycel` keeps an AI-agent mailbox with thread identity, stable `msg_id`, `thread_id`, ordered thread log, sync cursor, local outbox retry, read/delivery state, and local ACK rows keyed by logical message id; its caveat is that ACK tracking is local and experimental rather than a remote delivery-confirmation guarantee

## Risks introduced by adaptation

- the pattern can collapse into the active `phase-synchronized-agent-handoff` narrowing lane if repositories stop separating mailbox delivery from continuation permission
- teams may over-associate the pattern with a full communication product because the donor also bundles pub/sub, trust, federation, analytics, and installation surfaces
- the public bundle could drift into history or transcript doctrine if replay logs are treated as post-capture artifacts instead of as live mailbox transport
- clean evidence can be confused with broad messaging-platform evidence; `MCP Agent Mail` is useful as an adjacent signal, but its license posture and broader agent-coordination surface should not become the bundle's canonical source

## Evidence

- the donor README states that agents communicate through named channels with message ordering, delivery acknowledgment, and replay capability
- the same README frames the reusable center as persistent local communication that survives restarts and session gaps
- `GUIDE.md` shows channel create, send, receive, and search flows as explicit operator-visible mailbox actions
- `crates/agentic-comm/src/channel.rs` implements named-channel lifecycle and validates channel identity as a stable object
- `docs/public/SCENARIOS-AGENTIC-COMM.md` describes concurrent ordered delivery, self-messaging, and ack timeout scenarios, reinforcing that ordering and acknowledgment are part of the bounded contract
- `mycel` describes itself as an encrypted async mailbox for AI CLI agents and keeps the product boundary as "mailbox, not messenger" with sync-on-command behavior, local-first same-user delivery, and transport-neutral mailbox state.
- `mycel` exposes machine-readable inbox rows with `msg_id`, `thread_id`, `reply_to`, `read_status`, and `delivery_status`, giving receivers a stable replay and review surface.
- `mycel` stores outbound messages before sending, retries relay delivery, maintains per-relay sync cursors, and uses set reconciliation or overlap-window fetches so missed messages can be recovered without a long-running daemon.
- `mycel thread` creates bounded thread IDs, sends messages to thread members, and logs thread messages ordered by creation time with logical message IDs.
- `mycel` records local ACK rows keyed by the original logical `msg_id` when ACK tracking is enabled, and its tests verify ACK insertion and duplicate-control behavior while explicitly limiting ACK semantics to local tracking in the current release.
- `MCP Agent Mail` was inspected as an adjacent close fit because it has agent identities, inbox/outbox, searchable threads, and explicit `acknowledge_message`; it is not used as primary evidence because the license rider is not clean for this public canonical proof role.

## Result

- works across donor, documentation-first, and `mycel` contexts while preserving one bounded channelized mailbox contract: named mailbox or thread lane, ordered replay or sync cursor, and explicit local acknowledgment state. It does not carry over donor platform breadth, full messaging-product features, encryption or trust policy, remote ACK guarantees, adapters, transcript history, or handoff authorization.
