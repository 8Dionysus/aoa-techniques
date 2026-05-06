# Mechanics

`mechanics/` is the owner-local home where `aoa-techniques` participates in the
cross-project AoA mechanics. It keeps procedural movement around technique canon
out of the general docs pile without pretending those surfaces are already
published technique bundles.

The top-level package names follow the AoA mechanics vocabulary. Repo-local
concerns such as donor refinery, promotion readiness, adoption, mastery, and
stress live inside those cross-cutting mechanics instead of becoming unrelated
parallel axes.

[Owner Request Receipts](REQUEST_RECEIPTS.md) maps AoA center-side owner
requests that target `aoa-techniques` to local response surfaces. It is a
receipt route, not a copy of the AoA request queue and not proof of acceptance.

## Root Mechanics Files

The root of `mechanics/` is a dispatcher and organ route, not a second doctrine
store.

| File | Owns | Must not become |
|---|---|---|
| [`mechanics/AGENTS.md`](AGENTS.md) | local law for the mechanics tree, editing posture, validation, and closeout | package doctrine or technique bundle meaning |
| [`mechanics/README.md`](README.md) | this atlas, package map, package-card standard, and active/legacy split | a duplicate of package `README.md`, `PARTS.md`, `PROVENANCE.md`, or `LANDING_LOG.md` |
| [`mechanics/REQUEST_RECEIPTS.md`](REQUEST_RECEIPTS.md) | local receipt map for AoA center-side owner requests targeting this repo | request queue source, owner acceptance, or proof |

## Cross-Mechanics Map

- [method-growth](method-growth/README.md): technique adoption, technique-skill
  handoff, retention, obsolescence, and owner landing of reusable practice.
- [distillation](distillation/README.md): donor intake, external import,
  cross-layer candidate capture, long-gap re-entry, and candidate extraction.
- [audit](audit/README.md): promotion readiness, evidence sprinting, evidence
  ledgers, and canonical-pressure visibility.
- [growth-cycle](growth-cycle/README.md): mastery harvest, feat reflection,
  questbook integration, and reviewed closeout incubation.
- [questbook](questbook/README.md): repo-local durable technique obligations,
  quest source/index/projection posture, and harvest/promotion routing around
  canon hardening.
- [rpg](rpg/README.md): feat, progression, quest-overlay, and owner-handoff
  reflection that keeps RPG language adjunct to technique canon and owner
  truth.
- [agon](agon/README.md): Agon practice-candidate bridges, active parts,
  provenance, and preserved wave receipts.
- [recurrence](recurrence/README.md): recurrence observation and closure
  mechanics that feed technique review without becoming authority.
- [experience](experience/README.md): experience-mechanic governance,
  authority, service, scope, handoff, and decision surfaces.
- [release-support](release-support/README.md): installation and sovereign
  release support surfaces that remain bounded by owner consent.
- [antifragility](antifragility/README.md): stress, chaos, degraded-mode, and
  recovery-oriented practice routes.
- [checkpoint](checkpoint/README.md): phase handoff, handoff packet,
  compaction, re-entry, and checkpoint-bound repair pressure that stays
  candidate-only until a technique bundle owns the atomic move.
- [boundary-bridge](boundary-bridge/README.md): owner-boundary,
  derived-projection, and proof-claim practice pressure that keeps technique
  canon, generated surfaces, sibling owners, and public claims distinct.

## Boundary

Use `mechanics/` when a file describes how a practice candidate moves, matures,
gets reviewed, hands off, recurs, survives stress, or supports a release. Use
`docs/` when the file explains repository orientation, review doctrine,
generated-reader interpretation, or public selection guidance. Use
`techniques/` when the reusable practice unit is ready to stand as a bundle.

Mechanics can prepare canon. They do not replace canon.

Cross-repo references stay light: point to the owner, preserve provenance, and
keep AoA-only context outside the portable technique core.

Use root [`ROADMAP.md`](../ROADMAP.md) for repo-level technique-canon direction.
Use `mechanics/<slug>/ROADMAP.md` for package-local future pressure.

## Package Card Standard

Each `mechanics/<slug>/README.md` is an agent-operable local card. It should let
a reader answer when to use the mechanic, what this repository owns, which
stronger owners keep final truth, what may enter, what may leave, what must not
be claimed, how to validate the local route, and where to go next.

Use these headings in package READMEs:

| Heading | Purpose |
|---|---|
| `## Mechanic card` | compact package status and entry posture |
| `### Trigger` | when the local mechanic applies |
| `### Local owns` | what `aoa-techniques` may author here |
| `### Stronger owner split` | AoA center or sibling owners that keep stronger truth |
| `### Inputs` | material that may enter this mechanic |
| `### Outputs` | material that may leave without becoming canon by itself |
| `### Must not claim` | stop-lines that keep the package below stronger owners |
| `### Validation` | where to find exact checks for this package |
| `### Next route` | the next active surface, provenance bridge, or owner route |

This mirrors the AoA center mechanic-card shape, but adapts the authority. The
center can say what the center owns. This repository says what the local
technique-canon organ owns, then routes center law through
`REQUEST_RECEIPTS.md`, package `PROVENANCE.md`, or a sibling owner only when
that bridge is relevant.

## Package Roadmap Standard

Each `mechanics/<slug>/ROADMAP.md` should stay short enough for an agent to use
before editing. It should answer:

- current contour: what exists now and why it matters locally
- next work: which near-term moves are valid without widening authority
- when time comes: condition-based triggers for future depth
- out of scope or stop-lines: what the package must not claim
- update trigger: what kind of change should move the roadmap again

The package roadmap is not a landing log, raw ledger, proof verdict, hidden
backlog, package inventory, or substitute for the root roadmap. Update it when
future-facing package meaning moves. Leave checked landings in `LANDING_LOG.md`,
source lineage in `PROVENANCE.md` and `legacy/`, and repo-level direction in
root `ROADMAP.md`.

## Candidate Gate

Before a mechanics candidate becomes a technique bundle, it should pass the
atom and topology questions from [Technique Atom Contract](../docs/TECHNIQUE_ATOM_CONTRACT.md)
and [Technique Topology Contract](../docs/TECHNIQUE_TOPOLOGY_CONTRACT.md):

- one atomic move
- likely `domain` and primary `kind`
- likely family or reason no family is stable yet
- capability class, substrate, execution profile, and risk posture
- nearest related techniques, alternatives, or conflict points
- owner boundary, portable core, and stop line

If those cannot be named, keep the material in mechanics, legacy, or a
candidate ledger instead of drafting a broad technique bundle.

## Active And Legacy Split

When a mechanic has grown through waves, seeds, receipts, or candidate packets,
do not flatten every file into the package root. Build the package one mechanic
at a time:

- active behavior in `README.md`, `DIRECTION.md`, `PARTS.md`, and `parts/`
- provenance bridge in `PROVENANCE.md`
- checked landing history in `LANDING_LOG.md`
- source-to-active accounting in `legacy/INDEX.md` and
  `legacy/DISTILLATION_LOG.md`
- preserved source receipts in `legacy/raw/` when raw receipts exist; otherwise
  an explicit empty raw inventory in `legacy/raw/README.md`

Use the package card first, then open active parts. Enter legacy through
`PROVENANCE.md` only when the source route matters.
