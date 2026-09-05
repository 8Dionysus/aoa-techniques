# AGENTS.md

## Applies to

This card applies repository-wide; the nearest nested `AGENTS.md` supplies the
local delta for a touched path.

## Role

`aoa-techniques` is AoA's public practice canon: reusable, sanitized, bounded,
reviewable engineering methods that also work as a standalone public library.
A technique is an atomic executable move, small enough to adapt after an
orchestrator supplies context. It is not a skill bundle, proof surface,
questline, agent identity, or private project runbook.

This repository owns technique IDs, meaning, contracts, adaptation notes,
public-safe wording, topology, provenance, generated catalogs and readers, and
owner-local measurement over that canon. `domain` and `kind` are current
frontmatter truth; family, capability, substrate, execution profile, risk, and
relations remain explicit design axes rather than an undifferentiated tag set.

Skill workflows, proof doctrine, routing, roles, memory, playbooks, KAG
substrate, cross-owner statistics, and private runtime operations stay with
their owners.

## Skill-home boundary

This repository currently owns no local skill bundle. Do not create an empty
top-level `skills/` port or copy shared bundles into `.agents/skills/`.
Discovery starts from authored routes and `TECHNIQUE.md` bundles; derived
readers must return to them.

A future local skill requires a concrete capability with a distinct trigger,
input/output contract, composition value, failure boundary, and repeatable
benefit in no-skill and coexistence trials. A technique-to-skill idea remains a
proposal until the receiving owner accepts it; proposal, activation, and
projection are separate events.

## Read before editing

Read the root card first, then only the stronger source needed by the task.
Use [README](README.md) only when the task needs the public overview.

| Need | First owner surface |
|---|---|
| public first reading | only when public orientation is needed, [README](README.md), then [START_HERE](docs/START_HERE.md) |
| author or split one technique | [TECHNIQUE_ATOM_CONTRACT](docs/TECHNIQUE_ATOM_CONTRACT.md), then the target bundle |
| tree/topology change | [TECHNIQUE_TREE_CONTRACT](docs/TECHNIQUE_TREE_CONTRACT.md), then [TECHNIQUE_TOPOLOGY_CONTRACT](docs/TECHNIQUE_TOPOLOGY_CONTRACT.md) |
| root-file placement | [ROOT_SURFACE_LAW](docs/ROOT_SURFACE_LAW.md) |
| agent-card form or mesh | [DESIGN.AGENTS](DESIGN.AGENTS.md), then the nearest card |
| repo-wide historical provenance | only when historical evidence matters, [retirement decision](docs/decisions/AOA-TECH-D-0077-retire-spark-and-legacy-surfaces.md) |
| direction or future trigger | [ROADMAP](ROADMAP.md) |
| mechanic package or part | nearest `mechanics/**/AGENTS.md`; only when an atlas is needed, [Mechanics](mechanics/README.md) |
| generated parity | authored source, builder, generated output, then validator |
| owner-local measurement | [Stats](stats/AGENTS.md), then its source and consumer |

## Boundaries

- Root owns identity, boundaries, route choice, and claim limits. Nested cards
  own only local risk, stronger sources, stop-lines, and validation routing.
- Authored techniques and contracts define meaning. Generated catalogs,
  capsules, source-lift outputs, mesh mirrors, exports, and stats packets are
  derived evidence or navigation.
- Do not turn a technique into a skill, eval, route, playbook, memory object,
  role contract, runtime behavior, or ToS source.
- Do not publish secrets, project-private residue, unreduced transcripts, or
  machine-local assumptions as portable practice.
- Do not add root or docs-root surfaces without the root law, or infer quality,
  adoption, runtime use, or promotion from a local statistics packet.
- Route away when the object is a multi-step workflow rather than one reusable
  move, belongs to another owner class, or is philosophy without an operational
  method.

For recall or continuity, use `aoa-memo`; raw session grounding stays in
`.aoa`, local proposals use the repository memo port when present, and durable
reviewed memory lands through its owner.

## Decisions and propagation

After a route, topology, source-authority, validator, public-contract, or owner
change, use [decision guidance](docs/decisions/AGENTS.md) to determine whether future agents need
the rationale. Update only the roadmap, changelog, design, generated
companions, mechanic ledgers, quest surfaces, or neighboring owner routes whose
meaning actually changed. Historical detail stays at the exact Git commit and
original path recorded by the owning PROVENANCE surface or retirement
decision, not in active root guidance.

## Validation

Select the narrowest route in [VALIDATION](VALIDATION.md) after the evidence
class and touched path are known. Exact reusable sequences remain authoritative
in [validation_lanes.json](config/validation_lanes.json); `VALIDATION.md`, the
lane runner, release stabilizer, and part-local validation surfaces expose
on-demand procedure.

## Closeout

Report changed owner sources, validation lanes and focused checks, generated
parity, skipped routes, external blockers, remaining risk, decision review,
and the next owner. Keep local validation, CI, review, merge, publication,
runtime use, adoption, and owner acceptance as separate claims.
