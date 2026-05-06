# Offer Evidence Reference Practice Gate Card

Source candidate:
`candidate:aoa-techniques:agon/offer-evidence-reference-practice`

Source route:
[Agon Move Technique Bridge](../../../../agon/parts/move-technique-bridge/README.md)
via [Agon Candidate Handoff](../README.md).

Center source check:
`Agents-of-Abyss` lawful move grammar lists `offer_evidence_reference` as a
pre-protocol evidence move that provides a reviewable reference or artifact
pointer without claiming final proof. Owner binding gives `aoa-techniques` only
the future practice candidate, while `aoa-evals` owns adequacy checks,
`aoa-skills` owns packaging workflow, and `aoa-memo` owns any future memory
intake.

## Gate Posture

Status: gate-packet-landed, with one linked technique bundle landed separately.

Lane: `first_narrowing_watch`.

This card proves only that the candidate can be offered as one portable
practice move. It does not define Agon evidence law, create a skill, issue a
proof verdict, write memory, or start arena behavior.
It remains a gate card, not a technique bundle; the linked bundle carries the
reusable technique surface.

## Atom

Offer exactly one evidence reference with its relevance, scope, and limit before
relying on it.

The move has five fields:

- reviewed claim or decision point
- evidence reference or artifact pointer
- relevance to the claim
- scope and limit of what the reference can support
- review or use condition before the reference is relied on

## Gate Example

- [offer-evidence-reference-minimal-public-safe](examples/offer-evidence-reference-minimal-public-safe.md)

## Gate Checklist

- [offer-evidence-reference-gate-checklist](checklists/offer-evidence-reference-gate-checklist.md)

## Gate Evidence Note

- [offer-evidence-reference-gate-evidence-note](evidence-notes/offer-evidence-reference-gate-evidence-note.md)

## Bundle Readiness Review

- [offer-evidence-reference-bundle-readiness-review](bundle-reviews/offer-evidence-reference-bundle-readiness-review.md)

## Landed Technique Bundle

- [single-scoped-evidence-reference](../../../../../techniques/proof/review-evidence/single-scoped-evidence-reference/TECHNIQUE.md)

## Topology Read

| Axis | Read |
|---|---|
| likely domain | `docs` |
| primary kind | `artifact` |
| family posture | review-evidence reference practice; first bundle landed locally |
| capability class | offer-evidence-reference |
| substrate | source reference, artifact pointer, citation, or excerpt boundary |
| execution profile | small-agent when the claim and acceptable reference form are supplied |
| risk posture | citation overclaim, source-truth laundering, proof-by-link |

The `evidence-reference` wording belongs in family or capability notes, not in
current `kind` frontmatter. The later bundle draft should use `artifact` unless
the kind registry changes first, because the reusable object is a scoped
reference artifact rather than an eval verdict or workflow.

## Portable Core

The portable core is not Agon law. It is a small reference move:

1. Name the claim or decision the reference touches.
2. Offer exactly one source, artifact, line, excerpt, or pointer.
3. Explain why the reference is relevant.
4. State what the reference can support and what it cannot support.
5. State the condition for later reliance, such as inspect, quote, rerun,
   verify, or keep only as a weak pointer.

This works outside OS Abyss when the orchestrator supplies the claim, current
review state, and acceptable reference form.

## AoA-Only Context

Inside AoA, Agon may supply the pressure source and legal move name. That
context stays outside the technique atom. The technique candidate may learn the
hand motion, not the law of the arena.

## Nearest Overlaps

- [single-missing-evidence-request](../../../../../techniques/proof/review-evidence/single-missing-evidence-request/TECHNIQUE.md):
  asks for one missing evidence object; this candidate offers one available
  reference with scope and limit.
- [multi-source-primary-input-provenance](../../../../../techniques/instruction/capability-boundary/multi-source-primary-input-provenance/TECHNIQUE.md):
  orders several inputs by priority; this candidate offers one reference before
  multi-source synthesis.
- [public-safe-artifact-sanitization](../../../../../techniques/instruction/docs-boundary/public-safe-artifact-sanitization/TECHNIQUE.md):
  sanitizes a shareable artifact; this candidate only scopes one reference and
  does not transform the artifact.

## Stop Lines

- Do not define Agon evidence move law.
- Do not create a skill workflow.
- Do not issue proof, verdict, route, memory, rank, scar, KAG, ToS, runtime, or
  arena effects.
- Do not treat a reference as final proof or source truth transfer.
- Do not offer a bundle of references when one scoped reference is enough.
- Do not treat the linked technique bundle as Agon source acceptance or proof
  authority.

## Next Move

Keep the landed technique bundle at promoted/source-backed posture. Collect
second-context evidence before any canonical review and keep Agon source status
unchanged.
