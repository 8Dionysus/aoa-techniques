# Technique Topology Contract

This guide defines the classification topology for `aoa-techniques`.

Use it when the question is not only whether a candidate is one atomic
technique, but where that technique should live in a corpus that must scale
beyond hundreds or thousands of entries.

## Purpose

The technique corpus should become a large, navigable library of small agentic
moves, not a flat list and not five overloaded buckets.

The topology must support:

- coding, documentation, validation, recovery, history, media, tool use,
  dialogue, planning, observation, and other agent-capability surfaces
- `1000+` techniques as an early scale target, not a ceiling
- small-agent execution after orchestration has selected and packed context
- future cross-repo consumers in skills, evals, routing, playbooks, memory, KAG,
  agents, runtime, and stats without moving technique meaning out of this repo

## Topology Law

Classification is faceted, not a single tree.

No one axis should carry all meaning. A technique is routed through several
orthogonal questions:

- What owner/review lane should read it first?
- What atomic move shape does it perform?
- Which stable semantic family does it belong to?
- What agent capability does it exercise?
- What substrate or object does it operate on?
- What execution profile can use it?
- What risk posture does it carry?
- What relations make it compose, conflict, or sequence with other techniques?

The first two axes are current frontmatter truth. Other axes are design
contracts and scout surfaces until they are intentionally promoted into schema,
generated catalogs, and validators.

## Axis Stack

| axis | current status | role | current or future source |
|---|---|---|---|
| `domain` | authoritative frontmatter | first owner and review route | `docs/DOMAIN_MAP.md`, schema, validators |
| `kind` | authoritative frontmatter | atomic move shape | `docs/TECHNIQUE_KIND_GUIDE.md`, `config/technique_kind_registry.yaml`, schema, validators |
| `family` | scout-only | stable semantic shelf spanning domains or kinds | `config/technique_family_seed.yaml`, `reports/technique_family_scout.md` |
| `capability_class` | design axis | what agent capability the move exercises | `config/technique_topology_axes.yaml`, future generated projection |
| `substrate` | design axis | what object or medium the move operates on | `config/technique_topology_axes.yaml`, future generated projection |
| `execution_profile` | design axis | what size or orchestration level can execute it | `config/technique_topology_axes.yaml`, future capsule/catalog field |
| `risk_posture` | design axis | mutation, public-share, safety, reversibility, and approval posture | `config/technique_topology_axes.yaml`, future review/catalog field |
| `relations` | current bounded frontmatter plus future strengthening | direct composition, conflict, sequence, prerequisite, or alternative hints | current `relations` plus future typed relation guidance |

## Current Axes

### Domain

`domain` is not the whole category system. It is the first owner and review
route for a technique.

The current domains are intentionally narrow:

- `agent-workflows`
- `docs`
- `evaluation`
- `system-recovery`
- `validation-patterns`
- `history`

Do not treat these six domains as a complete map of everything agents can do.
They are the current public corpus lanes. Future growth may need new domains or
subdomains, but adding one must happen through schema, template, validator, and
docs updates in the same wave.

### Kind

`kind` names the atomic move shape.

The current kinds are:

- `workflow`
- `guardrail`
- `validation`
- `composition`
- `distribution`
- `artifact`
- `lift`
- `discovery`
- `handoff`
- `ingest`
- `assessment`
- `recovery`

The `kind` axis should stay singular. If one technique seems to need several
kinds, narrow the atomic move or split the candidate.

### Family

`family` is the future shelf layer.

A family groups nearby techniques that may cross domains or kinds but belong to
one durable semantic neighborhood. The current family seed is scout-only because
the corpus is still small and forcing frontmatter migration too early would
create false precision.

The existing seed already points toward real shelves such as:

- `instruction-surface`
- `kag-source-lift`
- `history-artifacts`
- `runtime-truth-lifecycle`
- `handoff-continuation`
- `media-ingest`
- `decision-routing`
- `diagnosis-repair`
- `automation-governance`
- `antifragility-recovery`

Future promotion of `family` should make it a stable optional frontmatter field
only after the family registry has clear ownership, examples, and tie-break
rules.

## Future Axes

The scout value registry for `capability_class`, `substrate`,
`execution_profile`, and `risk_posture` lives in
`config/technique_topology_axes.yaml`.

That registry names allowed scout values only. It does not add required
frontmatter fields, does not replace `domain` or `kind`, and does not authorize
generated reports to remap bundle meaning automatically.

The current generated readout is `reports/technique_topology_scout.md`, built
by `python scripts/build_topology_scout.py`. Use it for review pressure before
schema or frontmatter migration, not as a source of technique meaning.

### Capability Class

`capability_class` should answer what the agent is doing at the capability
level.

Likely classes include:

- observe
- read
- interpret
- plan
- choose
- transform
- write
- mutate
- validate
- compare
- summarize
- compress
- handoff
- recover
- coordinate
- communicate
- learn-from-artifact

This axis is broader than `kind`. For example, a technique can be a `guardrail`
kind while exercising the `choose` capability, or a `lift` kind while exercising
the `compress` capability.

### Substrate

`substrate` should answer what the technique acts on.

Likely substrates include:

- code
- tests
- docs
- instructions
- config
- shell
- APIs
- data
- media
- UI
- conversation
- history
- memory-adjacent artifacts
- graph-adjacent artifacts
- tool surfaces
- runtime state
- human approval surfaces

This axis prevents `docs` and `agent-workflows` from becoming overloaded
catch-all domains.

### Execution Profile

`execution_profile` should answer what kind of agent can execute the technique
after selection.

Likely profiles include:

- `tiny-card`: executable from a capsule or one short section with obvious
  inputs
- `small-agent`: suitable for 2-4B models when the orchestrator supplies the
  local frame, facts, stop line, and output shape
- `medium-agent`: requires more local reasoning, comparison, or multi-file
  awareness but still stays one technique
- `orchestration-required`: the technique is atomic, but safe use requires an
  outer workflow, approval gate, or tool choreography

This is not a quality score. It describes the execution envelope.

### Risk Posture

`risk_posture` should answer what can go wrong operationally.

Likely values include:

- read-only
- mutating
- public-share
- security-sensitive
- irreversible
- approval-required
- degraded-mode
- external-evidence

This axis should route safety expectations without moving proof doctrine into
this repo.

## Relation Topology

Direct `relations` already exist in frontmatter. They should remain bounded
links, not graph inference.

Future relation guidance should distinguish at least:

- prerequisite
- follows
- alternative
- conflicts-with
- strengthens
- narrows
- generalizes
- consumes-output-of
- produces-input-for

Relations should help an orchestrator compose techniques while preserving the
fact that each technique remains one atomic move.

## Growth Rules

- Add new topology axes as config and generated projections before requiring
  them in every technique bundle.
- Keep authored bundle meaning stronger than generated classifications.
- Use scout reports for exploration, then promote axes only after repeated
  review shows stable value.
- Do not let one domain become a junk drawer for many substrates.
- Do not use tags as a substitute for missing topology forever.
- Do not let family become a hidden status or quality score.
- Treat topology changes as public contract changes that need tests and
  decision notes.

## Mechanics Interface

Mechanics should use this topology while distilling candidates.

Before a candidate becomes a technique bundle, mechanics should be able to name:

- the atomic move
- the likely domain
- the likely kind
- the likely family or reason no family is stable yet
- the capability class being exercised
- the substrate being acted on
- the execution profile target
- the risk posture
- nearest related techniques or conflict seams

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
