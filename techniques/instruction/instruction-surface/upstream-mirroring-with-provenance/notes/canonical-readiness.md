# Canonical Readiness

## Technique
- id: AOA-T-0024
- name: upstream-mirroring-with-provenance

## Verdict
- approve for canonical promotion

## Evidence summary
- external origin: the imported technique has a bounded donor contract and explicit exclusions around marketplace policy, registry generation, installer behavior, and product-width sync detail
- first second context: `aoa-techniques` records the same contract as a documentation-first adaptation with examples and a checklist
- exact public reinforcement: `managedcode/dotnet-skills` keeps external upstream repositories in a dedicated `external-sources/` area, uses `vendir.yml` and `vendir.lock.yml` for fetch-and-pin, copies upstream `SKILL.md`, `AGENT.md`, and `references/` content verbatim, and keeps local-only metadata in sibling `manifest.json` files instead of injecting it into upstream markdown
- validation strength: the bundle now carries a checklist, two examples, a clean external-origin note, one documentation-first adaptation, one exact-fit public second context beyond the donor, and an adverse-effects review

## Default-use rationale
- this is the right canonical default when a local collection wants to mirror upstream-owned content with explicit provenance instead of silently claiming the mirrored copy as a new canonical source
- it remains narrower than `AOA-T-0013`, which starts when the canonical source is already local and the main problem is fan-out to many managed instruction targets
- it remains narrower than `AOA-T-0041`, which owns editorial skill discoverability rather than mirror provenance, fetch pins, or local copy ownership

## Fresh public-safety check
- review date: 2026-05-12
- result: pass
- source checked: `managedcode/dotnet-skills` at `1f47038f03a9bd0f7e927969ae271e122cd23777`
- sanitization still holds: the bundle keeps only the reusable mirroring-plus-provenance contract and excludes marketplace, installer, and registry detail
- public reuse check: the public examples, checklist, and adaptation notes remain understandable without hidden donor-repo context

## Remaining gaps
- no blocking promotion gap remains for the current canonical contract
- future work may still add a narrower checksum/pin-verification sibling if mirror integrity becomes the reusable center rather than upstream ownership and adjacent provenance

## Recommendation
- promote `AOA-T-0024` to `canonical`
- keep `notes/adverse-effects-review.md` as the watch surface for local-copy authority drift, provenance-file staleness, and sync-substrate overreach
