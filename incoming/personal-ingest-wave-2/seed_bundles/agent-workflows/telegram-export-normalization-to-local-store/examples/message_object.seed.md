# message object seed

Example normalized Telegram object:

- `message_id`
- `timestamp`
- `sender`
- `reply_to_id`
- `text`
- `media_refs[]`
- `source_kind`
- `source_path`

The technique normalizes to a local store.
It does not define auth, session, or memory policy.
