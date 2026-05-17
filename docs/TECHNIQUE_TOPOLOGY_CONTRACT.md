# Technique Topology Contract

This guide defines the classification topology for `aoa-techniques`.

Use it when the question is not only whether a candidate is one atomic
technique, but where it belongs in a corpus that must scale beyond hundreds or
thousands of entries. Use [Technique Tree Contract](TECHNIQUE_TREE_CONTRACT.md)
when the question is the authored `techniques/` path.

## Purpose

The technique corpus should become a large, navigable library of small agentic
moves, not a flat list and not five overloaded buckets.

The topology must support coding, documentation, validation, recovery, history, media, tool use,
dialogue, planning, observation, and other agent-capability surfaces. It must
also support `1000+` techniques, small-agent execution after orchestration
supplies context, and future consumers in skills, evals, routing, playbooks,
memory, KAG, agents, runtime, and stats without moving technique meaning out of
this repo.

## Topology Law

Classification is faceted, not a single tree. The authored directory tree is a
placement spine; it is not the whole classification model.

A technique is routed through distinct questions:

| Question | Axis |
|---|---|
| Which owner/review lane reads it first? | `domain` |
| What atomic move shape does it perform? | `kind` |
| Which stable semantic neighborhood does it join? | `family` |
| What agent capability does it exercise? | `capability_class` |
| What object or medium does it act on? | `substrate` |
| What agent or orchestration envelope can execute it? | `execution_profile` |
| What operational caution should route around it? | `risk_posture` |
| How does it compose, conflict, or sequence? | `relations` |

The first two axes are current frontmatter truth. Other axes are design
contracts and scout surfaces until intentionally promoted into schema,
generated catalogs, and validators.

## Axis Stack

| axis | current status | role | current or future source |
|---|---|---|---|
| `tree_path` | architecture contract | authored placement spine for trunks, shelves, and leaf bundles | `docs/TECHNIQUE_TREE_CONTRACT.md`, future projection |
| `domain` | authoritative frontmatter | first owner and review route | `docs/DOMAIN_MAP.md`, schema, validators |
| `kind` | authoritative frontmatter | atomic move shape | `docs/selection/TECHNIQUE_KIND_GUIDE.md`, `config/technique_kind_registry.yaml`, schema, validators |
| `family` | scout-only | stable semantic shelf spanning domains or kinds | `mechanics/distillation/parts/technique-reform-ingress/config/technique_family_scout.yaml`, `mechanics/distillation/parts/technique-reform-ingress/reports/technique_family_scout.md` |
| `capability_class` | design axis | what agent capability the move exercises | `mechanics/distillation/parts/technique-reform-ingress/config/technique_topology_axes.yaml`, future generated projection |
| `substrate` | design axis | what object or medium the move operates on | `mechanics/distillation/parts/technique-reform-ingress/config/technique_topology_axes.yaml`, future generated projection |
| `execution_profile` | design axis | what size or orchestration level can execute it | `mechanics/distillation/parts/technique-reform-ingress/config/technique_topology_axes.yaml`, future capsule/catalog field |
| `risk_posture` | design axis | mutation, public-share, safety, reversibility, and approval posture | `mechanics/distillation/parts/technique-reform-ingress/config/technique_topology_axes.yaml`, future review/catalog field |
| `relations` | current bounded frontmatter plus future strengthening | direct composition, conflict, sequence, prerequisite, or alternative hints | current `relations` plus future typed relation guidance |

## Current Axes

`domain` is the first owner and review route, not the whole category system.
Current domains are `agent-workflows`, `docs`, `evaluation`,
`system-recovery`, `validation-patterns`, and `history`.

`kind` names the atomic move shape. Current kinds are `workflow`, `guardrail`,
`validation`, `composition`, `distribution`, `artifact`, `lift`, `discovery`,
`handoff`, `ingest`, `assessment`, and `recovery`. The `kind` axis stays
singular; if several kinds feel necessary, narrow or split the candidate.

`family` is the future shelf layer. It groups nearby techniques that may cross
domains or kinds but belong to one durable semantic neighborhood. Current scout
examples include `instruction-surface`, `kag-source-lift`, `history-artifacts`,
`runtime-truth-lifecycle`, `handoff-continuation`, `media-ingest`,
`decision-routing`, `diagnosis-repair`, `automation-governance`, and
`antifragility-recovery`.

Family remains scout-only until the registry has clear ownership, examples, and
tie-break rules.

## Future Axes

The scout value registry for `capability_class`, `substrate`,
`execution_profile`, and `risk_posture` lives in
`mechanics/distillation/parts/technique-reform-ingress/config/technique_topology_axes.yaml`.

That registry names allowed scout values only. It does not add required
frontmatter fields, replace `domain` or `kind`, or authorize generated reports
to remap bundle meaning automatically.

The current generated readout is
`mechanics/distillation/parts/technique-reform-ingress/reports/technique_topology_scout.md`,
built by
`python mechanics/distillation/parts/technique-reform-ingress/scripts/build_topology_scout.py`.
Use it for review pressure before schema or frontmatter migration, not as a
source of technique meaning.

`capability_class` answers what the agent is doing: observe, read, interpret,
plan, choose, transform, write, mutate, validate, compare, summarize, compress,
handoff, recover, coordinate, communicate, or learn from artifact.

`substrate` answers what the move acts on: code, tests, docs, instructions,
config, shell, APIs, data, media, UI, conversation, history, memory-adjacent
artifacts, graph-adjacent artifacts, tool surfaces, runtime state, or human
approval surfaces.

`execution_profile` answers the execution envelope: `tiny-card`, `small-agent`,
`medium-agent`, or `orchestration-required`. This is not a quality score; it is
an estimate of what kind of context and outer workflow the technique needs.

`risk_posture` answers what can go wrong operationally: read-only, mutating,
public-share, security-sensitive, irreversible, approval-required,
degraded-mode, or external-evidence.

## Relation Topology

Direct `relations` already exist in frontmatter. They should remain bounded
links, not graph inference.

Future relation guidance should distinguish prerequisite, follows,
alternative, conflicts-with, strengthens, narrows, generalizes,
consumes-output-of, and produces-input-for. Relations should help orchestrators
compose techniques while preserving each technique as one atomic move.

## Growth Rules

- Keep the tree deliberate and browsable; use facets for selector detail.
- Promote axes through config, generated projections, tests, and review before
  requiring them in every bundle.
- Keep authored bundle meaning stronger than generated classifications.
- Do not let one domain become a junk drawer for many substrates.
- Do not use tags as a permanent substitute for missing topology.
- Do not let family become a hidden status or quality score.
- Treat topology changes as public contract changes that need tests and
  decision notes.

## Mechanics Interface

Mechanics should use this topology before promoting candidates.

Before a candidate becomes a technique bundle, mechanics should be able to name
the atomic move, likely domain, likely kind, likely family or no-family reason,
capability class, substrate, execution profile, risk posture, and nearest
related techniques or conflict seams.

If those cannot be named, keep the candidate in mechanics instead of promoting
it into canon.

## Next Honest Build Path

The next topology wave should not rewrite all existing bundles at once.

A bounded path is:

1. keep `domain` and `kind` authoritative
2. strengthen `family` from scout-only into a reviewed optional axis
3. add non-required generated projections for `capability_class`, `substrate`,
   `execution_profile`, and `risk_posture`
4. test the axes against distillation and mechanics candidates
5. promote only the axes that survive repeated review into schema/frontmatter

The goal is a corpus that can grow very large while staying navigable by both
large orchestrators and small executors.
