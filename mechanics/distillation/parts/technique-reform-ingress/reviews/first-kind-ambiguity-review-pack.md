# First Kind Ambiguity Review Pack

Source packet:
[Technique Reform Ingress](../README.md)

Generated lens:
[Kind Ambiguity Audit](../../../../../reports/kind_ambiguity_audit.md)

Kind source:
[Technique Kind Registry](../../../../../config/technique_kind_registry.yaml)
and
[Technique Kind Guide](../../../../../docs/TECHNIQUE_KIND_GUIDE.md)

Preceding review:
[First Topology Scout Review Pack](first-topology-scout-review-pack.md)

Status: review-pack-landed, not a remap wave.

## Verdict

The first direct-read kind ambiguity pass confirms that the generated audit is
useful for choosing review targets, but too broad to drive remaps by itself.

The strongest later remap candidates are:

- `AOA-T-0005` from `guardrail` toward `workflow`
- `AOA-T-0085` from `artifact` toward `lift`
- `AOA-T-0052` away from `handoff`, with `workflow` as the current closest
  registry-backed target

This review does not change bundle frontmatter, does not add a new `kind`, and
does not claim those remaps are ready to land. It only narrows the next honest
candidate set after reading the bundles directly.

## Direct Reads

| Technique | Current `kind` | Audit cue | Direct-read verdict |
|---|---|---|---|
| [AOA-T-0028](../../../../../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) | `guardrail` | `candidate remap` to `workflow` | Keep `guardrail`. The confirmation seam is the center of the contract; procedure exists to protect the gate. |
| [AOA-T-0005](../../../../../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) | `guardrail` | `candidate remap` to `workflow` | Strong remap candidate. The bundle's reusable object is the rollout path through fixtures, smoke, contract check, publication, and regression. Dry-run safety is risk posture, not the primary kind. |
| [AOA-T-0093](../../../../../techniques/agent-workflows/recommendation-truth-vs-host-actionability/TECHNIQUE.md) | `guardrail` | `candidate remap` to `workflow` | Keep `guardrail`. The technique preserves a boundary between recommendation truth and host executability; the boundary law is stronger than the procedure. |
| [AOA-T-0091](../../../../../techniques/agent-workflows/workspace-root-ingress-and-mutation-gate/TECHNIQUE.md) | `guardrail` | `revisit later` | Keep `guardrail` for now. Ingress and guard are procedural, but `must_confirm` and `blocked_actions` posture is the primary reusable object. |
| [AOA-T-0075](../../../../../techniques/agent-workflows/session-donor-harvest/TECHNIQUE.md) | `lift` | `candidate remap` to `artifact` | Keep `lift`. The donor pack is derived from a reviewed artifact and stays weaker than owner placement or promotion. |
| [AOA-T-0085](../../../../../techniques/agent-workflows/multi-axis-quest-overlay/TECHNIQUE.md) | `artifact` | `candidate remap` to `lift` | Strong remap candidate. The overlay is an adjunct derived surface over reviewed progression or route evidence, and it must stay weaker than owner truth. |
| [AOA-T-0008](../../../../../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) | `lift` | `candidate remap` to `artifact` | Keep `lift`. The snapshot is durable, but it is a downstream read-only view over already-published summaries. |
| [AOA-T-0052](../../../../../techniques/agent-workflows/review-findings-compaction/TECHNIQUE.md) | `handoff` | `candidate remap` to `workflow` | Strong remap candidate away from `handoff`. Transfer is not the center; the reusable move is dedupe, revalidation, and consolidation. `workflow` is the nearest current target, though a future review should still check `validation` and `lift` before editing frontmatter. |
| [AOA-T-0088](../../../../../techniques/agent-workflows/approval-sensitivity-check/TECHNIQUE.md) | `assessment` | `revisit later` | Keep `assessment`. The output is a classification verdict over approval burden, not proof that execution is allowed. |
| [AOA-T-0089](../../../../../techniques/agent-workflows/quest-unit-promotion-review/TECHNIQUE.md) | `assessment` | `revisit later` | Keep `assessment`. The output is owner-placement decision support; it is not validation proof and not promotion completion. |
| [AOA-T-0068](../../../../../techniques/agent-workflows/fail-closed-evidence-gate/TECHNIQUE.md) | `guardrail` | `keep current kind` | Calibration read. The report is correct: non-allow blocking and explicit allow are the center. |
| [AOA-T-0049](../../../../../techniques/agent-workflows/dependency-aware-task-graph/TECHNIQUE.md) | `workflow` | `keep current kind` | Calibration read. The graph supports a stepwise work loop; blocker cues do not make it a guardrail. |

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

Do not remap all three in one broad sweep unless the remap wave has explicit
scope, tests, generated-surface sync, and reviewer focus. The cleaner order is:

1. `AOA-T-0085`: `artifact` -> `lift`
2. `AOA-T-0005`: `guardrail` -> `workflow`
3. `AOA-T-0052`: `handoff` -> likely `workflow`, after one extra check against
   `validation` and `lift`

Why this order:

- `AOA-T-0085` is the cleanest source-weaker-than-derived-surface case.
- `AOA-T-0005` is a straightforward rollout procedure, but it is already
  source-backed and promoted, so the remap should be visible and narrow.
- `AOA-T-0052` is probably not `handoff`, but the destination deserves one more
  tie-break read before frontmatter changes.

## Stop Lines

- Do not change frontmatter from this review alone.
- Do not add `review`, `check`, `overlay`, `gate`, or `remap` as new `kind`
  values from these cues.
- Do not treat generated audit verdicts as stronger than direct bundle meaning.
- Do not use `family` as a hidden replacement for kind decisions.
- Do not change canonical or promoted status during a kind remap.

## Next Honest Move

Prepare one narrow remap wave, starting with `AOA-T-0085`, only if the pass
updates bundle frontmatter, generated surfaces, tests, and route notes together.
If the next pass should stay review-only, read `AOA-T-0052` against
`validation` and `lift` before choosing its destination.
