# Second Context Adaptation

## Technique
- id: AOA-T-0061
- name: cross-repo-resource-map-bootstrap

## Target project
- name: aoa-techniques
- environment: public technique repository with authored bundle contracts, generated routing surfaces, and validator-backed markdown discipline
- runtime: documentation-first corpus that records one bounded cross-repo startup seam rather than shipping the donor's whole workspace platform or bootstrap stack

## What changed

- paths: the donor uses `RESOURCE-MAP.yml` under orchestrator directories; this adaptation keeps the cross-repo map contract without requiring one specific workspace layout
- services: project boards, collaboration-mode branching, worktree conventions, and broader boot-sequence services were removed from the reusable contract
- dependencies: the adaptation depends on one explicit list of repos plus task-relevant surfaces, not on a global infrastructure catalog or a platform-specific workspace manager
- operating assumptions: contributors should read the technique as one bounded cross-repo startup map before broader context modeling, handoff protocol, or workspace orchestration layers

## What stayed invariant

- contract: cross-repo continuation begins from one explicit map of the repos and surfaces that matter to the current step
- validation logic: repo roles and resource roles stay visible enough that the next session can tell where to look first
- safety rules: the technique remains outside semantic context mapping, infrastructure encyclopedias, collaboration-mode doctrine, and full startup governance

## Risks introduced by adaptation

- the pattern can collapse into [AOA-T-0016](../../docs/bounded-context-map/TECHNIQUE.md) if repositories stop separating conceptual context boundaries from a task-bounded startup map
- teams may over-associate the pattern with a whole multi-repo platform because the donor also bundles boot sequences, project boards, worktrees, and collaboration modes
- the public bundle could drift into [AOA-T-0060](../../agent-workflows/session-opening-ritual-before-work/TECHNIQUE.md) if generic session-start ritual semantics become the real center of gravity

## Evidence

- the Code Relay README presents `RESOURCE-MAP.yml` as the global index of all repos and infrastructure and says the workspace gives the agent a global view across multiple independent repos
- the README explains that on startup the agent restores context from that map rather than treating each repo in isolation
- the shipped `RESOURCE-MAP.yml` templates enumerate repos plus supporting infrastructure surfaces as the bootstrap index the agent fills in for a real workspace

## Result

- works as a documentation-first second context and preserves one bounded cross-repo startup-map contract without carrying over the donor's workspace platform, collaboration-mode splits, or full infrastructure inventory doctrine
