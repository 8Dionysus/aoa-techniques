# External Origin Note

Use this note when a technique is adapted from an external open-source source.
It complements `TECHNIQUE.md` and records provenance, adaptation boundaries, and public-safety review.

## Source

- source_repo: `https://github.com/intellectronica/ruler`
- source_license: MIT
- inspired_by: not used in this import
- adapted_from: `ruler` nested rule loading behavior where layered rule sets can be loaded with explicit precedence while keeping ownership one-way

## What changed

- what_changed: reduced the donor package to one bounded pattern: hierarchical rule layers loaded with explicit precedence and one-way source ownership
- invariant core kept: canonical parent ownership, nested subordinate layers, explicit precedence, and repeatable resolution
- project-shaped details removed or generalized: MCP propagation, skills propagation, installer breadth, `.gitignore` automation, backup/revert behavior, and other donor features outside the nested-loading contract

## Public-safety review

- secrets or tokens removed: none from the donor surface used for this import
- private paths, URLs, or IDs removed: donor-specific local paths and environment conventions were generalized away
- environment-specific assumptions generalized: the public technique does not depend on the donor CLI packaging even though the donor repository ships a broader loader
- remaining public-safety concerns: the main risk is scope creep, especially if nested loading drifts toward multi-target distribution or product-width orchestration

## Review notes

- why this adaptation is reusable here: some repositories need layered rule files with a readable precedence order, not just one flat instruction file
- primary evidence used: the public `ruler` source describes hierarchical rule loading as a bounded part of a broader rule system, and the layered contract can be separated from the rest of the product breadth
- limits or follow-up review concerns: nested loading should stay distinct from multi-target propagation, and broader features such as MCP or skills propagation should remain separate sibling-technique candidates
