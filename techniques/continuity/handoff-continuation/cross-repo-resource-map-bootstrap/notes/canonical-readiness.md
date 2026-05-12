# Canonical Readiness

## Technique
- id: AOA-T-0061
- name: cross-repo-resource-map-bootstrap

## Verdict
- approve for canonical promotion

## Evidence summary

- external origin: the imported technique has a bounded donor contract and explicit exclusions around workspace-platform stacks, infrastructure inventories, collaboration-mode doctrine, and whole boot sequences
- second context: `aoa-techniques` now records the same cross-repo startup seam as a documentation-first adaptation with one example and one checklist
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- `calltelemetry/openclaw-linear-plugin` provides exact-fit public reinforcement beyond the donor family: its multi-repo dispatch path keeps a `repos` map, resolves the selected repo set from issue body markers, labels, team mappings, or config fallback, creates named worktrees for each selected repo, injects the repo path map into worker and audit prompts, and tells agents to read `CLAUDE.md` and `AGENTS.md` in the worktree root before coding or auditing
- validation strength: the bundle now carries one checklist, one example, a clean external-origin note, a documentation-first second context, and public cross-context reinforcement for a bounded repo-and-resource startup map

## Default-use rationale

- this is the right canonical default when the main problem is how to start a cross-repo task from one explicit map of repos and relevant surfaces
- it remains narrower than [AOA-T-0016](../../../../proof/skill-support/bounded-context-map/TECHNIQUE.md) and [AOA-T-0060](../../session-opening-ritual-before-work/TECHNIQUE.md) because it owns only the task-bounded cross-repo map object
- it also remains smaller than total workspace-platform doctrine because it does not define infrastructure catalogs, project-board semantics, or a whole boot-sequence stack
- it is now strong enough as a canonical default because the external reinforcement repeats the same "name relevant repos, map them to concrete starting surfaces, then begin work from those mapped surfaces" shape without making the bundle absorb dispatch governance, issue routing, model selection, worktree lifecycle, or audit loops

## Fresh public-safety check

- review date: 2026-05-12
- result: pass
- sanitization still holds: the bundle keeps only the reusable repo-and-resource startup seam and excludes donor workspace stacks, infra inventories, and collaboration-mode doctrine
- public reuse check: the example, checklist, and adaptation notes remain understandable without hidden donor-repo context; the inspected `openclaw-linear-plugin` source includes an MIT license file, and no source code, private paths, credentials, Linear workspace details, or plugin-specific operational data were copied into the technique

## Remaining gaps

- no blocker remains for canonical status
- future work can add another cross-repo startup implementation, but it must preserve the narrow boundary: name the repos, give each repo a task-tied role or path surface, show the first place to look, and route architecture inventories, topology stacks, dispatch policy, and full workspace-platform doctrine elsewhere

## Recommendation

- move `AOA-T-0061` to `canonical`
- add an adverse-effects review to preserve the boundary between the startup map, semantic context mapping, infrastructure inventory, multi-repo dispatch, worktree management, and full workspace-platform governance
