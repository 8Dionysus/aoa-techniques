# Concrete Confirmed Mutating Action

Scenario: an agent has identified one file that needs a small text update.

1. Read the file and describe the exact line-level change in plain language.
2. Ask for a visible confirmation before changing the file.
3. After confirmation, apply only that one bounded edit.
4. Report the result and stop instead of chaining more edits into the same run.

This stays inside the technique because the confirmation seam is explicit and the mutating action remains bounded to one named change.
