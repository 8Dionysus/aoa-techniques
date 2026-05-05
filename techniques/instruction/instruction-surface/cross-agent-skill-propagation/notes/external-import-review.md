# External Import Review

## Technique
- id: AOA-T-0027
- name: cross-agent-skill-propagation

## Verdict
- pass
- review date: 2026-03-21

## Evidence summary

- the bundle includes the expected bounded external-import package: `TECHNIQUE.md`, `notes/external-origin.md`, `notes/second-context-adaptation.md`, one public-safe checklist, and two public-safe examples
- the technique document states one narrow contract: one canonical skill or rule source can propagate to multiple agent-facing targets without turning those targets into canonical homes
- the provenance note records the donor source plus explicit exclusions around marketplace curation, runtime role semantics, MCP propagation, nested loading, and broader orchestration detail
- the second-context note shows the same contract surviving as a documentation-first adaptation inside `aoa-techniques`

## Boundedness check

- result: pass
- the invariant core stays narrow: one canonical source, repeatable propagation, adjacent managed targets, and targets that remain subordinate to the source
- excluded donor features remain explicit and out of scope: marketplace curation policy, runtime role semantics, MCP propagation, nested loading, and broader product-width behavior
- the examples reinforce propagation plus managed targets without widening the bundle into a marketplace, registry, or orchestration system

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
- this new adjacent import does not count as live closure evidence for `AOA-T-0013`, because one-source-to-many-target instruction distribution is a different contract from cross-agent skill or rule propagation

## Recommendation

- accept `AOA-T-0027` as a bounded external import and publish it as `promoted`
- defer any canonical review until another live adopter confirms that the shared-skill propagation contract survives outside the donor repository
