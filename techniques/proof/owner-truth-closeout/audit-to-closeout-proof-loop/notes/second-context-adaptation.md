# Second Context Adaptation

## Technique
- id: AOA-T-0092
- name: audit-to-closeout-proof-loop

## Target project
- name: aoa-techniques
- environment: public documentation repository for reusable engineering techniques
- runtime: human and agent contribution workflow over bounded technique bundles

## What changed
- the concrete repo list, audit filenames, and session-specific closeout narration were reduced to one reusable finding-first proof loop
- the local source-checkout exception for `abyss-stack` moved to adaptation guidance rather than the invariant core
- the bundle was reduced to one technique doc, one checklist, one example, and three evidence notes

## What stayed invariant
- reviewed findings still need live confirmation before patching
- each closed finding still needs one targeted proof seam
- broader repo-level closeout still reruns before the route can claim closure
- unresolved findings still stay explicit rather than disappearing into a green summary

## Risks introduced by adaptation
- the public wording can collapse into generic "test your fixes" advice if the named finding-first loop stops being central
- the bundle can drift toward scenario-level remediation choreography that belongs in `aoa-playbooks`
- the bundle can overfit to AoA audit habits if future contexts do not test different finding families

## Evidence
- the April 5 and April 6 remediation runs show the same proof boundary across different blocker families and repo mixes
- the adapted bundle stays in `agent-workflows` because the reusable object is one closure discipline, not a playbook or eval surface
- the origin evidence remains strong enough to justify a promoted bundle without importing local audit files or repo-private runtime detail

## Result
- verdict: works
- note: the adapted bundle stays readable as one bounded finding-first closeout law across more than one reviewed remediation context
