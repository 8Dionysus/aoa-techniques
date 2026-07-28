# Checkpoint Roadmap

This roadmap records future contour for the `aoa-techniques` checkpoint
package. It does not change technique status, generated contracts, checkpoint
law, runtime behavior, or validator behavior by itself.

## Current Contour

Checkpoint is the local route for phase handoff, handoff packet, compaction,
re-entry, and checkpoint-shaped repair pressure that may become one portable
technique.

- `phase-handoff-candidate` is the local home for the active
  `phase_sync_for_agents` to `phase-synchronized-agent-handoff` narrowing lane.
- `technique-anchors` maps current checkpoint-adjacent technique bundles without
  changing their canonical or promoted status.
- Checkpoint pressure is currently non-ORQ candidate-only pressure in this repo,
  not a direct AoA owner-request landing.

## Next Work

1. Reopen the phase handoff candidate only when public evidence exposes a
   standalone phase boundary, handoff packet, continuation permission, and
   stop/return/escalation rule.
2. Keep checkpoint-related references pointed at technique bundle homes when the
   bundle already exists.
3. Add a new part only if repeated technique-layer checkpoint signals no longer
   fit phase handoff candidate pressure or existing technique anchors.
4. Promote a reusable checkpoint practice into `techniques/` only after it can
   name one atomic move, likely domain, likely kind, family posture,
   capability, substrate, execution profile, risk posture, relations, and
   validation.

## When Time Comes

- Add examples only when they show a public-safe handoff artifact without
  implying hidden runtime state.
- Route memory canon to `aoa-memo`, proof to `aoa-evals`, route behavior to
  `aoa-sdk`, runtime activation to the runtime owner, and stats meaning to
  `aoa-stats`.
- Reassess this roadmap after a checkpoint-shaped candidate proves smaller than
  existing continuity or owner-truth-closeout techniques.

## Out Of Scope

- checkpoint implementation authority.
- checkpoint notes, handoff packets, receipts, or session artifacts as memory
  canon, route authority, proof verdicts, runtime activation, stats truth, or
  owner acceptance.
- hidden scheduler behavior or autonomous self-repair.
- automatic technique promotion from checkpoint-shaped pressure.
