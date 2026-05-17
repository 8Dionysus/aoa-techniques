# Technique Shadow Guide

This guide defines the markdown-first contract for `technique shadow discipline`.

Use it when a technique has intent, contracts, and validation, but its `Risks`
section is too vague to explain how the technique can quietly make a system
worse.

This guide is review-first. It keeps caution meaning in authored markdown.

See also:
- [Start Here](../START_HERE.md)
- [SHADOW_PATTERNS.md](../readers/review/SHADOW_PATTERNS.md)
- [`../../generated/shadow_review_manifest.json`](../../generated/shadow_review_manifest.json)
- [Documentation Map](../README.md)
- [Risk And Negative-Effect Lift Guide](../source-lift/RISK_AND_NEGATIVE_EFFECT_LIFT_GUIDE.md)
- [`risk-and-negative-effect-lift`](../../techniques/knowledge-lift/kag-source-lift/risk-and-negative-effect-lift/TECHNIQUE.md)

Stable shape:

| Role | Surface |
|---|---|
| authoritative source | authored `Risks` sections plus canonical-only `notes/adverse-effects-review.md` where needed |
| reader companion | `docs/readers/review/SHADOW_PATTERNS.md` |
| derived manifest | `generated/shadow_review_manifest.json` |
| must not become | generated caution policy, scoring, or machine-readable shadow metadata |

## Why `Risks` Alone Is Too Weak

A flat `Risks` list often mixes breakage, negative effects, misuse, and false
confidence. That makes review weaker because a technique can appear to work
while quietly degrading meaning, safety, or operator judgment.

Shadow discipline asks what the technique improves, what it worsens, what it
hides, where false-success appears, and which early signal should stop or narrow
the move.

## Shadow Vocabulary

Use these distinctions inside `## Risks`:

| Section | Question it answers |
|---|---|
| `Failure modes` | How does the technique break or stop holding its contract? |
| `Negative effects` | What does the technique worsen even when it appears to work? |
| `Misuse patterns` | Where will teams over-apply or misapply it? |
| `Detection signals` | How do we tell that drift, harm, or false-success has started? |
| `Mitigations` | How do we contain, roll back, or narrow damage before false-success hardens? |

Keep the language bounded. This is not a request for a long threat-model essay.

## Review Prompts

When reviewing shadow language, ask:

- What does this technique make better?
- What does it make worse or hide?
- What does its successful failure look like?
- What early signal says it should stop?
- What first containment or rollback move narrows the damage?
- When should the technique be banned for this bounded context instead of
  patched again?

These prompts matter most when the technique affects defaults, summaries,
memory, rules, or operator-facing review surfaces.

## Minimum Useful Specificity

Good shadow language makes three things reviewable:

1. one plausible successful failure
2. one early stop or watch signal
3. one first containment, rollback, or narrowing move

If a `Risks` section sounds safe only because it is vague, rewrite it until a
reviewer can see the deceptive success path and the first containment move.

## Current Authoring Shape

The current repository now requires the top-level `## Risks` section to stay
structured like this:

```md
## Risks

### Failure modes
- how the contract can break

### Negative effects
- what the technique worsens even when it appears to work

### Misuse patterns
- how the technique gets applied outside its bounded role

### Detection signals
- what early signals show drift or false-success

### Mitigations
- how to narrow, roll back, or contain the damage
```

This is the markdown-first authoring contract across the published corpus. It
strengthens review language without changing frontmatter or introducing
machine-readable shadow fields.

## Choosing The Right Shadow Surface

Use the smallest surface that makes the caution question reviewable:

| Need | Surface |
|---|---|
| Vague bundle-level caution | sharpen the bundle's authored `## Risks` |
| One canonical technique needs a tighter watch seam | add one canonical `notes/adverse-effects-review.md` |
| Several canonical techniques share one caution-dense seam | open a bounded repo-level shadow-review doc |
| Machine-readable lookup of current shadow seams | use [SHADOW_PATTERNS.md](../readers/review/SHADOW_PATTERNS.md) and `shadow_review_manifest.json` as derived companions |

More notes alone do not justify another repo-level shadow family.

## Explicitly Deferred

Still intentionally deferred:

- no new schema or frontmatter fields for shadow metadata
- no validator mode for scoring technique shadow quality
- no generated caution outputs or caution IDs

The current canonical adverse-effects review note is a bounded supplement over
authored `Risks`, not a replacement source or a policy/scoring program.
