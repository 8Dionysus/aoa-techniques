# Second Context Adaptation

## Technique
- id: AOA-T-0053
- name: local-first-session-index

## Target project
- name: aoa-techniques
- environment: public technique repository with authored bundle contracts, generated routing surfaces, and validator-backed markdown discipline
- runtime: documentation-first corpus that records bounded local-index meaning rather than shipping the donor desktop app, local server, or search UI

## What changed
- paths: the donor uses local session discovery plus a SQLite-backed search layer and UI; this adaptation keeps the generic existing-artifact plus local-index contract without depending on one product path
- services: analytics dashboards, live updates, publish flows, PostgreSQL sync, reverse-proxy exposure, and hosted access were removed from the reusable contract
- dependencies: the adaptation depends on an existing saved history layer and one local index surface, not on the donor application stack
- operating assumptions: contributors should read the technique as post-capture lookup over saved artifacts, not as installation or product deployment guidance

## What stayed invariant
- contract: indexing begins from already-saved local session artifacts
- validation logic: searchable lookup remains derivative and points back to original artifacts through stable references
- safety rules: source artifacts stay authoritative, and the technique remains outside capture, transcript export, and memory recall semantics

## Risks introduced by adaptation
- the pattern can collapse back into [AOA-T-0026](../../session-capture-as-repo-artifact/TECHNIQUE.md) if repositories cannot explain what indexing adds after capture already exists
- teams may over-associate indexing with transcript export or analytics because the donor product bundles those adjacent surfaces together
- the public bundle could drift into dashboard or memory language if the source-reference boundary is not kept explicit

## Evidence
- the public donor README says AI coding agents generate large volumes of session data and that `agentsview` indexes these sessions into a local SQLite database with full-text search
- the same README says startup discovers sessions from supported agents, syncs them into a local SQLite database with FTS5 full-text search, and then exposes a web UI
- the donor `SearchResult` and `Session` structures keep session IDs, names, timestamps, snippets, and stored file paths, which shows the lookup surface stays tied back to saved source artifacts rather than replacing them
- the donor search handler keeps the runtime query contract narrow: pass a query, run local search, and return session-level matches with snippet and cursor state

## Result
- works as a documentation-first second context and preserves one bounded local-index contract without carrying over dashboard, export, sync, or hosted product breadth
