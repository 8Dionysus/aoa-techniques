# Adverse Effects Review

## Technique

- id: AOA-T-0029
- name: nested-rule-loading

## Review focus

- current role: canonical default for hierarchical rule loading with explicit, reviewable precedence
- current watch seam: keep the bundle centered on parent/nested layer order rather than multi-target propagation, fragment hygiene, runtime injection, hidden prompt control, or product-width memory behavior

## Failure modes

- precedence becomes implicit and reviewers cannot explain why one instruction layer wins
- nested layers start carrying shared policy that should live in the parent source
- lazy or conditional loading hides important scoped rules from review
- hierarchical loading is treated as a general import system without an ownership or precedence contract

## Negative effects

- layered rules can make simple instructions harder to audit
- closer or later-loaded files can accidentally shadow broader guidance
- overuse of nested layers can fragment shared meaning and create local exceptions as default behavior
- canonical status can make teams add hierarchy before a flat instruction surface has actually become insufficient

## Misuse patterns

- using the bundle for one-source fan-out that belongs to `AOA-T-0013`
- using the bundle for managed skill or rule propagation that belongs to `AOA-T-0027`
- using hierarchy as a way to hide target-specific policy or prompt-control tricks
- treating all topic-file organization as nested-rule loading even when no precedence decision exists

## Detection signals

- reviewers cannot list parent, nested, and local layers in the order they load
- a nested layer is cited as the real source of a shared rule
- removing one scoped layer changes unrelated instruction behavior
- discussions focus on product memory features rather than rule hierarchy, scope, and precedence

## Mitigations

- document the loading order beside the hierarchy
- route shared rules back to the parent source when a nested layer starts carrying general policy
- keep nested layers small, scoped, and easy to remove
- verify loaded context or resolved output when precedence changes
- split target fan-out, fragment authoring, runtime injection, and hidden prompt-control behavior into sibling techniques or owner repos

## Recommendation

- keep current `canonical` status and use this note as the watch surface for implicit precedence, nested-source drift, over-layering, and sibling-boundary widening around the instruction-surface cluster
