---
id: AOA-T-0063
name: versioned-agent-registry-contract
domain: docs
kind: artifact
status: promoted
origin:
  project: agntcy/dir
  path: README.md + proto/agntcy/dir/core/v1/record.proto
  note: Adapted from Directory's named and versioned record contract so registry-facing capability publication stays reviewable without importing discovery queries, signature systems, or registry product semantics.
owners:
  - 8Dionysus
tags:
  - docs
  - registry
  - capability
  - versioning
  - contract
summary: Keep registry-facing capability entries reviewable as named versioned records with explicit references and metadata so publication stays bounded without widening into discovery policy or registry product doctrine.
maturity_score: 3
rigor_level: bounded
reversibility: moderate
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-28
export_ready: true
relations:
  - type: complements
    target: AOA-T-0025
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

# versioned-agent-registry-contract

## Intent

Keep registry-facing capability publication reviewable by expressing entries as named versioned records with explicit references and metadata instead of hiding registry meaning inside runtime state, search implementations, or marketplace surfaces.

## When to use

- a capability, agent, or similar object must be published into a directory or registry as a reviewable entry
- the main reusable object is the registry-facing entry contract rather than the capability spec alone
- downstream readers need explicit entry identity such as name, version, reference, and schema metadata
- the workflow needs one publication contract without widening into discovery ranking, curation, or registry product doctrine

## When not to use

- the real need is a single versioned capability spec with no registry-entry surface
- the real need is discovery query behavior, selector policy, or search ranking
- the real need is marketplace curation over upstream-owned entries
- the contract only makes sense when bundled with distributed routing, signing infrastructure, or registry implementation details

## Inputs

- one named record or capability object
- one explicit version identifier for the published entry
- one stable record reference such as a content ID or equivalent immutable locator
- one metadata layer that names schema version, timestamps, or bounded annotations

## Outputs

- one reviewable registry-entry contract for a versioned record
- one clearer publication story for how a capability record is named and referenced
- lower ambiguity between the record itself, its registry-facing entry, and adjacent discovery or curation layers
- a reusable contract surface that can stay stable while discovery, trust, or runtime behavior evolves separately

## Core procedure

1. Define one registry-facing entry for the published object before discussing discovery behavior or runtime implementation.
2. Make the entry identity explicit with a name, version, and stable record reference.
3. Keep metadata such as schema version, annotations, and creation time readable as part of the contract rather than implicit in storage internals.
4. Treat the registry entry as a reviewable publication surface distinct from the underlying record payload.
5. Review entry changes at the contract layer when names, versions, references, or metadata meaning change.
6. Keep discovery queries, signature systems, and routing semantics subordinate to the entry contract rather than letting them redefine it.
7. Split out separate techniques if discovery policy, semantic linkage, or registry implementation becomes the real reusable object.

## Contracts

- one registry-facing entry has explicit identity through name, version, and record reference
- metadata needed to interpret the entry remains reviewable without opening runtime code first
- the entry contract stays distinct from the underlying payload, discovery queries, and marketplace presentation
- version changes are visible at the entry-contract layer rather than only through implementation drift
- the technique does not own discovery ranking, registry governance, runtime synchronization, or signature-verification policy
- the registry entry does not become a disguised marketplace page, search policy, or graph semantics surface

Relationship to adjacent techniques: unlike [AOA-T-0025](../capability-spec-versioning/TECHNIQUE.md), this technique does not own the full internal capability contract; it owns the directory-facing entry that publishes a versioned record into a registry surface. Unlike [AOA-T-0041](../skill-marketplace-curation/TECHNIQUE.md), it does not curate discovery or editorial grouping; it only makes the published entry contract explicit. Unlike [AOA-T-0021](../bounded-relation-lift-for-kag/TECHNIQUE.md), it does not turn entry metadata into graph semantics or typed relation doctrine.

## Risks

### Failure modes

- entry versions change without any contract review, so the entry surface stops signaling meaningful publication changes
- the entry contract collapses into storage or runtime implementation detail
- metadata becomes so loose that another reader cannot tell what the published record actually is

### Negative effects

- an explicit entry contract can add ceremony if the workflow only needed a local capability spec and never truly needed registry publication
- teams may over-document entry metadata that belongs in adjacent trust or runtime layers
- a strong publication contract can create false confidence that discovery or trust semantics are already solved

### Misuse patterns

- widening the bundle into search behavior, selector policy, or marketplace curation
- treating a registry entry as if it already owns capability meaning, discovery ranking, and trust verification at once
- using entry annotations as a backdoor for graph semantics or registry governance rules

### Detection signals

- reviewers cannot explain what changed in the published entry except by reading runtime code or storage internals
- the entry surface starts listing search filters, ranking rules, or curation policy as core contract fields
- metadata fields multiply mainly to patch adjacent discovery or governance concerns

### Mitigations

- keep name, version, reference, and bounded metadata explicit and reviewable
- route discovery, trust, and curation concerns into separate sibling techniques
- require contract-level review when entry identity or metadata meaning changes
- trim annotations or metadata that do not support the bounded publication contract

## Validation

Verify the technique by confirming that:
- one registry entry has explicit name, version, and record reference
- schema version and other bounded metadata remain readable without opening implementation code first
- the published entry can be distinguished clearly from discovery queries and marketplace surfaces
- contract changes are visible at the entry layer rather than only in runtime or storage code
- discovery policy, trust policy, and graph semantics remain outside this bounded contract

See `checks/versioned-agent-registry-contract-checklist.md`.

## Adaptation notes

What can vary across projects:
- the format of the registry entry
- the versioning scheme
- the kind of stable record reference used
- which bounded metadata fields are required
- how compatibility notes are recorded when the entry changes

What should stay invariant:
- registry-facing entry identity remains explicit
- name, version, and record reference stay reviewable
- metadata stays bounded and interpretable
- the entry contract remains separate from discovery and curation layers

Project-shaped details that should not be treated as invariant:
- one distributed peer-to-peer network or DHT implementation
- one cryptographic signing system or trust pipeline
- one search API or query language
- one marketplace UI or selection surface
- one registry product or runtime deployment stack

## Public sanitization notes

This import narrows the donor to one bounded pattern: a registry-facing entry publishes a named versioned record with explicit references and metadata. Distributed routing, search services, signature referrers, and directory product semantics were intentionally left out of the public contract.

## Example

See `examples/minimal-versioned-agent-registry-contract.md`.

## Checks

See `checks/versioned-agent-registry-contract-checklist.md`.

## Promotion history

- adapted from open-source `agntcy/dir`
- staged through the chat wave 1A registry-discovery lane inside `aoa-techniques`
- promoted into `aoa-techniques` on 2026-03-28 as a bounded external-import technique for versioned registry-entry contracts

## Future evolution

- keep capability-spec ownership separate instead of widening this bundle back into full capability semantics
- keep discovery and query behavior separate instead of turning the entry contract into search policy
- keep semantic linkage separate instead of using registry metadata as a backdoor graph layer
