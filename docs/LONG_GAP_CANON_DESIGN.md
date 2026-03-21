# Long-Gap Canon Design

This design-first doc captures the current long-gap promotion backlog after the hybrid canon completion program reopened the fast evidence paths.

Use it when the question is not "which promoted bundle can we close now?", but "which remaining promoted bundle needs a new external product surface before another honest canonical review makes sense?"

These are not fast-promotion candidates.
They need new live consumers or new authored source contracts outside `aoa-techniques`, not another wording-only pass inside this repository.

## Scope

This design wave covers:

- [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md)
- [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md)
- [AOA-T-0022](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md)

It does not reopen [AOA-T-0018](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) or [AOA-T-0020](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md), because those remain evidence-prep questions rather than long-gap design problems.

## `AOA-T-0005` - New Intent Rollout Checklist

### Natural donor repo

- primary donor: `atm10-agent`

### Why this donor fits

- the live intent -> plan -> dry-run chain still exists there
- the repo already has explicit rollout milestones and real new-intent evolution history
- the missing proof is a second real rollout adopter, not another public-safe adaptation sketch

### Exact external contract needed

- one more real new-intent rollout should be documented as an authored checklist-driven change, not just implied by a finished feature
- the rollout record should keep the checklist distinct from the base intent chain so `AOA-T-0005` does not collapse back into `AOA-T-0004`
- the donor surface should capture what changed in contracts, dry-run path, and validation, so the checklist stays the reusable object rather than a private implementation story

### Shortcuts to reject

- another repo-local sketch inside `aoa-techniques`
- broad change-protocol evidence that never shows a new intent being added
- private rollout notes that cannot be cited as public reusable evidence

## `AOA-T-0013` - Single-Source Rule Distribution

### Natural donor repos

- first donor: `aoa-skills`
- second donor after that: `aoa-agents`

### Why these donors fit

- `aoa-skills` already has one-source technique meaning, multiple agent-facing `skills/*/agents/openai.yaml` targets, and schema-backed validation
- `aoa-agents` is the semantic home for later role-surface or handoff-rule distribution, but it is still too bootstrap-shaped to be the first proof source

### Exact external contract needed

- one canonical rule source should distribute to multiple agent-facing instruction targets with explicit generated or validator-backed drift control
- the flow has to be one-source -> many-target on committed authored surfaces, not one-source -> one-target or copy edits across several files
- the donor change should preserve source ownership, name the generated or synchronized targets explicitly, and show how rule drift is prevented without turning every target into a hand-maintained source of truth

### Shortcuts to reject

- another adaptation-only note in `aoa-techniques`
- a single-target sync path that never proves many-target distribution
- hand-edited copied rule blocks without validator-backed or generated parity

## `AOA-T-0022` - Risk And Negative-Effect Lift

### Natural donor repo

- primary donor: `aoa-skills`

### Why this donor fits

- skills already require authored caution language and publish a stable `Risks and anti-patterns` section
- that section is already lifted into source-owned section surfaces, so the repo is structurally closest to the needed markdown-first caution contract
- the missing proof is not generic caution language, but the exact five-part `Risks` split

### Exact external contract needed

- at least one skill bundle should adopt the exact five-part caution split or an authored companion note with the same five parts:
  - `Failure modes`
  - `Negative effects`
  - `Misuse patterns`
  - `Detection signals`
  - `Mitigations`
- the result must stay markdown-first and review-oriented, not generated policy, scoring, or metadata replacement for the skill bundle's meaning
- the donor surface should make the five-part caution split reusable as a public authored contract rather than as adjacent risk prose

### Shortcuts to reject

- treating `aoa-evals` `Failure modes` plus `Blind spots` as if they were the same contract
- treating `aoa-skills` review-path metadata as caution proof
- adding generated caution outputs before the authored five-part contract exists in another corpus

## Recommended Future Waves

Open a future external evidence wave only after one of these paths is ready:

1. `AOA-T-0005`: a second public-safe new-intent rollout record exists in `atm10-agent`
2. `AOA-T-0013`: `aoa-skills` lands a validator-backed one-source -> many-target instruction distribution flow
3. `AOA-T-0022`: `aoa-skills` lands the exact five-part caution contract on a committed authored bundle

Until then, these techniques should remain explicitly bounded `promoted` techniques rather than being pushed toward canonical by wording alone.
