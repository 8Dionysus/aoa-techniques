---
id: AOA-T-0027
name: cross-agent-skill-propagation
domain: docs
status: promoted
origin:
  project: ruler
  path: README.md
  note: Adapted from the open-source ruler project, which keeps one canonical rule source and fans it out to multiple agent-facing targets without turning the targets into new sources of truth.
owners:
  - 8Dionysus
tags:
  - docs
  - propagation
  - distribution
  - agent-instructions
  - anti-drift
summary: Keep one canonical skill or rule source and propagate it to multiple agent-facing targets without turning each target into a hand-maintained source of truth.
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

# cross-agent-skill-propagation

## Intent

Keep one canonical skill or rule source and propagate it to multiple agent-facing targets so shared guidance stays synchronized without making every target a separate source of truth.

## When to use

- repositories that need one shared skill or rule core to reach several agent-facing targets
- projects where managed outputs should stay derived from one canonical source rather than hand-edited in place
- workflows where the risk is target drift across agent-facing surfaces, not multi-step runtime orchestration
- cases where the same shared rule core should be visible to multiple agents without widening into a marketplace, registry, or role system

## When not to use

- repositories that only need one instruction surface
- projects where each target must carry materially different meaning
- workflows where the real need is upstream mirroring with provenance rather than local rule propagation
- cases where the real need is runtime role semantics, MCP propagation, or broader multi-target orchestration

## Inputs

- one canonical skill or rule source
- two or more agent-facing targets that should share the same core meaning
- one managed distribution step that refreshes the targets from the canonical source
- one explicit policy that keeps target files subordinate to the source

## Outputs

- synchronized agent-facing targets
- one retained canonical source of shared meaning
- lower drift risk across agent-facing outputs
- a repeatable way to re-apply the same shared skill or rule core

## Core procedure

1. Choose one canonical location for the shared skill or rule source.
2. Name the agent-facing targets that should receive that shared core.
3. Propagate the shared meaning into each target with only minimal destination-specific wrapper text.
4. Keep the targets treated as managed outputs rather than canonical homes.
5. Re-apply the distribution step whenever the canonical source changes.
6. Review the canonical source first and use the target files only to confirm synchronized propagation.
7. Keep the shared core narrow enough that it can survive repeated propagation without becoming target-specific policy.

## Contracts

- one canonical skill or rule source owns the shared meaning
- target files are managed or derived outputs, not canonical editable homes
- the same source update can be propagated repeatedly without introducing drift
- target-specific wrappers must not change the shared rule intent
- manual edits to target files are either forbidden or clearly subordinate to the canonical source
- the technique stays centered on skill or rule propagation into managed targets, not on role contracts, marketplace curation, or nested loader breadth

Relationship to adjacent techniques: unlike `AOA-T-0013`, this technique keeps the center of gravity on skill or rule propagation into managed agent-facing targets rather than the broader instruction-surface distribution story. Unlike `AOA-T-0024`, it does not mirror upstream-owned content into a curated local collection; the source here is a local canonical skill or rule core that fans out to managed outputs.

## Risks

### Failure modes

- target surfaces drift because local edits are applied without flowing back through the canonical source
- contributors start treating one of the managed targets as if it were a new source of truth
- propagation stops being repeatable, so synchronized-looking targets hide real source drift

### Negative effects

- one-to-many propagation can hide divergence longer than hand-maintained files would
- wrapper or formatting differences can make the shared meaning harder to compare across targets
- the technique can create false confidence if all targets look updated while the canonical source has already split in meaning

### Misuse patterns

- widening the technique into marketplace policy or runtime role semantics
- treating MCP propagation, nested loading, or broader orchestration as if they belong inside this contract
- adding target-specific shadow logic until each managed output becomes a semi-canonical source in disguise

### Detection signals

- canonical source changes stop flowing cleanly through to every managed target
- reviewers cannot confirm that the shared core still matches across wrappers or re-apply passes
- managed targets accumulate local edits that are not obviously derivable from the canonical source

### Mitigations

- keep one explicit canonical source and make every target clearly subordinate to it
- remove local target edits and route changes through the source before re-applying distribution
- keep repeatability checks part of the contract so synchronized appearance does not substitute for actual parity
- split broader propagation or loading behavior into separate techniques instead of letting target-specific shadow logic accumulate inside this one

## Validation

Verify the technique by confirming that:
- one canonical skill or rule source is named explicitly
- at least two agent-facing targets receive the same shared core
- target files are treated as managed or derived outputs rather than canonical editable files
- re-applying distribution does not duplicate the shared meaning in target files
- a source change routes through the canonical source first instead of through target-file edits

See `checks/cross-agent-skill-propagation-checklist.md`.

## Adaptation notes

What can vary across projects:
- the canonical source directory name
- the exact set of target instruction files
- whether propagation is a CLI command, build task, or CI-enforced check
- the target-specific wrapper format used around shared instructions

What should stay invariant:
- one canonical skill or rule source owns the shared meaning
- multiple agent-facing targets can be refreshed from that source
- target files remain derived rather than hand-maintained canonical documents
- propagation exists to reduce drift, not to create many divergent instruction variants

Project-shaped details that should not be treated as invariant:
- marketplace curation policy
- runtime role semantics
- MCP propagation
- nested loading breadth
- installer or plugin registry behavior

## Public sanitization notes

This import narrows the donor repository to one docs pattern: one canonical skill or rule source propagated to multiple agent-facing targets. Marketplace policy, runtime role semantics, MCP propagation, nested loading, registry behavior, and broader product-width detail were intentionally left out of the public technique contract.

## Example

See `examples/minimal-cross-agent-skill-propagation.md` and `examples/concrete-multi-target-skill-propagation.md`.

## Checks

See `checks/cross-agent-skill-propagation-checklist.md`.

## Promotion history

- adapted from open-source `ruler`
- promoted into `aoa-techniques` on 2026-03-21 as a bounded external-import technique for cross-agent skill or rule propagation into managed targets

## Future evolution

- split out `nested-rule-loading` as a separate sibling technique if hierarchical layering proves reusable on its own
- split out a dedicated skill-marketplace sibling if curated discovery becomes reusable without the rest of the propagation contract
- add a stronger second live context if another public repository adopts the same shared-source propagation pattern
