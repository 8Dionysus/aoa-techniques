# Origin Evidence

## Technique
- id: AOA-T-0015
- name: contract-test-design

## Source project
- name: abyss-stack
- source files:
  - `abyss-stack/planning-layer/`
  - `abyss-stack/docs/`

## Evidence
- The origin repeatedly needed service and workflow boundaries to be reviewed at the consumer-visible contract surface instead of only through internal implementation checks.
- The same planning-layer work kept forcing one reusable pattern: make the expected inputs, outputs, and failure surface explicit before refactor or feature pressure widened the change.
- In those uses, contract-oriented verification was strongest when downstream assumptions were named directly rather than being hidden inside implicit implementation knowledge.
- Across repeated uses, the stable reusable invariant was boundary-first verification: describe the observable contract, test or check that surface, and report what is guaranteed versus what still remains outside the contract.

## Interpretation
- The origin proves this technique as a reusable evaluation discipline for boundary stability: the contract is valuable because it keeps interface expectations explicit, reviewable, and resistant to internal churn.
