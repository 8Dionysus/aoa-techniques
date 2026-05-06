# Canonical Readiness

## Technique
- id: AOA-T-0096
- name: pinned-validation-matrix-before-generated-publish

## Verdict
- not approved for canonical promotion yet

## Evidence summary
- origin evidence is strong enough to justify a promoted public bundle
- the adapted bundle keeps the contract narrow around generated publish and
  workflow-pinned validation inputs
- the bundle now has a checklist and a public-safe example, and the
  via-negativa owner wave added a second live replay of the same bounded
  failure family
- live evidence is stronger than it was at first promotion, but it is still
  concentrated in the current AoA generated-surface sibling family

## Default-use rationale
- this is useful when generated outputs depend on sibling surfaces or mirrored
  contracts that CI pins more strictly than a local workspace does
- it is strongest when publish risk comes from false local confidence rather
  than from ordinary code drift
- it is not yet proven as the default publish posture outside the current AoA
  cross-repo generated-surface context

## Fresh public-safety check
- review date: 2026-04-08
- result: pass
- sanitization still holds: the published technique keeps the bounded
  pinned-matrix rule while stripping private runner setup, credentials, and
  broader release bureaucracy

## Remaining gaps
- the bundle would still benefit from a second live generated-surface repo
  outside the current `aoa-routing` and `aoa-skills` sibling family
- the via-negativa replay strengthens confidence, but it still replays the same
  family rather than proving a non-identical publish context
- the seam between upstream health checks, split-wave playbooks, and generated
  publish posture should stay explicit through future reuse

## Recommendation
- keep `AOA-T-0096` as `promoted`
- revisit canonical readiness only after at least one more non-identical
  generated-publish context proves the same pinned-matrix boundary
