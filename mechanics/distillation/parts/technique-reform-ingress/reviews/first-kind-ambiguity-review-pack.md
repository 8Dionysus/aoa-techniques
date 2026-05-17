# First Kind Ambiguity Review Pack

Source packet:
[Technique Reform Ingress](../README.md)

Generated lens:
[Kind Ambiguity Audit](../reports/kind_ambiguity_audit.md)

Kind source:
[Technique Kind Registry](../../../../../config/technique_kind_registry.yaml)
and
[Technique Kind Guide](../../../../../docs/selection/TECHNIQUE_KIND_GUIDE.md)

Preceding review:
[First Topology Scout Review Pack](first-topology-scout-review-pack.md)

Status: review-pack-landed, first shortlist remap wave closed.

## Verdict

The first direct-read kind ambiguity pass confirms that the generated audit is
useful for choosing review targets, but too broad to drive remaps by itself.

The first strongest later remap shortlist is now closed.

This review did not change bundle frontmatter by itself, did not add a new
`kind`, and did not claim every remap was ready to land. The first follow-up
remap wave landed `AOA-T-0085` as `lift` after moving bundle frontmatter,
generated surfaces, tests, route notes, and a decision note together. The next
follow-up remap wave landed `AOA-T-0005` as `workflow` with the same bounded
publication path. The final shortlist remap landed `AOA-T-0052` as `workflow`
after checking `workflow`, `validation`, and `lift` as possible destinations.

## Direct Reads

| Technique | Current `kind` | Audit cue | Direct-read verdict |
|---|---|---|---|
| [AOA-T-0028](../../../../../techniques/execution/agent-workflows-core/confirmation-gated-mutating-action/TECHNIQUE.md) | `guardrail` | `candidate remap` to `workflow` | Keep `guardrail`. The confirmation seam is the center of the contract; procedure exists to protect the gate. |
| [AOA-T-0005](../../../../../techniques/execution/intent-chain/new-intent-rollout-checklist/TECHNIQUE.md) | `workflow` | second shortlist remap landed | Landed. The bundle's reusable object is the rollout path through fixtures, smoke, contract check, publication, and regression. Dry-run safety is risk posture, not the primary kind. |
| [AOA-T-0093](../../../../../techniques/instruction/capability-boundary/recommendation-truth-vs-host-actionability/TECHNIQUE.md) | `guardrail` | `candidate remap` to `workflow` | Keep `guardrail`. The technique preserves a boundary between recommendation truth and host executability; the boundary law is stronger than the procedure. |
| [AOA-T-0091](../../../../../techniques/proof/owner-truth-closeout/workspace-root-ingress-and-mutation-gate/TECHNIQUE.md) | `guardrail` | `revisit later` | Keep `guardrail` for now. Ingress and guard are procedural, but `must_confirm` and `blocked_actions` posture is the primary reusable object. |
| [AOA-T-0075](../../../../../techniques/continuity/donor-harvest/session-donor-harvest/TECHNIQUE.md) | `lift` | `candidate remap` to `artifact` | Keep `lift`. The donor pack is derived from a reviewed artifact and stays weaker than owner placement or promotion. |
| [AOA-T-0085](../../../../../techniques/continuity/donor-harvest/multi-axis-quest-overlay/TECHNIQUE.md) | `lift` | first shortlist remap landed | Landed. The overlay is an adjunct derived surface over reviewed progression or route evidence, and it must stay weaker than owner truth. |
| [AOA-T-0008](../../../../../techniques/proof/published-summary/published-summary-remediation-snapshot/TECHNIQUE.md) | `lift` | `candidate remap` to `artifact` | Keep `lift`. The snapshot is durable, but it is a downstream read-only view over already-published summaries. |
| [AOA-T-0052](../../../../../techniques/continuity/review-compaction/review-findings-compaction/TECHNIQUE.md) | `workflow` | final shortlist remap landed | Landed. Transfer is not the center; the reusable move is dedupe, revalidation, and consolidation. The destination check rejected `validation` as an internal step and `lift` as a weaker fit than the ordered consolidation pass. |
| [AOA-T-0088](../../../../../techniques/agent-workflows/approval-sensitivity-check/TECHNIQUE.md) | `assessment` | `revisit later` | Keep `assessment`. The output is a classification verdict over approval burden, not proof that execution is allowed. |
| [AOA-T-0089](../../../../../techniques/agent-workflows/quest-unit-promotion-review/TECHNIQUE.md) | `assessment` | `revisit later` | Keep `assessment`. The output is owner-placement decision support; it is not validation proof and not promotion completion. |
| [AOA-T-0068](../../../../../techniques/governance/approval-evidence/fail-closed-evidence-gate/TECHNIQUE.md) | `guardrail` | `keep current kind` | Calibration read. The report is correct: non-allow blocking and explicit allow are the center. |
| [AOA-T-0049](../../../../../techniques/execution/ready-work-graphs/dependency-aware-task-graph/TECHNIQUE.md) | `workflow` | `keep current kind` | Calibration read. The graph supports a stepwise work loop; blocker cues do not make it a guardrail. |

## What The Audit Got Right

- It found the real pressure points around `workflow` vs `guardrail`,
  `artifact` vs `lift`, and `handoff` vs `workflow`.
- It correctly treated family-spanning clusters as review pressure rather than
  automatic remap authority.
- It exposed that words like `snapshot`, `artifact`, `workflow`, and `gate` can
  be misleading unless the reviewer asks what the technique primarily does.

## What Direct Reading Changed

The generated audit over-called several remaps because lexical cues were louder
than the actual center of gravity.

- `AOA-T-0028`, `AOA-T-0093`, and `AOA-T-0091` contain procedural steps, but
  the primary reusable contract is still boundary or gate posture.
- `AOA-T-0075` and `AOA-T-0008` emit durable surfaces, but those surfaces are
  derived from stronger source material and remain downstream views.
- `AOA-T-0088` and `AOA-T-0089` contain proof-like or promotion-like language,
  but their outputs are classifications and verdict supports rather than proof.

## Shortlist For Later Remap Work

Do not continue into a new broad remap sweep from this review pack. The first
shortlist has landed in three narrow waves:

1. `AOA-T-0085`: `artifact` -> `lift`
2. `AOA-T-0005`: `guardrail` -> `workflow`
3. `AOA-T-0052`: `handoff` -> `workflow`

Why stop here:

- the remaining audit candidates in this pack were already kept as current-kind
  holds after direct reading
- any next remap candidate should come from a fresh direct-read pass over the
  updated generated audit, not from extending this closed shortlist by inertia

## Stop Lines

- Do not change frontmatter from this review alone.
- Do not add `review`, `check`, `overlay`, `gate`, or `remap` as new `kind`
  values from these cues.
- Do not treat generated audit verdicts as stronger than direct bundle meaning.
- Do not use `family` as a hidden replacement for kind decisions.
- Do not change canonical or promoted status during a kind remap.

## Next Honest Move

Pause the first remap wave and run a fresh kind ambiguity read before any
additional frontmatter changes. If another candidate is chosen, start from the
updated generated audit, read the bundle directly, and land bundle frontmatter,
generated surfaces, tests, route notes, and a decision note together.
