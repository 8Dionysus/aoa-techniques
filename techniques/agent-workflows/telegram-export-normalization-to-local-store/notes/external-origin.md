# External Origin Note

Use this note when a technique is adapted from an external open-source or public documentation source.
It complements `TECHNIQUE.md` and records provenance, adaptation boundaries, and public-safety review.

## Source

- source_repo: `https://github.com/LonamiWebs/Telethon` plus `https://github.com/tdlib/td` plus `https://github.com/thedemons/opentele` plus `https://github.com/MasterScrat/Chatistics` plus `https://github.com/knadh/tg-archive` plus `https://github.com/chaindead/telegram-mcp`
- source_license: `mixed donor family: MIT + BSL-1.0`
- inspired_by: not used in this import
- adapted_from: upstream README guidance from Telethon, TDLib, opentele, Chatistics, tg-archive, and telegram-mcp showing message retrieval, export or sync access, media handling, archive shaping, and local persistence over Telegram data

## What changed

- what_changed: narrowed the donor family to one bounded storage seam: Telegram-source messages and media are normalized into a resumable local object store with visible provenance
- reusable object extracted: one stable local message object contract plus media references, source references, and bounded resume state
- invariant core kept: source provenance stays visible, reply edges and media references survive, and auth remains outside the normalized storage contract
- project-shaped details removed or generalized: session-secret storage, auth bootstrap procedures, bot or agent-control behavior, donor runtime packaging, and memory-writeback posture
- nearest existing technique or overlap watch: `AOA-T-0026 session-capture-as-repo-artifact + telegram-account-auth-and-session-bridge`
- what stays out of the donor: auth handoff, session conversion, secret storage policy, memory ingestion, live control surfaces, and broader Telegram ops doctrine

## Public-safety review

- secrets or tokens removed: none from the donor surfaces used for this import; the public bundle intentionally excludes credential and session handling detail
- private paths, URLs, or IDs removed: none; the donor inputs are public upstream repositories and public README documentation
- environment-specific assumptions generalized: the public technique does not depend on one Telegram client library, one local database backend, one export file layout, or one agent runtime
- remaining public-safety concerns: the main risks are drift into auth or session doctrine on one side and drift into memory-ingestion or general history-capture doctrine on the other

## Review notes

- why this adaptation is reusable here: many workflows need Telegram-origin data to become a resumable local structured store before later search, routing, or review can happen
- downstream repo impact: later auth, agent-control, or memory workflows belong outside `aoa-techniques`, while this repository keeps only the reusable normalization contract
- limits or follow-up review concerns: this import still needs one second live adopter beyond the donor Telegram family and documentation-first adaptation before any canonical discussion is honest
