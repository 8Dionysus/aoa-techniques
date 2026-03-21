# External Origin Note

Use this note when a technique is adapted from an external open-source source.
It complements `TECHNIQUE.md` and records provenance, adaptation boundaries, and public-safety review.

## Source

- source_repo: `https://github.com/codenamev/agentic`
- source_license: MIT
- inspired_by: not used in this import
- adapted_from: `agentic` capability specifications and providers, where named capabilities carry explicit versioned contracts instead of living only as hidden runtime behavior

## What changed

- what_changed: narrowed the donor repository to one bounded docs pattern: one named capability stays reviewable through an explicit versioned specification
- invariant core kept: named capability contracts, explicit version markers, reviewable inputs and outputs, and implementation staying subordinate to the spec
- project-shaped details removed or generalized: plan-and-execute orchestration, agent self-assembly, persistent agent store behavior, execution-history learning, extension systems, and product-level CLI commands

## Public-safety review

- secrets or tokens removed: none from the donor surface used for this import
- private paths, URLs, or IDs removed: donor-specific local config paths, API-token setup, and storage paths were generalized away
- environment-specific assumptions generalized: Ruby runtime, gem packaging, and donor-specific CLI flows were removed from the invariant core
- remaining public-safety concerns: the main risk is semantic overreach; later sibling techniques should treat orchestration, capability registries, or execution-history learning separately instead of widening this bundle

## Review notes

- why this adaptation is reusable here: agent-facing systems often need capability contracts to stay explicit and reviewable even when implementations and providers evolve quickly
- limits or follow-up review concerns: this first import keeps only versioned capability-spec meaning and intentionally rejects registry, persistence, and learning-system breadth
