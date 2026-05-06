# Automation-Governance Direct-Read Split Review

Source packet:
[Technique Reform Ingress](../README.md)

Previous landed review:
[Landed Owner-Truth-Closeout Pilot Review](landed-owner-truth-closeout-pilot-review.md)

Generated lens:
[Technique Tree Projection](../../../../../reports/technique_tree_projection.md)

Tree contract:
[Technique Tree Contract](../../../../../docs/TECHNIQUE_TREE_CONTRACT.md)

Status: split-required-before-migration, not path migration, not `tree_path`
frontmatter.

## Verdict

Reject `governance/automation-governance` as one bulk migration shelf.

Direct reading confirms that all nine leaves belong near the governance trunk,
but not under one immediate shelf. The projection's `split-review-needed`
marker is correct: the set mixes three different reusable questions that would
become muddy if migrated together as "automation governance".

Split the pressure into three reviewed candidate shelves before any path
movement:

- `governance/automation-readiness`: `AOA-T-0086`, `AOA-T-0087`, and
  `AOA-T-0088`
- `governance/promotion-boundary`: `AOA-T-0089`, `AOA-T-0090`, and
  `AOA-T-0102`
- `governance/practice-adoption-lifecycle`: `AOA-T-0101`, `AOA-T-0103`, and
  `AOA-T-0104`

This review does not move files. It preserves `domain`, `kind`, status,
evidence, support files, maturity, relations, validation-strength metadata,
public-safety posture, and current paths for all nine bundles.

## Sources Read

- [AOA-T-0086 automation-fit-matrix](../../../../../techniques/agent-workflows/automation-fit-matrix/TECHNIQUE.md)
- [AOA-T-0086 canonical readiness](../../../../../techniques/agent-workflows/automation-fit-matrix/notes/canonical-readiness.md)
- [AOA-T-0087 human-loop-to-seed-lift](../../../../../techniques/agent-workflows/human-loop-to-seed-lift/TECHNIQUE.md)
- [AOA-T-0087 canonical readiness](../../../../../techniques/agent-workflows/human-loop-to-seed-lift/notes/canonical-readiness.md)
- [AOA-T-0088 approval-sensitivity-check](../../../../../techniques/agent-workflows/approval-sensitivity-check/TECHNIQUE.md)
- [AOA-T-0088 canonical readiness](../../../../../techniques/agent-workflows/approval-sensitivity-check/notes/canonical-readiness.md)
- [AOA-T-0089 quest-unit-promotion-review](../../../../../techniques/agent-workflows/quest-unit-promotion-review/TECHNIQUE.md)
- [AOA-T-0089 canonical readiness](../../../../../techniques/agent-workflows/quest-unit-promotion-review/notes/canonical-readiness.md)
- [AOA-T-0090 nearest-wrong-target-rejection](../../../../../techniques/agent-workflows/nearest-wrong-target-rejection/TECHNIQUE.md)
- [AOA-T-0090 canonical readiness](../../../../../techniques/agent-workflows/nearest-wrong-target-rejection/notes/canonical-readiness.md)
- [AOA-T-0101 local-pattern-adoption-gate](../../../../../techniques/agent-workflows/local-pattern-adoption-gate/TECHNIQUE.md)
- [AOA-T-0101 canonical readiness](../../../../../techniques/agent-workflows/local-pattern-adoption-gate/notes/canonical-readiness.md)
- [AOA-T-0102 skill-proposal-handoff-packet](../../../../../techniques/agent-workflows/skill-proposal-handoff-packet/TECHNIQUE.md)
- [AOA-T-0102 canonical readiness](../../../../../techniques/agent-workflows/skill-proposal-handoff-packet/notes/canonical-readiness.md)
- [AOA-T-0103 adopted-practice-retention-review](../../../../../techniques/agent-workflows/adopted-practice-retention-review/TECHNIQUE.md)
- [AOA-T-0103 canonical readiness](../../../../../techniques/agent-workflows/adopted-practice-retention-review/notes/canonical-readiness.md)
- [AOA-T-0104 superseded-practice-obsolescence-route](../../../../../techniques/agent-workflows/superseded-practice-obsolescence-route/TECHNIQUE.md)
- [AOA-T-0104 canonical readiness](../../../../../techniques/agent-workflows/superseded-practice-obsolescence-route/notes/canonical-readiness.md)
- [Agent-workflows route card](../../../../../techniques/agent-workflows/AGENTS.md)
- [Governance route card](../../../../../techniques/governance/AGENTS.md)
- [Technique family scout rows for `automation-governance`](../../../../../reports/technique_family_scout.md)
- [Technique topology scout rows for `automation-governance`](../../../../../reports/technique_topology_scout.md)
- [Technique tree projection rows for `automation-governance`](../../../../../reports/technique_tree_projection.md)

## Direct Bundle Read

| technique | current posture | direct read |
|---|---|---|
| `AOA-T-0086` | `domain: agent-workflows`, `kind: assessment`, `status: promoted` | classifies one recurring manual route with a descriptive automation-fit matrix; it does not choose the landing or grant automation authority |
| `AOA-T-0087` | `domain: agent-workflows`, `kind: assessment`, `status: promoted` | chooses the first honest automation-facing landing for one recurring human loop; it does not implement the seed, skill, or playbook |
| `AOA-T-0088` | `domain: agent-workflows`, `kind: assessment`, `status: promoted` | marks approval, rollback, hidden-authority, or self-change burden before seed-ready language stays credible; it does not approve execution |
| `AOA-T-0089` | `domain: agent-workflows`, `kind: assessment`, `status: promoted` | emits one bounded promotion verdict for one repeated reviewed quest unit; it does not author the destination |
| `AOA-T-0090` | `domain: agent-workflows`, `kind: guardrail`, `status: promoted` | names the nearest wrong target beside one chosen verdict; it does not choose the verdict by itself |
| `AOA-T-0101` | `domain: agent-workflows`, `kind: guardrail`, `status: promoted` | gates local adoption of one shared pattern through consent, compatibility, rollback, and retention watch; it does not implement adoption |
| `AOA-T-0102` | `domain: agent-workflows`, `kind: handoff`, `status: promoted` | emits one skill-proposal packet from technique-side pressure; it does not create, accept, or activate a skill |
| `AOA-T-0103` | `domain: agent-workflows`, `kind: assessment`, `status: promoted` | reviews one adopted or shadowed practice for retention, revision, quarantine, defer, or obsolescence routing; it does not adopt new practice or delete old practice |
| `AOA-T-0104` | `domain: agent-workflows`, `kind: handoff`, `status: promoted` | routes one adopted or shadowed practice toward supersession, merge, reanchor, defer, drop, or deprecation review; it does not delete, deprecate, or erase evidence |

## Why One Shelf Fails

- The first three leaves share one automation-candidate readiness object:
  readiness matrix, first honest landing, and checkpoint burden.
- `AOA-T-0089` and `AOA-T-0090` are promotion-verdict boundary tools, while
  `AOA-T-0102` is a skill-owner handoff packet; they are adjacent because they
  keep owner targets honest, not because they are automation readiness checks.
- `AOA-T-0101`, `AOA-T-0103`, and `AOA-T-0104` are a local practice lifecycle:
  adoption gate, retention review, and obsolescence route.
- Calling all nine "automation governance" hides whether the current object is
  a candidate, a promotion verdict, a skill proposal, an adopted practice, or
  a superseded practice.
- All nine remain useful governance-facing techniques, but a single shelf
  would be too broad for small-agent retrieval and too tempting as fake
  automation policy.

## Split Candidates

### Candidate A: `governance/automation-readiness`

| technique | current path | proposed path |
|---|---|---|
| `AOA-T-0086` | `techniques/agent-workflows/automation-fit-matrix/` | `techniques/governance/automation-readiness/automation-fit-matrix/` |
| `AOA-T-0087` | `techniques/agent-workflows/human-loop-to-seed-lift/` | `techniques/governance/automation-readiness/human-loop-to-seed-lift/` |
| `AOA-T-0088` | `techniques/agent-workflows/approval-sensitivity-check/` | `techniques/governance/automation-readiness/approval-sensitivity-check/` |

Read:

This is the first split candidate because it is the smallest coherent
automation-facing shelf. It starts from one recurring route or candidate and
asks whether automation-oriented lift is honest yet: classify fit, choose the
first honest landing, and surface checkpoint burden.

### Candidate B: `governance/promotion-boundary`

| technique | current path | proposed path |
|---|---|---|
| `AOA-T-0089` | `techniques/agent-workflows/quest-unit-promotion-review/` | `techniques/governance/promotion-boundary/quest-unit-promotion-review/` |
| `AOA-T-0090` | `techniques/agent-workflows/nearest-wrong-target-rejection/` | `techniques/governance/promotion-boundary/nearest-wrong-target-rejection/` |
| `AOA-T-0102` | `techniques/agent-workflows/skill-proposal-handoff-packet/` | `techniques/governance/promotion-boundary/skill-proposal-handoff-packet/` |

Read:

This candidate keeps owner-target pressure explicit. It decides, sharpens, or
hands off a bounded reusable unit without turning that verdict into skill
acceptance, quest/playbook promotion doctrine, or owner-layer authorship.

### Candidate C: `governance/practice-adoption-lifecycle`

| technique | current path | proposed path |
|---|---|---|
| `AOA-T-0101` | `techniques/agent-workflows/local-pattern-adoption-gate/` | `techniques/governance/practice-adoption-lifecycle/local-pattern-adoption-gate/` |
| `AOA-T-0103` | `techniques/agent-workflows/adopted-practice-retention-review/` | `techniques/governance/practice-adoption-lifecycle/adopted-practice-retention-review/` |
| `AOA-T-0104` | `techniques/agent-workflows/superseded-practice-obsolescence-route/` | `techniques/governance/practice-adoption-lifecycle/superseded-practice-obsolescence-route/` |

Read:

This candidate keeps Method-growth lifecycle atoms together without importing
the full Method-growth mechanic. It covers local adoption, later retention, and
obsolescence routing for one practice surface.

## Governance Trunk Fit

All three candidates fit `governance` better than broad `agent-workflows`
because their primary browsing question is not "what sequence does the agent
execute next?" It is "what choice, approval, owner boundary, adoption posture,
or automation boundary must stay explicit before action?" The current
frontmatter should still remain unchanged: all nine continue to say
`domain: agent-workflows`, while `kind` keeps its current assessment,
guardrail, or handoff truth.

## Stop Lines

- Do not move any `automation-governance` bundle from this review alone.
- Do not add `tree_path`, `family`, capability, substrate, execution-profile,
  or risk frontmatter.
- Do not change `domain`, `kind`, ID, status, maturity, evidence, or relation
  metadata.
- Do not treat `automation-readiness` as automation policy authority, seed
  canon, implementation approval, scheduler doctrine, hidden automation
  governance, or runtime behavior.
- Do not treat `promotion-boundary` as skill acceptance, skill activation,
  quest/playbook promotion doctrine, role contract law, proof verdict, memory
  write, or routing policy.
- Do not treat `practice-adoption-lifecycle` as Method-growth law, local
  owner consent, deletion, deprecation execution, proof authority, memory
  truth, skill activation, route mutation, runtime change, or permanent
  practice retention.
- Keep generated projection weaker than authored bundle meaning.

## Next Honest Move

Do not migrate `governance/automation-governance` as one shelf.

Run a split-expansion closeout that activates the reserved automation split
steps, names Candidate A as `governance/automation-readiness`, and records
Candidate B and Candidate C as pending split candidates. After that, directly
review Candidate A before any twenty-fifth shelf movement.
