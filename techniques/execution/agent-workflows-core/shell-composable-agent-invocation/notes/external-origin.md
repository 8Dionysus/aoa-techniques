# External Origin Note

Use this note when a technique is adapted from an external open-source source.
It complements `TECHNIQUE.md` and records provenance, adaptation boundaries, and public-safety review.

## Source

- source_repo: `https://github.com/iagooar/qqqa`
- source_license: MIT
- inspired_by: not used in this import
- adapted_from: `qqqa`'s shell-first one-shot execution model where agent runs compose through explicit stdin, stdout, files, and pipes

## What changed

- what_changed: narrowed the donor repository to one bounded pattern: shell-composable one-shot agent invocation
- invariant core kept: one-shot invocation, explicit shell-visible I/O, pipe or file composability, and a clean run boundary after the current result
- project-shaped details removed or generalized: exact wrapper commands, install flow, provider assumptions, confirmation as the core invariant, and broader autonomous loop behavior

## Public-safety review

- secrets or tokens removed: none from the donor surface used for this import
- private paths, URLs, or IDs removed: donor-specific local paths, provider profiles, and runtime-specific assumptions were generalized away
- environment-specific assumptions generalized: the public technique does not depend on one shell wrapper, one provider, or one package manager
- remaining public-safety concerns: the main risk is scope creep; future siblings should treat confirmation logic and broader multi-step workflow behavior separately instead of widening this bundle

## Review notes

- why this adaptation is reusable here: many repositories need agent runs that fit existing shell workflows without becoming hidden long-running sessions
- limits or follow-up review concerns: this first import intentionally excludes generic shell advice, confirmation-boundary doctrine, and broader autonomous-loop behavior
