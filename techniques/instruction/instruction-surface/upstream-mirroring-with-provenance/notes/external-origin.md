# External Origin Note

Use this note when a technique is adapted from an external open-source source.
It complements `TECHNIQUE.md` and records provenance, adaptation boundaries, and public-safety review.

## Source

- source_repo: `https://github.com/numman-ali/n-skills`
- source_license: Apache-2.0
- inspired_by: not used in this import
- adapted_from: `n-skills` auto-sync model where `sources.yaml` names upstream skill mirrors and adjacent `.source.json` metadata preserves attribution for synced copies

## What changed

- what_changed: narrowed the donor repository to one bounded pattern: mirror upstream-owned content through an explicit source manifest and preserve adjacent provenance so the local copy stays subordinate to the upstream source
- invariant core kept: declared source manifest, repeatable sync path, preserved attribution, and readable upstream ownership
- project-shaped details removed or generalized: marketplace policy, installer behavior, registry generation, category taxonomy, daily cron specifics, and agent compatibility breadth

## Public-safety review

- secrets or tokens removed: none from the donor surface used for this import
- private paths, URLs, or IDs removed: donor-specific local paths and marketplace-specific operational assumptions were generalized away
- environment-specific assumptions generalized: GitHub Actions scheduling, installer integration, and agent-specific plugin conventions were removed from the invariant core
- remaining public-safety concerns: future follow-on techniques should review registry generation or marketplace policy separately rather than widening this mirroring contract

## Review notes

- why this adaptation is reusable here: many public collections need to reuse upstream-owned content locally without hiding attribution or silently claiming the mirror as the new source of truth
- limits or follow-up review concerns: this first import intentionally keeps only source-manifest mirroring plus provenance and excludes installer, registry, and marketplace policy layers
