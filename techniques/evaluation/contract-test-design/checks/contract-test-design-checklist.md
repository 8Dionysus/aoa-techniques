# Contract Test Design Checklist

Use this checklist to verify that a change really validates a boundary contract rather than only exercising hidden internals.

- The boundary and its consumers were named explicitly.
- The contract described observable inputs, outputs, or failure behavior.
- Validation targeted the real boundary surface instead of an internal surrogate.
- Downstream assumptions were stated where they materially affected the contract.
- The change report stated what the contract now guarantees.
- Remaining weak edges or out-of-contract behavior were named explicitly.
