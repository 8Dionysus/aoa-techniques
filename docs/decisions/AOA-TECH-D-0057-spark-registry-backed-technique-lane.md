# Decision Note: Spark Registry-Backed Technique Lane

Status: accepted
Date: 2026-05-15

## Index Metadata

- Decision ID: AOA-TECH-D-0057
- Original date: 2026-05-15
- Surface classes: agent route, generated/readout
- Technique axes: agent mesh
- Mechanic parents: none
- Guard families: AGENTS/mesh, generated/read-model
- Posture: accepted

## Context

`aoa-techniques` had moved the old root `Spark/` lane under
[.agents/spark](https://github.com/8Dionysus/aoa-techniques/tree/feffba63dc22fd921512ba5a3ff1b5d78606f93b/.agents/spark/), but the local lane still contained only
an operating card and a swarm recipe. That was enough to remove root clutter,
but not enough for repeated Codex Spark use.

The `Agents-of-Abyss` center lane already proved a stronger shape:
registry-backed scenarios, done-or-handoff exits, result and handoff templates,
storage homes, a local validator, lane tests, and release-check wiring. The
techniques repository needs that discipline, adapted to reusable public
practice rather than center civic direction.

OpenAI's public Spark framing also matters: Codex-Spark is a real-time,
ultra-low-latency coding model for targeted interactive work, with a
lightweight default style. It should not be treated as a smaller clone of a
long-running Codex agent.

## Options considered

1. Keep `.agents/spark/` as only `AGENTS.md` plus `SWARM.md`.
2. Copy the `Agents-of-Abyss` Spark lane exactly.
3. Build a registry-backed Spark lane adapted to technique-canon work.

## Decision

Build `.agents/spark/` as a registry-backed Codex Spark lane for
`aoa-techniques`.

The lane now owns:

- [README](https://github.com/8Dionysus/aoa-techniques/tree/feffba63dc22fd921512ba5a3ff1b5d78606f93b/.agents/spark/README.md)
- [registry](https://github.com/8Dionysus/aoa-techniques/tree/feffba63dc22fd921512ba5a3ff1b5d78606f93b/.agents/spark/registry.json)
- scenario packets under `../../.agents/spark/scenarios/`
- result and handoff homes under `../../.agents/spark/results/` and
  `../../.agents/spark/handoffs/`
- schemas under `../../.agents/spark/schemas/`
- [Spark lane validator](https://github.com/8Dionysus/aoa-techniques/tree/feffba63dc22fd921512ba5a3ff1b5d78606f93b/.agents/spark/scripts/validate_spark_lane.py)
- [Spark lane tests](https://github.com/8Dionysus/aoa-techniques/tree/feffba63dc22fd921512ba5a3ff1b5d78606f93b/.agents/spark/tests/test_spark_lane.py)

The registered scenarios are technique-canon specific:

- `technique-audit`
- `technique-refinement`
- `candidate-scout`
- `diff-review`
- `registry-sync`
- `test-factory`
- `release-prep`

## Rationale

The center lane shape gives Spark a bounded operating contract without making
Spark a source of doctrine. The local adaptation keeps that discipline while
changing the scenario set to match `aoa-techniques`: atomic technique moves,
public-safe wording, candidate scouting, generated parity, registry sync,
tests, and release readiness.

Keeping the lane as two prompt-like files would invite drift and repeated
reinvention. Copying the center lane exactly would import center concerns that
do not belong to the technique canon.

## Consequences

- Spark sessions in this repo have a checkable `done-or-handoff` route.
- New scenarios must be registered and validated.
- `scripts/release_check.py` now runs Spark lane validation and Spark lane
  tests.
- Ordinary Spark scenario work should stay lightweight and run only the
  explicit narrow validation named by the user, scenario, or repo law. The
  registry's per-scenario `default_validation` values are validation routes,
  not a command to run broad repo checks by default.
- Spark remains subordinate to technique bundles, source docs, mechanics,
  generated-source builders, validators, and sibling-owner repositories.
- Scenario shape is validated; scenario judgment still requires human or agent
  review in the actual task.

## Source surfaces

- [.agents AGENTS](../../.agents/AGENTS.md)
- [Spark AGENTS](https://github.com/8Dionysus/aoa-techniques/tree/feffba63dc22fd921512ba5a3ff1b5d78606f93b/.agents/spark/AGENTS.md)
- [Spark notebook](https://github.com/8Dionysus/aoa-techniques/tree/feffba63dc22fd921512ba5a3ff1b5d78606f93b/.agents/spark/SPARK_EXTRAPOLATION_NOTEBOOK.md)
- [Spark README](https://github.com/8Dionysus/aoa-techniques/tree/feffba63dc22fd921512ba5a3ff1b5d78606f93b/.agents/spark/README.md)
- [Spark registry](https://github.com/8Dionysus/aoa-techniques/tree/feffba63dc22fd921512ba5a3ff1b5d78606f93b/.agents/spark/registry.json)
- [Spark validator](https://github.com/8Dionysus/aoa-techniques/tree/feffba63dc22fd921512ba5a3ff1b5d78606f93b/.agents/spark/scripts/validate_spark_lane.py)
- [Spark tests](https://github.com/8Dionysus/aoa-techniques/tree/feffba63dc22fd921512ba5a3ff1b5d78606f93b/.agents/spark/tests/test_spark_lane.py)
- [Release check](../../scripts/release_check.py)
- [DESIGN.AGENTS](../../DESIGN.AGENTS.md)
- [ROOT_SURFACE_LAW](../ROOT_SURFACE_LAW.md)
- [Spark lane home decision](AOA-TECH-D-0054-spark-agent-lane-home.md)
- [OpenAI: Introducing GPT-5.3-Codex-Spark](https://openai.com/index/introducing-gpt-5-3-codex-spark/)
- [OpenAI Developers: Codex Use Cases](https://developers.openai.com/codex/use-cases/)

## Follow-up route

If a Spark scenario starts carrying durable technique doctrine, move that
doctrine to the owning technique contract, mechanic, or bundle. If the lane
becomes model-agnostic rather than Codex Spark specific, write a new decision
before renaming or widening `.agents/spark/`.

## Verification

This decision is validated by:

Verification was routed through the targeted owner checks and repository validation lanes.
