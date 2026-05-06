# Owner Boundary Anchors

This part maps current owner-boundary technique bundles so future
boundary-bridge work starts from existing canon instead of redrafting owner
placement rules inside mechanics.

It does not change technique status. The canonical or promoted meaning remains
inside each `techniques/**/TECHNIQUE.md` file.

## Anchor Map

| Technique | Boundary-bridge relevance | Boundary |
|---|---|---|
| [AOA-T-0076 owner-layer-triage](../../../../techniques/governance/decision-routing/owner-layer-triage/TECHNIQUE.md) | Places one bounded reusable unit in one primary owner layer and rejects one nearest wrong target. | Does not extract donor units, finish promotion review, or make derivative routing a first-authoring owner. |
| [AOA-T-0090 nearest-wrong-target-rejection](../../../../techniques/governance/promotion-boundary/nearest-wrong-target-rejection/TECHNIQUE.md) | Makes the closest wrong owner or promotion target explicit so adjacent layers stay distinct. | Does not choose the full placement verdict or author the next surface. |
| [AOA-T-0016 bounded-context-map](../../../../techniques/proof/skill-support/bounded-context-map/TECHNIQUE.md) | Names contexts, responsibilities, and handoff interfaces before changes cross the wrong boundary. | Does not define a full architecture program or replace interface cleanup. |
| [AOA-T-0094 canonical-owner-with-validated-mirror](../../../../techniques/proof/owner-truth-closeout/canonical-owner-with-validated-mirror/TECHNIQUE.md) | Keeps one canonical cross-repo owner while allowing mirrors only through explicit parity validation. | Does not make mirrors new primary sources or own rollout choreography. |

## Use

Use this map when a boundary-shaped request appears and the smaller existing
technique may already answer it.

If the request needs a new atomic move, send it back through candidate review
instead of editing these anchors into a broader boundary doctrine.

## Stop-lines

- Do not treat owner placement as owner acceptance.
- Do not treat mirrored or nearby surfaces as source truth.
- Do not let boundary-bridge language override bundle-local contracts, risks,
  validation, or adjacent-technique boundaries.
