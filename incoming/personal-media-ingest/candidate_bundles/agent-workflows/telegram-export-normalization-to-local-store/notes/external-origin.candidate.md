# external-origin seed - telegram-export-normalization-to-local-store

## Donor spine

- Telethon
- TDLib
- opentele
- Chatistics
- tg-archive
- telegram-mcp

## Bounded pattern extracted

- Normalize Telegram messages and media into a resumable local store while keeping auth, session, and memory doctrine outside the technique boundary.

## What stays out

- session-secret storage policy
- auth bootstrap doctrine
- agent-control rhetoric
- automatic memory writeback

## Why narrower than the donors

- this seed extracts one reusable operational form
- it leaves implementation, runtime packaging, and donor worldview behind
- it does not claim the donor repo should be imported wholesale

## Expected evidence package if landed later

- `TECHNIQUE.md`
- `notes/external-origin.md`
- one minimal example or checklist
- release-path generated surfaces only after source markdown is accepted
