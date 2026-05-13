# Adverse Effects Review

## Technique
- id: AOA-T-0078
- name: decision-fork-cards
- current role: bounded canonical default

## Review focus

Review the effects of making explicit branch cards the default move when one
reviewed source still leaves materially different next routes.

## Failure modes

- cards describe cosmetic variants of the same route
- a preferred path is hidden as if no alternatives exist
- route cards omit costs, risks, owner targets, or stop conditions
- branch cards are mistaken for runtime routing authority

## Negative effects

- too many thin cards can create fake complexity
- unresolved cards can encourage analysis loops when one route is already
  obvious
- downstream playbooks or summon gates may inherit branch noise if the route set
  is not pruned

## Misuse patterns

- writing fork cards before reviewed evidence exists
- hiding a decision already made by only decorating the chosen route
- using cards as a replacement for playbook design or route policy
- turning quest-board vocabulary into execution authority

## Detection signals

- card differences are mostly names or tone
- each card lacks at least one concrete downside
- stop conditions are missing for risky or expensive routes
- a downstream consumer treats the card set as permission to act

## Mitigations

- require materially distinct routes
- keep one gain, cost, risk, owner cue, and stop condition visible per route
- preserve hold, defer, or reanchor when uncertainty is honest
- keep route passports and execution gates separate from card authorship

## Recommendation

Keep the canonical bundle and use this note as one bounded watch surface. Future
changes should keep fork cards advisory and branch-local without widening them
into playbook scenario design, summon authorization, routing policy, proof
verdicts, or hidden recommendation machinery.
