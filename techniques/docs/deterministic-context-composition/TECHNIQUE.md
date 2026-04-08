---
id: AOA-T-0012
name: deterministic-context-composition
domain: docs
kind: composition
status: canonical
origin:
  project: agents-md
  path: README.md
  note: Adapted from the open-source agents-md project, which composes generated agent-context files from markdown fragments with deterministic ordering and source annotations.
owners:
  - 8Dionysus
tags:
  - docs
  - agent-context
  - composition
  - traceability
  - generated-artifact
summary: Compose agent context from smaller fragments into a stable generated artifact with deterministic ordering and source traceability.
maturity_score: 4
rigor_level: bounded
reversibility: moderate
review_required: true
validation_strength: cross_context
public_safety_reviewed_at: 2026-03-15
export_ready: true
relations: []
evidence:
  - kind: external_review
    path: notes/external-import-review.md
  - kind: external_origin
    path: notes/external-origin.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
  - kind: adverse_effects_review
    path: notes/adverse-effects-review.md
---

# deterministic-context-composition

## Intent

Keep agent context scalable by composing it from smaller source fragments into a stable generated artifact whose ordering and source boundaries remain explicit.

## When to use

- repositories where one hand-written `AGENTS.md` no longer scales
- projects that want fragment-first authoring with one generated context surface
- teams that need deterministic ordering rather than manual copy-paste merges
- agent documentation flows where source traceability matters during review

## When not to use

- very small repositories where one short hand-maintained context file is enough
- systems that depend on runtime code execution or network lookups during composition
- workflows where generated outputs cannot be regenerated reliably from source fragments

## Inputs

- source fragments that hold the real context content
- deterministic ordering rules such as priority plus stable path fallback
- one target artifact path such as `AGENTS.md`
- explicit source-traceability strategy such as annotations or equivalent metadata

## Outputs

- generated context artifact
- repeatable composition order
- explicit traceability from output back to source fragments
- reviewable fragment set that remains the source of truth

## Core procedure

1. Keep agent context in smaller source fragments instead of hand-editing one large generated file.
2. Define how fragments route to the target artifact and how composition order is resolved.
3. Compose fragments with deterministic ordering, usually explicit priority first and stable path order second.
4. Preserve traceability by annotating or otherwise recording which fragment produced each output section.
5. Regenerate the target artifact from fragments whenever sources change.
6. Review and edit the fragment set, not the generated artifact, as the canonical source of truth.

## Contracts

- source fragments remain the canonical editable inputs
- the output artifact is generated and should not become the hand-edited source of truth
- the same fragment set and ordering rules produce the same output ordering
- the output stays traceable back to source fragments
- composition does not require runtime code execution or network access to explain the core pattern

## Risks

### Failure modes

- ordering and priority rules become implicit, so the generated artifact changes in ways contributors cannot predict from the fragment set alone
- contributors edit the generated artifact directly and break the fragment-first source-of-truth contract
- source annotations or equivalent metadata erode until output sections can no longer be traced back to the fragments that produced them
- the output remains stable and deterministic at a glance, but only a small set of maintainers can still explain why that precedence order exists

### Negative effects

- deterministic composition can add hidden review overhead when maintainers must mentally reconstruct precedence instead of reading one obvious source path
- fragment-first authoring can make context feel cleaner while actually making routing and responsibility harder for new contributors to understand
- a generated artifact can create false-success by looking stable and ordered even when only a small set of maintainers can explain why it rendered that way
- once the output looks authoritative, teams can postpone simplifying precedence because determinism itself starts to masquerade as clarity

### Misuse patterns

- widening the technique into a general documentation build system instead of keeping it bounded to many fragments composing into one generated context artifact
- adding more precedence rules, fallback layers, or special-case routing instead of simplifying composition order
- treating traceability annotations as optional decoration rather than part of the bounded review contract
- using the stable output as a reason to drift toward multi-target management or propagation behavior that belongs in a different technique

### Detection signals

- reviewers cannot explain output ordering without consulting tribal knowledge or implementation details outside the fragment set
- generated artifact edits appear in normal maintenance diffs instead of source-fragment changes driving regeneration
- contributors know the output changed, but cannot quickly identify which fragment or precedence rule caused the change
- the output still looks deterministic, but repeated review comments reveal confusion about fragment authority, ordering, or ownership boundaries
- maintainers defend the current ordering because it is stable, but cannot explain why the next contributor should prefer that precedence over a simpler one

### Mitigations

- simplify the ordering contract so precedence is explainable from the fragment set and one small set of deterministic rules
- reassert fragment-first authority by rejecting direct edits to the generated artifact and routing fixes back to canonical fragments
- restore explicit traceability from output sections to source fragments before adding more composition features or target variants
- narrow the technique back to one generated context surface when additional routing rules start making source-of-truth boundaries opaque
- stop the expansion when the next requested improvement really needs multi-target propagation or another technique family rather than one-output composition

## Validation

Verify the technique by confirming that:
- the generated artifact can be recreated from source fragments without manual merge steps
- higher-priority fragments surface earlier and stable fallback ordering is predictable
- output sections can be traced back to source fragments
- removing or changing one fragment updates the generated artifact in a predictable way
- contributors can identify the source of truth without ambiguity

See `checks/deterministic-context-composition-checklist.md`.
For external provenance, second-context adaptation, the first import-review outcome, and canonical-readiness review, see `notes/external-origin.md`, `notes/second-context-adaptation.md`, `notes/external-import-review.md`, and `notes/canonical-readiness.md`.

## Adaptation notes

What can vary across projects:
- fragment discovery rules
- whether the target artifact is `AGENTS.md` or another generated context file
- routing behavior such as root-only or nearest-target composition
- annotation syntax or companion metadata used for source traceability

Project-shaped details that should not be treated as invariant:
- exact CLI commands such as `npx agents-md compose`
- runtime or package-manager assumptions such as Bun, Node, or `npx`
- report, watch, truncate, size-limit, and migration features around the composition core
- exact source filename patterns such as `*.agents.md`

What should stay invariant:
- context is authored in smaller fragments
- composition order is deterministic
- the generated context artifact is derived rather than hand-maintained
- output remains traceable back to sources

## Public sanitization notes

This imported technique narrows the donor repository to one bounded pattern: deterministic composition from fragments into a stable generated context artifact. CLI packaging details, token-estimate reporting, watch mode, migration helpers, and other product-shaped features were intentionally left out.

## Example

See `examples/minimal-deterministic-context-composition.md` for the smallest bounded composition flow and `examples/concrete-skill-doc-composition.md` for a public-safe `AGENTS.md`-style composition example with deterministic ordering and explicit source annotations.

## Checks

See `checks/deterministic-context-composition-checklist.md`.

## Promotion history

- adapted from open-source `agents-md`
- imported into `aoa-techniques` on 2026-03-14 as the first external-import pilot with explicit provenance and bounded adaptation review
- passed first external-import review on 2026-03-15; keep the technique `promoted` while preparing second-donor evaluation rather than widening this bundle
- approved for `canonical` in `aoa-techniques` on 2026-03-18 after explicit canonical-readiness review, clear instruction-surface boundary review, and stronger public example coverage

## Future evolution

- split out a broader `fragmented-agent-context` sibling technique if context partitioning deserves its own canonical surface
- add a follow-on technique for reporting or CI checks over generated context outputs
- capture a second external adaptation context beyond a documentation-first repository
