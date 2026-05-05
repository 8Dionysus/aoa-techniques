# Origin Evidence

## Technique
- id: AOA-T-0016
- name: bounded-context-map

## Source project
- name: atm10-agent
- source files:
  - `atm10-agent/planning-layer/`
  - `atm10-agent/docs/`

## Evidence
- The origin repeatedly needed a compact way to keep agent and human work semantically scoped when neighboring subsystems or concepts started to blur together.
- The same planning-layer work reused one stable pattern: name the bounded contexts, clarify what belongs inside each one, and make the handoff surfaces visible before larger changes expanded the wrong area.
- In those uses, the value came less from formal architecture diagrams and more from reducing vocabulary drift so reviews and implementation could stay inside the right responsibility boundary.
- Across repeated uses, the reusable invariant stayed stable: context naming should narrow ambiguity, expose interfaces, and help future changes stay better scoped.

## Interpretation
- The origin proves this technique as a reusable documentation and scoping pattern: a bounded context map is useful here because it reduces semantic drift and makes subsystem boundaries reviewable before code changes widen unnecessarily.
