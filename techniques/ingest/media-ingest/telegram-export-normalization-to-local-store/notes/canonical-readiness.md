# Canonical Readiness

## Technique
- id: AOA-T-0074
- name: telegram-export-normalization-to-local-store

## Verdict
- approve for canonical promotion

## Evidence summary

- external origin: the imported technique has a bounded donor contract and explicit exclusions around auth bootstrap, session conversion, secret storage, control-plane behavior, and memory writeback
- second context: `aoa-techniques` now records the same Telegram-normalization seam as a documentation-first adaptation with one example and one checklist
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- `3bl3gamer/tg_history_dumper` provides exact-fit public reinforcement beyond the original donor Telegram family and repo-local documentation-first adaptation: it exports messages as JSON Lines plus media from dialogs, groups, and channels; fetches only messages newer than the last already-fetched item; resumes interrupted file downloads; stores messages under chat-specific local paths; keeps related users and chats as JSON Lines peer surfaces; records a Telegram API layer marker on saved message objects; reads the last saved message id from the append-only local file; requests history with `OffsetID = lastMsgID + 1`; derives media file paths from chat id, message id, filename, and media source; and keeps account/auth/session dumps as optional surfaces rather than as the normalized message-store contract
- the inspected source is MIT licensed at commit `0058ab229043fc4af6b1859e0c367b9fd9b10d93` with commit date `2025-12-26T16:03:26+03:00`; inspected files include `README.md` (`61a3cada6eff63870cb5053dc5e456aeff4d3ccc`), `LICENSE` (`f75c3d5bbf2642271beb9a055f605f91768fe36f`), `saver.go` (`79545c068c6f62e9856aff8c97f4b123e3b8718c`), `main.go` (`5fa731efab9246c4a2b45b3e9d27e636d5964e80`), `tg.go` (`07d17b5c9cdf54626cbb8dbe111784a2d5f7a900`), `config.go` (`b096423b8b4eb1420afcc9d8b8623ec0f40402a8`), and `preview.go` (`d1a857589e7fdbad5be59b186460ca08a020e62a`)
- adjacent lanes were checked and kept out of the canonical proof: `GeiserX/Telegram-Archive` strongly reinforces incremental local Telegram backup pressure but is product-heavy around viewer, auth setup, realtime sync, deletion/edit sync, deduplication, and database deployment; `jackwener/tg-cli` reinforces local-first SQLite sync/search/export but is weaker on media-reference preservation and also includes live send/listen operations; `groupultra/telegram-search` reinforces core message/media/reply normalization but widens into search, embedding, web app, and storage service behavior; one-off HTML/CSV/Markdown converters and marketing/member-scraper projects were rejected as too narrow, too lossy, or outside the provenance-preserving local-store seam
- validation strength: the bundle now carries one checklist, one example, a clean external-origin note, a documentation-first second context, an import review, and live public cross-context reinforcement that repeats bounded Telegram-derived local storage outside the original donor README family

## Default-use rationale

- this is the right canonical default when the main problem is turning Telegram-origin data into stable local objects with visible provenance and resumable storage
- it remains narrower than [AOA-T-0026](../../../../history/history-artifacts/session-capture-as-repo-artifact/TECHNIQUE.md) because it does not own general project history capture or publication as review artifacts
- it also remains narrower than `telegram-account-auth-and-session-bridge` because it does not handle credentials, session conversion, or bootstrap approval
- it is now strong enough as a canonical default because the second public context repeats the key shape: Telegram messages are serialized into local append-only objects, media is preserved as message-linked files, related peers remain inspectable, and last-seen ids support continuation without turning the technique into auth, session, search, viewer, archive-product, or memory doctrine

## Fresh public-safety check

- review date: 2026-05-12
- result: pass
- sanitization still holds: the bundle keeps only the reusable normalization seam and excludes auth procedures, session secrets, session conversion, account/session dumps, live client control, viewer/UI behavior, search products, database deployment choices, media cleanup, deletion/edit sync, archive publication, and memory policy
- public reuse check: the example, checklist, and adaptation notes remain understandable without hidden donor-repo context; `3bl3gamer/tg_history_dumper` is cited only as public evidence, and the technique does not copy its Go source, Telegram client setup, session file handling, preview server, config schema, account/contact/session dumps, or download implementation

## Remaining gaps

- no blocker remains for canonical status
- future sources can reinforce the default, but they must preserve the narrow boundary: Telegram-derived message objects, media references, peer/source provenance, append-only or resumable local storage, and a stop-line before auth bootstrap, session conversion, account/session dumps, search products, archive presentation, deletion/edit sync, curation, routing, recall, or memory writeback

## Recommendation

- move `AOA-T-0074` to `canonical`
- add an adverse-effects review to preserve the boundary between Telegram-source normalization, media storage, resume state, auth/session surfaces, archive products, search, routing, recall, and memory writeback
