# AGENTS.md

## Applies to

This card applies to `.agents/spark/` and all descendants unless a nearer
`AGENTS.md` narrows the path.

## Role

`.agents/spark/` is the fast-loop Spark lane for `aoa-techniques`.

The root `AGENTS.md` remains authoritative for repository identity, ownership
boundaries, reading order, and validation commands. This local file only
narrows how GPT-5.3-Codex-Spark should behave when used as the fast-loop lane.

If `SWARM.md` exists in this directory, treat it as queue or swarm context.
This `AGENTS.md` is the operating policy for Spark work.

## Read before editing

Read root `AGENTS.md`, `.agents/AGENTS.md`, `DESIGN.AGENTS.md`, and the nearest
source route for the touched file before changing this lane or using it as
work context.

## Boundaries

- Use Spark for short-loop work where a small diff is enough.
- Start with a map: task, files, risks, and validation path.
- Prefer one bounded patch per loop.
- Read the nearest source docs before editing.
- Use the narrowest relevant validation already documented by the repo.
- Report exactly what was and was not checked.
- Escalate instead of widening into a broad architectural rewrite.
- Do not use Spark for project-specific operations that do not belong in the
  canon.
- Do not rewrite skill, eval, routing, or role meaning here.
- Do not turn technique surfaces into philosophy instead of operational
  practice.

Spark is strongest here for technique wording cleanup, template refinement,
index or capsule alignment, metadata drift repair, and tight audits of
boundedness, portability, and public hygiene.

## Validation

A Spark task is done here when the technique is more reusable, sanitized, and
reviewable; boundedness is clearer; generated surfaces are aligned when
touched; neighboring layer ownership is clearer; and the repository validation
flow was used when relevant.

For agent-lane changes, include:

```bash
python scripts/validate_agents_md_shape.py
python scripts/validate_agents_mesh.py
```

Spark should act like a sharp editor of reusable practice, not like a smuggler
of project folklore.

## Closeout

Always report the restated task and touched scope, which files or surfaces
changed, whether the change was semantic, structural, or clarity-only, what
validation actually ran, and what still needs a slower model or human review.
