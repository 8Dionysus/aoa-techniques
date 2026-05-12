# Adverse Effects Review

## Technique
- id: AOA-T-0050
- name: ready-work-from-blocker-graph

## Review focus
- current role: canonical default for deriving a next-work queue from blocker-free graph state once an explicit dependency graph already exists
- current watch seam: keep the bundle centered on blocker-free eligibility, visible excluded reasons, and frontier refresh rather than widening into graph authoring, ranking policy, staffing, dispatch, full tracker behavior, or generic prioritization doctrine

## Failure modes
- stale blocker state yields a ready queue that no longer matches reality
- open-but-blocked tasks leak into the frontier because dependency truth is ignored
- secondary ordering hints quietly replace blocker-free eligibility
- manual overrides happen without a visible reason
- the queue is treated as a complete prioritization policy instead of a readiness filter

## Negative effects
- operators may trust an outdated queue too much
- a narrow readiness surface can look like full prioritization if ranking is not kept separate
- queue maintenance can add friction when there is only one obvious next step
- blocker-first selection can hide urgent work if urgency is not routed to a later, explicit prioritization layer

## Misuse patterns
- mixing readiness derivation with broad backlog ranking, staffing, or scheduling doctrine
- using the queue to author the graph instead of deriving from an existing graph
- treating all open work as ready because it is visible in the same system
- making local overrides without recording why blocker truth was bypassed

## Detection signals
- excluded tasks do not show blocked reasons
- a blocked task appears in the ready queue
- queue order cannot be explained from visible inputs after blocker-free eligibility is checked
- arguments about priority happen before blocker-free eligibility is established
- the queue becomes the only work planning surface instead of handing off to execution and review

## Mitigations
- recompute the frontier after each meaningful graph or state change
- keep blocked exclusions visible
- apply secondary ordering only after blocker-free eligibility is established
- route graph authoring back to `AOA-T-0049`
- route ranking, staffing, dispatch, and tracker policy to separate owner surfaces

## Recommendation
- move `AOA-T-0050` to `canonical` and use this note as the watch surface for stale-frontier drift, ranking-policy drift, graph-authoring drift, hidden-override drift, and tracker-doctrine drift
