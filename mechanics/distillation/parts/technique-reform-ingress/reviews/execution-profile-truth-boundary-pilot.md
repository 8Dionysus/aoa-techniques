# Execution Profile Truth Boundary Pilot

Source packet: [Technique Reform Ingress](../README.md)

Status: scout calibration pilot, no local small-agent eval, no frontmatter
change, no schema migration, no technique leaf repair.

## Verdict

Treat `execution_profile` as a scout suitability estimate until a real local
small-agent harness proves execution.

This pilot reviewed `continuity/handoff-continuation` because the shelf has a
useful mix of `small-agent` and `orchestration-required` projections while
staying inside one semantic family. Direct reading supports the current scout
split, but only as static review truth:

- `small-agent` means "candidate for 2-4B execution after orchestration packs
  facts, frame, stop line, and output shape."
- It does not mean "already proven by a 2-4B local model."
- `orchestration-required` stays valid when the atomic move is safe only inside
  a guard, approval, tool, or episode-control wrapper.

The registry wording is clarified so future readers do not confuse scout
projection with empirical validation.

## Reviewed Surfaces

Reviewed:

- `docs/TECHNIQUE_ATOM_CONTRACT.md`
- `docs/TECHNIQUE_TOPOLOGY_CONTRACT.md`
- `config/technique_topology_axes.yaml`
- `reports/technique_topology_scout.md`
- `docs/TECHNIQUE_CAPSULES.md`
- `techniques/continuity/AGENTS.md`
- all `TECHNIQUE.md`, `examples/`, `checks/`, and `notes/` files under
  `techniques/continuity/handoff-continuation/`

## Shelf Calibration

| technique | current profile | pilot verdict | future local fixture |
|---|---|---|---|
| `AOA-T-0056` `channelized-agent-mailbox` | `small-agent` | keep as scout candidate: bounded replay and ack state are explicit, read-only, and capsule-shaped | named channel, two ordered messages, `last_seen`, expected replay plus `acked_through` |
| `AOA-T-0057` `structured-handoff-before-compaction` | `small-agent` | keep as scout candidate: one pre-boundary handoff artifact with clear fields | compaction boundary state with done/blocked/next refs, expected structured packet |
| `AOA-T-0058` `receipt-confirmed-handoff-packet` | `small-agent` | keep as scout candidate: existing packet plus visible receipt state keeps the move narrow | handoff packet and receiver, expected receipt record before continuation |
| `AOA-T-0059` `git-verified-handoff-claims` | `small-agent` | keep as scout candidate, but fixture must provide controlled git evidence | handoff claims plus local git fixture, expected verified/mismatch/unverifiable rows |
| `AOA-T-0060` `session-opening-ritual-before-work` | `orchestration-required` | keep: the move is pre-mutation and depends on an outer guard around first work | handed-off session start with current-state surfaces, expected baseline note and no mutation before check |
| `AOA-T-0061` `cross-repo-resource-map-bootstrap` | `small-agent` | keep as scout candidate when the repo list and task frame are supplied | bounded cross-repo task with three repos, expected role and first-look map |
| `AOA-T-0062` `episode-bounded-agent-loop` | `orchestration-required` | keep: episode boundaries and continue/stop/escalate need outer control to avoid open-ended autonomy | fixed episode goal, checkpoint criterion, and stop rule, expected checkpoint plus decision |

No profile changes are opened by this pilot. The point is to define the truth
boundary before scaling the pass.

## Future Long-Pass Rhythm

Use this rhythm for the long execution-profile pass:

1. Choose one bounded cohort from `reports/technique_topology_scout.md`.
2. Read every target `TECHNIQUE.md` directly.
3. Read examples, checks, notes, and capsule text for each target.
4. Record whether the current profile is `scout-confirmed`,
   `scout-needs-review`, or `empirical-fixture-needed`.
5. Write a tiny future fixture sketch for each `small-agent` candidate.
6. Do not call any profile empirically validated without running a real local
   small-agent harness.
7. Change registry wording or generated projection rules only when the pilot
   finds repeated confusion.
8. Rebuild generated scout surfaces only from source inputs.
9. Run `python scripts/release_check.py` and `python scripts/validate_repo.py`
   for any registry, generated, or broad reader-surface change.

Recommended order for the long pass:

1. all `small-agent` scout candidates;
2. all `medium-agent` scout candidates;
3. sampled `orchestration-required` rows;
4. only then a real local small-agent harness with model, fixture, and verdict
   surfaces.

## Stop Lines

- Do not run fake small-agent validation through the reviewing model.
- Do not promote `execution_profile` into required frontmatter.
- Do not change technique status from execution-profile review.
- Do not mass-relabel profiles from generated reports alone.
- Do not mutate technique leaves during this calibration pass.
- Do not let small-agent suitability imply autonomous technique selection.

## Validation

Passed locally:

1. `python scripts/build_topology_scout.py`
2. `python -m unittest tests.test_distillation_mechanics_topology`
3. `python scripts/validate_repo.py`
4. `python scripts/release_check.py`

`build_topology_scout.py` rewrote the generated scout files without producing
a tracked generated diff.
