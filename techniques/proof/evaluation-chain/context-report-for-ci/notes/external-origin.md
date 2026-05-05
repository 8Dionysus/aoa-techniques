# External Origin Note

Use this note when a technique is adapted from an external open-source source.
It complements `TECHNIQUE.md` and records provenance, adaptation boundaries, and public-safety review.

## Source

- source_repo: `https://github.com/ivawzh/agents-md`
- source_license: MIT
- inspired_by: not used in this import
- adapted_from: `agents-md` patterns for composable markdown fragments and CI-facing context reports that track source coverage and token estimates

## What changed

- what_changed: narrowed the donor repository to one bounded report surface for context composition, source coverage, and token-estimate drift
- invariant core kept: CI-facing report output, source coverage comparison, token drift comparison, and read-only observation rather than repair
- project-shaped details removed or generalized: fragment assembly mechanics, remediation snapshot doctrine, provider/runtime telemetry, generic observability breadth, and product-specific migration paths

## Public-safety review

- secrets or tokens removed: none from the donor surface used for this import
- private paths, URLs, or IDs removed: donor-specific local paths and repository-specific report destinations were generalized away
- environment-specific assumptions generalized: the public technique does not depend on a particular CI runner, provider runtime, or fragment-store implementation
- remaining public-safety concerns: future follow-on techniques should review remediation snapshots, runtime telemetry, or composition engines separately instead of widening this report contract

## Review notes

- why this adaptation is reusable here: public repositories often need one bounded report surface that tells CI whether context composition still matched its expected sources
- limits or follow-up review concerns: this first import intentionally keeps only the report surface and excludes composition, remediation, and telemetry breadth
