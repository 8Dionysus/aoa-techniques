# Stage Technique Anchors

This part maps AoA Growth Cycle stages to existing `aoa-techniques` bundles and
local hold lanes.

Use it when Growth-cycle pressure appears and the question is whether the next
move is already covered by a technique, still belongs in a local mechanics
part, or must route to a stronger owner.

It does not change bundle status. Canonical or promoted meaning remains inside
each `techniques/**/TECHNIQUE.md` file.

## Stage Anchor Map

| AoA center stage | Local Growth-cycle route | Existing technique anchor | Boundary |
|---|---|---|---|
| checkpoint intake | input only; keep checkpoint evidence provisional | [structured-handoff-before-compaction](../../../../techniques/continuity/handoff-continuation/structured-handoff-before-compaction/TECHNIQUE.md), [receipt-confirmed-handoff-packet](../../../../techniques/continuity/handoff-continuation/receipt-confirmed-handoff-packet/TECHNIQUE.md), [git-verified-handoff-claims](../../../../techniques/continuity/handoff-continuation/git-verified-handoff-claims/TECHNIQUE.md) | `mechanics/checkpoint`, `aoa-sdk`, and `aoa-skills` own checkpoint controls and bridge execution. |
| reviewed closeout chain | [promotion-readiness-incubation](../promotion-readiness-incubation/README.md) only after review | [harvest-packet-contract](../../../../techniques/continuity/donor-harvest/harvest-packet-contract/TECHNIQUE.md), [session-donor-harvest](../../../../techniques/continuity/donor-harvest/session-donor-harvest/TECHNIQUE.md) | A closeout note is lower-authority until reviewed; the packet is not promotion proof. |
| donor harvest | [mastery-harvest](../mastery-harvest/README.md) and promotion-readiness incubation | [session-donor-harvest](../../../../techniques/continuity/donor-harvest/session-donor-harvest/TECHNIQUE.md), [harvest-packet-contract](../../../../techniques/continuity/donor-harvest/harvest-packet-contract/TECHNIQUE.md), [owner-layer-triage](../../../../techniques/governance/decision-routing/owner-layer-triage/TECHNIQUE.md) | Donor harvest names candidate units and owner hints, not final technique truth. |
| progression lift | [technique-feat-model](../technique-feat-model/README.md) as derived reader support | [progression-evidence-lift](../../../../techniques/continuity/donor-harvest/progression-evidence-lift/TECHNIQUE.md), [multi-axis-quest-overlay](../../../../techniques/continuity/donor-harvest/multi-axis-quest-overlay/TECHNIQUE.md) | Progression and feat language stays descriptive; no rank, score, or owner acceptance. |
| route forks | questbook integration or hold, depending on the fork | [decision-fork-cards](../../../../techniques/governance/decision-routing/decision-fork-cards/TECHNIQUE.md), [owner-layer-triage](../../../../techniques/governance/decision-routing/owner-layer-triage/TECHNIQUE.md), [nearest-wrong-target-rejection](../../../../techniques/governance/promotion-boundary/nearest-wrong-target-rejection/TECHNIQUE.md) | Fork cards do not choose owner truth unless a bounded owner verdict is actually made. |
| automation opportunity | route away unless the reusable core is a technique candidate | [automation-fit-matrix](../../../../techniques/agent-workflows/automation-fit-matrix/TECHNIQUE.md), [human-loop-to-first-landing](../../../../techniques/agent-workflows/human-loop-to-first-landing/TECHNIQUE.md), [approval-sensitivity-check](../../../../techniques/agent-workflows/approval-sensitivity-check/TECHNIQUE.md) | Automation fit is descriptive and cannot activate hidden schedulers, hooks, runtime, or skills. |
| diagnosis gate | technique hardening or owner diagnosis only after reviewed friction exists | [diagnosis-from-reviewed-evidence](../../../../techniques/recovery/diagnosis-repair/diagnosis-from-reviewed-evidence/TECHNIQUE.md) | Diagnosis is read-only and does not repair or prove the cause. |
| repair cycle | questbook integration or technique hardening after diagnosis | [repair-shape-from-diagnosis](../../../../techniques/recovery/diagnosis-repair/repair-shape-from-diagnosis/TECHNIQUE.md), [checkpoint-bound-self-repair](../../../../techniques/recovery/diagnosis-repair/checkpoint-bound-self-repair/TECHNIQUE.md) | Repair shape stays smaller than playbook rollout and behind checkpoint posture when needed. |
| quest promotion | [questbook-integration](../questbook-integration/README.md) | [quest-unit-promotion-review](../../../../techniques/governance/promotion-boundary/quest-unit-promotion-review/TECHNIQUE.md), [multi-axis-quest-overlay](../../../../techniques/continuity/donor-harvest/multi-axis-quest-overlay/TECHNIQUE.md) | A quest remains a durable obligation until owner evidence supports another surface. |
| owner followthrough | request receipt, owner route, or hold | [owner-layer-triage](../../../../techniques/governance/decision-routing/owner-layer-triage/TECHNIQUE.md), [local-pattern-adoption-gate](../../../../techniques/governance/practice-adoption-lifecycle/local-pattern-adoption-gate/TECHNIQUE.md), [skill-proposal-handoff-packet](../../../../techniques/governance/promotion-boundary/skill-proposal-handoff-packet/TECHNIQUE.md) | Owner followthrough is not owner acceptance, proof, memory canon, or execution. |

## How To Use

1. Name the AoA center stage signal.
2. Check whether an existing technique anchor already owns the reusable move.
3. If an anchor exists, open that bundle rather than adding doctrine here.
4. If the signal is only local route pressure, update the owning Growth-cycle
   part and keep it mechanics-only.
5. If the signal needs hooks, skills, proof, memory, runtime, role, route,
   playbook, stats, seed, or owner acceptance, route to the stronger owner.
6. Record a quest only when the obligation survives the current bounded change.

## Open Gaps

- `promotion-readiness-incubation` still has no standalone technique bundle for
  "promotion-readiness discrimination." The existing anchors cover donor
  harvest, owner placement, progression, diagnosis, repair, automation, and
  quest promotion, but not the specific decision of when a promoted technique
  is ready for canonical review.
- The feat-card reader model remains an example-level local surface. Do not add
  generated feat manifests until there is a real reader need beyond this repo.
- Checkpoint intake remains checkpoint-owned. Growth-cycle may consume
  reviewed checkpoint evidence, but it should not become a second checkpoint
  mechanic.

## Stop-lines

- no achievement authority
- no permanent rank or universal progression score
- no hidden scheduler or autonomous self-repair
- no proof verdicts before `aoa-evals`
- no memory canon before `aoa-memo`
- no runtime export or activation before `abyss-stack`
- no executable workflow truth before `aoa-skills`
- no owner acceptance without owner-local receipt
- no automatic technique promotion
