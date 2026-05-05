# External Import Review

## Technique
- id: AOA-T-0064
- name: capability-discovery

## Verdict
- pass
- review date: 2026-03-28

## Evidence summary

- the bundle includes the expected bounded external-import package: `TECHNIQUE.md`, `notes/external-origin.md`, `notes/second-context-adaptation.md`, one public-safe checklist, and one public-safe example
- the technique document states one narrow contract: published capability records are discovered through explicit bounded queries with visible result shape
- the provenance note records the donor sources plus explicit exclusions around ranking, trust filters, semantic linkage, and registry runtime breadth
- the second-context note keeps the same contract readable as a documentation-first adaptation inside `aoa-techniques`

## Boundedness check

- result: pass
- the invariant core stays narrow: explicit query fields, bounded match rules, identifier-or-record result shape, and reviewable lookup semantics
- excluded donor features remain explicit and out of scope: registry publication, semantic linkage, signature systems, distributed routing, ranking policy, and runtime resolution
- the example and checklist reinforce lookup-contract review without widening the technique into curation, trust, or product doctrine

## Provenance readability

- result: pass
- a reviewer can trace the path from donor docs and proto query models to public technique through the external-origin note, bounded exclusions, and documentation-first adaptation without hidden internal context
- the bundle reads as one discovery-query contract rather than a disguised directory-platform import
- the import path is public-safe and reviewable at the present repo scale

## Import-path assessment

- result: pass
- this is a successful bounded external import and the bundle is strong enough to enter the corpus as a `promoted` technique
- the import path is strong enough for initial publication, but not strong enough to justify canonical default status without another live workflow context beyond the current donor family

## Remaining gaps

- the smallest remaining gap is still one live second context beyond the donor family and documentation-first adaptation
- a future stronger context should show another public workflow surface where bounded discovery queries stay explicit without widening into ranking, trust policy, or directory-platform semantics

## Recommendation

- accept `AOA-T-0064` as a bounded external import and publish it as `promoted`
- defer any canonical review until another live adopter confirms that the discovery-query contract survives outside the current donor family
