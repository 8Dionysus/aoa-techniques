# External Origin Note

Use this note when a technique is adapted from an external open-source or public documentation source.
It complements `TECHNIQUE.md` and records provenance, adaptation boundaries, and public-safety review.

## Source

- source_repo: `https://github.com/gotalab/cc-sdd`
- source_license: `MIT`
- inspired_by: not used in this import
- adapted_from: `README.md`, `.kiro/specs/photo-albums-en/requirements.md`, `.kiro/specs/photo-albums-en/design.md`, and `.kiro/specs/photo-albums-en/tasks.md`

## What changed

- what_changed: narrowed the donor to one bounded planning pattern: keep requirements, design, and tasks as explicit successive layers before implementation
- invariant core kept: one visible requirement layer constrains one design layer, and one design layer constrains one bounded task layer
- project-shaped details removed or generalized: command suites, agent-specific installation paths, template systems, steering docs, project memory, validation commands, and broader spec-driven methodology doctrine

## Public-safety review

- secrets or tokens removed: none from the donor surfaces used for this import
- private paths, URLs, or IDs removed: donor-specific command names, install instructions, and directory conventions were omitted
- environment-specific assumptions generalized: the public technique does not depend on one CLI, one IDE workflow, or one template pack
- remaining public-safety concerns: the main risks are overlap with general planning or execution workflows on one side and drift into full methodology doctrine on the other

## Review notes

- why this adaptation is reusable here: many repositories need a visible requirement -> design -> tasks seam without importing the donor's full SDD stack
- limits or follow-up review concerns: this import intentionally excludes steering, research, template ecosystems, project-memory surfaces, validation commands, and methodology branding
