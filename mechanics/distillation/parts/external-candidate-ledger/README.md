# External Candidate Ledger

This active ledger records the current external donor-derived technique
candidate accounting for `aoa-techniques`. It is intentionally compact: use it
to decide the current route, not to replay every wave note.

The detailed pre-prune receipt is preserved at
[legacy/raw/EXTERNAL_CANDIDATE_LEDGER_2026-05-01_PRE_PRUNE.md](../../legacy/raw/EXTERNAL_CANDIDATE_LEDGER_2026-05-01_PRE_PRUNE.md).

It does not change technique status, create a new bundle, or authorize import by
itself.

## Source Status

The `seed_4.txt` and `seed_6.txt` names are retained as historical source
labels. A workspace search on 2026-05-01 did not find checked-out
`seeds/seed_4.txt` or `seeds/seed_6.txt` files under `/srv/AbyssOS`.

Therefore this active ledger is the current reviewable accounting surface for
those historical labels, not a claim that the raw seed files are present in this
checkout.

## Scope

- this ledger tracks the remaining `13` external donor-derived candidates
- it excludes already-landed external imports now owned by technique bundles
- it keeps `phase_sync_for_agents` as the only active narrowing lane
- it keeps overlap, incubation, and substrate items visible without expanding
  them into active wave notes

## Current Summary

- `0` ready to distill here
- `1` future import here
- `4` hold because overlap
- `5` needs layer incubation before distillation here
- `3` substrate or architecture pattern, not yet a technique

## Structured Registry

The part-local registry keeps the compact ledger machine-checkable without
turning it into technique canon:

- [config/external_candidate_registry.seed.json](config/external_candidate_registry.seed.json)
  carries the structured candidate accounting.
- [generated/external_candidate_registry.min.json](generated/external_candidate_registry.min.json)
  is derived evidence for counts, gates, donors, and the active narrowing lane.
- [schemas/](schemas/) and [examples/](examples/) document the expected entry
  shape.
- [scripts/build_external_candidate_registry.py](scripts/build_external_candidate_registry.py)
  builds the derived index, and
  [scripts/validate_external_candidate_registry.py](scripts/validate_external_candidate_registry.py)
  verifies that the index still matches the seed.

The registry must preserve this README's candidate statuses and stop line. It
does not create technique bundles, change candidate status, or authorize import
without bundle-local review.

Validation:

```bash
python mechanics/distillation/parts/external-candidate-ledger/scripts/build_external_candidate_registry.py --check
python mechanics/distillation/parts/external-candidate-ledger/scripts/validate_external_candidate_registry.py
python -m pytest -q mechanics/distillation/parts/external-candidate-ledger/tests/test_external_candidate_registry.py
```

## Current Active Lane

| seed candidate | donor | suggested technique name | tentative domain | status | current gate |
|---|---|---|---|---|---|
| `phase_sync_for_agents` | `agentwise` | `phase-synchronized-agent-handoff` | `agent-workflows` | `future import here` | keep as active narrowing lane until public evidence exposes a standalone phase boundary, handoff packet, continuation permission, and stop/return/escalation rule |

Current donor read remains no-go for drafting: public material checked on
2026-03-23 still presents phase sync inside broad orchestration rather than as a
standalone handoff contract. The active lane must stay narrower than model
routing, shared context server behavior, token optimization, dynamic specialist
generation, registry behavior, and dashboard monitoring.

Nearest overlap watch:

- [AOA-T-0001](../../../../techniques/execution/agent-workflows-core/plan-diff-apply-verify-report/TECHNIQUE.md)
  owns the broader multi-step change loop.
- [AOA-T-0023](../../../../techniques/execution/agent-workflows-core/stateless-single-shot-agent/TECHNIQUE.md)
  owns the single-shot fast path.
- `bounded-specialist-generation` remains an adjacent incubation lane, not part
  of this handoff contract.

## Candidate Accounting

### Future Import Here

| seed candidate | donor | suggested technique name | tentative domain | next move |
|---|---|---|---|---|
| `phase_sync_for_agents` | `agentwise` | `phase-synchronized-agent-handoff` | `agent-workflows` | reopen only when public evidence names the phase boundary, packet, continuation permission, and stop/return/escalation rule |

### Hold Because Overlap

| seed candidate | donor | suggested technique name | tentative domain | overlap watch |
|---|---|---|---|---|
| `external_sync_manifest` | `n-skills` | `external-sync-manifest` | `docs` | too close to [AOA-T-0024](../../../../techniques/instruction/instruction-surface/upstream-mirroring-with-provenance/TECHNIQUE.md) unless sync control separates from provenance-backed mirroring |
| `project_memory_bootstrap` | `OpenMemory-Code` | `project-history-bootstrap` | `history` | too close to [AOA-T-0026](../../../../techniques/history/history-artifacts/session-capture-as-repo-artifact/TECHNIQUE.md) unless it narrows to history bootstrap without memory substrate semantics |
| `context_injection_for_coding_agents` | `agents-md` | `bounded-context-injection-for-coding-agents` | `docs` | overlaps [AOA-T-0012](../../../../techniques/instruction/instruction-surface/deterministic-context-composition/TECHNIQUE.md) and [AOA-T-0023](../../../../techniques/execution/agent-workflows-core/stateless-single-shot-agent/TECHNIQUE.md) until injection becomes the distinct contract |
| `single_step_agent` | `qqqa` | `single-step-confirmed-agent-action` | `agent-workflows` | too close to [AOA-T-0023](../../../../techniques/execution/agent-workflows-core/stateless-single-shot-agent/TECHNIQUE.md) unless the center becomes one-step mutating confirmation |

### Needs Layer Incubation Before Distillation Here

| seed candidate | donor | suggested technique name | tentative domain if later imported | incubation need |
|---|---|---|---|---|
| `memory_enforcement_layers` | `OpenMemory-Code` | `layered-memory-enforcement` | not in current domain map | needs a stable public-safe memory-layer contract before extraction |
| `history_to_instructions` | `SpecStory` | `review-gated-history-derived-instructions` | not in current domain map | needs an invariant review gate so history does not become hidden instruction authority |
| `dynamic_specialist_generation` | `agentwise` | `bounded-specialist-generation` | `agent-workflows` only after narrowing | needs a stable specialist-scope and handoff contract separated from orchestration |
| `persistent_agent_registry` | `agentic` | `versioned-agent-registry-contract` | `docs` only after spec extraction | needs registry semantics separated from stateful runtime registry implementation |
| `execution_history_learning` | `agentic` | `review-gated-execution-history-distillation` | not in current domain map | needs an explicit distillation contract subordinate to human review |

### Substrate Or Architecture Pattern, Not Yet A Technique

| seed candidate | donor | why it is not technique-shaped yet | what would have to change |
|---|---|---|---|
| `shared_context_server` | `agentwise` | shared runtime substrate with state and coordination semantics | extract a smaller public-safe context-sharing handoff contract above the server layer |
| `token_optimization_by_context_sharing` | `agentwise` | performance strategy tied to caching and product tradeoffs | extract one reviewable context reuse discipline, not generalized token optimization |
| `agent_self_assembly` | `agentic` | architecture cluster around runtime composition of agents from capabilities and constraints | extract one smaller contract, such as bounded capability selection or bounded assembly review |

## Landed External Anchors

The old wave notes are no longer active execution instructions, but their
landed anchors remain useful for route memory:

- Wave A external anchor: [AOA-T-0038](../../../../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md)
- Wave B external anchor: [AOA-T-0041](../../../../techniques/instruction/skill-discovery/skill-marketplace-curation/TECHNIQUE.md)
- Wave C external anchor: [AOA-T-0044](../../../../techniques/history/history-artifacts/versionable-session-transcripts/TECHNIQUE.md)
- adjacent landed imports from the earlier external backlog include
  [AOA-T-0027](../../../../techniques/instruction/instruction-surface/cross-agent-skill-propagation/TECHNIQUE.md),
  [AOA-T-0028](../../../../techniques/execution/agent-workflows-core/confirmation-gated-mutating-action/TECHNIQUE.md),
  [AOA-T-0029](../../../../techniques/instruction/instruction-surface/nested-rule-loading/TECHNIQUE.md),
  [AOA-T-0030](../../../../techniques/instruction/instruction-surface/fragmented-agent-context/TECHNIQUE.md),
  [AOA-T-0031](../../../../techniques/execution/agent-workflows-core/shell-composable-agent-invocation/TECHNIQUE.md),
  [AOA-T-0032](../../../../techniques/proof/evaluation-chain/context-report-for-ci/TECHNIQUE.md),
  [AOA-T-0042](../../../../techniques/instruction/skill-discovery/upstream-skill-health-checking/TECHNIQUE.md),
  [AOA-T-0043](../../../../techniques/instruction/capability-boundary/multi-source-primary-input-provenance/TECHNIQUE.md),
  and [AOA-T-0045](../../../../techniques/history/history-artifacts/witness-trace-as-reviewable-artifact/TECHNIQUE.md)

For exact wave execution roles, public donor-read details, and the old expected
first import package, use the preserved raw receipt.

## Reopen Gate

Reopen a candidate from this ledger only when the active ledger row and
structured registry seed can carry the same Distillation gate packet.

Atom/topology gate:

- `atomic_move_note`: the one executable move being extracted
- `atomic_move_status`: named or still not named cleanly
- likely `domain` and primary `kind`
- likely family or reason no family is stable yet
- capability class, substrate, execution profile, and risk posture
- bounded reusable practice being extracted
- nearest landed technique or overlap watch

Boundary/portability gate:

- `higher_law`: the source owner or layer whose authority and stop lines matter
  for extraction
- `local_route`: why this row should stay held, move to incubation, or enter
  import review
- `bridge_stop_line`: what must not cross from donor into technique canon
- what remains portable outside OS Abyss
- `aoa_only_context` or equivalent note for local integration context
- what stays out of the donor

Accounting gate:

- evidence package needed for the current maturity claim
- generated or indexed surfaces expected to change
- registry seed update before any generated index is rebuilt

If those cannot be named, keep the candidate in this ledger rather than drafting
a technique bundle. Do not change status in the generated registry directly;
change the seed and let validation rebuild evidence.
