# Adverse Effects Review

## Technique
- id: AOA-T-0017
- name: property-invariants

## Review focus
- current role: canonical default for invariant-oriented coverage when one stable truth should constrain behavior across many cases
- current watch seam: keep the technique centered on meaningful invariant design rather than generic "stronger tests" language, generator theater, or contract-boundary drift

## Failure modes
- the chosen invariant is too weak to constrain real behavior
- generator or input assumptions become too broad or opaque to review
- the technique is applied where the real question is a consumer-visible contract, not invariant breadth

## Negative effects
- overly abstract invariant language can hide domain confusion behind polished testing vocabulary
- complex generators can slow debugging without increasing real confidence
- teams can skip a few clearer examples because the invariant framing sounds more sophisticated

## Misuse patterns
- writing properties like "should not fail" and calling them invariants
- treating random or wide input generation as proof by itself
- using `AOA-T-0017` as a substitute for `AOA-T-0015 contract-test-design`
- forcing invariant coverage onto presentation-only or narrow snapshot behavior

## Detection signals
- reviewers cannot explain why the invariant matters to the domain
- the generated or repeated input space grows, but the actual constraint on behavior stays weak
- boundary-stability questions keep appearing even though the bundle is framed as invariant coverage
- failing cases are noisy, but the report cannot say what stable truth was violated

## Mitigations
- rewrite the check around one stronger domain truth
- narrow the input strategy to meaningful ranges first
- pair the invariant with a few clear examples when readability is the limiting factor
- route boundary-definition questions back to `AOA-T-0015` instead of stretching this technique

## Recommendation
- keep current `canonical` status and use this note as the watch surface for weak invariants, opaque generator assumptions, and contract-boundary drift
