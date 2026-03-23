# Origin Evidence

## Technique
- id: AOA-T-0043
- name: multi-source-primary-input-provenance

## Source project
- name: `aoa-kag` plus `Tree-of-Sophia`
- source files:
  - `aoa-kag/docs/BRIDGE_CONTRACTS.md`
  - `aoa-kag/examples/tos_retrieval_axis_surface.example.json`
  - `aoa-kag/scripts/validate_kag.py`
  - `Tree-of-Sophia/docs/COUNTERPART_POLICY.md`
  - `Tree-of-Sophia/docs/KNOWLEDGE_MODEL.md`

## Evidence
- the `aoa-kag` bridge contract says that when more than one repo contributes to one bridge surface, the registry should preserve the full `source_inputs` list, keep exactly one `primary` input, and mark additional inputs as `supporting`
- the `aoa-kag` example and validator rules reinforce that the primary input remains the top semantic anchor while supporting inputs stay visible without becoming equal owners of the derived surface
- the `Tree-of-Sophia` bridge handoff keeps conceptual origin explicit and routes machine-readable or retrieval-ready projection into `aoa-kag`, which reinforces that source ordering must stay visible before downstream bridge use depends on it
- the useful boundary is input ordering, not note-level provenance handles, direct relations, or graph semantics

## Interpretation
- the reusable object is a bounded priority-ordering rule for multi-source docs surfaces
- the public technique should stay separate from note kinds, direct relation hints, ranking, and graph behavior
