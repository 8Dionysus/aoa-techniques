# Donor Sources - Personal Ingest Wave 2

These are donor references for **bounded pattern extraction**.
They are not merge units and not vendor instructions.

## OCR and receipt extraction donors

- PaddleOCR
  - repo: https://github.com/PaddlePaddle/PaddleOCR
  - bounded pattern: staged OCR / document parsing spine
- docTR
  - repo: https://github.com/mindee/doctr
  - bounded pattern: text detection + recognition seam
- invoice2data
  - repo: https://github.com/invoice-x/invoice2data
  - bounded pattern: template-backed post-OCR field extraction
- receiptparser
  - repo: https://github.com/knipknap/receiptparser
  - bounded pattern: receipt-specific field heuristics and OCR fallback handling
- receipt-parser-legacy
  - repo: https://github.com/ReceiptManager/receipt-parser-legacy
  - bounded pattern: receipt parsing with explicit amount / date / merchant extraction pressure

## Media dedupe and bucketing donors

- CLIP
  - repo: https://github.com/openai/CLIP
  - bounded pattern: image-text semantic bucketing
- imagededup
  - repo: https://github.com/idealo/imagededup
  - bounded pattern: duplicate detection with reviewable similarity thresholds
- imgdupes
  - repo: https://github.com/knjcode/imgdupes
  - bounded pattern: perceptual-hash near-duplicate grouping

## Telegram normalization donors

- Telethon
  - repo: https://github.com/LonamiWebs/Telethon
  - bounded pattern: Python MTProto client and message/media retrieval
- TDLib
  - repo: https://github.com/tdlib/td
  - bounded pattern: client-grade Telegram object model and sync posture
- opentele
  - repo: https://github.com/thedemons/opentele
  - bounded pattern: tdata/session conversion seam
- Chatistics
  - repo: https://github.com/MasterScrat/Chatistics
  - bounded pattern: chat logs into DataFrame-shaped normalized analysis surfaces
- tg-archive
  - repo: https://github.com/knadh/tg-archive
  - bounded pattern: resumable sync into local SQLite plus media-aware archive build
- telegram-mcp
  - repo: https://github.com/chaindead/telegram-mcp
  - bounded pattern: explicit assistant-facing Telegram control surface

## Explicit anti-donor for new work

- Pyrogram
  - repo: https://github.com/pyrogram/pyrogram
  - keep out as a new primary donor because the project is archived and no longer maintained
