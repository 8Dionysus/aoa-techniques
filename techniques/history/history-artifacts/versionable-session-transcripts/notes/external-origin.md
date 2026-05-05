# External Origin Note

Use this note when a technique is adapted from an external open-source or public documentation source.
It complements `TECHNIQUE.md` and records provenance, adaptation boundaries, and public-safety review.

## Source

- source_repo: `https://docs.specstory.com/`
- source_license: not stated in the public documentation used for this import
- inspired_by: not used in this import
- adapted_from: `specstory/quickstart`, `specstory/features`, `integrations/terminal-coding-agents`, and `integrations/claude-code`

## What changed

- what_changed: narrowed the donor to one bounded post-capture pattern: already-saved AI conversations can be selected, combined, reviewed, edited, and exported as readable Markdown transcript artifacts
- invariant core kept: transcript export starts from an existing saved artifact layer, preserves readable Markdown plus timestamps or metadata, and supports review, commit, citation, or selective sharing
- project-shaped details removed or generalized: autosave toggles, wrapper launch flows, hosted share URLs, login or account requirements, cloud search and organization, and automatic rule derivation from conversation history

## Public-safety review

- secrets or tokens removed: none from the donor surfaces used for this import
- private paths, URLs, or IDs removed: donor-specific share URLs, support paths, and exact product account behavior were omitted
- environment-specific assumptions generalized: the public technique does not depend on one editor, one CLI wrapper, or one hosted publication path
- remaining public-safety concerns: the main risks are overlap with capture on one side and drift into rule-derivation or memory-style authority on the other

## Review notes

- why this adaptation is reusable here: many repositories need a readable transcript artifact for review or handoff after capture already happened, and the donor shows concrete post-capture packaging behavior instead of capture alone
- limits or follow-up review concerns: this import intentionally excludes first-save capture, cloud sync, search UX, public-link hosting, and derived-rules behavior
