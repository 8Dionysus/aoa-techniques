# Stateless Single-Shot Agent Checklist

- Name one explicit question or one explicit action request for the invocation.
- Keep read-only question flows free of tool access unless the contract is intentionally changed.
- Keep tool-using action flows bounded to one step per invocation.
- Require an explicit confirmation gate before any mutating command or file write runs.
- Treat transient context as invocation input, not as hidden long-lived memory.
- End the invocation after one answer or one confirmed action result.
- Escalate to a broader workflow when the task now needs planning, multiple steps, or stronger verification.
