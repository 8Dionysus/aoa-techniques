# Technique Intelligence Guide

This guide defines the bounded contract for the Technique Intelligence layer.

Technique Intelligence is attention over atomic moves. It helps a reader or
agent find, compare, explain, and pack one source-linked technique without
turning the registry into source truth, execution workflow, proof verdict,
role law, runtime behavior, or graph semantics.

See also:

- [Start Here](../START_HERE.md)
- [Technique Atom Contract](../TECHNIQUE_ATOM_CONTRACT.md)
- [Technique Topology Contract](../TECHNIQUE_TOPOLOGY_CONTRACT.md)
- [Technique Intelligence](../readers/intelligence/TECHNIQUE_INTELLIGENCE.md)
- [`../../generated/technique_intelligence_registry.json`](../../generated/technique_intelligence_registry.json)
- [`../../generated/technique_intelligence_registry.min.json`](../../generated/technique_intelligence_registry.min.json)
- [`../../generated/technique_intelligence_dag.json`](../../generated/technique_intelligence_dag.json)

## Source Contract

The registry is derived from existing source-owned and validator-backed
surfaces:

- authored `techniques/**/TECHNIQUE.md` bundles
- `generated/technique_catalog.json`
- `generated/technique_capsules.json`
- `generated/technique_sections.full.json`
- checklist, example, evidence-note, semantic-review, and shadow-review
  manifests
- Distillation topology scout, family scout, tree projection, and fixture
  sketch surfaces

The registry may join these surfaces, but it may not outrank them. If a
derived entry conflicts with a bundle, repair the source, builder, or generated
parity path before trusting the entry.

## Move Shape

Each registry entry should answer the smallest useful attention questions:

- what move this is
- when it applies
- when it does not apply
- what input it needs
- what output it produces
- which contract must stay true
- what can go wrong
- what minimal validation keeps the move honest
- where the move stops

This shape is deliberately not an activation shape. The registry does not say
what to run. It says which move to inspect and how to keep that inspection
source-linked.

## Query, Explain, Pack

The local CLI exposes three reader actions:

- `query`: find likely technique moves for an intent using portable lexical
  search with SQLite FTS5 when available
- `explain`: show why one candidate fits, what cues can reject it, and which
  adjacent candidates should be compared
- `pack`: emit a bounded packet for a capsule, small agent, orchestrator,
  workflow handoff, or evaluation fixture consumer

The packet is always weaker than the authored bundle. It should be used to
load the next source, not to replace it.

## Topology And DAG Boundary

`domain` and `kind` remain current frontmatter truth. Direct relations remain
frontmatter direct relation hints.

Family, capability, substrate, execution profile, risk posture, and tree
projection remain scout-only or projection-only. The Technique Intelligence DAG
is a navigation DAG over domains, kinds, family hints, techniques, and load
refs. It is not relation truth, graph inference, or composition order.

## Route Away

Stay in this repo when the object is one atomic technique move.

Leave when the object class changes:

- execution workflow: nearest workflow or agent-lane owner
- proof verdict: `aoa-evals`
- dispatch policy: `aoa-sdk`
- runtime behavior: `abyss-stack`
- role contract: `aoa-agents`
- scenario composition: `aoa-playbooks`
- graph semantics: `aoa-kag`
- ecosystem doctrine: `Agents-of-Abyss`

## Regeneration

Use [AGENTS](AGENTS.md#validation) for the current regeneration and validation
lane. Release-visible generated companion changes should also follow the root
release route.
