# Deterministic Context Composition Checklist

Use this checklist to validate whether a repository really follows `deterministic-context-composition`.

- Source fragments are the canonical editable inputs.
- The generated context artifact is explicitly treated as derived output.
- Composition order is deterministic and documented.
- Explicit priority or equivalent ordering rules surface earlier content first.
- Output sections remain traceable to their source fragments.
- Changing or removing a fragment updates the generated artifact predictably.
- Contributors can tell that the generated file should be regenerated, not hand-edited.
