# Second Kind Ambiguity Review Pack

Status: review-pack-landed, no frontmatter remap by itself.

This packet is the fresh read after the first kind ambiguity shortlist closed.
It starts from the updated `reports/kind_ambiguity_audit.md`, then checks the
remaining pressure against direct bundle text, the kind registry, and the first
review pack.

It does not change frontmatter and does not authorize a broad remap wave.

## Source Packet

- updated `reports/kind_ambiguity_audit.md`
- [Technique Kind Registry](../../../../../config/technique_kind_registry.yaml)
- [Technique Kind Guide](../../../../../docs/TECHNIQUE_KIND_GUIDE.md)
- [Technique Topology Scout](../../../../../reports/technique_topology_scout.md)
- [First Kind Ambiguity Review Pack](first-kind-ambiguity-review-pack.md)

## Verdict

The updated audit is cleaner after the landed `AOA-T-0085`, `AOA-T-0005`, and
`AOA-T-0052` corrections, but it still repeats several already-reviewed false
positives. Those should stay held unless new bundle text changes the center of
gravity.

The only fresh pressure point is `AOA-T-0054`
`compaction-resilient-skill-loading`. The audit frames it as `handoff` vs
`workflow`, but direct reading exposes a third plausible destination:
`recovery`. The bundle is about bounded skill availability after context
compaction, which is continuation across loss, not an ordinary steady-state work
loop.

Packet-time next move: run one destination check for `AOA-T-0054` against
`handoff`, `workflow`, and `recovery`. Do not remap it from this packet alone.

Follow-up: [0054-kind-destination-check](0054-kind-destination-check.md)
landed the destination check and recommended remapping `AOA-T-0054` from
`handoff` to `recovery`.

## Direct Reads

| Technique | Current kind | Audit pressure | Review result |
|---|---:|---|---|
| [AOA-T-0054](../../../../../techniques/continuity/review-compaction/compaction-resilient-skill-loading/TECHNIQUE.md) | `handoff` | candidate remap to `workflow` | Hold for a destination check. The bundle centers post-compaction skill-availability recovery and resume. Workflow steps exist, but the normal-path loss makes `recovery` a real third candidate beside `handoff` and `workflow`. |
| [AOA-T-0028](../../../../../techniques/execution/agent-workflows-core/confirmation-gated-mutating-action/TECHNIQUE.md) | `guardrail` | candidate remap to `workflow` | Keep `guardrail`. The confirmation seam is still the center; procedure protects the gate. |
| [AOA-T-0093](../../../../../techniques/instruction/capability-boundary/recommendation-truth-vs-host-actionability/TECHNIQUE.md) | `guardrail` | candidate remap to `workflow` | Keep `guardrail`. Recommendation truth vs host executability is boundary posture, not a work loop. |
| [AOA-T-0091](../../../../../techniques/proof/owner-truth-closeout/workspace-root-ingress-and-mutation-gate/TECHNIQUE.md) | `guardrail` | revisit later | Keep `guardrail` for now. Ingress is procedural, but `must_confirm` and `blocked_actions` remain the reusable contract. |
| [AOA-T-0068](../../../../../techniques/governance/approval-evidence/fail-closed-evidence-gate/TECHNIQUE.md) | `guardrail` | keep current kind | Keep `guardrail`. Non-allow blocking before mutation is the center. |
| [AOA-T-0075](../../../../../techniques/continuity/donor-harvest/session-donor-harvest/TECHNIQUE.md) | `lift` | candidate remap to `artifact` | Keep `lift`. The donor pack is a bounded derived surface from reviewed evidence, not primary artifact authority. |
| [AOA-T-0008](../../../../../techniques/proof/published-summary/published-summary-remediation-snapshot/TECHNIQUE.md) | `lift` | candidate remap to `artifact` | Keep `lift`. It derives a read-only remediation snapshot from already published summaries. |
| [AOA-T-0088](../../../../../techniques/agent-workflows/approval-sensitivity-check/TECHNIQUE.md) | `assessment` | revisit later against `validation` | Keep `assessment`. The output is an approval-burden classification and downgrade route, not proof or permission. |
| [AOA-T-0089](../../../../../techniques/agent-workflows/quest-unit-promotion-review/TECHNIQUE.md) | `assessment` | revisit later against `validation` | Keep `assessment`. The output is owner-placement decision support, not validation proof and not promotion completion. |

## Boundary Notes

- The first shortlist remap wave is closed. `AOA-T-0085`, `AOA-T-0005`, and
  `AOA-T-0052` already landed as bounded frontmatter corrections.
- Repeated audit candidates are now review holds, not automatic next remaps.
- `AOA-T-0054` should be read with the registry definition of `recovery`, not
  only with the audit's `handoff` vs `workflow` tie-break.
- At packet time, the destination check could still have kept `AOA-T-0054` as
  `handoff`; the point was to name the real fork before touching bundle
  frontmatter.

## Next Honest Move

The landed narrow `AOA-T-0054` destination check followed this sequence:

1. read the bundle, example, checks, and notes again;
2. compare the primary reusable object against `handoff`, `workflow`, and
   `recovery`;
3. update frontmatter only if the destination check proves a stronger fit than
   current `handoff`;
4. add a decision note only if a public kind correction lands.
