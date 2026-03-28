# Second Context Adaptation

## Technique
- id: AOA-T-0074
- name: telegram-export-normalization-to-local-store

## Target project
- name: aoa-techniques
- environment: public technique repository with authored bundle contracts, generated routing surfaces, and validator-backed markdown discipline
- runtime: documentation-first corpus that records the bounded Telegram-normalization pattern rather than shipping donor client libraries, session bridges, or archive apps

## What changed

- donor Telegram stacks were reduced to one portable normalization contract rather than one full client, archive, analytics, or MCP workflow
- auth bootstrap, session conversion, and control-plane behavior were removed from the reusable public bundle
- memory writeback and general history-capture ownership were kept out so the adaptation stays source-specific
- the bundle was reduced to one technique doc, one checklist, one example, and four bounded evidence notes

## What stayed invariant

- Telegram-derived messages become stable local objects
- source provenance remains visible
- media references and reply edges survive normalization
- resume behavior remains bounded and explicit

## Risks introduced by adaptation

- the technique can collapse into auth doctrine if later users stop separating session handling from normalization
- teams may over-associate the technique with one donor library if the local object contract is not kept generic
- local stores can be mistaken for memory or final curation if provenance and boundary notes weaken

## Evidence

- Telethon and TDLib expose programmatic message retrieval, sync, and media access over Telegram data
- opentele shows why session conversion and auth bridging are adjacent but separate concerns
- Chatistics, tg-archive, and telegram-mcp show Telegram-derived content being archived, analyzed, or surfaced through local structured storage and local-first tool-facing paths

## Result

- works as a documentation-first second context and preserves the bounded core without carrying over auth procedures, session bridging, memory doctrine, or donor runtime packaging
