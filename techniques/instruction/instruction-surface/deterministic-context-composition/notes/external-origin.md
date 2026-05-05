# External Origin Note

Use this note when a technique is adapted from an external open-source source.
It complements `TECHNIQUE.md` and records provenance, adaptation boundaries, and public-safety review.

## Source

- source_repo: `https://github.com/ivawzh/agents-md`
- source_license: MIT
- inspired_by: not used in this import
- adapted_from: `agents-md` composition model for generated `AGENTS.md` files built from markdown fragments with deterministic ordering and source annotations

## What changed

- what_changed: narrowed the donor repository to one bounded pattern: deterministic composition from fragments into a stable generated context artifact
- invariant core kept: fragment-first authoring, deterministic ordering, generated output, and explicit source traceability
- project-shaped details removed or generalized: CLI commands, package-manager assumptions, report and token-estimate features, watch mode, migration helpers, and exact filename conventions

## Public-safety review

- secrets or tokens removed: none from the donor surface used for this import
- private paths, URLs, or IDs removed: donor-specific local paths and operational assumptions were generalized away
- environment-specific assumptions generalized: Bun, `npx`, and repo-specific command flows were removed from the core technique contract
- remaining public-safety concerns: later follow-on techniques should review reporting, migration, or automation layers separately rather than treating them as part of this bounded import

## Review notes

- why this adaptation is reusable here: many agent-oriented repositories need a stable generated context surface without collapsing everything into one manually maintained file
- limits or follow-up review concerns: this first external-import pilot intentionally excludes CI reporting, token accounting, and migration helpers so provenance readability and bounded adaptation stay clear
