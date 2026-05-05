# Origin Evidence

## Technique
- id: AOA-T-0045
- name: witness-trace-as-reviewable-artifact

## Source project
- name: aoa-memo + aoa-playbooks
- source files:
  - `docs/WITNESS_TRACE_CONTRACT.md`
  - `docs/MEMORY_MODEL.md`
  - `docs/RUNTIME_WRITEBACK_SEAM.md`
  - `playbooks/witness-to-compost-pilot/PLAYBOOK.md`
  - `docs/SEAM_PILOT_REPORT.md`

## Evidence
- the donor memo contract explicitly says `WitnessTrace` is a trace export contract, not a memory object, and that the trace remains the reviewable source artifact for the route
- the donor memo contract defines a run-level `WitnessTrace`, step-level `WitnessStep`, and compact `TraceSummary`, which together preserve goal, bounded status, ordered steps, tool visibility, state deltas, review flags, and human-readable summary output
- the donor memo contract requires redaction-first handling and says the trace should not preserve raw secret-bearing payloads or hidden chain-of-thought dumps
- the donor playbook keeps the witness route review-first by requiring a reviewable witness surface before deeper memo writeback or compost promotion
- the donor playbook and seam report both keep writeback, promotion, eval anchors, and role choreography separate from the witness artifact itself

## Interpretation
- the reusable object is one reviewable trace artifact with summary posture, not the whole witness runtime or pilot route
- the public technique can stay bounded to export and review semantics without importing memo taxonomy, role choreography, deep recall, or compost promotion doctrine
