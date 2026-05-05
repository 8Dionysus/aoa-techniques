# Confirmed Single-Step Action

Scenario: a shell operator wants to rename one generated report file.

1. Frame the request as one explicit action: rename `reports/today.json` to `reports/archive/today.json`.
2. Provide only the transient context needed for that rename.
3. Ask for one tool-using step.
4. Show the exact mutating command before it runs.
5. Require explicit confirmation.
6. Run the command once.
7. Return the result and stop.

This stays inside the technique because the flow remains one invocation, one confirmed action, and no hidden multi-step autonomy.
