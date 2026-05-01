# Method-Growth Direction

## Current Intent

Method-growth in `aoa-techniques` is the reusable-practice movement mechanic. It
receives repeated practice pressure, adoption pressure, and technique-to-skill
handoff pressure, then decides whether the material should become:

- an adoption boundary
- a reusable pattern adoption route
- a retention or obsolescence check
- a technique-to-skill handoff candidate
- a real `techniques/` bundle through the normal review path

The mechanic keeps owner consent, rollback, evidence, and retention visible
without turning adoption into automatic activation.

## Current Route

1. Use [Pattern Adoption](parts/pattern-adoption/README.md) when a shared pattern
   may become reusable technique practice.
2. Use [Adoption Boundaries](parts/adoption-boundaries/README.md) when a local
   owner must consent before practice changes behavior.
3. Use [Technique To Skill Handoff](parts/technique-to-skill-handoff/README.md)
   when a practice may need an executable skill proposal.
4. Use [Retention Checks](parts/retention-checks/README.md) when an adopted
   practice must prove it should remain active.
5. Use [Obsolescence](parts/obsolescence/README.md) when an adopted practice
   should be removed, superseded, or deprecated.

## Boundaries

Method-growth does not mint technique canon by itself. A promoted or canonical
technique still needs bundle-local evidence and validation expected by
`aoa-techniques`.

Method-growth also does not activate sibling owners. Skills stay in
`aoa-skills`, proof stays in `aoa-evals`, memory stays in `aoa-memo`, recurring
scenario method stays in `aoa-playbooks`, and center doctrine stays in
`Agents-of-Abyss`.

## Current Structural Posture

The first active split moved five formerly flat Method-growth files into
part-local homes. Their v0.7 adoption-wave wording was preserved as active
mechanics behavior, not archived as discarded legacy.

The next work should deepen one part at a time instead of trying to convert the
whole adoption surface into technique bundles in one pass.
