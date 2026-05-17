# Execution Profile Medium-Agent Calibration Review

Source packet: [Technique Reform Ingress](../README.md)

Status: direct-read review packet for the Phase 2 `medium-agent` cohort. No
local model harness was run. No frontmatter, schema, generated scout rule,
capsule builder, registry, or technique leaf was changed.

## Verdict

The current `medium-agent` profile is mostly doing useful work: it marks
atomic techniques whose safe execution needs more comparison, multi-surface
awareness, or judgement than the `small-agent` fixture lane should carry.

The reviewed rows are not broad enough to become skills or playbooks by
default. Most remain one technique. They require medium context because the
agent must preserve one or more of these boundaries while acting:

- current artifact versus stale artifact;
- graph state versus remembered readiness;
- selected owner versus adjacent wrong owner;
- reviewed evidence versus live proof;
- source fragment versus generated target;
- adopted practice versus current usefulness;
- symptom, drift type, diagnosis, and repair shape.

No row in this phase is confirmed as a clean `small-agent` candidate from
direct reading alone. One row, `AOA-T-0095`
`github-only-owner-endcap-with-reality-sync`, is flagged `scout-needs-review`
because its authored procedure and outputs include a real GitHub-native owner
landing before coordination-layer sync. That may belong in the
`orchestration-required` review lane when Phase 3 samples owner-truth wrappers.

Reviewed rows:

| profile | rows reviewed | verdict |
|---|---:|---|
| `medium-agent` | 21 | mostly confirmed as medium calibration rows |
| `scout-needs-review` subset | 1 | carry to Phase 3 and Phase 5 |
| possible future small fixture subset | 0 | no relabel from this packet |

## Reviewed Surfaces

Reviewed before this packet:

- `AGENTS.md`
- `docs/TECHNIQUE_ATOM_CONTRACT.md`
- `docs/TECHNIQUE_TOPOLOGY_CONTRACT.md`
- `docs/TECHNIQUE_TREE_CONTRACT.md`
- `mechanics/distillation/parts/technique-reform-ingress/config/technique_topology_axes.yaml`
- `mechanics/distillation/parts/technique-reform-ingress/reports/technique_topology_scout.json`
- `mechanics/distillation/parts/technique-reform-ingress/reports/technique_topology_scout.md`
- `docs/readers/runtime/TECHNIQUE_CAPSULES.md`
- `techniques/continuity/AGENTS.md`
- `techniques/execution/AGENTS.md`
- `techniques/governance/AGENTS.md`
- `techniques/instruction/AGENTS.md`
- `techniques/proof/AGENTS.md`
- `techniques/recovery/AGENTS.md`
- all `TECHNIQUE.md`, capsule, checklist, example, and note surfaces for the
  21 reviewed rows

## Medium Rows

| technique | shelf | direct-read verdict | why medium, not small | why not orchestration by default |
|---|---|---|---|---|
| `AOA-T-0004` `intent-plan-dry-run-contract-chain` | `execution/intent-chain` | `scout-confirmed` | the agent must preserve intent normalization, plan artifact, dry-run evidence, and contract check links across one chain | the chain is dry-run-only and explicitly refuses real action before execution |
| `AOA-T-0005` `new-intent-rollout-checklist` | `execution/intent-chain` | `scout-confirmed` | extending one existing intent-chain requires fixture parity, smoke path, and contract-drift awareness | the move adds one intent fixture/checklist rather than executing live automation |
| `AOA-T-0023` `stateless-single-shot-agent` | `execution/agent-workflows-core` | `scout-confirmed` | the capsule is compact, but the agent must resist hidden state, tool-loop creep, and multi-step expansion | one invocation remains read-only or one confirmed step; a full workflow wrapper is not inherent |
| `AOA-T-0031` `shell-composable-agent-invocation` | `execution/agent-workflows-core` | `scout-confirmed` | shell composition requires awareness of stdin, stdout, files, pipes, and hidden session-state failure modes | the technique stays one shell-visible invocation and refuses autonomous loops |
| `AOA-T-0049` `dependency-aware-task-graph` | `execution/ready-work-graphs` | `scout-confirmed` | graph nodes, edges, blocked state, and ready frontier must stay mutually consistent | the output is a planning graph, not task execution or scheduling authority |
| `AOA-T-0050` `ready-work-from-blocker-graph` | `execution/ready-work-graphs` | `scout-confirmed` | the agent must derive a queue from explicit blocker state and preserve excluded blocked reasons | the move reports a ready frontier; it does not perform the work or own prioritization policy |
| `AOA-T-0055` `requirements-design-tasks-ladder` | `execution/ready-work-graphs` | `scout-confirmed` | three layers must stay distinct and traceable from requirement to design to task slices | the output is a planning ladder, not implementation or spec governance |
| `AOA-T-0051` `commit-triggered-background-review` | `continuity/review-compaction` | `scout-confirmed`; sample again in Phase 3 | commit target, bounded review scope, runner or queue surface, and durable artifact link all need context | the technique forbids auto-merge, auto-rewrite, and CI governance; a real job runner may still be an outer wrapper |
| `AOA-T-0052` `review-findings-compaction` | `continuity/review-compaction` | `scout-confirmed` | noisy findings must be compared against current code so duplicates and stale findings do not survive as truth | compaction produces a read-only current findings artifact and does not fix code |
| `AOA-T-0076` `owner-layer-triage` | `governance/decision-routing` | `scout-confirmed` | the agent compares adjacent AoA owner layers and rejects one nearest-wrong target without collapsing reuse kinds | the output is a routing verdict aid, not owner authority or repo mutation |
| `AOA-T-0086` `automation-fit-matrix` | `governance/automation-readiness` | `scout-confirmed` | repeat signal, determinism, proof posture, reversibility, and approval sensitivity must be weighed together | the matrix does not create automation authority or run automation |
| `AOA-T-0087` `human-loop-to-first-landing` | `governance/automation-readiness` | `scout-confirmed` | one recurring loop must be matched to a first honest landing such as skill, playbook seed, repair quest, or defer | the output is a landing recommendation, not live automation or owner acceptance |
| `AOA-T-0089` `quest-unit-promotion-review` | `governance/promotion-boundary` | `scout-confirmed` | choosing among quest, skill, playbook, route, role, proof, recall, or defer requires owner-shape comparison | the verdict is bounded and evidence-linked; it does not author the receiving object |
| `AOA-T-0103` `adopted-practice-retention-review` | `governance/practice-adoption-lifecycle` | `scout-confirmed` | retention depends on original adoption record, current evidence, usefulness, drift, and rollback posture | the output is a retain/revise/quarantine/defer/route verdict, not live adoption governance |
| `AOA-T-0012` `deterministic-context-composition` | `instruction/instruction-surface` | `scout-confirmed` | source fragments, ordering rules, generated output, and traceability must remain aligned | the technique is composition/readout, not runtime code loading or hidden prompt control |
| `AOA-T-0029` `nested-rule-loading` | `instruction/instruction-surface` | `scout-confirmed` | precedence among canonical, parent, and nested layers must be preserved and explainable | the output is layered rule resolution, not runtime law or independent local authority |
| `AOA-T-0035` `profile-preset-composition` | `instruction/instruction-surface` | `scout-confirmed` | module, profile, preset, duplicate handling, and expansion order must stay separate | the technique defines reviewable composition posture, not launcher doctrine or runtime owner law |
| `AOA-T-0080` `session-drift-taxonomy` | `recovery/diagnosis-repair` | `scout-confirmed` | several reviewed frictions must be classified without jumping to cause, owner, or repair shape | the output is read-only taxonomy and explicitly not diagnosis or mutation |
| `AOA-T-0081` `diagnosis-from-reviewed-evidence` | `recovery/diagnosis-repair` | `scout-confirmed` | symptoms, probable causes, unknowns, and owner hints must stay distinct and evidence-linked | the output is a diagnosis packet and does not repair anything yet |
| `AOA-T-0092` `audit-to-closeout-proof-loop` | `proof/owner-truth-closeout` | `scout-confirmed` | reviewed audit findings must be compared against live source and proof-backed closeout evidence | the technique can remain medium when used as proof mapping; actual fixes remain owner-surface work |
| `AOA-T-0095` `github-only-owner-endcap-with-reality-sync` | `proof/owner-truth-closeout` | `scout-needs-review` | owner-native GitHub state, merge evidence, staging truth, and post-merge reality sync must all align | the authored output includes a merged owner-side landing, so Phase 3 should test whether this really needs orchestration-required |

## Calibration Patterns

Medium rows fall into five repeatable shapes:

| pattern | rows | calibration note |
|---|---|---|
| chain and shell boundary | `AOA-T-0004`, `AOA-T-0005`, `AOA-T-0023`, `AOA-T-0031` | compact, but hidden execution state and chain drift make small-agent proof risky without broader context |
| graph and planning state | `AOA-T-0049`, `AOA-T-0050`, `AOA-T-0055` | the move is read-only planning, but correctness depends on preserving several linked nodes or layers |
| reviewed evidence comparison | `AOA-T-0051`, `AOA-T-0052`, `AOA-T-0080`, `AOA-T-0081`, `AOA-T-0092` | medium is mostly about comparing stale/current/reviewed/live evidence without turning comparison into proof doctrine |
| owner and adoption judgement | `AOA-T-0076`, `AOA-T-0086`, `AOA-T-0087`, `AOA-T-0089`, `AOA-T-0103` | the technique stays one verdict, but the agent must compare nearby owner or lifecycle options |
| instruction composition precedence | `AOA-T-0012`, `AOA-T-0029`, `AOA-T-0035` | medium protects precedence, source/target traceability, and generated-output limits |

## Possible Profile Follow-Up

No `medium-agent` row should be promoted to `small-agent` from direct reading
alone. Several can use toy examples, but a toy example would hide the reason
they are medium in the current corpus.

Rows to sample again in Phase 3:

- `AOA-T-0095` `github-only-owner-endcap-with-reality-sync`: likely
  orchestration edge because the procedure includes issue/PR/CI/merge and
  post-merge coordination sync.
- `AOA-T-0051` `commit-triggered-background-review`: medium as a read-only
  review packet pattern, but actual background runner or queue activation may
  need an orchestration wrapper.
- `AOA-T-0092` `audit-to-closeout-proof-loop`: medium as a proof-mapping loop,
  but any owner-surface fixes inside the loop route away from this review lane.

Rows not worth small-agent demotion now:

- `AOA-T-0023` and `AOA-T-0031` look small in one-shot examples, but their
  actual value is preventing hidden state, shell leakage, and loop expansion.
- `AOA-T-0012`, `AOA-T-0029`, and `AOA-T-0035` look small on two fragments, but
  source precedence and generated-output traceability are the whole point.
- `AOA-T-0050` can derive a tiny queue, but the current profile should still
  reflect blocker-graph comparison rather than the shortest possible example.

## Useful Threads

Carry these forward:

- Phase 3 should not treat `orchestration-required` as "larger than medium";
  some rows are tiny but need approval, runner, host, public-share, or owner
  wrappers.
- Phase 4 fixture ledger should probably not include medium rows as executable
  small-agent candidates. It can still reference medium rows as negative or
  contrast fixtures.
- Phase 5 should check whether the scout wording can better explain rows that
  are medium for comparison but orchestration-required for side-effect
  execution.
- `AOA-T-0095` is the first clear candidate where authored output and current
  scout profile may disagree.

## Stop Lines

- Do not relabel medium rows from this packet alone.
- Do not treat toy examples as proof that a row should become `small-agent`.
- Do not mutate technique leaves, generated scout rules, registry wording, or
  frontmatter in this wave.
- Do not route owner-layer verdict authority, GitHub execution, background
  runner control, live remediation, instruction runtime law, or recovery repair
  into `aoa-techniques`.

## Validation

This packet is a review-only source artifact. Required validation after landing
this wave:

1. `python -m unittest tests.test_distillation_mechanics_topology`
2. `python scripts/validate_repo.py`
3. `python scripts/release_check.py` before GitHub merge
