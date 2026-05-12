# Canonical Readiness

## Technique
- id: AOA-T-0042
- name: upstream-skill-health-checking

## Verdict
- not approved for canonical promotion yet

## Evidence summary
- origin evidence is strong enough to justify a promoted public bundle
- the second context adaptation kept the contract bounded around source availability and manifest-readiness before surfacing
- the bundle now has a checklist and a public-safe example, but the pattern is still strongest through one wave of adjacent discovery infrastructure rather than multiple independent downstream consumers
- 2026-05-12 Pack 5 search found useful adjacent skill-ecosystem surfaces, including `shskills` manifest plus `doctor`, `fast-agent` registry-backed skill install/update behavior, and Aescut registry risk checks, but each widens into install state, managed registry behavior, security or permission review, or update/doctor commands rather than the same minimal pre-surface source availability plus manifest-readiness verdict

## Default-use rationale
- this is useful when the missing object is a bounded readiness verdict over upstream-owned skill sources before they become selectable inputs
- it is strongest when reviewers need a smaller answer than full registry governance, monitoring, or security policy
- it is not yet proven as the default evaluation pattern for every upstream registry, marketplace, or import pipeline
- the current evidence supports promotion, but not canonical status

## Fresh public-safety check
- review date: 2026-03-23
- result: pass
- sanitization still holds: the published technique keeps the source-readiness contract while stripping donor-specific registry brands, URLs, auth flows, and scanner products

## Remaining gaps
- the bundle would benefit from a second independent downstream consumer that uses the same pre-surface readiness boundary
- the separation from monitoring, curation, and security scanning should stay tested through future sibling imports
- the next honest search shape is a public source-intake or catalog-publish workflow that checks one upstream skill source for reachability plus minimal `SKILL.md` or manifest parseability before surfacing it, without adding install/update management, security scoring, registry governance, or generic monitoring

## Recommendation
- keep `AOA-T-0042` as `promoted`
- revisit canonical readiness only after at least one more live context proves the same upstream source-readiness contract
