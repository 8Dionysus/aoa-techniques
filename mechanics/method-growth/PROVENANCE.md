# Method-Growth Provenance Bridge

This is the active-first bridge from current Method-growth parts back to the
pre-split v0.7 downstream adoption surfaces. Use it when auditing how source
pressure feeds an active part, not when you need the current operating contract.

## Current Route First

Start with the active surfaces:

- [README](README.md)
- [DIRECTION](DIRECTION.md)
- [PARTS](PARTS.md)
- [parts](parts/)
- [LANDING_LOG](LANDING_LOG.md)

If those surfaces answer the task, stop there. Do not pull old flat paths into
the active route just because they existed before this split.

## Source Map

| Evidence source | Active route | Distilled signal |
|---|---|---|
| Pre-split flat `TECHNIQUE_PATTERN_ADOPTION.md` | [parts/pattern-adoption](parts/pattern-adoption/README.md) | Shared patterns can become reusable technique practice only through explicit adoption, owner consent, evidence, rollback, and retention. |
| Pre-split flat `TECHNIQUE_ADOPTION_BOUNDARIES.md` | [parts/adoption-boundaries](parts/adoption-boundaries/README.md) | Adoption needs local owner consent and no-policy-overreach stop-lines before durable behavior changes. |
| Pre-split flat `TECHNIQUE_TO_SKILL_HANDOFF.md` | [parts/technique-to-skill-handoff](parts/technique-to-skill-handoff/README.md) | Technique adoption may request a skill proposal, but technique canon and skill execution remain separate owners. |
| Pre-split flat `TECHNIQUE_RETENTION_CHECKS.md` | [parts/retention-checks](parts/retention-checks/README.md) | Adopted practice needs evidence, rollback, and retention checks to remain active. |
| Pre-split flat `TECHNIQUE_OBSOLESCENCE.md` | [parts/obsolescence](parts/obsolescence/README.md) | Obsolescence and supersession must be explicit instead of silently deleting owner evidence. |

## Legacy Posture

This split did not create `legacy/raw/` because the pre-split files were current
compact active surfaces rather than large wave receipts. Their content moved
into part-local active homes.

Future compaction or raw-wave preservation can add `legacy/` only when there is
real source accounting to preserve.

## Method-Growth Rule

When source evidence changes current behavior, update the relevant active part
first, then update this bridge and `LANDING_LOG.md`. Active part docs must not
become hidden technique bundles.
