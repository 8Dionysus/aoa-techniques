# Canonical Readiness

## Technique
- id: AOA-T-0039
- name: baseline-first-additive-profile-benchmarks

## Verdict
- approve for canonical promotion

## Evidence summary
- origin evidence is strong enough to justify a promoted public bundle
- LOCOMO/OpenClaw now provides an exact-fit public second context: `memory-core` is the baseline, `memory-lancedb` and `memory-lancedb-pro` are additive backend comparisons, all runs share the LOCOMO rows, gateway/judge path, and run artifact family, and additive prework stays isolated through prebuilt stores and plugin setup
- the second context adaptation keeps the contract bounded around baseline-first additive comparison discipline rather than benchmark-suite ownership, product ranking, leaderboard policy, or rolling historical baseline governance
- the bundle now has a checklist, a public-safe example, origin evidence, exact-fit second-context evidence, and an adverse-effects review

## Default-use rationale
- this is the right canonical default when one stable baseline must anchor a comparison before richer profiles are evaluated
- it is strongest when additive profiles should remain off the default path
- it remains narrower than benchmark-suite governance because it only owns comparison discipline: same measurement surface, same artifact shape, baseline first, additive second
- LOCOMO/OpenClaw confirms that the default move can survive outside `atm10-agent`: baseline backend first, additive backend legs later, prework isolated, and summaries comparable without turning the result into product scoring

## Fresh public-safety check
- review date: 2026-05-12
- result: pass
- sanitization still holds: the published technique keeps the reusable comparison contract while stripping donor-specific service names, workflow paths, and private benchmark labels
- public-safety boundary: LOCOMO/OpenClaw evidence is cited for comparison discipline, not as a universal memory benchmark, model judgement policy, product ranking, or plugin endorsement

## Remaining gaps
- no blocking promotion gap remains as long as the bundle stays centered on same-surface baseline/additive comparison discipline
- future review should reject benchmark matrices, A/B tests, product leaderboards, rolling baselines, or regression gates unless they preserve baseline-first ordering, additive isolation, and same artifact shape

## Recommendation
- promote `AOA-T-0039` to `canonical`
- use `AOA-T-0039` as the default benchmark-comparison technique when richer profiles or backends must remain additive and comparable against one stable baseline without owning policy or product scoring
