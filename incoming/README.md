# Incoming

`incoming/` is the repo quarantine for public-safe candidate packets.

Nothing here is canon. Use this directory to inspect donor-wave accounting,
landed-bundle provenance, explicit exclusions, and final non-import verdicts
for material that was not safe to promote on the first pass.

## Current State

The first-pass landing queues in every current packet are exhausted.

| Packet | State | Closed tail |
|---|---|---|
| [chat-graph-review-mailbox](chat-graph-review-mailbox/README.md) | `evidence-only` | `markdown-definition-of-done-defaults` is `closed-no-import`; `shadow-epic-federation` and `typed-governance-obligation-ledger` are explicit exclusions |
| [chat-handoff-bounded-continuation](chat-handoff-bounded-continuation/README.md) | `evidence-only` | `governed-action-surfaces` remains an explicit exclusion |
| [chat-history-lineage-governed-actions](chat-history-lineage-governed-actions/README.md) | `evidence-only` | `agent-readiness-telemetry` and `signed-trace-artifacts` are `closed-no-import`; `cross-agent-session-browser` and `why-retrieval-from-code` are explicit exclusions |
| [chat-registry-discovery](chat-registry-discovery/README.md) | `evidence-only` | `semantic-linkage-records` is `closed-no-import`; five skill/registry spillovers are explicit exclusions |
| [chat-tool-proxy-runtime](chat-tool-proxy-runtime/README.md) | `evidence-only` | `preflight-reputation-check` is `closed-no-import`; six runtime/orchestration spillovers are explicit exclusions |
| [personal-media-ingest](personal-media-ingest/README.md) | `evidence-only` | `telegram-account-auth-and-session-bridge` is `closed-no-import` |

## How To Use This Directory

- Open a packet README when you need the compact status.
- Open `docs/*CLOSEOUT_MEMO.md` when you need the final non-import rationale
  for a closed candidate.
- Open `support/registry.json` when a machine-readable packet inventory is
  useful.
- Use the landed `techniques/**/TECHNIQUE.md` bundle for current technique
  meaning.
- Start a new Distillation intake only when fresh public evidence can name one
  bounded atom/topology route; do not revive a closed packet-local lane.

## Stop Line

Do not recreate packet-local `candidate_bundles/` for already landed
techniques. The old seed drafts were removed after landing so `incoming/` stays
evidence-only instead of duplicating canon.
