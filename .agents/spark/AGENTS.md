# AGENTS.md

## Applies to

This card applies to `.agents/spark/` and all descendants unless a nearer
`AGENTS.md` narrows the path.

## Role

`.agents/spark/` is the real-time, interruptible Spark lane for
`aoa-techniques`.

The root `AGENTS.md` remains authoritative for repository identity, ownership
boundaries, reading order, and validation commands. This local file only
narrows how GPT-5.3-Codex-Spark should behave when used as the fast-loop lane.

If `SWARM.md` exists in this directory, treat it as queue or swarm context.
This `AGENTS.md` is the operating policy for Spark work.

## Read before editing

Read root `AGENTS.md`, `.agents/AGENTS.md`, `DESIGN.AGENTS.md`, and the nearest
source route for the touched file before changing this lane or using it as
work context.

Read `SPARK_EXTRAPOLATION_NOTEBOOK.md` when changing the lane contract,
scenario set, validator, tests, or release-check wiring. It records the studied
`Agents-of-Abyss/.agents/spark` pattern and the local technique-canon
adaptation boundary.
Read `README.md` only when the selected task needs its human map; do not preload unrelated maps.

## Boundaries

- Use Spark for short-loop work where a small diff is enough.
- Start with a map: task, files, risks, and validation path.
- Prefer one bounded patch per loop.
- Choose exactly one registered scenario from `.agents/spark/registry.json`.
- End as `done` or `handoff`; this is the `done-or-handoff` rule. Do not
  depend on an in-session model switch.
- Keep the default loop lightweight: targeted edits, tight audits, or explicit
  handoffs.
- Do not run broad tests automatically. Run validation when the user, scenario,
  or repo law asks for it; otherwise name skipped checks honestly.
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
boundedness, portability, and public hygiene. It is not the right lane for
multi-hour architecture synthesis or canon promotion.

## Validation

Select the narrowest owner route: `source-fast` for authored or route-card work; add `generated` for projections and `release` only for release posture. See [VALIDATION.md](../../VALIDATION.md); exact order is `config/validation_lanes.json`; focused procedure stays with the nearest owner. Report checks, skips, and blockers.

## Closeout

Always report the restated task and touched scope, which files or surfaces
changed, whether the change was semantic, structural, or clarity-only, what
validation actually ran, and what still needs a slower model or human review.
