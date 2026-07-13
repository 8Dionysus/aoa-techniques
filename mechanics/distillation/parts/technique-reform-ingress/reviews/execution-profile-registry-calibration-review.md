# Execution Profile Registry Calibration Review

Source packet: [Technique Reform Ingress](../README.md)

Status: Phase 5 calibration review. No frontmatter, schema, registry,
generated scout rule, capsule builder, template, or technique leaf changed.

## Verdict

Do not change `mechanics/distillation/parts/technique-reform-ingress/config/technique_topology_axes.yaml` or
`mechanics/distillation/parts/technique-reform-ingress/scripts/build_topology_scout.py` in this wave.

The current registry and topology contract already say the important thing:
`execution_profile` is a scout suitability estimate from authored technique
shape, not empirical proof and not frontmatter truth. The long pass found
review pressure and fixture-design work, but not enough evidence for a source
rule change.

The one real edge is `AOA-T-0095`
`github-only-owner-endcap-with-reality-sync`: it is generated as
`medium-agent` because it is a `workflow` with read-only risk, but direct
reading shows it touches GitHub-native issue/PR/CI/merge reality and
post-merge sync. That edge should move into the repair queue and future eval or
owner-route design. It should not be patched by a broad generated keyword rule.

## Reviewed Sources

- [execution-profile-truth-boundary-pilot](execution-profile-truth-boundary-pilot.md)
- [execution-profile-small-agent-core-shelves-review](execution-profile-small-agent-core-shelves-review.md)
- [execution-profile-small-agent-remaining-shelves-review](execution-profile-small-agent-remaining-shelves-review.md)
- [execution-profile-medium-agent-calibration-review](execution-profile-medium-agent-calibration-review.md)
- [execution-profile-orchestration-boundary-review](execution-profile-orchestration-boundary-review.md)
- [execution-profile-fixture-sketch-ledger](execution-profile-fixture-sketch-ledger.md)
- `mechanics/distillation/parts/technique-reform-ingress/config/technique_topology_axes.yaml`
- `docs/TECHNIQUE_TOPOLOGY_CONTRACT.md`
- `mechanics/distillation/parts/technique-reform-ingress/scripts/build_topology_scout.py`
- `scripts/validate_repo.py`
- `mechanics/distillation/parts/technique-reform-ingress/reports/technique_topology_scout.json`
- `docs/decisions/AOA-TECH-D-0042-topology-scout-axis-registry.md`

## Current Source Shape

The current generated count remains:

| profile | count |
|---|---:|
| `small-agent` | 33 |
| `medium-agent` | 21 |
| `orchestration-required` | 53 |

The builder currently infers execution profile from:

- high-risk posture: `mutating`, `public-share`, `security-sensitive`, or
  `irreversible` becomes `orchestration-required`;
- otherwise kind defaults:
  - `guardrail`, `validation`, `artifact`, `lift`, and `handoff` become
    `small-agent`;
  - `workflow`, `composition`, and `assessment` become `medium-agent`;
  - `distribution`, `ingest`, and `recovery` become
    `orchestration-required`;
  - `discovery` becomes `tiny-card`.

That is intentionally coarse. It is useful as scout pressure because it is
deterministic, reviewable, and weaker than direct reading.

## Calibration Decisions

| pressure | decision | why |
|---|---|---|
| `small-agent` can sound like proven 2-4B success | no registry change | the registry, contract, pilot, and fixture ledger now all say empirical success requires a separate local eval |
| `orchestration-required` can sound like a quality demotion | no registry change | the current summary already says the move can be atomic while requiring an outer workflow, approval gate, or tool choreography |
| many `small-agent` rows need orchestrator-packed facts | no builder change | that is the intended meaning of `small-agent`, and Phase 4 now makes the packed fixture shape explicit |
| approval-shaped but read-only guard rows such as `AOA-T-0091` remain `small-agent` | keep current behavior | a simulated guard/ingress record can be one small fixture; real risky mutation remains outside the fixture |
| `AOA-T-0095` is generated `medium-agent` but reads like an orchestration edge | carry to repair queue | a single edge is not enough for a broad rule, and a keyword rule around GitHub/merge would overfit public or owner-facing rows |
| future local model testing belongs somewhere | route to `aoa-evals` | `aoa-techniques` owns fixture sketches and technique shape, not model verdict surfaces |

## Rejected Changes

| possible change | rejected for now because |
|---|---|
| add more registry wording to `small-agent` | the registry already names orchestration-supplied facts, frame, output shape, and separate eval proof |
| add more registry wording to `orchestration-required` | the current text is clear enough, and the nuance is better preserved in review packets than repeated law blocks |
| add generated keyword promotion from GitHub/merge words to `orchestration-required` | it would confuse owner-native evidence reading with side-effecting execution and would likely overclassify read-only closeout rows |
| add `execution_profile` to bundle frontmatter | this pass produced scout review and fixture sketches, not schema migration proof |
| mutate technique leaves during calibration | the pass is still classifying and routing; leaf repair belongs to Phase 6 |
| create an eval harness in this repo | empirical verdicts need model, prompt, fixture, output, verdict, and failure surfaces under a proof owner |

## Source Change Triggers

Change the registry, builder, generated scout, or schema only after one of
these happens:

- multiple direct-read review packets find the same profile class misleading in
  the same way;
- local small-agent evals show systematic failure or success that the scout
  vocabulary cannot express;
- several rows repeat the same owner-boundary edge that cannot be captured by
  repair notes or future fixture metadata;
- a separate decision promotes `execution_profile` from scout surface toward
  optional or required bundle metadata;
- downstream `aoa-evals`, `aoa-routing`, or `aoa-skills` consumers need a
  stable machine-readable field and bring evidence back to this repo.

## Carry Forward

- Phase 6 should create a repair queue with `AOA-T-0095` as the only named
  profile-pressure edge from this pass unless more direct evidence appears.
- Phase 7 should decide the empirical harness route without treating this
  repo's review packets as model outputs.
- Final closeout should state that the generated scout stayed unchanged and
  that profile truth remains scout-only.

## Validation

This packet is review-only. Required validation after landing this wave:

1. the targeted tests
2. repository validation
3. the release lane before GitHub merge
