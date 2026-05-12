# Second Context Adaptation

## Technique
- id: AOA-T-0029
- name: nested-rule-loading

## Target project
- name: Claude Code memory and rules
- environment: public Claude Code documentation for project, user, local, managed, nested, and path-scoped instruction surfaces
- runtime: `CLAUDE.md`, `CLAUDE.local.md`, and `.claude/rules/` files loaded through directory hierarchy, import, and path-scope rules

## What changed

- paths: Claude Code loads `CLAUDE.md` and `CLAUDE.local.md` files while walking up from the working directory, discovers subtree files on demand, and also supports `.claude/rules/` markdown files with optional path scoping
- services: no donor CLI, MCP propagation, skill propagation, installer behavior, or multi-target distribution is required for this proof
- dependencies: the adaptation depends on declared scope, loading order, closer-file priority, and repeatable path-triggered rule inclusion
- operating assumptions: parent instructions carry shared project context while nested files and path-scoped rules stay subordinate, scoped, and reviewable

## What stayed invariant

- contract: one canonical source owns the shared meaning
- validation logic: nested layers remain subordinate to the canonical source through explicit precedence
- safety rules: local nested layers do not silently become new canonical homes

## Risks introduced by adaptation

- Claude Code concatenates loaded files rather than enforcing a strict override engine, so the proof must stay on declared order and priority rather than hidden conflict resolution
- project rules can become a fragment library if topic splits dominate the hierarchy question
- path-scoped rules load lazily, so reviewers need to check the source hierarchy and the loaded context rather than only the session start view

## Evidence

- Claude Code memory documentation checked on 2026-05-12 states that `CLAUDE.md` files have scoped locations, more specific locations take precedence over broader ones, hierarchy files above the working directory load at launch, and subdirectory files load on demand
- the same documentation describes filesystem-root-to-working-directory ordering, closer files being read later, and user-level rules loading before project rules so project rules have higher priority
- `.claude/rules/` adds a recursive markdown rule layer with topic files, unconditional rules, and path-scoped rules that load only for matching files

## Result

- exact-fit second context confirmed
- the bundle can move from documentation-first promoted posture to canonical default, as long as it stays about hierarchical loading and explicit precedence rather than hidden prompt control, multi-target propagation, generic fragment management, or product-width Claude Code memory doctrine
