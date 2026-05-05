# External Origin Note

Use this note when a technique is adapted from an external open-source source.
It complements `TECHNIQUE.md` and records provenance, adaptation boundaries, and public-safety review.

## Source

- source_repo: `https://github.com/iagooar/qqqa`
- source_license: MIT
- inspired_by: not used in this import
- adapted_from: `qqqa`'s split between read-only shell-side work and one explicit confirmed mutating step

## What changed

- what_changed: narrowed the donor repository to one bounded pattern: a visible confirmation seam before a mutating action
- invariant core kept: read or plan work stays distinct from mutation, the confirmation is explicit, and the action stays bounded to the named target
- project-shaped details removed or generalized: stateless-shell framing, provider/runtime assumptions, generic caution prose, and broad orchestration breadth

## Public-safety review

- secrets or tokens removed: none from the donor surface used for this import
- private paths, URLs, or IDs removed: donor-specific local paths and runtime-specific assumptions were generalized away
- environment-specific assumptions generalized: the public technique does not depend on a particular shell wrapper, provider, or CLI stack
- remaining public-safety concerns: the main risk is scope creep, not data leakage; future siblings should treat broader multi-step workflow behavior separately

## Review notes

- why this adaptation is reusable here: many repositories need a small, visible gate between advice and mutation so the action stays reviewable and bounded
- limits or follow-up review concerns: this first import intentionally excludes stateless-shell posture, generic caution prose, and broader autonomous loops
