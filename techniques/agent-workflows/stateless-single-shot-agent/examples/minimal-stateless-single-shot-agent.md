# Minimal Stateless Single-Shot Agent

Use one invocation for one narrow shell-side need.

- question mode:
  - ask one explicit question
  - pass only the transient context needed for that answer
  - return one answer without tool use
- action mode:
  - state one explicit action request
  - allow one tool step only
  - require confirmation before mutation
  - stop after the result

If the task now needs several dependent actions or hidden continuity, leave this fast path and switch to a broader workflow.
