# Adverse Effects Review

## Technique

- id: AOA-T-0055
- name: requirements-design-tasks-ladder

## Review focus

- current role: canonical default for keeping requirement, design, and task layers distinct before implementation starts
- current watch seam: keep the bundle centered on the bounded planning ladder rather than widening into full SDD doctrine, command suites, template ecosystems, approval workflows, task graphs, memory, or implementation execution

## Failure modes

- requirements stay vague, so design and tasks inherit ambiguity
- design restates requirements instead of answering them with a solution shape
- tasks are invented independently instead of being derived from visible design choices
- the three layers become decorative headings over one undifferentiated planning blob
- methodology, command, approval, or template concerns become the real object of the bundle

## Negative effects

- simple changes can be slowed by unnecessary planning ceremony
- teams can mistake the existence of three documents for actual traceability
- over-detailed design can delay the first useful implementation slice
- the ladder can pull in governance, staffing, research, memory, or execution policy if its stop line is not guarded

## Misuse patterns

- treating the technique as a mandate to adopt one spec-driven development stack
- using `tasks.md` as a substitute for design review
- hiding design decisions inside task lists to skip an explicit design layer
- folding approval flow, auto-execution, task dependency graphs, or full project-management behavior into the ladder

## Detection signals

- tasks cannot name the design choice that produced them
- design sections do not answer a visible requirement
- reviewers discuss template compliance before layer traceability
- the planning surface grows faster than the bounded work it is supposed to prepare
- implementation begins while requirements, design, and tasks still contradict each other

## Mitigations

- keep each layer short, explicit, and reviewable
- require a visible transition from requirement to design and from design to tasks
- trim command, template, approval, and methodology language that does not serve the layer transition
- route blocker graphs, ready-frontier derivation, implementation execution, approvals, and memory to neighboring techniques or owner repositories

## Recommendation

- move `AOA-T-0055` to `canonical` and use this note as the watch surface for planning-theater drift, methodology-stack drift, task-list-without-design drift, and execution-policy drift
