# Canonical Readiness

## Technique
- id: AOA-T-0041
- name: skill-marketplace-curation

## Verdict
- approve for canonical promotion

## Evidence summary
- donor repo: `n-skills` explicitly frames itself as a curated marketplace for AI coding-agent skills and separates discovery posture from adjacent sync tooling
- first reinforcement: the donor uses categories, featured quality language, and an explicit discovery surface rather than only raw source mirroring
- exact public reinforcement: `VoltAgent/awesome-agent-skills` is a public curated collection of agent skills, groups skills by source families and topic sections, and presents short editorial descriptions and outbound source links without owning the underlying skill meaning, installer behavior, or registry governance
- validation strength: the bundle now has a checklist, one example, a clean external-origin note, an explicit external-import review, one exact-fit public curated collection beyond the donor, and an adverse-effects review

## Default-use rationale
- this is the right canonical default when a local collection wants to surface upstream-owned skills through one bounded discovery layer without claiming ownership of the underlying skills
- it is narrower than `AOA-T-0024`, because it starts after upstream ownership and sync posture are already legible
- it is narrower than marketplace governance or registry doctrine, because it keeps the center of gravity on editorial discoverability only

## Fresh public-safety check
- review date: 2026-05-12
- result: pass
- source checked: `VoltAgent/awesome-agent-skills` at `95fa85de2b8044984d8ee790d0a4c1884ff2cf0b`
- sanitization still holds: the bundle keeps only the reusable curation contract and excludes donor-specific installer, registry, and sync implementation details
- public reuse check: the current wording remains understandable without needing either source repository's full product surface

## Remaining gaps
- no blocking promotion gap remains for the current canonical contract
- future work may still add a separate registry-trust or install-substrate sibling if a curation surface begins making safety, availability, or installability claims

## Recommendation
- promote `AOA-T-0041` to `canonical`
- keep `notes/adverse-effects-review.md` as the watch surface for catalog authority drift, thin curation, registry overreach, and hidden install policy
