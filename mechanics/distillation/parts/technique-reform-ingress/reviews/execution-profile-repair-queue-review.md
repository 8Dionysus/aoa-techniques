# Execution Profile Repair Queue Review

Source packet: [Technique Reform Ingress](../README.md)

Status: Phase 6 repair-queue review. No technique leaf, registry, generated
scout rule, schema, capsule builder, or frontmatter changed.

## Verdict

No broad repair wave is needed from the execution-profile long pass.

One row should stay in a named repair queue:

| technique | current scout profile | queue status | smallest honest issue | next owner route |
|---|---|---|---|---|
| `AOA-T-0095` `github-only-owner-endcap-with-reality-sync` | `medium-agent` | profile-pressure repair candidate | the bundle is one coherent owner-closeout workflow, but actual execution includes GitHub issue/PR/CI/merge plus immediate coordination-layer reality sync | future targeted leaf/profile review in `aoa-techniques`; empirical or harness verdicts in `aoa-evals`; scenario choreography in `aoa-playbooks` if it widens |

This is not a demotion. The direct-read packet still supports `AOA-T-0095` as
a promoted technique bundle. The queue item exists because the generated
`medium-agent` scout value can under-signal the outer orchestration needed when
the technique is executed against a real GitHub owner surface.

## Reviewed Sources

- [execution-profile-medium-agent-calibration-review](execution-profile-medium-agent-calibration-review.md)
- [execution-profile-orchestration-boundary-review](execution-profile-orchestration-boundary-review.md)
- [execution-profile-registry-calibration-review](execution-profile-registry-calibration-review.md)
- `mechanics/distillation/parts/technique-reform-ingress/reports/technique_topology_scout.json`
- `techniques/proof/AGENTS.md`
- `techniques/proof/owner-truth-closeout/github-only-owner-endcap-with-reality-sync/TECHNIQUE.md`
- `techniques/proof/owner-truth-closeout/github-only-owner-endcap-with-reality-sync/checks/github-only-owner-endcap-with-reality-sync-checklist.md`
- `techniques/proof/owner-truth-closeout/github-only-owner-endcap-with-reality-sync/examples/minimal-github-only-owner-endcap-with-reality-sync.md`
- `techniques/proof/owner-truth-closeout/github-only-owner-endcap-with-reality-sync/notes/canonical-readiness.md`
- `techniques/proof/owner-truth-closeout/github-only-owner-endcap-with-reality-sync/notes/second-context-adaptation.md`
- `techniques/proof/owner-truth-closeout/github-only-owner-endcap-with-reality-sync/notes/origin-evidence.md`

## Direct-Read Finding

`AOA-T-0095` has the necessary promoted-bundle anatomy:

- bounded intent: one remote-only owner surface lands through GitHub-native
  issue/PR flow, then staging truth is rebound to merged owner anchors;
- explicit use boundary: use when the owner repo is intentionally GitHub-only
  and one bounded owner-side endcap is enough;
- explicit non-use boundary: do not use when a local owner checkout is the
  intended execution surface or when the route widens into multi-repo
  choreography;
- concrete outputs: merged owner-side landing, visible GitHub trail, validation
  result, coordination-layer lineage update, and reality-check update;
- risk handling: overclaiming green CI, hidden local execution source, and
  stale staging truth are all named;
- checklist and example: the fixture can inspect whether goal/non-goals,
  visible GitHub trail, validation, merge, and post-merge sync happened.

The profile pressure is not missing technique structure. It is execution
envelope ambiguity:

- as a reviewer/designer move, a medium agent can read a bounded packet and
  decide whether the owner-first plus reality-sync law is satisfied;
- as a real execution move, the action crosses GitHub-native owner state,
  validation checks, merge timing, and coordination-layer writeback, so an
  outer workflow or skill must gate tools, credentials, public claims, and
  post-merge state.

## Repair Queue Item

| field | value |
|---|---|
| id | `AOA-T-0095` |
| slug | `github-only-owner-endcap-with-reality-sync` |
| current generated profile | `medium-agent` |
| current direct-read verdict | coherent promoted workflow; profile-pressure edge |
| smallest future repair | clarify execution envelope without widening the technique into GitHub handbook or remediation playbook |
| likely edit surface | a targeted review packet first; possibly one narrow leaf wording patch later if repeated evidence still shows ambiguity |
| do not do | do not mass-relabel workflow rows, do not add a GitHub keyword rule to the builder, do not split the bundle before a second non-identical context exists |
| proof owner | `aoa-evals` if small/medium/local model verdicts are collected |
| scenario owner | `aoa-playbooks` if the route becomes multi-step remediation or campaign choreography |

## Non-Queue Decisions

| cohort | decision |
|---|---|
| 33 `small-agent` rows | no leaf repair from this pass; all have fixture sketches and remain empirical-fixture candidates |
| 20 other `medium-agent` rows | no repair queue item; Phase 2 confirmed broader comparison or judgement without structural ambiguity |
| 53 `orchestration-required` rows | no repair queue item; Phase 3 confirmed orchestration as an authority or side-effect wrapper, not technique failure |
| negative fixture candidates | keep for future eval design; they are refusal/trap cases, not repair defects |
| registry and builder wording | keep unchanged from Phase 5; repair evidence is too narrow for source-rule mutation |

## Future Targeted Slice

If `AOA-T-0095` is repaired later, keep the slice small:

1. Re-read the technique, checklist, example, and evidence notes.
2. Decide whether the ambiguity can be solved by adding an explicit execution
   envelope note to the bundle.
3. Keep the invariant law unchanged: owner repo lands first, GitHub stays the
   declared execution surface for the remote-only route, and coordination-layer
   reality sync follows immediately.
4. Avoid changing `domain`, `kind`, status, ID, or relations unless a separate
   direct-read remap packet proves that need.
5. Rebuild generated readers if the leaf text changes.
6. Route empirical model execution results to `aoa-evals`, not this review
   packet.

## Stop Lines

- Do not treat this queue as permission to repair every medium or
  orchestration row.
- Do not use `AOA-T-0095` as proof that all GitHub-facing techniques require
  generated `orchestration-required`.
- Do not conflate a review/design fixture with real GitHub execution.
- Do not move scenario-level choreography into `aoa-techniques`.

## Validation

This packet is review-only. Required validation after landing this wave:

1. `python -m unittest tests.test_distillation_mechanics_topology`
2. `python scripts/validate_repo.py`
3. `python scripts/release_check.py` before GitHub merge
