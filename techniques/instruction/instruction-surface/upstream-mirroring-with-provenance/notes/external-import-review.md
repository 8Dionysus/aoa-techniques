# External Import Review

## Technique
- id: AOA-T-0024
- name: upstream-mirroring-with-provenance

## Verdict
- pass
- review date: 2026-03-21

## Evidence summary
- the bundle includes the expected bounded external-import package: `TECHNIQUE.md`, `notes/external-origin.md`, `notes/second-context-adaptation.md`, one public-safe checklist, and two public-safe examples
- the technique document states one narrow contract: upstream-owned content can be mirrored locally through one explicit source manifest while adjacent provenance keeps origin ownership readable
- the provenance note records the donor source plus explicit exclusions around marketplace policy, registry generation, installer behavior, and other product-width details
- the second-context note shows the same contract surviving as a documentation-first adaptation inside `aoa-techniques`

## Boundedness check
- result: pass
- the invariant core stays narrow: explicit source manifest, repeatable sync, adjacent provenance, and local copies that stay subordinate to upstream ownership
- excluded donor features remain explicit and out of scope: marketplace curation policy, registry generation, installer integration, category taxonomy, daily cron specifics, and agent compatibility breadth
- the examples reinforce mirroring plus provenance without widening the bundle into a marketplace or policy system

## Provenance readability
- result: pass
- a reviewer can trace the path from donor repository to public technique through the external-origin note, bounded exclusions, and documentation-first adaptation without hidden internal context
- the bundle reads as one reusable docs pattern rather than a disguised skill-market product dump
- the current import path is public-safe and reviewable at the present repo scale

## Import-path assessment
- result: pass
- this is a successful bounded external import and the bundle is strong enough to enter the corpus as a `promoted` technique
- the import path is strong enough for initial publication, but not strong enough to justify canonical default status without another live reuse context

## Remaining gaps
- the smallest remaining gap is still one live second context beyond the donor and documentation-first adaptation
- this new adjacent import does not count as live closure evidence for `AOA-T-0013`, because provenance-first mirroring is a different contract from one-source -> many-target rule distribution

## Recommendation
- accept `AOA-T-0024` as a bounded external import and publish it as `promoted`
- defer any canonical review until another live adopter confirms that manifest-driven mirroring plus adjacent provenance survives outside the donor repository
