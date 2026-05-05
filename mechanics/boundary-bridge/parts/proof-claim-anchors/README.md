# Proof Claim Anchors

This part maps current proof and public-claim boundary techniques so future
boundary-bridge work can name proof routes without issuing proof from
mechanics.

It does not change technique status. The canonical or promoted meaning remains
inside each `techniques/**/TECHNIQUE.md` file.

## Anchor Map

| Technique | Boundary-bridge relevance | Boundary |
|---|---|---|
| [AOA-T-0015 contract-test-design](../../../../techniques/evaluation/contract-test-design/TECHNIQUE.md) | Makes one consumer-visible boundary explicit through expected inputs, outputs, and verification. | Does not prove hidden internals or broader owner truth. |
| [AOA-T-0068 fail-closed-evidence-gate](../../../../techniques/agent-workflows/fail-closed-evidence-gate/TECHNIQUE.md) | Stops mutating execution unless explicit allow evidence exists. | Does not replace proof owners or broad approval policy. |
| [AOA-T-0092 audit-to-closeout-proof-loop](../../../../techniques/agent-workflows/audit-to-closeout-proof-loop/TECHNIQUE.md) | Turns reviewed audit findings into live-confirmed, proof-backed closeout. | Does not let audit wording become proof by itself. |
| [AOA-T-0093 recommendation-truth-vs-host-actionability](../../../../techniques/instruction/capability-boundary/recommendation-truth-vs-host-actionability/TECHNIQUE.md) | Separates recommendation truth from host actionability when tools or routing surfaces cannot execute a recommendation. | Does not let runnable action or router relevance masquerade as authority. |

## Use

Use this map when a boundary-shaped request wants to claim that a bridge,
projection, route, receipt, or generated surface is proven or publicly
supportable.

If the proof question needs a verdict, route to `aoa-evals` or the source
owner rather than expanding mechanics.

## Stop-lines

- Do not make public claims without evidence.
- Do not issue proof verdicts from this package.
- Do not treat generated companions, route hints, owner requests, or audit
  wording as proof.
