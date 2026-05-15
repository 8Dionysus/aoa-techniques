# Spark Lane

`.agents/spark/` is the Codex Spark fast-session lane for `aoa-techniques`.

Use it when a small model can finish one bounded technique-canon scenario or
leave a portable handoff for a slower session. Spark is calibrated here as a
real-time, interruptible, lightweight coding loop for targeted edits and
audits, not as a long-running autonomous worker. The lane is agent-facing
launch, result, and handoff material. It does not author technique meaning,
mechanic law, generated truth, proof authority, skill workflow meaning, or
runtime state.

## Core Contract

| Rule | Meaning |
|---|---|
| one scenario | choose exactly one registered scenario from [registry](registry.json) |
| one scope | keep the technique, source surface, registry family, or validation path small |
| done-or-handoff | finish the scenario or write a handoff; do not depend on an in-session model switch |
| targeted edit | prefer minimal local edits, tight audits, or explicit handoffs over broad rewrites |
| explicit validation | run narrow checks named by the user, scenario, or repo law; do not run broad tests just because they exist |
| source respect | route to stronger source surfaces instead of absorbing their authority |
| public safety | do not carry private residue, raw logs, secrets, host paths, or project folklore into public technique text |
| evidence | name files read, files changed, validation run, skipped checks, remaining risk, and next owner route |

## Start Here

1. Read root [AGENTS](../../AGENTS.md).
2. Read [.agents AGENTS](../AGENTS.md).
3. Read local [AGENTS](AGENTS.md).
4. Choose one scenario from [registry](registry.json).
5. Read that scenario `README.md` and `PROMPT.md`.
6. Finish with a result packet or a handoff packet.

Use [SWARM](SWARM.md) only when a Spark swarm is explicitly requested.

## Scenarios

| Scenario | Use |
|---|---|
| [technique-audit](scenarios/technique-audit/README.md) | read-only audit of boundedness, duplicate meaning, stale paths, public hygiene, and owner route |
| [technique-refinement](scenarios/technique-refinement/README.md) | one small source-backed patch to an existing technique bundle |
| [candidate-scout](scenarios/candidate-scout/README.md) | map donor, legacy, or mechanic-local material before deeper distillation |
| [diff-review](scenarios/diff-review/README.md) | review a concrete diff or PR for technique-canon risk and missed checks |
| [registry-sync](scenarios/registry-sync/README.md) | align docs, registry, validator, release gate, and generated companions |
| [test-factory](scenarios/test-factory/README.md) | add bounded tests for an already clear source contract |
| [release-prep](scenarios/release-prep/README.md) | run a fast release-readiness pass without publishing |

## Output Homes

| Home | Role |
|---|---|
| [handoffs/open](handoffs/open/) | portable packets for later Spark or non-Spark sessions |
| [handoffs/closed](handoffs/closed/) | resolved or superseded handoff packets kept as traceable examples |
| [results](results/) | reusable completed Spark results worth preserving beyond chat closeout |

Ordinary closeout belongs in the conversation or pull request. Commit result or
handoff packets only when the packet helps future sessions reproduce a bounded
lane.

The registry's `default_validation` entries are validation routes, not an
instruction to run every broad repository check by default. Ordinary Spark work
should keep the loop narrow and report skipped checks honestly.

## Validation

Run the lane validator before broad gates:

```bash
python .agents/spark/scripts/validate_spark_lane.py
python -m unittest discover -s .agents/spark/tests -p 'test*.py'
```

For broad agent-lane, generated, or release-facing changes, run:

```bash
python scripts/release_check.py
```

For ordinary Spark scenario work, prefer the scenario's narrow validation path.
If validation is not requested or not safe to run inside the fast loop, report
it under `Skipped checks` and leave a handoff when confidence would otherwise
be overstated.
