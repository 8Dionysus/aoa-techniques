# Second Context Adaptation

## Technique
- id: AOA-T-0013
- name: single-source-rule-distribution

## Target project
- name: aoa-techniques
- environment: public library repository with canonical policy docs, one agent-facing collaboration surface, and no built-in multi-agent distribution toolchain
- runtime: documentation-first repository that can describe the pattern clearly even when it does not automate the donor workflow directly

## What changed
- paths: the donor uses `.ruler/` as the canonical rule hub; this adaptation presents a generic canonical rule source such as `rules/` or another docs directory
- services: there is no local `ruler` CLI or automatic fan-out step in this repository
- dependencies: the adaptation depends on a clear canonical source plus managed target policy, not on Node, npm, or the donor package
- operating assumptions: a public docs-oriented repository could keep one canonical rule source and distribute it into multiple agent-facing instruction surfaces while keeping those targets derived rather than canonical

## What stayed invariant
- contract: one canonical rule source fans out to multiple agent-facing instruction surfaces
- validation logic: repeated application should not duplicate shared instructions across targets
- safety rules: managed targets should not become hand-maintained source-of-truth files

## Risks introduced by adaptation
- a small repository may over-abstract the pattern before it truly needs multiple target surfaces
- without an actual apply step, contributors could describe the pattern well but fail to prove synchronization discipline in practice
- the donor's nested-loading and broader orchestration surfaces could blur the boundary unless they stay explicitly excluded

## Evidence
- `AOA-T-0002 source-of-truth-layout` already proves that this repository values one canonical home per information class rather than many drifting copies
- `AOA-T-0012 deterministic-context-composition` already proves that this repository can publish bounded docs patterns around managed derived outputs
- this adaptation combines those repository-native instincts into a bounded sketch for one canonical rule source that could fan out into several agent-facing instruction surfaces without making each target canonical
- this is sufficient as repo-local adaptation evidence for a first `promoted` external-import draft, but it is not enough to argue for `canonical` status on its own

## Result
- works as a bounded repo-local adaptation sketch for a first promoted draft, while still needing stronger live reuse evidence before any future canonical review
