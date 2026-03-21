# Concrete Pipe-First Agent Invocation

This example keeps the agent invocation composable with ordinary shell tools.

```powershell
git diff -- README.md |
  qa "extract one user-facing change summary and one reviewer watch point" |
  Set-Content review-note.txt
```

Why this fits the technique:

- the agent run is one shell-visible invocation
- the input comes from a pipe
- the result is captured into an explicit file
- the shell flow stays inspectable without depending on hidden long-lived session state
