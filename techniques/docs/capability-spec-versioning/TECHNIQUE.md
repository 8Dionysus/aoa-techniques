---
id: AOA-T-0025
name: capability-spec-versioning
domain: docs
status: promoted
origin:
  project: agentic
  path: README.md
  note: Adapted from the open-source agentic project, which defines agent capabilities through explicit versioned specifications instead of treating them as hidden runtime behavior.
owners:
  - 8Dionysus
tags:
  - docs
  - capability
  - versioning
  - contract
  - agent-facing
summary: Keep agent-facing capability contracts in a versioned, reviewable spec so capability changes stay explicit and reusable without turning the spec into routing or registry policy.
maturity_score: 3
rigor_level: bounded
reversibility: moderate
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-21
export_ready: true
relations:
  - type: complements
    target: AOA-T-0013
evidence:
  - kind: external_origin
    path: notes/external-origin.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: external_review
    path: notes/external-import-review.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# capability-spec-versioning

## Intent

Keep capability behavior reviewable by naming it in one versioned spec instead of letting capability meaning hide inside provider code, runtime wiring, or agent registry state.

## When to use

- agent-facing systems that expose named capabilities and need contract changes to be explicit
- repositories where capability inputs, outputs, and invariants should stay reviewable across revisions
- workflows that need one capability source of truth without widening into orchestration or registry semantics
- teams that want compatibility discussion to happen at the spec layer before implementation drift accumulates

## When not to use

- workflows whose main problem is plan orchestration, task scheduling, or multi-agent execution order
- systems where the real reusable object is a persistent agent registry rather than one capability contract
- cases where version labels are cosmetic and no contract-level compatibility review is expected
- repositories that actually need one-source fan-out to many targets instead of one versioned capability description

## Inputs

- one named capability with a bounded purpose
- one explicit version marker for the current contract
- one spec that names expected inputs, outputs, and invariants
- one review path for compatibility notes when the contract changes
- one implementation layer that stays subordinate to the spec

## Outputs

- one reviewable capability contract with explicit version identity
- one clearer compatibility story when capability behavior changes
- lower ambiguity around what the capability promises versus how it is currently implemented
- a reusable source surface that can stay stable while implementations evolve underneath it

## Core procedure

1. Name one capability and its bounded purpose before expanding implementation detail.
2. Write one explicit capability spec that states version, expected inputs, outputs, and invariant behavior.
3. Keep the capability spec readable as the source of truth for the contract, not just as generated metadata or runtime code comments.
4. Record compatibility expectations when a version changes so reviewers can tell whether consumers need an update.
5. Treat implementations, providers, and runtime adapters as subordinate realizations of the capability contract.
6. Review capability changes at the spec layer before widening registry behavior, orchestration, or persistence semantics.
7. Split out separate techniques if registry management, orchestration, or learning behavior becomes the real reusable object.

## Contracts

- one capability spec stays the authoritative contract for the named capability
- version changes are explicit and reviewable rather than implicit in runtime code drift
- inputs, outputs, and invariants remain readable without opening implementation internals first
- implementations and providers stay subordinate to the capability spec
- the technique does not own plan-and-execute orchestration, persistent registries, or execution-history learning
- the capability spec does not become routing policy, agent-role registry, or hidden runtime magic

## Risks

### Failure modes

- a version number changes without any real contract review, so the spec stops signaling meaningful change
- implementation detail overwhelms the spec until reviewers cannot tell what the stable capability contract actually is
- teams treat the capability spec as a registry or orchestration object instead of a bounded contract

### Negative effects

- extra contract discipline can slow down fast experiments when a team really only needs a local prototype
- versioned specs can create ceremony if the capability boundary is still unstable or poorly named
- a strong spec surface can tempt teams to over-document implementation detail that does not belong in the reusable contract

### Misuse patterns

- widening the technique into agent self-assembly, capability discovery, or persistence behavior
- treating provider implementations as interchangeable proof that the spec no longer needs explicit review
- using spec versioning as a substitute for real compatibility thinking

### Detection signals

- reviewers cannot explain what changed in a new version except by reading code diffs
- capability docs start listing runtime adapters, registries, or orchestration hooks as if they were the core contract
- compatibility notes disappear while capability versions keep changing

### Mitigations

- keep one explicit capability spec with version, inputs, outputs, and invariants named in plain reviewable language
- route orchestration, registry, and persistence concerns into separate techniques instead of widening this contract
- require contract-level review notes when a version changes
- treat implementation detail as subordinate unless it materially changes the reusable capability boundary

## Validation

Verify the technique by confirming that:
- one capability has one explicit versioned spec
- the spec names inputs, outputs, and invariants clearly enough to review without reading implementation code first
- contract changes are visible at the spec layer rather than hidden only in provider or runtime code
- compatibility notes exist when version changes matter to downstream consumers
- orchestration, persistence, and registry semantics stay outside this bounded contract

See `checks/capability-spec-versioning-checklist.md`.

## Adaptation notes

What can vary across projects:
- the file format of the capability spec
- the versioning scheme
- the names of implementations or providers
- the review ritual used to explain compatibility changes

What should stay invariant:
- one capability contract stays explicit and versioned
- the spec remains readable as the source of truth
- implementations stay subordinate to the spec
- the technique remains about capability contract versioning, not orchestration or registry behavior

Project-shaped details that should not be treated as invariant:
- plan-and-execute workflow design
- persistent agent store layout
- learning or history analysis features
- plugin or protocol extension systems

## Public sanitization notes

This import narrows the donor repository to one docs pattern: a versioned capability specification that remains reviewable as a contract. Plan orchestration, self-assembly, persistence, learning through execution history, plugin management, protocol adapters, and product-level CLI behavior were intentionally left out of the public technique contract.

## Example

See `examples/minimal-capability-spec-versioning.md` and `examples/concrete-capability-upgrade-with-compat-window.md`.

## Checks

See `checks/capability-spec-versioning-checklist.md`.

## Promotion history

- adapted from open-source `agentic`
- promoted into `aoa-techniques` on 2026-03-21 as a bounded external-import technique for versioned capability contracts

## Future evolution

- split out a dedicated capability-registry technique if stored capability discovery and lifecycle management proves reusable on its own
- split out a dedicated compatibility-matrix sibling if version-bridge policy becomes reusable beyond one capability spec
- add a stronger second live context if another public repository uses the same versioned capability contract outside the donor repo
