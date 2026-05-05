# Second Context Adaptation

## Technique

- id: AOA-T-0100
- name: stress-receipt-reground-closeout

## Target project

- a runtime substrate, routing layer, playbook layer, or control surface where
  one bounded stress event must stay visible from receipt through closeout

## What changed

- receipt schema names can change
- the next bounded hop can point to routing, playbooks, KAG, or a local review surface
- the degraded continuation may stay active or become an explicit hold
- closeout storage paths and review mechanics can change

## What stayed invariant

- one owner-local receipt comes first
- degraded posture stays weaker than the normal path
- blocked widening remains explicit
- reviewed closeout arrives before stronger proof reading
- eval bridge candidates stay evidence-only until a real eval consumes them

## Risks introduced by adaptation

- a target repo may copy the wording while skipping the actual reviewed closeout artifact
- routing or playbook consumers may overstate their role and obscure owner-local evidence
- adaptation can get mistaken for blanket incident doctrine instead of one bounded recovery workflow

## Evidence

- the donor pack already showed the workflow across several owner layers, which
  demonstrates that the sequence travels better than any single example file
- the technique depends on boundary discipline more than on one particular
  runtime, registry, or generated surface layout

## Result

- the technique remains portable across owner repos as long as they preserve:
  one owner-local receipt, one honest degraded continuation or hold, one
  reviewed closeout artifact, and an explicit weaker-than-verdict eval bridge
