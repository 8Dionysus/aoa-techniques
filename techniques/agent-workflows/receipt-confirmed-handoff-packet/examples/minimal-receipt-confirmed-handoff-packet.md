# minimal receipt-confirmed handoff packet

Handoff packet:

```markdown
# Handoff Packet
- id: handoff-serializer-fix
- summary: Parser refactor is done; serializer still fails on nested arrays
- next_step: Fix nested-array emission in `src/serializer.ts`
- references:
  - `src/serializer.ts`
  - `tests/serializer.test.ts`
  - commit `abc1234`
```

Receipt record:

```markdown
# Handoff Receipt
- handoff_id: handoff-serializer-fix
- receiver: @review-agent
- state: accepted
- reviewed_at: 2026-03-28T18:10:00Z
- first_next_step: Reproduce the nested-array failure in `tests/serializer.test.ts`
```

Continuation rule:
- do not continue the serializer work until the receipt record exists

Why this example stays bounded:
- the packet exists before receipt
- receipt is not confused with delivery
- the contract does not become a mailbox platform, queue system, or broad approval workflow
