# Bundle Anatomy Corpus Synthesis

Source packet: [Technique Reform Ingress](../README.md)

Baseline packet: [Bundle Anatomy Baseline Inventory](bundle-anatomy-baseline-inventory.md)

Rubric packet: [Bundle Anatomy Rubric Hardening](bundle-anatomy-rubric-hardening.md)

Audit waves:

- [Bundle Anatomy Wave A Review](bundle-anatomy-wave-a-review.md)
- [Bundle Anatomy Wave B Review](bundle-anatomy-wave-b-review.md)
- [Bundle Anatomy Wave C Review](bundle-anatomy-wave-c-review.md)

Status: corpus-synthesis, no leaf repair, not path movement, not frontmatter
migration, not status promotion.

## Verdict

The first full post-tree bundle anatomy pass reviewed all `107` current
technique bundles.

The corpus is structurally healthier than expected after the tree migration:

- `107/107` bundles have path parity with the generated tree projection.
- `107/107` bundles have catalog and capsule presence.
- `107/107` bundles have examples, checks, and notes present.
- `107/107` bundles pass direct anatomy review.
- `105/107` bundles require no immediate repair.
- `2/107` bundles need generated-reader capsule follow-through.
- `0/107` bundles currently need route-away, split, merge, deprecation, path
  movement, frontmatter migration, or broad template rewrite from this audit.

The first repair cohort should be the smallest concrete gap:

- `AOA-T-0095`
- `AOA-T-0096`

Both are coherent in authored source, but their generated capsule shorts are
awkward around wrapped source bullets. The next stage should inspect the
capsule extraction path and decide whether to repair source line shaping,
builder extraction, or both.

## Label Counts

| label | bundles |
|---|---:|
| `anatomy-pass` | 107 |
| `old-template-watch` | 107 |
| `owner-boundary-watch` | 95 |
| `promotion-evidence-hold` | 82 |
| `portability-watch` | 43 |
| `capsule-gap` | 2 |

## Repair Action Counts

| repair action | bundles |
|---|---:|
| `no-repair` | 105 |
| `capsule-source-or-builder-review` | 2 |

## Corpus Shape

### Trunks

| trunk | bundles |
|---|---:|
| `continuity` | 14 |
| `execution` | 14 |
| `governance` | 14 |
| `history` | 6 |
| `ingest` | 5 |
| `instruction` | 19 |
| `knowledge-lift` | 8 |
| `proof` | 18 |
| `recovery` | 8 |
| `tool-use` | 1 |

### Status

| status | bundles |
|---|---:|
| `canonical` | 25 |
| `promoted` | 82 |

### Domain

| domain | bundles |
|---|---:|
| `agent-workflows` | 57 |
| `docs` | 28 |
| `evaluation` | 12 |
| `history` | 6 |
| `system-recovery` | 3 |
| `validation-patterns` | 1 |

### Kind

| kind | bundles |
|---|---:|
| `artifact` | 14 |
| `assessment` | 10 |
| `composition` | 7 |
| `discovery` | 2 |
| `distribution` | 4 |
| `guardrail` | 13 |
| `handoff` | 11 |
| `ingest` | 5 |
| `lift` | 12 |
| `recovery` | 6 |
| `validation` | 10 |
| `workflow` | 13 |

## Watch Pressure By Trunk

| trunk | owner boundary | portability | promotion hold | capsule gap |
|---|---:|---:|---:|---:|
| `continuity` | 14 | 12 | 14 | 0 |
| `execution` | 6 | 3 | 8 | 0 |
| `governance` | 14 | 4 | 14 | 0 |
| `history` | 6 | 6 | 4 | 0 |
| `ingest` | 5 | 5 | 5 | 0 |
| `instruction` | 15 | 0 | 14 | 0 |
| `knowledge-lift` | 8 | 3 | 5 | 0 |
| `proof` | 18 | 4 | 9 | 2 |
| `recovery` | 8 | 5 | 8 | 0 |
| `tool-use` | 1 | 1 | 1 | 0 |

## Cohorts

### No-Touch Healthy Cohort

`105` bundles are healthy for this phase. They should not be rewritten merely
because their headings predate the newest template shape.

Carry `old-template-watch` as a modernization note only. It becomes actionable
when a target bundle already needs nearby edits, when small-agent usability
actually fails, or when a later template migration is planned with its own
source contract and validation path.

### Generated-Reader Repair Cohort

`AOA-T-0095` and `AOA-T-0096` form the first repair cohort.

Current evidence:

- `AOA-T-0095` capsule validation includes `before the;`.
- `AOA-T-0096` capsule risk ends with `older or.`
- Both source techniques are coherent when read directly.
- Both defects appear at wrapped source bullets.

Next stage:

1. Inspect capsule builder extraction for wrapped list items.
2. Inspect source line shaping for both affected bullets.
3. Choose the smaller durable repair.
4. Rebuild generated capsule surfaces if the builder or source changes require
   it.
5. Run repo validation and release check if generated public-reader surfaces
   move.

### Decision-Needed Cohort

No corpus-wide decision record is required from anatomy findings alone.

The audit did not move contracts, owner authority, path architecture, schema,
frontmatter truth, or generated-source authority. A decision note may become
appropriate only if the capsule repair changes builder behavior or if a later
template modernization changes authoring expectations.

### Route-Away Cohort

No bundle is routed away by this pass.

Many bundles sit near stronger owners, but direct reading shows they stay
portable technique atoms. `owner-boundary-watch` is therefore a caution label,
not a removal or migration verdict.

### Topology And Frontmatter Cohort

No `domain`, `kind`, path, or future topology axis change is justified from
this pass.

Future axes such as family, capability, substrate, execution profile, risk
posture, and relation topology should remain design notes until the project
opens a separate schema or generated-reader program.

## Findings

### The Tree Migration Did Not Hide A Broad Bundle Collapse

The tree produced a more legible corpus without forcing broad path churn,
frontmatter churn, or mass leaf repair. The anatomy pass confirms that the
current tree is a useful root for scaling toward hundreds and then thousands of
atomic techniques.

### Old Template Shape Is Real But Not Urgent

All `107` reviewed bundles predate explicit `Atomic move` and `Small-agent
execution shape` headings, but direct reading found the atomic center
recoverable from intent, core procedure, risks, validation, examples, checks,
notes, and capsule text.

Do not convert `old-template-watch` into mass rewriting. That would create
noise and risk without evidence.

### Boundary Pressure Is The Normal State Of A Portable Technique Organ

`95` bundles carry `owner-boundary-watch`, mostly because technique atoms often
sit next to stronger organs: skills, evals, routing, memory, playbooks, agents,
KAG, runtime, and AoA center law.

This is compatible with the repo vision: `aoa-techniques` must be portable on
its own while still able to plug into OS Abyss. The correct shape is a bounded
bridge, not imported authority.

### First Repair Should Be Narrow And Concrete

The first repair should not be a grand re-template. It should repair the only
specific broken reader evidence found by the audit: the two capsule shorts in
`AOA-T-0095` and `AOA-T-0096`.

## Stop Lines

- Do not rewrite all old-template bundles.
- Do not add future topology axes to required frontmatter from this synthesis.
- Do not move technique paths.
- Do not promote, deprecate, split, merge, or route away bundles from watch
  labels alone.
- Do not hand-edit generated capsules as source truth.
- Do not choose a broad repair cohort until the capsule repair proves the
  repair rhythm on a small concrete defect.
