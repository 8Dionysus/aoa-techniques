# External Origin Note

Use this note when a technique is adapted from an external open-source source.
It complements `TECHNIQUE.md` and records provenance, adaptation boundaries, and public-safety review.

## Source

- source_repo: `https://github.com/FatStinkyPanda/OpenMemory-Code`
- source_license: MIT
- inspired_by: not used in this import
- adapted_from: `README.md`, `QUICKSTART.md`, `AUTOMATIC_STARTUP.md`, `package.json`, `start-openmemory.js`, and `stop-openmemory.ps1`

## What changed

- what_changed: narrowed the donor repository to one bounded pattern: one explicit operator-facing lifecycle entrypoint owns startup and shutdown for a local multi-service stack
- invariant core kept: one main entrypoint starts the bounded stack, dependent services are owned together, runtime status is printed visibly, and shutdown is part of the same lifecycle contract
- project-shaped details removed or generalized: memory-system breadth, enforcement architecture, logging and OAuth side services, global install paths, desktop integration, Windows autorun guidance, and donor-specific ports or file locations

## Public-safety review

- secrets or tokens removed: none from the donor surface used for this import
- private paths, URLs, or IDs removed: donor-specific user paths, local host details, and config locations were generalized away
- environment-specific assumptions generalized: the public technique does not depend on Node.js, Windows wrappers, one process manager implementation, or one specific local service set
- remaining public-safety concerns: the main risk is contract widening into launcher or platform doctrine, not data leakage

## Review notes

- why this adaptation is reusable here: many repositories need one visible lifecycle surface for a bounded local stack without forcing operators to remember several startup and cleanup commands
- limits or follow-up review concerns: this first import intentionally excludes memory semantics, project bootstrap, desktop integration, remote deployment, and donor-specific process-manager breadth
