# Narrowing Memo - markdown-definition-of-done-defaults

This memo records the current narrowing result for the remaining Wave 2 candidate `markdown-definition-of-done-defaults`.

It is a staging note only.
It does not create a canonical bundle or authorize import by itself.

## Candidate chosen

- `markdown-definition-of-done-defaults`
- donor: `MrLesk/Backlog.md`

## Overlap watch

- [AOA-T-0055](../../../techniques/agent-workflows/requirements-design-tasks-ladder/TECHNIQUE.md)
- [AOA-T-0001](../../../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md)

## Boundary statement

The current donor evidence does not yet expose one standalone markdown-native technique contract.

What is public today is a mixed feature cluster:

- a project config field `definition_of_done`
- wizard support for editing defaults
- task creation behavior that seeds defaults into new tasks
- task-finalization guidance that requires DoD items to be checked before `Done`
- MCP and UI tools for reading and mutating those defaults

That is useful product behavior, but it is not yet one sharply bounded technique in the `aoa-techniques` sense.

The narrowest plausible extraction target is:

- project-level default completion checklist items that preseed new task artifacts while staying distinct from planning ladders, finalization workflow, and general task-manager product behavior

Even that smaller target is not stable enough yet, because the donor still presents it mostly as config UX plus task-manager integration rather than as one reusable markdown contract.

## What stays out

- full task-finalization workflow and `Done` status transitions
- acceptance-criteria doctrine and broader completion governance
- config wizard UX, settings pages, MCP tool taxonomy, and CLI command ergonomics
- task-manager product behavior outside one smaller markdown-default contract
- methodology claims that make the candidate sound like a general project-management doctrine

## Evidence snapshot

- `README.md` frames the feature as `Definition of Done defaults`, meaning a reusable checklist added to every new task
- `ADVANCED-CONFIG.md` describes `definition_of_done` as a project config option edited through the advanced wizard
- `CLI-INSTRUCTIONS.md` reiterates the same wizard/config posture rather than a standalone technique contract
- `backlog/tasks/back-354 - Project-Definition-of-Done-defaults.md` defines the feature as project-level defaults inherited by tasks with per-task override support
- `src/guidelines/mcp/task-finalization.md` folds DoD checking into a wider task-finalization workflow
- `src/mcp/tools/definition-of-done/index.ts` exposes config-management tools, which reinforces that the current public seam is product/config behavior

## Verdict

- keep `markdown-definition-of-done-defaults` in the `narrowing-only` lane
- do not create a seed bundle yet
- do not assign a technique ID yet

## Honest reopen trigger

Reopen this candidate only if the draft can say, in plain language:

- what the default checklist object is
- how it gets attached to new markdown task artifacts
- how it stays distinct from acceptance criteria and from finalization workflow
- why the reusable center is the default-checklist contract itself rather than config UX or broader task-manager product behavior

## Files touched or proposed

- touched: this memo
- touched: Wave 2 staging docs and registry to link the memo and keep the narrowing lane honest
- not proposed yet: no `TECHNIQUE.md`, no bundle-local example, no checklist seed, no note package

## Whether operator approval is needed

- no operator approval needed to keep this candidate in narrowing-only state
- operator approval is required before any future move from this memo into a real seed bundle
