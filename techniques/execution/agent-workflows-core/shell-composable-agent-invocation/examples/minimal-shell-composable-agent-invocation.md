# Minimal Shell-Composable Agent Invocation

Use the agent as one more command in a shell pipeline.

```powershell
Get-Content TODO.md | qa "summarize the next three safe cleanup steps"
```

The important part is not the exact wrapper name.
The important part is that:

- the input arrives through stdin
- the output returns through stdout
- the run ends after one result
- the next shell step can consume the result directly
