# Risk And Negative-Effect Lift Guide

This guide defines the bounded contract for `risk-and-negative-effect-lift`.

Use it when the repository already has a stronger shadow-language contract inside `TECHNIQUE.md`, but the next question is how that caution language can act as a later KAG-oriented lift surface without pretending it is already machine-readable caution metadata.

This guide is caution-first. It does not add shadow fields or generated caution outputs.

See also:
- [Documentation Map](README.md)
- [Technique Shadow Guide](TECHNIQUE_SHADOW_GUIDE.md)
- [KAG Source Lift Guide](KAG_SOURCE_LIFT_GUIDE.md)
- [`risk-and-negative-effect-lift`](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md)

## Role Split

Keep the current caution surfaces distinct:

- `TECHNIQUE.md` `Risks` remains the primary caution source
- the shadow-language substructure already names:
  - `Failure modes`
  - `Negative effects`
  - `Misuse patterns`
  - `Detection signals`
  - `Mitigations`
- markdown remains authoritative for caution meaning, interpretation, and bounded review

That split is the current caution-layer contract.

## Current Lift Surface

The current repository already has enough structure to support bounded caution lookup by technique.

The first reusable technique surface for that bounded lift now lives in [`risk-and-negative-effect-lift`](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md).

Canonical bundles now also use one typed `notes/adverse-effects-review.md` supplement as a review-only caution watch surface over the same markdown-first contract.

That lift surface is useful for:

- inspecting how a technique fails
- inspecting what it worsens even when it appears to work
- spotting misuse and false-success patterns
- keeping early-stop and containment signals attached to the same bounded technique contract
- later section-level caution extraction without widening metadata first

This is a source-lift opportunity, not a reason to turn caution into a score or policy engine.

## What The Caution Layer Is Not

The current `Risks` surface should not be treated as:

- a new schema or frontmatter block
- a risk score
- a threat model
- machine-extracted policy
- a reason to widen validator behavior beyond enforcing the current markdown-first `Risks` contract

If a reviewer needs the actual meaning of a failure mode, hidden tradeoff, or mitigation boundary, the answer still lives in authored markdown.

## Explicitly Deferred

Still intentionally deferred:

- no shadow metadata fields
- no caution IDs
- no generated caution outputs

The current job is to keep the bounded caution layer explicit and enforced in markdown so later extraction work can build on it without reopening whether shadow meaning belongs in markdown or metadata. The reusable technique plus the canonical-only adverse-effects review note now capture that contract without implying that generated caution outputs or policy metadata have already landed.
