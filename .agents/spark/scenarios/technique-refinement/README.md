# Spark Scenario: technique-refinement

Use `technique-refinement` for one small source-backed patch to an existing
technique bundle.

## Scope

One technique bundle and its directly relevant notes, examples, or generated
freshness path.

## Done Signal

One existing technique is more atomic, portable, sanitized, and reviewable, and
the relevant validation was named and run.

## Stop-line

Stop when the patch asks for a second owner, broader design, canon promotion,
skill workflow, playbook sequence, eval proof, runtime behavior, or sibling
owner decision.

## Handoff Route

Write a handoff when source truth is unclear, the candidate is too broad, or a
mechanic or sibling repository must accept the next move.

## Validation

Run the narrowest validation named by the target bundle or owner route. For a
text-only patch with no generated surface, `git diff --check` plus an honest
manual contract pass is enough. Use `python scripts/validate_repo.py` only when
repo law, touched generated surfaces, or the user asks for that broader proof.
