# Adverse Effects Review

## Technique
- id: AOA-T-0074
- name: telegram-export-normalization-to-local-store

## Review focus
- promotion from `promoted` to `canonical` after exact-fit public reinforcement from `3bl3gamer/tg_history_dumper`
- confirm that the bundle remains one bounded Telegram-source normalization and resumable local-store contract, not auth bootstrap, session conversion, account/session dumping, live client control, archive presentation, search, routing, recall, memory writeback, or a general history-artifact doctrine

## Failure modes
- message ids, chat ids, sender fields, reply edges, or media references are normalized away into flat text
- export and live-sync records are mixed without preserving source kind or resume boundary
- a resume cursor skips messages after interruption or replays already-stored records as duplicates
- media files are downloaded but lose their message-level source linkage
- related users or chats drift from the messages that need them for review

## Negative effects
- local stores can look like memory or canon even when they are only source-normalized evidence
- Telegram auth and session artifacts can leak into normalized output paths if the boundary is weak
- downstream search, routing, or archive viewers can pressure the technique into product behavior
- preserving Telegram-derived data can increase privacy and retention risk if the local store is treated casually
- generic history-capture language can erase the source-specific constraints that make this technique useful

## Misuse patterns
- treating the normalized store as final memory, recall truth, or curated archive by default
- placing session files, auth secrets, API credentials, or account/session dumps beside normalized message objects
- using this bundle as a Telegram control-plane, scraper, bot automation, or archive publishing recipe
- collapsing media, reply, peer, and source provenance into a lossy CSV or text-only export while still claiming the technique
- importing donor viewer, search, deletion/edit sync, media cleanup, or database deployment behavior as invariant requirements

## Detection signals
- outputs lack stable message ids, chat/source ids, sender fields, reply references, media refs, or source kind
- resume after interruption produces missing, duplicated, or reordered message records
- docs start explaining auth bootstrap, session conversion, account scraping, or live client actions as part of the technique
- examples center search UX, archive publishing, memory ingestion, or routing rather than normalized local objects
- media files cannot be traced back to the message and chat that produced them

## Mitigations
- keep one stable message object contract with visible Telegram/source identifiers
- preserve media references and peer surfaces as reviewable companions to messages
- keep resume state explicit and test interruption/restart behavior against duplicates and gaps
- store auth/session/account artifacts outside the normalized local object surface
- route search, archive presentation, routing, recall, memory writeback, deletion/edit sync, and viewer behavior to sibling techniques or owner repos

## Recommendation
- safe to promote as a canonical agent-workflow ingest technique when Telegram-derived message objects, media references, peer/source provenance, and resume state remain visible before later policy or action layers begin
- keep future revisions narrow: do not absorb auth bootstrap, session conversion, account/session dumping, search products, archive presentation, database deployment doctrine, media cleanup, deletion/edit sync, routing, recall, memory writeback, or broad history-artifact ownership into this bundle
