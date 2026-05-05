# External Import Review

## Technique
- id: AOA-T-0025
- name: capability-spec-versioning

## Verdict
- pass
- review date: 2026-03-21

## Evidence summary
- the bundle includes the expected bounded external-import package: `TECHNIQUE.md`, `notes/external-origin.md`, `notes/second-context-adaptation.md`, one public-safe checklist, and two public-safe examples
- the technique document states one narrow contract: one named capability remains reviewable through an explicit versioned spec rather than hiding meaning inside provider code or runtime wiring
- the provenance note records the donor source plus explicit exclusions around plan-and-execute orchestration, self-assembly, persistence, learning through execution history, and extension-system breadth
- the second-context note keeps the same contract readable as a documentation-first adaptation inside `aoa-techniques`

## Boundedness check
- result: pass
- the invariant core stays narrow: named capability contract, explicit version marker, reviewable inputs and outputs, and implementation staying subordinate to the spec
- excluded donor features remain explicit and out of scope: plan-and-execute orchestration, persistent agent store behavior, execution-history learning, protocol handlers, plugin systems, and product CLI management
- the examples reinforce contract review and compatibility discipline without widening the technique into runtime registry or routing behavior

## Provenance readability
- result: pass
- a reviewer can trace the path from donor repository to public technique through the external-origin note, bounded exclusions, and documentation-first adaptation without hidden internal context
- the bundle reads as one docs pattern rather than a disguised donor feature dump or whole-product import
- the current import path is public-safe and reviewable at the present repo scale

## Import-path assessment
- result: pass
- this is a successful bounded external import and the bundle is strong enough to enter the corpus as a `promoted` technique
- the import path is strong enough for initial publication, but not strong enough to justify canonical default status without another live repository context

## Remaining gaps
- the smallest remaining gap is still one live second context beyond the donor and documentation-first adaptation
- a future stronger context should show a public repository using a versioned capability spec as an actual agent-facing contract, not only as imported review prose

## Recommendation
- accept `AOA-T-0025` as a bounded external import and publish it as `promoted`
- defer any canonical review until another live adopter confirms that the versioned capability-contract pattern survives outside the donor repository
