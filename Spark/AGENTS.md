# Spark lane for aoa-techniques

This file only governs work started from `Spark/`.

The root `AGENTS.md` remains authoritative for repository identity, ownership boundaries, reading order, and validation commands. This local file only narrows how GPT-5.3-Codex-Spark should behave when used as the fast-loop lane.

If `SWARM.md` exists in this directory, treat it as queue / swarm context. This `AGENTS.md` is the operating policy for Spark work.

## Default Spark posture

- Use Spark for short-loop work where a small diff is enough.
- Start with a map: task, files, risks, and validation path.
- Prefer one bounded patch per loop.
- Read the nearest source docs before editing.
- Use the narrowest relevant validation already documented by the repo.
- Report exactly what was and was not checked.
- Escalate instead of widening into a broad architectural rewrite.

## Spark is strongest here for

- technique wording cleanup
- template refinement
- index, catalog, or capsule alignment
- metadata drift repair between source markdown and generated surfaces
- tight audits of boundedness, portability, and public hygiene

## Do not widen Spark here into

- project-specific operations that do not belong in the canon
- rewriting skill, eval, routing, or role meaning here
- broad donor-intake or portfolio redesign
- turning technique surfaces into philosophy instead of operational practice

## Local done signal

A Spark task is done here when:

- the technique is more reusable, sanitized, and reviewable
- boundedness is clearer
- generated surfaces are aligned when touched
- neighboring layer ownership is clearer, not blurrier
- the repository’s documented validation flow was used when relevant

## Local note

Spark should act like a sharp editor of reusable practice, not like a smuggler of project folklore.

## Reporting contract

Always report:

- the restated task and touched scope
- which files or surfaces changed
- whether the change was semantic, structural, or clarity-only
- what validation actually ran
- what still needs a slower model or human review
