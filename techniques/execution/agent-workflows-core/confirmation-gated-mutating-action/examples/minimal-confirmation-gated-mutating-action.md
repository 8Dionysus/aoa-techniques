# Minimal Confirmation Gated Mutating Action

Use one read or plan step first, then pause for confirmation before mutation.

- read or plan step:
  - inspect the target file or target command
  - state the proposed change in one sentence
- confirmation step:
  - ask for an explicit yes/no before any write runs
- mutating step:
  - perform only the confirmed bounded change
  - stop after the confirmed action completes

If the task now needs multiple writes, diff review, or a longer verification chain, hand it off to a broader workflow technique.
