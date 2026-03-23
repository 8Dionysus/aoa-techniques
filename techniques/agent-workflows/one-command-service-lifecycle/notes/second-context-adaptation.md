# Second Context Adaptation

## Technique

- id: AOA-T-0038
- name: one-command-service-lifecycle

## Target project

- name: aoa-techniques
- environment: public library repository with reusable technique bundles, generated catalog surfaces, and documentation-first validation
- runtime: documentation-first repository that records the lifecycle contract rather than shipping the donor startup manager itself

## What changed

- paths: the donor uses `npm start`, wrapper scripts, and companion stop helpers; this adaptation presents a generic one-entrypoint local lifecycle contract without depending on those exact commands
- services: donor-specific memory, logging, OAuth, and desktop-integration breadth is removed from the reusable contract
- dependencies: the adaptation depends on visible lifecycle ownership rather than on one process-manager implementation or one platform setup path
- operating assumptions: contributors should read the technique as a local runtime-control pattern for bounded stacks, not as a generic launcher or bootstrap program

## What stayed invariant

- contract: one explicit operator-facing entrypoint owns local stack startup
- validation logic: the entrypoint should fail early on missing prerequisites, print visible runtime status, and provide a real stop path
- safety rules: shutdown remains part of the same contract and should not collapse into silent background leftovers

## Risks introduced by adaptation

- the pattern can become vague if a project says "one command" but still relies on hidden manual prep
- some repositories may widen lifecycle wording into general platform doctrine instead of one bounded local stack contract

## Evidence

- the donor `README.md`, `QUICKSTART.md`, and `AUTOMATIC_STARTUP.md` describe a single startup surface that owns the dependent local services and cleanup path
- `package.json`, `start-openmemory.js`, and `stop-openmemory.ps1` show the same contract in executable form: one visible lifecycle surface starts the bounded stack and one explicit stop path shuts it down

## Result

- works as a documentation-first second context and preserves the bounded lifecycle core without carrying over donor-specific memory or platform breadth
