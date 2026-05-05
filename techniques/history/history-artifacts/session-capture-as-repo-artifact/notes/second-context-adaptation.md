# Second Context Adaptation

## Technique
- id: AOA-T-0026
- name: session-capture-as-repo-artifact

## Target project
- name: aoa-techniques
- environment: public technique repository with authored bundle contracts, generated routing surfaces, and validator-backed markdown discipline
- runtime: documentation-first corpus that records local-first history technique meaning rather than shipping the donor wrapper CLI

## What changed
- paths: the donor uses `.specstory/history/`; this adaptation preserves that artifact idea generically without depending on the donor product wrapper
- services: cloud sync, search UI, login, and cross-tool product behavior are removed from the reusable contract
- dependencies: the adaptation depends on project-scoped history artifacts and local-first persistence, not on the donor platform stack
- operating assumptions: contributors should read the technique as a history-artifact pattern for AI-assisted repositories, not as installation guidance for the donor product

## What stayed invariant
- contract: sessions are persisted as project-scoped history artifacts
- validation logic: the local artifact layer remains usable even without cloud sync
- safety rules: captured history stays separate from memory recall semantics and authored instruction authority

## Risks introduced by adaptation
- the pattern can become vague if repositories save sessions locally but then quietly treat them as universal instructions
- teams may over-associate session history with memory systems if the history boundary is not kept explicit

## Evidence
- the donor `README.md` describes a local-first workflow where supported AI coding tools save sessions into `.specstory/history/`
- the same public README keeps cloud sync optional and presents local artifact capture as the first durable layer
- the adjacent public `agent-skills` repository reinforces that `.specstory/history` can act as an inspectable artifact base for later summaries or organization, rather than only as hidden product state

## Result
- works as a documentation-first second context and preserves the bounded core without carrying over cloud, search, or memory-system breadth
