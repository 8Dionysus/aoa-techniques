# Second Context Adaptation

## Technique
- id: AOA-T-0040
- name: skill-vs-command-boundary

## Target project
- name: aoa-techniques
- environment: public documentation repository for reusable engineering techniques
- runtime: documentation-first canon with neighboring `aoa-skills` and `aoa-routing` source surfaces

## What changed
- donor-specific plugin install flows, review-agent catalogs, and orchestrator behavior were removed
- the donor's slash-command surface was generalized into any explicit user-facing command artifact
- the second context now uses `aoa-skills` to show that local commands and overlays may change while the base skill boundary remains stable
- the second context also uses `aoa-routing` to show that navigation and dispatch stay separate from skill-owned meaning

## What stayed invariant
- reusable capability meaning stays in the skill artifact
- invocation syntax, steps, and output stay in the command artifact
- downstream wrappers and routing surfaces remain subordinate to source-owned skill meaning
- the same skill can still be referenced by more than one consumer without becoming command-local

## Risks introduced by adaptation
- the public wording could drift into a vague taxonomy if the ownership split is not restated clearly
- the bundle could overreach into routing or shell-command design if user entrypoints become the center of gravity
- a minimal example can look too thin if it does not show both an agent-facing skill reference and a user-facing command

## Evidence
- `aoa-skills/docs/OVERLAY_SPEC.md` explicitly says local overlays may change paths and commands but must not change the base skill boundary
- `aoa-skills/generated/skill_catalog.min.json` keeps skills as source-owned artifacts with their own path, scope, and invocation metadata
- `aoa-routing/README.md` and `aoa-routing/generated/task_to_surface_hints.json` keep `skill` as a separate source kind with inspect and expand surfaces instead of turning routing hints into skill meaning

## Result
- verdict: works
- note: the adapted bundle stays readable as a bounded docs technique for artifact ownership between reusable skills and command entrypoints
