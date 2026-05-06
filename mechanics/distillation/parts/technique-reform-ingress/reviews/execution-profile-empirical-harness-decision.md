# Execution Profile Empirical Harness Decision

Source packet: [Technique Reform Ingress](../README.md)

Status: Phase 7 owner-route decision. No local model was run. No eval harness,
runner, scorer, report, registry, generated scout rule, schema, frontmatter, or
technique leaf changed.

## Decision

Do not run local small-agent validation from `aoa-techniques` in this pass.

`aoa-techniques` now owns a complete fixture sketch ledger for all 33 current
`small-agent` scout candidates. That is enough to design a future empirical
harness, but it is not enough to publish a proof claim.

Actual empirical validation should be designed and recorded in `aoa-evals`,
because that repository owns bounded proof meaning, fixture contracts, scoring
or verdict logic, report artifacts, blind spots, and interpretation limits.

## Why Not Run Now

Local model resources may exist, but a real proof surface is not only a model
call. A legitimate run must have:

- one bounded eval claim;
- a public-safe fixture or case family;
- exact prompt packet and allowed context;
- forbidden hidden context;
- named local model and version;
- runtime and hardware assumptions;
- runner contract and retry policy;
- per-case output capture;
- pass/fail or categorical verdict logic;
- failure-mode notes;
- report artifact and interpretation boundary.

Those surfaces belong in `aoa-evals`. Running a small model now from this repo
would create orphan evidence: useful as a private experiment, but too weak to
change `execution_profile`, prove small-agent success, or guide generated scout
rules.

## Owner Split

| surface | owner | reason |
|---|---|---|
| technique intent, contracts, risks, examples, checks | `aoa-techniques` | this repo owns reusable practice meaning |
| fixture sketches for future technique-profile testing | `aoa-techniques` | sketches describe what each technique needs before proof begins |
| eval bundle, bounded claim, fixture contract, runner, scorer, verdict, report | `aoa-evals` | that repo owns bounded proof meaning and interpretation limits |
| repeated workflow application or multi-technique execution | `aoa-skills` if needed | skills own bounded execution workflows, not proof verdicts |
| scenario or campaign choreography | `aoa-playbooks` if needed | playbooks own multi-step scenario composition |
| selector hints after proof exists | `aoa-routing` if needed | routing can consume evidence but should not mint proof |

## First Future Pilot

When the harness route is opened, do one tiny pilot before any bulk run.

Recommended first pilot:

| candidate | why |
|---|---|
| `AOA-T-0056` `channelized-agent-mailbox` | synthetic, no network, no tools, no secrets, no mutation, clear ordered input, clear pass/fail around replay and `acked_through` |

Useful second pilots after the first one works:

| candidate | why |
|---|---|
| `AOA-T-0106` `single-scoped-evidence-reference` | tests proof-overclaim discipline with one claim and one source reference |
| `AOA-T-0028` `confirmation-gated-mutating-action` | tests refusal and approval-boundary behavior without real mutation |
| `AOA-T-0059` `git-verified-handoff-claims` | introduces a tiny local git fixture after no-tool synthetic pilots are stable |

Do not start with `AOA-T-0095`; it is the repair-queue edge and needs an
owner-route profile decision before empirical model execution would be clean.

## Model Selection Posture

No concrete model is selected in this repo.

The future eval packet should choose the local candidate model explicitly in
the proof owner surface, including version, quantization or serving path if
relevant, context length, runtime, hardware, and any orchestration wrapper.

The target class remains `2-4B` local agents because that is the reason
`small-agent` exists as a scout profile. But the claim must be per model and
per fixture family, not a global statement that all small agents can execute
the technique.

## Minimum Eval Bundle Shape

A future `aoa-evals` bundle should include:

- object under evaluation: local small model executing one orchestrator-packed
  technique fixture;
- bounded claim: under the packed fixture constraints, the model can produce
  the expected artifact while preserving stop lines;
- fixture surface: public-safe synthetic cases derived from
  [execution-profile-fixture-sketch-ledger](execution-profile-fixture-sketch-ledger.md);
- scoring: per-case pass/fail plus failure mode;
- report: exact model, prompt, fixture input, output, verdict, and reviewer or
  harness note;
- blind spots: no autonomous selection proof, no hidden-context proof, no
  transfer claim across all techniques, and no proof of real side-effecting
  execution.

## Stop Lines

- Do not call review packets model outputs.
- Do not treat fixture sketches as eval fixtures until `aoa-evals` gives them
  a case-family contract.
- Do not update `execution_profile` counts from direct reading alone.
- Do not let a single toy pass become a profile-wide proof claim.
- Do not run fixtures with network, secrets, public-share, or real mutation
  before an owner-approved eval route exists.

## Carry Forward

- Final closeout should state that empirical proof was intentionally deferred
  to `aoa-evals`.
- The next cross-repo pass should open an `aoa-evals` design slice for the
  `AOA-T-0056` pilot if the project wants real local small-agent validation.
- `aoa-techniques` should remain ready to supply fixture sketches and technique
  contracts, but should not store model verdict authority.

## Validation

This packet is review-only. Required validation after landing this wave:

1. `python -m unittest tests.test_distillation_mechanics_topology`
2. `python scripts/validate_repo.py`
3. `python scripts/release_check.py` before GitHub merge
