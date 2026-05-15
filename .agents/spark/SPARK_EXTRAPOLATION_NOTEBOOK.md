# Spark Extrapolation Notebook

This notebook is the working surface for adapting the `Agents-of-Abyss`
Codex Spark lane to `aoa-techniques`.

It is not the final authority for daily Spark use. The active lane contract is
now in `README.md`, `AGENTS.md`, `registry.json`, scenario packets, the
validator, and tests. This notebook records what was preserved from the center
pattern and why the technique-canon adaptation has this shape.

## Source Studied

Primary source in `Agents-of-Abyss`:

- `DESIGN.AGENTS.md`
- `.agents/AGENTS.md`
- `.agents/spark/AGENTS.md`
- `.agents/spark/README.md`
- `.agents/spark/SWARM.md`
- `.agents/spark/registry.json`
- `.agents/spark/scenarios/**`
- `.agents/spark/schemas/**`
- `.agents/spark/scripts/validate_spark_lane.py`
- `.agents/spark/tests/test_spark_lane.py`
- `docs/decisions/2026-04-30-spark-session-lane-contract.md`
- `docs/decisions/2026-05-13-codex-spark-agent-lane-home.md`

Local `aoa-techniques` surfaces that constrain the adaptation:

- `AGENTS.md`
- `DESIGN.md`
- `DESIGN.AGENTS.md`
- `.agents/AGENTS.md`
- `.agents/spark/AGENTS.md`
- `.agents/spark/SWARM.md`
- `docs/ROOT_SURFACE_LAW.md`
- `docs/decisions/2026-05-14-spark-agent-lane-home.md`
- `docs/TECHNIQUE_ATOM_CONTRACT.md`
- `docs/TECHNIQUE_TOPOLOGY_CONTRACT.md`
- `docs/TECHNIQUE_TREE_CONTRACT.md`
- `TECHNIQUE_INDEX.md`

## Center Pattern To Preserve

The `Agents-of-Abyss` Spark lane is not just prompt text. Its shape is:

1. `.agents/spark/` is the durable home.
2. Spark is a Codex-specific fast session lane, not a mechanic package and not
   source authority.
3. The core execution rule is `done-or-handoff`.
4. A Spark session chooses exactly one registered scenario and one bounded
   scope.
5. A scenario must provide `README.md`, `PROMPT.md`,
   `templates/result.md`, `templates/handoff.md`, and
   `examples/result.example.md`.
6. The registry is the scenario source of truth and names prompt, result,
   handoff, example, default validation route, done signal, and stop-line.
7. Results and handoffs have stable packet homes:
   `.agents/spark/results/`, `.agents/spark/handoffs/open/`, and
   `.agents/spark/handoffs/closed/`.
8. `SWARM.md` is only for explicit swarm requests.
9. A local validator checks registry shape, required scenario files, required
   result and handoff markers, registered-vs-discovered scenario parity, and
   release-check wiring.
10. Tests cover the validator and at least one negative case such as an
    unregistered scenario directory.

The important design move is registry-backed boundedness. The lane is useful
because a future Spark session can start, finish, or hand off without inventing
its own route.

## Web Calibration

OpenAI describes GPT-5.3-Codex-Spark as a smaller Codex model designed for
real-time coding rather than long-horizon autonomous work. The important
operating signals for this lane are:

- Spark is optimized for ultra-low-latency interactive work, not exhaustive
  architecture synthesis.
- Spark is strongest for targeted edits, reshaping local logic, refining
  interfaces, and seeing results immediately.
- Spark can be interrupted or redirected during work.
- Its default working style is lightweight: minimal targeted edits rather than
  broad rewrites.
- It does not automatically run tests unless the user or the prompt explicitly
  asks it to.
- During the research-preview framing, Spark is text-only with a 128k context
  window and separate access/rate-limit behavior.

Local consequence: `.agents/spark/` should not behave like a smaller copy of a
full long-running Codex agent. It should preserve one-scenario, one-scope,
done-or-handoff operation, with narrow validation named explicitly. Broad gates
belong to release-prep, registry-sync, lane-contract changes, or user-requested
verification.

Reference:

- [Introducing GPT-5.3-Codex-Spark](https://openai.com/index/introducing-gpt-5-3-codex-spark/)
- [Codex Use Cases](https://developers.openai.com/codex/use-cases/)

## Technique-Canon Adaptation

`aoa-techniques` cannot copy the center scenarios blindly.

The center owns AoA civic direction. This repository owns reusable public
practice. Spark here must therefore optimize for one atomic technique move,
public-safe wording, topology honesty, generated parity, and owner boundaries.

Spark must not:

- promote a candidate into canon by proximity;
- turn a technique into a skill, eval, route, playbook, role, memory object, or
  runtime behavior;
- smuggle private donor residue, host paths, raw logs, or project folklore into
  public technique text;
- treat generated catalogs, capsules, or source-lift outputs as authored
  meaning;
- invent validation commands not named by the owner surface.

Spark should be good at:

- small read-only audits of boundedness, duplicate meaning, stale paths, and
  public hygiene;
- one existing technique refinement with local validation;
- donor or legacy scout work that maps likely active homes without deep
  distillation;
- compact diff review against technique contracts and generated parity;
- registry or generated-surface sync when the source owner is already clear;
- release-prep checks that name public-claim and validation risk without
  publishing.

## Local Implementation Status

`aoa-techniques` now has the center-grade Spark lane shape:

- `.agents/spark/AGENTS.md`
- `.agents/spark/SWARM.md`
- `.agents/spark/README.md`
- `.agents/spark/registry.json`
- `.agents/spark/scenarios/**`
- `.agents/spark/schemas/**`
- `.agents/spark/scripts/validate_spark_lane.py`
- `.agents/spark/tests/test_spark_lane.py`
- `.agents/spark/results/`
- `.agents/spark/handoffs/open/`
- `.agents/spark/handoffs/closed/`
- `docs/decisions/2026-05-14-spark-agent-lane-home.md`
- AGENTS mesh registration for `.agents/spark/AGENTS.md`

Spark lane validation is wired into `scripts/release_check.py`.

The registry's per-scenario `default_validation` values are validation routes.
They are intentionally not all broad executable commands: audit, scout,
refinement, and test-factory work should name the narrow check that matches the
touched source surface, while release-prep and lane-contract sync can run
broader gates.

## Target Structure

The adapted lane should grow toward:

```text
.agents/spark/
  AGENTS.md
  README.md
  SWARM.md
  registry.json
  handoffs/
    README.md
    open/README.md
    closed/README.md
  results/
    README.md
  scenarios/
    README.md
    technique-audit/
      README.md
      PROMPT.md
      templates/result.md
      templates/handoff.md
      examples/result.example.md
    technique-refinement/
    candidate-scout/
    diff-review/
    registry-sync/
    test-factory/
    release-prep/
  schemas/
    spark-registry.schema.json
    spark-result.schema.json
    spark-handoff.schema.json
  scripts/
    validate_spark_lane.py
  tests/
    test_spark_lane.py
```

## Scenario Sketches

### `technique-audit`

Use for read-only audit of one technique, shelf, root route surface, or
generated reader seam.

Done signal: findings are evidenced, scoped, and routed to the technique
bundle, docs contract, mechanic, generated builder, or sibling owner.

Stop-line: do not edit during audit-only work.

### `technique-refinement`

Use for one small source-backed patch to an existing technique bundle.

Done signal: the technique is more atomic, portable, sanitized, and
reviewable, with validation named and run.

Stop-line: stop when the patch asks for a second technique, skill workflow,
playbook sequence, eval proof, runtime behavior, or sibling-owner decision.

### `candidate-scout`

Use for donor, legacy, or mechanic-local material that might become one
technique later.

Done signal: likely active homes, rejected material, portability concerns, and
next owner route are named.

Stop-line: do not perform deep semantic distillation or canon promotion inside
scout mode.

### `diff-review`

Use for a concrete diff or PR touching technique meaning, route docs, generated
parity, validators, or mechanics-to-canon edges.

Done signal: findings are ordered by severity and tied to exact paths.

Stop-line: do not rewrite the diff while acting as reviewer.

### `registry-sync`

Use when a route, registry, generated companion, validator, README, or AGENTS
surface needs alignment after a file moved or appeared.

Done signal: source, registry, docs, validator, and generated mirror agree.

Stop-line: do not create a new source of truth while syncing derived routes.

### `test-factory`

Use to add bounded tests for an existing technique contract, validator, or
generated-parity rule.

Done signal: tests prove a named existing contract and pass locally.

Stop-line: do not invent new semantics to make tests interesting.

### `release-prep`

Use for a fast readiness pass before publication, release support, or GitHub
landing hardens a claim.

Done signal: changed surfaces, checks, public-claim risks, generated parity,
and owner routes are named.

Stop-line: do not publish, tag, push, or merge without an explicit user
command.

## Implementation Order Used

1. Keep `.agents/spark/AGENTS.md` as the local operating card.
2. Add `.agents/spark/README.md`, storage README files, registry, schemas,
   scenarios, validator, and validator tests in one bounded change.
3. Adapt the `Agents-of-Abyss` validator with `aoa-techniques` constants,
   required scenario markers, and release-check integration.
4. Wire the Spark lane validator into `scripts/release_check.py` only after the
   full lane exists.
5. Add tests that reject unregistered scenario directories and missing
   done-or-handoff markers.
6. Run:

```bash
python .agents/spark/scripts/validate_spark_lane.py
python -m unittest discover -s .agents/spark/tests -p 'test*.py'
python scripts/validate_agents_md_shape.py
python scripts/validate_agents_mesh.py
python scripts/build_agents_mesh_index.py --check
python scripts/validate_agents_mesh_index.py
python scripts/validate_repo.py
python scripts/release_check.py
```

Adjust the test invocation if the final test module path cannot be imported as
a dotted module because `.agents` is hidden; the center repo uses direct pytest
collection for that reason.

## Open Design Questions

1. Should `technique-refinement` and `micro-patch` be separate scenarios, or
   should technique refinement be the local name for the micro-patch shape?
2. Should `candidate-scout` live only as a Spark scenario, or should deeper
   candidate handling remain exclusively under `mechanics/distillation/`?
3. Should Spark results ever be committed in `aoa-techniques`, or should most
   completed results stay in chat/PR closeout unless they are reusable
   examples?
4. Should release-check always run Spark validation once the lane exists, or
   only validate Spark when `.agents/spark/` changed?
5. Should the final registry include `quest-triage`, or is quest routing better
   left to `mechanics/questbook/` until a concrete Spark use case exists?

## Non-Negotiables For The Future Pass

- Keep Spark under `.agents/spark/`.
- Keep Spark Codex-specific unless a decision record renames the lane.
- Use registry-backed scenarios, not loose prompt files.
- Preserve `done-or-handoff`.
- Keep technique bundle meaning stronger than Spark instructions.
- Keep generated outputs weaker than source builders and docs.
- Validate scenario shape and release-check wiring.
- Add a decision update only if the future pass changes the lane contract, not
  merely because it fills in the planned structure.
