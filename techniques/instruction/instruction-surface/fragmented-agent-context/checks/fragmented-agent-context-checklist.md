# Fragmented Agent Context Checklist

- Context is authored in smaller fragments rather than one large hand-maintained file.
- Each fragment has bounded local or topical scope.
- Fragment naming or placement makes ownership legible to reviewers.
- Contributors treat the fragments as the editable source of truth.
- Deterministic assembly, CI reporting, and runtime injection stay outside this contract.
- Removing one fragment removes one bounded scope rather than breaking the whole context layer.
- The fragment set stays readable without hidden loader behavior.
