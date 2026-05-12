# Canonical Readiness

## Technique
- id: AOA-T-0067
- name: transcript-linked-code-lineage

## Verdict
- approve for canonical promotion

## Evidence summary
- external origin: the imported technique has a bounded donor contract and explicit exclusions around dashboards, metrics, retrieval UX, and wider analytics-product breadth
- second context: `aoa-techniques` now records the same code-to-evidence lineage contract as a documentation-first adaptation with one example and one checklist
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- `ai4curation/ai-blame` provides exact-fit public reinforcement beyond the donor family: it parses AI agent execution traces, computes line-by-line blame with line number, line content, model, session id, timestamp, and agent tool metadata, and documents review workflows where a reviewer focuses on a line or block, then opens the related session transcript for context
- `ai-blame` transcript docs keep the source evidence explicit: transcripts are complete session records with messages, metadata, tool/file-operation content blocks, and a source trace file, while transcript listing and viewing remain distinct from the blame output
- `empathic/toolpath` supports the broader provenance-document shape by deriving Toolpath documents from Claude conversation logs and mapping write/edit tool use into change entries keyed by file path, but it remains supporting evidence rather than primary proof because its center of gravity is a provenance document format rather than a direct review/blame seam
- validation strength: the bundle now carries one checklist, one example, a clean external-origin note, a documentation-first second context, and public cross-context reinforcement for code anchors reopening saved session evidence

## Default-use rationale
- this is the right canonical default when the main problem is reopening saved session provenance from code review without widening into analytics or retrieval-product doctrine
- it remains narrower than [AOA-T-0045](../../witness-trace-as-reviewable-artifact/TECHNIQUE.md) because it owns one provenance link from code back to existing evidence rather than a fuller run artifact
- it also remains narrower than [AOA-T-0059](../../../../continuity/handoff-continuation/git-verified-handoff-claims/TECHNIQUE.md) because it does not verify current handoff claims; it preserves historical lineage from code to saved evidence
- it is now strong enough as a canonical default because `ai-blame` repeats the same code-line-to-session-evidence shape in a separate public implementation while letting this bundle reject model scorecards, policy gates, dashboard analytics, hosted search, transcript indexing, and free-form Q and A product behavior

## Fresh public-safety check
- review date: 2026-05-12
- result: pass
- sanitization still holds: the bundle keeps only the reusable lineage seam and excludes donor-specific notes backends, dashboards, and analytics or retrieval product behavior
- public reuse check: the example, checklist, and adaptation notes remain understandable without hidden donor-repo context; the inspected `ai4curation/ai-blame` source is BSD-3-Clause licensed and no source code, private trace data, local directories, session identifiers, account details, hosted URLs, or product-specific setup instructions were copied into the technique

## Remaining gaps
- no blocker remains for canonical status
- future lineage sources can reinforce the default, but they must preserve the narrow boundary: already-saved execution traces or session artifacts, one code/file/line/diff anchor, a stable reference back to the saved evidence, and an inspection path that lets another reviewer reopen the source evidence without importing scorecards, dashboards, hosted search, policy enforcement, telemetry, memory doctrine, or broad retrieval UX

## Recommendation
- move `AOA-T-0067` to `canonical`
- add an adverse-effects review to preserve the boundary between code-to-session lineage, fuller witness traces, handoff claim verification, generic repo analytics, scorecards, policy gates, hosted search, and memory or retrieval products
