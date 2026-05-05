# External Import Review

## Technique
- id: AOA-T-0029
- name: nested-rule-loading

## Verdict
- pass
- review date: 2026-03-21

## Evidence summary

- the bundle includes the expected bounded external-import package: `TECHNIQUE.md`, `notes/external-origin.md`, `notes/second-context-adaptation.md`, one checklist, and two public-safe examples
- the technique document states one narrow contract: hierarchical rule layers load with explicit precedence and one-way source ownership
- the provenance note records the donor source plus explicit exclusions around MCP propagation, skills propagation, installer breadth, and broader product-width behavior
- the second-context note shows the same contract surviving as a documentation-first adaptation inside `aoa-techniques`

## Boundedness check

- result: pass
- the invariant core stays narrow: canonical parent ownership, subordinate nested layers, explicit precedence, and repeatable resolution
- excluded donor features remain explicit and out of scope: MCP propagation, skills propagation, nested-output breadth, installer behavior, and broader orchestration detail
- the examples reinforce hierarchical loading plus explicit precedence without widening the bundle into a distribution or registry system

## Provenance readability

- result: pass
- a reviewer can trace the path from donor repository to public technique through the external-origin note, bounded exclusions, and documentation-first adaptation without hidden internal context
- the bundle reads as one reusable docs pattern rather than a disguised runtime or role contract
- the current import path is public-safe and reviewable at the present repo scale

## Import-path assessment

- result: pass
- this is a successful bounded external import and the bundle is strong enough to enter the corpus as a `promoted` technique
- the import path is strong enough for initial publication, but not strong enough to justify canonical default status without another live reuse context

## Remaining gaps

- the smallest remaining gap is still one live second context beyond the donor and documentation-first adaptation
- this new adjacent import does not count as live closure evidence for `AOA-T-0013`, because nested hierarchical loading is a different contract from one-source-to-many-target instruction distribution

## Recommendation

- accept `AOA-T-0029` as a bounded external import and publish it as `promoted`
- defer any canonical review until another live adopter confirms that hierarchical rule loading survives outside the donor repository
