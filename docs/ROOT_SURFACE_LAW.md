# Root Surface Law

This document decides what may live in the root of `aoa-techniques` and what
may stay flat under `docs/`.

The root is not a warehouse for every useful note. It is the public front of the
technique canon: a small set of surfaces that let humans, agents, contributors,
validators, and downstream consumers orient before entering `docs/`,
`mechanics/`, `techniques/`, or generated outputs.

## Root Principle

A root surface is allowed only when it serves at least one durable role:

1. **Public entry**: it introduces the repository and routes new readers.
2. **Canon authority**: it names the repository boundary, corpus map, direction,
   or public obligation posture.
3. **Public governance**: GitHub or contributors expect it at root.
4. **Thin public example or index**: it routes to deeper source-owned material
   without duplicating that material.
5. **Agent lane**: it gives agents a stable route card.
6. **Tooling or machine district**: it is a top-level directory expected by
   tooling, builders, validators, or source layout.

A surface that is historical, mechanic-local, generated, experimental,
future-looking, raw donor material, or interesting only because it was created
during a package should not sit at root by default.

## Docs-Root Principle

`docs/` root is for current repo doctrine, route contracts, reader maps, and
guide surfaces that are still active across the technique canon.

Historical receipts, audit baselines, mechanic-specific raw records, movement
traces, and durable rationale need named homes:

- `docs/decisions/` for why a structural or workflow choice was made
- `mechanics/<slug>/legacy/` for preserved mechanic lineage
- `mechanics/<slug>/legacy/raw/` for raw receipts and pre-prune evidence
- `mechanics/<slug>/parts/` for current mechanic-owned operating surfaces
- `generated/` for reproducible derived outputs

Flat docs files should be current enough to guide a future change. If a file is
only evidence of how a past change happened, it belongs in a decision, trace, or
legacy route.

## Allowed Root Surfaces

| Class | Allowed examples | Why root is justified | Guardrail |
|---|---|---|---|
| Public entry and authority | `README.md`, `CHARTER.md` | they define the public door and repository authority boundary | stay compact and route to stronger contracts |
| Corpus map and direction | `TECHNIQUE_INDEX.md`, `ROADMAP.md`, `QUESTBOOK.md` | they expose current corpus shape, direction, and durable obligations | do not become generated manifests, audit ledgers, or changelog copies |
| Public governance and legal | `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `LICENSE` | contributors and platforms expect them at root | do not become technique doctrine catalogs |
| Release history | `CHANGELOG.md` | release history belongs at root for public readers | do not store future direction or audit baselines here |
| Thin example | `WALKTHROUGH.md` | one first example helps readers understand the canon path | stay one example; move broader tutorials into docs or examples |
| Agent lane | `AGENTS.md`, `.agents/` | agent-facing route cards need stable local entry | do not replace civic docs or owner contracts |
| Tooling and machine districts | `.github/`, `config/`, `data/`, `docs/`, `examples/`, `generated/`, `incoming/`, `mechanics/`, `quests/`, `reports/`, `schemas/`, `scripts/`, `templates/`, `tests/`, `techniques/` | source layout and tooling expect stable directories | each active district should keep local route guidance when needed |
| Development requirements | `.gitignore`, `requirements-dev.txt` | development hygiene | stay technical and small |

## Surfaces That Should Not Live In Root

| Surface kind | Better home | Reason |
|---|---|---|
| Deep audit baseline, closure packet, or searched-lane ledger | `mechanics/audit/legacy/raw/` plus `mechanics/audit/PROVENANCE.md` | audit evidence is useful, but root direction should stay live and compact |
| Mechanic runbook or part-local operating surface | `mechanics/<slug>/parts/<part>/README.md` | current mechanic behavior belongs with its package and part |
| Mechanic landing history | `mechanics/<slug>/LANDING_LOG.md` | landings are checked history, not root direction |
| Donor intake notes, raw external records, or pre-prune candidate lists | `mechanics/distillation/legacy/raw/` or the owning candidate ledger | donor evidence should be inspectable without becoming canon |
| Generated catalog, capsule, or projection | `generated/` | generated surfaces are reproducible companions, not authored root truth |
| Technique meaning | `techniques/**/TECHNIQUE.md` | root may route to technique meaning but must not re-author it |
| Decision rationale | `docs/decisions/` | decisions explain why; current source docs define what |
| Local scratchpad or private operation note | untracked local notes or the owning private repo | public root must remain sanitized and reusable |
| Sibling-repo implementation truth | the owning AoA repository | `aoa-techniques` routes to owners; it does not absorb their object classes |

## Decision Procedure Before Adding A Root File

Ask these questions in order:

1. Does the file define public entry, canon authority, corpus direction,
   obligation posture, public governance, a thin example, agent entry, or a
   required tooling district?
2. Would a human or small agent make a safer first decision because this file is
   visible before entering `docs/`, `mechanics/`, or `techniques/`?
3. Does a generated, mechanic, quest, decision, trace, technique, or owner-local
   home already fit better?
4. Can the file stay compact over time without becoming a duplicate of a
   stronger source?
5. Can validation or generated parity keep the surface discoverable without
   turning it into authority?

If the answer to question 3 is yes, do not place the file at root. If the file
cannot stay compact, route it to the owner surface that can carry the detail.

## Current Root Decisions

| Surface | Decision | Why |
|---|---|---|
| `CHARTER.md` | add | the practice canon needs a root authority boundary distinct from README and AGENTS |
| `README.md` | keep and slim toward public front door | it should introduce and route, not index every active detail |
| `ROADMAP.md` | keep as live direction | historical closure audit detail belongs to Audit legacy, while root roadmap owns horizons and update rules |
| previous closure-audit `ROADMAP.md` | move to `mechanics/audit/legacy/raw/ROOT_CLOSURE_AUDIT_ROADMAP_2026-05-03.md` | preserves the evidence without making old audit detail the live direction surface |
| `QUESTBOOK.md` | keep as root obligation index | it is useful only while it stays a compact index, not a second roadmap |
| `TECHNIQUE_INDEX.md` | keep | public corpus map by ID, status, domain, and summary is root-worthy |
| `WALKTHROUGH.md` | keep for now as one thin example | broader examples should move into `docs/` or `examples/` if this grows |
| `AGENTS.md` | keep as agent route card | agent route law complements, but does not replace, public canon docs |

## Final Rule

The root is healthy when every file there can explain why it is visible before
the reader enters a district.

The docs root is healthy when every flat docs file can explain why it is current
doctrine or route guidance rather than historical evidence, generated output,
mechanic-local detail, or raw lineage.
