---
id: AOA-T-0012
name: deterministic-context-composition
domain: docs
status: promoted
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

- hidden priority rules can make composition feel deterministic only to maintainers who already know the ordering logic
- contributors may edit the generated artifact directly and break the fragment-first contract
- traceability can erode if source annotations or equivalent metadata are removed without replacement

## Validation

Verify the technique by confirming that:
- the generated artifact can be recreated from source fragments without manual merge steps
- higher-priority fragments surface earlier and stable fallback ordering is predictable
- output sections can be traced back to source fragments
- removing or changing one fragment updates the generated artifact in a predictable way
- contributors can identify the source of truth without ambiguity

See `checks/deterministic-context-composition-checklist.md`.
For external provenance and second-context adaptation, see `notes/external-origin.md` and `notes/second-context-adaptation.md`.

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

See `examples/minimal-deterministic-context-composition.md`.

## Checks

See `checks/deterministic-context-composition-checklist.md`.

## Promotion history

- adapted from open-source `agents-md`
- imported into `aoa-techniques` on 2026-03-14 as the first external-import pilot with explicit provenance and bounded adaptation review

## Future evolution

- split out a broader `fragmented-agent-context` sibling technique if context partitioning deserves its own canonical surface
- add a follow-on technique for reporting or CI checks over generated context outputs
- capture a second external adaptation context beyond a documentation-first repository
