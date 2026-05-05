# Concrete Shell Composable Agent Invocation

Scenario: normalize a short task brief into a reusable text artifact.

1. Write the brief to `stdin` or save it in `request.txt`.
2. Run one shell-composable command that reads the brief and emits normalized output.
3. Pipe the result into `stdout` or `result.txt`.
4. Stop after the single invocation and use the output as the handoff artifact.

This stays inside the technique because the interaction remains one bounded shell step with explicit stream or file transport.
