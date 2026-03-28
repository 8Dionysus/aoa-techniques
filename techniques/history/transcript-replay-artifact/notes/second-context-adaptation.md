# Second Context Adaptation

## Technique
- id: AOA-T-0066
- name: transcript-replay-artifact

## Target project
- name: aoa-techniques
- environment: public technique repository with authored bundle contracts, generated routing surfaces, and validator-backed markdown discipline
- runtime: documentation-first corpus that records one bounded replay artifact contract rather than shipping the donors' replay viewers or session apps

## What changed

- paths: the donors ship concrete replay viewers and session apps; this adaptation keeps the generic saved-session-to-replay contract without requiring one viewer implementation
- services: publish flows, hosted sharing, dashboards, editor surfaces, and live monitoring were removed from the reusable contract
- dependencies: the adaptation depends on already-saved session artifacts plus one replay transformation path, not on the donor web products
- operating assumptions: contributors should read the technique as post-capture replay for review, demos, or audit rather than as a hosted viewer or collaboration product

## What stayed invariant

- contract: replay begins after capture and stays derivative from saved source artifacts
- validation logic: bounded flow cues survive into one replayable artifact
- safety rules: replay remains separate from transcript packaging, witness tracing, hosted product semantics, and memory doctrine

## Risks introduced by adaptation

- the pattern can collapse into [AOA-T-0044](../versionable-session-transcripts/TECHNIQUE.md) if repositories stop distinguishing replay from readable transcript packaging
- the public bundle could drift into [AOA-T-0045](../witness-trace-as-reviewable-artifact/TECHNIQUE.md) if teams expect state-delta and review-flag semantics from a replay artifact
- teams may over-associate replay with hosted viewer product features because the donors bundle replay with richer UX surfaces

## Evidence

- the `claude-replay` README says the tool converts Claude Code, Cursor, and Codex session transcripts into self-contained HTML replays
- the same README positions replay as useful for demos, docs, bug reports, teaching, and monitoring, which shows the reusable center is a replay artifact rather than first-save capture
- the `agentsview` README provides a second public context where saved AI sessions are revisited and exported through richer viewing surfaces, which helps confirm that replay sits after capture and alongside, not inside, session storage
- both donors show why hosted viewer product breadth should stay outside the invariant core

## Result

- works as a documentation-first second context and preserves one bounded replay-artifact contract without carrying over the donors' web products or hosted viewer semantics
