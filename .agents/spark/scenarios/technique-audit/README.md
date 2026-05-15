# Spark Scenario: technique-audit

Use `technique-audit` for read-only checks of boundedness, duplicate meaning,
stale paths, public hygiene, owner routing, and missing validation.

## Scope

Read one technique bundle, shelf, route surface, generated reader seam, or
small file family. Editing is out of scope unless the user explicitly asks for
audit plus fix.

## Done Signal

Findings are scoped, evidenced, and routed to the technique bundle, docs
contract, mechanic, generated builder, validator, or sibling owner.

## Stop-line

Do not rewrite the audited surface during audit-only work.

## Handoff Route

Write a handoff when findings require architecture, owner-local decisions,
large rewrites, canon promotion, or cross-repo synthesis.

## Validation

Use the smallest validator tied to the audited surface. If no validator exists,
report a manual consistency pass.
