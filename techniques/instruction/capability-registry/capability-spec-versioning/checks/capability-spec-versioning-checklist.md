# Capability Spec Versioning Checklist

- Name one bounded capability rather than a whole orchestration system.
- Record one explicit spec version for the capability contract.
- State expected inputs, outputs, and invariants in the spec.
- Keep implementations and providers subordinate to the spec.
- Record compatibility notes when the capability version changes in a consumer-relevant way.
- Keep persistent registry, plan orchestration, and history-learning behavior out of this technique.
- Make it possible to review a capability change without reading runtime code first.
