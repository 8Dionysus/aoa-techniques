# External Origin Note

Use this note when a technique is adapted from an external open-source source.
It complements `TECHNIQUE.md` and records provenance, adaptation boundaries, and public-safety review.

## Source

- source_repo: `https://github.com/ivawzh/agents-md`
- source_license: MIT
- inspired_by: not used in this import
- adapted_from: `agents-md` fragment-first context authoring model where smaller markdown sources stay primary before any later generated aggregate is produced

## What changed

- what_changed: narrowed the donor repository to one bounded pattern: keep agent context in smaller bounded fragments before deterministic assembly
- invariant core kept: fragment-first authoring, bounded fragment scope, locally legible ownership, and separation between canonical fragments and any later aggregate artifact
- project-shaped details removed or generalized: exact fragment file patterns, deterministic composition behavior, JSON reports, token-estimate reporting, migration helpers, and runtime injection behavior

## Public-safety review

- secrets or tokens removed: none from the donor surface used for this import
- private paths, URLs, or IDs removed: donor-specific local paths and filename conventions were generalized away
- environment-specific assumptions generalized: the public technique does not depend on one generator, one CLI, or one CI stack
- remaining public-safety concerns: the main risk is scope creep; future siblings should treat deterministic composition, CI reporting, and runtime injection separately instead of widening this bundle

## Review notes

- why this adaptation is reusable here: many repositories need context source partitioning before they need a generated aggregate, and fragment-first authoring is reusable independent of the donor toolchain
- primary evidence used: the donor README and public feature surface both center smaller markdown fragments as the authoring layer that scales better than one large manual context file
- limits or follow-up review concerns: this first import intentionally stops before deterministic assembly and CI reporting so the bundle stays source-layer only
