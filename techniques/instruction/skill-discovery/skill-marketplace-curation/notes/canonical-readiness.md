# Canonical Readiness

## Technique
- id: AOA-T-0041
- name: skill-marketplace-curation

## Verdict
- bounded defer for now

## Evidence summary
- donor repo: `n-skills` explicitly frames itself as a curated marketplace for AI coding-agent skills and separates discovery posture from adjacent sync tooling
- public reinforcement: the donor uses categories, featured quality language, and an explicit discovery surface rather than only raw source mirroring
- adjacent-seam reinforcement: the current bundle stays cleanly distinct from `AOA-T-0024` mirroring/provenance and `AOA-T-0040` skill-versus-command ownership
- validation strength: the bundle now has one checklist, one example, and an explicit external-import review with clear exclusions

## Default-use rationale
- this is the right promoted default when a local collection wants to surface upstream-owned skills through one bounded discovery layer without claiming ownership of the underlying skills
- it is narrower than `AOA-T-0024`, because it starts after upstream ownership and sync posture are already legible
- it is narrower than marketplace governance or registry doctrine, because it keeps the center of gravity on editorial discoverability only

## Fresh public-safety check
- review date: 2026-03-23
- result: pass
- sanitization still holds: the bundle keeps only the reusable curation contract and excludes donor-specific installer, registry, and sync implementation details
- public reuse check: the current wording remains understandable without needing the original donor repository's full product surface

## Remaining gaps
- the smallest remaining gap is one second live context that shows the same editorial discovery layer surviving outside the donor repository
- category and featured examples are intentionally thin here, so a future follow-up could strengthen the bundle with a second public curated collection if needed

## Recommendation
- keep `AOA-T-0041` `promoted`
- defer canonical promotion until a second live context confirms that curated discoverability can stay editorial and bounded without drifting into registry or installer behavior
