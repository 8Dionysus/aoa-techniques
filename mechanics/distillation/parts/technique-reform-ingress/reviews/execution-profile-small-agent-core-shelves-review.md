# Execution Profile Small-Agent Wave A Review

Source packet: [Technique Reform Ingress](../README.md)

Temporary plan:
[Temporary Execution Profile Long-Pass Plan](../TEMP_EXECUTION_PROFILE_LONG_PASS_PLAN.md)

Status: direct-read review packet for the first post-pilot small-agent cohort.
No local small-agent harness was run. No frontmatter, schema, generated scout
rule, capsule builder, or technique leaf was changed.

## Verdict

Wave A confirms the current scout profiles for the reviewed shelves as static
execution-envelope estimates.

The `small-agent` rows in this wave remain good fixture candidates when an
orchestrator supplies the bounded source artifact, explicit stop line, and
output schema. They are not empirical proof. The `orchestration-required` rows
also remain useful and should not be treated as failures: they name atomic
moves whose safe use depends on approval, mutation, runtime, or authority
wrappers outside the technique itself.

Reviewed shelves:

- `continuity/donor-harvest`
- `execution/agent-workflows-core`
- `execution/runtime-truth-lifecycle`
- `governance/approval-evidence`
- `governance/promotion-boundary`

Wave totals:

| profile | rows reviewed | verdict |
|---|---:|---|
| `small-agent` | 8 | keep as fixture candidates |
| `medium-agent` | 3 | keep for Phase 2 calibration |
| `orchestration-required` | 7 | boundary confirmed |

## Reviewed Surfaces

Reviewed before this packet:

- `docs/TECHNIQUE_ATOM_CONTRACT.md`
- `docs/TECHNIQUE_TOPOLOGY_CONTRACT.md`
- `docs/TECHNIQUE_TREE_CONTRACT.md`
- `mechanics/distillation/parts/technique-reform-ingress/config/technique_topology_axes.yaml`
- `mechanics/distillation/parts/technique-reform-ingress/reports/technique_topology_scout.json`
- `mechanics/distillation/parts/technique-reform-ingress/reports/technique_topology_scout.md`
- `docs/TECHNIQUE_CAPSULES.md`
- `techniques/continuity/AGENTS.md`
- `techniques/execution/AGENTS.md`
- `techniques/governance/AGENTS.md`
- all `TECHNIQUE.md`, `examples/`, `checks/`, and `notes/` files under the
  five reviewed shelves

## Small-Agent Rows

| technique | current profile | direct-read verdict | orchestrator must supply | future fixture sketch |
|---|---|---|---|---|
| `AOA-T-0075` `session-donor-harvest` | `small-agent` | `scout-confirmed`; `empirical-fixture-needed` | reviewed session artifact, closure state, evidence anchors, donor-pack schema, defer/hold rules | reviewed recap with three candidate signals and one weak theme; expect split donor pack with evidence anchors and hold list |
| `AOA-T-0077` `harvest-packet-contract` | `small-agent` | `scout-confirmed`; `empirical-fixture-needed` | reviewed source artifacts, extracted reusable units, required packet spine, optional family-field stop line | reviewed session ref plus two extracts and tempting optional diagnosis/progression fields; expect compact `HARVEST_PACKET` with optional fields subordinate |
| `AOA-T-0084` `progression-evidence-lift` | `small-agent` | `scout-confirmed`; `empirical-fixture-needed` | reviewed evidence refs, bounded axis set, allowed verdict vocabulary, rule that zero/negative movement is valid | evidence packet with mixed axis movement; expect bounded `PROGRESSION_DELTA`, no universal score, no hidden route authority |
| `AOA-T-0028` `confirmation-gated-mutating-action` | `small-agent` | `scout-confirmed`; `empirical-fixture-needed` | read/plan result, proposed mutation, explicit confirmation state, refusal path | planned file edit with confirmation absent, denied, or granted; expect pause/refusal or one named confirmed mutation, not a workflow loop |
| `AOA-T-0039` `baseline-first-additive-profile-benchmarks` | `small-agent` | `scout-confirmed`; `empirical-fixture-needed` | stable baseline, additive profile list, normalized measurement surface, default-path stop line | baseline result plus two additive profile requests; expect baseline-first artifact shape and additive comparison without promoting additive profile to default |
| `AOA-T-0069` `approval-bound-durable-jobs` | `small-agent` | `scout-confirmed`; `empirical-fixture-needed` | durable job identity, persisted checkpoint/status state, approval seam, resume/stop output shape | long job with checkpoint and pending approval; expect durable job record plus explicit approval checkpoint before continuation |
| `AOA-T-0090` `nearest-wrong-target-rejection` | `small-agent` | `scout-confirmed`; `empirical-fixture-needed` | one chosen target, one adjacent plausible wrong target, boundary reason, defer fallback | chosen playbook target with tempting skill target; expect one adjacent rejection reason and no broad anti-pattern essay |
| `AOA-T-0102` `skill-proposal-handoff-packet` | `small-agent` | `scout-confirmed`; `empirical-fixture-needed` | named practice, receiving skill owner, trigger boundary, inputs/outputs, risks, verification hints, non-acceptance stop line | technique-side adoption pressure with skill-shaped need; expect proposal packet that does not create, accept, install, or activate a skill |

Small-agent pattern found:

- All eight rows have compact input and output shapes in the authored bundle,
  checklist, example, and capsule.
- None should be considered autonomously selectable by a small model.
- The likely harness can be fixture-only and mostly read-only, except where the
  fixture simulates approval or mutation state without performing real side
  effects.

## Medium Rows Deferred To Phase 2

| technique | current profile | wave A note |
|---|---|---|
| `AOA-T-0023` `stateless-single-shot-agent` | `medium-agent` | capsule is compact, but direct reading shows the model must preserve one-shot boundaries against hidden state and tool-use creep; keep for Phase 2 comparison |
| `AOA-T-0031` `shell-composable-agent-invocation` | `medium-agent` | shell visibility is clear, but safe composition across stdin/stdout/files/pipes needs more environment awareness than the small-agent fixture lane should assume |
| `AOA-T-0089` `quest-unit-promotion-review` | `medium-agent` | one verdict is atomic, but choosing among skill/playbook/agent/eval/memo/quest targets needs owner-shape comparison and evidence judgment |

## Orchestration Boundaries

| technique | current profile | direct-read verdict | why the outer wrapper remains required |
|---|---|---|---|
| `AOA-T-0085` `multi-axis-quest-overlay` | `orchestration-required` | `orchestration-boundary-confirmed` | flavor is safe only after an evidence-backed progression or route base exists; the overlay must not grant authority, rights, rank, memory, or routing truth |
| `AOA-T-0001` `plan-diff-apply-verify-report` | `orchestration-required` | `orchestration-boundary-confirmed` | the atom is reviewable change execution, but safe use crosses planning, mutation, validation, and report boundaries that need a larger workflow |
| `AOA-T-0014` `tdd-slice` | `orchestration-required` | `orchestration-boundary-confirmed` | the technique mutates code/tests and needs test-first discipline, implementation, refactor limits, and validation sequencing |
| `AOA-T-0036` `render-truth-before-startup` | `orchestration-required` | `orchestration-boundary-confirmed` | rendering effective runtime truth depends on local composition engines and pre-start operational state |
| `AOA-T-0037` `contextual-host-doctor` | `orchestration-required` | `orchestration-boundary-confirmed` | selector-aware host checks touch local runtime prerequisites and must influence preflight decisions through an outer gate |
| `AOA-T-0038` `one-command-service-lifecycle` | `orchestration-required` | `orchestration-boundary-confirmed` | the move owns a bounded lifecycle entrypoint, but actual start/stop behavior is mutating local service orchestration |
| `AOA-T-0068` `fail-closed-evidence-gate` | `orchestration-required` | `orchestration-boundary-confirmed` | the gate matters only if non-allow truly blocks side effects; that enforcement boundary cannot be proven by a prose-only small-agent fixture |

## Calibration Notes

- `small-agent` should continue to mean "a future fixture candidate after
  orchestration packs the exact local frame", not "safe autonomous execution".
- The reviewed `small-agent` rows are mostly packet, boundary, or single-check
  moves. They need a typed fixture more than a stronger model.
- `approval-bound-durable-jobs` is the closest edge case: the technique is
  small-agent shaped for reading/writing the durable approval packet, but real
  job continuation remains outside the fixture.
- `multi-axis-quest-overlay` is correctly not `small-agent`: the text is short,
  but misuse risk is authority drift, not text complexity.
- `plan-diff-apply-verify-report` and `tdd-slice` remain atomic technique
  moves, yet their safe execution is larger than a small fixture because they
  cross real mutation boundaries.

## Useful Threads

Carry these forward:

- Small-agent fixtures should explicitly include `forbidden hidden context`.
  This matters for donor-harvest and promotion-boundary rows because a model
  may otherwise import owner doctrine from memory.
- Some `small-agent` rows can be tested with synthetic packet fixtures before
  any repo mutation is allowed.
- The long pass should likely produce a fixture-sketch ledger grouped by
  substrate: reviewed session packet, approval seam, runtime benchmark,
  promotion boundary, and skill proposal.

## Stop Lines

- Do not relabel any profile from this wave alone.
- Do not promote `execution_profile` to frontmatter.
- Do not treat fixture sketches as empirical validation.
- Do not route job continuation, code mutation, service lifecycle, proof
  verdict, skill acceptance, or quest authority into `aoa-techniques`.

## Validation

This packet is a review-only source artifact. Required validation after landing
this wave:

1. `python -m unittest tests.test_distillation_mechanics_topology`
2. `python scripts/validate_repo.py`
3. `python scripts/release_check.py` before GitHub merge if the packet is
   published as a durable review surface
