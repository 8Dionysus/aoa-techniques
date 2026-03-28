# minimal-telegram-export-normalization-to-local-store

Normalized message object:
- `message_id: 18422`
- `chat_id: saved_messages`
- `timestamp: 2026-03-27T18:42:11Z`
- `sender: self`
- `reply_to_id: 18410`
- `text: check the invoice screenshots later`
- `media_refs[]`
  - `media/2026/03/receipt-18422.jpg`
- `source_kind: telegram_export`
- `source_path: exports/saved-messages/messages.json`

Resume metadata:
- `resume_cursor: 18422`
- `last_sync_at: 2026-03-27T18:43:00Z`

The point of the example is that Telegram-derived data becomes one stable local object contract.
It does not define auth, session, or memory policy.
