# Bundle Anatomy Execution And Instruction Review

Source packet: [Technique Reform Ingress](../README.md)

Baseline packet: [Bundle Anatomy Baseline Inventory](bundle-anatomy-baseline-inventory.md)

Rubric packet: [Bundle Anatomy Rubric Hardening](bundle-anatomy-rubric-hardening.md)

Status: execution-instruction-direct-read-review, no leaf repair, not path movement, not
frontmatter migration, not status promotion.

## Verdict

Complete the first shelf-wide bundle anatomy audit wave over the execution and
instruction shelves.

Wave A directly reviewed `33` bundles across `9` shelves:

- `execution/agent-workflows-core`
- `execution/intent-chain`
- `execution/ready-work-graphs`
- `execution/runtime-truth-lifecycle`
- `instruction/docs-boundary`
- `instruction/instruction-surface`
- `instruction/capability-registry`
- `instruction/capability-boundary`
- `instruction/skill-discovery`

The wave finds no immediate leaf-repair cohort. Every reviewed bundle has a
clear atomic center, support files, generated catalog and capsule presence, and
current tree placement parity. The strongest repeated finding is
`old-template-watch`: these bundles usually predate explicit `Atomic move` and
`Small-agent execution shape` headings, but direct reading shows their intent,
procedure, checks, examples, risks, and capsules still carry the executable
center.

The second repeated finding is `owner-boundary-watch` on runtime, registry,
capability, and skill-discovery-adjacent bundles. That is not a failure; it is
the right caution for portable techniques that sit near `aoa-skills`,
`aoa-routing`, runtime, registry, or command surfaces without absorbing those
owners.

## Shelf Verdicts

| shelf | bundles | verdict | repair cohort |
|---|---:|---|---|
| `execution/agent-workflows-core` | 5 | healthy core workflow shelf; old-template watch only | none |
| `execution/intent-chain` | 2 | healthy intent-chain shelf; dry-run and fixture contracts stay atomic | none |
| `execution/ready-work-graphs` | 3 | healthy planning/graph shelf; task-graph adjacency remains bounded | none |
| `execution/runtime-truth-lifecycle` | 4 | healthy runtime-adjacent shelf; owner-boundary watch around runtime and eval posture | none |
| `instruction/docs-boundary` | 4 | healthy docs-boundary shelf; decision/status/sanitization contracts stay portable | none |
| `instruction/instruction-surface` | 7 | healthy instruction assembly/distribution shelf; generated-instruction boundary watch | none |
| `instruction/capability-registry` | 3 | healthy capability record/discovery shelf; registry/routing owner-boundary watch | none |
| `instruction/capability-boundary` | 3 | healthy capability boundary shelf; skill/command/recommendation seam watch | none |
| `instruction/skill-discovery` | 2 | healthy discovery/health shelf; skill marketplace and upstream-health owner watch | none |

## Bundle Rows

| id | shelf | anatomy labels | repair action | evidence refs |
|---|---|---|---|---|
| `AOA-T-0001` | `execution/agent-workflows-core` | `anatomy-pass`, `old-template-watch` | `no-repair` | `TECHNIQUE.md`, `checks/review-checklist.md`, `examples/minimal-change-flow.md`, `notes/adverse-effects-review.md` |
| `AOA-T-0014` | `execution/agent-workflows-core` | `anatomy-pass`, `old-template-watch` | `no-repair` | `TECHNIQUE.md`, `checks/tdd-slice-checklist.md`, examples, notes |
| `AOA-T-0023` | `execution/agent-workflows-core` | `anatomy-pass`, `old-template-watch` | `no-repair` | `TECHNIQUE.md`, checklist, examples, notes |
| `AOA-T-0028` | `execution/agent-workflows-core` | `anatomy-pass`, `old-template-watch` | `no-repair` | `TECHNIQUE.md`, checklist, examples, notes |
| `AOA-T-0031` | `execution/agent-workflows-core` | `anatomy-pass`, `old-template-watch` | `no-repair` | `TECHNIQUE.md`, checklist, examples, notes |
| `AOA-T-0004` | `execution/intent-chain` | `anatomy-pass`, `old-template-watch` | `no-repair` | `TECHNIQUE.md`, intent-chain checks, examples, notes |
| `AOA-T-0005` | `execution/intent-chain` | `anatomy-pass`, `old-template-watch`, `promotion-evidence-hold` | `no-repair` | `TECHNIQUE.md`, rollout checklist, examples, notes |
| `AOA-T-0049` | `execution/ready-work-graphs` | `anatomy-pass`, `old-template-watch`, `owner-boundary-watch`, `promotion-evidence-hold` | `no-repair` | `TECHNIQUE.md`, task-graph checklist, example, notes |
| `AOA-T-0050` | `execution/ready-work-graphs` | `anatomy-pass`, `old-template-watch`, `owner-boundary-watch`, `promotion-evidence-hold` | `no-repair` | `TECHNIQUE.md`, blocker-graph checklist, example, notes |
| `AOA-T-0055` | `execution/ready-work-graphs` | `anatomy-pass`, `old-template-watch`, `portability-watch`, `promotion-evidence-hold` | `no-repair` | `TECHNIQUE.md`, `checks/requirements-design-tasks-ladder-checklist.md`, example, external notes |
| `AOA-T-0036` | `execution/runtime-truth-lifecycle` | `anatomy-pass`, `old-template-watch`, `owner-boundary-watch`, `portability-watch`, `promotion-evidence-hold` | `no-repair` | `TECHNIQUE.md`, runtime truth checklist, example, notes |
| `AOA-T-0037` | `execution/runtime-truth-lifecycle` | `anatomy-pass`, `old-template-watch`, `owner-boundary-watch`, `promotion-evidence-hold` | `no-repair` | `TECHNIQUE.md`, host-doctor checklist, example, notes |
| `AOA-T-0038` | `execution/runtime-truth-lifecycle` | `anatomy-pass`, `old-template-watch`, `owner-boundary-watch`, `portability-watch`, `promotion-evidence-hold` | `no-repair` | `TECHNIQUE.md`, lifecycle checklist, example, notes |
| `AOA-T-0039` | `execution/runtime-truth-lifecycle` | `anatomy-pass`, `old-template-watch`, `owner-boundary-watch`, `promotion-evidence-hold` | `no-repair` | `TECHNIQUE.md`, benchmark checklist, example, notes |
| `AOA-T-0002` | `instruction/docs-boundary` | `anatomy-pass`, `old-template-watch` | `no-repair` | `TECHNIQUE.md`, source-of-truth checklist, example, notes |
| `AOA-T-0009` | `instruction/docs-boundary` | `anatomy-pass`, `old-template-watch` | `no-repair` | `TECHNIQUE.md`, status snapshot checklist, example, notes |
| `AOA-T-0033` | `instruction/docs-boundary` | `anatomy-pass`, `old-template-watch`, `promotion-evidence-hold` | `no-repair` | `TECHNIQUE.md`, decision-rationale checklist, example, notes |
| `AOA-T-0034` | `instruction/docs-boundary` | `anatomy-pass`, `old-template-watch` | `no-repair` | `TECHNIQUE.md`, sanitization checklist, example, notes |
| `AOA-T-0012` | `instruction/instruction-surface` | `anatomy-pass`, `old-template-watch`, `owner-boundary-watch` | `no-repair` | `TECHNIQUE.md`, deterministic context checklist, examples, notes |
| `AOA-T-0013` | `instruction/instruction-surface` | `anatomy-pass`, `old-template-watch`, `owner-boundary-watch` | `no-repair` | `TECHNIQUE.md`, rule distribution checklist, examples, notes |
| `AOA-T-0024` | `instruction/instruction-surface` | `anatomy-pass`, `old-template-watch`, `owner-boundary-watch`, `promotion-evidence-hold` | `no-repair` | `TECHNIQUE.md`, mirroring checklist, examples, notes |
| `AOA-T-0027` | `instruction/instruction-surface` | `anatomy-pass`, `old-template-watch`, `owner-boundary-watch`, `promotion-evidence-hold` | `no-repair` | `TECHNIQUE.md`, propagation checklist, examples, notes |
| `AOA-T-0029` | `instruction/instruction-surface` | `anatomy-pass`, `old-template-watch`, `owner-boundary-watch`, `promotion-evidence-hold` | `no-repair` | `TECHNIQUE.md`, nested-rule checklist, examples, notes |
| `AOA-T-0030` | `instruction/instruction-surface` | `anatomy-pass`, `old-template-watch`, `owner-boundary-watch`, `promotion-evidence-hold` | `no-repair` | `TECHNIQUE.md`, fragmented-context checklist, examples, notes |
| `AOA-T-0035` | `instruction/instruction-surface` | `anatomy-pass`, `old-template-watch`, `owner-boundary-watch`, `promotion-evidence-hold` | `no-repair` | `TECHNIQUE.md`, profile-preset checklist, example, notes |
| `AOA-T-0025` | `instruction/capability-registry` | `anatomy-pass`, `old-template-watch`, `owner-boundary-watch`, `promotion-evidence-hold` | `no-repair` | `TECHNIQUE.md`, capability spec checklist, examples, notes |
| `AOA-T-0063` | `instruction/capability-registry` | `anatomy-pass`, `old-template-watch`, `owner-boundary-watch`, `promotion-evidence-hold` | `no-repair` | `TECHNIQUE.md`, registry contract checklist, example, notes |
| `AOA-T-0064` | `instruction/capability-registry` | `anatomy-pass`, `old-template-watch`, `owner-boundary-watch`, `promotion-evidence-hold` | `no-repair` | `TECHNIQUE.md`, capability discovery checklist, example, notes |
| `AOA-T-0040` | `instruction/capability-boundary` | `anatomy-pass`, `old-template-watch`, `owner-boundary-watch`, `promotion-evidence-hold` | `no-repair` | `TECHNIQUE.md`, skill-command boundary checklist, example, notes |
| `AOA-T-0043` | `instruction/capability-boundary` | `anatomy-pass`, `old-template-watch`, `owner-boundary-watch`, `promotion-evidence-hold` | `no-repair` | `TECHNIQUE.md`, provenance checklist, example, notes |
| `AOA-T-0093` | `instruction/capability-boundary` | `anatomy-pass`, `old-template-watch`, `owner-boundary-watch`, `promotion-evidence-hold` | `no-repair` | `TECHNIQUE.md`, recommendation/actionability checklist, example, notes |
| `AOA-T-0041` | `instruction/skill-discovery` | `anatomy-pass`, `old-template-watch`, `owner-boundary-watch`, `promotion-evidence-hold` | `no-repair` | `TECHNIQUE.md`, marketplace curation checklist, example, notes |
| `AOA-T-0042` | `instruction/skill-discovery` | `anatomy-pass`, `old-template-watch`, `owner-boundary-watch`, `promotion-evidence-hold` | `no-repair` | `TECHNIQUE.md`, upstream health checklist, example, notes |

## Wave A Label Counts

| label | bundles |
|---|---:|
| `anatomy-pass` | 33 |
| `old-template-watch` | 33 |
| `owner-boundary-watch` | 21 |
| `promotion-evidence-hold` | 24 |
| `portability-watch` | 4 |
| `no-repair` | 33 |

## Findings

### Old Template Watch Is Not A Repair Mandate

All Wave A bundles predate the newest template sections for explicit
`Atomic move` and `Small-agent execution shape`. Direct reading does not justify
rewriting all of them now. Their summaries, intent sections, core procedures,
validation sections, support files, and capsules still carry the executable
move.

Carry `old-template-watch` as a future modernization cohort only if later waves
show that small-agent usability truly suffers, or if a selected repair cohort
already needs nearby edits.

### Owner-Boundary Watch Is Healthy In This Wave

Instruction and runtime-adjacent shelves naturally sit near stronger owners:
skills, commands, runtime, routing, registry, generated instruction surfaces,
and upstream health checks. The reviewed bundles are healthy because they name
one technique-level seam and keep stronger owner doctrine out.

Do not convert these watches into route-away verdicts without a later direct
finding that the atom has collapsed.

### No First Repair Cohort From Wave A Alone

Wave A does not name a repair cohort. The next honest move is Wave B, not leaf
rewriting. The first repair cohort should be chosen only after Waves A, B, and
C are synthesized together, unless a later wave finds a blocking defect.

## Next Gate

Run Wave B over proof, continuity, and governance shelves:

1. `proof/skill-support`
2. `proof/evaluation-chain`
3. `proof/published-summary`
4. `proof/review-evidence`
5. `proof/owner-truth-closeout`
6. `continuity/review-compaction`
7. `continuity/handoff-continuation`
8. `continuity/donor-harvest`
9. `governance/approval-evidence`
10. `governance/decision-routing`
11. `governance/automation-readiness`
12. `governance/promotion-boundary`
13. `governance/practice-adoption-lifecycle`

## Stop Lines

- Do not rewrite Wave A leaves just to add current-template headings.
- Do not treat `owner-boundary-watch` as a route-away decision.
- Do not promote Wave A `promoted` bundles from anatomy health alone.
- Do not open generated capsule repair from Wave A; carry known capsule
  pressure into the corpus synthesis.
- Do not choose the first repair cohort until all three shelf-audit waves have
  landed or a blocking defect appears.
