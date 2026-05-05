# External Origin Note

Use this note when a technique is adapted from an external open-source source.
It complements `TECHNIQUE.md` and records provenance, adaptation boundaries, and public-safety review.

## Source

- source_repo: `https://github.com/numman-ali/n-skills`
- source_license: Apache-2.0
- inspired_by: not used in this import
- adapted_from: `n-skills` curated marketplace model where upstream-owned skills are surfaced through one local discovery layer with categories, summaries, and quality bars while sync plumbing and installer behavior stay adjacent rather than central

## What changed

- what_changed: narrowed the donor repository to one bounded pattern: curate a local discoverability layer over upstream-owned skills without claiming the local catalog as the canonical source
- invariant core kept: editorial grouping, short discovery summaries, visible upstream ownership, and a bounded local marketplace surface
- project-shaped details removed or generalized: installer commands, plugin lifecycle semantics, registry generation, daily sync automation, command syntax, and exact donor category names

## Public-safety review

- secrets or tokens removed: none from the donor surface used for this import
- private paths, URLs, or IDs removed: donor-specific marketplace paths, install commands, and sync workflow wiring were generalized away
- environment-specific assumptions generalized: GitHub Actions cadence, plugin installer specifics, and agent-specific command syntax were removed from the invariant core
- remaining public-safety concerns: future sibling techniques should handle sync/provenance, health checking, or registry generation separately rather than widening this curation contract

## Review notes

- why this adaptation is reusable here: many public collections need a reviewable discovery layer over upstream-owned skills without collapsing discoverability into raw mirroring or installer behavior
- primary evidence used: the donor README presents `n-skills` as a curated marketplace, names `AGENTS.md` as the discovery surface, shows explicit categories and quality-bar language, and keeps auto-sync through `sources.yaml` as an adjacent substrate rather than the center of the marketplace story
- limits or follow-up review concerns: this first import intentionally keeps only editorial discoverability and excludes installer, registry, sync-engine, and health-check concerns
