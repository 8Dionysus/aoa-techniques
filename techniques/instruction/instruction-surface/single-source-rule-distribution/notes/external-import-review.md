# External Import Review

## Technique
- id: AOA-T-0013
- name: single-source-rule-distribution

## Verdict
- pass
- review date: 2026-03-21

## Evidence summary
- the bundle already includes the expected bounded external-import package: `TECHNIQUE.md`, `notes/external-origin.md`, `notes/second-context-adaptation.md`, one public-safe checklist, and two public-safe examples
- the technique document states one narrow contract: one canonical rule source fans out to multiple managed instruction targets without turning those targets into separate sources of truth
- the provenance note records the donor source plus explicit exclusions around nested loading, MCP propagation, skills propagation, and other product-width behavior, and that bounded donor package still reads cleanly against the current `ruler` README and duplication test surface
- the second-context note now anchors the first live donor in `aoa-skills`, so the remaining gap is no longer "another import review", but another live many-target context beyond that first sibling-repo proof
- current seeded donor evaluation also records `agents-md` as an overlap hold against `AOA-T-0012` and `n-skills` as the adjacent `AOA-T-0024 upstream-mirroring-with-provenance` import rather than treating either as synthetic evidence for this bundle

## Boundedness check
- result: pass
- the invariant core stays narrow: one canonical rule source, multiple managed instruction targets, repeatable re-application, and minimal target-specific wrappers
- excluded donor features remain explicit and out of scope: nested loading, MCP propagation, skills propagation, backup/revert flows, `.gitignore` automation, and other broader orchestration behavior
- the newer concrete example strengthens the bounded contract by showing multi-target synchronization without widening into product-specific automation behavior

## Provenance readability
- result: pass
- a reviewer can trace the path from the donor repository to the public technique through the external-origin note, the bounded exclusions, and the repo-local adaptation note without hidden internal context
- the bundle still reads as one docs pattern rather than a disguised donor feature dump or a mixed orchestration package
- the current import path remains public-safe and reviewable at the present repo scale

## Import-path assessment
- result: pass
- this is a successful bounded external import, and the bundle is strong enough to remain confidently `promoted`
- the current external intake path is strong enough to stay as the origin anchor, but it is no longer the missing closure item for this technique
- the bundle should therefore stop at intake-strengthening in this wave instead of pretending that another import-only review can substitute for a second live one-source multi-target context

## Remaining gaps
- the smallest remaining gap is still one more live reuse context across multiple agent-facing outputs beyond the first `aoa-skills` donor
- a future stronger context should show an actual managed multi-target instruction flow, not just another readable external-import package or overlap-heavy composition tool

## Recommendation
- keep `AOA-T-0013` `promoted`
- accept this as a successful bounded external-intake refresh and defer any canonical-readiness path until stronger live multi-target reuse exists
