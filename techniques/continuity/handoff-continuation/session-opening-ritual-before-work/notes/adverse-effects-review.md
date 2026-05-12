# Adverse Effects Review

## Technique

- id: AOA-T-0060
- name: session-opening-ritual-before-work

## Review focus

- current role: canonical default for starting a resumed or handed-off session with one visible read-and-verify step before the first mutation
- current watch seam: preserve the opening ritual without turning it into handoff authoring, detailed git-claim verification, startup test doctrine, task routing, or a full long-running-agent harness

## Failure modes

- the session reads a handoff or progress file but never checks current repo or artifact state
- edits begin before the expected baseline and actual visible state are compared
- mismatch notes are omitted because the opening ritual is treated as a symbolic checklist
- the baseline check is too generic to catch stale branch, dirty tree, missing file, failed smoke, or wrong target state

## Negative effects

- small uninterrupted tasks can gain ceremony when no real context boundary exists
- agents can overtrust the opening ritual and skip detailed claim verification that a specific handoff still needs
- startup can become slow if every project folds full test suites, task selection, and harness boot into the ritual
- a broad startup checklist can crowd out the one thing this technique owns: read current context and verify baseline before mutation

## Misuse patterns

- treating "read the handoff" as sufficient without checking live state
- importing packet-writing, mailbox receipt, or git-claim verdicts into the opening ritual
- making a mandatory startup test suite part of the technique instead of a project-local baseline choice
- turning the ritual into task-priority, budget, evaluator, or orchestration doctrine
- ignoring mismatches and continuing from inherited narration anyway

## Detection signals

- the first edit happens before any visible context read or baseline check
- the incoming session cannot name which current-state surface was inspected
- a mismatch is found later that should have been visible at session start
- opening notes start listing full mission rules, task policies, evaluator loops, or test matrices instead of the verified baseline

## Mitigations

- require one current context read and one visible baseline check before mutation
- record mismatches in the starting plan and let them redirect or stop the first move
- keep detailed handoff packet creation in AOA-T-0057 and concrete claim verification in AOA-T-0059
- treat project smoke/build/test commands as optional baseline checks, not as universal startup doctrine
- keep the ritual short enough that a fresh session can perform it cold without hiding the actual first task

## Recommendation

- move `AOA-T-0060` to `canonical` and use this note as the watch surface for symbolic openings, unchecked inherited context, startup-suite creep, task-routing drift, and long-running-harness overreach
