# Adverse Effects Review

## Technique
- id: AOA-T-0067
- name: transcript-linked-code-lineage

## Review focus
- promotion from `promoted` to `canonical` after exact-fit public reinforcement from `ai4curation/ai-blame`, with `empathic/toolpath` used only as supporting provenance-document shape evidence
- failure cases where code-to-session lineage is mistaken for full witness tracing, current handoff-claim verification, generic repo analytics, scorecards, policy enforcement, hosted search, or memory doctrine

## Failure modes
- code anchors break because line ranges, file paths, or diff hunks move without a stable evidence reference
- reviewers treat lineage metadata as the evidence itself instead of reopening the saved transcript or trace artifact
- attribution output becomes a model scorecard or contributor ranking surface
- transcript lookup drifts into broad session search, Q and A, or memory recall instead of one bounded provenance reopening path
- policy gates, CI enforcement, dashboards, or hosted analytics become more central than the code-to-evidence link

## Negative effects
- maintaining lineage links can add review overhead, especially when refactors churn line anchors
- model and session attribution can be overtrusted when the source trace is partial, noisy, redacted, or tool-specific
- provenance displays can create false confidence if they hide missing traces or unresolved anchors
- teams may overfocus on who or which model touched a line instead of reviewing the code and source evidence

## Misuse patterns
- using lineage as a substitute for [AOA-T-0045](../../witness-trace-as-reviewable-artifact/TECHNIQUE.md) when a fuller run trace is needed
- using lineage as a substitute for [AOA-T-0059](../../../../continuity/handoff-continuation/git-verified-handoff-claims/TECHNIQUE.md) when current handoff claims need git verification
- importing AI percentage metrics, policy thresholds, dashboards, model allow lists, or contributor scorecards as technique requirements
- publishing trace-derived lineage before public-safe redaction and source-scope review
- treating transcript search, chat with history, or memory recall as part of the invariant core

## Detection signals
- the lineage surface names a code anchor but cannot reopen the saved evidence artifact
- the explanation starts with analytics, compliance, policy, or scorecard behavior instead of provenance reopening
- reviewers ask the lineage pointer to prove correctness, authorship policy, or current repo state
- examples include private trace paths, raw session identifiers, account names, local directories, hosted share links, or unsanitized transcript content
- the source can only produce aggregate AI-contribution metrics and cannot map code anchors back to saved session evidence

## Mitigations
- keep saved session or trace artifacts authoritative; lineage pointers are navigational aids
- record anchor instability, missing traces, redaction, and unresolved evidence as limitations rather than silently filling gaps
- prefer repo-relative or abstract anchors in public examples and avoid raw local trace paths or live session identifiers
- route witness tracing, handoff verification, policy gates, telemetry, dashboards, hosted search, and memory recall to sibling surfaces
- reject evidence that cannot survive without scorecards, hosted services, product dashboards, or broad retrieval UX

## Recommendation
- safe to promote as a canonical history technique when code anchors can reopen already-saved session evidence through a bounded inspection path and the saved evidence remains the source of truth
- use this note as the watch surface for anchor brittleness, attribution overclaim, analytics creep, policy creep, hosted-search creep, and lineage replacing the underlying evidence artifact
