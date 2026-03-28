# minimal transcript-replay-artifact

Saved source artifact:

```text
sessions/2026-03-28-parser-fix.jsonl
```

Replay artifact:

```text
docs/replays/parser-fix-session.html
```

Bounded replay metadata:

```json
{
  "source_session": "2026-03-28-parser-fix",
  "message_count": 42,
  "replay_format": "html",
  "redacted": true
}
```

Why this example stays bounded:

- the replay starts from an already-saved session file
- the replay artifact remains a derivative review object
- the example does not depend on hosted sharing, live collaboration, or dashboard product behavior
