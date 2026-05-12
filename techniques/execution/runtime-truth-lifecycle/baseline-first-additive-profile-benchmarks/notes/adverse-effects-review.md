# Adverse Effects Review

## Technique

- id: AOA-T-0039
- name: baseline-first-additive-profile-benchmarks

## Review focus

- current role: canonical default for baseline-first additive benchmark comparison discipline
- current watch seam: keep the bundle centered on same-surface comparison rather than benchmark-suite governance, product scoring, promotion policy, rolling baseline management, or runtime lifecycle control

## Failure modes

- additive setup mutates the baseline path, so the comparison stops being like-for-like
- baseline and additive runs produce different artifact shapes or use different measurement surfaces
- benchmark results are treated as product rankings or promotion decisions
- a rolling historical baseline replaces the explicit current baseline-first contract

## Negative effects

- insisting on a baseline-first run can add overhead when a quick smoke comparison would be enough
- additive prework can become elaborate enough to hide setup differences
- a shared summary shape can mask semantic differences if fields are not interpreted carefully
- canonical status can encourage teams to over-formalize small experiments as benchmark programs

## Misuse patterns

- using the technique to crown a winner rather than compare bounded profile shapes
- treating additive backends, plugins, profiles, or richer setup as the new default path
- folding benchmark-suite ownership, leaderboard policy, promotion decisions, or product scoring into the technique
- widening the bundle into profile composition, render truth, host readiness, service lifecycle, or regression-gate policy

## Detection signals

- default runs now require additive-only setup
- baseline and additive outputs no longer contain the same summary fields
- comparison notes use ranking, acceptance, or promotion language instead of bounded deltas
- reviewers cannot identify which prework was isolated for additive profiles

## Mitigations

- run the stable baseline first and keep it visible as the reference point
- require the same measurement surface and artifact shape for every compared run
- isolate additive prework in a separate script, workflow step, or operator note
- report bounded deltas and explicitly reject product-scoring or promotion-policy claims
- route profile composition, rendered truth, host readiness, lifecycle, and proof authority to sibling techniques or owner repos

## Recommendation

- keep current `canonical` status and use this note as the watch surface for false comparability, additive-default drift, benchmark-governance expansion, and product-scoring overreach
