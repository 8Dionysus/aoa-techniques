---
id: AOA-T-0022
name: risk-and-negative-effect-lift
domain: docs
kind: lift
status: promoted
origin:
  project: aoa-techniques
  path: docs/RISK_AND_NEGATIVE_EFFECT_LIFT_GUIDE.md
  note: Extracted from the current shadow guides, validator-enforced Risks contract, and live corpus to keep caution lookup bounded and markdown-first while staying subordinate to authored Risks and canonical adverse-effects review.
owners:
  - 8Dionysus
tags:
  - docs
  - shadow
  - caution
  - risks
  - source-lift
summary: Lift richer `Risks` language into bounded caution-oriented lookup and reuse without turning caution into metadata, scoring, or generated policy.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-19
export_ready: true
relations:
  - type: complements
    target: AOA-T-0018
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# risk-and-negative-effect-lift

## Intent

Lift richer `Risks` language into bounded caution-oriented lookup and reuse so reviewers and later derived surfaces can find failure, harm, misuse, detection, and mitigation signals without turning caution into metadata, scoring, generated policy, or a new source of truth.

## When to use

- repositories where `TECHNIQUE.md` already uses the fixed five-part `Risks` shape
- review or reuse flows that need to inspect how a technique can fail, mislead, or quietly make a system worse
- markdown-first source-lift work that wants bounded caution lookup without widening schema
- cases where caution should stay attached to the technique bundle instead of becoming a separate policy program
- corpus-level review paths where a canonical adverse-effects review note can supplement the same markdown-first caution source without replacing it

## When not to use

- systems that need a threat model, incident taxonomy, or policy-scoring framework rather than bounded technique caution
- repos that do not yet have stable `Failure modes`, `Negative effects`, `Misuse patterns`, `Detection signals`, and `Mitigations` language in markdown
- workflows that want shadow metadata, caution IDs, generated caution outputs, or a new `kag` domain
- workflows that expect the lifted caution surface to become authoritative over the bundle's authored `Risks`
- cases where reviewers would treat a lifted caution view as more authoritative than the underlying `TECHNIQUE.md`

## Inputs

- one authoritative `TECHNIQUE.md` bundle with a richer `## Risks` section
- a bounded caution question such as failure review, misuse review, or early-stop review
- a human or generated reader surface that can point back to the source markdown
- explicit agreement that caution meaning still lives in authored markdown

## Outputs

- bounded caution lookup by technique
- clearer review access to the five shadow-language distinctions
- preserved markdown authority over caution meaning
- reusable source-lift pattern for later derived consumers that still stay bounded
- canonical-only adverse-effects review notes when one repo needs a separate caution watch surface for its default techniques
- no generated caution policy layer, scoring surface, or metadata-only replacement for `Risks`

## Core procedure

1. Keep authored `## Risks` as the primary caution source for the bundle.
2. Preserve the fixed five-part split between `Failure modes`, `Negative effects`, `Misuse patterns`, `Detection signals`, and `Mitigations`.
3. Use those subsection names for bounded caution lookup, review prompts, or later derived read surfaces.
4. Route interpretation and policy judgment back to the full markdown section when meaning matters.
5. Keep any derived caution usage rebuildable from the markdown bundle rather than hand-maintained elsewhere.
6. Stop and narrow the request if the next step starts asking for shadow metadata, scoring, or generated caution outputs.
7. Treat any canonical adverse-effects review note as a supplement to `Risks`, not as a new policy source.

## Contracts

- `TECHNIQUE.md` `Risks` remains the primary caution source
- the five shadow-language distinctions stay explicit and bounded
- caution lift stays derived and source-lift oriented rather than metadata-first
- the technique does not require shadow metadata, caution IDs, generated caution outputs, or a new `kag` domain
- no new source of truth is introduced beyond markdown bundles and derived artifacts
- any canonical-only adverse-effects review note remains a supplement over the same markdown-first caution source
- the technique does not turn caution into scoring, generated policy, or a metadata replacement for `Risks`

## Risks

### Failure modes

- reviewers can mistake the presence of five caution subsections for proof that the technique's shadow is already fully understood
- a bounded caution view can drift into a pseudo-schema if teams start optimizing the lifted representation instead of the markdown source
- the technique can fail if later consumers treat caution lookup as a permission to skip the rest of the bundle contract

### Negative effects

- richer caution language can make techniques feel heavier to author even when only a small bounded warning set is needed
- a reusable lift pattern can attract premature requests for scoring, policy, or machine-readable caution metadata
- caution lookup can over-focus readers on risk language and hide the need to re-check intent, contracts, or validation around it

### Misuse patterns

- treating the technique as a reason to add shadow metadata, caution IDs, or generated caution outputs now
- using the five caution labels as a generic policy template instead of as bounded markdown review language
- widening the pattern into a new domain or graph program because later KAG work exists elsewhere in the repo

### Detection signals

- contributors propose caution fields in frontmatter or new generated caution artifacts instead of improving `TECHNIQUE.md`
- a review request asks for scores, enforcement tiers, or policy routing rather than bounded lookup into authored caution language
- the lifted caution usage no longer points readers back to the source markdown
- the same caution question cannot be answered without inventing metadata that the current markdown-first contract never claimed to provide

### Mitigations

- keep the five-part caution split tied to authored markdown and rebuild any derived use from that source
- reject requests that would turn caution into scoring, IDs, or policy metadata in this wave
- route deeper interpretation back to the full technique bundle and its validation context
- open a later wave only when markdown-first caution lookup clearly stops being enough

## Validation

Verify the technique by confirming that:
- the source bundle keeps `Failure modes`, `Negative effects`, `Misuse patterns`, `Detection signals`, and `Mitigations` inside `## Risks`
- caution lookup still routes back to the authored markdown section
- no shadow metadata, caution IDs, generated caution outputs, or new domain were required
- the caution lift remains bounded to technique-level review and reuse questions
- the source bundle stays authoritative even when a derived caution-oriented read surface exists

See `checks/caution-lift-checklist.md` and `examples/minimal-risk-and-negative-effect-lift.md`.
For repo-grounded origin evidence, see `notes/origin-evidence.md`.

## Adaptation notes

What can vary across projects:
- which technique families most need explicit caution lookup
- whether the bounded consumer is a review checklist, retrieval layer, or another reader-facing aid
- how much prose each caution subsection needs
- which downstream source-lift surfaces later point readers back to `Risks`

What should stay invariant:
- markdown stays authoritative
- the five caution distinctions remain explicit
- caution lift stays bounded and review-shaped
- the pattern does not turn into a machine-readable caution program

This technique is a markdown-first lift over existing `Risks`, not a new shadow platform. A canonical-only adverse-effects review note can supplement the same contract for already-canonical bundles, but generated caution outputs, policy scoring, and metadata layers remain deferred.

## Public sanitization notes

This public version keeps the reusable caution-lift contract while stripping repo-local implementation trivia and any suggestion that a scoring or policy engine already exists. It is not a generated caution-output contract, not a metadata program, and not a new domain.

## Example

See `examples/minimal-risk-and-negative-effect-lift.md`.

## Checks

See `checks/caution-lift-checklist.md`.

## Promotion history

- shaped inside `aoa-techniques` while the repo's richer `Risks` contract, shadow guides, and validator enforcement converged into a stable markdown-first caution layer
- extracted into first public reusable form on 2026-03-19 as the first bounded shadow/caution technique in the existing `docs` domain

## Future evolution

- strengthen second-context evidence once another markdown-first corpus reuses the same bounded caution-lift split
- clarify when the existing canonical adverse-effects review supplement is enough and when a corpus should still stay with `Risks` alone
- keep caution lookup bounded to review and reuse questions rather than letting it become a policy or scoring surface
- keep shadow metadata, generated caution outputs, and scoring layers deferred unless bounded caution lookup stops being enough
