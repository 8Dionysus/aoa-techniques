# Second Context Adaptation

## Technique
- id: AOA-T-0053
- name: local-first-session-index

## Target project
- name: coding-agent-search (`cass`)
- environment: open-source local TUI and CLI for indexing and searching saved coding-agent session history across multiple local providers
- runtime: derivative local search and index surfaces over already-saved session artifacts, with provenance-aware results and one searchable timeline rather than a hosted dashboard or memory product

## What changed
- paths: the donor uses local session discovery plus a SQLite-backed search layer and UI, while the second context aggregates saved session artifacts from several local coding-agent families into one searchable timeline
- services: the second context also offers semantic search, export, and optional remote-source features, but this adaptation narrows to the local derivative index and source-reference contract only
- dependencies: the adaptation depends on an existing saved history layer and one local search index surface, not on a specific web UI or deployment stack
- operating assumptions: contributors should read the technique as post-capture lookup over saved artifacts, not as dashboard installation, multi-machine sync, or product deployment guidance

## What stayed invariant
- contract: indexing begins from already-saved local session artifacts
- validation logic: searchable lookup remains derivative and points back to original artifacts through stable references
- safety rules: source artifacts stay authoritative, and the technique remains outside capture, transcript export, and memory recall semantics

## Risks introduced by adaptation
- the pattern can collapse back into [AOA-T-0026](../../session-capture-as-repo-artifact/TECHNIQUE.md) if repositories cannot explain what indexing adds after capture already exists
- teams may over-associate indexing with export, semantic recall, or cross-machine aggregation because the second context bundles those adjacent surfaces together
- the public bundle could drift into dashboard or memory language if the source-reference boundary is not kept explicit

## Evidence
- the public `cass` README describes the tool as a unified local TUI that indexes and searches coding-agent history from several saved-session providers into one searchable timeline
- the same README says tool calls become searchable text, exports can stay local, and the system tracks provenance so operators can see where each conversation originated
- those public surfaces preserve the same reusable core: the index stays local and derivative, the searchable layer sits over already-saved session artifacts, and useful results still point back to the original history source rather than replacing it

## Result
- works as a real public second context and preserves one bounded local-index contract without carrying over dashboard, export, sync, or hosted product breadth
