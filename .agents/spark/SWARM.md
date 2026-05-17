# Spark Swarm

Use this file only when the user explicitly asks for a Spark swarm. Ordinary
Spark work starts from one scenario in `.agents/spark/registry.json`.

This swarm file is local orchestration guidance, not a claim that Spark itself
is a long-running background-worker system. Keep every lane real-time,
interruptible, and narrow.

## Swarm Rule

A swarm still follows the Spark lane contract:

- one coordinator
- one registered scenario per worker
- one bounded file family per writer
- no in-session switch to a larger model
- no broad validation unless explicitly assigned
- every lane ends as `done` or `handoff`

## Launch Context

Use [AGENTS](AGENTS.md#read-before-editing) for the Spark read order before
launching a swarm. Then read `registry.json` and the scenario `README.md` plus
`PROMPT.md` for every assigned lane.

## Roles

| Role | Work |
|---|---|
| Coordinator | chooses the scenario, exact scope, risks, and validation path |
| Scout | reads and reports findings without editing |
| Builder | makes one bounded patch inside the assigned scope |
| Verifier | runs the named validation and reports skipped checks |
| Boundary Keeper | checks that Spark did not absorb stronger technique, mechanic, generated, or sibling-owner truth |

## Parallel Lanes

Allowed parallelism:

- one audit lane plus one verifier lane
- one builder lane per disjoint file family
- one boundary review lane after a patch exists

Do not run two writers on the same family of files.

## Coordinator Launch Packet

```text
We are working in aoa-techniques through Spark.
Choose one registered scenario from .agents/spark/registry.json.

Return:
1. scenario id
2. exact scope
3. files to read first
4. expected done signal
5. handoff condition
6. validation command
```

## Worker Launch Packet

```text
You are a Spark worker in aoa-techniques.
Read .agents/spark/AGENTS.md, .agents/spark/registry.json, and the assigned scenario.
Finish the assigned scope or leave a handoff packet.
Do not widen into another scenario.
Report files read, files changed, validation run, skipped checks, and risk.
```

Use [AGENTS](AGENTS.md#validation) for the Spark validation lane and report any
checks that the swarm intentionally skips.
