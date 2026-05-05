# Second Context Adaptation

## Technique
- id: AOA-T-0097
- name: degrade-reground-recover

## Target project
- a runtime substrate, routing layer, or operator-facing control surface where one helper stage can weaken while a smaller truthful mode still exists

## What changed
- the surface names can change
- the fallback mechanics can change
- the receipt storage path can change
- the stronger authority used for regrounding can change

## What stayed invariant
- degraded mode stays weaker, not broader
- regrounding leans on stronger owner-local authority
- the stress event leaves one source-owned receipt
- later recovery remains a reviewed adaptation step instead of hidden auto-repair

## Risks introduced by adaptation
- a target repo may copy the language while skipping the explicit reground step
- receipt naming may drift if the target project already uses overloaded degraded-state terms
- adaptation can get mistaken for blanket runtime guidance instead of one bounded recovery posture

## Evidence
- the origin `ATM10-Agent` landing already demonstrated that the posture can be expressed through docs, schemas, and one bounded live receipt path
- the sequence depends on authority discipline more than on any one storage or transport detail

## Result
- the technique remains portable across owner repos as long as they preserve weaker degraded mode, stronger reground authority, one source-owned receipt, and reviewed recovery changes
