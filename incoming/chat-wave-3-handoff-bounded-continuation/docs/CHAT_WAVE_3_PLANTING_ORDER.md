# Chat Wave 3 - Planting Order

This note is for operator-guided staging inside `aoa-techniques`.

## Hard rules

- keep all Wave 3 seed bundles under `seed_bundles/agent-workflows/` on the first pass
- do not assign `AOA-T-XXXX` ids from worker-owned wave tasks yet
- do not absorb governed actions into the handoff lane
- do not edit `TECHNIQUE_INDEX.md`, `generated/**`, or repo-wide queue docs from worker-owned tasks

## Landed first

1. `structured-handoff-before-compaction` is now landed as `AOA-T-0057` by the main agent
2. `receipt-confirmed-handoff-packet` is now landed as `AOA-T-0058` by the main agent
3. `git-verified-handoff-claims` is now landed as `AOA-T-0059` by the main agent
4. `session-opening-ritual-before-work` is now landed as `AOA-T-0060` by the main agent
5. `cross-repo-resource-map-bootstrap` is now landed as `AOA-T-0061` by the main agent
6. `episode-bounded-agent-loop` is now landed as `AOA-T-0062` by the main agent

## Preferred sequence

No remaining `draft-now` candidates.

## Explicit exclusion to leave closed

- `governed-action-surfaces`

## Stop conditions

Stop and restage instead of forcing a seed if:

- the candidate needs generic orchestration doctrine to explain itself
- the seed collapses into mailbox transport instead of a handoff contract
- the seed needs governance or policy surfaces to stay coherent
- the handoff object cannot say what is handed off, what must be verified, and when continuation must stop
