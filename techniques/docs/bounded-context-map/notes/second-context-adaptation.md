# Second Context Adaptation

## Technique
- id: AOA-T-0016
- name: bounded-context-map

## Target project
- name: aoa-techniques
- environment: public documentation repository for reusable engineering techniques
- runtime: human+agent contribution workflow over reviewable repository changes

## What changed
- adaptation path: the context-mapping pattern was extracted into one focused public docs/scoping bundle rather than opening a separate architecture domain
- scoping surface: origin-specific planning-layer boundary pressure was rewritten as repo-agnostic vocabulary, responsibility, and handoff framing for public-safe reuse
- support surfaces: the public form now includes a bounded checklist, a minimal example, an origin note, and derived repository manifests
- operating assumptions: contributors need a compact way to reduce semantic confusion before implementation or evaluation work widens into the wrong area

## What stayed invariant
- contract: the technique still names visible responsibility boundaries rather than creating taxonomy for its own sake
- scoping value: the main goal remains reducing semantic confusion and making handoff or interface points explicit enough for future reviewers
- reporting: the result still constrains later work by clarifying what belongs inside the target context and what should stay outside it

## Risks introduced by adaptation
- the technique can drift into generic architecture formalism if future examples stop being scoping- and handoff-centric
- public vocabulary can encourage over-structuring if later notes present context maps as default ceremony rather than as a response to real ambiguity
- broad architectural language can hide the technique's practical docs/scoping role if contributors stop tying the map back to bounded change decisions

## Evidence
- The focused landing into `aoa-techniques` kept the pattern in `docs` as a scoping technique rather than using it to justify a new architecture-domain opening.
- The public checklist and minimal example still center vocabulary drift, responsibility clarity, and visible handoff notes instead of abstract platform modeling.
- The later `Skill-Support Semantic Review` preserved `AOA-T-0016` as a docs/scoping pattern and identified architecture-formalism drift as a watch seam without justifying remediation or domain expansion.

## Result
- verdict: works
- note: the technique remained readable and bounded as a docs/scoping pattern after public shaping into `aoa-techniques`
