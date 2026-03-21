# External Origin Note

Use this note when a technique is adapted from an external open-source source.
It complements `TECHNIQUE.md` and records provenance, adaptation boundaries, and public-safety review.

## Source

- source_repo: `https://github.com/specstoryai/getspecstory`
- source_license: Apache-2.0
- inspired_by: not used in this import
- adapted_from: `SpecStory` local-first session capture where AI coding sessions are saved into project-scoped `.specstory/history/` artifacts across supported tools

## What changed

- what_changed: narrowed the donor repository to one bounded history pattern: local-first session capture into project-scoped repo artifacts
- invariant core kept: local-first capture, project-scoped history directory, versioned session artifacts, and later review or reuse on top of those artifacts
- project-shaped details removed or generalized: cloud sync, search UI, login flows, tool installation, history-derived skills, and history-to-instructions behavior

## Public-safety review

- secrets or tokens removed: none from the donor surface used for this import
- private paths, URLs, or IDs removed: donor-specific cloud endpoints, login steps, and product links were generalized away
- environment-specific assumptions generalized: Homebrew install flows, provider-specific wrappers, and product-specific CLI naming were removed from the invariant core
- remaining public-safety concerns: the main risk is boundary confusion; later sibling techniques should review history-to-instructions or memory-style behavior separately instead of widening this bundle

## Review notes

- why this adaptation is reusable here: many AI-assisted repositories need session history to persist as inspectable project artifacts even before they adopt heavier memory or analytics systems
- limits or follow-up review concerns: this first import keeps only the local artifact contract and intentionally rejects cloud sync, memory recall, and derived-skill breadth
