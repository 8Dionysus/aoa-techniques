# Adverse Effects Review

## Technique

- id: AOA-T-0061
- name: cross-repo-resource-map-bootstrap

## Review focus

- current role: canonical default for starting a cross-repo task from one bounded map of relevant repos, resource surfaces, and first-look paths
- current watch seam: preserve the startup map without turning it into semantic context mapping, infrastructure inventory, dispatch policy, worktree lifecycle management, or workspace-platform governance

## Failure modes

- the map names repos but does not say why each repo matters to the current task
- the map lists broad projects while omitting the concrete files, docs, worktrees, or surfaces the next session should inspect first
- the first-look path is missing, so a fresh session still has to infer startup order across repos
- repo roles drift out of date because the map is treated as a permanent inventory instead of a task-bounded handoff object

## Negative effects

- a small cross-repo task can gain too much ceremony when one repo-local handoff would be enough
- contributors can mistake the startup map for an architecture model and stop maintaining the real architecture docs
- infra, auth, issue-routing, and worktree details can crowd out the one bounded question: where should the next session look first across repo boundaries
- agents can overtrust the map and skip current-state checks in the selected repos

## Misuse patterns

- listing every known repo, service, database, queue, board, and environment because they exist
- using the map as a durable workspace encyclopedia rather than a current task startup aid
- hiding repo roles behind names like `api`, `frontend`, or `core` without a task-specific reason
- importing dispatch rules, model routing, worktree creation, or audit policy into the technique
- replacing semantic bounded-context maps with a path list

## Detection signals

- the map cannot be reviewed quickly before the next session starts
- a reader cannot identify the first repo or first surface to inspect
- listed resources are not tied to the current handoff, issue, or continuation goal
- the artifact grows whenever the workspace grows, even if the current task does not need those repos
- follow-up work fails because one named repo was present but the relevant file, doc, branch, or worktree surface was not named

## Mitigations

- require one task-tied reason for every repo and every listed resource surface
- mark one first-look repo or surface before listing optional supporting surfaces
- prune any infrastructure or platform detail that does not affect the next bounded step
- keep semantic context maps in AOA-T-0016 and session-opening ritual in AOA-T-0060 instead of merging them here
- pair the map with current-state checks when the next session crosses into mutation

## Recommendation

- move `AOA-T-0061` to `canonical` and use this note as the watch surface for inventory creep, missing first-look paths, stale repo-role assumptions, and accidental absorption of multi-repo dispatch or workspace-platform machinery
