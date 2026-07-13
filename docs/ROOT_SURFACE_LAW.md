# Root Surface Law

This document decides what may live in the root of `aoa-techniques` and what
may stay flat under [docs](./).

The root is the public front of the technique canon. It should help humans,
agents, contributors, validators, and downstream consumers orient before they
enter [docs](./), [mechanics](../mechanics/), [techniques](../techniques/), or
[generated](../generated/).

## Root Principle

A root surface is allowed only when it serves a durable role:

1. public entry or route orientation
2. canon authority, corpus map, direction, or obligation posture
3. public governance expected by GitHub or contributors
4. agent lane entry
5. tooling or machine district required by source layout
6. public-safe provenance district for repo-wide raw, archive, or receipts

Historical evidence, mechanic-local operation, generated output, experiments,
raw donor material, and package-era scratch surfaces do not sit at root by
default.

## Docs-Root Principle

[docs](./) root is for current repo doctrine, route contracts, reader maps, and
guide surfaces that are active across the technique canon.

Use named homes for everything else:

| Role | Home |
|---|---|
| durable rationale | [decisions](decisions/) |
| repo-wide public-safe raw, archive, and receipts | [legacy](../legacy/) |
| mechanic lineage or part operation | [mechanics](../mechanics/) |
| generated JSON | [generated](../generated/) |
| active review contracts | [review](review/) |
| active selection, kind, handoff, and capsule contracts | [selection](selection/) |
| active KAG/source-lift contracts | [source-lift](source-lift/) |
| active validation lane topology and command authority | [validation](validation/) |
| generated Markdown readers | [readers](readers/) |

Flat docs files should guide a future change. If a file only explains how a
past change happened, route it to decisions, legacy, or the owning mechanic
evidence trail.

## Allowed Root Surfaces

| Class | Allowed examples | Guardrail |
|---|---|---|
| Public entry and authority | [README](../README.md), [CHARTER](../CHARTER.md), [DESIGN](../DESIGN.md), [DESIGN.AGENTS](../DESIGN.AGENTS.md) | stay compact and route to stronger contracts |
| Corpus map and direction | [TECHNIQUE_INDEX](../TECHNIQUE_INDEX.md), [ROADMAP](../ROADMAP.md), [QUESTBOOK](../QUESTBOOK.md) | do not become generated manifests, audit ledgers, or changelog copies |
| Public governance and legal | [CONTRIBUTING](../CONTRIBUTING.md), [CODE_OF_CONDUCT](../CODE_OF_CONDUCT.md), [SECURITY](../SECURITY.md), [LICENSE](../LICENSE) | do not become technique doctrine catalogs |
| Release history | [CHANGELOG](../CHANGELOG.md) | record release history, not future direction |
| Agent lane | [AGENTS](../AGENTS.md), [.agents](../.agents/), [agents mesh config](../config/agents_mesh.json), [agents mesh mirror](../generated/agents_mesh.min.json), [AGENTS_MESH_PROTOCOL](guardrails/AGENTS_MESH_PROTOCOL.md) | route agents without replacing public docs or owner contracts |
| Tooling, provenance, and machine districts | [.github](../.github/), [config](../config/), [docs](./), [evals](../evals/), [examples](../examples/), [generated](../generated/), [kag](../kag/), [legacy](../legacy/), [mechanics](../mechanics/), [quests](../quests/), [schemas](../schemas/), [scripts](../scripts/), [stats](../stats/), [templates](../templates/), [tests](../tests/), [techniques](../techniques/) | keep local route guidance where needed |
| Development requirements | [.gitignore](../.gitignore), [requirements-dev.txt](../requirements-dev.txt) | stay technical and small |

## Surfaces That Should Not Live In Root

| Surface kind | Better home | Reason |
|---|---|---|
| Audit baselines, closure packets, or searched-lane ledgers | [Audit raw legacy](../mechanics/audit/legacy/raw/) plus [Audit provenance](../mechanics/audit/PROVENANCE.md) | evidence is useful; root direction should stay live |
| Repo-wide pre-migration receipts or retired tail surfaces | [legacy/raw](../legacy/raw/), [legacy/archive](../legacy/archive/), [legacy/receipts](../legacy/receipts/) | history stays auditable without becoming active canon |
| Mechanic runbooks, reports, configs, scripts, schemas, examples, manifests, or tests | owning `mechanics/<slug>/parts/<part>/` district | one-owner operating surfaces belong beside their mechanic |
| Root catch-all data district without active repo-wide payload | strongest owner home, or a decision-backed new root district | an empty `data/` shelf attracts misplaced mechanic-local or generated material |
| Agent-lane packet or swarm recipe | `.agents/<lane>/`, including `.agents/spark/` | agent-lane packet guidance belongs under the agent district |
| Donor intake notes, raw external records, or candidate lists | [Distillation candidate intake](../mechanics/distillation/parts/candidate-intake/README.md), another owning Distillation part, or root [legacy/raw](../legacy/raw/) only for repo-wide preservation | donor evidence should not become canon or a second incoming queue |
| Generated catalogs, capsules, projections, or readers | [generated](../generated/) or [readers](readers/) as appropriate | generated surfaces are reproducible companions, not authored truth |
| Technique meaning | [techniques](../techniques/) | root routes to meaning; it does not re-author it |
| Local scratchpads or private operation notes | untracked local notes or the owning private repo | public root must stay sanitized and reusable |
| Sibling-repo implementation truth | the owning AoA repository | this repo routes to owners; it does not absorb their object classes |

## Decision Procedure Before Adding A Root File

Ask these questions in order:

1. Does the file define public entry, canon authority, corpus direction,
   obligation posture, public governance, agent entry, a thin example, or a
   required tooling district?
2. Would a human or small agent make a safer first decision because the file is
   visible before entering [docs](./), [mechanics](../mechanics/), or
   [techniques](../techniques/)?
3. Does a generated, mechanic, quest, decision, trace, technique, or owner-local
   home already fit better?
4. Can the file stay compact without duplicating a stronger source?
5. Can validation or generated parity keep it discoverable without making it
   authority?

If question 3 is yes, do not place the file at root. If the file cannot stay
compact, route it to the owner surface that can carry the detail.

## Current Root Decisions

| Decision | Current rule |
|---|---|
| Public front door | [README](../README.md) stays compact and hands off to stronger docs; it does not duplicate validation commands, GitHub-native legal/governance tabs, generated readers, or mechanic runbooks. |
| Authority and design | [CHARTER](../CHARTER.md), [DESIGN](../DESIGN.md), and [DESIGN.AGENTS](../DESIGN.AGENTS.md) stay root because they define boundary, system form, and agent-surface form. |
| Corpus direction | [TECHNIQUE_INDEX](../TECHNIQUE_INDEX.md), [ROADMAP](../ROADMAP.md), and [QUESTBOOK](../QUESTBOOK.md) stay root only while they remain compact route/status surfaces. |
| Docs districts | [guardrails](guardrails/), [review](review/), [selection](selection/), [source-lift](source-lift/), [validation](validation/), and [readers](readers/) keep flat docs from turning into a maze. |
| Provenance | [legacy](../legacy/) is the repo-wide public-safe provenance district; active mechanic lineage stays mechanic-local. |
| Mechanics artifacts | Reports, scout inputs, overlays, scripts, manifests, schemas, examples, and tests that serve one mechanic part live with that part. |
| Local KAG provider | [kag](../kag/) carries the repo-local provider packet, source-return handles, and validation receipts for downstream KAG consumers. |
| Local stats port | [stats](../stats/) carries owner-defined technique-canon questions, measurement contracts, and public reference packets; cross-owner grammar and aggregation remain with `aoa-stats`. |
| Root data | Empty root `data/` is retired until a concrete repo-wide data contract justifies it. |
| Spark lane | The previous root Spark surface lives under [.agents/spark](../.agents/spark/) as an agent-lane packet, not a standalone public root district. |

## Final Rule

The root is healthy when every file there can explain why it is visible before
the reader enters a district.

The docs root is healthy when every flat docs file can explain why it is current
doctrine or route guidance rather than historical evidence, generated output,
mechanic-local detail, or raw lineage.
