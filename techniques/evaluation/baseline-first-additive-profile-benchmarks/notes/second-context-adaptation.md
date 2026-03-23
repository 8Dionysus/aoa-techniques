# Second Context Adaptation

## Technique
- id: AOA-T-0039
- name: baseline-first-additive-profile-benchmarks

## Target project
- name: aoa-techniques
- environment: public documentation repository for reusable engineering techniques
- runtime: reviewable technique bundles with portable wording

## What changed
- donor-specific profile labels and service names were rewritten into a portable baseline-first comparison contract
- the cross-service benchmark path became a public-safe example of additive comparison discipline instead of a private suite recipe
- additive setup was kept separate from the default path so the benchmark reads as a comparison technique, not as a benchmark owner surface
- the bundle was reduced to one technique doc, one checklist, one example, and three evidence notes

## What stayed invariant
- the baseline still runs first
- additive profiles still reuse the same measurement surface
- the artifact shape still stays consistent across compared runs
- additive prework still stays off the default path
- the result still reports comparison discipline rather than product scoring

## Risks introduced by adaptation
- the public wording can drift into benchmark-suite governance if it starts describing ownership of the whole harness
- the bundle can widen into promotion policy if the comparison result is treated like a decision policy
- a generic example can become too abstract if it does not show why additive setup must stay isolated

## Evidence
- the public technique stays in `evaluation` because the reusable object is a bounded comparison contract rather than a composition or lifecycle technique
- the donor lineage already treats the baseline-first suite as a default path with an additive sibling path
- the adapted bundle preserves the key donor invariant: compare like with like, and keep richer profiles secondary

## Result
- verdict: works
- note: the adapted bundle stays readable as a bounded evaluation technique for stable baseline-plus-additive comparisons
