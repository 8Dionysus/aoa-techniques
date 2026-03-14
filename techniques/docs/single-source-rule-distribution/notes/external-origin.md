# External Origin Note

Use this note when a technique is adapted from an external open-source source.
It complements `TECHNIQUE.md` and records provenance, adaptation boundaries, and public-safety review.

## Source

- source_repo: `https://github.com/intellectronica/ruler`
- source_license: MIT
- inspired_by: not used in this import
- adapted_from: `ruler` single-source instruction model where one canonical rule directory is applied to multiple agent-facing instruction files

## What changed

- what_changed: narrowed the donor repository to one bounded docs pattern: one canonical rule source distributed to multiple agent-facing instruction surfaces
- invariant core kept: one canonical rule source, repeatable propagation to multiple targets, managed target files, and anti-duplication behavior on re-apply
- project-shaped details removed or generalized: exact supported-agent matrix, CLI flags, Node/npm assumptions, nested loading as a core contract, MCP propagation, skills propagation, `.gitignore` automation, and backup/revert behavior

## Public-safety review

- secrets or tokens removed: none from the donor surface used for this import
- private paths, URLs, or IDs removed: donor-specific local paths, environment conventions, and generated target layouts were generalized away
- environment-specific assumptions generalized: the public technique does not depend on `npm`, `npx`, or a particular local runtime even though the donor repository ships a Node-based CLI
- remaining public-safety concerns: the main risk is scope creep rather than security leakage; later sibling techniques should review nested loading, MCP propagation, or skills propagation separately instead of widening this bundle

## Review notes

- why this adaptation is reusable here: repositories that support multiple coding agents often need shared guidance to reach several instruction surfaces without making each target file canonical
- primary evidence used: `README.md` in `ruler` defines the single-source-to-many-target contract, and `tests/mixed-agents-duplication.test.ts` shows repeated application without duplicating shared instructions
- limits or follow-up review concerns: this first draft intentionally ignores beta-preview product breadth and keeps the technique at the `docs` layer only
