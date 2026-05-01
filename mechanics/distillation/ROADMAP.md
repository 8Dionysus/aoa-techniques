# Distillation Roadmap

## Next honest passes

1. Compact one candidate ledger at a time only after preserving a pre-prune
   receipt in `legacy/raw/`.
2. Compact the external candidate ledger only after the active source-status
   note and pre-prune receipt remain green in validation.
3. Decide whether the external and cross-layer ledgers need structured
   part-local registries like Agon's candidate registries.
4. Repoint recurrence observation to the part-local cross-layer ledger without
   giving recurrence candidate or promotion authority.
5. Reassess the active narrowing lane only when new public donor evidence
   changes the boundary, handoff packet, continuation permission, or
   stop/return/escalation signals.

## Hold line

Do not flatten all donor material at once. Distillation should keep moving one
part at a time, with provenance and active behavior updated together.
