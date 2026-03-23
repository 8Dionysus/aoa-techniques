# Minimal Skill Vs Command Boundary

Keep reusable capability meaning in a skill file and keep user-facing invocation in a command file.

## Reusable skill

`skills/contract-test.md`

```md
# Contract Test

## Guidelines

- name the boundary first
- state expected inputs and outputs
- prefer contract-first checks over internal detail
```

## Agent-facing reuse

`agents/backend-reviewer.md`

```md
## Skills

- [Contract Test](../skills/contract-test.md) - invoke when reviewing interface changes
```

## User-facing command

`commands/review-contract.md`

```md
---
name: review-contract
argument-hint: " <path>"
user-invocable: true
---

# Review Contract

1. Parse the target path from the user request.
2. Load the `contract-test` skill.
3. Apply that skill to the selected boundary.
4. Return structured findings for the named path.
```

## What The Contract Shows

- the skill defines reusable review meaning
- the command defines user entrypoint, argument shape, and structured workflow
- the same skill can be used by an agent and by a command without rewriting it
