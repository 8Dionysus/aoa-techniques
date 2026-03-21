# Shell-Composable Agent Invocation Checklist

- The agent run behaves like one shell-visible invocation.
- Inputs and outputs move through explicit stdin, stdout, files, or pipes.
- The invocation ends after one answer or one action result.
- The shell boundary remains clear without relying on hidden session state.
- Confirmation logic is treated as a separate concern unless another bundle explicitly owns it.
- The workflow does not widen into a hidden autonomous loop.
- The command remains usable in a pipe, file handoff, or explicit review step.
