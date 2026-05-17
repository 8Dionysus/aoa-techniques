# Spark Lane

`.agents/spark/` is the Codex Spark fast-session lane for `aoa-techniques`.

Use it when a small model can finish one bounded technique-canon scenario or
leave a portable handoff for a slower session. Spark is calibrated here as a
real-time, interruptible, lightweight coding loop for targeted edits and
audits, not as a long-running autonomous worker. The lane is agent-facing
launch, result, and handoff material. It does not author technique meaning,
mechanic law, generated truth, proof authority, skill workflow meaning, or
runtime state.

## Operating Route

Use [AGENTS](AGENTS.md) for the Spark read order, boundaries, validation lane,
skipped-check reporting, and closeout shape.

Choose one registered scenario from [registry](registry.json), then read that
scenario `README.md` and `PROMPT.md`. Finish with a result packet or a handoff
packet.

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
