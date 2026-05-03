# Mechanics Owner Request Receipts

This file is the `aoa-techniques` owner-local receipt map for AoA center-side
owner requests that target this repository.

It is not the AoA request queue, not the request-status vocabulary, and not
proof that a center request is accepted or landed. AoA owns the center-side
request grammar in `Agents-of-Abyss:mechanics/OWNER_REQUEST_PROTOCOL.md` and
the current queue in `Agents-of-Abyss:mechanics/OWNER_REQUEST_QUEUE.md`.

Use this file when a mechanics change in `aoa-techniques` carries an `ORQ-*`
request ID or claims to answer an AoA downstream request.

## Local Status Vocabulary

These statuses are local to this file. They do not change AoA queue status.

| Status | Meaning |
|---|---|
| `mapped` | The center request is named here and local route surfaces are identified, but no local acceptance or landing claim is made. |
| `mapped-with-local-evidence` | Existing local mechanics surfaces, bundle references, or validation routes appear to answer part of the request, but this file does not promote the AoA request to accepted or landed. |
| `candidate-only` | Local pressure exists only as a candidate lane, watch surface, or receipt; no technique bundle landing is claimed. |

## Direct AoA Requests

### `ORQ-METHOD-TECHNIQUES-001`

- Mechanic: `method-growth`
- Center queue: `requested`; center mechanic `landed`
- Local status: `mapped-with-local-evidence`
- Local response surface: [method-growth](method-growth/README.md),
  [Parts](method-growth/PARTS.md),
  [Pattern Adoption](method-growth/parts/pattern-adoption/README.md),
  [Adoption Boundaries](method-growth/parts/adoption-boundaries/README.md),
  [Technique To Skill Handoff](method-growth/parts/technique-to-skill-handoff/README.md),
  [Retention Checks](method-growth/parts/retention-checks/README.md), and
  [Obsolescence](method-growth/parts/obsolescence/README.md).
- Owner landing readout:
  - reusable-practice promotion lives in Pattern Adoption and Adoption
    Boundaries.
  - technique-to-skill movement lives in Technique To Skill Handoff without
    becoming skill acceptance.
  - retention and pruning posture lives in Retention Checks and Obsolescence.
  - technique canon lands only when a real `techniques/**/TECHNIQUE.md` bundle
    carries procedure, boundaries, examples, and canonical-readiness posture.
- Local proof or evidence route: normal technique review, and `aoa-evals` before
  public technique-quality claims.
- Stop-line: AoA center may request reusable practice promotion, but
  `aoa-techniques` owns reusable-practice canon and `aoa-skills` owns executable
  workflow meaning.

### `ORQ-DISTILLATION-TECHNIQUES-001`

- Mechanic: `distillation`
- Center queue: `requested`; center mechanic `landed`
- Local status: `mapped-with-local-evidence`
- Local response surface: [distillation](distillation/README.md),
  [Parts](distillation/PARTS.md),
  [Donor Refinery](distillation/parts/donor-refinery/README.md),
  [External Import Runbook](distillation/parts/external-import-runbook/README.md),
  and candidate ledgers.
- Owner landing readout:
  - source intake lives in Donor Refinery and External Import Runbook gates.
  - active extraction lives in the external and cross-layer candidate ledgers.
  - noise pruning lives in donor exclusions, overlap holds, layer-incubation
    lanes, and not-technique-shaped verdicts.
  - provenance-preserving condensation lives in [Provenance](distillation/PROVENANCE.md),
    `legacy/raw/` receipts, and [Landing Log](distillation/LANDING_LOG.md).
  - technique canon lands only when a real `techniques/**/TECHNIQUE.md` bundle
    carries the reusable practice.
- Local proof or evidence route: [Landing Log](distillation/LANDING_LOG.md),
  part-local registries, part-local validators, and any landed
  `techniques/**/TECHNIQUE.md` bundle refs.
- Stop-line: Distillation can intake, narrow, hold, or route source pressure.
  Only technique bundles own reusable practice canon, and public quality claims
  still route to `aoa-evals`.

### `ORQ-EXPERIENCE-TECHNIQUES-001`

- Mechanic: `experience`
- Center queue: `requested`; center mechanic `planted`
- Local status: `mapped-with-local-evidence`
- Local response surface: [experience](experience/README.md),
  [Parts](experience/PARTS.md),
  [Governance Precedent](experience/parts/governance-precedent/README.md),
  [Authority Resolution](experience/parts/authority-resolution/README.md),
  [Appeal Reasoning](experience/parts/appeal-reasoning/README.md),
  [Sealed Decision](experience/parts/sealed-decision/README.md),
  [Scope Boundary](experience/parts/scope-boundary/README.md),
  [Handoff Compression](experience/parts/handoff-compression/README.md), and
  [Service Clarity](experience/parts/service-clarity/README.md).
- Owner landing readout:
  - governance and appeal practice live in Governance Precedent, Authority
    Resolution, Appeal Reasoning, and Sealed Decision.
  - office/service practice lives in Scope Boundary, Handoff Compression, and
    Service Clarity.
  - portable practice stops before live office activation, release approval,
    assistant self-authority, runtime truth, and ToS write authority.
  - technique canon lands only when a real `techniques/**/TECHNIQUE.md` bundle
    carries the reusable practice.
- Local proof or evidence route: owner-local technique review or reviewed owner
  receipts before any public usefulness claim.
- Stop-line: Experience technique notes must not carry live office authority,
  release approval, runtime truth, or Tree-of-Sophia write authority.

## Non-ORQ Center Pressure

Some local mechanics receive center pressure through wave receipts, provenance,
or candidate lanes without a direct AoA owner-request ID targeting
`aoa-techniques`.

### [agon](agon/README.md)

- Current status: `candidate-only`
- Why it stays separate: the current AoA Agon request queue has no direct
  `ORQ-AGON-TECHNIQUES-*` request. Local Agon surfaces preserve Wave IV and Wave
  XV technique-side pressure as requested-only practice candidates, not
  owner-request acceptance.

### [antifragility](antifragility/README.md)

- Current status: `candidate-only`
- Why it stays separate: the current AoA Antifragility request queue has no
  direct `ORQ-ANTIFRAGILITY-TECHNIQUES-*` request. Local Antifragility surfaces
  preserve bounded chaos, degraded-mode, regrounding, and recovery practice
  pressure without claiming center request acceptance, one-score health, proof
  verdicts, owner-local cleanup authority, runtime self-healing, or automatic
  technique promotion. Existing antifragility-recovery technique bundles remain
  canonical only through their `techniques/**/TECHNIQUE.md` homes.

### [boundary-bridge](boundary-bridge/README.md)

- Current status: `candidate-only`
- Why it stays separate: the current AoA Boundary Bridge owner-request queue
  has no direct `ORQ-BRIDGE-TECHNIQUES-*` request. Local Boundary-bridge
  surfaces preserve owner-boundary, derived-projection, and proof-claim
  practice pressure without claiming owner acceptance, identity between bridged
  surfaces, AoA-authored Tree-of-Sophia canon, source interpretation, derived
  projection as source truth, routing authority, SDK authority, memory
  authority, runtime authority, public projection authority, proof before
  `aoa-evals` or the source owner lands evidence, generated companion
  authority, or automatic technique promotion. Existing boundary-related
  technique bundles remain canonical only through their
  `techniques/**/TECHNIQUE.md` homes.

### [checkpoint](checkpoint/README.md)

- Current status: `candidate-only`
- Why it stays separate: the current AoA Checkpoint owner-request queue has no
  direct `ORQ-CHECKPOINT-TECHNIQUES-*` request. Local Checkpoint surfaces
  preserve phase handoff, handoff packet, compaction/re-entry, and
  checkpoint-bound repair pressure without claiming checkpoint implementation
  authority, memory canon, proof verdicts, runtime activation, owner
  acceptance, hidden scheduler behavior, autonomous self-repair, or automatic
  technique promotion. Existing checkpoint-related technique bundles remain
  canonical only through their `techniques/**/TECHNIQUE.md` homes.

### [growth-cycle](growth-cycle/README.md)

- Current status: `candidate-only`
- Why it stays separate: the current AoA Growth Cycle request queue has no
  direct `ORQ-GROWTHCYCLE-TECHNIQUES-*` request. Local Growth-cycle surfaces
  preserve technique-layer harvest, feat-reader, questbook, and
  promotion-readiness pressure without claiming center request acceptance.

### [questbook](questbook/README.md)

- Current status: `candidate-only`
- Why it stays separate: the current AoA Questbook owner-request queue has no
  direct `ORQ-QUESTBOOK-TECHNIQUES-*` request. Local Questbook surfaces
  preserve repo-local durable technique obligations, source quest files,
  generated quest projections, and harvest/promotion pressure without claiming
  a second roadmap, private scratchpad, raw donor backlog, owner acceptance,
  closure proof, proof verdicts, playbook choreography, memory canon, routing
  authority, generated quest views as source truth, RPG playable reading
  authority, or automatic technique promotion. Existing quest-related
  technique bundles remain canonical only through their
  `techniques/**/TECHNIQUE.md` homes.

### [recurrence](recurrence/README.md)

- Current status: `candidate-only`
- Why it stays separate: the current AoA Recurrence request queue has no direct
  `ORQ-RECURRENCE-TECHNIQUES-*` request. Local Recurrence surfaces preserve
  technique-layer observation and review-closure pressure without claiming
  center request acceptance, recurrence law ownership, runtime return, memory
  recall, routing dispatch, proof verdicts, or automatic technique promotion.

### [release-support](release-support/README.md)

- Current status: `candidate-only`
- Why it stays separate: the current AoA Release-support request queue has no
  direct `ORQ-RELEASE-TECHNIQUES-*` request. Local Release-support surfaces
  preserve installation and sovereign-release practice pressure without
  claiming center request acceptance, release authority, public-claim proof,
  operator consent, runtime rollback, sibling acceptance, or automatic
  technique promotion.

## Update Discipline

When AoA adds, supersedes, or lands an owner request targeting
`aoa-techniques`:

1. Read the AoA request packet and package-local `OWNER_REQUESTS.md`.
2. Add or update only the matching row here.
3. Link the local response surface that can actually be reviewed in this repo.
4. Keep generated indexes, ledgers, and compact companions as evidence only.
5. Do not mark a local landing unless the local owner surface and proof route are
   already present.
