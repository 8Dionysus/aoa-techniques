# Technique Shadow Guide

This guide defines the first markdown-first contract for `technique shadow discipline`.

Use it when a technique already has intent, contracts, and validation, but its `Risks` section is still too vague to explain how the technique can quietly make a system worse.

This guide is review-first. It does not add schema fields or machine-readable shadow metadata.

See also:
- [Start Here](START_HERE.md)
- [SHADOW_PATTERNS.md](SHADOW_PATTERNS.md)
- [`../generated/shadow_review_manifest.json`](../generated/shadow_review_manifest.json)
- [Documentation Map](README.md)
- [Risk And Negative-Effect Lift Guide](RISK_AND_NEGATIVE_EFFECT_LIFT_GUIDE.md)
- [`risk-and-negative-effect-lift`](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md)

This family uses one stable shape:

- authoritative source: authored `Risks` sections plus canonical-only `notes/adverse-effects-review.md` where needed
- reader companion: `SHADOW_PATTERNS.md`
- derived manifest: `generated/shadow_review_manifest.json`
- what it must not become: generated caution policy, scoring, or machine-readable shadow metadata

## Why `Risks` Alone Is Too Weak

A flat `Risks` list often mixes together very different problems:

- how the technique breaks
- what the technique worsens even when it "works"
- how people start using it outside its bounded role
- how the technique creates false confidence before an actual failure is obvious

That makes review weaker. A stronger technique should describe not only what it improves, but also the shape of its shadow.

## Shadow Vocabulary

Use these distinctions inside `## Risks`:

| section | question it answers |
|---|---|
| `Failure modes` | How does the technique break or stop holding its contract? |
| `Negative effects` | What does the technique worsen even in a nominally working path? |
| `Misuse patterns` | Where will teams over-apply or misapply the technique? |
| `Detection signals` | How do we tell that drift, harm, or false-success has started? |
| `Mitigations` | How do we contain, roll back, or narrow the damage? |

Keep the language bounded. This is not a request for a long threat-model essay.

## Review Prompts

When reviewing a technique's shadow, ask:

- What does this technique make better?
- What does it make worse?
- What does it hide?
- Where can it create false-success or false confidence?
- What does its "successful failure" look like?
- What early signals show that it should be stopped?
- When should the technique be banned for a bounded context instead of patched again?

These prompts are especially important when the technique affects defaults, summaries, memory, rules, or operator-facing review surfaces.

## Current Authoring Shape

The current repository now requires the top-level `## Risks` section to stay structured like this:

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

This is the current markdown-first authoring contract across the published corpus. It strengthens review language without changing frontmatter or introducing machine-readable shadow fields.

The same shadow-language contract is also the current upstream for bounded caution/source-lift work. The first reusable implementation surface for that lift now lives in [`risk-and-negative-effect-lift`](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md), and canonical bundles now pair it with one typed `notes/adverse-effects-review.md` supplement when the repo needs a bounded shadow watch surface beyond the main `Risks` section.

## Explicitly Deferred

Still intentionally deferred:

- no new schema or frontmatter fields for shadow metadata
- no validator mode for scoring technique shadow quality
- no generated caution outputs or caution IDs

The current canonical adverse-effects review note is a bounded supplement over authored `Risks`, not a replacement source or a policy/scoring program.
