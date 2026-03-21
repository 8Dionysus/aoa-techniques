# Canonical Readiness

## Technique
- id: AOA-T-0016
- name: bounded-context-map

## Verdict
- approved for canonical promotion

## Evidence summary
- origin evidence: the origin repeatedly needed a compact way to keep agent and human work semantically scoped when neighboring subsystems or concepts blurred together
- second context: the public `aoa-techniques` adaptation preserved the contract as a docs and scoping pattern rather than letting it drift into generic architecture formalism
- consumer evidence: the committed `aoa-bounded-context-map` skill wires `AOA-T-0016` through `techniques.yaml`, exposes the same contract in `SKILL.md`, and includes a concrete example with overloaded terminology and named handoff notes
- validation strength: the bundle now has origin evidence, a public second-context adaptation, and a committed downstream consumer with explicit section-level traceability

## Default-use rationale
- this is the default docs and scoping pattern when a repository needs to name neighboring responsibilities before changes widen into the wrong area
- the committed skill consumer shows the same contract is not just publishable but actually selected as a bounded default in another repo, which is enough for default-use approval

## Fresh public-safety check
- review date: 2026-03-20
- result: pass
- sanitization still holds: the published technique keeps only reusable boundary-mapping guidance and strips project-specific naming, local layout, and private operational detail
- public reuse check: the bundle and committed skill consumer are understandable without origin-project access and do not rely on hidden architecture context

## Remaining gaps
- a second independent consumer beyond `aoa-skills` would further strengthen breadth
- the technique still needs judgment to avoid use where no real ambiguity exists

## Recommendation
- approve `AOA-T-0016` for `promoted -> canonical` in this wave; the cross-context consumer evidence is strong enough for default-use approval, and the remaining risk is misuse scope rather than lack of reuse proof
