# AGENTS.md

## Applies to

This card applies to `mechanics/checkpoint/` and every descendant unless a nearer
`AGENTS.md` narrows the path.

## Role

This package owns the `aoa-techniques` side of Checkpoint: local practice
pressure around phase handoff, handoff packets, compaction/re-entry,
checkpoint-bound repair, and candidate narrowing that may feed future technique
canon.

It does not own AoA checkpoint law, checkpoint controls, checkpoint-note
protocol, memory writeback, proof verdicts, runtime activation, route
authority, stats truth, owner acceptance, hidden scheduling, autonomous
self-repair, or technique status changes.

## Read before editing

1. Root `AGENTS.md`.
2. `mechanics/AGENTS.md`.
3. `mechanics/REQUEST_RECEIPTS.md` only when naming AoA center-side pressure.
Read `README.md` only when the selected task needs its human map; do not preload unrelated maps.

## Boundaries

- Keep checkpoint here technique-layered: reusable practice pressure, not
  checkpoint implementation authority.
- Do not import `Agents-of-Abyss` checkpoint law as local implementation
  authority.
- Do not treat checkpoint notes, session artifacts, handoff packets, receipts,
  or repair posture as memory canon, proof verdicts, runtime truth, owner
  acceptance, or route authority.
- Keep sibling owner truth with its owner: controls in `aoa-sdk`, protocol in
  `aoa-skills`, actor posture in `aoa-agents`, memory/relaunch in `aoa-memo`,
  proof in `aoa-evals`, routing in `aoa-sdk`, stats in `aoa-stats`, runtime
  exports in `abyss-stack`, and center law in `Agents-of-Abyss`.
- If a stable reusable practice emerges, route it into `techniques/` through
  the normal technique review path.

## Validation

Select the narrowest owner route: `mechanics/part-local` for part-local work; add `source-fast` for authored routes or `generated` for projections. See [VALIDATION.md](../../VALIDATION.md); exact order is `config/validation_lanes.json`; focused procedure stays with the nearest owner. Report checks, skips, and blockers.

## Closeout

Report the mechanic package, part, legacy surface, or helper changed;
whether source, generated, schema, example, or test surfaces moved; checks run;
checks skipped; and the next owner route.
