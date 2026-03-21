# Long-Gap Canon Design

This design-first doc captures the current long-gap promotion backlog after the hybrid canon completion program reopened the fast evidence paths.

Use it when the question is not "which promoted bundle can we close now?", but "which remaining promoted bundle needs a new external product surface before another honest canonical review makes sense?"

These are not fast-promotion candidates.
They need new live consumers or new authored source contracts outside `aoa-techniques`, not another wording-only pass inside this repository.

The first donor wave has now landed for all three targets.
What remains is not donor selection, but one more independent reinforcement beyond those first landed proofs.

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

### Landed donor evidence

- merged `ATM10-Agent@7cf55f70badbe8b1a51e2eabbe1424f35b833dd3` now records reusable `M6.19` rollout evidence across `open_quest_book`, `check_inventory_tool`, and `open_world_map`
- the landed donor keeps the checklist distinct from the base intent chain by naming one shared public `intent -> plan -> dry-run` contract plus checklist-complete rollout records

### Next external contract still needed

- one non-origin real new-intent rollout should now be documented as an authored checklist-driven change beyond `atm10-agent`
- the next rollout record should keep the checklist distinct from the base intent chain so `AOA-T-0005` does not collapse back into `AOA-T-0004`
- the donor surface should capture what changed in contracts, dry-run path, and validation, so the checklist stays the reusable object rather than a private implementation story in a second context
- current seeded external donors do not yet show an exact-fit open-source rollout record for this contract, so the open donor slot should stay explicit rather than being filled by a merely similar workflow repo

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

### Landed donor evidence

- merged `aoa-skills@b1b3fc7b330f2fecc5412c0444bc108b4aecc67c` now extends `docs/BRIDGE_SPEC.md` with one-source -> many-target fan-out proof and explicit drift-control commands
- the same donor change updates `skills/aoa-source-of-truth-check/SKILL.md` so one authoritative source staying aligned across multiple downstream consumer surfaces is now part of an authored runtime skill surface

### External OSS donor intake

- `ruler`: `pass` as the bounded origin donor and current external-intake anchor for this technique
- `agents-md`: `hold because overlap`; it reinforces fragment-first deterministic composition and generated `AGENTS.md` routing, but it sits too close to `AOA-T-0012` to count as a clean second proof for one-source -> many-target rule distribution
- `n-skills`: now landed as the adjacent [AOA-T-0024](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) import; its upstream mirroring with provenance and `.source.json` attribution remain useful, but they still do not match this bundle's exact live many-target contract closely enough to count as closure evidence here
- `agentic`: now landed as the adjacent [AOA-T-0025](../techniques/docs/capability-spec-versioning/TECHNIQUE.md) import; its versioned capability-contract pattern is useful as a neighboring docs import, but it still does not match this bundle's exact live one-source -> many-target rule-distribution contract closely enough to count as closure evidence here

### Next external contract still needed

- one more canonical rule source should distribute to multiple agent-facing instruction targets in a second repo or surface family, ideally `aoa-agents`
- the flow still has to be one-source -> many-target on committed authored surfaces, not one-source -> one-target or copy edits across several files
- the donor change should preserve source ownership, name the synchronized targets explicitly, and show how rule drift is prevented without turning every target into a hand-maintained source of truth
- external-intake-only reinforcement is no longer enough by itself; the next honest step must be another live managed multi-target context

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

### Landed donor evidence

- merged `aoa-skills@b1b3fc7b330f2fecc5412c0444bc108b4aecc67c` now gives `skills/aoa-sanitized-share/SKILL.md` the exact five-part caution split:
  - `Failure modes`
  - `Negative effects`
  - `Misuse patterns`
  - `Detection signals`
  - `Mitigations`
- the landed donor stays markdown-first and review-oriented, not generated policy, scoring, or metadata replacement for the skill bundle's meaning

### Next external contract still needed

- at least one more committed bundle or corpus should now adopt the same exact five-part caution split beyond the first `aoa-skills` donor
- the result must stay markdown-first and review-oriented, not generated policy, scoring, or metadata replacement for bundle meaning
- the donor surface should make the five-part caution split reusable as a public authored contract rather than as adjacent risk prose in only one skill
- current seeded external donors do not yet show an exact-fit second corpus for this five-part contract, so the open donor slot should remain explicit

### Shortcuts to reject

- treating `aoa-evals` `Failure modes` plus `Blind spots` as if they were the same contract
- treating `aoa-skills` review-path metadata as caution proof
- adding generated caution outputs before the authored five-part contract exists in another corpus

## Recommended Future Waves

Open a future external evidence wave only after one of these paths is ready:

1. `AOA-T-0005`: a non-origin public-safe new-intent rollout record exists beyond `atm10-agent`
2. `AOA-T-0013`: a second instruction-heavy repo such as `aoa-agents` lands one-source -> many-target distribution with explicit drift control; `ruler` now stays the bounded origin donor, not the missing live reinforcement
3. `AOA-T-0022`: a second committed corpus lands the exact five-part caution contract beyond the first `aoa-skills` donor

Until then, these techniques should remain explicitly bounded `promoted` techniques rather than being pushed toward canonical by wording alone.
